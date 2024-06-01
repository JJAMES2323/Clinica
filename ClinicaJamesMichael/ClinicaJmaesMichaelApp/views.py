from django.shortcuts import render
from datetime import datetime
from typing import Any
from django import http 
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Personas,Paciente,Ordenes,Sesion,AyudaDiagnostica,Medicamentos,Procedimiento,Asistencia,Enfermeras
from ClinicaJamesMichael.conexionMongo import collection, visita_collection
import json,secrets,string
from.ValidarEntradas import ValidarPersonas
from bson import json_util

# Create your views here.

def validarRol(sesion,rol):
    if sesion.usuario.rol not in rol:
        print("entra")
        print(sesion)
        raise Exception("El usuario no posee permisos")
    
class Logueo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)  
    def get(self, request,id=None):
        pass
    def put(self,request):
        pass
    def post(self,request):
        token=""
        message1=""
        try:
            body=json.loads(request.body)
            rol=body["rol"]
            usuario=body["usuario"]
            password=body["password"]
            persona=Personas.objects.get(usuario=usuario,rol=rol,password=password)
            fechaActual=datetime.now().date()
            sesion=Sesion.objects.filter(usuario=persona)
            if sesion.exists():
                raise Exception("El usuario ya esta en sesion")
            caracteres = string.ascii_letters+string.digits
            token= "".join(secrets.choice(caracteres)for _ in range(128))
            sesion=Sesion(usuario=persona, token=token)
            sesion.save()
            ultimaAsistencia= Asistencia.objects.filter(usuario=persona).order_by("-fecha").first()
            if ultimaAsistencia and ultimaAsistencia.fecha.date() == fechaActual:
                message1="ya el ususario tiene una asistencia exixtente"                
            else:
               fecha=str(datetime.now())
               asistencia=Asistencia(fecha=fecha,usuario=persona.usuario)
               asistencia.save()
               message1="OK"
            message = "login exitoso"
            status= 200
        except Exception as error:
            message=str(error)
            status=400
        response={"message": message, "message1": message1,"token" : token}
        return JsonResponse(response,status=status)

    def delete(self,request):
        try:
            token = request.META.get('HTTP_TOKEN')
            sesion=Sesion.objects.get(token=token)
            sesion.delete()
            message="se ha cerrado sesion"
            status=200
        except Exception as error:
            message=str(error)
            status=400
        response={"message":message}
        return JsonResponse(response,status=status)

   
class RegistroUsuario(View):
        @method_decorator(csrf_exempt)
        def dispatch(self,request, *args: Any, **kwargs: Any):
            return super().dispatch(request, *args, **kwargs)
        def get(self,request,id=None):
            personas=None
            try:
                token = request.META.get("HTTP_TOKEN")
                sesion=Sesion.objects.get(token=token)
                validarRol(sesion,["RH"])
                if id:
                    personas=list(Personas.objects.filter(cedula=id).values())
                else:
                    personas=list(Personas.objects.values())
                if len(personas)>0:
                    message="Resgistro encontrado"
                else:
                    message="resgitro no encontrado"
                status=200
            except Exception as error:
                message=str(error)
                status=400
            response={"message":message, "persona":personas}
            return JsonResponse(response,status=status)                        
        def put(self, request):
            pass
        def post(self,request):
            try:
                token = request.META.get("HTTP_TOKEN")
                sesion=Sesion.objects.get(token=token)
                validarRol(sesion,["RH"])
                body=json.loads(request.body)
                cedula=body["cedula"]
                ValidarPersonas.ValidarCedula(cedula)
                nombre=body["nombre"]
                ValidarPersonas.ValidarNombre(nombre)
                rol=body["rol"]
                usuario=body["usuario"]
                ValidarPersonas.ValidarUsuario(usuario)
                password=body["password"]
                ValidarPersonas.ValidarContraseña(password)
                correoE=body["correoE"]
                ValidarPersonas.ValidarCorreo(correoE)
                telefono=body["telefono"]
                ValidarPersonas.ValidaTelefono(telefono)
                fecha=body["fecha"]
                ValidarPersonas.ValidarfechaN(fecha)
                direccion=body["direccion"]
                ValidarPersonas.ValidarDireccion(direccion)
                persona=Personas.objects.filter(cedula=cedula)
                if persona.exists():
                    raise Exception("Ya hay una persona con esta cedula")
                persona=Personas.objects.filter(usuario=usuario)
                if persona.exists():
                    raise Exception("Ya exixte una persona con este ususario")
                persona=Personas(cedula=cedula,nombre=nombre,rol=rol,usuario=usuario,password=password,correoE=correoE,telefono=telefono,fecha=fecha,direccion=direccion)
                persona.save()
                message="Registro exitoso"
                status=200
            except Exception as error:
                message=str(error)
                status=400
            response={"message": message}
            return JsonResponse (response,status=status)
        def delete(self,request):
            try:
                token = request.META.get("HTTP_TOKEN")
                sesion=Sesion.objects.get(token=token)
                validarRol(sesion,["RH"])
                body=json.loads(request.body)
                cedula=body["cedula"]
                ValidarPersonas.ValidarCedula
                persona=Personas.objects.get(cedula=cedula)
                persona.delete()
                message="Se ha eliminado la persona"
                status=200
            except Exception as error:
                message=str(error)
                status=400
            response={"message" :message}
            return JsonResponse(response,status=status)
        def patch(self,request,id=None):
            persona=None
            try: 
                token=request.META.get("HTTP_TOKEN")
                sesion=Sesion.objects.get(token=token)
                validarRol(sesion,["RH"])
                body=json.loads(request.body)
                cedula=body.get("cedula")
                if cedula is not None:
                    persona=Personas.objects.get(cedula=cedula)                
                    if "nombre" in body:
                        persona.nombre = body["nombre"]
                    if "rol" in body:
                        persona.rol = body["rol"]
                    if "usuario" in body:
                        persona.usuario = body["usuario"]
                    if "password" in body:
                        persona.password = body["password"]
                    if "correoE" in body:
                        persona.correoE = body["correoE"]                                                                                
                    if "telefono" in body:
                        persona.telefono = body["telefono"]
                    if "fecha" in body:
                        persona.fecha = body["fecha"]
                    if "direccion" in body:
                        persona.direccion = body["direccion"]

                    persona.save()
                    message="Actualizacion exitosa"
                    status=200
                else:
                    message = "Se requiere el campo 'cedula' para la actualización."
                    status = 400
            except Personas.DoesNotExist:
               message = f"No se encontró ninguna persona con la cédula: {cedula}"
               status = 404
            except Exception as error:
                message = str(error)
                status(400)
            response={"message": message}
            return JsonResponse(response,status=status)    

class Pacientes(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=None):
        paciente=None
        try:
            token = request.META.get("HTTP_TOKEN")
            sesion=Sesion.objects.get(token=token)
            validarRol(sesion,["Administrador"])
            if id:
                paciente=list(Paciente.objects.filter(cedula=id).values())
            else:
                paciente=list(Paciente.objects.values())    
            if len(paciente)>0:
                message="Registros encontrados"
            else:
                message="Registros no encontrados"
            status=200
        except Exception as error:
            message=str(error)
            status=400
        response={"message":message, "paciente":paciente}
        return JsonResponse(response,status=status)
    def put(self, request):
        pass
    def post(self, request):
        try:
            token= request.META.get("HTTP_TOKEN")
            sesion=Sesion.objects.get(token=token)
            validarRol(sesion,["Administrador"])
            body=json.loads(request.body)
            cedula=body["cedula"]
            ValidarPersonas.ValidarCedula(cedula)
            nombre=body["nombre"]
            ValidarPersonas.ValidarNombre(nombre)
            fecha=body["fecha"]
            ValidarPersonas.ValidarfechaN(fecha)
            genero=body["genero"]
            ValidarPersonas.ValidarGenero(genero)
            direccion=body["direccion"]
            ValidarPersonas.ValidarDireccion(direccion)
            telefono=body["telefono"]
            ValidarPersonas.ValidaTelefono(telefono)
            correoE=body["correoE"]
            ValidarPersonas.ValidarCorreo(correoE)
            nombreContacto=body["nombreContacto"]
            ValidarPersonas.ValidarNombreContacto(nombreContacto)
            parentezcoContacto=body["parentezcoContacto"]
            telefonoContacto=body["telefonoContacto"]
            ValidarPersonas.ValidaTelefonoContacto(telefonoContacto)
            nombreSeguro=body["nombreSeguro"]
            ValidarPersonas.ValidarNombreSeguro(nombreSeguro)
            numeroPoliza=body["numeroPoliza"]
            ValidarPersonas.ValidarNumeroDePoliza(numeroPoliza)
            estadoPoliza=body["estadoPoliza"]
            paciente=Paciente.objects.filter(cedula=cedula)
            if paciente.exists():
                raise Exception("Ya exixte un paciente con esta cedula")
            paciente=Paciente(cedula=cedula,nombre=nombre,fecha=fecha,genero=genero,direccion=direccion,telefono=telefono,correoE=correoE,nombreContacto=nombreContacto,parentezcoContacto=parentezcoContacto,telefonoContacto=telefonoContacto,nombreSeguro=nombreSeguro,numeroPoliza=numeroPoliza,estadoPoliza=estadoPoliza)
            paciente.save()
            historiaClinica={"_id":paciente.cedula,"historias":{}}
            collection.insert_one(historiaClinica)
            visita={"_id":paciente.cedula,"visita":{}}
            visita_collection.insert_one(visita)
            message="Registro Exixtoso"
            status=200
        except Exception as error:
            message=str(error)
            status=400
        response={"message": message}
        return JsonResponse (response,status=status)
    def delete(self,request):
            try:
                token = request.META.get("HTTP_TOKEN")
                sesion=Sesion.objects.get(token=token)
                validarRol(sesion,["Administrador"])
                body=json.loads(request.body)
                cedula=body["cedula"]
                ValidarPersonas.ValidarCedula
                paciente=Paciente.objects.filter(cedula=cedula)
                paciente.delete()
                message="Se ha eliminado el paciente"
                status=200
            except Exception as error:
                message=str(error)
                status=400
            response={"message" :message}
            return JsonResponse(response,status=status) 
    def patch(self,request,id=None):
            paciente=None
            try: 
                token=request.META.get("HTTP_TOKEN")
                sesion=Sesion.objects.get(token=token)
                validarRol(sesion,["Administrador"])
                body=json.loads(request.body)
                cedula=body.get("cedula")
                if cedula is not None:
                    paciente=Paciente.objects.get(cedula=cedula)                
                    if "nombre" in body:
                        paciente.nombre = body["nombre"]
                    if "fecha" in body:
                        paciente.fecha = body["fecha"]
                    if "genero" in body:
                        paciente.genero = body["genero"]
                    if "direccion" in body:
                        paciente.direccion = body["direccion"]
                    if "telefono" in body:
                        paciente.telefono = body["telefono"]                                                                                
                    if "correoE" in body:
                        paciente.correoE = body["correoE"]
                    if "nombreContacto" in body:
                        paciente.nombreContacto = body["nombreContacto"]
                    if "parentezcoContacto" in body:
                        paciente.parentezcoContacto = body["parentezcoContacto"]
                    if "telefonoContacto" in body:
                        paciente.telefonoContacto = body["telefonoContacto"]
                    if "nombreSeguro" in body:
                        paciente.nombreSeguro = body["nombreSeguro"]
                    if "numeroPoliza" in body:
                        paciente.numeroPoliza = body["numeroPoliza"]
                    if "estadoPoliza" in body:
                        paciente.estadoPoliza = body["estadoPoliza"]
                    paciente.save()
                    message="Actualizacion exitosa"
                    status=200
                else:
                    message = "Se requiere el campo 'cedula' para la actualización."
                    status = 400
            except Paciente.DoesNotExist:
               message = f"No se encontró ninguna persona con la cédula: {cedula}"
               status = 404
            except Exception as error:
                message = str(error)
                status(400)
            response={"message": message}
            return JsonResponse(response,status=status)   
class ConsultaMedica(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=None):
        historias = {}
        try:
            token = request.META.get("HTTP_TOKEN")
            sesion = Sesion.objects.get(token=token)
            validarRol(sesion,["Medico"])

            cedula = request.GET.get("cedula")
            fecha = request.GET.get("fecha")

            if cedula and fecha:
                fecha_datetime = datetime.strptime(fecha, "%Y-%m-%d")
                fecha_str = fecha_datetime.strftime("%Y-%m-%d")
                print(fecha_str)
                print("entro")

                paciente = Paciente.objects.get(cedula=cedula)
                historia_especifica = collection.find_one({'_id': cedula, 'historias.' + fecha_str: {'$exists': True}})
                if historia_especifica:
                    historias[fecha_str] = historia_especifica['historias'][fecha_str]

            elif id and fecha:
                paciente = Paciente.objects.get(id=id)
                historia_especifica = collection.find_one({'_id': paciente.id, 'historias.' + fecha: {'$exists': True}})
                if historia_especifica:
                    historias[fecha] = historia_especifica['historias'][fecha]
                    print("entro2")

            elif fecha:
                historias = list(collection.find({'historias.' + fecha: {'$exists': True}}))

            if historias:
                message = "Registros encontrados"
            else:
                message = "Registros no encontrados"

            status = 200
        except Exception as error:
            message = str(error)
            status = 400

        response = {"message": message, "historias": historias}
        return JsonResponse(response, status=status)

    def put(self, request):
        pass

    def post(self,request):
        try:
            token=request.META.get("HTTP_TOKEN")
            sesion=Sesion.objects.get(token=token)
            validarRol(sesion,["Medico"])
            body=json.loads(request.body)
            cedula=body["cedula"]
            fechaActual=str(datetime.now().strftime("%Y-%m-%d"))
            paciente=Paciente.objects.get(cedula=cedula)
            medico=sesion.usuario
            historiaActual={"fecha": fechaActual,
                            "medico":medico.usuario
                            }
            historiaActual["motivoConsulta"]=body["motivoConsulta"]
            historiaActual["sintomatologia"]=body["sintomatologia"]
            historiaActual["diagnostico"]=body["diagnostico"]
            orden=Ordenes(cedulaPcaiente=paciente.cedula,fecha=fechaActual,cedulaMedico=medico.cedula)
            orden.save()
            if "ayudaDiagnostica" in body:
                if "medicamento" in body or "procedimiento" in body:
                    raise ValueError("No se puede agregar ayuda diagnostica con medicamentos o procedimientos")
                else:    
                   nmbreAyuda=body["ayudaDiagnostica"]["nmbreAyuda"]
                   cantidad=body["ayudaDiagnostica"]["cantidad"]
                   especialista=body["ayudaDiagnostica"]["especialista"]
                   ordenA=AyudaDiagnostica(nmbreAyuda=nmbreAyuda,cantidad=cantidad,especialista=especialista,orden=orden)
                   ordenA.save()
                   historiaActual["idOrden"]=ordenA.ordenAyud
                   historiaActual["nmbreAyuda"]=nmbreAyuda
                   historiaActual["cantidad"]=cantidad
                   historiaActual["especialista"]=especialista    
            elif "medicamento" in body:
                if "AyudaDiagnostica" in body:
                    raise ValueError("No puedes agregar un medicamnto si se agrega ayuda")
                else:

                   historiaActual["medicamento"]=[]
                   for medicamento in body["medicamento"]:
                       nombreMedicamnto=medicamento["nmbreMedicamento"]
                       dosis=medicamento["Dosis"]
                       duracionTratamiento=medicamento["duracionTratamiento"]
                       ordenM=Medicamentos(nmbreMedicamento=nombreMedicamnto,dosis=dosis,duracionTratamiento=duracionTratamiento,orden=orden)
                       ordenM.save()
                       historiaActual["medicamento"].append({
                           "ordenM": ordenM.ordenMed,
                           "nombreMedicamnto": nombreMedicamnto,
                           "dosis": dosis,
                           "duracionTratamiento": duracionTratamiento
                       })  
            if "procedimiento" in body:
                    if "AyudaDiagnostica" in body:
                        raise ValueError("No puedes agregar un procedimiento si se agrega ayuda")
                    else: 
                       historiaActual["procedimiento"]=[]
                       for procedimiento in body["procedimiento"]:
                           nombreProcedimientos=procedimiento["nombreProcedimientos"]
                           cantidad=procedimiento["cantidad"]
                           frecuencia=procedimiento["frecuencia"]
                           especialista=procedimiento["especialista"]
                           ordenP=Procedimiento(nombreProcedimientos=nombreProcedimientos,cantidad=cantidad,frecuencia=frecuencia,especialista=especialista,orden=orden)
                           ordenP.save() 
                           historiaActual["procedimiento"].append({
                               "ordenP": ordenP.id,
                               "nombreProcedimientos": nombreProcedimientos,
                               "cantidad": cantidad,
                               "frecuencia": frecuencia,
                               "especialista": especialista
                           })   
            historia=collection.find_one({"_id": str(paciente.cedula)})  
            historia["historias"][fechaActual]=historiaActual
            collection.update_one({"_id":str(paciente.cedula)}, {"$set": historia})
            orden.save()
            message="se agrego la historia clinica"
            status=200
        except Exception as error:
            message=str(error)
            status=400
        response={"message": message}
        return JsonResponse(response,status=status)   
                   
class registroEnfermeras (View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=None):
        visita={}
        try:
            token= request.META.get("HTTP_TOKEN")
            sesion=Sesion.objects.get(token=token)
            validarRol(sesion,["Enfermera"])
            if id:
                paciente=Paciente.objects.get(id=id)
                visita=visita_collection.find_one({"_id": paciente.id})
            else:
                visita=list(visita_collection.find())
            if visita:
                message="registros encontrados"
            else:
                message="registros no encontrados"
            status=200
        except Exception as error:
            message=str(error)
            status=400
        response={"message" : message, "visita": visita}
        return JsonResponse(response, status=status)                                
    def post(self,request,id=None):
        try:
            token= request.META.get("HTTP_TOKEN")
            sesion=Sesion.objects.get(token=token)
            validarRol(sesion,["Enfermera"])            
            body=json.loads(request.body)
            cedula=body["cedula"]
            fechaActual=str(datetime.now().strftime("%Y-%m-%d"))
            paciente=Paciente.objects.get(cedula=cedula)
            enfermera=sesion.usuario
            visitaActual={
                "fecha": fechaActual,
                "enfermera": enfermera.usuario
            }
            visitaActual["presion"] =body["presion"]
            visitaActual["temperatura"]= body["temperatura"]
            visitaActual["pulso"]= body["pulso"]
            visitaActual["oxigeno"]= body["oxigeno"]
            if "medicamentos" in body :
                visitaActual["medicamentos"]=[]
                for medicamento in body["medicamentos"]:
                    ordenMed= medicamento.get("ordenMedica")
                    ordenMedicamento = Medicamentos.objects.get(ordenMed=ordenMed)
                    ordenGeneral=str(ordenMedicamento.orden)
                    ordenDeMedicamento=str(ordenMedicamento.ordenMed)
                    nombreMedicamento= ordenMedicamento.nmbreMedicamento
                    dosisAplicada=medicamento["dosisAplicada"]
                    Dosis=ordenMedicamento.dosis.replace("mg", "").strip()
                    Dosis=int(Dosis)
                    if int(dosisAplicada) > Dosis:
                        print(type(Dosis), Dosis)
                        message="No puedes aplicar mas dosis de la recetada"
                    else: 
                       visitaActual["medicamentos"].append({
                           "ordenGeneral":ordenGeneral,
                           "oredenmedicamnto": ordenDeMedicamento,
                           "nombreMedicamento": nombreMedicamento,
                           "dosisAplicada" : dosisAplicada,
                           "enfermera" : enfermera.usuario
                       })
            visita=visita_collection.find_one({"_id": str (paciente.cedula)}) 
            print("paso1")
            visita["visita"][fechaActual]=visitaActual
            print("paso2")
            try:
               print(f"Contenido de visita antes de la actualización: {visita}")
               visita_collection.update_one({"_id": str(paciente.cedula)},{"$set":visita})
               print("paso3")
            except Exception as update_error:
                print(f"Error during update: {str(update_error)}")   
            message="se agrego la visita"
            status=200
        except Exception as error:
            message=str( error)
            status=400
        response={"message": message}    
        return JsonResponse(response,status=status)            