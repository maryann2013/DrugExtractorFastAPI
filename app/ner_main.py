import spacy
import en_core_med7_lg

med7 = en_core_med7_lg.load()

#==========Extract drug details using Med7 Library ==============
def extractDrugDetails(prescriptionText):
    doc=med7(prescriptionText)
    for ent in doc.ents:
        yield ent.text,ent.label_