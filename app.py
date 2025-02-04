import phonenumbers
from phonenumbers import geocoder
from phonenumbers.timezone import time_zones_for_number
from phonenumbers.geocoder import description_for_number 
from phonenumbers.carrier import name_for_number 

number= input("Enter the Number: ")
phone = phonenumbers.parse(number)
time = time_zones_for_number(phone)
sim_details = name_for_number(phone, "en")
register = geocoder.description_for_number(phone, "en")

print(register)
print(phone)
print(time)
print(sim_details)
print(register) 