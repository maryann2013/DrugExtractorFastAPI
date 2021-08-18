import requests as req

input_text="Levothyroxine 100mg daily for next 5 days"
input_keys={"text":input_text}

extract_NER=req.get('http://127.0.0.1:8000/extractDrug/',params=input_keys)

results=extract_NER.json()
print(results["Drug Details"])