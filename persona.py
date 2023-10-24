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

        # Añade los datos a la siguiente fila disponible en la hoja de trabajo
        fila = [str(dato) for dato in datos]
        worksheet.append(fila)

        # Guarda los cambios en el archivo Excel
        workbook.save(nombre_archivo)


