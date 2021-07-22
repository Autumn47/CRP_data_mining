# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:54:30 2021

@author: Autumn47
"""
# read BLAST file
BLAST = input("BLAST File name: ")
file = open(BLAST, "r")

# extract out the all the peptide names from BLAST file and put them in a list
peptide_names = []
for row in file:
    count = 0
    if row[0] == ">":
        for char in row:
            count += 1
            if char.isspace():
                peptide_names.append(row[1:count-1] )
                break
            
# close and reopen BLAST file to read again from the beginning
file.close() 
file = open(BLAST, "r")

# open EXCEL file (The full file to check)
EXCEL_file = open(r"complete_list_CRP.txt","r")

# open another file for collecting non-duplicates
non_duplicates = open("non-duplicates.txt", "w")

# declaring variables
info =""
list_not_found=[]
fullinfo=""
fullinfolist=[]
count =0

# Turn EXCEL file(object) into EXCEL_file(string), arrange them line-by-line
for i in EXCEL_file:
    info += str(i)
    info+='|n'

# Create a list of peptide names of the non-duplicates (but lack species name and full sequence)   
for i in peptide_names:
    if info.find(i)==-1:
        non_duplicates.write(i+'\n')
        #list_not_found.append(i)

#close all files
file.close()        
EXCEL_file.close()
non_duplicates.close() 
  









        
