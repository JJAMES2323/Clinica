import re

def ValidarGenero(genero):
    if genero == None or genero == "":
        raise ValueError("Genero no valido")

def ValidarNombreContacto(nombreC):
    if nombreC == None or nombreC =="":
        raise ValueError("Nombre de contacto no valido")

def ValidaTelefonoContacto(telefonoC):
    if telefonoC is None or telefonoC == "":
        raise ValueError("Teléfono de contacto no válido")
    
    if len(str(telefonoC)) != 10:
        raise ValueError("Teléfono de contacto debe tener 10 dígitos")
    
    try:
        telefonoC = int(telefonoC)
    except ValueError:
        raise ValueError("Teléfono de contacto debe ser entero")

def ValidarNombreSeguro(nombreS):
    if nombreS == None or nombreS =="":
        raise ValueError("Nombre de seguro no valido")

def ValidarNumeroDePoliza(numeroP):
    if numeroP=="" or numeroP== None:
        raise ValueError("Numero de poliza no valido")
    
    try:
        numeroP=int(numeroP)
    except ValueError:
        raise ValueError("Numero de poliza debe ser entero")

def ValidarEstadoDePoliza(estadoPoliza):
    if estadoPoliza == None or estadoPoliza =="":
        raise ValueError("Estado de poliza no valido")

def ValidarNombre(nombre):
    if nombre == None or nombre =="":
        raise ValueError("Nombre no valido")

def ValidarEdad(edad):
    if edad=="" or edad== None:
        raise ValueError("Edad no valida")
    
    try:
        edad=int(edad)
    except ValueError:
        raise ValueError("Edad debe ser entero")

def ValidarCedula(cedula):
    if cedula is None or cedula == "":
        raise ValueError("Cédula no válida")
    
    if len(cedula) != 10:
        raise ValueError("Cédula debe contener 10 dígitos")
    
    try:
        cedula = int(cedula)
    except ValueError:
        raise ValueError("Cédula debe ser entero")

def ValidarUsuario(usuario):
    if usuario == None or usuario =="":
        raise ValueError("Usuario no valido")

def ValidarContraseña(contraseña):
    if contraseña is None or contraseña == "":
        raise ValueError("Contraseña no válida")
    
    if not any(c.isupper() for c in contraseña):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula")
    
    if not any(c.isdigit() for c in contraseña):
        raise ValueError("La contraseña debe contener al menos un número")
    
    if not re.search(r"[!@#$%^&*()-_=+[\]{}|;:'\",.<>?/]", contraseña):
        raise ValueError("La contraseña debe contener al menos un carácter especial")
    
    if len(contraseña) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")

def ValidarCorreo(correo):
    if correo is None or correo == "":
        raise ValueError("Correo no válido")
    
    partes = correo.split("@")

    if len(partes) != 2:
        raise ValueError("Correo no válido")

    usuario, dominio = partes

    if not (usuario.isalnum() and dominio.count(".") == 1 and all(c.isalnum() or c == "." for c in dominio)):
        raise ValueError("Correo no válido")

def ValidaTelefono(telefono):
    if telefono is None or telefono == "":
        raise ValueError("Teléfono no válido")
    
    if len(str(telefono)) != 10:
        raise ValueError("Teléfono debe tener 10 dígitos")
    
    try:
        telefono = int(telefono)
    except ValueError:
        raise ValueError("Teléfono debe ser entero")

def ValidarfechaN(fechaN):
    if fechaN == None or fechaN =="":
        raise ValueError("Fecha no valida")

def ValidarDireccion(direccion):
    if direccion == None or direccion =="":
        raise ValueError("Dirección no valida")

def validarPersonaUnica(hospital, nuevo):
    for personas in hospital.personas:
        if (personas.usuario == nuevo.usuario and personas.usuario != None) or personas.cedula == nuevo.cedula:
            raise ValueError("Los datos están duplicados")

def buscarPersona(hospital, cedula):
    for persona in hospital.personas:
        if persona.cedula == cedula:
            return persona
    raise ValueError("No se encontró la cédula")

def validarPacUnico(hospital, nuevo):
    for pacientes in hospital.pacientes:
        if pacientes.cedula == nuevo.cedula:
            raise ValueError("Los datos están duplicados")

def buscarPersonaUser(hospital, usuario):
    for persona in hospital.personas:
        if persona.usuario == usuario:
            return persona
    raise ValueError("No se encontró el usuario")

def buscarPaciente(hospital, cedula):
    for paciente in hospital.pacientes:
        if paciente.cedula == cedula:
            return paciente
    raise ValueError("No se encontró el paciente")

def buscarHistoriaClinica(hospital, cedula, fecha):
    if cedula in hospital.historiaClinica:
        historia = hospital.historiaClinica[cedula]
        if fecha in historia:
            return historia[fecha]
    raise ValueError("No se encontró la historia clínica para la cédula y fecha especificadas")
