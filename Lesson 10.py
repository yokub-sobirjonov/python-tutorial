# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:19:23 2021

@author: User
"""
#avtos = ['lacetti','audi','chevrolet','toyota','bmw']

#for av in avtos:
#    if av == 'bmw' :
#        print(av.upper())
#    else:
#        print(av.title())
 
#ism = input('Ismingizni kiritig \n')    
#if ism.lower() != 'ali' :
#        print(f' Salom {ism.lower()} uzur biz izlagan inson Ali emassiz')
#else :
#        print('Salom Ali , Ahvollaringiz qalay?')
        
#javob = float(input())
#if javob != 71:
#    print("javob xato")
    
#yosh = int(input('yoshingizni kiriting : '))
#if yosh >= 18 :
#    print('Kirishingiz mumkin')
#else :
#    print('kirish mumkin emas')    

#login = input("Loginni kiriting : ")
#if len(login) <= 5:
#    print('login uzunligi 5 tadan ortiq bolishi kerak')

#tug_yilingiz = int(input("Tugilgan yilingizni kiriting : "))
#if 2021-tug_yilingiz < 18:
#    print("Siz {} yoshdasiz, 18 yoshdan kichiklar kirishi mumkin emas".format(2021-tug_yilingiz))
#else:
#    print(" Xush kelibsiz")

#ism1 = "Anvar"
#ism2 = 'Sarvar'
#print("ism1>ism2") if len(ism1)>len(ism2) else print('ism1<ism2')

#AMALIYOT

#cars = ['nexia','lacetti','bmw','audi','mercedes','toyota']
#for carname in cars:
#    if  carname != 'audi': 
#        print(carname.upper())
#    else :
#       print(carname.title())
    
#logins = ['Yoqub','Richard','john','Amin','Edison','Mark']
#login = input('Loginingini kiriting : ')
#if login == 'Admin' :
#       print('Salom Admin , Xush kelibiz, foydalanuvchilar royxatii korasizmi ?')
#       answer = input('xa yoki yoq ? \n')
#       if answer.lower() == 'xa' :
#                   print(logins)
#else :
#       print(f"Xush kelibsiz {login} ")

#son1 = input("Sonlarni kiriting : ") 
#son2 = input("Sonlarni kiriting : ")
#if son1 == son2:
#    print('Ikki son bir biriga teng ekan')
#else :
#    print('bu sonlar bir biriga teng emas')    

#son = int(input('Sonni kiriting : '))
#if son > 0:
#    print("{} Bu musbat son".format(son))
#if son < 0 :
#    print("{} Bu manfiy son".format(son))

son = int(input('Sonni kiriting : '))
if son > 0:
    print(f"bu sonning kvadrati {son**(1/2)}")
if son < 0 :
    print("Musbat son kiriting")
    