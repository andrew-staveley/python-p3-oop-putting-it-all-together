#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size if (type(size) is (int)) else print("size must be an integer")
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"