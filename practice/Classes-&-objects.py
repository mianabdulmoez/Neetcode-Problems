class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def details(self):
        self.name = "Honda"
        self.model = 2010
    
    def display(self):
        return f"The car is {self.name} and the model is {self.model}."
    

# Objects

obj1 = Car("Nissan", 2010)
print(obj1.display())