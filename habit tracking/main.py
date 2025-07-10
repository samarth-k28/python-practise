import requests
import datetime

GENDER = 'male'
WEIGHT_KG = 74
HEIGHT_CM = 180
AGE = 18

APP_ID = 'b0118d1c'
API_KEY = 'efeca4c907dce8d63bdeaee2c4ad9022'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
today = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")
for exercise in result['exercises']:
    sheet_input = {'workout': {'date': today, 'time': time, 'exercises': exercise['user_input'].title(), 'duration': exercise['duration_min'], 'calories': exercise['nf_calories']}}

    sheet_response = requests.post('https://api.sheety.co/fff0192390abbd49ca74ac07011b9ac1/copyOfMyWorkouts/workouts', json=sheet_input)
    print(sheet_response.text)
