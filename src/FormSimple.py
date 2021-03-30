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
        7: random.randint(65,68),
    }
    return switcher.get(agegroup,"nothing")
#Returns a random province based on the probability distribution from the survey
def get_random_province():

    #Province probability distribution
    #Provinces
    population = ["San+Jos%C3%A9","Heredia","Alajuela","Cartago","Lim%C3%B3n","Puntarenas","Guanacaste"]
    #Probability of living in a province
    weights = [0.388,0.136,0.131,0.231,0.055,0.026,0.033]

    province = choices(population,weights)[0]
    return province
#Returns a random education level based on the probability distribution from the survey
def get_random_education_level(age):
    #education_level probability distribution
    #education_levels
    education_levels = ["Nulo","Escuela","Bachillerato+9%C2%B0","Bachillerato+11%C2%B0","Bachillerato+Universitario","Licenciatura"]
    #Probability of education_level
    weights = [0.002,0.005,0.026,0.398,0.288,0.281]
   
    #Adjusts to match the current age with an acceptable education level
    if age<=15:
        print("menor de 15")
        education_levels = education_levels[0:3]
        weights = weights[0:3]
    elif age<=18:
        print("menor de 18")
        education_levels = education_levels[0:4]
        weights = weights[0:4]
    elif age<=23:
        print("menor de 23")
        education_levels = education_levels[0:5]
        weights = weights[0:5]
    else:
        pass
    print(education_levels)
    print(weights)
    education_level = choices(education_levels,weights)[0]
    return education_level
#Returns a random number of habitants per house based on the probability distribution from the survey
def get_random_habitantsPerHouse():

    #habitantsPerHouse probability distribution
    #habitantsPerHouse
    habitantsPerHouse = [1,2,3,4,5,6,7,8,10]
    #Probability of habitantsPerHouse
    weights = [0.031,0.145,0.245,0.253,0.252,0.06,0.007,0.002,0.005]
    result = choices(habitantsPerHouse,weights)[0]
    return result
#Returns a random income range based on the probability distribution from the survey
def get_random_Income():

    #Income probability distribution
    #Income ranges
    income_groups= ["Menos+de+%C2%A2300000","De+%C2%A2300000+a+%C2%A2700000","De+%C2%A2700000+a+%C2%A21200000","M%C3%A1s+de+%C2%A21200000"]
    weights = [0.077,0.211,0.282,0.428]
    result= choices(income_groups,weights)[0]
    return result
#Returns if a person interacts with people with risk factors, based on the data from the survey
def with_riskFactor():

    #Probability of interacting with someone with risk factos
    prob= 0.671
    interacts=[True,False]
    weights = [0.671,0.329]
    return choices(interacts,weights)[0]
#Return a random reason of the selfcare of a person based on the data from the survey
def get_random_selfcare_motivation():

    #Probability of a given reason of the self care during the pandemic
    reasons = ["su+salud","la+salud+de+los+dem%C3%A1s","Ambas"]
    weights = [0.057,0.234,0.708]
    return choices(reasons,weights)[0]
#Returns a random number of time a person leaves the house based on the data from the survey
def get_random_departures_from_home():
    #Number of times a person leaves the house for non educational/work reasons
    times = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15]
    weights = [0.029,0.077,0.16,0.138,0.183,0.093,0.077,0.053,0.036,0.007,0.048,0.002,0.019,0.001,0.036] 
    return choices(times,weights)[0]
#Returns what a person's going to do after the 3rd group of vaccinations get vaccinated

def get_random_conclusion_after_vaccination():
    #Conclusions
    conclusions = ["Aumentar%C3%A1+las+veces+que+salga","Saldr%C3%A9+igual","Saldr%C3%A9+menos"]
    weights = [0.354,0.622,0.024]
    return choices(conclusions,weights)[0]

#Returns a random number of people who the surveyed person relations with based on the data from the survey
def get_random_risk_people():
    number_people = [1,2,3,4,5,6,8,10]
    weights = [0.313,0.298,0.209,0.113,0.053,0.004,0.004,0.007]
    return choices(number_people,weights)[0]

#Returns a random risk factor based on the data from the survey
def get_random_riskFactor():
    #Possible Risk Factors 
    while True:
        randomProb = random.randint(0,100)
        if randomProb<66:
            return "entry.925426602=Avanzada+edad&"
        randomProb = random.randint(0,100)
        if randomProb<49.3:
            return "entry.925426602=Hipertensi%C3%B3n&"
        randomProb = random.randint(0,100)
        if randomProb<27.7:
            return "entry.925426602=Obesidad&"
        randomProb = random.randint(0,100)
        if randomProb<36.2:
            return "entry.925426602=Diabetes&"
        randomProb = random.randint(0,100)
        if randomProb<24.8:
            return "entry.925426602=Asma&"
        randomProb = random.randint(0,100)
        if randomProb<9.6:
            return "entry.925426602=Padecimientos+pulmonares&"
        randomProb = random.randint(0,100)
        if randomProb<14.2:
            return "entry.925426602=Sistema+inmunol%C3%B3gico+deficiente&"
        randomProb = random.randint(0,100)
        if randomProb<10.3:
            return "entry.925426602=Embarazo&"
#General random results
random_age = get_random_age()
random_province = get_random_province()
random_education = get_random_education_level(random_age)
random_habitants = get_random_habitantsPerHouse()
random_income = get_random_Income()
interact_risk_factor = with_riskFactor()
selfcare_reason = get_random_selfcare_motivation()
times_leaves_house = get_random_departures_from_home()
conclusion_vaccination = get_random_conclusion_after_vaccination()

#Probability of interacting with someone with risk factors
url= ""
if interact_risk_factor:
    print("Hay")
    #se relaciona con personas de riesgo
    number_of_people_interacts = get_random_risk_people()
    print(number_of_people_interacts)
    #formResponse
    url = f'https://docs.google.com/forms/d/e/1FAIpQLSc5IoP6g9TtNkK9kBFp8VYlysEDfQ8Ij8gHwkMBut2aAMjJ8A/viewform?usp=pp_url&'\
        f'entry.1488779718={random_age}&'\
        f'entry.935746347={random_province}&'\
        f'entry.926861655={random_education}&'\
        f'entry.985634184={random_habitants}&'\
        f'entry.1148479870={random_income}&'\
        f'entry.253307569=S%C3%AD&'\
        f'entry.1517196595={number_of_people_interacts}&'
    i=0
    for i in range(number_of_people_interacts):
        riskFactor = get_random_riskFactor()
        url=url+riskFactor
    end_string =f'entry.900018422={selfcare_reason}&'\
                f'entry.826941713={times_leaves_house}&'\
                f'entry.602591205={conclusion_vaccination}&'\
                f'submit=Submit'
    url=url+end_string
else:
        print("No Hay")
      #No se relaciona con personas de riesgo
        url =   "https://docs.google.com/forms/d/e/1FAIpQLSc5IoP6g9TtNkK9kBFp8VYlysEDfQ8Ij8gHwkMBut2aAMjJ8A/viewform?"\
            f"entry.1488779718={random_age}&"\
            f"entry.935746347={random_province}&"\
            f"entry.926861655={random_education}&"\
            f"entry.985634184={random_habitants}&"\
            f"entry.1148479870={random_income}&"\
            f"entry.253307569=No&"\
            f"entry.900018422={selfcare_reason}&"\
            f"entry.826941713={times_leaves_house}&"\
            f"entry.602591205={conclusion_vaccination}&"\
            #"submit=Submit"   


print(url)
# # #Requests.post(url)


