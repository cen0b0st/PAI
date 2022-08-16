from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import CierreMensualInsumo, CierreMensual, Insumos, UnidadMedida, Categoria, Cargo, SubDepartamento, Usuario, Formulariosr, Departamento, Seccion
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class Maestroins(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        insumos = Insumos.objects.all()
        unidades = UnidadMedida.objects.all()
        categorias = Categoria.objects.all()

        ctx = {
            'insumos': insumos,
            'unidades': unidades,
            'categorias': categorias,
        }
        return render(request, 'frontweb/maestroins.html', ctx)
    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'enviar_cierre':
            insid = request.POST['id']
            insid = insid.replace(',', '.')
            insid = insid.split('_')
            del insid[0]
            idcierremensual = len(CierreMensual.objects.all()) + 1
            fecha = datetime.today()
            #cierremensual = CierreMensual.objects.create(id_cierre_mensual = idcierremensual, fecha_cierre_mensual = fecha, activo = 1)
            #cierremensual.save()
            datos = []
            for i in insid:
                datos.append(i.split('-'))
                print(i)
            for i in datos:
                idcierremensualinsumo = len(CierreMensualInsumo.objects.all()) + 1
                saldo = i[1]
                precio = i[2]
                fkcierremensual = CierreMensual.objects.get(id_cierre_mensual = idcierremensual)
                fkinsumo = Insumos.objects.get(id_insumos = i[0])
                fkcategoria = Categoria.objects.get(id_categoria = i[3])
                #cierremensualinsumo = CierreMensualInsumo.objects.create(id_cierre_mensual_insumo = idcierremensualinsumo, saldo= saldo, precio = precio, estado = 1, fk_id_cierre_mensual = fkcierremensual, fk_id_insumos = fkinsumo, fk_id_categoria = fkcategoria)
                #cierremensualinsumo.save()
            return JsonResponse(insid, safe=False)



class Formsr(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        cargo = Cargo.objects.all().order_by('nombre_cargo')
        dpto = Departamento.objects.all().order_by('nombre_dpto')
        fecha = datetime.today().strftime('%d-%m-%Y')
        nfolio = datetime.today().strftime('%Y')
        idfolio = len(Formulariosr.objects.all()) + 1

        letra = ''
        # ELIJE LA LETRA
        if idfolio < 1000:
            letra = 'A'
        elif idfolio < 2000 and idfolio > 1000:
            letra = 'B'
        elif idfolio < 3000 and idfolio > 2000:
            letra = 'C'
        elif idfolio < 4000 and idfolio > 3000:
            letra = 'D'

        # PONE LA CANTIDAD DE 0 LUEGO DE LA LETRA
        if idfolio < 10:
            cfolio = letra + '00' + str(idfolio) + '/' + str(nfolio)
        elif idfolio < 100:
            cfolio = letra + '0' + str(idfolio) + '/' + str(nfolio)
        elif idfolio < 1000:
            cfolio = letra + str(idfolio) + '/' + str(nfolio)

        ctx = {
            'cargo': cargo,
            'fecha': fecha,
            'dpto': dpto,
            'cfolio': cfolio,
        }
        return render(request, 'frontweb/formsr.html', ctx)

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'search_sdpto_id':
            data = []
            for i in SubDepartamento.objects.filter(fk_id_dpto=request.POST['id']).order_by('nombre_sub_dpto'):
                data.append({'id': i.id_sub_dpto, 'name': i.nombre_sub_dpto})
            return JsonResponse(data, safe=False)
        elif request.POST['action'] == 'search_seccion_id':
            data = []
            for i in Seccion.objects.filter(fk_id_sub_dpto=request.POST['id']).order_by('nombre_seccion'):
                data.append({'id': i.id_seccion, 'name': i.nombre_seccion})
            return JsonResponse(data, safe=False)


def registrosr(request):
    idfolio = len(Formulariosr.objects.all()) + 1
    pkfolio = request.POST['folio']
    fecha = datetime.today()
    tipoform = request.POST.getlist('tipoform')
    anexo = request.POST['anexo']
    email = request.POST['email']
    comentario = request.POST['comentario']

    cargo = request.POST.getlist('cargo')[0]
    dpto = request.POST.getlist('depto')[0]
    subdpto = request.POST.getlist('subdpto')[0]
    seccion = request.POST.getlist('section')[0]

    carg = Cargo.objects.get(id_cargo=cargo)
    departamento = Departamento.objects.get(id_dpto=dpto)
    subdepartamento = SubDepartamento.objects.get(id_sub_dpto=subdpto)
    section = Seccion.objects.get(id_seccion=seccion)

    formulariosr = Formulariosr.objects.create(id_formulariosr=idfolio, pk_foliosr=pkfolio, tipo_formulario=tipoform, fecha_ingreso=fecha, fecha_respuesta=None,
                                               anexo=anexo, email=email, comentario=comentario, activo=1, fk_id_cargo=carg, fk_id_dpto=departamento, fk_id_sub_dpto=subdepartamento, fk_id_seccion=section)
    formulariosr.save()

    return redirect('home:formulariosr')


def login(request):
    return render(request, 'frontweb/login.html')


def ingresar(request):
    rut_ingreso = request.POST['rut']
    paswd = request.POST['paswd']
    usuario = Usuario.objects.filter(
        rut=rut_ingreso).filter(password=paswd).exists()
    if usuario == True:
        return redirect('home:formulariosr')
    else:
        return redirect('home:login')
