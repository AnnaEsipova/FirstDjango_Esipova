from django.http import HttpResponse, HttpResponseNotFound 
from django.shortcuts import render


author = {
    'name': 'Анна',
    'middlename': 'Дмитриевна',
    'surname': 'Есипова',
    'phone': '8-927-018-30-45',
    'email': 'anna.esipova@moex.com'
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

# Create your views here.
def home(request):
    text = """<h1>"Изучаем django"</h1>
        <strong>Автор</strong>: <i>Esipova A.D.</i>"""
    return HttpResponse(text)

def about(request):
    text = f"""Имя: <b>{author.get('name')}</b></br>
            Отчество: <b>{author.get('middlename')}</b></br>
            Фамилия: <b>{author.get('surname')}</b></br>
            Телефон: <b>{author.get('phone')}</b></br>
            email: <b>{author.get('email')}</b></br>"""
    return HttpResponse(text)

def item(request, item_id):
    for item_num in items:
        if item_id == item_num['id']:
            inf = f"""<b>{item_num.get('name')} {item_num.get('quantity')}</b></br>
            <a href='/items'>Back</a>
            """
            return HttpResponse(inf)
    return HttpResponseNotFound(f'Item whit id = {item_id} not found')


def items_list(request):
    result = "<h2>Список товаров</h2> <ol>"
    for item_num in items:
       result += f"<li><a href='/item/{item_num['id']}'>{item_num.get('name')}</a></li>"
    return HttpResponse(result + "</ol>")

