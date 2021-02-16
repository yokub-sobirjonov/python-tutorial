# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:04:58 2021

@author: User
"""
# =============================================================================
# phone0 = {'smartphone':'galaxy fold x',
#          'price':'250$',
#          'memory':'256GB',
#          'camera':'12mp',
#          'sim card':'dual nano'}
# phone1 = {'smartphone':'ipxone 12 pro max',
#          'price':'1499$',
#          'memory':'256GB',
#          'camera':'12mp+2x12mp',
#          'sim card':'one nano'}
# phone2 = {'smartphone':'Resmi 10T lite',
#          'price':'600$',
#          'memory':'128GB',
#          'camera':'12mp',
#          'sim card':'dual nano'}
# =============================================================================
# =============================================================================
# phone = phone0
# print(f"{phone['smartphone']} ,narxi - {phone['price']} ,\
# xotirasi - {phone['memory']} ,sim karta - {phone['sim card']}")
# phone = phone1
# print(f"{phone['smartphone']} ,narxi - {phone['price']} ,\
# xotirasi - {phone['memory']} ,sim karta - {phone['sim card']}")
# phone = phone2
# print(f"{phone['smartphone']} ,narxi - {phone['price']} ,\
# xotirasi - {phone['memory']} ,sim karta - {phone['sim card']}")
# =============================================================================

# =============================================================================
#phones = [phone0,phone1,phone2]
#for phone in phones:
#     print(f"Telefon : {phone['smartphone']} , "
#           f"Narxi : {phone['price']} , "\
#           f"Xotirasi : {phone['memory']} , "\
#           f"Sim karta : {phone['sim card']}")
# =============================================================================

#print(phones[0])

#print(phones[0]['smartphone'])

# =============================================================================
# print(f"{phones[1]['price']} lik "
#       f"{phones[1]['smartphone'].title()}")
# =============================================================================

# =============================================================================
# top_smartphones = []
# for n in range(4):
#     phone0 = {'smartphone':'galaxy fold x',
#          'price':'250$',
#          'memory':None,
#          'camera':'12mp',
#          'sim card':'dual nano'}
#     top_smartphones.append(phone0)
# for smphn in top_smartphones[:2] :
#     smphn['memory'] = "128GB"
# for smphn in top_smartphones[2:4] :
#     smphn['memory'] = "256GB"
# print(top_smartphones)
# =============================================================================

# =============================================================================
# programmers = {'david':['phyton','c++'],
#                'bobur':['sql','c++'],
#                'aziz':['java','c#'],
#                'doniyor':['android','ios'],
#                'Jahongir':['ML and AI','phyton']}
# for name,plang in programmers.items():
#     print(f"\n{name} quyidagi dasturlash tillarini biladi : ",end=' ')
#     for lang in plang :
#         print(lang.upper(), end=' ')
# =============================================================================

# =============================================================================
# programmers = {
#     'sardor':{
#               'age':22,
#               'plang':['c++','phyton','java'],
#               'adress':'new york',
#               'rating':2000,        
#              }, 
#     'umid': {
#              'age':26,
#              'plang':['c++','phyton','java','sql'],
#              'adress':'new york',
#              'rating':1000,        
#              },
#     'steve':{
#              'age':31,
#               'plang':['c#','c++','android','phyton','java'],
#               'adress':'new york',
#               'rating':700,        
#              } 
#             }
# for name,info in programmers.items():
#     print(f"{name.title()}, yoshi : {info['age']} da, "
#           f"Manzili : {info['adress'].title()}, \n"
#           f"Xalqaro reytingi : {info['rating']} talikka kirgan\n"
#           f"Quyidagi dasturlash tillarini biladi : ")
#     for lang in info['plang']:
#         print(lang.upper())
# =============================================================================
    
# =============================================================================
# famousp = {
#     'Alisher Navoiy':{
#               'spec':['poet','writer','minister'],
#               'novels':['hamsa','hayrat-ul abror','layli va majnun'],
#               'adress':'hirot shahri',
#               'umri':60,
#              }, 
#     'Erkin Vohidov': {
#              'spec':['writer','minister'],
#               'novels':['tong nafasi','qoshnilarim sizga'],
#               'adress':'Fargona viloyati', 
#               'umri':67,
#              },
#     'Abdulla Qodiriy':{
#              'spec':['poet','writer'],
#               'novels':['otkan kunlar','mehrobdan chayon'],
#               'adress':'Toshkent viloyati',
#               'umri':72,
#              } 
#             } 
# for name,info in famousp.items():
#       print(f"\n{name}, {info['adress']} da tugilgan ", end = ' ')
#       print(f"{info['umri']} yil umr korgan")
#       for i in info['novels']:
#            print(i,end=" ")
#       print("kabi asarlar yozgan")     
# =============================================================================
    
# =============================================================================
# people = {'dadam':['terminator','jeck london','hachiko','titanik','rembo'],
#           'oyim':['Karib dengizi qaroqchilari','saroy javohiri','titanik','qish sonatasi'],
#           'singlim':['qalb rishtasi','titanik','abu bakr siddiq','paygambarlar tarixi']}
# #name = input("whose favourite films do you want to know ? --->  ")
# #if name == people:
# for name in people.keys():
#     print(f"{name.title()} ning yoqtirgan filmalari : ")
#     for i in people[name]:
#         print(i.title())
# =============================================================================
    
# =============================================================================
# countries = {
#     'Uzbekistan':{'capital':'tashkent',
#           'area':'449M kvm',
#           'citizens':'35M people',
#           'currency':'sum'
#         },
#     'AQSH':{'capital':'washington',
#           'area':'10,456M kvm',
#           'citizens':'229m people',
#           'currency':'dollor' 
#         },
#     'Kazakhstan':{'capital':'bishkek',
#           'area':'1,123M kvm',
#           'citizens':'57M people',
#           'currency':'tenge' 
#         }
#             }    
# # =============================================================================
# #   print(f" {country} ning poytaxti  {info['capital'].title()} \n",
# #         f"Maydoni : {info['area']} \n",
# #         f"Aholisi : {info['citizens']} kishi \n Pul birligi : {info['currency']} ")  
# # =============================================================================
# for country,info in countries.items():
#     print(country,'------------------------->')    
#     for i in info.keys():
#         print(f"{i} : {info[i]}")
# =============================================================================
 
countries = {
    'uzbekistan':{'capital':'tashkent',
          'area':'449M kvm',
          'citizens':'35M people',
          'currency':'sum'
        },
    'aqsh':{'capital':'washington',
          'area':'10,456M kvm',
          'citizens':'229m people',
          'currency':'dollor' 
        },
    'kazakhstan':{'capital':'bishkek',
          'area':'1,123M kvm',
          'citizens':'57M people',
          'currency':'tenge' 
        }
            }   
country = input('Davlat nomini kiriting : ').lower()
if country in countries:
    info = countries[country]
    print(country.upper())    
    for i in info.keys():
             print(f"{i} : {info[i]}")      






