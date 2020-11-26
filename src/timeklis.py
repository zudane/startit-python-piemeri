import requests
import pprint

# Dokumentācija: https://requests.readthedocs.io/en/master/


def vienkarss_get(url):
    r = requests.get(url)

    pprint.pprint("statusa kods: ", r.status_code)
    return r.json()


# joks = vienkarss_get("https://api.chucknorris.io/jokes/random?category=dev")
# pprint.pprint(joks["value"])

# lietotajs = vienkarss_get("https://randomuser.me/api/?nat=fi&inc=email,dob")
# pprint.pprint(lietotajs["results"])


def get_ar_parametriem(url, parametri):
    r = requests.get(url, params=parametri)
    return r.json()


# parami = {'nat': 'fi', 'inc': 'email,dob'}
# lietotajs2 = get_ar_parametriem("https://randomuser.me/api/", parami)
# pprint.pprint(lietotajs["results"])


# Testēšanai izmantojam https://docs.postman-echo.com/
# Šis API vienkārši atgriež visu ko mēs tam aizsūtām
# echo = get_ar_parametriem("https://postman-echo.com/get", parami)
# pprint.pprint(echo)


def vienkarss_post(url, dati):
    """Nosūta formas datus uz dotu API

    Args:
        url (string): API URL
        dati (dict): formas dati

    Returns:
        dict: API atbilde dict (json) formā
    """
    r = requests.post(url, data=dati)
    return r.json()


# formas_dati = {"vards": "Māris", "epasts": "maris@example.com"}
# echo2 = vienkarss_post("https://postman-echo.com/post", formas_dati)
# pprint.pprint(echo2)

