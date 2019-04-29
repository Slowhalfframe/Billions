from django.shortcuts import render
from django.http import JsonResponse
from . import models

# Create your views here.


def index(request):
    nav_list = models.Nav.objects.filter(parent=None)
    logo = models.Logo.objects.all().first()
    topbox = models.TopBox.objects.all().first()
    footer = models.Footer.objects.all().first()
    friends_link = models.FriendsLink.objects.all()
    res = {
        'nav_list': nav_list, 'logo': logo,
        'topbox': topbox, 'footer': footer,
        'friends_link': friends_link,
    }
    return render(request, 'common/index.html', res)
    # return render(request, 'common/index.html', {'nav_list': nav_list})


def get_child_menu(request):
    ret = {'code': 0}
    try:
        id = request.GET['id']
        child_menu = models.Nav.objects.filter(parent=id)
        data = []
        for c in child_menu:
            menu = {
                'name':c.name,
                'link':c.link,
            }
            data.append(menu)
        ret['data'] = data
    except Exception as e:
        print(e)
        ret['code'] = -3
    return JsonResponse(ret)

