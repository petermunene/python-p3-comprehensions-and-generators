#!/usr/bin/env python3

def return_evens(num_list):
    even=[]
    for num in num_list:
        if(num%2==0):
            even.append(num)
    return even
    pass

def make_exclamation(sentence_list):
    lines=[]
    for sentence in sentence_list:
        lines.append(sentence + "!")
    return lines
    pass