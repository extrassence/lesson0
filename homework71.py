class Product:

    def __init__(self, name, wgt, catg):
        self.name = name
        self.weight = wgt
        self.category = catg

    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        catalog = ''
        self.file = open(self._Shop__file_name)
        catalog = self.file.read()
        self.file.close()
        return catalog

    def add(self, *products):
        catalog = self.get_products()
        self.file = open(self._Shop__file_name, 'a')
        for i in products:
            if catalog.count(str(i)) > 0:
                print(f'Поставка {str(i)} уже проведена')
            else:
                self.file.write(str(i)+'\n')
        self.file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
