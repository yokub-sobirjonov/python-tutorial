# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:38:59 2021

@author: User
"""
# =============================================================================
# student = {'name':'tolib',
#            'age':23,
#            'adress':'namangsn viloyati',
#            'malumoti':'oliy',
#            'kasbi':'jurnalist'}
# print(student.items())
# =============================================================================

# =============================================================================
# student = {'name':'tolib',
#            'age':23,
#            'adress':'namangsn viloyati',
#            'malumoti':'oliy',
#            'kasbi':'jurnalist'}
# for key,value in student.items():
#     print(f"key : {key}")
#     print(f"value : {value} \n-----------------------")
# =============================================================================

# =============================================================================
# phones = {'Asror':'redmi 9C',
#           'Abror':'oppo find x',
#           'Axror':'iphone xs max',
#           'Toxir':'samsung a51'}
# for key, value in phones.items():
#     print(f"{key}ning telefoni {value}")
# =============================================================================

# =============================================================================
# phones = {'Asror':'Wesminister talabasi',
#           'Abror':'Cambridge talabasi',
#           'Axror':'TATU talabasi',
#           'Toxir':'NamSU talabasi'}
# print(phones.keys())
# =============================================================================

# =============================================================================
# students = {'asror':'Wesminister talabasi',
#           'abror':'Cambridge talabasi',
#           'axror':'TATU talabasi',
#           'toxir':'NamSU talabasi'}
# for student in students.keys():
#     print(student.title())
# =============================================================================

# =============================================================================
# students = {'asror':'Wesminister talabasi',
#           'abror':'Cambridge talabasi',
#           'abdulloh':'TATU talabasi',
#           'toxir':'NamSU talabasi'}
# print('Talaba bolgan abiturientlar royhati : ')
# for student in students.keys(): #bu yerda keys() ni ishlatmasa ham natija chiqaveradi
#     print(student.title())
# =============================================================================

# =============================================================================
# mahsulotlar = {'olcha':2500,
#                'anor':5000,
#                'gilos':6000,
#                'orik':11000,
#                'banan':15000,
#                'olma':4000}
# bozorlik = ['olma','banan','mandarin','gilos']
# for mahsulot in mahsulotlar :
#     if mahsulot in bozorlik :
#         print(f" {mahsulot.title()} ning narxi {mahsulotlar[mahsulot]} ")
# =============================================================================
        
# =============================================================================
# mahsulotlar = {'olcha':2500,
#                'anor':5000,
#                'gilos':6000,
#                'orik':11000,
#                'banan':15000,
#                'olma':4000}
# bozorlik = ['olma','banan','mandarin','gilos']
# for buyum in bozorlik:
#     if buyum not in mahsulotlar :
#         print(f"Iltimos dokonga {buyum} ham olib keling")
# =============================================================================
        
# =============================================================================
# mahsulotlar = {'olcha':2500,
#                'anor':5000,
#                'gilos':6000,
#                'orik':11000,
#                'banan':15000,
#                'olma':4000}
# print('Dokonimizdagi mahsulotlar : ')
# for one in sorted(mahsulotlar):
#     print(one.title())
# #print(mahsulotlar.values())    
# for tel in mahsulotlar.values():
#     print(tel)
# =============================================================================

# =============================================================================
# dictionaries = {'apple':'olma','car':'mashina','tea':'yoy','go':'bormoq'
#        ,'bus':'avtobus','icecream':'muzqaymoq'}
# for key,value in sorted(dictionaries.items()) :
#     print(f" {key} ning ozbekcha manosi {value} ")
# =============================================================================

# =============================================================================
# countries = {'USA':'Washington D.C','Kyrgizistan':'Bishkek','Polsha':'Riga','UK':'london'}
# print('Davlatlar : ')
# for davlat  in sorted(countries.keys()) :
#     print(davlat)
#    
# print('potyaxtlar : ')
# for poytaxt  in sorted(countries.values()) :
#     print(poytaxt)
# =============================================================================

# =============================================================================
# countries = {'USA':'Washington D.C','Kyrgizistan':'Bishkek','Polsha':'Riga','UK':'london'}
# capital = input("Qaysi davlatning poytaxtini bilmoqchisiz : ")
# for cap in countries.keys():
#     if cap in capital :
#         print(f" {capital} ning poytaxti {countries[cap]} ")
# =============================================================================
        
meals = {'osh':12000,
         'shorva':8000,
         'kabob qiyma':9000,
         'orama kabob':10000,
         'kavkaz kabob':15000}
buyurtma = []
for i in range(3):
    buyurtma.append(input(f'{(i+1)} - taomni kiriting : '))            
for taom in buyurtma:
        if taom in meals.keys():
            print(f"{taom} ning narxi {meals[taom]} som")
        else :
            print('bunday taom yoq')
















