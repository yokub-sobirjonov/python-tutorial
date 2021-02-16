# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:21:14 2021

@author: User
"""

# =============================================================================
# def summ(*nums):
#     yegindi = 0
#     for num in nums:
#         yegindi += num
#     return yegindi
# print(summ(3,5))    
# =============================================================================

# =============================================================================
# def summ(*nums):
#     return sum(nums)
# print(summ(1,2,3,4,5,6))
# =============================================================================

# =============================================================================
# def summa(x,y,*nums):
#     return x+y+sum(nums)
# print(summa(1,2))
# =============================================================================

# =============================================================================
# def avto_info(company,model,**info):
#     info['company'] = company
#     info['model'] = model
#     return info
# avto1 = avto_info('Mercedes','G63', rangi = 'qora',yili = 2019)
# avto2 = avto_info("CHEVROLET",'malibu',rangi = 'oq',yili = 2020)
# print(avto1)
# =============================================================================

#AMALIYOT

# =============================================================================
# def number(*numbers):
#     num = 1
#     for son in numbers:
#         num *= son
#     return num
# print(number(1,2,7,9))    
# =============================================================================

def student(name, surname,adress,pnum,**info):
    info['name'] = name
    info['surname'] = surname
    info['adress'] = adress
    info['pnum'] = pnum
    return info
talaba1 = student('Sardor','azizov','namangan',2223329,kasbi = 'Dasturchi')
talaba2 = student('Bahtiyor','orinov','fargona',1123434,kasbi = 'jurnalist')
print(talaba1)













