from pprint import pprint
def introspection_info(obj):
    info = {}
    info["Тип"] = type(obj).__name__       # Определение типа объекта
    try:                                    # Определение модуля, к которому относится объект
        info["Модуль"] = obj.__module__
    except AttributeError:
        info["Модуль"] = None
    attributes = []
    methods = []
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if callable(attr_value):            # Разделение атрибутов и методов
            methods.append(attr_name)
        else:
            attributes.append(attr_name)

    info["Атрибуты"] = attributes
    info["Методы"] = methods

    return info


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет, меня зовут {self.name}.")


person = Person("Васисуалий Череззаборногузадерищенко", 25)
info = introspection_info(person)
pprint(info)