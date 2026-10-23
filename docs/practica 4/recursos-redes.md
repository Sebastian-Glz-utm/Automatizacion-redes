
# Recursos de GNS3 y automatización de redes

## 1. ¿Qué tipo de problema podrías resolver consultando la documentación de GNS3?

La documentación de GNS3 permite resolver problemas relacionados con la creación y configuración de topologías de red, la conexión entre dispositivos virtuales, la configuración del servidor y el uso de la máquina virtual de GNS3. También ayuda a identificar errores de instalación, problemas de comunicación y fallas al iniciar los dispositivos. Por ejemplo, si un router no inicia o dos dispositivos no pueden comunicarse, se puede consultar la documentación para revisar la configuración y encontrar una posible solución.

## 2. ¿Qué diferencia existe entre la documentación de una herramienta y el repositorio de una biblioteca?

La documentación de una herramienta explica cómo instalarla, configurarla y utilizar sus funciones. Por otro lado, el repositorio de una biblioteca contiene su código fuente, archivos del proyecto, ejemplos, pruebas, versiones y las instrucciones necesarias para instalarla o colaborar en su desarrollo. Ambos recursos se complementan porque la documentación facilita el uso de la herramienta, mientras que el repositorio permite conocer cómo está desarrollada la biblioteca y revisar sus cambios.

## 3. ¿Qué información revisarías antes de utilizar una biblioteca de automatización?

Antes de utilizar una biblioteca de automatización revisaría su documentación, los requisitos de instalación, la versión de Python compatible, las dependencias, la licencia, los ejemplos de uso, la actividad del proyecto y los problemas conocidos. También comprobaría los métodos disponibles, los requisitos de conexión y la manera de manejar los errores. Esto permite determinar si la biblioteca es adecuada para las necesidades del proyecto y evita utilizar herramientas incompatibles o que no reciben mantenimiento.

## 4. ¿Por qué es importante comprobar qué plataformas y funciones admite una biblioteca?

Es importante porque no todas las bibliotecas funcionan con los mismos dispositivos, sistemas operativos, protocolos o versiones de software. Por ejemplo, Netmiko permite establecer conexiones SSH con diferentes plataformas de red, pero es necesario revisar su lista de dispositivos compatibles y el identificador correspondiente a cada equipo. Comprobar esta información ayuda a evitar errores de compatibilidad y permite elegir una solución apropiada para los routers y switches que se desean administrar.

## 5. ¿Cómo podrían utilizarse estos recursos en las siguientes prácticas?

Estos recursos podrían utilizarse para mejorar los programas desarrollados en Python, consultar información de los dispositivos de red y aprender a automatizar tareas repetitivas. La documentación de GNS3 ayudaría a resolver problemas de topología y conectividad, mientras que los repositorios y ejemplos de bibliotecas como Netmiko servirían para estudiar cómo establecer conexiones con dispositivos compatibles. En las siguientes prácticas, estos conocimientos podrían aplicarse para obtener información de los equipos, ejecutar comandos de consulta y documentar los resultados. Antes de implementar conexiones reales, sería necesario verificar la compatibilidad y probar los scripts en un entorno controlado.

---

# Recursos técnicos consultados

## Recurso 1. Documentación oficial de GNS3

- **Nombre:** GNS3 Documentation.
- **URL:** https://docs.gns3.com/
- **Tema que aborda:** Instalación, configuración, creación de topologías y solución de problemas en GNS3.
- **Tipo de información:** Guías, procedimientos, explicaciones técnicas y recomendaciones para configurar el entorno de simulación y emulación de redes.
- **Utilidad para el proyecto integrador:** Permite comprender y solucionar problemas en la infraestructura de red simulada que se utiliza para las prácticas de automatización.
- **Ejemplo de cuándo lo consultaría:** Cuando un dispositivo virtual no inicia o cuando necesito revisar la configuración de una topología.

## Recurso 2. Repositorio oficial de Netmiko

- **Nombre:** Netmiko - Multi-vendor library to simplify Paramiko SSH connections to network devices.
- **URL:** https://github.com/ktbyers/netmiko
- **Tema que aborda:** Automatización de dispositivos de red mediante conexiones SSH desde Python.
- **Tipo de información:** Código fuente, instrucciones de instalación, ejemplos, documentación, plataformas compatibles y seguimiento de problemas.
- **Utilidad para el proyecto integrador:** Permite investigar cómo desarrollar scripts que obtengan información de routers y switches compatibles sin ejecutar manualmente cada comando.
- **Ejemplo de cuándo lo consultaría:** Cuando necesite investigar cómo establecer una conexión SSH con un router compatible y obtener información mediante comandos de consulta.

## Recurso 3. Plataformas compatibles con Netmiko

- **Nombre:** Netmiko Supported Platforms.
- **URL:** https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md
- **Tema que aborda:** Dispositivos y plataformas de red admitidos por Netmiko.
- **Tipo de información:** Listas de plataformas probadas, plataformas con pruebas limitadas e identificadores utilizados para establecer conexiones.
- **Utilidad para el proyecto integrador:** Ayuda a comprobar si los equipos que se desean automatizar son compatibles con la biblioteca antes de desarrollar los scripts.
- **Ejemplo de cuándo lo consultaría:** Antes de intentar establecer una conexión desde Python con un router Cisco u otro dispositivo compatible, para verificar su plataforma y el identificador correcto.
