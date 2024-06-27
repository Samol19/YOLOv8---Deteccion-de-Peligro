import os
import cv2
import numpy as np
from ultralytics import YOLO

# Cargamos los modelos
pose_model = YOLO('yolov8n-pose.pt')
object_model = YOLO('yolov8m.pt')


# Lista de nombres de los puntos clave (basado en el conjunto de datos COCO)
keypoint_names = [
    "Nose", "Left Eye", "Right Eye", "Left Ear", "Right Ear",
    "Left Shoulder", "Right Shoulder", "Left Elbow", "Right Elbow",
    "Left Wrist", "Right Wrist", "Left Hip", "Right Hip",
    "Left Knee", "Right Knee", "Left Ankle", "Right Ankle"
]

# Iniciar la captura de video desde la webcam
cap = cv2.VideoCapture(0)

LeftArmRaised = False
RightArmRaised = False
knife_box = None
cont = 0

def save_image(frame, knife_box = None):

    # Verificar si la carpeta "frames" existe
    if not os.path.exists('Frames'):
        os.makedirs('Frames')

    # Aplicamos el filtro gaussiano 
    frame_filter = cv2.GaussianBlur(frame, (15, 15), 5)

    # Aplicamos el filtro de color
    if knife_box is not None:
        x1, y1, x2, y2 = knife_box
        knife_region = frame[y1:y2, x1:x2]
        hsv_image = cv2.cvtColor(knife_region, cv2.COLOR_BGR2HSV)

        # Definir los rangos de color para segmentar
        lower_bound = np.array([0, 0, 100])
        upper_bound = np.array([180, 50, 200])

        # Crear una máscara binaria donde los colores dentro del rango son blancos
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

        # Aplicar la máscara a la imagen original
        segmented_image = cv2.bitwise_and(knife_region, knife_region, mask=mask)

        # La guardamos en la carpeta "frames"
        cv2.imwrite('Frames/frame_color_filter.jpg', segmented_image)

    # Guardamos el frame ORIGINAL en la carpeta "frames"
    cv2.imwrite('Frames/frame_original.jpg', frame)

    # Guardamos el frame con el FILTRO GAUSSIANO en la carpeta "frames"
    cv2.imwrite('Frames/frame_gaussian_filter.jpg', frame_filter)


    print("Frame guardado")

# Mientras la cámara esté abierta capturamos frame por frame
while cap.isOpened():

    # Leemos un frame de la cámara
    ret, frame = cap.read()  
    if not ret:
        break

    # Hacer una copia del frame para mostrar los resultados
    frame_original = frame.copy()

    # Obtener los resultados de la detección de poses
    pose_results = pose_model(frame)

    # Obtener los resultados de la detección de objetos
    object_results = object_model(frame)

    # Acceder a las coordenadas de los cuadros delimitadores (boxes) de objetos
    object_boxes = object_results[0].boxes
    if object_boxes is not None:

        for box in object_boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()  # Extraer las coordenadas xyxy
            conf = box.conf[0].item()  # Obtener la confianza de la detección
            cls = box.cls[0].item()  # Obtener la clase del objeto detectado

            if conf > 0.5:
                # Obtener el nombre de la clase
                label = object_model.names[int(cls)] 

                # Dibujar el cuadro delimitador en la imagen
                color = (0, 255, 0) if cls != 43 else (0, 0, 255)  
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

                if cls == 43:  # 43 es el ID de clase para "knife" en COCO
                    cv2.putText(frame, 'DANGER', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                    knife_box = (int(x1), int(y1), int(x2), int(y2))
                    print("PELIGRO , CUCHILLO DETECTADO")
                    cont += 1
                else:
                    knife_box = None

    # Acceder a los puntos clave de las poses (keypoints)
    keypoints = pose_results[0].keypoints
    if keypoints is not None:
        for keypoint in keypoints:
            points = keypoint.xy[0].tolist()  # Extraer los puntos clave
            for i, point in enumerate(points):
                x, y = point

                if x != 0 or y != 0:  # Ignorar puntos clave en (0, 0)
                    cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)  # Dibujar los puntos clave
                    # cv2.putText(frame, keypoint_names[i], (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)  # Etiquetar puntos clave con nombres en amarillo

            # Detectar el movimiento de la mano izquierda
            if len(points) > 9 and points[9][1] != 0:
                if points[9][1] < points[0][1]:
                    #cv2.putText(frame, 'Left hand raised', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                    LeftArmRaised = True
                else :
                    LeftArmRaised = False

            # Detectar el movimiento de la mano derecha
            if len(points) > 10 and points[10][1] != 0:
                if points[10][1] < points[0][1]:
                    #cv2.putText(frame, 'Right hand raised', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                    RightArmRaised = True
                else :
                    RightArmRaised = False

            if LeftArmRaised and RightArmRaised:
                cv2.putText(frame, 'DANGER', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                print("PELIGRO DETECTADO")
                cont += 1

    # Mostrar la imagen con los resultados
    cv2.imshow('Pose and Object Detection', frame)

    # Guardar el frame en la carpeta "frames" si se detecta un cuchillo
    if cont == 1:
        save_image(frame_original, knife_box)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar la ventana
cap.release()
cv2.destroyAllWindows()