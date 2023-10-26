import pandas as pd
import openpyxl
import re

class Persona:
    def __init__(self, nombre, apellido, ob_social, dx, urgencia, procedimiento, mail_contacto, departamento, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.ob_social = ob_social
        self.dx = dx
        self.urgencia = urgencia
        self.procedimiento = procedimiento
        self.mail_contacto = mail_contacto
        self.departamento = departamento
        self.dni = dni
        
    def guardar_en_xlsx(self, nombre_archivo):
        try:
            # Cargar el archivo Excel en un DataFrame
            df = pd.read_excel(nombre_archivo, engine='openpyxl')

            # Crear un nuevo DataFrame con los datos de la persona
            nueva_fila = pd.DataFrame({
                'NOMBRE': [self.nombre],
                'APELLIDO': [self.apellido],
                'OB. SOCIAL': [self.ob_social],
                'DIAGNOSTICO': [self.dx],
                'URGENCIA': [self.urgencia],
                'PROCEDIMIENTO': [self.procedimiento],
                'MAIL': [self.mail_contacto],
                'DEPARTAMENTO': [self.departamento],
                'DNI': [self.dni]
            })

            # Concatenar el nuevo DataFrame a los datos existentes
            df = pd.concat([df, nueva_fila], ignore_index=True)

            # Guardar el DataFrame actualizado en el archivo Excel
            df.to_excel(nombre_archivo, index=False, engine='openpyxl')
            print("Datos guardados exitosamente.")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no fue encontrado.")


## funciones del menu 2 y 3


def eliminar_por_dni(nombre_archivo, dni_a_eliminar):
    try:
        # Cargar el archivo Excel en un DataFrame
        df = pd.read_excel(nombre_archivo, engine='openpyxl')

        # Buscar el índice de la fila con el DNI a eliminar
        index_to_delete = df[df['DNI'] == dni_a_eliminar].index

        if not index_to_delete.empty:
            # Eliminar la fila por índice
            df.drop(index_to_delete, inplace=True)

            # Guardar el DataFrame actualizado en el archivo Excel
            df.to_excel(nombre_archivo, index=False, engine='openpyxl')
            print(f"La persona con DNI {dni_a_eliminar} ha sido eliminada.")
        else:
            print(f"No se encontró ninguna persona con DNI {dni_a_eliminar}.")

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")

#

def buscar(palabra, excel):
    df = pd.read_excel(excel)
    filas_coincidentes = set()  # Usamos un conjunto para evitar duplicados

    # Crear una expresión regular que coincida con la palabra, sin importar las mayúsculas y minúsculas
    regex = re.compile(re.escape(palabra), re.IGNORECASE)

    # Recorrer las filas y columnas del DataFrame
    for fila in df.index:
        for columna in df.columns:
            celda = str(df.at[fila, columna])
            if regex.search(celda):
                filas_coincidentes.add(tuple(df.loc[fila]))

    if filas_coincidentes:
        # Crear un nuevo DataFrame con las filas coincidentes
        resultado_df = pd.DataFrame(list(filas_coincidentes), columns=df.columns)

        # Imprimir las filas coincidentes
        print(resultado_df.to_string(justify='left', index=False))
    else:
        print(f"No se encontraron filas que coincidan con '{palabra}'.")


def validarString(texto):
     # Utilizar una expresión regular para verificar si solo contiene letras
    if re.match("^[a-zA-Z ]{3,20}$", texto):
        # Convertir el texto a minúsculas
        return texto.upper()
    else:
         return None

def validarUrgencia(urgencia):
    if re.match("^[1-3]$", urgencia):
        if urgencia == '1':
            return "ALTA"
        elif urgencia == '2':
            return "MEDIA"
        elif urgencia == '3':
            return "BAJA"
    return None


def validarProcedimiento(procedimiento):
    #verificar si contiene caracteres alfanuméricos y está en el rango de 3 a 50 caracteres
    if re.match("^[a-zA-Z0-9 ]{3,50}$", procedimiento):
        return procedimiento.upper()
    else:
        return None
    
def validar_email(email):
    # Utilizar una expresión regular para validar el formato del correo electrónico
    if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return email.lower()
    else:
        return None
    
def validarDNI(dni):
    # Utilizar una expresión regular para verificar si el DNI contiene 7 u 8 dígitos numéricos
    if re.match(r"^\d{7,8}$", dni):
        return dni
    else:
        return None
    
def validarDepartamento(departamento):
    if re.match("^[1-4]$", departamento):
        if departamento == '1':
            return "TRAUMATOLOGIA"
        elif departamento == '2':
            return "CIRUJIA"
        elif departamento == '3':
            return "CLINICA"
        elif departamento == '4':
            return "ENFERMERIA"
    return None
