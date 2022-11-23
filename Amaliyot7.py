#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:48:27 2022

@author: user
"""

#mehmonlar = ["Abbosxon","Odilbek","Quvonchbek","G'ayratjon","Abdusalim"]
#for mehmon in mehmonlar:
#   print(mehmon)

#mehmonlar = ["Abbosxon","Odilbek","Quvonchbek","G'ayratjon","Abdusalim"]
#for mehmon in mehmonlar:
#    print(f'Hurmatli {mehmon},')
#    print("Sizni nikoh to'yimizga taklif etamiz")
#    print("Hurmat bilan, Isaqjonovlar oilasi")


#cars = ["tico", 'damas','nexia']
#for car in cars:
#    print(car.upper())
#print("GM da ishlab chiqarilgan")


#cars = ["tico", 'damas','nexia']
#for car in cars:
#    print(car.upper())
#    print("GM da ishlab chiqarilgan")


#sonlar = list(range(1,11))
#for son in sonlar:
#    print(f'{son} ning kvadrati {son**2} ga teng')


#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print("5 ta eng yaqin do'stingiz kim?")
#for n in range(5):
#    dostlar.append(input(f"{n+1}-ismini kiriting:"))
#print(dostlar)


#1.00

#names = ["Ibratillo","Abduvohid","Lazizbek","Karimjon", "Abbosxon", "Boburjon"]
#for name in names:
#    print(f'{name} ahvollaring yaxshimi')

#1.01

#names = ["Ibratillo","Abduvohid","Lazizbek","Karimjon", "Abbosxon", "Boburjon"]
#for name in names:
#    print(f'{name}')
#print(len(names), "marta takrorlanadi")


#1.02

#sonlar = list(range(11,100,2))
#sonning_kubi = []
#for son in sonlar:
#    sonning_kubi.append(son**3)
#for kub in sonning_kubi:
#    print(kub)

#1.03

#1.04

#kinolar = []
#print("eng sevimli 5 ta filmingiz qaysilar?")
#for n in range(5):
#    kinolar.append(input(f"{n+1}-kinoni kiriting:"))
#print(kinolar)

#1.05


n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)