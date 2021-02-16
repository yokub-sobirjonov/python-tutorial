# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:21:30 2021

@author: User
"""
# =============================================================================
# ism = input('Ism kiriting : ')
# savol = f"{ism} yoshingiz nechida ? "
# yosh = input(savol)
# height = input("boyingizni kiriting : ")
# height = float(height)
# print(f"{ism}, yoshingiz {yosh} , boyingiz {height}")
# =============================================================================

# =============================================================================
# son = 22
# while son >= 10:
#     print(son)
#     son-=1
# =============================================================================

# =============================================================================
# print('Kiritilgan sonning kvadratini qaytaradigan dastur.')
# savol = 'Istalgan son kiriting '
# savol += "(dasturni toxtatish uchun exit sozini kiriting ) : "
# qiymat = ''
# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat != "exit":
#             print(float(qiymat)**2)
# =============================================================================

# =============================================================================
# print('Kiritilgan sonning kvadratini qaytaradigan dastur.')
# savol = 'Istalgan son kiriting '
# savol += "(dasturni toxtatish uchun exit sozini kiriting ) : "
# ishora = True
# qiymat = ''
# while ishora:
#     qiymat = input(savol) 
#     if qiymat != "exit":
#         ishora = False
#     else :
#         print(float(qiymat)**2)
# =============================================================================

# =============================================================================
# print('Kiritilgan sonning kvadratini qaytaradigan dastur.')
# savol = 'Istalgan son kiriting '
# savol += "(dasturni toxtatish uchun exit sozini kiriting ) : "
# while True :
#     qiymat = input(savol) 
#     if qiymat == "exit":
#         break
#     else :
#         print(float(qiymat)**2)
# =============================================================================

# =============================================================================
# sonlar = range(1,11)
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")
# =============================================================================
    
# =============================================================================
# son = 1
# while son > 0:
#     son += 1
#     if son%2 == 1:
#         continue
#     else:
#         print(son)
# =============================================================================
        
# =============================================================================
# savol = "Kiritilgan sonni ildizini qaytaruvchi dstur ."
# savol = "Istalgan musbat sonni kiriting"
# savol += "(Dasturni toxtatish uchun (exit) sozini kiriting) : "
# while True:
#     qiymat = float(input(savol))
#     if qiymat < 0:
#         break
#     elif qiymat == 'exit':
#         break
#     else:
#         ildiz = float(qiymat**(0.5)) 
#         print(f" {qiymat} ning ildizi {ildiz} ga teng")
# =============================================================================

# =============================================================================
# print('foydalanuvchi yaxshi koradigan kitoblar royhatini chiqarib beruvchi dastur.')
# savol = 'Kitobni kiriting '
# savol += '(Dasturni toxtatish uchun (stop) sozini kiriting) : '
# taom = ''
# while True:
#     taom = input(savol)
#     if taom =='exit':
#         break
#     else:
#         continue
# =============================================================================

# =============================================================================
# print('foydalanuvchiga chipta narxlarini chiqarib beruvchi dastur.')
# savol = 'Yoshingizni  kiriting '
# savol += '(Dasturni toxtatish uchun (stop) sozini kiriting) : '
# taom = ''
# while True:
#     taom = input(savol)
#     if taom =='exit':
#         break
#     else:
#         continue
# =============================================================================

print('foydalanuvchiga chipta narxlarini chiqarib beruvchi dastur.')
savol = 'Yoshingizni  kiriting '
savol += '(Dasturni toxtatish uchun (exit , quit) sozini kiriting) : '
while True:
    qiymat = input(savol)
    if qiymat =='exit' or qiymat  == 'quit':
        break
    yosh = int(qiymat)
    if yosh <= 7:
        chipta = 2000
    elif yosh > 7 and yosh <= 18:
        chipta = 3000 
    elif yosh > 18 and yosh <= 65:
        chipta = 10000
    else :
        chipta = 0
    if chipta == 0:
        print('Sizga kirish tekin')    
    else:    
        print(f"chipta narxi siz uchun {chipta} ")        






