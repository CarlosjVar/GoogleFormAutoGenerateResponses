# Autofill Google Form

import requests
import datetime
import time
import sys
import random
from random import choices
from collections import Counter


#Returns a random age based on the probability distribution from the survey
def get_random_age():
    #Age probability distribution
    #Number of age groups
    population = [0,1,2,3,4,5,6,7]
    #Probability of being in an age group
    weights = [0.383,0.098,0.085,0.134,0.19,0.049,0.042,(3/305)]

    agegroup = choices(population,weights)[0]
    #Switch case for age groups
    switcher = {
        0: random.randint(14,21),
        1: random.randint(21,28),
        2: random.randint(28,36),
        3: random.randint(36,43),
        4: random.randint(43,50),
        5: random.randint(50,58),
        6: random.randint(58,65),
        7: random.randint(65,72),
    }
    return switcher.get(agegroup,"nothing")
#Returns a random province based on the probability distribution from the survey
def get_random_province():
    #Province probability distribution
    #Provinces
    population = ["San+Jos%C3%A9","Heredia","Alajuela","Cartago","Lim%C3%B3n","Puntarenas","Guanacaste"]
    #Probability of living in a province
    weights = [0.47,0.125,0.102,0.234,0.03,0.023,0.016]

    province = choices(population,weights)[0]
    return province
def get_random_education_level():
    #education_level probability distribution
    #education_levels
    education_levels = ["Nulo","Escuela","Bachillerato+9%C2%B0","Bachillerato+11%C2%B0","Bachillerato+Universitario","Licenciatura"]
    #Probability of education_level
    weights = [0.003,0.007,0.033,0.384,0.275,0.298]

    education_level = choices(education_levels,weights)[0]
    return education_level
def get_random_habitantsPerHouse():
    #habitantsPerHouse probability distribution
    #habitantsPerHouse
    habitantsPerHouse = [1,2,3,4,5,6,7,8,10]
    #Probability of habitantsPerHouse
    weights = [0.036,0.154,0.22,0.246,0.262,0.066,0.01,0.003,0.003]

    result = choices(habitantsPerHouse,weights)[0]
    return result



# if(edadprobability>)

print(get_random_age())
print(get_random_province())
print(get_random_education_level())
print(get_random_habitantsPerHouse())
##Probability of interacting with someone with risk factors
interact_risk_factor= random.randint(1,100)
if interact_risk_factor< 62.3:
    #se relaciona con personas de riesgo
    url = f'https://docs.google.com/forms/d/e/1FAIpQLSc5IoP6g9TtNkK9kBFp8VYlysEDfQ8Ij8gHwkMBut2aAMjJ8A/formResponse?usp=pp_url&'\
        f'entry.1488779718={edad}'\
        f'entry.935746347=Heredia&'\
        f'entry.926861655=Bachillerato+11%C2%B0&'\
        f'entry.985634184=3&'\
        f'entry.1148479870=De+%C2%A2300000+a+%C2%A2700000&'\
        f'entry.253307569=S%C3%AD&'\
        f'entry.1517196595=2&'
    Adv_edad = "entry.925426602=Avanzada+edad&"
    hipertension = 'entry.925426602=Hipertensi%C3%B3n&'
    Obesidad = 'entry.925426602=Obesidad&'
    Diabtes = 'entry.925426602=Diabetes'
    Asma = '&entry.925426602=Asma&'
    pulmonares = 'entry.925426602=Padecimientos+pulmonares&'
    VIH = 'entry.925426602=Sistema+inmunol%C3%B3gico+deficiente&'
    embarazo = 'entry.925426602=Embarazo&'
    end_string =f'entry.900018422=su+salud&'\
                f'entry.826941713=2&'\
                f'entry.602591205=Saldr%C3%A9+igual&'\
                f'submit=Submit'
else:
      No se relaciona con personas de riesgo
    url =   "https://docs.google.com/forms/d/e/1FAIpQLSc5IoP6g9TtNkK9kBFp8VYlysEDfQ8Ij8gHwkMBut2aAMjJ8A/formResponse?"\
            "entry.1488779718=21&"\
            "entry.935746347=Cartago&"\
            "entry.926861655=Bachillerato+Universitario&"\
            "entry.985634184=1&"\
            "entry.1148479870=De+%C2%A2700000+a+%C2%A21200000&"\
            "entry.253307569=No&"\
            "entry.900018422=la+salud+de+los+dem%C3%A1s&"\
            "entry.826941713=3&"\
            "entry.602591205=Saldr%C3%A9+igual&"\
            "submit=Submit"   
            #EDAD
            #PROVINCIA
            #Escolaridad
            #Personas en vivienda
            #Ingresos
            #Se relaciona con personas con factores de riesgo
            #Razón de cuidados
            #Días de salida
            #Qué hará luego



# print(url_No_Risk)
# #Requests.post(url)


