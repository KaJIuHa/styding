# class Animal(ParentClass):
class Animal:  # базовый = супер = родительский класс
    __FOOT = 4  # атрибут = свойство = поле
    __NAME = 'Unknown'  # атрибут = свойство = поле
    
    def __init__(self, name: str =__NAME, foot: int =__FOOT):  # конструктор класса
        self.name = name
        self.foot = foot
        
    def get_foot(self) -> int:
        return self.foot


class Dog(Animal):  # дочерний класс
    _ins = None
    
    def __new__(cls, *args, **kwargs):
        if cls._ins is None:
            cls._ins = super().__new__(cls)  # cls._ins = object.__new__(cls)
            return cls._ins
        raise AttributeError("Создать более чем одного экземпляра класса ЗАПРЕЩЕНО!")

    def __init__(self, name, foot):  # конструктор класса
        super().__init__(name, foot)  # --> Animal.__init__(self, name, foot)
    
    def get_foot(self) -> int:
        # print("Я фут из класса Dog")
        print(f"ID {id(self)} объекта{self}")
        return self.foot
    
    def __str__(self):
        return f'Имя: {self.name} Кол-во ног: {self.foot}'
    
    def __repr__(self):
        return f'{self} из Dog'
        

if __name__ == '__main__':
    # a_1 = Animal()  # объект(экземпляр) класса Animal  
    # print(type(a_1))  # тип объекта a_1
    # print(a_1.get_foot())
    
    
    # dog_1 = Dog('Recs', 6)
    # print(type(dog_1))  # тип объекта dog_1  # объект = экземпляр
    # print(dog_1.get_foot())
    
    # print(f"ID {id(dog_1)} объекта{dog_1}")
    # ----------------------------------------------
    dog_2 = Dog('Tuzik', 4)
    del dog_2
    Dog._ins = None
    dog_3: Dog = Dog('Recs', 4)
    print(dog_3)
    
    # dog_4 = Dog('Alabay', 4)  # AttributeError 
    
    greeting: str = 'Привет!'
