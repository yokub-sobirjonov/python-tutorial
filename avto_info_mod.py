# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:09:38 2021

@author: User
"""

def avto_info(kompaniya,model,rangi, korobka,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rangi':rangi,
          'korobka':korobka,
          'yili':yili,
          'narhi':narhi
          }
    return avto
def avto_kirit():
    avtolar = []
    while True:
        print("\nQuyidagi malumotlarni kiriting",end='')
        kompaniya = input('Ishlab chiqaruvchi : ')
        model = input('Rusumini kiriting : ')
        rangi = input('Rangini kiritng : ')
        korobka = input('Holatini kiriting : ')
        yili = input('Yilini kiriting : ')
        narhi = input('Narhini kiriting : ')
        avtolar.append(avto_kirit(kompaniya,model,rangi,korobka,yili,narhi))
        javob = input('Yana odam qoshasizmi (yes/no): ')
        if javob == 'no':
            break
    return avtolar
def info_print(avto_info):
     print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yili']}-yil, {avto_info['narhi']}$")
    

   
    
        
    
    