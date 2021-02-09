import json

dictionaryJoke = {
    "type": "success",
    "value": {
        "id": 493,
        "joke": "Chuck Norris can binary search unsorted data",
        "categories": ["nerdy"]
    }
}

with open('exampleObj.json','w') as outfile:
    json.dump(dictionaryJoke, outfile, indent=4)