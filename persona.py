import pandas as pd
import openpyxl

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
