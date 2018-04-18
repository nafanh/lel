import json
import requests
from pprint import pprint
url = 'http://exac.hms.harvard.edu/rest/gene/variants_in_gene/ENSG00000049656'
response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)
freq = {}
for i in range(len(data)):
    temp = data[i]["pop_acs"]
    for ethnicity in (temp):
        if ethnicity in freq:
            freq[ethnicity] += temp[ethnicity]
        else:
            freq[ethnicity] = temp[ethnicity]

pprint(freq)
print(sum(freq.values()))
#pprint(data[1])