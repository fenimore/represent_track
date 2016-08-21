"""
A small, perhaps useless Python 3 wrapper
for the Govtrack.us API

Fenimore Love 2016
 MIT
"""
import requests, json

url_bill = "https://www.govtrack.us/api/v2/bill?"
url_person_by_id = "https://www.govtrack.us/api/v2/person/"
url_person = "https://www.govtrack.us/api/v2/person?q="
url_votes = "https://www.govtrack.us/api/v2/vote_voter/?person="
# Recent votes automatically limit 100, change limit up to 5999
url_person_recent_votes = "https://www.govtrack.us/api/v2/vote_voter/?order_by=-created&person="

warner_id = "412321" # PS: I'm from virginia...
kaine_id = "412582"

def get_votes_by_person_id(person_id):
    url = url_votes + person_id
    j = requests.get(url).json()
    return j

def get_person_by_id(person):
    """Get a Person profile by ID number """
    url = url_person_by_id + person
    r = requests.get(url)
    json_parsed = json.loads(r.text) # built in json
    return json_parsed

def get_person(name):
    """Get Person by name"""
    url = url_person + name
    r = requests.get(url)
    # json parsed is a dict type
    j = r.json()
    return j

def get_bill(branch, number, congress):
    """Get a bill from specificications
    
    Bill type could also be bill_type_label
    https://www.govtrack.us/api/v2/bill?number=1349
        &bill_type=senate_bill&congress=103

    Attributes:
    branch - house or senate either senate_bill or house_bill
    number - bill number id for govtrack
    congress - congress number
    """
    url = (url_bill + "bill_type=" + branch + "&number="
           + number + "&congress=" + congress)
    r = requests.get(url)
    j = r.json()
    return j # maybe this should return the first objects[0]?

def get_bill_title_by_id(bill_id):
    url = "https://www.govtrack.us/api/v2/bill/" + bill_id
    j = requests.get(url).json()  
    return j['title']

def get_recent_votes(person):
    url = url_person_recent_votes + person
    j = requests.get(url).json()
    return j['objects'] # list of dicts

def get_recent_votes_titled(person):
    url = url_person_recent_votes + person
    j = requests.get(url).json()
    votes = j['objects']
    for x in votes:
        print(x['option']['value'], ": ", x['vote']['question'])
        print('Related Bill ID: ', x['vote']['related_bill'], " | ",
              x['vote']['result'])
        print("----")

def test_votes():
    v = get_votes_by_person_id("412582")
    #print(type(v['objects'][0]))
    return v['objects']
    #for x in v['objects']:
        #print(x)
        #print(x[0]['value'])
        #for x in v['objects'][0]:
        #print(x['value']

def test_bill():
    """Get bill takes branch, number, congress
    fast-track is : 
    """
    b = get_bill("senate_bill", "1349", "103")
    # This should return a single bill
    bill = b['objects'][0]
    print(bill['title'])
        

def test_person():
    """Search by a name, and then list possible reps"""
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


        
if __name__ == "__main__":
    #test_bill()
    test_votes()

    
