from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse,response
import requests
import json
from .models import sesion
import random
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def login(request):
    try:
        api_url = "http://127.0.0.1:8081/logueo"
        print(request.GET)
        datos = {
            "rol": request.GET["rol"],
            "usuario": request.GET["usuario"],
            "password": request.GET["password"]
        }
        respuesta = requests.post(api_url, json=datos)
        response = json.loads(respuesta.text)
        print(respuesta.text)
        print(response["message"])
        if respuesta.status_code == 200:
            id = random.randint(100, 99999)
            ses = sesion(id=id, token=response["token"], rol=datos['rol'])
            ses.save()
            redireccion = f"/{datos['rol']}/{str(ses.id)}"
            return redirect(redireccion)
        else:
            return render(request, "error.html", {"mensaje": response["message"]})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def renderLogin(request):
    return render(request, "login.html")

def closeSesion(request, id):
    try:
        ses = sesion.objects.get(id=id)
        headers = {"token": str(ses.token)}
        api_url = "http://127.0.0.1:8081/logueo"
        respuesta = requests.delete(api_url, headers=headers)
        response = json.loads(respuesta.text)
        print(respuesta.text)
        print(response["message"])
        redireccion = reverse('renderLogin')
        return redirect(redireccion)
    except sesion.DoesNotExist:
        return render(request, "error.html", {"mensaje": "La sesión no existe."})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def renderRH(request, id):
    try:
        # Obtener la sesión
        ses = sesion.objects.get(id=id)

        # Validar el rol
        headers = {"token": str(ses.token)}
        api_url = "http://127.0.0.1:8081/RH"
        respuesta = requests.get(api_url, headers=headers)
        response = json.loads(respuesta.text)
        print("entra1")
        if ses.rol == "RH":
            print("entra2")
            return render(request, "RH.html", {"id": id})
        else:
            print("entra3")
            # Si el rol no es válido, puedes redirigir a otra página o mostrar un mensaje de error
            return render(request, "error.html", {"mensaje": "Acceso denegado: Rol no válido"})

    except sesion.DoesNotExist:
        return render(request, "error.html", {"mensaje": "Sesión no encontrada"})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def registraUsusario(request, id):
    try:
        ses = sesion.objects.get(id=id)
        if ses.rol == "RH":
            print(ses.token)
            print("entro")
            headers = {"token": str(ses.token)}
            print(ses.token)
            print("Registeo de paciente")
            api_url = "http://127.0.0.1:8081/RH"
            print(request.GET)
            datos = {
                "cedula": request.GET["cedula"],
                "nombre": request.GET["nombre"],
                "rol": request.GET["rol"],
                "usuario": request.GET["usuario"],
                "password": request.GET["password"],
                "correoE": request.GET["correoE"],
                "telefono": request.GET["telefono"],
                "fecha": request.GET["fecha"],
                "direccion": request.GET["direccion"],
            }
            print(datos)
            respuesta = requests.post(api_url, json=datos, headers=headers)
            print(respuesta)
            response = json.loads(respuesta.text)
            print(respuesta.text)
            print(response["message"])
            if respuesta.status_code == 200:
                messages.add_message(request, messages.SUCCESS, "Se ha registrado la persona")
                return render(request, "RH.html", {"id": id})
            else:
                return render(request, "error.html", {"mensaje": response["message"]})
        else:
            return render(request, "error.html", {"mensaje": "Acceso denegado: Rol no válido"})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def eliminarUsuario(request, id):
    try:
        ses = sesion.objects.get(id=id)
        headers = {"token": str(ses.token)}
        api_url = "http://127.0.0.1:8081/RH"
        datos = {
            "cedula": request.GET["cedula"]
        }
        respuesta = requests.delete(api_url, json=datos, headers=headers)
        response = json.loads(respuesta.text)
        print(response["message"])
        if respuesta.status_code == 200:
            messages.add_message(request, messages.SUCCESS, "Se ha elminado la persona")
            return render(request, "RH.html", {"id": id})
        else:
            return render(request, "error.html", {"mensaje": response["message"]})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def actualizarUsuario(request, id):
    try:
        if request.method == 'POST':
            ses = sesion.objects.get(id=id)
            headers = {"token": str(ses.token)}
            api_url = "http://127.0.0.1:8081/RH"
            datos = {key: value for key, value in request.POST.items() if value != ''}
            respuesta = requests.patch(api_url, json=datos, headers=headers)
            response = json.loads(respuesta.text)
            if respuesta.status_code == 200:
                messages.add_message(request, messages.SUCCESS, "Se ha actualizado a la persona")
                return render(request, "RH.html", {"id": id})
            else:
                return render(request, "error.html", {"mensaje": response["message"]})
        else:
            return HttpResponseBadRequest("Método no permitido")
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def renderAdministradores(request, id):
    try:
        ses = sesion.objects.get(id=id)
        if ses.rol == "Administrador":
            headers = {"token": str(ses.token)}
            api_url = "http://127.0.0.1:8081/administradores"
            respuesta = requests.get(api_url, headers=headers)
            response = json.loads(respuesta.text)
            print(response)
            return render(request, "administradores.html", {"id": id})
        else:
            return render(request, "error.html", {"mensaje": "Acceso denegado: Rol no válido"})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def registrarCliente(request, id):
    try:
        ses = sesion.objects.get(id=id)
        print(ses.token)
        headers = {"token": str(ses.token)}
        print(ses.token)
        print("Registro de paciente")
        api_url = "http://127.0.0.1:8081/administradores"
        print(request.GET)
        datos = {
            "cedula": request.GET["cedula"],
            "nombre": request.GET["nombre"],
            "fecha": request.GET["fecha"],
            "genero": request.GET["genero"],
            "direccion": request.GET["direccion"],
            "telefono": request.GET["telefono"],
            "correoE": request.GET["correoE"],
            "nombreContacto": request.GET["nombreContacto"],
            "parentezcoContacto": request.GET["parentezcoContacto"],
            "telefonoContacto": request.GET["telefonoContacto"],
            "nombreSeguro": request.GET["nombreSeguro"],
            "numeroPoliza": request.GET["numeroPoliza"],
            "estadoPoliza": request.GET["estadoPoliza"],
        }
        print(datos)
        respuesta = requests.post(api_url, json=datos, headers=headers)
        print(respuesta)
        response = json.loads(respuesta.text)
        print(respuesta.text)
        print(response["message"])
        if respuesta.status_code == 200:
            messages.add_message(request, messages.SUCCESS, "Se ha registrado el paciente")
            return render(request, "administradores.html", {"id": id})
        else:
            return render(request, "error.html", {"mensaje": response["message"]})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def renderMedico(request, id):
    try:
        ses = sesion.objects.get(id=id)
        if ses.rol == "Medico":
            headers = {"token": str(ses.token)}
            api_url = "http://127.0.0.1:8081/historia"
            respuesta = requests.get(api_url, headers=headers)
            response = json.loads(respuesta.text)
            print(response)
            return render(request, "medico.html", {"id": id})
        else:
            return render(request, "error.html", {"mensaje": "Acceso denegado: Rol no válido"})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def registrarHistoria(request, id):
    try:
        ses = sesion.objects.get(id=id)
        headers = {"token": str(ses.token)}
        api_url = "http://127.0.0.1:8081/historia/"

        cedula = request.GET.get("cedula", "")
        motivo_consulta = request.GET.get("motivoConsulta", "")
        sintomatologia = request.GET.get("sintomatologia", "")
        diagnostico = request.GET.get("diagnostico", "")

        medicamentos = []
        procedimientos = []
        ayuda_diagnostica = {}

        listaMedicamentos = request.GET.get("medicamentosData")
        if listaMedicamentos:
            medicamentosP = json.loads(listaMedicamentos) if listaMedicamentos else []
            medicamentos = [v for v in medicamentosP.values()]

        listaProcedimientos = request.GET.get("procedimientosData")
        if listaProcedimientos:
            procedimientosP = json.loads(listaProcedimientos) if listaProcedimientos else []
            procedimientos = [v for v in procedimientosP.values()]

        listaAyudas = request.GET.get("ayudasDiagnosticasData")
        if listaAyudas:
            ayuda_diagnostica = json.loads(listaAyudas) if listaAyudas else {}

        datos = {
            "cedula": cedula,
            "motivoConsulta": motivo_consulta,
            "sintomatologia": sintomatologia,
            "diagnostico": diagnostico,
        }

        if medicamentos:
            datos["medicamento"] = medicamentos

        if procedimientos:
            datos["procedimiento"] = procedimientos

        if ayuda_diagnostica:
            datos["ayudaDiagnostica"] = ayuda_diagnostica

        respuesta = requests.post(api_url, headers=headers, json=datos)

        print("Datos a enviar:", datos)

        if respuesta.status_code == 200:
            messages.add_message(request, messages.SUCCESS, "Se ha registrado la historia")
            return render(request, "medico.html", {"id": id})
        else:
            return render(request, "error.html", {"mensaje": response["message"]})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})

def buscarHistoria(request, id):
    try:
        ses = sesion.objects.get(id=id)
        headers = {"token": str(ses.token)}
        cedula = request.GET["cedula"]
        fecha = request.GET["fecha"]
        api_url = f"http://127.0.0.1:8081/historia/?cedula={cedula}&fecha={fecha}"

        respuesta = requests.get(api_url, headers=headers)
        respuesta.raise_for_status()

        response = respuesta.json()
        print(response)

        return render(request, 'mostrarHistoria.html', {'historia': response})

    except Exception as error:
        print(f"Error: {error}")
        return render(request, "error.html", {"mensaje": str(error)})

def renderEnfermera(request, id):
    try:
        ses = sesion.objects.get(id=id)
        if ses.rol == "Enfermera":
            return render(request, "Enfermera.html", {"id": id})
        else:
            return render(request, "error.html", {"mensaje": "Acceso denegado: Rol no válido"})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})
    
def registrarVisita(request, id):
    try:
        ses = sesion.objects.get(id=id)

        if ses.rol == "Enfermera":
            headers = {"token": str(ses.token)}
            api_url = "http://127.0.0.1:8081/registroVisita"

            cedula = request.GET.get("cedula")
            presion = request.GET.get("presion")
            temperatura = request.GET.get("temperatura")+" °C"
            pulso = request.GET.get("pulso")
            oxigeno = request.GET.get("oxigeno")

            listaMedicamentos = request.GET.get("medicamentosData", "[]")
            medicamentos = []

            if listaMedicamentos:
                try:
                    medicamentosP = json.loads(listaMedicamentos)
                    medicamentos = [v for v in medicamentosP.values()]
                except json.JSONDecodeError:
                    return render(request, "error.html", {"mensaje": "Error al decodificar la lista de medicamentos"})

            datos = {
                "cedula": cedula,
                "presion": presion,
                "temperatura": temperatura,
                "pulso": pulso,
                "oxigeno": oxigeno
            }

            if medicamentos:
                datos["medicamentos"] = medicamentos

            respuesta = requests.post(api_url, headers=headers, json=datos)
            print("Datos a enviar:", datos)
            print("Respuesta del servidor:", respuesta.text)

            if respuesta.status_code == 200:
                messages.add_message(request, messages.SUCCESS, "Se ha registrado la visita")
                print (messages.SUCCESS)
                return render(request, "Enfermera.html", {"id": id})
            else:
                try:
                    response_data = respuesta.json()
                    mensaje_error = response_data.get("message", "Error desconocido en el servidor")
                except json.JSONDecodeError:
                    mensaje_error = "Error al decodificar la respuesta del servidor"

                return render(request, "error.html", {"mensaje": mensaje_error})
    except sesion.DoesNotExist:
        return render(request, "error.html", {"mensaje": "No se encontró la sesión"})
    except Exception as error:
        return render(request, "error.html", {"mensaje": str(error)})          




