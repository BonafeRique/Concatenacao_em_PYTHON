# -*- coding: utf-8 -*-
"""Formas de concatenar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TM9X8MWgwrl5UjPES2OZhNviQnWgHaoe
"""

var = 123
var2 = 'World'

print ("Hello to the",var2,var)

var = 123
var2 = 'World'

print ('Hello to the %s %d' %(var2,var))

var = 123
var2 = 'World'

print ('Hello to the word {} {}'.format(var2,var))

var = 123
var2 = 'World'

print ('Hello to the' + var2 + str(var))

var = 123
var2 = 'World'
print (f'Hello to the {var2} {var}')