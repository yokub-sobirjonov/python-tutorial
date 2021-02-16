# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:10:50 2021

@author: User
"""
# =============================================================================
# cars = {'model':'Lexus','color':'white'}
# print(cars['model'])
# =============================================================================

# =============================================================================
# student = {'name':'Sardor Arslonov','dof':'2001','age':'19'}
# print(f" {student['name'].title()} \
#       {student['dof']} - yilda tugilgan \
#        yoshi {student['age']} da")
# =============================================================================

# =============================================================================
# student = {'name':'Sardor Arslonov','dof':'2001','age':'19'}
# student['kurs'] = 2
# student['fish'] = 'Soliyev Anvar'
# print(student['fish'])
# print(f"{student['kurs']} - kurs")
# print(student)
# =============================================================================

# =============================================================================
# student = {}
# student['ismi'] = 'Sardor'
# student['yoshi'] = 23
# student['kursi'] = 3
# print(student)
# print("Talaba {} ,{} yoshda, {} - kursda oqiydi "
# .format(student['ismi'],student['yoshi'],student['kursi']  ))  
# =============================================================================
  
# =============================================================================
# student = {'name':'Sardor Arslonov','dof':'2001','age':'19'}
# print(student)
# del student['dof']
# print(student)
# =============================================================================

# =============================================================================
# phones = {'bobur':'iphone Xs',
#           'sarvar':'samsung a71',
#           'abdulaziz':'redmi 10T',
#           'sardor':'oppo find x',
#           'jaxongir':'pocofon p3'}
# onephone = phones['sadulla']
# print("Telefonning markasi {}".format(onephone))
# =============================================================================

# =============================================================================
# phones = {'bobur':'iphone Xs',
#           'sarvar':'samsung a71',
#           'abdulaziz':'redmi 10T',
#           'sardor':'oppo find x',
#           'jaxongir':'pocofon p3'}
# onephone = phones.get('husan','bunday ism mavjud emas')
# print(onephone)
# =============================================================================

#AMALIYOT

# =============================================================================
# otam = {'name':'Muhammadsodiq','datebirth':1971,'malumoti':'orta','adress':'namangan'}
# onam = {'name':'Muhayyo','datebirth':1974,'malumoti':'orta','adress':'namangan tumani'}
# dostim = {'name':'Muhammad','datebirth':1996,'malumoti':'oliy','adress':'Buxoro viloyati'}
# tugilganyil = otam['datebirth']
# print(f"Otamning ismi {otam['name']} , {tugilganyil} - yilda {otam['adress']} da tugilgan")
# =============================================================================

# =============================================================================
# favfood = {'onam':'kabob','dadam':'palov','singlim':'spagetti'}
# print("Singlimning sevimli taomi {}".format(favfood['singlim']))
# =============================================================================

# =============================================================================
# dicphyton = {'int':'buntun (son) qiymat qabul qiladi','float':'haqiqiy son qabul qiladi'
# ,'if':'shart operatori','else':'aks holda operatori','append()':'qiymat (element) qoshish operatori'
# ,'upper()':'matn ni katta harfga ogiruvchi qiymat','get()':'bor yoki yoqligini aniqlab bruvchi oprator'}
# print(f"If operatori {dicphyton['if']} \nelse operatori {dicphyton['else']}")
# =============================================================================

# =============================================================================
# dicphyton = {'int':'buntun (son) qiymat qabul qiladi','float':'haqiqiy son qabul qiladi'}
# text = input('Soz kiriting : ')
# if text in dicphyton:
#     print(dicphyton[text])
# =============================================================================

dicphyton = {'int':'buntun (son) qiymat qabul qiladi','float':'haqiqiy son qabul qiladi'}
text = input('Soz kiriting : ')
if text in dicphyton:
    print(dicphyton[text])
else :
    print("bunday operator (key) mavjud emas !")










