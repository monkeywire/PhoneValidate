#!/usr/bin/python 
import httplib, urllib, json, sys
from MaltegoTransform import *

API_DOMAIN = "www.phone-validator.net"
API_URL = "/api/verify?"
API_KEY = "INSERT YOUR API KEY"

def validateNumber( phoneNumber, countryCode, locale):
    params = urllib.urlencode({ "PhoneNumber" : phoneNumber,
                                "CountryCode" : countryCode,
                                "Locale" : locale,
                                "APIKey" : API_KEY})

    conn = httplib.HTTPConnection(API_DOMAIN)
    url = API_URL + params
    conn.request("GET", API_URL + params)
    response = conn.getresponse()
    data = response.read()

    return json.loads(data)

#Read the input
phoneNumber = sys.argv[1]
countryCode = ""
locale = ""

#validate the number
data = validateNumber(phoneNumber, countryCode, locale)

#create and return the new transform
me = MaltegoTransform()
entity = me.addEntity("maltego.PhoneNumber", phoneNumber)
entity.addAdditionalFields("lineType", "Line Type", True, data["linetype"])
entity.addAdditionalFields("geoLocation", "GeoLocation", True, data["geolocation"])
entity.addAdditionalFields("regionCode", "Region", True, data["regioncode"])
entity.addAdditionalFields("nationalFormat", "Region Formated", True, data["formatnational"])
entity.addAdditionalFields("internationalFormat", "International Formated", True, data["formatinternational"])
me.returnOutput()

