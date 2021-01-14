# inmangacp



Un programa/herramienta para descargar capítulos de manga enteros desde www.inmanga.com.
Por el momento inmangacp solo soporta Firefox para descargar los capítulos, en el futuro planeo agregar soporte para Chrome.
Inmangacp requiere de geckodriver para poder controlar Firefox, de lo contrarío, no va a funcionar. Por eso se deberá descargar geckodriver y agregarlo al PATH del sistema
o en su defecto, colocarlo en la misma dirección que inmangacp.

link de descarga geckodriver: https://github.com/mozilla/geckodriver/releases

link de descarga inmangacp: https://mega.nz/folder/ilcXASrB#fPB9yJrwDRoeHc3mmPDeow

## Utilización

La idea de esta herramienta es que se utilice como un programa dentro de la línea de comandos. 

```
C:\Users\Pepe> inmangacp <URL DEL CAPITULO>
```

La dirección donde se encuentre el ejecutable se debe agregar al PATH del sistema para que sea más cómodo y accesible.
Desde su ejecucion comenzaran a aparecer una serie de mensajes que informarán que está ocurriendo y en el peor de los casos soltara un error de URL inválida o que no se ha podido localizar el "elemento", lo que terminara la ejecución; Esto quiere decir que quizás la página cargo lento y el programa ha sido incapaz de resolver el HTML o quizás la página ha sido actualizada, por lo tanto, el HTML dejo de ser el mismo. 
Al terminar la ejecución se creará una carpeta en la misma direccion que el ejecutable con el nombre del capítulo descargado con todas las páginas dentro en formato .PNG.

## Consideraciones

- No parece funcionar cuando es ejecutado a traves de Windows Powershell.
- Debido a que lo empaquete con Pyinstaller es altamente probable que Windows Defender crea que es un virus, no lo es, se debe agregar una excepción al archivo de la siguiente forma: https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26
- Los capitulos se estan guardando en el directorio "Users\\tu usuario" Windows.



