from fastapi import FastAPI
import joblib 
from pydantic import BaseModel
import pandas as pd
import os ,uvicorn
import logging

#load pipeline
pipeline  = joblib.load('toolkit/pipeline.joblib')
encoder  = joblib.load('toolkit/encoder.joblib')

# Configurer les logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#Create class to defineie our input
class SepsiFeature(BaseModel):
    PRG:float
    PL:float
    PR:float
    SK:float
    TS:float
    M11:float
    BD2:float
    Age:float
    Insurance : float
    


#ENDPOINTS
app = FastAPI()

@app.get("/home")
async def home():
    return 'hello word'

@app.post('/predict')
async def PredictSepsi(input:SepsiFeature):
    "function that receive the posted input data,do the operation and return an output /error message"
    output ={}   
    #try to execute the operation
    try:
        data = {
            'PRG': input.PRG,
            'PL':input.PL,
            'PR':input.PR,
            'SK':input.SK,
            'TS':input.TS,
            'M11':input.M11,
            'BD2':input.BD2,
            'Age':input.Age,
            'Insurance': input.Insurance,
        }
        
        df = pd.DataFrame([data])
        prediction = pipeline.predict(df)
        # print(f"[iNFO] Input data as dataframe:\n{prediction}")

        #Ml part
        if(prediction[0].tolist() ==0):
            response = "Negative"
        if(prediction[0].tolist() ==1 ):
            response ="Positive"
        # print(prediction)
        #format output
        output ={
            "data" : data,
            "operation" : "Addition",
            "way": "Sendind a data to predict",
            "result":response 
        }
    except ValueError as e :
        logger.error(f"ValueError: {e}")
        output ={ "error":str(e)}
        
    except Exception as e :
        output ={"error ": f"OOps something went wrong :\n{e}"}
    
    finally:
        return output # output must be json serializable

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)