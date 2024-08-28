#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self._page_count = None #only updated with setter, or retrieved with getter

        self.page_count = page_count #uses setter
        self.title = title

    def get_page_count(self):
        print("gpc", self._page_count)
        return self._page_count
    
    def set_page_count(self, page_count):
         if isinstance(page_count, int):
            print("spc", page_count)
            self._page_count = page_count
         else:
            print("page_count must be an integer")

    # page_count is linked to gett and setter functions
    # calling mybook.page_count actually invokes functions
    # calling mybook.page_count invokes getter
    # combining mybook.page_count with = invokes setter
    page_count = property(get_page_count, set_page_count)
       

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



    
mybook = Book("mybook", 55)

# print(mybook)
print("pc 1", mybook.page_count)
# mybook.page_count = 100
# print("pc 2", mybook.page_count)
