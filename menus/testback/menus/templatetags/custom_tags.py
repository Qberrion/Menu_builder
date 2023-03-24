import django.utils.http

from django import template
from django.utils.html import escape, format_html


from ..models import Menu
import json

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name, cur_url='', level=0, html='', js=''):

    # первый импортируемый файл с бд требуется отформатировать
    if js == '':
        js = Menu.objects.get(name = menu_name).json
        dct = json.loads(js.replace("\n", '').replace("\r", ''))
    # при повторном вызове функции не делаем лишних действий
    else: dct = js

    # во избежании ограничений был выбран более экзотичный способ выбора активного пункта.
    # Пример: /menu/test1.test11.test111 (name через точку)

    cur_url = cur_url + '.' + dct["name"]

    #Обозначаем корневые элементы для выполнения стартовых действий и постобработки для правильного отображения (1)
    is_start = False
    if level == 0:
        is_start = True
        cur_url = cur_url[1:]
        html = f'<a href="{dct["name"]}"> {dct["title"]} </a>'
    level +=1

    # если элемент имеет дочерние вкладки, то...
    if 'sub_menus' in dct:
        for menu in dct['sub_menus']:
            try:

                # ...добавляем в конечный фрагмент html
                html += f'<a href="{cur_url+"."+menu["name"]}" style="margin-left: {50*level}px;"> {menu["title"]} </a>\n'
                # и если в ссылке присутствует этот элемент, то раскрываем его
                if (context["request"].path).split("/")[2].split(".")[level] == menu["name"] or context["request"].path == '/menu/0':
                    html = draw_menu(context, menu_name, cur_url, level, html, menu)
            except:
                pass
    # (1) постобработка для правильного отображения
    if is_start:
        html = format_html(html)
    return html
