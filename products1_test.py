# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:56:23 2018

@author: tmthi
"""
#%%
from products1 import Product
from products1 import recalculate_quality

potato = Product("potato", 18)
cheese = Product("cheese", 23)
beer = Product("beer", 10)
spoon = Product("spoon",9 )

def test_recalculate_quality_cheese():
    recalculate_quality(cheese)
    assert cheese.quality == 33
    
def test_recalculate_quality_potato():
    recalculate_quality(potato)
    assert potato.quality == 28
    
def test_reclaculate_quality_beer():
    recalculate_quality(beer)
    assert beer.quality == 6
    
def test_recalculate_quality_spoon():
    recalculate_quality(spoon)
    assert spoon.quality == 42
    
    