from django.db import models

from menu.models import Drink

class Order(models.Model):
    #drink(메뉴) stock(몇개) cup(크기) ice(얼음얼마나) suger(설탕얼마나) pearl(펄) price(가격)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='order')
    stock = models.IntegerField(default=1)
    cup = models.IntegerField() #0:레귤러 1:점보
    ice = models.IntegerField(default=100) #0, 50, 100, 150%
    suger = models.IntegerField(default=100) #0, 50, 100, 150%
    # pearl은 나중에 만들것이다.!
    price = models.IntegerField()

    def __str__(self):
        return f'음료 : {self.drink}, 개수 : {self.stock}, 컵사이즈 : {self.cup}, 얼음량 : {self.ice}, 당도 : {self.suger}, 가격 : {self.price}'