# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:23:17 2021

@author: User
"""
# =============================================================================
# ismlar = []
# print('Yaqin dostlaringiz royhatini tuzsmiz.')
# n=1
# while True:
#     savol  = f"{n} - dostingizni kiriting : "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qoshasizmi (ha/yoq) ? ")
#     if javob == 'ha':
#         n += 1
#         continue
#     elif javob == 'yoq':
#         break
# print("Dostalar royhati : ")
# for ism in ismlar :
#     print(f'{ism}')
# =============================================================================
        
# =============================================================================
# print('Dostlaringizni yoshini saqlaydigan  dastur.')
# dostlar = {}
# ishora = True 
# while ishora :
#     ism = input('Dostingizni ismini kiritig: ')
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")        
#     dostlar[ism] = int(yosh)
#     
#     javob = input('Yana malumot qosgasizmi (ha/yoq)')
#     if javob == 'yoq':
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")        
# =============================================================================
    
# =============================================================================
# cars = ['malibu','rolls roys','nexia','damas','lacetti','damas','cobalt','damas']
# while 'damas' in cars:
#     cars.remove('damas')
# print(cars)    
# =============================================================================

# =============================================================================
# talabalar = ['sardor','azizbek','abdulloh','ismoil']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop() 
#     baho = input(f"{talaba.title()}ning bahosini kiriting : ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)
# for ismi in baholangan_talabalar:
#     print(f"{ismi.title()} ning bahosi {baholangan_talabalar[ismi]} ")         
# =============================================================================

# =============================================================================
# buyurtmalar = []
# savol = input("taomni kiriting : ")
# while True:
#     taom = input(savol)
#     buyurtmalar.append(taom)
#     
# print(buyurtmalar)
# =============================================================================
""""Oxiri togri bolmadi """
# =============================================================================
# ebozor = {}
# while True :
#     mahsulot = input("Mahsulotni kiriting (Agar mahsulot kiritmasangiz yoq ni tering) : \n")
#     if mahsulot == 'yoq':
#        buyurtmalar = []
#        while True:
#           
#            buyurtma = input("Buyurtmangizni kiriting : ")
#            for i in ebozor.keys():
#                if i in ebozor.keys():
#                    print(ebozor[i])
#                else :
#                    print('Bizda bunday mahsulot yoq')
#     else:
#         narx = input(f"{mahsulot}ning narxini kiriting : ")
#         ebozor[mahsulot] = int(narx)
# 
# for i in ebozor:
#     print(f"{i}ning narxi {ebozor[i]} som")
# =============================================================================
    
buyurtmalar = ['anor', 'non', 'olma', 'blender','shampoo','sochiq','qulupnay']
mahsulotlar = {
               'orik':'3000',
               'shaftoli':'7000',
               'olma':'4000',
               'gilos':'9000',
               'qulupnay':'4500',
               'behi':'6000'
               }    
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma} ning 1 kilosi {narh}  so'm")
    else :
        print(f"{buyurtma} bizda mavjud emas.")
    









    