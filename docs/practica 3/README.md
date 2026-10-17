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

*Nota: las direcciones IP son ejemplos y deben sustituirse si son diferentes a las de la topología desarrollada en la Práctica 2.*

## 4. Evidencias

Se integrarán las capturas de pantalla de la estructura del repositorio, el código fuente, la ejecución del programa, el uso de listas y diccionarios, las funciones, las condiciones, la búsqueda de dispositivos y las pruebas realizadas.

## 5. Problemas y soluciones

| Problema | Causa | Solución |
|---|---|---|
| El programa no se ejecutaba | Posible error de sintaxis o comando incorrecto | Revisar el código y ejecutar desde la carpeta correcta |




## 6. Conclusión

Durante esta práctica aprendí a utilizar variables, diccionarios, listas, ciclos, condiciones y funciones en Python para representar información de dispositivos de red. Organicé los datos de varios equipos y desarrollé una función para mostrar sus características de manera ordenada. También comprendí cómo verificar el estado de los dispositivos y cómo buscar un equipo por su nombre. Una dificultad que puede presentarse es mantener las direcciones IP y los nombres correctamente registrados, por lo que es importante verificar los datos de la topología. Este programa constituye una base para desarrollar herramientas de automatización de redes, ya que posteriormente podría conectarse con dispositivos reales o simulados para obtener información y ejecutar tareas de administración.
