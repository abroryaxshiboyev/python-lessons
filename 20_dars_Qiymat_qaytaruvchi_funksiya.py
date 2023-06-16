# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:20:24 2023

#20-dars Qiymat qaytaruvchi funksiyalar

@author: Abror
"""



def toliq_ism_yasa(ism,familiya,otasining_ismi=""):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism=f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism=f"{ism} {familiya}"
    return toliq_ism.title()

toliq_ismi=toliq_ism_yasa(ism="abror", familiya="yaxshiboyev",otasining_ismi="sultonboy o'g'li")
print(toliq_ismi)