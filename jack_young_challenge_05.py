# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:45:07 2024

@author: JackD
"""
def FileControl():
    
   movieFile = open('C:\\Users\\JackD\\OneDrive\\Desktop\\IS310\\FunWithFiles.txt')
   for movieName in movieFile:
       line=movieName
       print(movieName.strip())

    
   movieTitle=input('Enter your favourite movie : ')
    
   movieFile = open('C:\\Users\\JackD\\OneDrive\\Desktop\\IS310\\FunWithFiles.txt','a')
   if line.endswith('\n'):
       movieFile.write(movieTitle)
   else:
       movieFile.write('\n'+movieTitle)
       movieFile.close()

def main():
    FileControl()

main()