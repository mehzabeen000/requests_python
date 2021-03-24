import requests
import json
r = requests.get('https://saral.navgurukul.org/api/courses')
response = r.json()

i=0
while i<len(response["availableCourses"]):
    abc =response["availableCourses"][i]["name"]
    xyz =response["availableCourses"][i]["id"]
    print(i+1 ,abc , "id" ,xyz)
    i+=1
user = int(input("Enter the number "))
print(response["availableCourses"][user-1]["name"])