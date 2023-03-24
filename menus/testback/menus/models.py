from django.db import models

json = '{\n ' \
       '  "title": "Уровень 1.0",\n ' \
       '  "name": "Test",\n ' \
       '  "sub_menus":\n ' \
       '  [\n ' \
       '    {\n ' \
       '      "title": "Уровень 1.1",\n ' \
       '      "name": "sub_test",\n ' \
       '      "sub_menus":\n ' \
       '      [\n ' \
       '        {\n ' \
       '          "title": "Уровень 1.1.1",\n ' \
       '          "name": "sub_sub_test",\n ' \
       '          "url": "#"\n ' \
       '        }\n ' \
       '      ]\n ' \
       '    },\n ' \
       '    {\n ' \
       '      "title": "Уровень 2",\n ' \
       '      "name": "sub_test",\n ' \
       '      "sub_menus":\n ' \
       '      [\n ' \
       '        {\n ' \
       '          "title": "Уровень 2.1",\n ' \
       '          "name": "sub_sub_test",\n ' \
       '          "url": "#"\n ' \
       '        }\n ' \
       '      ]\n ' \
       '    }\n ' \
       '  ]\n ' \
       '}'


class Menu(models.Model):
    name = models.CharField(max_length=50, default='test', unique=True)
    json = models.TextField(default=json)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
        ordering = ["id"]

    def __str__(self):
        return self.name
