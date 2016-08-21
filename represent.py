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
    j = r.json()
    # In meta, total count means
    # that there have been that many matches
    # In 'kaines' case, that is only one
    # Brian is 7...
    return j


if __name__ == "__main__":
    #p = get_person("brian") # There are seven
    p = get_person("kaine")  # There is one
    count = int(p['meta']['total_count'])
    if count > 1:
        print('There are ', count, ' in total')
        #print(p['objects'][0]['name'])
        print('Did you mean?')
        for x in range(0, count):
            # Did you mean
            perso = p['objects'][x]
            print(x+1, perso['name'], perso['id'])
    else:
        print(p['objects'][0]['name'])
        
