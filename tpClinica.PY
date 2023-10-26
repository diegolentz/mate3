from persona import Persona
from persona import eliminar_por_dni,buscar,validarString,validarUrgencia,validarProcedimiento,validar_email,validarDNI,validarDepartamento
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

print("BIENVENIDO AL SISTEMA DE GESTION DE CLINICAS \n")
print("ENTITY MANAGEMENT => 1")
print("NETWORKX GRAPHIC => 2")
print("SMART SEARCH => 3")
print("EXIT => 0\n")

while True:
    opcion_principal = input("ELIJE TU OPCION : \n")

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
                
                #verifica nombre, solo letras
                while True:
                    ingresa = input("Nombre: ")
                    nombre = validarString(ingresa)

                    if nombre:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, ingrese solo letras y sin caracteres especiales.")
                
                #verifica apellido, similar a nombre
                while True:
                    ingresa = input("Apellido: ")
                    apellido = validarString(ingresa)

                    if apellido:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, ingrese solo letras y sin caracteres especiales.")
                
                #verifica ob. social
                while True:
                    ingresa = input("Obra social: ")
                    obSoc = validarString(ingresa)

                    if obSoc:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, ingrese solo letras y sin caracteres especiales.")
                
                #valida diagnostico
                while True:
                    ingresa = input("Diagnóstico: ")
                    diagnostico = validarString(ingresa)

                    if diagnostico:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, ingrese solo letras y sin caracteres especiales.")
                
                #valido urgencia, solo puede ser alta/media/baja
                while True:
                    ingresa = input("Urgencia (1 para alta, 2 para media, 3 para baja): ")
                    urgencia = validarUrgencia(ingresa)
                    
                    if urgencia:
                        print(f"Urgencia: {urgencia}")
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, elija 1 para alta, 2 para media o 3 para baja.")
               
                #valido procedimiento, puede admitir caracteres numericos
                while True:
                    ingresa = input("Procedimiento: ")
                    procedimiento = validarProcedimiento(ingresa)

                    if procedimiento:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, ingrese solo letras y sin caracteres especiales.")
                
                #valido e-mail
                while True:
                    ingresa = input("e-mail: ")
                    mail = validar_email(ingresa)

                    if mail:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, vuelve a intentarlo.")
                
                #valido departamento
                while True:
                    ingresa = input("Departamento: (1 para traumatologia, 2 para cirujia, 3 para clinica, 4 para enfermeria )")
                    departamento = validarDepartamento(ingresa)

                    if departamento:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, ingrese solo numero.")
                #valido dni
                while True:
                    ingresa = input("DNI: ")
                    dni = validarDNI(ingresa)

                    if dni:
                        break  # Salir del bucle si la entrada es válida
                    else:
                        print("Entrada inválida. Por favor, ingrese solo letras y sin caracteres especiales.")
                
                
                
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
        try:
            df = pd.read_excel('clinicaDB.xlsx', engine='openpyxl')
        except FileNotFoundError:
            print("El archivo 'clinicaDB.xlsx' no se encontro.")
            continue

        # Crea un grafico de red
        G = nx.DiGraph()

        # Agrega el nodo principal (hospital)
        G.add_node('Hospital')

        # Agrega nodos para cada departamento
        departamentos = df['DEPARTAMENTO'].unique()
        for i, departamento in enumerate(departamentos):
            G.add_node(departamento)
            G.add_edge('Hospital', departamento)

        # Recopila pacientes activos en cada departamento
        pacientes_por_departamento = {}
        for departamento in departamentos:
            pacientes = df[df['DEPARTAMENTO'] == departamento]
            pacientes_por_departamento[departamento] = list(pacientes['MAIL'])

        # Agrega nodos para cada paciente y conectarlos a sus correspondientes departamentos
        for departamento, pacientes in pacientes_por_departamento.items():
            for paciente in pacientes:
                nombre_paciente = df[(df['DEPARTAMENTO'] == departamento) & (df['MAIL'] == paciente)]['NOMBRE'].values[0]
                nombre_correo = f'{nombre_paciente}\n{paciente}'
                G.add_node(nombre_correo, label=paciente)  # Usamos 'label' para almacenar el correo
                G.add_edge(departamento, nombre_correo)

        # Establecemos la posición de los nodos 
        pos = {}
        x_offset = 0

        # Calcular el ancho total necesario para los departamentos y pacientes
        ancho_total = len(departamentos) + max(len(pacientes) for pacientes in pacientes_por_departamento.values())

        for nodo in G.nodes():
            if nodo == 'Hospital':
                pos[nodo] = (x_offset, 3)
            elif nodo in departamentos:
                pos[nodo] = (x_offset - (ancho_total / 3), 2)
                x_offset += 1.5
            else:
                pos[nodo] = (x_offset - (8), 1)
                x_offset += 1
            

        # Dibujar el gráfico de red
        plt.figure(figsize=(10, 10))

        # Dibujar nodos y bordes
        
        edge_colors = [edge[2].get('color', 'darkgray') for edge in G.edges(data=True)]
        edge_styles = [edge[2].get('style', '-') for edge in G.edges(data=True)]
        
        nx.draw_networkx_nodes(G, pos, node_size=2200, nodelist=['Hospital'], node_color='lightcoral',node_shape="s")
        nx.draw_networkx_nodes(G, pos, node_size=6000, nodelist=departamentos, node_color='teal')
        nx.draw_networkx_nodes(G, pos, node_size=2000, nodelist=[n for n in G.nodes() if n not in ['Hospital'] and n not in departamentos], node_color='lightblue')
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, style=edge_styles, width=2, arrowsize=15)

        # Etiquetas de los nodos (incluyendo el nodo "Hospital")
        labels = {n: n for n in G.nodes()}
        
        # Tamaño de la fuente de las etquitas
        font_size = 10

        nx.draw_networkx_labels(G, pos, labels, font_size=font_size, font_color='black')

        plt.axis('off')
        plt.show()
        
    elif opcion_principal == '3':
        palabra =input("escribe una palabra para traer los resultados. \n")
        buscar(palabra,"clinicaDB.xlsx")
    elif opcion_principal == '0':
        print("Saliendo del programa.")
        break  # Salir del bucle while
    else:
        print("\nOPCION INVALIDA, SELECCIONA ENTRE LAS SIGUIENTES.")  
        print("ENTITY MANAGEMENT => 1")
        print("NETWORKX GRAPHIC => 2")
        print("SMART SEARCH => 3")
        print("EXIT => 0\n")
        
    print("\nELIGE UNA OPCION \n.")  
    print("ENTITY MANAGEMENT => 1")
    print("NETWORKX GRAPHIC => 2")
    print("SMART SEARCH => 3")
    print("EXIT => 0\n")
 
    
print("hasta la proxima!")