import uuid
class Persona:
    def __init__(self,nombre,cedula,correo,telefono,fechan,direccion,rol,usuario,contraseña):
        self.nombre=nombre
        self.cedula=cedula
        self.rol=rol
        self.usuario=usuario
        self.contraseña=contraseña
        self.correo=correo
        self.telefono=telefono
        self.fechaN=fechan
        self.direccion=direccion
class NuevosDatos:
    def __init__(self,nombre,cedula,correo,telefono,fechan,direccion,rol,usuario,contraseña):
        self.nombre=nombre
        self.cedula=cedula
        self.rol=rol
        self.usuario=usuario
        self.contraseña=contraseña
        self.correo=correo
        self.telefono=telefono
        self.fechaN=fechan
        self.direccion=direccion
class Doctores:
    def __init__(self,nombre,cedula,correo,telefono,fechan,direccion,rol,usuario,contraseña):
        self.nombre=nombre
        self.cedula=cedula
        self.rol=rol
        self.usuario=usuario
        self.contraseña=contraseña
        self.correo=correo
        self.telefono=telefono
        self.fechaN=fechan
        self.direccion=direccion
class RecursosHumanos():
    def __init__(self,nombre,cedula,correo,telefono,fechan,direccion,rol,usuario,contraseña):
        self.nombre=nombre
        self.cedula=cedula
        self.rol=rol
        self.usuario=usuario
        self.contraseña=contraseña
        self.correo=correo
        self.telefono=telefono
        self.fechaN=fechan
        self.direccion=direccion
class Administrador():
    def __init__(self,nombre,cedula,correo,telefono,fechan,direccion,rol,usuario,contraseña):
        self.nombre=nombre
        self.cedula=cedula
        self.rol=rol
        self.usuario=usuario
        self.contraseña=contraseña
        self.correo=correo
        self.telefono=telefono
        self.fechaN=fechan
        self.direccion=direccion
class Soporte():
    def __init__(self,nombre,cedula,correo,telefono,fechan,direccion,rol,usuario,contraseña):
        self.nombre=nombre
        self.cedula=cedula
        self.rol=rol
        self.usuario=usuario
        self.contraseña=contraseña
        self.correo=correo
        self.telefono=telefono
        self.fechaN=fechan
        self.direccion=direccion        
class Enfermeras():
    def __init__(self,nombre,cedula,correo,telefono,fechan,direccion,rol,usuario,contraseña):
        self.nombre=nombre
        self.cedula=cedula
        self.rol=rol
        self.usuario=usuario
        self.contraseña=contraseña
        self.correo=correo
        self.telefono=telefono
        self.fechaN=fechan
        self.direccion=direccion
class Paciente:
    def __init__(self,nombre,cedula,fechaNacimiento,genero,direccion,telefono,correo,nombreContacto,parentezcoContacto,numeroContacto,nombreSeguro,numeroPoliza,estadoPoliza):
        self.id= str(uuid.uuid4())
        self.nombre=nombre
        self.cedula=cedula
        self.fechaNacimiento=fechaNacimiento
        self.genero=genero
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
        self.nombreContacto=nombreContacto
        self.parentezcoContacto=parentezcoContacto
        self.numeroContacto=numeroContacto
        self.nombreSeguro=nombreSeguro
        self.numeroPoliza=numeroPoliza
        self.estadoPoliza=estadoPoliza
"""class ContacoEmergencia:
    def __init__(self,nombre,apellidos,relacion,telefono):
        self.nombre=nombre
        self.apellidos=apellidos
        self.relacion=relacion
        self.telefono=telefono"""""
"""class Seguro:
    def __init__(self,nombre,numeroPoliza,estadoPoliza):
        self.nombre=nombre
        self.numeroPoliza=numeroPoliza
        self.estadoPoliza=estadoPoliza """"" 
class HistroriaClinica:
    def __init__(self,cedulaPaciente,fecha,cedulaMedico,motivoConsulta,sintomatologia,diagnostico):
        self.cedulapaciente=cedulaPaciente
        self.fecha=fecha 
        self.cedulaMedico=cedulaMedico
        self.motivoConsulta=motivoConsulta
        self.sintomatologia=sintomatologia
        self.diagnostico=diagnostico
class Medicamentos:
    def __init__(self,orden,nombreMedicamento,dosis,duracionTratamiento):
        self.orden=orden
        self.nombreMedicamento=nombreMedicamento
        self.dosis=dosis
        self.duracionTratamiento=duracionTratamiento
class Procedimiento:
    def __init__(self,orden,nombreProcedimiento,cantidad,frecuencia,requiereEspecialista):
        self.orden=orden
        self.nombreProcedimiento=nombreProcedimiento
        self.cantidad=cantidad
        self.frecuencia=frecuencia
        self.requiereEspecialista=requiereEspecialista    
class AyudaDiagnostica :
    def __init__(self,orden,nombreAyuda,cantidad,requiereAyuda):
        self.orden=orden
        self.nombreAyuda=nombreAyuda
        self.cantidad=cantidad
        self.requiereayuda=requiereAyuda                
class Facturacion:
    def __init__(self,nombrePaciente,nombreMedico,nombreCompañia,numeroPoliza,vigenciaPoliza):
        self.nombrePaciente=nombrePaciente
        self.nombreMedico=nombreMedico
        self.nombreCompañia=nombreCompañia
        self.numeroPoliza=numeroPoliza
        self.vigenciaPoliza=vigenciaPoliza
class Asistencia:
    def __init__(self,fecha,usuario):
        self.fecha=fecha
        self.usuario=usuario
class Hospital:   
    def __init__(self):
        self.personas=[]
        self.pacientes=[]
        self.historiaClinica={}
        self.visita={}
        self.ordenes=[]
        self.ordenesMed=[]
        self.ordenesProc=[]
        self.asistencia=[] 
        self.nuevosDatos=[]   
class Orden:
    def __init__(self,orden,cedulaPaciente,fecha,cedulaMedico,nombreMedicamento,dosis,duracionTratamiento):
        self.orden=orden
        self.cedulapaciente=cedulaPaciente
        self.fecha=fecha 
        self.cedulaMedico=cedulaMedico        
        self.nombreMedicamento=nombreMedicamento
        self.dosis=dosis
        self.duracionTratamiento=duracionTratamiento                              
class Visita:
    def __init__(self,cedulaPaciente,cedulaMedico,fecha,presion,temperatura,pulso,oxigeno):
        self.cedulaPaciente=cedulaPaciente
        self.cedulaMedico=cedulaMedico
        self.fecha=fecha
        self.presion=presion
        self.temperatura=temperatura
        self.pulso=pulso
        self.oxigeno=oxigeno
    