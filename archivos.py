#modulo para guardar la libreria con el manejo de archivo.
from cryptography.fernet import Fernet 
from pathlib import Path

def leerArchivo(archivo): 
    stream=open(archivo,"rt", encoding="utf-8")#conjunto de datos que se almacena cuando se abra el archivo
    #en esta parte se abre en modo lectura
    print(stream.read())#por el este meto se mostrara la informacion del archivo



def escribirArchivo(linea, archivo):
    with open(archivo,'a')as file : #argumento a=append o agregar 

        file.write("\n"+linea)
def generar_clave():
    archivo= r'Key.Key'
    objetoArchivo=Path(archivo)
    if not objetoArchivo.is_file():

        clave=Fernet.generate_key()

        with open("Key.Key", "wb") as Key_file:
            Key_file.write(clave)
def cargar_clave():
    return open("key.key","rb").read()


def encriptar(archivo,clave):
 f=Fernet(clave)
 with open(archivo,"rb") as file:
   file_data=file.read()


   datos_encriptados = f.encrypt(file_data)

   with open(archivo,"wb") as file:
      file.write(datos_encriptados)

def desencriptar(archivo,clave):
   f = Fernet(clave)
   with open(archivo,"rb") as file:
      datos_encriptados = file.read()
      datos = f.decrypt(datos_encriptados)
      with open(archivo, "wb") as file:
         file.write(datos)

# En el archivo "archivos.py"


