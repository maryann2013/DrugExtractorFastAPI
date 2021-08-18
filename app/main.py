import uvicorn
  
from typing import List,Dict
from fastapi import FastAPI ,HTTPException
import ner_main

app=FastAPI(
    title="Drug Extraction",
    description="Extracting drug details from clinical text"
)


@app.get('/extractDrug')
def extractDrug(text:str):
    output=list(ner_main.extractDrugDetails(text))
    result={"Drug Details":output}
    return result