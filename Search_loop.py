# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 15:16:31 2021

@author: Autumn47
"""

import pyperclip

go_on = True
while(go_on == True):
    
    def Search():

#define variables
        Cysteine_amount = 6
        max_length =  40
        data = []
        combined = ""
        new_data = []
        arranged = []

#Clean up data into a string: accept sequences containing new lines, whitespaces, "-", then copy the cleaned data onto clipboard
        data.append(input(""))
        for i in data :
            combined += str(i)
            combined = combined.replace("\n","")
            combined = combined.replace(" ","")
            combined = combined.replace("-","")
            pyperclip.copy(combined)

#Slicing data into max length for CRP in a frameshift manner, append the whole input sequence if the length of input sequence is less than max_length
        for i in range(len(combined) - max_length):
            if len(combined[i:i+max_length]) == max_length:
                new_data.append(combined[i:i+max_length])
        if len(new_data) == 0:
            new_data.append(combined)

#Check first letter for "C" and check for last item in list (because the start may not start with C), then iterate the list, append to list if cysteine counted reached var Cysteine_amount 
        for i in new_data:
            count = 0
            distance = 0
            first_C = 0

            if i[0] == "C" or i == new_data[-1]:
                for j in i:
                    distance += 1
                    if j == "C":
                        count += 1
                        if count == Cysteine_amount:
                            if i not in arranged:
                                first_C = i.find("C")
                                arranged.append(i[first_C:distance])              
        return(arranged)

#Run Search()
    arranged = Search()

#Print out results in a more readable way
    if len(arranged) == 0:
        print("\nCRP not found")
    else:
        print("\nCRP Search Result: \n")
        for i in arranged:
            print(i)
            pyperclip.copy(i)
