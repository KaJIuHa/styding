class Human:
    
    def say(self):
        print("Я говорю")
    
    def think(self):
        print("Я думаю")
    
    def walk(self):
        print("Я иду")
        

class Student(Human):
    
    def grades(self):
        print("Мои оценки")
        
    def think(self):
        print("Я решаю задачи")
 
 
class Employee(Human):
    
    def post(self):
        print("Моя должность")
 
 
 
if __name__ == '__main__':
    vasya = Human()
    petya = Human()
    
    vasya.say()
    petya.walk()

    tolya = Student()
    tolya.think()
    tolya.grades()
    
    julia = Employee()
    julia.walk()
    julia.post()
