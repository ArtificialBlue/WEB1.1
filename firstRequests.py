import requests

#Text Response Object
result1 = requests.get("http://127.0.0.1:3000/")
print("base result 1 Print === ", result1)

result1_text = result1.text
print(result1_text)

#JSON Response Object
result2 = requests.get("http://127.0.0.1:3000/jsonExample")
print("base result 2 Print === ", result2)

result2_json = result2.json()
print(result2_json)