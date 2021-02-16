# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:37:45 2021

@author: User
"""

# =============================================================================
# def say_hello(ism):
#     print(f"Assalomu aleykum {ism.title()}")
# say_hello('sardor')
# =============================================================================

# =============================================================================
# def say_hello(ism):
#     """"Bu funksiya foydalanuvhcidan ismini sorab,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu aleykum {ism.title()}")
# print("Ismingizni kiritng : ")
# say_hello(ism=input())
# =============================================================================

# =============================================================================
# def say_hello(ism):
#     
#     """Bu funksiya foydalanuvhcidan ismini sorab,
#     unga salom beruvchi funksiya"""
# #consoleda print(say_hello.__doc__) ni kiritilsa  yuqoridagi yozuv(docstring) chiqadi
#     print(f"Assalomu aleykum {ism.title()}")
# say_hello('sardor')
# =============================================================================

# =============================================================================
# def info(ism,familiya):
#     print(f"Foydalanuvchining ismi - {ism.title()}")
#     print(f"Foydalanuvchinig familiyasi - {familiya.title()}")
# print("Foydalanuvchining ismi va familiyasini kiriting :")
# info(ism=input() , familiya=input())
# =============================================================================

# =============================================================================
# def info(t_yil,now = 2021):
#     print(f"Siz {now-t_yil} yoshdasiz")
# print("Foydalanuvchining ismi va familiyasini kiriting :")
# info(1996,2021)
# =============================================================================

# =============================================================================
# def yosh_hisobla(t_yil,now = 2021):
#     print(f"Siz {now-t_yil} yoshdasiz")
# print("Foydalanuvchining ismi va familiyasini kiriting :")
# t_yil = int(input('tugilgan yilingizni kiriting : '))
# yosh_hisobla(t_yil)
# =============================================================================

#AMALIYOT

# =============================================================================
# def yosh_hisobla(ism,t_yil,now = 2021):
#     print(f"{ism.title()} siz {now-t_yil} yoshdasiz")
# ism = input("Ismingizni kiriting : ")
# t_yil = int(input('tugilgan yilingizni kiriting : '))
# yosh_hisobla(ism,t_yil)
# =============================================================================

# =============================================================================
# def kvadrat(son1,son2):
#     if son1>son2:
#         print(f"{son1} katta son.")
#     elif son1<son2:
#         print(f"{son2} katta son.")
#     else :
#         print(f"{son1} {son2} ga teng.")
# son1 = int(input("1-sonni kiriting : "))
# son2 = int(input("2-sonni kiriting : "))
# kvadrat(son1,son2)    
# =============================================================================

# =============================================================================
# def kvadrat(x,y):
#    print(f"{x} ning {y} chi darajasi - {x**y} ga teng.")
# x = int(input("x-sonni kiriting : "))
# y = int(input("y-sonni kiriting : "))
# kvadrat(x,y)  
# =============================================================================

# =============================================================================
# def kvadrat(x,y=2):
#    print(f"{x} ning {y} chi darajasi - {x**y} ga teng.")
# x = int(input("x-sonni kiriting : "))
# kvadrat(x,2)
# =============================================================================
#WHILE ORQALI ISHLANGANI 
# =============================================================================
# def bolish(x):
#     a=2
#     while a<=10:
#             if x%a==0:
#                 print(f"{x} ,{a} ga qoldiqsiz bolinadi")
#             a +=1
# x = int(input("x-sonni kiriting : "))
# 
# bolish(x)
# =============================================================================

def bolish(x):
    for a in range(2,11):
        if not x%a:
          print(f"{x} ,{a} ga qoldiqsiz bolinadi")
            
x = int(input('Sonni kiriting : '))
bolish(x)








