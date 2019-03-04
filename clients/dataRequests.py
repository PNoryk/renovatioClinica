import requests

data = {"api_key": "3971c1a15e8449ef7c5e0486471c63cd"}


def getClinics():
    r = requests.post("https://app.rnova.org/api/public/getClinics", data=data)

    return r.json()


def getProfessions():
    r = requests.post("https://app.rnova.org/api/public/getProfessions", data=data)

    return r.json()


def getUsers(clinic_id, profession_id, role):
    users_data = data.copy()
    users_data["clinic_id"] = clinic_id
    users_data["profession_id"] = profession_id
    users_data["role"] = role

    r = requests.post("https://app.rnova.org/api/public/getUsers", data=users_data)

    return r.json()


def getSchedule(clinic_id, user_id, time_start, time_end, step):
    users_data = data.copy()
    users_data["clinic_id"] = clinic_id
    users_data["user_id"] = user_id
    users_data["time_start"] = time_start
    users_data["time_end"] = time_end
    users_data["step"] = step

    r = requests.post("https://app.rnova.org/api/public/getSchedule", data=users_data)

    return r.json()
