import requests

data = {"api_key": "3971c1a15e8449ef7c5e0486471c63cd"}
error = {"error": 1,
         "data": {"code": 503,
                  "desc": "Service Unavailable"}}


def getClinics():
    try:
        r = requests.post("https://app.rnova.org/api/public/getClinics", data=data)
        return r.json()

    except requests.exceptions.ConnectionError:
        return error


def getProfessions():
    try:
        r = requests.post("https://app.rnova.org/api/public/getProfessions", data=data)
        return r.json()

    except requests.exceptions.ConnectionError:
        return error


def getUsers(clinic_id, profession_id, role):
    users_data = data.copy()
    users_data["clinic_id"] = clinic_id
    users_data["profession_id"] = profession_id
    users_data["role"] = role

    try:
        r = requests.post("https://app.rnova.org/api/public/getUsers", data=users_data)
        return r.json()

    except requests.exceptions.ConnectionError:
        return error


def getSchedule(clinic_id, user_id, time_start, time_end, step):
    users_data = data.copy()
    users_data["clinic_id"] = clinic_id
    users_data["user_id"] = user_id
    users_data["time_start"] = time_start
    users_data["time_end"] = time_end
    users_data["step"] = step

    try:
        r = requests.post("https://app.rnova.org/api/public/getSchedule", data=users_data)
        return r.json()

    except requests.exceptions.ConnectionError:
        return error
