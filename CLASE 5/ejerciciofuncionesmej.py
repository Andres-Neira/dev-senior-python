estudiantes = []
cursos=['Java','Python']
docentes = []
horarios=[]

#funcion para matricular un estudiantes
def matricularEstudiante():
    nombre=input('digite el nombre del estudiante : ')
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

# Funcion para mostrar estudiantes
def mostrarEstudiantes():
    if estudiantes:
        print('\nLista de estudiantes matriculados')
        for estudiante in estudiantes:
            print(f'Estudiante : {estudiante['nombre']}, Curso : {estudiante['curso']}')
    else:
        print('No hay estudiantes asignados')

# Funcion para mostrar docentes
def mostrarDocentes():
    if docentes:
        print('\n Lista de Docentes')
        for docente in docentes:
            print(f'Estudiate : {docente['nombre']}, Curso : {docente['curso']}')
    else:
        print('no hay docentes asignados')

# Funcion para mostrar horarios
def mostrarHorarios():
    if horarios:
        print('\n Horario de los cursos')
        for horario in horarios:
            print(f'Curso : {horario['curso']},dias : {horario['dias']},hora : {horario['hora']}')
    else:
        print('no hay horarios asignados')

# Función editar información estudiante
def editarEstudiante():
    if estudiantes:
        nombreEstudiante=input('Digite el nombre del estudiante a editar')
        for estudiante in estudiantes:
            if nombreEstudiante==estudiante['nombre']:
                nuevoNombre=input('Digite nombre para actualizar de estudiante')
                for i,curso in enumerate(cursos):
                    print(f'{i+1} : {curso}')
                cursoSeleccionado=int(input("Ingrese el numero del curso"))
                if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
                    cursoN = cursos[cursoSeleccionado-1]
                    estudiante['nombre']=nuevoNombre
                    estudiante['curso']=cursoN
                    print(f'Nombre actualizado : {estudiante['nombre']} curso actualizado {estudiante['curso']}')
    else:
        print('No hay estudiantes inscritos')

# funcion eliminar estudiantes
def eliminarEstudiante():
    nombreEstudiante=input('Digite el nombre del estudiante a editar')
    for estudiante in estudiantes:
        if nombreEstudiante==estudiante['nombre']:
            print(len(estudiantes))
            estudiantes.clear()
            print(estudiantes
                  )

# menu de inicio
while True:
    print('\n Sistema de matricula de dev senior')
    print('1. matricular estudiante')
    print('2. Editar información de estudiante')
    print('3. Eliminación de estudiantes nuevos')
    print('4. asignar docente')
    print('5. Cambio de docente a curso')
    print('6. asiganar horario a un curso')
    print('7. Modificar horario')
    print('8. mostrar estudiantes')
    print('9. mostrar docentes')
    print('10. mostrar  horarios')
    print('11.Mostrar información completa')
    print('12. Salir')
    opcion = int(input('Digite una opcion'))
    if opcion == 1:
        matricularEstudiante()
    elif opcion==2:
        editarEstudiante()
    elif opcion==3:
        eliminarEstudiante()
    elif opcion == 4:
        asignarDocente()
    elif opcion ==6:
        asignarHorario()
    elif opcion == 8:
        mostrarEstudiantes()
    elif opcion == 9:
        mostrarDocentes()
    elif opcion == 10:
        mostrarHorarios()
    elif opcion == 12:
        print(" Gracias por usar el sistema de matricula de  dev senior")
        break
    else:
        print('Opción no valida, intente de nuevo')