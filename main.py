from src.timeklis import vienkarss_get, vienkarss_post


# 1. solis
# vienkārši GET pieprasījumi no API, kas atgriež json formāta atbildi
# joks = vienkarss_get("https://api.chucknorris.io/jokes/random?category=dev")
# pprint.pprint(joks["value"])

# lietotajs = vienkarss_get("https://randomuser.me/api/?nat=fi&inc=email,dob")
# pprint.pprint(lietotajs["results"])


# 2.solis
# GET, bet izmantojot parametrus, nevis pašam taisot URL
# parami = {'nat': 'fi', 'inc': 'email,dob'}
# lietotajs2 = get_ar_parametriem("https://randomuser.me/api/", parami)
# pprint.pprint(lietotajs["results"])

# 3.solis
# GET ar parametriem uz labu testēšanas API
# Testēšanai izmantojam https://docs.postman-echo.com/
# Šis API vienkārši atgriež visu ko mēs tam aizsūtām
# echo = get_ar_parametriem("https://postman-echo.com/get", parami)
# pprint.pprint(echo)

# 4. solis
# Piemērs POST ar formas datiems
# formas_dati = {"vards": "Māris", "epasts": "maris@example.com"}
# echo2 = vienkarss_post("https://postman-echo.com/post", formas_dati)
# pprint.pprint(echo2)
