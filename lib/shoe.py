#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size, condition = "old"):

        self._size = None

        self.condition = condition
        self.brand = brand
        self.size = size

        

    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)
    
    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")

# myshoe = Shoe("nike", 3, "old")
# myshoe.size = 3
# # myshoe.cobble()
# # print(myshoe.size)
# print(myshoe.size)

