# inmangacp



Un programa/herramienta para descargar capítulos de manga enteros desde www.inmanga.com.
Por el momento inmangacp solo soporta Firefox para descargar los capítulos, en el futuro planeo agregar soporte para Chrome.
Inmangacp requiere de geckodriver para poder controlar Firefox, de lo contrarío, no va a funcionar. Por eso se deberá descargar geckodriver y agregarlo al PATH del sistema
o en su defecto, colocarlo en la misma dirección que inmangacp.

link de descarga geckodriver: https://github.com/mozilla/geckodriver/releases

link de descarga inmangacp: https://github.com/obskur123/inmangacp/releases/tag/v1.0

## Utilización

La idea de esta herramienta es que se utilice como un programa dentro de la línea de comandos (cmd). 

La dirección donde se encuentre el ejecutable se debe agregar al PATH del sistema para que sea más cómodo y accesible.
Desde su ejecucion comenzaran a aparecer una serie de mensajes que informarán que está ocurriendo y en el peor de los casos soltara un error de URL inválida o que no se ha podido localizar el "elemento", lo que terminara la ejecución; Esto quiere decir que quizás la página cargo lento y el programa ha sido incapaz de resolver el HTML o quizás la página ha sido actualizada, por lo tanto, el HTML dejo de ser el mismo. 
Al terminar la ejecución se creará una carpeta en la misma direccion que el ejecutable con el nombre del capítulo descargado con todas las páginas dentro en formato .PNG.

### Buscar el editor de variables del sistema. 

![Captura de pantalla 2021-01-18 184006](https://user-images.githubusercontent.com/65251657/104965276-2470df00-59bd-11eb-8a12-c403d79b15ce.png)

### Clickear variables de entorno.

![Captura de pantalla 2021-01-18 184300](https://user-images.githubusercontent.com/65251657/104965280-25a20c00-59bd-11eb-9ed8-3bf650eac190.png)

### Buscar la variable "Path" dentro de las variables del sistema y clickear editar.

![Captura de pantalla 2021-01-18 185922](https://user-images.githubusercontent.com/65251657/104966366-787cc300-59bf-11eb-96f1-dc47f45de1cf.png).

### Clickear nuevo y agregar la carpeta en donde se encuentran "geckodriver" y "inmangacp".

![Captura de pantalla 2021-01-18 184237](https://user-images.githubusercontent.com/65251657/104965274-233fb200-59bd-11eb-9768-620dcaa8137c.png)

Ahora solo queda reiniciar el sistema o reiniciar el explorer de Windows para que pueda encontrar la direccion del programa y del driver.

### Ejemplo de utilización: 

```
C:\Users\Pepe> inmangacp <URL DEL CAPITULO>
```

## Consideraciones

- No parece funcionar cuando es ejecutado a traves de Windows Powershell.
- Debido a que lo empaquete con Pyinstaller es altamente probable que Windows Defender crea que es un virus, no lo es, se debe agregar una excepción al archivo de la siguiente forma: https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26
- Los capitulos se estan guardando en el directorio "Users\\tu usuario" Windows.



