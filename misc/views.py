from django.http import HttpResponse
from django.shortcuts import render_to_response
from coffin.shortcuts import render_to_response as jinja_render_to_response
from django.template.context import RequestContext
from django.conf import settings


from tuitter.models import Tuit


def index(request):
    page = int(request.GET.get('page', 1))
    recent_tuits = list(Tuit.objects.select_related('user').all().order_by("-added")[(page-1)*settings.TUITS_PER_PAGE:page*settings.TUITS_PER_PAGE])

    return render_to_response("index.html", {"recent_tuits": recent_tuits}, context_instance=RequestContext(request))


def index_jinja2(request):
    page = int(request.GET.get('page', 1))
    recent_tuits = list(Tuit.objects.select_related('user').all().order_by("-added")[(page-1)*settings.TUITS_PER_PAGE:page*settings.TUITS_PER_PAGE])

    return jinja_render_to_response("index_jinja2.html", {"recent_tuits": recent_tuits}, context_instance=RequestContext(request))


def index_wo_user(request):
    page = int(request.GET.get('page', 1))
    recent_tuits = list(Tuit.objects.select_related('user').all().order_by("-added")[(page-1)*settings.TUITS_PER_PAGE:page*settings.TUITS_PER_PAGE])

    return render_to_response("index_wo_user.html", {"recent_tuits": recent_tuits}, context_instance=RequestContext(request))


def index_wo_user_jinja2(request):
    page = int(request.GET.get('page', 1))
    recent_tuits = list(Tuit.objects.select_related('user').all().order_by("-added")[(page-1)*settings.TUITS_PER_PAGE:page*settings.TUITS_PER_PAGE])

    return jinja_render_to_response("index_wo_user_jinja2.html", {"recent_tuits": recent_tuits}, context_instance=RequestContext(request))


def return_42(request):
    return HttpResponse('42')
