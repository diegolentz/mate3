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
            # Abre el archivo Excel
            workbook = openpyxl.load_workbook(nombre_archivo)
        except FileNotFoundError:
            # Si el archivo no existe, se crea uno nuevo
            workbook = openpyxl.Workbook()

        # Selecciona la hoja de trabajo (worksheet) donde deseas escribir o crear
        worksheet = workbook.active

        # Crear una lista de datos con los valores de la persona
        datos = [self.nombre, self.apellido, self.ob_social, self.dx, self.urgencia, self.procedimiento, self.mail_contacto, self.departamento, self.dni]

        # Agrega los encabezados a la primera fila si no existen
        if worksheet.max_row == 1:
            encabezados = ["NOMBRE", "APELLIDO", "OB. SOCIAL", "DIAGNOSTICO", "URGENCIA", "PROCEDIMIENTO", "MAIL", "DEPARTAMENTO", "DNI"]
            worksheet.append(encabezados)

        # Añade los datos a la segunda fila disponible en la hoja de trabajo
        worksheet.append(datos)

        # Guarda los cambios en el archivo Excel
        workbook.save(nombre_archivo)

# Ejemplo de uso
nueva_persona = Persona("John", "Doe", "ObraSocial1", "DX1", "Urgencia", "Procedimiento1", "email@example.com", "Departamento1", "12345")
nueva_persona.guardar_en_xlsx('clinicaDB.xlsx')
