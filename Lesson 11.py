# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:05:59 2021

@author: User
"""
#yosh = int(input('Yoshingizni kiriting : '))
#if yosh <= 4:
#    price = 0
#elif 4 < yosh <= 12 :
#    price =5000
#else :
#    price = 10000
#print("Hayvonot bogiga kirish {} som".format(price))    

#yosh = int(input('Yoshingizni kiriting : '))
#if yosh <= 4:
#   price = 0
#elif yosh <= 12 :
#    price = 5000
#elif yosh <= 60 :
#   price = 15000
#else :
#   price = 8000
#print("hayvonot bog'iga kirish {} som ".format(price))
           
# =============================================================================
# day = input("Bugun nima kun ? : ")
# if day.lower() == "shanba" or day.lower() == "yakshanba" :
#     print('Bugun dam olish kuni')
# else :
#     print('Bugun ish kuni')
# =============================================================================
# =============================================================================

# =============================================================================
# day = input('Bugun qanday kun : ') 
# temp = float(input('Havo harorati qanday : '))
# if day.lower() =='yakshanba' and temp >=30 :
#         print('Chomilishga borsa boladi')   
# elif day.lower() == 'yakshanba' and temp < 30 :
#         print('Bugun chomilgani bormagan maqul')
# =============================================================================

# day = input('Bugun qanday kun : ')
# if day.lower() != 'yakshanba':
#         print('Bugun chomilishga bora olmaymiz')
# else :     
#    temp = float(input('Havo harorati qanday : '))
#    if day.lower() =='yakshanba' and temp >=30 :
#         print('Chomilishga borsa boladi')   
#    elif day.lower() == 'yakshanba' and temp < 30 :
#         print('Bugun chomilgani bormagan maqul')    
# =============================================================================

# =============================================================================
# day = input('Bugun qanday kun : ')
# if day.lower() != 'yakshanba' and day.lower() != 'shanba':
#         print('Bugun chomilishga bora olmaymiz')
# else :     
#    temp = float(input('Havo harorati qanday : '))
#    if   temp >=30 :
#         print('Chomilishga borsa boladi')   
#    elif temp < 30 :
#         print('Bugun chomilgani bormagan maqul')
# =============================================================================
    
# =============================================================================
# narh = 16000
# tea = True
# salat = False
# 
# if tea and salat:
#     narh = narh + 10000
# elif tea or salat :
#     narh = narh + 6000
# print(f" Jami {narh} som boladi")    
# =============================================================================

# =============================================================================
# narh = 9000
# tea = True
# coffee = False
# cake = True
# soup = True
# kabab = False
# if tea : 
#     print( 'mijon tea oldi')
#     narh = narh +3000
# if coffee :
#     print('Mijoz coffee oldi')
#     narh = narh + 5000
# if cake :
#     print('Mijoz cake oldi')
#     narh = narh + 7000
# if soup :
#     print('Mijoz soup oldi')
#     narh = narh + 10000    
# if kabab :
#     print('Mijoz kabab oldi')
#     narh = narh + 8500
# print("Jami summa {} som boldi".format(narh))
# =============================================================================
 
# =============================================================================
# menu = ['somsa','kabob','shorva','dimlama','mastava','palov']
# print('perok' in menu)  
# 
# menu = ['somsa','kabob','shorva','dimlama','mastava','palov']
# print('palov' in menu)   
# =============================================================================

# =============================================================================
# menu = ['somsa','kabob','shorva','dimlama','mastava','palov']
# ovqat = input('Qanday ovqat buyurtma qilasiz ? \n')
# if ovqat.lower() in menu:
#     print('Buyurtmangiz qabul qilindi !!!')
# else:
#     print('Kechirasiz bizda bunday ovqat yoq .')
# =============================================================================
    
# =============================================================================
# menu = ['somsa','kabob','shorva','dimlama','mastava','palov']
# print('perok' not in menu)  
# 
# menu = ['somsa','kabob','shorva','dimlama','mastava','palov']
# print('palov' not in menu)      
# =============================================================================
    
# =============================================================================
# menu = ['somsa','kabob','shorva','dimlama','mastava','coffee','palov']
# buyurtmalar = ['tovuq','baliq','coffee']
# for taom in buyurtmalar :
#     if taom in menu :
#         print('Menyuda {} bor'.format(taom))
#     else :
#         print('Bizde siz buyurtirgan {} yoq'.format(taom))    
# =============================================================================

# =============================================================================
# menu = ['somsa','kabob','shorva','dimlama','mastava','coffee','palov']
# buyurtmalar = ['tovuq','baliq','coffee']
# for taom  in buyurtmalar :
#     if taom not in menu :
#         print('Bizde siz buyurtirgan {} yoq'.format(taom)) 
#        
#     else :
#           print('Menyuda {} bor'.format(taom))
# =============================================================================

# =============================================================================
# menu = ['somsa','kabob','shorva','dimlama','mastava','coffee','palov']
# ovqat = input('Nima ovqat yesam boladi ? :')
# if ovqat.lower() not in menu:
#     print('Bizda buday ovqat yoq')
# else :
#     print('Buyurtmangiz qabul qilindi')    
# =============================================================================

# =============================================================================
# menu = ['somsa','kabob','shorva','dimlama','mastava','coffee','palov']
# buyurtmalar = ['tovuq','baliq','coffee']
# if buyurtmalar :
#     for taom in buyurtmalar :
#         if taom in menu :
#             print(f"{taom} menyuda bor")
#         else :
#             print(f"{taom} menyuda yoq")
# else :
#     print('Buyurtma qiling, hali buyurtma qilmadingiz')
# =============================================================================
            
# =============================================================================
# number = int(input("Juft raqam kiriting : "))
# if number%2 == 0:
#     print("{} juft son ".format(number))
# elif number%2 == 1 :
#     print("{} bu toq son, juft emas".format(number))
#     
# =============================================================================

# =============================================================================
# age = int(input("Yoshingizni kiriting : "))
# if (age <= 4 or age >= 60) :
#     price = 0
# elif age <= 12 :
#     price = 5000
# elif  age < 60 :
#     price = 10000
# print("Kirish chipta narxi {}".format(price))    
# =============================================================================

# =============================================================================
# num1 = float(input('Birinchi son : '))
# num2 = float(input('Birinchi son : '))
# if num1>num2:
#     print(f"{num1} > {num2}")
# if num1<num2:
#     print(f"{num1} < {num2}")
# if num1==num2:
#     print(f"{num1} = {num2}")
# =============================================================================

# =============================================================================
# mahsulotlar = ['olma','anor','gilos','uzum','xurmo','olcha','orik']
# savat = []
# for num in range(5):
#     savat.append(input("Savatchaga mahsulotlarni kkiriting : "))
# for num in savat:    
#     if num in mahsulotlar :
#         print('Dokonimizda {} bor'.format(num))
#     else :
#         print('Dokonimizda {} yoq'.format(num))
# =============================================================================

# =============================================================================
# mahsulotlar = ['olma','anor','gilos','uzum','xurmo','olcha','orik']
# savat = []
# bor_mahsulot = []
# yoq_mahsulot = []
# for num in range(5):
#     savat.append(input("Savatchaga mahsulotlarni kkiriting : "))
# for num in savat:    
#     if num in mahsulotlar :
#         bor_mahsulot.append(num)
#     else :
#         yoq_mahsulot.append(num)
# print("Bor mahsulotlar royhati : {} ".format(bor_mahsulot))
# print("Yor mahsulotlar royhati : {} ".format(yoq_mahsulot))
# =============================================================================

# =============================================================================
# logins = ['sarvar','aziz','baxtiyor','ravshan','ibrohim']
# newlog = (input('Login kiriting : '))
# if newlog in logins:
#     for num in logins:
#       if num == newlog :  
#             print("Bu login band ,iltimos boshqa login kiriting !!!")
# else :
#             print('Xush kelibsiz !!!')         
# =============================================================================

# =============================================================================
# number = int(input('Istalgan butun son kiriting : '))
# for num in range(2,10):
#     if number%num == 0:
#         print(f"{number} soni {num} ga qoldiqsiz bolinadi." )
# =============================================================================
        








