import sys

# python main.py Москва, ул. Ак. Королева, 12

toponym_to_find = " ".join(sys.argv[1:])

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
