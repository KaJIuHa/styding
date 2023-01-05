class Player:
    
    # _ - запрет на уровне согласения
    
    # __ - полный запрет на использование метода или атрибута класса
    
    __SCORE = 0  # атрибут = поле = свойство класса
     
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    
    def show(self):
        print(f"Имя: {self.name} Очки: {self.__score}")
        
        
    # Геттеры  (метод получения)
    # Сеттеры (метод установки)


if __name__ == '__main__':
    p1 = Player('Игрок 1', 100)
    
    p1.show()
    #p1.__score = 200
    p1.show()
    Player.__score
    
    # Player.__SCORE = 90
    
    # print(p1.__SCORE)
