#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size, condition = "old"):
        self.condition = condition
        self.brand = brand
        if type(size) == int:
            self.size = size
        else:
            print("size must be an integer")

    
    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")

myshoe = Shoe("nike", 8, "old")
myshoe.cobble()
print(myshoe.condition)