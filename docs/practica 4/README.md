
# Práctica 4: Exploración de comunidades, documentación y recursos de colaboración

## 1. Propósito de la práctica

El propósito de esta práctica es investigar y analizar diferentes recursos de documentación técnica y comunidades de colaboración relacionados con Python, GNS3 y la automatización de redes. También se busca aprender a identificar fuentes confiables y organizar la información para utilizarla en futuras actividades.

## 2. Relación con el proyecto integrador

Esta práctica se relaciona con el proyecto `automatizacion-redes`, porque permite conocer recursos que ayudarán a resolver errores de programación, comprender la configuración de la infraestructura simulada y preparar futuros scripts para consultar información de dispositivos de red.

## 3. Recursos consultados

- **Documentación de Python:** https://docs.python.org/3/  
  Permite consultar las instrucciones, funciones, tipos de datos y bibliotecas del lenguaje Python.

- **Documentación de GNS3:** https://docs.gns3.com/  
  Proporciona guías para instalar, configurar y utilizar GNS3, así como información para resolver problemas relacionados con las topologías de red.

- **Repositorio de Netmiko:** https://github.com/ktbyers/netmiko  
  Contiene el código fuente, ejemplos, instrucciones de instalación y documentación de una biblioteca de Python para automatizar conexiones de administración con dispositivos de red compatibles.

## 4. Evaluación de confiabilidad de los recursos

| Criterio | Recurso 1: Python | Recurso 2: GNS3 | Recurso 3: Netmiko |
|---|---|---|---|
| ¿Quién publica o mantiene el recurso? | El equipo responsable de Python y sus colaboradores. | El proyecto GNS3 y sus responsables de documentación. | Kirk Byers y los colaboradores del proyecto Netmiko. |
| ¿La información corresponde al tema investigado? | Sí, explica el lenguaje Python y sus bibliotecas. | Sí, aborda la simulación, configuración y uso de GNS3. | Sí, trata sobre conexiones y automatización de dispositivos de red mediante Python. |
| ¿Incluye ejemplos o instrucciones verificables? | Sí, incluye tutoriales, ejemplos y referencias del lenguaje. | Sí, ofrece guías e instrucciones de configuración. | Sí, contiene ejemplos, instrucciones de instalación y código fuente. |
| ¿Se identifica la versión o fecha de actualización cuando corresponde? | Sí, permite consultar la documentación por versiones de Python. | Se debe revisar la información de la guía y las versiones de GNS3 aplicables. | Sí, el repositorio muestra versiones, etiquetas de lanzamiento e historial de cambios. |
| ¿Es posible comprobar la información con otra fuente? | Sí, mediante ejemplos ejecutados en Python y otras referencias técnicas confiables. | Sí, mediante pruebas en GNS3 y otras guías técnicas. | Sí, mediante pruebas controladas, documentación y comprobación de las plataformas compatibles. |
| ¿Qué utilidad tiene para el proyecto integrador? | Ayuda a mejorar el código y resolver dudas de programación. | Ayuda a comprender y solucionar problemas de la topología simulada. | Permite investigar futuras tareas de automatización de dispositivos compatibles. |

### Análisis de los resultados

Los tres recursos son pertinentes para el proyecto, pero cumplen funciones diferentes. La documentación de Python es apropiada para estudiar el lenguaje; GNS3 es útil para comprender y configurar el entorno de simulación; y Netmiko permite investigar técnicas de conexión y administración de dispositivos de red. Su confiabilidad se puede evaluar mediante la identificación de sus responsables, la revisión de versiones, los ejemplos disponibles y las pruebas realizadas.

## 5. Estrategia para investigar y resolver un problema técnico

### Problema identificado

El programa `dispositivos.py`, desarrollado en la Práctica 3, muestra correctamente la información de los dispositivos R1 y R2, pero no identifica un dispositivo cuando se busca por su nombre.

| Elemento | Respuesta del equipo |
|---|---|
| Problema identificado | El programa no encuentra el dispositivo solicitado mediante su nombre. |
| Palabras clave para realizar la búsqueda | Python, buscar dispositivo por nombre, diccionarios, ciclos, condiciones y comparación de cadenas. |
| Documentación o comunidad que consultarían primero | Primero consultaría la documentación oficial de Python sobre diccionarios y estructuras de control. Si la duda continúa, revisaría Stack Overflow en español. |
| Información que revisarían en el código | Las variables, los nombres registrados, la estructura de los datos, las condiciones de búsqueda y las posibles diferencias entre mayúsculas y minúsculas. |
| Tipo de ejemplo o solución que buscarían | Un ejemplo de búsqueda de una clave en un diccionario o de comparación de nombres dentro de una lista de dispositivos. |
| Cómo comprobarían que la solución funciona | Probarían con R1, R2, un nombre inexistente y diferentes formas de escribir el nombre, verificando que cada resultado sea correcto. |
| Cómo documentarían la solución encontrada | Registrarían el problema, la causa identificada, el cambio realizado, las pruebas y el resultado en la documentación de la práctica dentro de GitHub. |

### Preguntas de análisis

**¿Cuál de los recursos consideras más útil para resolver dudas de Python? ¿Por qué?**

Considero que la documentación oficial de Python es el recurso más útil para resolver dudas sobre el lenguaje, porque contiene explicaciones, ejemplos y referencias que permiten comprender el funcionamiento de sus instrucciones. También permite consultar la documentación correspondiente a diferentes versiones y comprobar si el código utiliza correctamente las funciones y estructuras del lenguaje.

**¿Cuál consultarías para resolver un problema relacionado con GNS3?**

Consultaría primero la documentación oficial de GNS3, porque contiene guías para configurar el programa, construir topologías y solucionar problemas de funcionamiento. Después, si fuera necesario, buscaría experiencias y soluciones de otros usuarios en las comunidades de colaboración.

**¿Por qué no conviene copiar directamente una solución sin comprobar que funciona en el entorno de trabajo?**

No conviene copiar una solución sin comprobarla porque puede depender de otra versión del programa, utilizar bibliotecas diferentes o estar diseñada para dispositivos que no tenemos. Además, el código podría contener errores o no resolver exactamente el problema identificado. Por eso es necesario comprender la solución, adaptarla a nuestro entorno y realizar pruebas antes de incorporarla al proyecto.

## 6. Aprendizajes obtenidos

Durante esta práctica aprendí que existen diferentes recursos para investigar y resolver problemas relacionados con la programación y las redes. La documentación oficial permite consultar información técnica organizada, mientras que las comunidades facilitan el intercambio de experiencias y soluciones. También comprendí la importancia de revisar la compatibilidad de las herramientas, comprobar los ejemplos y registrar los hallazgos en GitHub para facilitar el trabajo colaborativo.

## 7. Conclusión individual


Estrada Rios Jovany de Jesus

Esta práctica me permitió comprender la importancia de consultar fuentes confiables cuando se desarrolla un programa o se configura una red. Aprendí que la documentación oficial proporciona información estructurada, mientras que las comunidades permiten conocer experiencias y soluciones de otros usuarios. También identifiqué que es necesario revisar las versiones, los requisitos y la compatibilidad de las herramientas antes de utilizarlas. En el proyecto de automatización de redes, estos recursos me ayudarán a resolver dudas sobre Python, investigar problemas de GNS3 y conocer bibliotecas como Netmiko. Además, comprendí que no basta con encontrar una solución, sino que debemos probarla y verificar que funcione correctamente. Finalmente, documentar los resultados en GitHub permitirá mantener organizada la información y reutilizar los conocimientos en las siguientes prácticas.


Gonzáles Cavazos Sebastián

Durante esta práctica aprendí la importancia de consultar documentación oficial y utilizar comunidades tecnológicas para resolver dudas relacionadas con la programación y la automatización de redes. Comprendí que investigar en fuentes confiables permite obtener información más precisa y actualizada, lo cual ayuda a evitar errores durante el desarrollo de un proyecto. También conocí herramientas como Python, GNS3 y Netmiko, que pueden ser útiles para crear programas, diseñar topologías de red y automatizar tareas en dispositivos. Además, entendí que GitHub facilita la organización y colaboración en proyectos, mientras que comunidades como Stack Overflow permiten consultar problemas similares y aprender de las experiencias de otros desarrolladores. Otro aspecto importante fue reconocer que no debemos copiar soluciones sin comprenderlas, sino analizarlas y probarlas antes de aplicarlas. Estos conocimientos me ayudarán a investigar de manera más ordenada, documentar los procedimientos realizados y encontrar soluciones cuando surjan errores. Finalmente, considero que saber buscar, evaluar y utilizar recursos técnicos es una habilidad fundamental para continuar desarrollando el proyecto de automatización de redes y mejorar mis conocimientos de programación.
