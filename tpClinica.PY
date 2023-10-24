from persona import Persona



while True:
    print("Bienvenido al sistema de gestion de clinicas \n")
    print("ENTITY MANAGEMENT => 1")
    print("NETWORKX GRAPHIC => 2")
    print("SMART SEARCH => 3")
    print("EXIT => 0\n")
    opcion = input("ELIJE TU OPCION : \n")
    
    if opcion == '1':
        while True:
            print("ENTITY MANAGEMENT => 1")
            print("NETWORKX GRAPHIC => 2")
            print("SMART SEARCH => 3")
            print("EXIT => 0\n")
            
            opcion = input("ELIJE TU OPCION: ")
            
            if opcion == '1':
                while True:
                    print("\nENTITY MANAGEMENT MENU: \n")
                    print("1. Crear nuevo")
                    print("2. Eliminar")
                    print("0. Volver atrás \n")
                    
                    subopcion = input("Elige una opción: \n")
                    
                    if subopcion == '1':
                        print("Has seleccionado 'Crear nuevo' dentro de Entity Management.")
                        print("completa los campos.\n")
                    
                        nombre = input("Nombre: ")
                        apellido = input("Apellido: ")
                        obSoc = input("Obra social: ")
                        diagnostico = input("Diagnostico: ")
                        urgencia = input("Urgencia: ")
                        procedimiento = input("Procedimiento: ")
                        mail = input("e-mail: ")
                        departamento = input("Departamento: ")
                        dni = input("DNI: ")
                        
                        nueva_persona = Persona(nombre, apellido, obSoc, diagnostico, urgencia, procedimiento, mail, departamento, dni)
                        nueva_persona.guardar_en_xlsx('clinicaDB.xlsx')
                        
                    elif subopcion == '2':
                        print("Has seleccionado 'Eliminar' dentro de Entity Management.")
                        # Coloca aquí la lógica para eliminar un elemento
                    elif subopcion == '0':
                        break  # Salir del menú de Entity Management y volver al menú principal
                    else:
                        print("Opción no válida. Por favor, elige una opción válida.")

    elif opcion == '2':
        print("Estás en la página 2.")
    elif opcion == '3':
        print("Estás en la página 3.")
    elif opcion == '0':
        print("Saliendo del programa.")
        break  # Salir del bucle while
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
        
