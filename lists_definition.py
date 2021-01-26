# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:11:12 2021

@author: Dina
"""
class DefineCorpus():


    app_dic={"i am": "i'm", "you'll": "you will","don't":"do not", "we'll":"we will", "can't":"cannot", "you've": "you have"}
    synonyms={'cut out': 'clip', 'products': 'items', 'easiest':'best'}
    exclude=['the', 'to', 'you', 'any', 'will','do','just', 'and','we', 'a', 'have', 'for', 'is', 'i', 'd']

    punct_remove=r"[-()\"#/@;:<>{}=~|.?,]"  