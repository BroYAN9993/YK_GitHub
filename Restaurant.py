# -*- coding: utf-8 -*-
class Restaurant(object):
    """餐馆对象的模拟"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆的名字和菜色"""
        print self.restaurant_name.title() + ' is a restaurant that sells ' + self.cuisine_type + '.'

    def open_restaurant(self):
        """打印餐馆开始营业"""
        print self.restaurant_name.title() + ' is opening now!'

    def set_number_served(self, nums):
        """设置并打印已服务客人数量"""
        self.number_served = nums
        print 'This restaurant has served ' + self.number_served + ' people.'

    def increment_number_served(self, nums):
        """增加某个数量的已服务人数"""
        self.number_served += nums

class Flavor(object):
    """模拟冰淇淋口味的类"""
    def __init__(self, flavors=['original']):
        self.flavors = flavors

    def remove_repeated_flavors(self):
        """去除重复的口味"""
        i = 1
        while i < len(self.flavors):
            if self.flavors[i] == self.flavors[i-1]:
                self.flavors.pop(i)
            else:
                i += 1
        return self.flavors

    def add_flavors(self, flavors):
        """增加几种冰淇淋口味"""
        self.flavors.extend(flavors)
        self.flavors.sort()
        self.remove_repeated_flavors()

    def set_flavors(self, flavors):
        """设置新的冰淇淋口味清单"""
        self.flavors = flavors
        self.flavors.sort()
        self.remove_repeated_flavors()
        print 'This ice-cream stand has a new menu:'
        for i in self.flavors:
            print i.title()

    def show_flavors(self):
        """打印所有的冰淇淋口味"""
        print 'There are different ice-cream flavors you can choice:'
        for i in self.flavors:
            print i.title()

  
class IceCreamStand(Restaurant):
    """冰淇淋店，一个继承自Restaurant的子类"""
    def __init__(self, restaurant_name, cuisine_type='ice-cream'):
        """
        初始化父类的属性
        子类IceCreamStand的菜色固定
        只有ice-cream，将其设定为默认属性
        另外需要创建一个Flavor类
        用以存储冰淇淋的口味
        """
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = Flavor()

"""
my_restaurant = Restaurant('buger king', 'hambuger')
print my_restaurant.restaurant_name
print my_restaurant.cuisine_type
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
"""
my_DQ = IceCreamStand('dairy queen')
my_DQ.flavors.set_flavors(['apple', 'banana', 'lemon', 'strawberry'])
my_DQ.flavors.add_flavors(['blueberry', 'oreo', 'strawberry'])
my_DQ.flavors.show_flavors()
