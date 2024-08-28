#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size):
        self.brand = brand
        if type(size) == int:
            self.size = size
        else:
            print("size must be an integer")

    
    def cobble(self, condition):
        self.condition = new


myshoe = Shoe("nike", 8)
myshoe.cobble()
print(myshoe.condition)