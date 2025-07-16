class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate
    
    def sleep(self,hours):
        if not isinstance(hours, (int, float)):
            raise ValueError('Please enter numbers only')
        
        if hours == 7:
            self.mood='Happy'
        elif hours < 7:
            self.mood='Tired'
        else:
            self.mood='Lazy'
        
    def eat(self,meals):
        if not isinstance(meals, (int)):
            raise ValueError('Please enter numbers only')
        
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            raise ValueError("Meals should be 1, 2, or 3.")


    def buy(self,items):
        if not isinstance(items, int):
            raise ValueError("Please enter numbers only")
        
        cost=items*10
        self.money-=cost

    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Money: {self.money}\n"
                f"Mood: {self.mood}\n"
                f"Health Rate: {self.healthRate}%")
