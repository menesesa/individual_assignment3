# -*- coding: utf-8 -*-
#%% 

from exercise1 import Product
from exercise1 import recalculate_quality

#potato2= potato.quality - 0.5
#cheese2 = cheese.quality - 2
#sandwich2 = sandwich.quality 
#pasta2 = pasta.quality -3
#banana2= banana.quality 

potato = Product("potato",9)
cheese = Product("cheese",5)
sandwich = Product("sandwich",7)
pasta = Product("pasta",1)
banana = Product("banana",8)

potato2 = Product("potato",8.5)
cheese2 = Product("cheese",3)
salad2 = Product("sandwich",7)
chips2 = Product("pasta",-2)
orange2 = Product("banana",8)

def test_recalculate_quality():
    assert potato.quality == 9
    assert cheese.quality == 5
    assert sandwich.quality == 7
    assert pasta.quality == 1
    assert banana.quality == 8
    

def test_recalculate_quality2():
    recalculate_quality(potato)
    assert potato.quality == 8.5
    recalculate_quality(cheese)
    assert cheese.quality == 3
    recalculate_quality(sandwich)
    assert sandwich.quality == 7
    recalculate_quality(pasta)
    assert pasta.quality == -2
    recalculate_quality(banana)
    assert banana.quality == 8


def test_recalculate_quality3():
    assert potato2.quality == 8.5
    assert cheese2.quality == 3
    assert sandwich.quality == 7
    assert pasta.quality == -2
    assert banana.quality == 8

def test_recalculate_quality4():
    recalculate_quality(potato2)
    assert potato2.quality == 8
    recalculate_quality(cheese2)
    assert cheese2.quality == 1
    recalculate_quality(salad2)
    assert salad2.quality == 7
    recalculate_quality(chips2)
    assert chips2.quality == -5
    recalculate_quality(orange2)
    assert orange2.quality == 8


