# -*- coding: utf-8 -*-

#%%

#Exercise 1 

# 1. 2 points. Imagine you’re creating an application for handling the stock
# of a small shop, and controlling when things go bad in the warehouse.

# Given the following class:

# We have a function that calculates the degrading quality of different
# products in a shop.
# Create all the tests you find meaningful for the following function.

class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality


def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
            
            
potato = Product("potato",9)
cheese = Product("cheese",5)
sandwich = Product("sandwich",7)
pasta = Product("pasta",1)
banana = Product("banana",8)
    
product_lst={Product("potato",9),Product("cheese",5),
            Product("sandwich",7), Product("pasta",1),
            Product("banana",8)}

