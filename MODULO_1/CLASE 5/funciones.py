estudiantes = []
cursos=['Java','Python']
docentes = []
horarios=[]

#funcion para matricular un estudiantes
def matricularEstudiante():
    nombre=input('digite el nombre del estudiante')
    print('seleccione el curso a matricular:  ')
    for i,curso in enumerate(cursos):
        print(f'{i+1} : {curso}')
    cursoSeleccionado=int(input('Ingrese el número del curso : '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        estudiante = {'nombre':nombre, 'curso':curso}
        estudiantes.append(estudiante)
        print(f'Estudiante : {nombre}, matriculado en el curso : {curso}')
    else:
        print(f"opción de curso no valida, recuerde que solo hay {len(curso)} cursos")

# Función para asignar un docente a un curso
def asignarDocente():
    print("Seleccionar el curso al que desea asignar un docente")
    for i,curso in enumerate(cursos):
        print(f'{i+1} : {curso}')
    cursoSeleccionado=int(input("Ingrese el numero del curso"))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        nombreDelDocente = input('Digite el nombre del docente')
        docente = {'nombre':nombreDelDocente, 'curso':curso}
        docentes.append(docente)
        print(f'Docente : {nombreDelDocente}, asigando en el curso : {curso}')
    else:
        print(f"opción de curso no valida, recuerde que solo hay {len(curso)} cursos")

# Funcion para asignar horario a un curso
def asignarHorario():
    for i,curso in enumerate(cursos):
        print(f'{i+1} : {curso}')
    cursoSeleccionado=int(input("Ingrese el numero del curso"))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        dias = input('Ingrese los dias de clase (ejemplo: martes y jueves:  ')
        hora = input('ingrese la hora de la clase (ejemplo )')
        horario = {'curso': curso,'dias':dias,'hora':hora}
        horarios.append(horario)
        print(f'Horario Asigando al curso {curso}: {dias} a las {hora}')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)}')


def mostrarEstudiantes():
    if estudiantes:
        print('Lista de estudiantes matriculados')
        for estudiante in estudiantes:
            print(f'Estudiate : {estudiante['nombre']}, Curso : {estudiante['curso']}')
    else:
        print('No hay estudiantes asignados')


def mostrarDocentes():
    if docentes:
        print('Lista de Docentes')
        for docente in docentes:
            print(f'Estudiate : {docente['nombre']}, Curso : {docente['curso']}')
    else:
        print('no hay docentes asignados')

def mostrarHorarios():
    if horarios:
        print('\n Horario de los cursos')
        for horario in horarios:
            print(f'Curso : {horario['curso']},dias : {horario['dias']},hora : {horario['hora']}')
    else:
        print('no hay horarios asignados')

while True:
    print('\n Sistema de matricula de dev senior')
    print('1. matricular estudiante')
    print('2. asignar docente')
    print('3. asiganar horario a un curso')
    print('4. mostrar estudiantes')
    print('5. mostrar docentes')
    print('6. mostrar  horarios')
    print('7.salir')
    opcion = int(input('Digite una opcion'))
    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion ==3:
        asignarHorario()
    elif opcion == 4:
        mostrarEstudiantes()
    elif opcion == 5:
        mostrarDocentes()
    elif opcion == 6:
        mostrarHorarios()
    elif opcion == 7:
        print(" Gracias por usar el sistema de matricula de  dev senior")
        break
    else:
        print('Opción no valida, intente de nuevo')