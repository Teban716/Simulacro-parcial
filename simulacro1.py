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
        'nombre': 'Camilo', 
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

def visualizar_menu():
    print('1. Agregar estudiantes')
    print('2. Buscar estudiantes')
    print('3. Actualizar informacion de los estudiantes')
    print('4. Eliminar estudiantes')
    print('5. Calcular promedio de notas')
    print('6. Listado de estudiantes inferiores a la nota')
    print('7. Salir')

    interactuar_menu()

def interactuar_menu():
    while(True):
        opcion = input('\nOpcion:')
        if opcion == '1':
            agregar_Estudiantes()
        if opcion == '2':
            buscar_Estudiantes_menu()
        if opcion == '3':
            actualizar_informacion_estiudiantes()
        if opcion == '4':
            eliminar_estudiantes()
        if opcion == '5':
            calcular_promedio_notas()
        if opcion == '6':
            listar_estudiantes_inferiores_a_nota()
        if opcion == '7':
            break

def agregar_Estudiantes():
    print('\n NUEVO ESTUDIANTE')

    id = pedir_numero_entero_positivo('ID: ')
    if id in lista_de_estudiantes:
        print("\n||El estudiante ya esta registrado||")
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
    print(lista_de_estudiantes)

def buscar_Estudiantes_menu():
    print('1. Buscar estudiantes por ID')
    print('2. Buscar estudiantes por Nombre')

    opcion = input('Opcion: ')

    if opcion == '1':
        buscar_estudiantes_por_id()
    elif opcion == '2':
        buscar_estudiantes_por_nombre()
    else:
        ("Opcion invalida")


def buscar_estudiantes_por_id():
    ()
    
def buscar_estudiantes_por_nombre():
    ()
    
def actualizar_informacion_estiudiantes():
    ()

def eliminar_estudiantes():
    ()

def calcular_promedio_notas():
    ()

def listar_estudiantes_inferiores_a_nota():
    ()


visualizar_menu()



        







