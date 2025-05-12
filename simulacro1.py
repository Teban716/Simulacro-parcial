from operator import truediv


lista_de_estudiantes = [   
    {
        'id':1027660067, 
        'nombre': 'Esteban', 
        'primer_apellido': 'Gonzalez', 
        'segundo_apellido': 'Sanchez', 
        'edad': 20,
    },
    {
        'id':1028394039, 
        'nombre': 'Juan Esteban', 
        'primer_apellido': 'Gonzalez', 
        'segundo_apellido': 'Sanchez', 
        'edad': 19,
    } 
    
]
   
def pedir_numero_entero_positivo(prompt):
    while(True):
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("\n||El numero no es positivo|| \n")
        except ValueError:
            print("\n||Ingresa un dato valido|| \n")

def imprimir_fila(a, b, c, d, e):
    print('{:<12}  {:<12}  {:<12}  {:<12}  {:<12}'.format(a, b, c, d, e) )

def visualizar_menu():
    while(True):
        print('\n--------------------------------------------------------')
        print('MENU')
        print('1. Agregar estudiantes')
        print('2. Buscar estudiantes')
        print('3. Actualizar informacion de los estudiantes')
        print('4. Eliminar estudiantes')
        print('5. Calcular promedio de notas')
        print('6. Listado de estudiantes inferiores a la nota')
        print('7. Ver lista de estudiantes')
        print('8. Salir')
        print('--------------------------------------------------------\n')

        opcion = input('\nOpcion:')
        if opcion == '1':
            agregar_Estudiantes()
        if opcion == '2':
            buscar_Estudiantes_menu()
        if opcion == '3':
            actualizar_informacion_estudiantes()
        if opcion == '4':
            eliminar_estudiantes()
        if opcion == '5':
            calcular_promedio_notas()
        if opcion == '6':
            listar_estudiantes_inferiores_a_nota()
        if opcion == '7':
            print(lista_de_estudiantes)
        if opcion == "8":
            break
def agregar_Estudiantes():
    print('\n NUEVO ESTUDIANTE')

    id = pedir_numero_entero_positivo('ID: ')

    estudiantes_ids = []
    for estudiante in lista_de_estudiantes:
        estudiantes_ids.append(estudiante["id"])

    if id in estudiantes_ids:
        print("\n||El estudiante ya esta registrado|| \n")
        return None
    nombre = input('Nombre: ')
    primer_apellido = input('Primer Apellido: ')
    segundo_apellido = input('Segundo Apellido: ')
    edad = pedir_numero_entero_positivo('Edad: \n')

    estudiante = {
        'id':id, 
        'nombre': nombre, 
        'primer_apellido': primer_apellido, 
        'segundo_apellido': segundo_apellido, 
        'edad': edad,
    }
    lista_de_estudiantes.append(estudiante)
    print('\nEstudiante agregado \n')

def buscar_Estudiantes_menu():
    print('1. Buscar estudiantes por ID')
    print('2. Buscar estudiantes por Nombre')

    opcion = input('Opcion: ')

    if opcion == '1':
        buscar_estudiantes_por_id()
    elif opcion == '2':
        buscar_estudiantes_por_nombre()
    else:
        print(f'\nOpcion invalida\n')
        buscar_Estudiantes_menu()


def buscar_estudiantes_por_id():
    if len(lista_de_estudiantes) == 0:
        print("||No hay nadie en la lista||")
    id = pedir_numero_entero_positivo('Id del estudiante: ')
    print("")
    imprimir_fila('ID', 'Nombre', 'Apellido 1', 'Apellido 2', 'Edad')
    for estudiante in lista_de_estudiantes:
        if id == estudiante['id']:
            imprimir_fila(
                estudiante['id'],
                estudiante['nombre'],
                estudiante['primer_apellido'],
                estudiante['segundo_apellido'],
                estudiante['edad'])
            return
    print('\nEl estudiante no esta en la lista \n')
    
def buscar_estudiantes_por_nombre():
    if len(lista_de_estudiantes) == 0:
        print("||No hay nadie en la lista||")

    nombre = input('Nombre del estudiante: ')

    encontrado = False

    for estudiante in lista_de_estudiantes:
        if nombre in estudiante['nombre']:
            print(
                estudiante['id'],
                estudiante['nombre'],
                estudiante['primer_apellido'],
                estudiante['segundo_apellido'],
                estudiante['edad'])
            encontrado = True
            
    if not encontrado:
        print("\n||El estudiante no esta en la lista|| \n")
    
def actualizar_informacion_estudiantes():
    id = pedir_numero_entero_positivo("ID del estudiante a eliminar: ")
    for i, estudiante in enumerate(lista_de_estudiantes):
        if id == estudiante['id']:
            nombre = input ('Nombre')
            apellido1 = input ('Primer apellido')
            apellido2 = input ('Segundo apellido')
            edad = pedir_numero_entero_positivo ('edad')
            
            lista_de_estudiantes[i]['nombre'] = nombre
            lista_de_estudiantes[i]['primer_apellido'] = apellido1
            lista_de_estudiantes[i]['segundo_apellido'] = apellido2
            lista_de_estudiantes[i]['edad'] = edad
            print('Estudiante actualizado')
            return
    print("\n||El estudiante no esta en la lista||")

def eliminar_estudiantes():
    id = pedir_numero_entero_positivo("ID del estudiante a eliminar: ")
    for estudiante in lista_de_estudiantes:
        if id == estudiante['id']:
            lista_de_estudiantes.remove(estudiante)
            print('Estudiante Eliminado')
            return
    print("\n||El estudiante no esta en la lista||")

def calcular_promedio_notas():
    ()

def listar_estudiantes_inferiores_a_nota():
    ()


visualizar_menu()



        







