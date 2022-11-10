#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:29:18 2022

@author: user
"""

#1   Ismlar degan ro'yhat yarating va kamida 3 ta do'stingiz ismini kiriting

#Ismlar = ["Ibratillo",'Akmaljon',"G'ayratali"]
#print(Ismlar)


#2 Ro'yhatdagi har bir do'stingizga qisqa habar yozib konsulga chiqaring

#Ismlar = ["Ibratillo",'Akmaljon',"G'ayratali"]

#print("Salom", Ismlar[0], "ishlar yaxshimi")
#print(Ismlar[1],"va",Ismlar[2], "qadirdon do'stlar")


#3 Sonlar deb nomlangan ro'yhat yarating va ichiga turli sonlarni yuklang
# (musbat,manfiy, butun, o'nlik)

#Sonlar = []

#Sonlar.append(12)
#Sonlar.append(-23)
#Sonlar.append(12.23)
#Sonlar.append(23.0)

#print(Sonlar)


#4 Yuqoridagi ro'yhatdan sonlar ustida turli arifmetik amallar bajarib ko'ring
# Ro'yhatdagi ba'zi sonlarning qiymatini o'zgartiring, Ba'zilarini esa almashtiring

#Sonlar = []

#Sonlar.append(12)
#Sonlar.append(-23)
#Sonlar.append(12.23)
#Sonlar.append(23.0)

#print(Sonlar[0]+Sonlar[2])
#print(Sonlar[3]-Sonlar[2])
#print(Sonlar[0]*Sonlar[3])
#print(Sonlar[3]/Sonlar[2])
#Sonlar[0]=23
#Sonlar[3]=Sonlar[3]+21
#print(Sonlar)

#5 t_shaxslar va z_shaxslar degan 2 ta ro'yhat yarating va bir-biriga o'zingiz 
#eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi 
#tirik bo'lgan shaxslarning ismini kiriting

#t_shaxslar=['Buxoriy','Amir Temur', "Navoiy","Bobur","Jaloliddin"]
#z_shaxslar=["Karimov","Oybek","Avloniy","Lazizbek","Ibratillo"]
#print("Zamonaviy shaxslar:",z_shaxslar,"\nTarixiy shaxslar:",t_shaxslar)


#6 Yuqoridagi ro'yhatlarning har biridan bittadan qiymatni sug'urib olib (.pop())
#quyidagi ko'rinishda chiqaring

#t_shaxslar=['Buxoriy','Amir Temur', "Navoiy","Bobur","Jaloliddin"]
#z_shaxslar=["Karimov","Oybek","Avloniy","Lazizbek","Ibratillo"]

#print("Men tarixiy shaxslardan", t_shaxslar.pop(1), "bilan\n",
#      "zamonaviy shaxslardan esa", z_shaxslar.pop(0),"bilan suhbat qilishni\n"
#      "istar edim")

#7  friends nomli bo'sh ro'yhat tuzing va unga .append() yordamida 5-6 ta mehmonga
#chaqirmoqchi bo'lgan do'stlaringizni kiriting.

#friends = []
#friends.append("Ibratillo")
#friends.append("Sobirjon")
#friends.append('Jeyms')
#friends.append('Pulatjon')
#friends.append("Jasurbek")
#friends.append("Masrurbek")

#print(friends)


#8 Yuqoridagi ro'yhatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
#yordamida olib tashlang

#friends = []
#friends.append("Ibratillo")
#friends.append("Sobirjon")
#friends.append('Jeyms')
#friends.append('Pulatjon')
#friends.append("Jasurbek")
#friends.append("Masrurbek")
#friends.remove("Sobirjon")
#friends.remove("Pulatjon")

#print(friends)

#9 Ro'yhatlar oxiriga,boshiga, va o'rtasiga yangi ismlar kiriting

#Ismlar=['Ibratillo', 'Jeyms', 'Jasurbek', 'Masrurbek']
#Ismlar.append("Lazizbek")
#Ismlar.insert(0,"Hamidullo")
#Ismlar.insert(3,"Hoshimjon")

#print(Ismlar)

#10 Yangi mehmonlar deb nomlangan bo'sh ro'yhat yarating .pop() va .append() 
#metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yhatidan 
#sug'urib olib, mehmonlar ro'yhatiga qo'shing

#mehmonlar = []
#friends = ['Hamidullo', 'Ibratillo', 'Jeyms', 'Hoshimjon','Masrurbek', 'Lazizbek']
#friends.pop(0)
#mehmonlar.append("Hamidullo")
#friends.pop(3)
#mehmonlar.append("Hoshimjon")
#friends.pop(-1)
#mehmonlar.append("Lazizbek")

#print(mehmonlar)
#print(friends)