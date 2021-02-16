# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:37:03 2021

@author: User
"""
# =============================================================================
# def toliq_ism_yasa(ism,familiya):
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('Sardor', 'Azizov')
# talaba2 = toliq_ism_yasa('Qobil', 'Umarov')
# print(f"Darsni qoldirgan oquvchilar : {talaba1} va {talaba2}")
# =============================================================================

# =============================================================================
# def toliq_ism_yasa(ism,familiya,otasining_ismi = ""):
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else :
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('yodgor','azizov')
# talaba2 = toliq_ism_yasa('abdulloh','Abdujalilov','Sadulla ogli')
# print(f"Talabaning FISHi {talaba1} va {talaba2}")        
# =============================================================================

# =============================================================================
# def avto_info(kompaniya,modeli,rangi,korobka,yili,narhi=None):
#     avto = {'kompaniya':kompaniya,
#         'modeli':modeli,
#         'rangi':rangi,
#         'korobka':korobka,
#         'yili':yili,
#         'narh':narhi
#         }
#     return avto
# avto1 = avto_info('BMW','x5','black','mehanik',2018)    
# avto2 = avto_info('Mercedes','amg 222','white','avtomat',2019,45000)    
# avtolar = [avto1,avto2]
# print("Online bozordagi mashinalar : ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = 'nomalum'
#     print(f"{avto['rangi']} {avto['modeli']}, Narxi : {narh}")
# =============================================================================
        
# =============================================================================
# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min +=1
#     return sonlar
# print(oraliq(2,6))    
# print(oraliq(0,9))    
# =============================================================================
        
# =============================================================================
# def oraliq(min,max,qadam):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min +=qadam
#     return sonlar
# print(oraliq(2,24,3))    
# print(oraliq(0,9,2))
# =============================================================================

# =============================================================================
# def avto_info(kompaniya,modeli,rangi,korobka,yili,narhi=None):
#     avto = {'kompaniya':kompaniya,
#         'modeli':modeli,
#         'rangi':rangi,
#         'korobka':korobka,
#         'yili':yili,
#         'narh':narhi
#         }
#     return avto
# =============================================================================
# =============================================================================
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
#     
#       #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#       #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# =============================================================================

# =============================================================================
# def user(ismi,familiyasi,tyil,adress,age,email,pnumber=None):
#     info = {'ismi':ismi,
#             'familiyasi':familiyasi,
#             'tyil':tyil,
#             'adress':adress,
#             'age':age,
#             'email':email,
#             'pnumber':pnumber
#             }
#     return info
# print('Talba haqida ,alomatlarni oynaga chiqarib beruvchi dastur:')
# talaba = []
# belgi = ''
# while True:
#     ismi = input("ismini kiritnig : ")
#     familiya = input("Familiyasini kiriting : ")
#     tyil = int(input("Tugilgan yilini kiriting : "))
#     adress = input("Adresini kiriting : ")
#     age = 2021-tyil
#     email = ''
#     pnumber = ''
#     belgi = input("Email kiritaszmi ? ")
#     if belgi=='ha':
#         email = input("Email ni kiriting : ")
#     elif belgi == 'yoq':
#         continue    
#     belgi = input("telefon raqam kiritaszmi ? ")    
#     if belgi == 'ha':
#         pnumber = input("telefon raqamni kiriting : ")
#     elif belgi == 'yoq':
#         continue
#     if email :
#       talaba.append(user(ismi,familiya,tyil,adress,age,email,pnumber))
#     else :
#         if pnumber :
#             talaba.append(user(pnumber))
#         else :
#             continue      
#     javob = input('Yana talaba qoshasizmi : ')
#     if javob =='no':
#            print(talaba)
#            break
# =============================================================================

# =============================================================================
# def user(ismi,familiyasi,tyil,adress,age,email,pnumber=None):
#     info = {'ismi':ismi,
#             'familiyasi':familiyasi,
#             'tyil':tyil,
#             'adress':adress,
#             'age':age,
#             'email':email,
#             'pnumber':pnumber
#             }
#     return info
# print('Talba haqida ,alomatlarni oynaga chiqarib beruvchi dastur:')
# talaba = []
# while True:
#     ismi = input("ismini kiritnig : ")
#     familiyasi = input("Familiyasini kiriting : ")
#     tyil = int(input("Tugilgan yilini kiriting : "))
#     adress = input("Adresini kiriting : ")
#     age = 2021-tyil
#     email = input('Email ni kiriting :')
#     pnumber = input("Raqamni kiriting : ")  
#     javob = input('Yana talaba qoshasizmi (yes/no) : ')
#     talaba.append(user(ismi,familiyasi,tyil,adress,age,email,pnumber))
#     if javob !='yes':
#            break
#        
# for info in talaba:
#    print(f"Ismi : {info['ismi'].title()} , Familiyasi : {info['familiyasi'].title()}",
#          f"Tugilgan yili : {info['tyil']} , Yoshi : {info['age']} ,Email : {info['email']} ,Raqami : {info['pnumber']}")
# =============================================================================

# =============================================================================
# def son(a,b,c):
#     if a>b:
#         if a>c:
#             print(a) 
#     else:
#         if b>c:
#             print(b)
#         else :
#             print(c)
#     return
#                 
# a = input("a ni kiriting : ")
# b = input('b ni kiriting : ')
# c = input("c ni kiriting : ")
# maxx= son (a, b, c)
# print(maxx) 
# =============================================================================

# =============================================================================
# def tub_sonlar_top(min,max):
#     tub_sonlar = []
#     for n in range(min,max+1):
#          tub = True
#          if (n==1):
#              tub = False
#          elif (n==2):
#              tub = True
#          else:
#              for x in range(2,n):
#                  if (n%x==0):
#                      tub = False
#          if tub:
#              tub_sonlar.append(n)
#     return tub_sonlar
# =============================================================================

# =============================================================================
# def fibonachi(n):
#     fib = []
#     for x in range(n):
#         if x==0 or x==1:
#             fib.append(n)
#         else:
#             fib.append(fib[x-1]+fib[x-2])
#     return fib
# print(fibonachi(9))
# =============================================================================
    
# =============================================================================
    # def fib(x):
    #     """Recursive function of Fibonacci number"""
    #     if x==0:
    #         return 0
    #     elif x==1:
    #         return 1
    #     else:
    #         return fib(x-1)+fib(x-2)
# =============================================================================

# =============================================================================
# def fib2(x):
#     """Making a list of "x" fib numbers (not recursive)
#     Returns a list of fib numbers"""
#     len = [0,1]
#     while len(len)<=x:
#         len.append(len[-1]+len[-2])
#     return len
# =============================================================================

# =============================================================================
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f" {ism} ning bahosini kiriting : ")
#         baholar[ism] = baho
#     return baholar
# talabalar = ['aziz','sardor','botir','abdulloh']
# baholar = bahola(talabalar)    
# print(baholar)    
# =============================================================================

# =============================================================================
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f" {ism} ning bahosini kiriting : ")
#         baholar[ism] = baho
#     return baholar
# talabalar = ['aziz','sardor','botir','abdulloh']
# baholar = bahola(talabalar[:])    
# print(talabalar)
# 
# =============================================================================

# =============================================================================
# def my_func(*ism):
#     print("Salom "+ism[0])
#     
# my_func('Sardor','aziz','bahodir')    
# =============================================================================

# =============================================================================
# def my_func(**ism):
#     print("Salom "+ism['b'].title())
#     
# my_func(a = 'Sardor',b = 'aziz',c = 'bahodir')
# =============================================================================



# =============================================================================
# def katta_harf(texts):
#    for i in range(len(texts)):
#        texts[i] = texts[i].title()
# talabalar = ['aziz','sardor','botir','abdulloh']
# katta_harf(talabalar)   
# print(talabalar)
# =============================================================================

def katta_harf(texts):
    texts = texts[:]
    for i in range(len(texts)):
        texts[i] = texts[i].title()
    return texts    
talabalar = ['bobur','alisher','bahodir','fathulla']
katta_harf(talabalar)
new_talabalar = katta_harf(talabalar[:])
print(talabalar)        
print(new_talabalar)





