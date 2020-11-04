'''
Created Date: Friday September 4th 2020
Author: skaushikk
-----
Last Modified:
Modified By:
-----
Copyright (c) 2020 Your Company
'''

def get_hash(key):
    h=0
    for char in key:
        h+=ord(char)
    return h, h%100