from Modelo.Modelo import RecursosHumanos,Administrador,Enfermeras,Paciente,Facturacion,Hospital,Doctores,Persona,Soporte,Asistencia,NuevosDatos,Orden,Medicamentos
#,ContacoEmergencia,Seguro
from ValidarEntradas import ValidarPersonas
from datetime import datetime


hospital=Hospital()
nuevosDatos=NuevosDatos("","","","","","","","","")
pac=Paciente("","","","","","","","","","","","","")
rh=Persona("j","123","j","123","j","j","recursos Humanos","j","j")
hospital.personas.append(rh)
medico=Persona("m","1234","m","1234","m","m","Medico","m","m")
hospital.personas.append(medico)
admin=Persona("a","12345","a","12345","a","a","Administrador","a","a")
hospital.personas.append(admin)
asistencia=Asistencia(datetime.now(),"j")
hospital.asistencia.append(asistencia)
print("se creo una persona en rh "+str(hospital.personas[0].nombre))
print("se creo una persona en rh "+str(hospital.personas[0].usuario))
print("se creo una persona en rh "+str(hospital.personas[0].contraseña))

#-----------------------------------------------------------------------------

def rh(hospital):
    usuario= input("ingrese usuario de recursos humanos: "+"\n")
    password=input("ingrese contraseña de recursos humanos: "+"\n")
    sesion=inicioSesion(hospital,usuario,password,"recursos Humanos")
    while sesion:
        print ("\n"+"***MENU RH***"+"\n")
        print("1.Para agregar alguien en recursos humanos")
        print("2.Para agregar alguien como administrador")
        print("3.Para agregar alguien como soporte")
        print("4.Para agregar alguien como doctor")
        print("5.Para agregar alguien como enfermera")
        print("6.Para ver asistencia")
        print("7. Para editar una persona")
        print("8. Para eliminar una persona")
        print("0. para salir"+"\n")
        opcRh= input("ingrese una opcion"+"\n")
        if opcRh=="1":
            print("***MENU CREACION RH***"+"/n")
            nombre= input ("Ingrese el nombre de RH "+"\n")
            cedula= input ("Ingrese el cedula de RH "+"\n")
            correo= input ("Ingrese el correo de RH "+"\n")
            telefono= input ("Ingrese el telefono de RH "+"\n")
            fechaN= input ("Ingrese el fecha de nacimento de RH "+"\n")
            direccion= input ("Ingrese el direccion de RH "+"\n")
            usuario= input ("Ingrese el nombre de usuario de RH "+"\n")
            password= input ("Ingrese el contraseña de RH "+"\n")
            try:
                ValidarPersonas.ValidarNombre(nombre)
                ValidarPersonas.ValidarCedula(cedula)
                ValidarPersonas.ValidarCorreo(correo)
                ValidarPersonas.ValidaTelefono(telefono)
                ValidarPersonas.ValidarfechaN(fechaN)
                ValidarPersonas.ValidarDireccion(direccion)
                rh=Persona(nombre,cedula,correo,telefono,fechaN,direccion,"recursos Humanos",usuario,password)
                ValidarPersonas.validarPersonaUnica(hospital,rh)
                ValidarPersonas.ValidarContraseña(password)
                hospital.personas.append(rh)
                print("se ha creado la persona de RH")
                print("se creo una persona en rh"+str(rh.nombre))
            except:
                print("No se ha creado la persona de RH")
        elif opcRh=="2":
            print("***MENU CREACION ADMINISTRADOR***"+"/n")
            nombre= input ("Ingrese el nombre del administrador "+"\n")
            cedula= input ("Ingrese el cedula del administrador"+"\n")
            correo= input ("Ingrese el correo del administrador"+"\n")
            telefono= input ("Ingrese el telefono del administrador"+"\n")
            fechaN= input ("Ingrese el fecha de nacimento del administrador"+"\n")
            direccion= input ("Ingrese el direccion del administrador"+"\n")
            usuario= input ("Ingrese el nombre de usuario del administrador"+"\n")
            password= input ("Ingrese el contraseña del administrador"+"\n")
            try:
                ValidarPersonas.ValidarNombre(nombre)
                ValidarPersonas.ValidarCedula(cedula)
                ValidarPersonas.ValidarCorreo(correo)
                ValidarPersonas.ValidaTelefono(telefono)
                ValidarPersonas.ValidarfechaN(fechaN)
                ValidarPersonas.ValidarDireccion(direccion)
                Administrador=Persona(nombre,cedula,correo,telefono,fechaN,direccion,"Administrador",usuario,password)
                ValidarPersonas.validarPersonaUnica(hospital,Administrador)
                ValidarPersonas.ValidarContraseña(password)
                hospital.personas.append(Administrador)
                print("se ha creado la persona de administrador")
                print("se creo una persona en administrador"+str(Administrador.nombre))
            except:
                print("No se ha creado la persona de Administrador")             
        elif opcRh=="3":
            print("***MENU CREACION SOPORTE***"+"/n")
            nombre= input ("Ingrese el nombre de soporte "+"\n")
            cedula= input ("Ingrese el cedula de soporte"+"\n")
            correo= input ("Ingrese el correo de soporte"+"\n")
            telefono= input ("Ingrese el telefono de soporte"+"\n")
            fechaN= input ("Ingrese el fecha de nacimento de soporte"+"\n")
            direccion= input ("Ingrese el direccion de soporte"+"\n")
            usuario= input ("Ingrese el nombre de usuario de soporte"+"\n")
            password= input ("Ingrese el contraseña de soporte"+"\n")
            try:
                ValidarPersonas.ValidarNombre(nombre)
                ValidarPersonas.ValidarCedula(cedula)
                ValidarPersonas.ValidarCorreo(correo)
                ValidarPersonas.ValidaTelefono(telefono)
                ValidarPersonas.ValidarfechaN(fechaN)
                ValidarPersonas.ValidarDireccion(direccion)
                Soporte=Persona(nombre,cedula,correo,telefono,fechaN,direccion,"Soporte",usuario,password)
                ValidarPersonas.validarPersonaUnica(hospital,Soporte)
                ValidarPersonas.ValidarContraseña(password)
                hospital.personas.append(Soporte)
                print("se ha creado la persona de soporte")
                print("se creo una persona en soporte "+str(Soporte.nombre))
            except:
                print("No se ha creado la persona de soporte")
        elif opcRh=="4":
            print("***MENU CREACION DOCTOR***"+"/n")
            nombre= input ("Ingrese el nombre de doctor "+"\n")
            cedula= input ("Ingrese el cedula de doctor"+"\n")
            correo= input ("Ingrese el correo de doctor"+"\n")
            telefono= input ("Ingrese el telefono de doctor"+"\n")
            fechaN= input ("Ingrese el fecha de nacimento de doctor"+"\n")
            direccion= input ("Ingrese el direccion de doctor"+"\n")
            usuario= input ("Ingrese el nombre de usuario de doctor"+"\n")
            password= input ("Ingrese el contraseña de doctor"+"\n")
            try:
                ValidarPersonas.ValidarNombre(nombre)
                ValidarPersonas.ValidarCedula(cedula)
                ValidarPersonas.ValidarCorreo(correo)
                ValidarPersonas.ValidaTelefono(telefono)
                ValidarPersonas.ValidarfechaN(fechaN)
                ValidarPersonas.ValidarDireccion(direccion)
                Doctores=Persona(nombre,cedula,correo,telefono,fechaN,direccion,"Medico",usuario,password)
                ValidarPersonas.validarPersonaUnica(hospital,Doctores)
                ValidarPersonas.ValidarContraseña(password)
                hospital.personas.append(Doctores)
                print("se ha creado la persona doctor")
                print("se creo una persona en doctor "+str(Doctores.nombre))
            except Exception as error:
                print(str(error))
                print("No se ha creado la persona en doctores")
        elif opcRh== "5":
            print("***MENU CREACION ENFERMERA***"+"/n")
            nombre= input ("Ingrese el nombre de enfermera "+"\n")
            cedula= input ("Ingrese el cedula de enfermera"+"\n")
            correo= input ("Ingrese el correo de enfermera"+"\n")
            telefono= input ("Ingrese el telefono de enfermera"+"\n")
            fechaN= input ("Ingrese el fecha de nacimento de enfermera"+"\n")
            direccion= input ("Ingrese el direccion de enfermera"+"\n")
            usuario= input ("Ingrese el nombre de usuario de enfermera"+"\n")
            password= input ("Ingrese el contraseña de enfermera"+"\n")
            try:
                ValidarPersonas.ValidarNombre(nombre)
                ValidarPersonas.ValidarCedula(cedula)
                ValidarPersonas.ValidarCorreo(correo)
                ValidarPersonas.ValidaTelefono(telefono)
                ValidarPersonas.ValidarfechaN(fechaN)
                ValidarPersonas.ValidarDireccion(direccion)
                Enfermeras=Persona(nombre,cedula,correo,telefono,fechaN,direccion,"Enfermeras",usuario,password)
                ValidarPersonas.validarPersonaUnica(hospital,Enfermeras)
                ValidarPersonas.ValidarContraseña(password)
                hospital.personas.append(Enfermeras)
                print("se ha creado la persona en enfermeras")
                print("se creo una persona en enfermeras "+str(Enfermeras.nombre))
            except:
                print("No se ha creado la persona en enfermeras")
        elif opcRh=="6":
            verAsistencias(hospital)
        elif opcRh=="7":
            cedula = input("Ingrese la cédula de la persona a modificar:\n")
            datosActual = ValidarPersonas.buscarPersona(hospital, cedula)
            if datosActual:
              print("***MENU CREACION MODIFICACION***\n")
              nombre = input(f"1. Ingrese el nuevo nombre (actual: {datosActual.nombre}): ")
              if nombre == "":
                 nombre = datosActual.nombre
              cedula = input(f"Ingrese la nueva cédula (actual: {datosActual.cedula}): ")
              if cedula == "":
                 cedula = datosActual.cedula
              correo = input(f"Ingrese el nuevo correo (actual: {datosActual.correo}): ")
              if correo == "":
                 correo = datosActual.correo
              telefono = input(f"Ingrese el nuevo teléfono (actual: {datosActual.telefono}): ")
              if telefono == "":  
                 telefono = datosActual.telefono
              fechaN = input(f"Ingrese la nueva fecha de nacimiento (actual: {datosActual.fechaN}): ")
              if fechaN == "":
                 fechaN = datosActual.fechaN
              direccion = input(f"Ingrese la nueva dirección (actual: {datosActual.direccion}): ")
              if direccion == "":
                 direccion = datosActual.direccion
              rol = input(f"Ingrese nuevo rol (actual: {datosActual.rol}): ")
              if rol == "":
                 rol = datosActual.rol
              usuario = input(f"Ingrese el nuevo nombre de usuario (actual: {datosActual.usuario}): ")
              if usuario == "":
                 usuario = datosActual.usuario
              password = input(f"Ingrese la nueva contraseña (actual: {datosActual.contraseña}): ")
              if password == "":
                 password = datosActual.contraseña
              nuevosDatos = NuevosDatos(nombre, cedula, correo, telefono, fechaN, direccion, rol, usuario, password)
              actualizarDatos(nuevosDatos, datosActual)
              print("Los datos de la persona han sido actualizados.")
            else:
                print("No se encontró a la persona con esa cédula.") 
        elif opcRh=="8":
            cedula=input("inrese la cedula de la persona a eliminar"+"\n")
            eliminarPersona(hospital,cedula)                                                                      
        elif opcRh=="0":
            print("cerrando sesion")
            sesion=False
        break
#---------------------------------------------------------------------------------------------

def admin(hospital):
    usuario= input("ingrese usuario de administrador: "+"\n")
    password=input("ingrese contraseña de administrador: "+"\n")
    sesion=inicioSesion(hospital,usuario,password,"Administrador")
    while sesion:
        print ("\n"+"***MENU ADMINISTRADOR***"+"\n")
        print("1.Para registrar un paciente")
        print("0. para salir"+"\n")
        opcadm= input("ingrese una opcion"+"\n")
        if opcadm=="1":
            cedula=input("ingrese cedula del paciente: "+"\n")
            nombre=input("ingrese nombre completo del paciente: "+"\n")
            fechaN=input("ingrese fecha de ncimiento del paciente: "+"\n")
            genero=input("ingrese genero del paciente: "+"\n")
            direccion=input("ingrese direccion del paciente: "+"\n")
            numero=input("ingrese numero del paciente: "+"\n")
            correo=input("ingrese correo del paciente: "+"\n")
            nombreContacto=input("ingrese nombre de contacto de emergencia: "+"\n")
            parentezcoContacto=input("ingrese parentezco de contacto de emergencia: "+"\n")
            numeroContacto=input("ingrese numero de contacto de emergencia: "+"\n")
            nombreSeguro=input("ingrese nombre compañia de seguros: "+"\n")
            numeroPoliza=input("ingrese numero de poliza: "+"\n")
            estadoPoliza=input("ingrese estado de poliza: "+"\n")
            try:
                ValidarPersonas.ValidarNombre(nombre)
                ValidarPersonas.ValidarCedula(cedula)
                ValidarPersonas.ValidarCorreo(correo)
                ValidarPersonas.ValidaTelefono(numero)
                ValidarPersonas.ValidarfechaN(fechaN)
                ValidarPersonas.ValidarNombreContacto(nombreContacto)
                ValidarPersonas.ValidaTelefonoContacto(numeroContacto)
                ValidarPersonas.ValidarNombreSeguro(nombreSeguro)
                ValidarPersonas.ValidarNumeroDePoliza(numeroPoliza)
                ValidarPersonas.ValidarEstadoDePoliza(estadoPoliza)
                ValidarPersonas.ValidarGenero(genero)
                ValidarPersonas.ValidarNombreContacto(parentezcoContacto)
                ValidarPersonas.ValidarDireccion(direccion)
                pac=Paciente(nombre,cedula,fechaN,genero,direccion,numero,correo,nombreContacto,parentezcoContacto,numeroContacto,nombreSeguro,numeroPoliza,estadoPoliza)
                ValidarPersonas.validarPacUnico(hospital,pac)
                hospital.pacientes.append(pac)
                hospital.historiaClinica[str(cedula)]={}
                hospital.visita[str(cedula)]={}
                print("se creo un paciente "+str(pac.nombre))
            except:
                print("No se ha creado el paciente")
        elif opcadm== "0":
            break                    

#-----------------------------------------------------------------------------------------------------------------------------

def med(hospital):
    usuario = input("Ingrese usuario de médico: " + "\n")
    password = input("Ingrese contraseña de médico: " + "\n")
    sesion = inicioSesion(hospital, usuario, password, "Medico")

    while sesion:
        print("\n**MENU MEDICO**\n")
        print("1. Para Ingresar historia clínica")
        print("2. Para ver historia clínica")
        print("0. Para salir\n")
        opcMed = input("Ingrese una opción\n")

        if opcMed == "1":
            cedula = input("Ingrese la cédula del paciente: ")

            if cedula not in hospital.historiaClinica:
                print("No existe paciente con esa cédula")
                continue

            historia = hospital.historiaClinica[cedula]
            fecha = datetime.now().strftime("%Y-%m-%d")
            print(fecha)
            paciente = ValidarPersonas.buscarPaciente(hospital, cedula)
            medico = ValidarPersonas.buscarPersonaUser(hospital, usuario)
            historiaActual = {
                "fecha": fecha,
                "medico": usuario,
                "paciente": cedula,
            }

            motivoConsulta = input("Ingrese motivo de consulta: ")
            historiaActual["motivoConsulta"] = motivoConsulta
            sintomas = input("Ingrese síntomas: ")
            historiaActual["sintomatologia"] = sintomas
            diagnostico = input("Ingrese diagnóstico: ")
            historiaActual["diagnostico"] = diagnostico

            ayuda_diagnostica = input("¿Necesita una ayuda diagnóstica? (Sí/No): ")
            if ayuda_diagnostica.lower() == "si":
                Orden=(len(hospital.ordenes)+1)
                historiaActual["orden"]=Orden
                ayuda = input("Ingrese nombre de ayuda diagnóstica: ")
                historiaActual["nombreAyuda"]=ayuda
                cantidad = input("Ingrese cantidad: ")
                historiaActual["cantidadAyuda"]=cantidad
                especialista = input("¿Se necesita especialista para esta ayuda diagnóstica? (Sí/No): ")
                historiaActual["especialista"]=especialista
                hospital.ordenes.append((len(hospital.ordenes), paciente.cedula, fecha, medico.cedula, ayuda, "", cantidad))  
                historia[fecha] = historiaActual  
                print("Se agregó historia clínica")
            else:
                while True:

                    print("\n1. Agregar medicamento")
                    ordenMed=(len(hospital.ordenes)+1)
                    print("2. Agregar procedimiento")
                    ordenProc=(len(hospital.ordenes)+1)
                    print("0. Continuar")
                    opcion = input("Ingrese una opción: ")

                    if opcion == "1":
                        Medicamento={}
                        Orden=ordenMed
                        Medicamento["orden"]=Orden
                        medicamento = input("Ingrese nombre del medicamento: ")
                        Medicamento["medicamentos"]=medicamento
                        dosis = input("Ingrese dosis de este medicamento: ")
                        Medicamento["dosis"]=dosis
                        duracion = input("Ingrese duración de tratamiento: ")
                        Medicamento["duracion"]=duracion
                        historiaActual.setdefault("medicamentos",[]).append(Medicamento) 
                        hospital.ordenesMed.append((len(hospital.ordenesMed), paciente.cedula, fecha, medico.cedula, medicamento, dosis, duracion))


                    elif opcion == "2":
                        Procedimiento={}
                        Orden=ordenProc
                        Procedimiento["orden"]=Orden                        
                        procedimiento = input("Ingrese nombre del procedimiento: ")
                        Procedimiento["procedimientos"]=procedimiento
                        cantidad = input("Ingrese cantidad: ")
                        Procedimiento["cantidadProcedimiento"]=cantidad
                        frecuencia = input("Ingrese la frecuencia del procedimiento: ")
                        Procedimiento["frecuencia"]=frecuencia
                        especialista = input("¿Se necesita especialista para este procedimiento? (Sí/No): ")
                        Procedimiento["especialista"]=especialista
                        historiaActual.setdefault("procedimientos",[]).append(Procedimiento)
                        hospital.ordenesProc.append((len(hospital.ordenesProc), paciente.cedula, fecha, medico.cedula, procedimiento, cantidad, frecuencia))

                    elif opcion == "0":
                        hospital.ordenesMed.append((len(hospital.ordenesMed), paciente.cedula, fecha, medico.cedula))
                        historia[fecha] = historiaActual  
                        print("Se agregó historia clínica")
                        break

        elif opcMed == "2":
            cedula = input("Ingrese la cédula del paciente: ")

            if cedula not in hospital.historiaClinica:
                print("No existe paciente con esa cédula")
                continue

            print("\n**HISTORIA CLÍNICA DEL PACIENTE**\n")
            print("Cédula del Paciente:", cedula)

            while True:
                fecha_buscar = input("Ingrese la fecha de consulta (YYYY-MM-DD): ")
                historia_paciente = hospital.historiaClinica[cedula]

                if fecha_buscar in historia_paciente:
                    historia = historia_paciente[fecha_buscar]
                    print(historia)
                    break
                else:
                    print("No existe historia clínica para esa fecha")
                    break

        elif opcMed == "0":
            break
# -------------------------------------------------------------------------------------------------
def enfer(hospital):
    usuario= input("ingrese usuario de la enfermera: "+"\n")
    password=input("ingrese contraseña la enfermera: "+"\n")
    sesion=inicioSesion(hospital,usuario,password,"Enfermeras")
    while sesion:
        print ("\n"+"***MENU ENFERMERAS***"+"\n")
        print("1.Para registrar visita de un paciente")
        print("0. para salir"+"\n") 
        opcEnf= input("ingrese una opcion"+"\n")
        if opcEnf== "1":
            cedula=input ("ingrese la cedula del paciente")
            if cedula not in hospital.visita:
                print("no existe paciente con esa cedula")
                continue
            visita=hospital.visita[cedula]  
            fecha=datetime.now()
            paciente = ValidarPersonas.buscarPaciente(hospital,cedula)
            enfermera = ValidarPersonas.buscarPersonaUser(hospital,usuario)
            visitaActual={"fecha":fecha,
                "medico":usuario
                }
            visitaActual["cedulaPaciente"]=paciente
            visitaActual["cedulaEnfermera"]=enfermera
            presion = input("ingrese nivel de presion")
            visitaActual["presion"]=presion
            temperatura = input("ingrese temperatura")
            visitaActual["temperatura"]=temperatura
            pulso = input("ingrese pulso")
            visitaActual["pulso"]=pulso
            oxigeno = input("ingrese nivel de oxigeno")
            visitaActual["oxigeno"]=oxigeno
            visita[fecha]=visitaActual
            print("se registro una visita")
        elif opcEnf == "0":
            break    
                                             
#-----------------------------------------------------------------------------------------------------------------------------
            
def inicioSesion(hospital, usuario, password, rol):
    for personas in hospital.personas:
        if personas.usuario == usuario and personas.contraseña == password and personas.rol == rol:
            asis(hospital,usuario)            
            print("Se ha iniciado sesión")
            return True
    print("No se ha iniciado sesión")
    return False

#----------------------------------------------------1
# -------------------------------------------------------------------------

def asis(hospital, usuario):
    print("entro")
    for asistencia in hospital.asistencia:
        print("entro2")
        if asistencia.usuario == usuario:
            print("No se registró asistencia")
            break
    else:
        nuevaAsistencia = Asistencia(datetime.now(), usuario)
        hospital.asistencia.append(nuevaAsistencia)
        print("Se registró una asistencia de " + nuevaAsistencia.usuario)

#------------------------------------------------------------------------------------------------------------------------------

def verAsistencias(hospital):
        print("Listado de Asistencias:")
        for asistencia in hospital.asistencia:
            print(f"Fecha: {asistencia.fecha}, Usuario: {asistencia.usuario}")
#------------------------------------------------------------------------------------------------------------------------------
def eliminarPersona(hospital, cedula):
    print("entro")
    for persona in hospital.personas:
        if persona.cedula == cedula:
            hospital.personas.remove(persona)
            print(f"Se ha eliminado a {persona.usuario}")
            return
    print("No se encontró la persona a eliminar")

#------------------------------------------------------------------------------------------------------------------------------

def actualizarDatos(nuevosDatos, datosActual):
    atributos = ['nombre', 'cedula', 'correo', 'telefono', 'fechaN', 'direccion', 'rol', 'usuario', 'contraseña']

    for atributo in atributos:
        if hasattr(nuevosDatos, atributo):
            nuevo_valor = getattr(nuevosDatos, atributo)
            if nuevo_valor != "":
                setattr(datosActual, atributo, nuevo_valor)

#------------------------------------------------------------------------------------------------------------------------------
 

while True:
    print ("\n"+"***MENU PRINCIPAL***"+"\n")
    print("1.Para ingresar como recursos humanos")
    print("2.Para ingresar como administrador")
    print("3.Para ingresar como soporte")
    print("4.Para ingresar como medico")
    print("5.Para ingresar como enfermera")
    print("0. para salir"+"\n")
    opc = input("Ingrese su opcion"+"\n")

    if opc =="1":
        rh(hospital)
    elif opc == "2":
        admin(hospital) 
    elif opc == "4":
        med(hospital)
    elif opc == "5":
        enfer(hospital)           
    elif opc=="0":
         break    
    
 












