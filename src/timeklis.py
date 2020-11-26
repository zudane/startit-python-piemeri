import requests
import pprint

# Dokumentācija: https://requests.readthedocs.io/en/master/


def vienkarss_get(url):
    r = requests.get(url)

    pprint.pprint("statusa kods: ", r.status_code)
    return r.json()


def get_ar_parametriem(url, parametri):
    r = requests.get(url, params=parametri)
    return r.json()


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
