import requests, json

url_person_by_id = "https://www.govtrack.us/api/v2/person/"
url_person = "https://www.govtrack.us/api/v2/person?q="


warner_id = "412321"
kaine_id = "412582"

def get_person_by_id(person):
    """Get a Person profile by ID number """
    url = url_person_by_id + person
    r = requests.get(url)
    json_parsed = json.loads(r.text)
    return json_parsed

def get_person(name):
    """Get Person by name"""
    url = url_person + name
    r = requests.get(url)
    # json parsed is a dict type
    json_parsed = json.loads(r.text)
    # In meta, total count means
    # that there have been that many matches
    # In 'kaines' case, that is only one
    # Brian is 7...
    return json_parsed


if __name__ == "__main__":
    kaine = get_person("brian")
    print(kaine)
