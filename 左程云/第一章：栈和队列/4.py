"""
猫狗队列：
宠物、狗和猫的类如下：
class Pet:
    def __init__(self, type):
        self.type = type
    def get_pet_type(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super().__init__('dog')

class Cat(Pet):
    def __init__(self):
        super().__init__('cat')

实现一种猫狗队列的结构，要求如下：
1）用户可以调用add方法将cat类或者dog类的实例放入队列中
2）用户可以调用pollAll方法，将队列中的所有实例按照进队列的先后顺序依次弹出
3）用户可以调用pollDog方法，将队列中dog类的实例按照进队列的先后顺序依次弹出
4）用户可以调用pollCat方法，将队列中cat类的实例按照队列的先后顺序依次弹出
5）用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例
6）用户可以调用isDogEmpty方法，检查队列中是否有dog类的实例
7）用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例

思路：使用两个队列，一个来保存猫，另外一个来保存狗。同时实现一个类来记录猫狗加入队列的先后
"""

class Pet:
    def __init__(self, type):
        self.type = type
    def get_pet_type(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super().__init__('dog')

class Cat(Pet):
    def __init__(self):
        super().__init__('cat')


class CatDogCount:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count 

class CatDogQueue:
    def __init__(self):
        self.cat_queue = []
        self.dog_queue = []
    
    def isEmpty(self):
        return len(self.cat_queue)==0 and len(self.dog_queue)==0
    
    def isDogEmpty(self):
        return len(self.dog_queue) == 0
    
    def isCatEmpty(self):
        return len(self.cat_queue) == 0
    
    def add(self, pet):
        count = len(self.cat_queue) + len(self.dog_queue)
        if pet == 'dog':
            self.dog_queue.append(CatDogCount(pet, count))
        else:
            self.cat_queue.append(CatDogCount(pet, count))
    
    def pollDog(self):
        if len(self.dog_queue) == 0:
            return None
        return self.dog_queue.pop(0).pet
    
    def pollCat(self):
        if len(self.cat_queue) == 0:
            return None
        return self.cat_queue.pop(0).pet

    
    def pollAll(self):
        if self.isEmpty():
            return None
        if self.isDogEmpty():
            return self.cat_queue.pop(0).pet
        if self.isCatEmpty():
            return self.dog_queue.pop(0).pet
        
        if self.cat_queue[0].count < self.dog_queue[0].count:
            return self.cat_queue[0].pet
        else:
            return self.dog_queue[0].pet

        