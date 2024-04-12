import archivos
opcion =  0

archivos.generar_clave()
clave = archivos.cargar_clave()


archivo="archivo.txt"
while opcion !=5:
    print("\nSelecciona una opcion")
    print("1.Leer Archivo\n2.Agregar texto al archivo\n3.Encriptar\n4.Desencriptar\n5.Salir")
    opcion = int(input("Ingresar una opcion:"))

    if opcion==1:
        print("El contenido del archivo es:")
        archivos.leerArchivo(archivo)

    elif opcion == 2:
            linea = input("Introduce el texto que deseas agregar al archivo:") #agregar un texto que deseas engcriptar
            archivos.escribirArchivo(linea, archivo)

    elif opcion == 3:
         archivos.encriptar(archivo,clave)
         print("¡¡¡ Archivo encriptado Correctamente")#arrojara un mensaje que el archicho hacido encriptado

    elif opcion == 4:
         archivos.desencriptar(archivo,clave)
         print("¡¡¡ Archivo desencriptado correctamente")        
        
    else:
         print("\n ¡¡¡ La Opcion Seleccionada es incorrecta!!!")