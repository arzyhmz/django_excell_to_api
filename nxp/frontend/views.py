from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from nxp.apps.formulir.models import Formulir

from .forms import FormulirForm


def index(request):
    form = FormulirForm(data=request.POST or None)
    context = {
        "form": form,
    }
    return TemplateResponse(request, "frontend/index.html", context)


@csrf_exempt
def post_formulir(request):
    if request.is_ajax and request.method == "POST":
        form = FormulirForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "sukses"}, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse({"error": "error gk jelas hehe"}, status=400)
