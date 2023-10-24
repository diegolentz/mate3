from persona import Persona
from persona import eliminar_por_dni

print("Bienvenido al sistema de gestión de clínicas \n")
print("ENTITY MANAGEMENT => 1")
print("NETWORKX GRAPHIC => 2")
print("SMART SEARCH => 3")
print("EXIT => 0\n")

opcion_principal = input("ELIJE TU OPCION : \n")
while opcion_principal < "4":

    if opcion_principal == '1':
        while True:
            print("\nENTITY MANAGEMENT MENU: \n")
            print("1. Crear nuevo")
            print("2. Eliminar")
            print("0. Volver atrás \n")
            subopcion_entity = input("Elige una opción: \n")
            
            if subopcion_entity == '1':
                print("Has seleccionado 'Crear nuevo' dentro de Entity Management.")
                print("Completa los campos.\n")
            
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                obSoc = input("Obra social: ")
                diagnostico = input("Diagnóstico: ")
                urgencia = input("Urgencia: ")
                procedimiento = input("Procedimiento: ")
                mail = input("e-mail: ")
                departamento = input("Departamento: ")
                dni = input("DNI: ")
                
                nueva_persona = Persona(nombre, apellido, obSoc, diagnostico, urgencia, procedimiento, mail, departamento, dni)
                nueva_persona.guardar_en_xlsx('clinicaDB.xlsx')
                
            elif subopcion_entity == '2':
                print("Has seleccionado 'Eliminar' dentro de Entity Management.")
                dni_a_eliminar = input("Introduce el DNI a eliminar: ")
                dni_a_eliminar = int(dni_a_eliminar)
                
                eliminar_por_dni('clinicaDB.xlsx', dni_a_eliminar)
                                
            elif subopcion_entity == '0':
                break  # Salir del menú de Entity Management y volver al menú principal
            else:
                print("Opción no válida. Por favor, elige una opción válida.")
                
    elif opcion_principal == '2':
        print("Estás en la página 2.")
    elif opcion_principal == '3':
        print("Estás en la página 3.")
    elif opcion_principal == '0':
        print("Saliendo del programa.")
        break  # Salir del bucle while
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
    
    print("Bienvenido al sistema de gestión de clínicas \n")
    print("ENTITY MANAGEMENT => 1")
    print("NETWORKX GRAPHIC => 2")
    print("SMART SEARCH => 3")
    print("EXIT => 0\n")

    opcion_principal = input("ELIJE TU OPCION : \n")
