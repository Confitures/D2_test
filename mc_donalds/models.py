from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    pass


class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:  # если завершён, возвращаем разность объектов
            return (self.time_out - self.time_in).total_seconds() // 60
        else:  # если ещё нет, то сколько длится выполнение
            return (datetime.now(timezone.utc) - self.time_in).total_seconds() // 60

    pass


director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]


class Staff(models.Model):
    full_name = models.CharField(max_length=255)  # ...CharField(max_length=255, null = True)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)
    labor_contract = models.IntegerField()

    def get_last_name(self):
        return self.full_name.split()[0]


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()

    pass
# Create your models here.


# vp = Products.objects.create(name = "Витая пара (3м)", price = 993)
# keyboard = Product.object.create(name = "Клавиатура", price = 1060)
#
# product_1 = Product(name = "Витая пара (3 м)", price = 993.0)
# product_1.save()
#
# product_2 = Product.objects.create(name = "Клавиатура", price = 1060.0)


# cashier1 = Staff.objects.create(full_name = "Иванов Иван Иванович", position = "CA", labor_contract = 1754)
# cashier2 = Staff.objects.create(full_name = "Петров Петр Петрович",
#                                 position = "CA",
#                                 labor_contract = 4355)
# direct = Staff.objects.create(full_name = "Максимов Максим Максимович",
#                                 position = "DI",
#                                 labor_contract = 1254)



