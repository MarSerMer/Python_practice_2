# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from seminar_10.sem_10_task_6_animals_again import Fish, Bird, Cat

class Fabric:
    def __init__(self,type_of_animal:str,name:str, color:str, size:float, unique):
        self.type = type_of_animal.lower()
        self.name = name
        self.color = color
        self.size = size
        self.unique = unique
    def make_any_animal(self):
        if self.type == 'fish':
            fish = Fish(self.name,self.color,self.size,self.unique)
            return fish
        elif self.type == 'bird':
            bird = Bird(self.name,self.color,self.size,self.unique)
            return bird
        elif self.type == 'cat':
            cat = Cat(self.name,self.color,self.size,self.unique)
            return cat
        else:
            print('That did not work')

fabric = Fabric('bird','soika','grey',12.22,'forest')
bird_from_fabric = fabric.make_any_animal()
print(type(bird_from_fabric))
bird_from_fabric.show_unique()