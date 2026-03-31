import csv # tranbajamos con archivos tipo excel
import json # archivos tipo texto ordenado
import os # manejo de caroetas y archivos

# definimos la ruta para guardar los datos
CARPETA_DATA = "data"
ARCHIVO_CSV = os.path.join(CARPETA_DATA, "data.csv") # ruta para archivo csv
ARCHIVO_JSON = os.path.join(CARPETA_DATA, "data.json") # ruta para archivo json

# funcion existencia revisa si existe y si no, la crea
def crear_carpeta_si_no_exite():
    if not os.path.exists(CARPETA_DATA):
        os.mkdir(CARPETA_DATA)
        
# ----- PARTE DE JSON --------
# json es una lista ordenada que contien diccionarios
# cada diccionario representa un registro

def leer_registros_json():
    # lee los datos en el archivo json
    if not os.path.exists(ARCHIVO_JSON):
        return [] # si no existe un archivo json, nos regresa uno vacio
    with open(ARCHIVO_JSON, 'r', encoding="utf-8") as f:
        return json.load(f)

def guardar_registros_json(registros):
    # guardo los registros en el archivo json
    crear_carpeta_si_no_exite() # nos aseguramos que exista la carpeta
    with open(ARCHIVO_JSON, 'w', encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=4)

def crear_registro_json(registro):
    # agrega un registro nuevo al archivo registros
    registros = leer_registros_json() # traemos todos los datos en el json a registros
    registros.append(registro) # agregamos el nuevo registro a registros
    guardar_registros_json(registros) # guardamos los registros actualizados

def actualizar_registro_json(id_valor, campo_id, nuevos_datos):
    # buscamos el registro por su id para cambiar datos
    registros = leer_registros_json() # traemos todos los datos en el json a registros
    for registro in registros:
        # utilizamos el for para buscar con el id el registro deseado
        # .get() nos permite llamar el valor de una llave
        if registro.get(campo_id) == id_valor:
            # .update() es un metodo de los diccionarios que permite reemplazar o agregar pares clave-valor
            registro.update(nuevos_datos) # actualizamos los datos del registro elegido
            guardar_registros_json(registros) # actulizamos el archivo json con los cambios realizados
            return True # Encontro y actualizo el registro
    return False # No encontro el registro

def eliminar_registro_json(id_valor, campo_id):
    # Busca y elimina el registro si coincide con el id ingresado
    registros = leer_registros_json() # traemos todos los datos en el json a registros
    nuevos_registros = [] # lista donde guardamos los registros execto el que desamos eliminar
    eliminado = False # Bnadera para determinar si encontro el id ingresado
    for  registro in registros:
        if registro.get(campo_id) == id_valor:
            eliminado = True # si encuentra el registro lo aparta de los demas
        else:
            nuevos_registros.append(registro) # guarda los registros que no pasan la condicion
    if eliminado:
        # si eliminado es True guarda registros actualizados
        guardar_registros_json(nuevos_registros)
    # retorna True o False segun la busqueda del registro
    return eliminado

# --------- PARTE DE CSV -----------------
# CSV es una hoja de calculo tipo excel donde cada fila es un registro

def leer_registros_csv():
    # lee el archivo csv
    if not os.path.exists(ARCHIVO_CSV):
        return [] # si no existe, retorna una hoja vacia
    # utilizamos el temodo read 'r' para leer y traer los registros del archivo
    with open(ARCHIVO_CSV, 'r', newline="", encoding="utf-8") as f:
        # utilizamos .DictReader() por que vamos a leer como diccionarios los datos del csv
        lector = csv.DictReader(f)
        # nos retorna una lista que contega lo leido en el archivo csv
        return list(lector)

def crear_registro_csv(registro):
    # Agrea una nueva fila al archivo csv
    crear_carpeta_si_no_exite() # Nos aseguramos de crear la carpeta si no existe
    archivo_existe = os.path.exists(ARCHIVO_CSV) # verificamos si el archivo existe True o Fals
    # utilizamos el metodo appen 'a' para agregar sin sobrescribir
    with open(ARCHIVO_CSV, 'a', newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=f.keys())
        # si el archivo no existe entra a esta condicion
        if not archivo_existe:
            escritor.writeheader() # si es la primera vez escribe los titulos de las columnas
        escritor.writerow(registro) # escribe la nueva fila al final del archivo

def actualizar_registro_csv(id_valor, campo_id, nuevos_datos):
    # Buscamos el registro por su id
    # traemos a la variable registro los datos del archivo csv
    registros = leer_registros_csv()
    # verificamos tengamos registros que comidificar
    if len(registros) == 0:
        return False
    # actualizado -> bandera que nos permite saber si se encontro el id ingresado
    actualizado = False
    for registro in registros:
        # con el for buscamos diccionario por diccionarios con el id
        if registro.get(campo_id) == id_valor:
            registro.update(nuevos_datos) # actualizamos los datos 
            actualizado = True
            # importabte para con break el for, si no la bandera puede cambiar a False
            break
    # si encontramos el registro True pasa a la siguiente condicion
    if actualizado:
        # utilizamos el metodo write 'w' para borrar y escribir los registros actualizados
        with open(ARCHIVO_CSV, 'w', newline="", encoding="utf-8") as archivo:
            # fieldnames=registro[0].keys() -> extrae las claves del primer diccionario y las asigan como nombre a cada columna
            escritor = csv.DictWriter(archivo, fieldnames=registros[0].keys())
            escritor.writeheader()
            escritor.writerows(registros)
    # si se logra actualizar retorna True si no False
    return actualizado

def eliminar_registro_csv(id_valor, campo_id):
    # elimina una fila del archivo
    # leemos y treamos los datos del archivo csv
    registros = leer_registros_csv()
    if len(registros) == 0:
        return False # si no hay registros, no hay nada para eliminar
    # nuevos registros -> va a guardar todos los datos que no se van a eliminar
    nuevos_registros = []
    # eliminado -> bandera que nos permite saber si se encontro el id ingresado
    eliminado = False
    for registro in registros:
        # si el valor de la llave campo id es igual al id ingresado es el registro a eliminar
        if registro.get(campo_id) == id_valor:
            # si lo encontramos cambiamos la bandera y lo separamos del resto de registros
            eliminado = True
        else:
            nuevos_registros.append(registro)
    # si el registro fue encontrado True sigue la siguiente condicion
    if eliminado:
        # utilizamos el metodo write 'w' para borra y sobrescribir los datos actualizados
        with open(ARCHIVO_CSV, 'w', newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=registros[0].keys())
            escritor.writeheader()
            escritor.writerows(nuevos_registros)
    # si se elimino retona True sino False
    return eliminado