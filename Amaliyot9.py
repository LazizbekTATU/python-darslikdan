#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:01:48 2022

@author: user
"""


#narx = 15000
#salat = True
#choy = False


#if choy and salat:
#    narx = narx + 10000
#elif choy or salat:
#    narx = narx + 5000
#print(f"{narx} buladi")


#narx = 15000
#salat = True
#choy = False
#suzma = True
#meva = False
#cola = True


#if salat:
#     print("mijoz salat oldi")
#     narx = narx + 8000
#if choy:
#    print("mijoz salat oldi")
#    narx = narx + 2000
#if suzma:
#    print("mijoz suzma oldi")
#    narx = narx + 5000
#if meva:
#    print("mijoz meva oldi")
 #   narx = narx + 11000 
#if cola:
#    print("mijoz cola ham oldi")
#    narx = narx + 12000
#print(f"Jami {narx} sum")



#9.05

#menyu = ['somsa','osh','shashlik','qugurma',"norin"]
#ovqat = input("nima ovqat yeysiz>>>>")
#if ovqat.lower() in menyu:
#    print("buyurtna qabul qilindi")
#else:
#    print("Bunday taom yuq")



#9.06

#menyu = ['somsa','osh','shashlik','qugurma',"norin"]
#orders = ["somsa",'cola','shashlik','bosma','osh']

#for taom in orders:
#    if taom in menyu:
#        print(f"menyuda {taom} bor")
#    else:
#        print(f"kechirasiz, menyuda {taom} yuq")


#menyu = ['somsa','osh','shashlik','qugurma',"norin"]
#orders = ["somsa",'cola','shashlik','bosma','osh']#

#if orders:
#    for taom in orders:
#        print(f"Menyuda {taom} bor")
#    else:
#        print(f"Menuda {taom} yuq ")
#else:
#    print("savatchangiz bush")
 

#Amaliyot vazifasi

#1

#son = int(input("Iltimos juft son kiriting>>>"))

#if son%2==0:
#    print("Rahmat!")
#else:
#    print("Bu son juft son emas")
 

#2

#yosh = int(input("Yoshingiz nechida>>>"))

#if yosh<4 or yosh>60:
#    print("bepul")
#elif yosh<18:
#    print("chipta narxi 10000 sum")
#elif yosh>18:
#    print("chipta narxi 20000 sum")


#3

#a = int(input("a = "))
#b = int(input("b = "))

#if a==b:
#    print("Sonlar o'zaro teng ekan")
#elif a>b:
#    print("a son katta")
#else:
#    print("b son katta")


#4

#product = ['computer', 'pen','pencil','book','lamb','watch','jacet','tv','radio','chalk']
#savat = []

#for n in range(5):
#    savat.append(input(f"{n+1}- mahsulotni kiriting>>>"))
    
#if savat:
#    for buyum in savat:
#        if buyum in product:
#            print(f"dokonimizda {buyum} bor")
#        else:
#            print(f"dokonimizda {buyum} yuq")
#else:
#    print("savatchangiz bush")

 
#5

         
#product = ['computer', 'pen','pencil','book','lamb','watch','jacet','tv','radio','chalk']
#savat = []

#for n in range(5):
#    savat.append(input(f"{n+1}- mahsulotni kiriting>>>"))
#bor_mahsulotlar = []
#yuq_mahsulotlar = []

#for buyum in savat:
    
#    if buyum in product:
#          bor_mahsulotlar.append(buyum)
#    else:
#          yuq_mahsulotlar.append(buyum)

#if yuq_mahsulotlar:
#    print("do'konimizda quyidagi mahsulotlar yuq")
#    for buyum in yuq_mahsulotlar:
#        print(buyum)
#else:
#    print("Siz so'ragan hamma mahsulotlar bor")

#6

#foydalanuvchilar = ['lazizbek', "ibratillo",'kitob','pen']

#login = input("Iltimos yangi login tanlang>>>")

#if login in foydalanuvchilar:
#    print("login band, boshqa login kirit")
#else:
#    print("Xush kelibsiz")

#7

a = int(input("a = "))

for i in range(2,11):
    if i%a==0:
        print(i)
  
print("Qoldiqsiz bo'linmaydi")










