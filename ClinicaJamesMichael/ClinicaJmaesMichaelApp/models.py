from django.db import models

# Create your models here.
class Personas(models.Model):
    cedula=models.IntegerField(primary_key=True,null=False)
    nombre=models.CharField(max_length=30, null=True)
    rol=models.CharField(max_length=30,null=True)
    usuario=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30, null=True)
    correoE=models.EmailField(max_length=30,null=True)
    telefono=models.IntegerField(null=True)
    fecha=models.DateField(null=True)
    direccion=models.CharField(max_length=30,null=True)

class nuevosDatos(models.Model):
    cedula=models.ForeignKey(Personas,on_delete=models.CASCADE,primary_key=True,null=False)
    nombre=models.CharField(max_length=30, null=True)
    rol=models.CharField(max_length=30,null=True)
    usuario=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30, null=True)
    correoE=models.EmailField(max_length=30,null=True)
    telefono=models.IntegerField(null=True)
    fecha=models.DateField(null=True)
    direccion=models.CharField(max_length=30,null=True)
    fecha=models.DateField(null=True)

class doctores(models.Model):
    cedula=models.ForeignKey(Personas,on_delete=models.CASCADE,primary_key=True,null=False)
    nombre=models.CharField(max_length=30, null=True)
    rol=models.CharField(max_length=30,null=True)
    usuario=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30, null=True)
    correoE=models.EmailField(max_length=30,null=True)
    telefono=models.IntegerField(null=True)
    fecha=models.DateField(null=True)
    direccion=models.CharField(max_length=30,null=True)
    fecha=models.DateField(null=True)

class recurososHumanos(models.Model):
    cedula=models.ForeignKey(Personas,on_delete=models.CASCADE,primary_key=True,null=False)
    nombre=models.CharField(max_length=30, null=True)
    rol=models.CharField(max_length=30,null=True)
    usuario=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30, null=True)
    correoE=models.EmailField(max_length=30,null=True)
    telefono=models.IntegerField(null=True)
    fecha=models.DateField(null=True)
    direccion=models.CharField(max_length=30,null=True)
    fecha=models.DateField(null=True)

class administrador(models.Model):
    cedula=models.ForeignKey(Personas,on_delete=models.CASCADE,primary_key=True,null=False)
    nombre=models.CharField(max_length=30, null=True)
    rol=models.CharField(max_length=30,null=True)
    usuario=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30, null=True)
    correoE=models.EmailField(max_length=30,null=True)
    telefono=models.IntegerField(null=True)
    fecha=models.DateField(null=True)
    direccion=models.CharField(max_length=30,null=True)
    fecha=models.DateField(null=True)

class Soporte(models.Model):
    cedula=models.ForeignKey(Personas,on_delete=models.CASCADE,primary_key=True,null=False)
    nombre=models.CharField(max_length=30, null=True)
    rol=models.CharField(max_length=30,null=True)
    usuario=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30, null=True)
    correoE=models.EmailField(max_length=30,null=True)
    telefono=models.IntegerField(null=True)
    fecha=models.DateField(null=True)
    direccion=models.CharField(max_length=30,null=True)
    fecha=models.DateField(null=True)

class Enfermeras(models.Model):
    cedula=models.ForeignKey(Personas,on_delete=models.CASCADE,primary_key=True,null=False)
    nombre=models.CharField(max_length=30, null=True)
    rol=models.CharField(max_length=30,null=True)
    usuario=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=30, null=True)
    correoE=models.EmailField(max_length=30,null=True)
    telefono=models.IntegerField(null=True)
    fecha=models.DateField(null=True)
    direccion=models.CharField(max_length=30,null=True)
    fecha=models.DateField(null=True)

class Paciente(models.Model):
    nombre=models.CharField(max_length=30, null=True)
    cedula=models.IntegerField(primary_key=True,null=False)
    fecha=models.DateField(null=True)
    genero=models.CharField(max_length=10,null=True)
    direccion=models.CharField(max_length=30,null=True)
    telefono=models.IntegerField(null=True) 
    correoE=models.EmailField(max_length=30,null=True)
    nombreContacto=models.CharField(max_length=30, null=True)
    parentezcoContacto=models.CharField(max_length=30, null=True)
    telefonoContacto=models.IntegerField(null=True)
    nombreSeguro=models.CharField(max_length=30, null=True)
    numeroPoliza=models.IntegerField(null=True)
    estadoPoliza=models.BooleanField(null=True)

class HistoriaClinica(models.Model):
    cedulaPcaiente=models.ForeignKey(Paciente,on_delete=models.CASCADE,null=False,primary_key=True)
    fecha=models.DateField(null=True)    
    cedulaMedico=models.IntegerField(null=True)
    MotivoCosnulta=models.CharField(null=True, max_length=100)
    sintamotologia=models.CharField(null=True, max_length=100)
    diagnostico=models.CharField(null=True, max_length=100)

class Ordenes(models.Model):
    orden=models.AutoField(primary_key=True)
    cedulaPcaiente=models.IntegerField(null=True)
    fecha=models.DateField(null=True)    
    cedulaMedico=models.IntegerField(null=True)    

class Medicamentos(models.Model):
    ordenMed=models.AutoField(primary_key=True)
    nmbreMedicamento=models.CharField(null=True,max_length=30)
    dosis=models.CharField(null=True,max_length=30)
    duracionTratamiento=models.CharField(null=True,max_length=30)
    orden=models.ForeignKey(Ordenes,on_delete=models.CASCADE)
    
class Procedimiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombreProcedimientos = models.CharField(null=True, max_length=30)
    cantidad = models.CharField(null=True, max_length=30)
    frecuencia = models.CharField(null=True, max_length=30)
    especialista = models.CharField(null=True,max_length=30)
    orden=models.ForeignKey(Ordenes,on_delete=models.CASCADE)
    
class AyudaDiagnostica(models.Model):
    ordenAyud=models.AutoField(primary_key=True)
    nmbreAyuda=models.CharField(null=True,max_length=30)
    cantidad=models.CharField(null=True,max_length=30)  
    especialista=models.CharField(null=True,max_length=30)
    orden=models.ForeignKey(Ordenes,on_delete=models.CASCADE)

class Factura(models.Model):
    id=models.AutoField(primary_key=True, null=False)
    nombrePaciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,null=True,max_length=30)
    nombreMedico=models.ForeignKey(Personas,on_delete=models.CASCADE,null=True,max_length=30)
    nombreCompañia=models.CharField(null=True,max_length=30)
    numeroPoliza=models.IntegerField(null=True)
    estadoPoliza=models.BooleanField(null=True)

class Asistencia(models.Model):
    fecha=models.DateTimeField(null=True)
    usuario=models.CharField(max_length=30,null=True)

class Vista(models.Model):
    cedulaPcaiente=models.ForeignKey(Paciente,on_delete=models.CASCADE,null=False,primary_key=True)
    fecha=models.DateField(null=True)    
    cedulaMedico=models.IntegerField(null=True)    
    presion=models.CharField(null=True,max_length=30)
    temperatura=models.CharField(null=True,max_length=30)
    pulso=models.CharField(null=True,max_length=30)
    oxigeno=models.CharField(null=True,max_length=30)
        
class Sesion(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    usuario=models.ForeignKey(Personas, on_delete=models.CASCADE, null=True)
    token=models.CharField(max_length=200,null=True,default="")
