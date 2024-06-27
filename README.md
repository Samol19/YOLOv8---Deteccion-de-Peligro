Universidad Peruana de Ciencias Aplicadas

INFORME TRABAJO FINAL
CURSO PROCESAMIENTO DE IMÁGENES
Carrera de Ciencias de la Computación 
Sección: CC61

Alumnos:
Código         Nombres y Apellidos
----------------------------------------
u202122837     Fernando Samuel Paredes Espinoza
u202114233     Anthony Hans Tarrillo Ayllón
u202121973     Andres Joshua Rodriguez Guerrero

Lima, Junio de 2024

Introducción

Problemática
En el contexto actual, la seguridad y el monitoreo en entornos específicos como espacios públicos, hogares o centros educativos han cobrado una relevancia significativa. La necesidad de implementar sistemas de vigilancia efectivos y proactivos se ha intensificado con el fin de prevenir incidentes y proteger a las personas. Dentro de este marco, el presente proyecto se centra en desarrollar una aplicación que utilice técnicas avanzadas de procesamiento de imágenes en tiempo real para mejorar la detección y alerta ante situaciones de riesgo.

Solución
El objetivo principal de esta aplicación es aplicar los conocimientos adquiridos en el curso de Procesamiento de Imágenes, específicamente utilizando técnicas como YOLO (You Only Look Once) v8 para la detección precisa de objetos y acciones relevantes en videos en tiempo real. Además de la detección de objetos mediante YOLO, se aplicarán filtrado espacial con filtro Gaussiano y la segmentación de color que permitan complementar y enriquecer la capacidad de vigilancia y detección del sistema.

El principio fundamental de YOLO v8 radica en su capacidad para dividir la imagen en una cuadrícula y predecir cuadros delimitadores (bounding boxes) y probabilidades de clase para cada cuadro simultáneamente. Esto se realiza mediante una única red neuronal convolucional, lo que permite una detección rápida y precisa de objetos en tiempo real.

En resumen, YOLO v8 representa una herramienta poderosa para la detección de objetos en tiempo real, integrando capacidades avanzadas de aprendizaje profundo para mejorar la seguridad y el monitoreo mediante el procesamiento eficiente y preciso de imágenes y videos.

Motivación
La motivación detrás de este proyecto radica en la necesidad de contar con herramientas tecnológicas que puedan asistir en la supervisión continua y efectiva de entornos críticos, como áreas restringidas o espacios públicos donde se requiera un monitoreo constante. La aplicación propuesta busca no solo detectar la presencia de objetos específicos, como armas o intrusos, sino también alertar de manera inmediata al personal de seguridad o a los responsables del monitoreo en caso de identificar una situación potencialmente peligrosa.

Para respaldar la relevancia de este proyecto, se han consultado fuentes que destacan la efectividad de sistemas de vigilancia inteligente basados en procesamiento de imágenes para mejorar la seguridad y la prevención de incidentes. La implementación de este tipo de tecnologías no solo puede reducir los tiempos de respuesta ante emergencias, sino también optimizar los recursos humanos destinados a la seguridad, mejorando así la eficiencia y la efectividad de los sistemas de monitoreo.

En resumen, este trabajo final se enfocará en diseñar, desarrollar e implementar una solución que integre técnicas avanzadas de procesamiento de imágenes para la detección y alerta temprana de situaciones de riesgo, contribuyendo así a fortalecer la seguridad en entornos críticos mediante el uso de tecnologías innovadoras y efectivas.

Objetivos

Objetivo General:
Desarrollar una aplicación de procesamiento de imágenes en tiempo real que utilice técnicas avanzadas para la detección y alerta de objetos y acciones específicas, con el fin de mejorar la seguridad y el monitoreo en entornos críticos.

Objetivos Específicos:
1. Implementar la configuración de la cámara web y la captura de video en tiempo real dentro del entorno de desarrollo elegido.
2. Integrar el modelo YOLO v8 para la detección precisa de objetos como armas y personas en áreas restringidas en los frames del video, asegurando una implementación robusta y eficiente.
3. Investigar, seleccionar y aplicar técnicas de procesamiento de imágenes como el Filtrado Espacial con Filtro Gaussiano para suavizar las imágenes y la Segmentación de Color, con el objetivo de mejorar la precisión y la capacidad de alerta del sistema junto con YOLO v8.
4. Desarrollar un sistema de alertas que notifique de manera inmediata al usuario cuando se detecte un objeto o acción de interés en el video, garantizando tiempos de respuesta rápidos y efectivos.
5. Evaluar la precisión y eficiencia del sistema implementado mediante pruebas exhaustivas con diferentes escenarios y condiciones de iluminación, validando la efectividad del conjunto de técnicas empleadas para la detección y alerta en tiempo real.

Conclusión

En este proyecto, hemos desarrollado una aplicación avanzada de procesamiento de imágenes en tiempo real que utiliza técnicas innovadoras para mejorar la detección y alerta ante situaciones de riesgo en entornos críticos. A través de la integración de modelos como YOLOv8 para la detección precisa de objetos y poses, junto con técnicas de filtrado espacial y segmentación de color, hemos logrado crear un sistema robusto y efectivo.

La implementación de YOLOv8 ha demostrado ser crucial, permitiendo la detección rápida y precisa de múltiples clases de objetos en tiempo real, lo cual es fundamental para la seguridad y el monitoreo proactivo. Además, el uso de filtros como el gaussiano y la segmentación de color ha mejorado significativamente la capacidad de alerta del sistema, proporcionando imágenes más claras y precisas cuando se identifica un objeto de interés, como un cuchillo.

Nuestra aplicación no solo cumple con el objetivo de detectar objetos y poses relevantes, sino que también incorpora un sistema de alertas que notifica en tiempo real cualquier situación potencialmente peligrosa. Esto es crucial para optimizar la respuesta ante emergencias y mejorar la eficiencia de los sistemas de seguridad existentes.

En resumen, este proyecto ha demostrado cómo la combinación de tecnologías avanzadas de procesamiento de imágenes puede fortalecer la seguridad en entornos críticos, proporcionando herramientas efectivas para la prevención y respuesta ante incidentes, y contribuyendo así a un entorno más seguro y protegido.

Bibliografía

Link del repositorio: https://github.com/Samol19/YOLOv8---Deteccion-de-Peligro
Ultralytics. (n.d.). YOLOv8. Recuperado el 24 de junio de 2024, de https://www.ultralytics.com/es/yolo
Ultralytics. (n.d.). YOLOv8. GitHub. Recuperado el 24 de junio de 2024, de https://github.com/ultralytics/ultralytics
OpenSistemas. (s.f.). YOLOv8 transforma la visión artificial. Recuperado el 26 de junio de 2024, de https://opensistemas.com/yolov8-transforma-la-vision-artificial/
