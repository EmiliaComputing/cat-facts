import urllib.request
import json
import ssl
import random

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://cat-fact.herokuapp.com/facts'
response = urllib.request.urlopen(url)
json_data = response.read()
cat_data = json.loads(json_data)
all_facts = cat_data['all']

while True:
    prompt = input('press enter to get a random cat fact')
    random_fact = random.choice(all_facts)
    print(random_fact['text'])
    print()
