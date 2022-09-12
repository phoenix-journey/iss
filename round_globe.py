# import statemnts. What we will use.
import requests
import json

# ISS class definition
class ISS():
    # Class to represent the International Space Station
    # initialize the class
    def __init__(self):
        # get the ISS location data
        response = requests.get("http://api.open-notify.org/iss-now.json")
        status_code = response.status_code
        # if the response was successful, parse the JSON data
        if status_code == 200:
            response_json = response.json()
            self.lat = response_json['iss_position']['latitude']
            self.lon = response_json['iss_position']['longitude']
        # if the response was not successful, print the status code and exit
        else:
            print("Error: " + str(status_code))
            exit(1)

    # return self.lat, self.lon
    def get_lat(self):
        return self.lat
    def get_lon(self):
        return self.lon

    # pretty print the ISS location
    def __str__(self):
        return "ISS location: latitude: {}, longitude: {}" \
                .format(self.get_lat(), self.get_lon())

# PositionRelativeToEarth class definition
class PositionRelativeToEarth():
    # Initialize the class
    def __init__(self, latitude, longitude):
        # get the position data
        response = requests.get(
                "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={}&longitude={}" \
                        .format(latitude, longitude))
        status_code = response.status_code
        # if the response was successful, parse the JSON data
        if status_code == 200:
            response_json = response.json()
            self.country = response_json['countryName']
            self.countryCode = response_json['countryCode']
            self.city = response_json['locality']
        # if the response was not successful, print the status code and exit
        else:
            print("Error: " + str(status_code))
            exit(1)

    # pretty print position
    def __str__(self):
        return "Position: country: {}, countryCode: {}, city: {}" \
                .format(self.country, self.countryCode, self.city)


# requests.get("http://api.open-notify.org/astros.json")
# who is in space?
def astros():
    # make the request
    response = requests.get("http://api.open-notify.org/astros.json")
    status_code = response.status_code
    # if the response was successful, parse the JSON data
    if status_code == 200:
        data = response.json()
        # Get number of people in space.
        number = data["number"]
        print("Number of people in space: {}".format(number))
        people = data["people"]
        # Print people in space.
        print("People in space: ")
        for person in people:
            print(person["name"])
    # if the response was not successful, print the status code and exit
    else:
        print("Error: " + str(status_code))
        exit(1)

# main function
def main():
    astros()
    iss = ISS()
    print(f"{iss}")
    position = PositionRelativeToEarth(iss.lat, iss.lon)
    print(position)

# call main function only if this file is executed
if __name__ == '__main__':
    main()

