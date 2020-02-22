# IMPORTS
import requests, datetime

# CONSTANTS
HOST_NAME = "https://www.gmp365.io/api/"
USERNAME = "xx"
PASSWORD = "xx"

# FUNCTION DEFINITIONS

def log_in():
    return return_post_as_text("login", {"username": USERNAME, "password": PASSWORD})

def get_countries(token, year = datetime.datetime.now().year):
    return return_post_as_json(token, "v1/countries/year/" + year)

def get_years(token, country = None):
    url = ""
    if country is None:
        url = "v1/years"
    else:
        url = "v1/years/country/" + country
    return return_get_as_json(token, url, params)

def get_brands(token, country, year):
    return return_get_as_json(token, ("v1/brands/country/%s/%s" % (country, year)))

def get_campaigns(token, country, year):
    return return_get_as_json(token, ("v1/campaigns/country/%s/%s" % (country, year)))

def get_campaign(token, country_id):
    return return_get_as_json(token, ("v1/campaigns/%s" % country_id))

def get_media_plan(token, type):
    return return_get_as_json(token, ("v1/%s/plans/" % type))


def return_post_as_text(url, params):
    r = requests.post(url=HOST_NAME + url, json=params)
    return r.text

def return_get_as_json(token, url, params):
    headers = {"X-auth": token}
    if params is None:
        r = requests.get(url=HOST_NAME + url, headers=headers)
    else:
        r = requests.get(url=HOST_NAME + url, headers=headers, json=params)
    return r.json

# RUNTIME

token = log_in()


# extracting latitude, longitude and formatted address
# of the first matching location
#latitude = data['results'][0]['geometry']['location']['lat']
#longitude = data['results'][0]['geometry']['location']['lng']
#formatted_address = data['results'][0]['formatted_address']

# printing the output
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#      % (latitude, longitude, formatted_address))



