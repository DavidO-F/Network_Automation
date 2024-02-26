# Date: 28/12/2023
# Author: David O. Folorunsho
# ISS: International Space Station

import requests

# response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

# print(response.status_code)

response = requests.get("https://api.open-notify.org/astros.json")
print(response.status_code)