# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:41:15 2023
#19-Dars : Funksiyalar

@author: Abror
"""

def salom_ber(ism):
    """salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.lower()}!")

salom_ber("Abror")


def yosh_hisobla(ism,t_yil):
    """Foydalanuvchi yoshini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2023-t_yil} yoshda")

yosh_hisobla(ism="Abror", t_yil=2002)