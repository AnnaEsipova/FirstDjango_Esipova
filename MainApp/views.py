from django.http import HttpResponse, HttpResponseNotFound 
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


author = {
    'name': 'Анна',
    'middlename': 'Дмитриевна',
    'surname': 'Есипова',
    'phone': '8-927-018-30-45',
    'email': 'anna.esipova@moex.com'
}


# Create your views here.
def home(request):
    context = {
        "name": 'Anna Esipova',
        "email": 'my_mail@mail.ru'
    }
    return render(request, "index.html", context)


def about(request):
    text = f"""Имя: <b>{author.get('name')}</b></br>
            Отчество: <b>{author.get('middlename')}</b></br>
            Фамилия: <b>{author.get('surname')}</b></br>
            Телефон: <b>{author.get('phone')}</b></br>
            email: <b>{author.get('email')}</b></br>"""
    return HttpResponse(text)


def item(request, id):
    try:
        item = Item.objects.get(id = id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Item with id = {id} not found')
    else:
        context = {
            'item': item
        }
        return render(request, "item.html", context)
 
    # for item_num in items:
    #     if item_id == item_num['id']:
    #         return render(request, "item.html", item_num)
    # return HttpResponseNotFound(f'Item with id = {item_id} not found')

        

def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)

