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
        # Abre el archivo Excel existente
        workbook = openpyxl.load_workbook(nombre_archivo)
        # Selecciona la hoja de trabajo (worksheet) donde deseas escribir
        worksheet = workbook.active

        # Crear una lista de datos con los valores de la persona
        datos = [self.nombre, self.apellido, self.ob_social, self.dx, self.urgencia, self.procedimiento, self.mail_contacto, self.departamento, self.dni]

        # Validar si el DNI ya existe
        for fila in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=9, max_col=9):
            for celda in fila:
                if celda.value == self.dni:
                    print(f"El DNI {self.dni} ya existe en la fila {celda.row}. No se puede agregar la persona.")
                    return  # Salir sin guardar los datos

        # Encontrar la primera fila vacía en la columna A
        fila = 1
        while worksheet.cell(row=fila, column=1).value:
            fila += 1

        # Añadir los datos a la fila encontrada
        for col, dato in enumerate(datos, start=1):
            worksheet.cell(row=fila, column=col, value=dato)

        # Guardar los cambios en el archivo Excel
        workbook.save(nombre_archivo)
        # Cerrar el archivo Excel
        workbook.close()
        
        
        
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
