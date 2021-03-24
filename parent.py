import requests
import json
resp = requests.get('https://saral.navgurukul.org/api/courses')
response = resp.json()
with open("saral.json","w") as all_content:
    json.dump(response,all_content,indent=4)
i=0
while i<len(response["availableCourses"]):
    course_name =response["availableCourses"][i]["name"]
    course_id =response["availableCourses"][i]["id"]
    print(i+1 ,course_name , "id" ,course_id)
    i+=1
user = int(input("Enter the number "))
print(response["availableCourses"][user-1]["name"])
_id = response["availableCourses"][user-1]["id"]

response = requests.get("https://saral.navgurukul.org/api/courses/"+str(_id)+"/exercises")
response_ex = requests.get(response.url)
my_dict=response_ex.json()

with open ("file.json","w") as id_exercises:
    json.dump(my_dict,id_exercises,indent=4)
i=0
while i<len(my_dict["data"]):
    parent_ex = my_dict["data"][i]["name"]
    print(i+1 , parent_ex)
    slug = my_dict["data"][i]["slug"]
    child = my_dict["data"][i]["childExercises"]
    if child==[]:
        print("    ", slug)
    j=0
    while j<len(my_dict["data"][i]["childExercises"]):
        child_ex=my_dict["data"][i]["childExercises"][j]["name"]
        print("    ", j+1,child_ex)
        j+=1
    i+=1    

user1 = int(input("Enter the parent number"))
parent_user = (my_dict["data"][user1-1]["name"])
print(parent_user)
i=0
while i<len(my_dict["data"][user1-1]["childExercises"]):
    if my_dict["data"][user1-1]["childExercises"]==[]:
        print("   ",my_dict["data"][user1-1]["slug"])
        break
    else:
        print("   ",i+1,my_dict["data"][user1-1]["childExercises"][i]["name"])
    i+=1

if my_dict["data"][user1-1]["childExercises"]==[]:
    print("   ",my_dict["data"][user1-1]["slug"])
    slug_input = input("Do you want the slug: Enter y or n ").lower()
    response_3 = requests.get("http://saral.navgurukul.org/api/courses/"+str(_id)+"/exercise/getBySlug?slug="+(my_dict["data"][user1-1]["slug"]))
    response_3 = requests.get(response_3.url)
    # print(response_3.url)
    new_dict=response_3.json()
    with open ("content.json","w") as all_content:
        json.dump(new_dict,all_content,indent=4)
    if slug_input=="y":
        print(new_dict["content"])
else:
    user2 = int(input("Enter the question number"))
    print(my_dict["data"][user1-1]["childExercises"][user2-1]["name"])
    response_3 = requests.get("http://saral.navgurukul.org/api/courses/"+str(_id)+"/exercise/getBySlug?slug="+(my_dict["data"][user1-1]["childExercises"][user2-1]["slug"]))
    # print(response_3)
    # print(response_3.url)
    response_3 = requests.get(response_3.url)
    new_dict=response_3.json()
    with open ("content.json","w") as all_content:
        json.dump(new_dict,all_content,indent=4)
    print(new_dict["content"])
    i=0
    while (True):
        user_input = input("Do you want to go to previous or next question : Enter p or n or else exit")
        if user_input=="p":
            response_3 = requests.get("http://saral.navgurukul.org/api/courses/"+str(_id)+"/exercise/getBySlug?slug="+(my_dict["data"][user1-1]["childExercises"][user2-2]["slug"]))
            response_3 = requests.get(response_3.url)
            new_dict=response_3.json()
            with open ("content.json","w") as all_content:
                json.dump(new_dict,all_content,indent=4)
            print(new_dict["content"])
            user2=user2-2
        elif user_input=="n":
            response_3 = requests.get("http://saral.navgurukul.org/api/courses/"+str(_id)+"/exercise/getBySlug?slug="+(my_dict["data"][user1-1]["childExercises"][user2]["slug"]))
            response_3 = requests.get(response_3.url)
            new_dict=response_3.json()
            with open ("content.json","w") as all_content:
                json.dump(new_dict,all_content,indent=4)
            print(new_dict["content"])
            user2=user2+1
        else:
            break
        i+=1
