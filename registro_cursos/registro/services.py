from .models import Estudiante, Direccion, Curso, Profesor, CursoEstudiante

def crear_curso(codigo, nombre, version):
    curso = Curso(
        codigo=codigo, 
        nombre=nombre, 
        version=version
        )
    curso.save()
    return curso

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor(
        rut=rut, 
        nombre=nombre, 
        apellido=apellido, 
        creado_por=creado_por
        )
    profesor.save()
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por):
    estudiante = Estudiante(
        rut=rut, 
        nombre=nombre, 
        apellido=apellido, 
        fecha_nac=fecha_nac, 
        creado_por=creado_por
        )
    estudiante.save()
    return estudiante

def crear_direccion(estudiante_rut, calle, numero, dpto, comuna, ciudad, region):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    direccion = Direccion(
        estudiante=estudiante, 
        calle=calle, 
        numero=numero, 
        dpto=dpto, 
        comuna=comuna, 
        ciudad=ciudad, 
        region=region
        )
    direccion.save()
    return direccion

def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def agrega_profesor_a_curso(codigo_curso, rut_profesor):
    curso = Curso.objects.get(codigo=codigo_curso)
    profesor = Profesor.objects.get(rut=rut_profesor)
    curso.profesor = profesor
    curso.save()
    return curso

def agrega_cursos_a_estudiante(rut_estudiante, codigos_cursos):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    for codigo in codigos_cursos:
        curso = Curso.objects.get(codigo=codigo)
        curso_estudiante = CursoEstudiante(
            curso=curso, 
            estudiante=estudiante
        )
        curso_estudiante.save()

def imprime_estudiante_cursos(rut_estudiante):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    cursos_estudiante = CursoEstudiante.objects.filter(estudiante=estudiante)
    resultado = []

    for curso_estudiante in cursos_estudiante:
        curso = curso_estudiante.curso
        resultado.append(f"Curso: {curso.nombre}, Estudiante: {estudiante.nombre} {estudiante.apellido}")
    
    return resultado
