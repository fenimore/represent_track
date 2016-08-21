import requests, json

url_bill = "https://www.govtrack.us/api/v2/bill?"
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
    return j

def get_bill(branch, number, congress):
    """Get a bill from specificications
    
    Bill type could also be bill_type_label
    https://www.govtrack.us/api/v2/bill?number=1349
        &bill_type=senate_bill&congress=103

    Attributes:
    branch - house or senate
    number - bill number
    congress - congress number
    """
    url = (url_bill + "bill_type=" + branch + "&number="
           + number + "&congress=" + congress)
    r = requests.get(url)
    j = r.json()
    return j # maybe this should return the first objects[0]?


def test_bill():
    """Get bill takes branch, number, congress"""
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
    test_bill()
