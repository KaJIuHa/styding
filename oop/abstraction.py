from abc import ABC, abstractmethod


class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    
class Triangle(Shape):
    def method_1(self):
        print('Я метод 1 класса Triangle')
        
    def method_2(self):
        print('Я метод 2 класса Triangle')
    
    def method_3(self):
        print('Я метод 3 класса Triangle')
        
    def area(self):
        pass
        # print('Площадь треугольника')


class Square(Shape):
    def method_1(self):
        print('Я метод 1 класса Square')
        
    def method_2(self):
        print('Я метод 2 класса Square')
    
    def method_3(self):
        print('Я метод 3 класса Square')

    def area(self):
        print('Площадь квадрата')
    

if __name__ == '__main__':
    
    """
    
    """
    
    
    s = Square()
    t = Triangle()
    