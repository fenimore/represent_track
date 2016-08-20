import requests

url_person = "https://www.govtrack.us/api/v2/person/"

warner = "412321"
kaine = "412582"

def get_person(person):
    """Get a Person profile by ID number """
    url = url_person + person

    r = requests.get(url)

    return r.text


if __name__ == "__main__":
    print(get_person(warner))
