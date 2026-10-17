# Práctica 3. Primer programa de Python para representar información de dispositivos

## 1. Propósito

El propósito de esta práctica fue desarrollar un programa en Python para representar, organizar y mostrar información de los dispositivos utilizados en la infraestructura de red simulada en GNS3. Se utilizaron diferentes estructuras del lenguaje para facilitar la consulta de los datos y preparar el proyecto para futuras actividades de automatización de redes.

## 2. Conceptos utilizados

- **Variables:** almacenan datos como nombres, direcciones IP y estados.
- **Tipos de datos:** permiten representar cadenas de texto y otros valores según la información que se necesite manejar.
- **print():** muestra información en la terminal.
- **Diccionarios:** agrupan los datos de cada dispositivo mediante claves y valores.
- **Listas:** almacenan varios dispositivos en una misma estructura.
- **Ciclo for:** recorre los dispositivos para procesar su información.
- **Condicional if:** permite tomar decisiones según el estado del equipo.
- **Funciones:** agrupan instrucciones reutilizables para mostrar o buscar dispositivos.

## 3. Dispositivos representados

| Dispositivo | Tipo | Dirección IP | Estado | Función |
|---|---|---|---|---|
| R1 | Router | 10.1.1.1 | Activo | Enrutamiento |
| R2 | Router | 10.1.1.2 | Activo | Enrutamiento |
| S1 | Switch | 10.1.1.3 | Activo | Conectividad local |

## 4. Evidencias

Se integrarán las capturas de pantalla de la estructura del repositorio, el código fuente, la ejecución del programa, el uso de listas y diccionarios, las funciones, las condiciones, la búsqueda de dispositivos y las pruebas realizadas.
**Evidencia 2. Código fuente**

En esta captura se observa el código desarrollado en Python para almacenar información de los dispositivos de red mediante variables y mostrarla en pantalla utilizando la función `print()`.

**Evidencia 3. Ejecución del programa**

Se muestra la ejecución del programa en la terminal de Visual Studio Code, donde se visualizan los datos del dispositivo representado y se comprueba que las instrucciones se ejecutan correctamente.

**Evidencia 4. Representación de la topología**

En esta evidencia se representa la información de los dispositivos utilizados en la Práctica 2, incluyendo sus nombres, tipos, direcciones IP, interfaces y estados.

**Evidencia 5. Lista y diccionarios**

Se observa cómo se organizó la información de varios dispositivos mediante una lista que contiene diccionarios, permitiendo almacenar los datos de cada equipo de manera estructurada.

**Evidencia 6. Recorrido de dispositivos**

La captura muestra el uso del ciclo `for` para recorrer la lista e imprimir la información de cada dispositivo de la infraestructura de red.

**Evidencia 7. Función y datos adicionales**

Se muestra la función `mostrar_dispositivo()`, utilizada para presentar la información de cada equipo, incluyendo fabricante, protocolo, ubicación y estado.

**Evidencia 8. Búsqueda de dispositivos**

En esta evidencia se demuestra el funcionamiento de la búsqueda por nombre. Se ingresa el identificador de un dispositivo y el programa muestra su información cuando lo encuentra.

**Evidencia 9. Verificación del estado**

Se modificó temporalmente el estado de un dispositivo para comprobar que la condición `if` identifica los equipos activos y aquellos que requieren atención.

**Evidencia 10. Modificación de información**

Se cambió temporalmente la dirección IP de un dispositivo para comprobar que el programa muestra el nuevo valor. Posteriormente, se restauró la información original.

**Evidencia 11. Documentación**

Se presenta el archivo README de la Práctica 3, donde se documentan el propósito, los conceptos utilizados, los dispositivos representados, las pruebas y las conclusiones.

**Evidencia 12. Repositorio actualizado**

Se muestra el repositorio de GitHub con los archivos de código, documentación y evidencias correspondientes al desarrollo de la práctica.

## 5. Problemas y soluciones

| Problema | Causa | Solución |
|---|---|---|
| El programa no se ejecutaba | Posible error de sintaxis o comando incorrecto | Revisar el código y ejecutar desde la carpeta correcta |




## 6. Conclusión

Durante esta práctica aprendí a utilizar variables, diccionarios, listas, ciclos, condiciones y funciones en Python para representar información de dispositivos de red. Organicé los datos de varios equipos y desarrollé una función para mostrar sus características de manera ordenada. También comprendí cómo verificar el estado de los dispositivos y cómo buscar un equipo por su nombre. Una dificultad que puede presentarse es mantener las direcciones IP y los nombres correctamente registrados, por lo que es importante verificar los datos de la topología. Este programa constituye una base para desarrollar herramientas de automatización de redes, ya que posteriormente podría conectarse con dispositivos reales o simulados para obtener información y ejecutar tareas de administración.
