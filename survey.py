import json

#This is the Master Survey List that I REFERENCE BY THE SURVEY RESPONDENT"S NAME
surveys_by_name = {}


consent_to_survey = False

has_the_time = input("Do you have the time to conduct a survey? ")

if has_the_time == "yes" or has_the_time == "Yes":
    consent_to_survey = True


#this is one survey
while consent_to_survey == True:
    survey_q = {}
# overall questions: What are teens like today?
    survey_q["name"] = input("What"s your name?")
    survey_q["age"] = input("How old are you?")
    survey_q["shows"] = input("What is one of your favorite TV shows?")
    survey_q["social media apps"] = input("What is your preferred social media app?")
    survey_q["sport brands"] = input("Do you prefer Nike or Adidas?")
    survey_q["comics"] = input("Marvel or D.C.?")
    survey_q["pets"] = input("Do you like cats or dogs?")
    survey_q["fav summer hits"] = input("What is one of your favorite summer hits?")
    survey_q["sun"] = input("sunrise or sunset?")
    survey_q["schedules"] = input("Are you a morning person or a night owl?")

    surveys_by_name[survey_q["name"]] = survey_q
   
    continue_survey = input("Would your friend like to conduct a survey? (yes or no)")
    if continue_survey != "yes" and continue_survey != "Yes":
        consent_to_survey = False
        print("Thank you for your time")
        break

print ("completed surveys:", surveys_by_name)
#at this point, we have all the surveys that we want to get, and we want to save them in a differnt file.

fp = open("survey_responses.json", "r")
old_surveys = json.load(fp)
#print (old_surveys)
for key in surveys_by_name.keys():
    old_surveys[key] = surveys_by_name[key]
#print (old_surveys)
fp.close()

fp = open("survey_responses.json", "w")
json.dump(old_surveys, fp)
fp.close()


print("Thank you for your time")