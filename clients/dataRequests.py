import requests

data = {"api_key": "3971c1a15e8449ef7c5e0486471c63cd"}


def getClinics():
    r = requests.post(r"https://app.rnova.org/api/public/getClinics", data=data)

    return r.json()


def getProfessions():
    r = requests.post(r"https://app.rnova.org/api/public/getProfessions", data=data)

    return r.json()


def getUsers(clinic_id, profession_id, role):
    users_data = data.copy()
    users_data["clinic_id"] = clinic_id
    users_data["profession_id"] = profession_id
    users_data["role"] = role

    r = requests.post(r"https://app.rnova.org/api/public/getUsers", data=users_data)

    return r.json()
