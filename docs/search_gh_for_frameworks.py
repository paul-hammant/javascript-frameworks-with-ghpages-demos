import requests
from requests.auth import HTTPBasicAuth
import json
import time
import sys
import getpass

def search_for(framework):
    ctr = 0
    r = requests.get('https://api.github.com/search/repositories?q=' + framework, auth=HTTPBasicAuth(sys.argv[1], passwd))
    while(r is not None):
        ctr += 1
        try:
            for item in json.loads(r.text)['items']:
                result = {}
                result['framework'] = framework
                result['orgOrPerson'] = item['html_url'].split("/")[-2]
                result['repo'] = item['html_url'].split("/")[-1]
                result['desc'] = str(item['description'])
                result['stars'] = item['stargazers_count']
                open('search_results.json', 'a').write(json.dumps(result)+",\n")
        except KeyError:
            print (r.text)
            raise
        try:
            next = list(filter(lambda x:'rel="next"' in x, r.headers['Link'].split(",")))[0].split(">")[0].split("<")[1]
            time.sleep(3)
            r = requests.get(next, auth=HTTPBasicAuth(sys.argv[1], passwd))
        except KeyError:
            r = None
        except IndexError:
            r = None

if len(sys.argv) < 2:
    print("Error: You should pass your GitHub ID as the first arg")
    exit(10)

print("Enter your GH password:")

passwd = getpass.getpass()


search_for("Angular")
search_for("React")
search_for("Vue")
search_for("Ember")
search_for("Polymer")
search_for("Backbone")
search_for("Knockout")
search_for("Aurelia")
search_for("Mithril")
search_for("Marko")
search_for("Riot")
search_for("Inferno")
search_for("Ractive")
search_for("Flight")
search_for("Cycle")
search_for("Enyo")



