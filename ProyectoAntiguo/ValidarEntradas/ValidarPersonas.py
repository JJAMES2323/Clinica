import re

def ValidarGenero(genero):
    if genero == None or genero == "":
        print("genero no valido")
        raise Exception("Genero no valido")
def ValidarNombreContacto(nombreC):
    if nombreC == None or nombreC =="":
        print("nombre de contacto no valido")
        raise Exception("nombre de contacto no valido")
def ValidaTelefonoContacto(telefonoC):
    if telefonoC is None or telefonoC == "":
        print("Teléfono de contacto no válido")
        raise Exception("Teléfono de contacto no válido")
    
    if len(str(telefonoC)) != 10:
        print("Teléfono de contacto debe tener 10 dígitos")
        raise Exception("Teléfono de contacto no valido")
    
    try:
        telefonoC = int(telefonoC)
    except ValueError:
        print("Teléfono de contacto no valido")
        raise Exception("Teléfono de contacto debe ser entero")
def ValidarNombreSeguro(nombreS):
    if nombreS == None or nombreS =="":
        print("nombre de seguro no valido")
        raise Exception("nombre de seguro no valido") 
def ValidarNumeroDePoliza(numeroP):
    if numeroP=="" or numeroP== None:
        print("Numero de poliza no valido")
        raise Exception("Numero de poliza no valido")
    try:
        numeroP=int(numeroP)
    except:
        print("Numero de poliza no valido")
        raise Exception("Numero de poliza debe ser entero") 
def ValidarEstadoDePoliza(estadoPoliza):
    if estadoPoliza == None or estadoPoliza =="":
        print("estado de poliza no valido")
        raise Exception("estado de poliza no valido")                     
def ValidarNombre(nombre):
    if nombre == None or nombre =="":
        print("nombre no valido")
        raise Exception("nombre no valido")
def ValidarEdad(edad):
    if edad=="" or edad== None:
        print("edad no valido")
        raise Exception("edad no valido")
    try:
        edad=int(edad)
    except:
        print("edad no valido")
        raise Exception("edad debe ser entero")
def ValidarCedula(cedula):
    if cedula is None or cedula == "":
        print("Cédula no válida")
        raise Exception("Cédula no válida")
    
    if len(cedula) != 10:
        print("Cédula debe contener 10 dígitos")
        raise Exception("Cédula no válida")
    
    try:
        cedula = int(cedula)
    except ValueError:
        print("Cédula no válida")
        raise Exception("Cédula no válida")

def ValidarUsuario(usuario):
    if usuario == None or usuario =="":
        print("usuario no valido")
        raise Exception("usuario no valido")   
    
def ValidarContraseña(contraseña):
    if contraseña is None or contraseña == "":
        print("Contraseña no válida")
        raise Exception("Contraseña no válida")
    
    
    if not any(c.isupper() for c in contraseña):
        print("La contraseña debe contener al menos una letra mayúscula")
        raise Exception("Contraseña no válida")
    

    if not any(c.isdigit() for c in contraseña):
        print("La contraseña debe contener al menos un número")
        raise Exception("Contraseña no válida")
    

    if not re.search(r"[!@#$%^&*()-_=+[\]{}|;:'\",.<>?/]", contraseña):
        print("La contraseña debe contener al menos un carácter especial")
        raise Exception("Contraseña no válida")
    
    
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        raise Exception("Contraseña no válida")
    try:
       ValidarContraseña(contraseña)
    except Exception as e:
       print("Error:", e)

def ValidarCorreo(correo):
    if correo is None or correo == "":
        print("Correo no válido")
        raise Exception("Correo no válido")
    
    partes = correo.split("@")

    if len(partes) != 2:
        print("Correo no válido")
        raise Exception("Correo no válido")

    usuario, dominio = partes

    if not (usuario.isalnum() and dominio.count(".") == 1 and all(c.isalnum() or c == "." for c in dominio)):
        print("Correo no válido")
        raise Exception("Correo no válido")




def ValidaTelefono(telefono):
    if telefono is None or telefono == "":
        print("Teléfono no válido")
        raise Exception("Teléfono no válido")
    
    if len(str(telefono)) != 10:
        print("Teléfono debe tener 10 dígitos")
        raise Exception("Teléfono no válido")
    
    try:
        telefono = int(telefono)
    except ValueError:
        print("Teléfono no válido")
        raise Exception("Teléfono debe ser entero")
   
def ValidarfechaN(fechaN):
    if fechaN == None or fechaN =="":
        print("fecha no valida")
        raise Exception("fecha no valida")
def ValidarDireccion(direccion):
    if direccion == None or direccion =="":
        print("direccion no valida")
        raise Exception("direccion no valida")
def validarPersonaUnica(hospital,nuevo):
    for personas in hospital.personas:
        if (personas.usuario==nuevo.usuario and personas.usuario!=None) or personas.cedula==nuevo.cedula :
            raise Exception("los datos estan duplicados")   
def buscarPersona(hospital, cedula):
    for persona in hospital.personas:
        if persona.cedula == cedula:
            return persona
    raise Exception ("no se encontro cedula")         
def validarPacUnico(hospital,nuevo):
    for pacientes in hospital.pacientes:
        if pacientes.cedula==nuevo.cedula :
           raise Exception("los datos estan duplicados")        
def buscarPersonaUser(hospital,usuario):
    for persona in hospital.personas:
        if persona.usuario==usuario:
            return persona
    raise Exception ("no se encontro usuario")
def buscarPaciente(hospital, cedula):
    for paciente in hospital.pacientes:
        if paciente.cedula == cedula:
            return paciente
def buscarHistoriaClinica(hospital, cedula, fecha):
    if cedula in hospital.historiaClinica:
        historia = hospital.historiaClinica[cedula]
        if fecha in historia:
            return historia[fecha]
    raise Exception("No se encontró la historia clínica para la cédula y fecha especificadas")
        
                    
        
