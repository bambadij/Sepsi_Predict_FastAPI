from fastapi import FastAPI,HTTPException,Response,status
import joblib 
from pydantic import BaseModel
import pandas as pd
import os ,uvicorn
import logging
from fastapi.middleware.cors import CORSMiddleware



# Additional information to include in app description
Util_info = """
- PRG: Plasma Glucose
- PL: Blood Work Result-1 (mu U/ml)
- PR: Blood Pressure (mm Hg)
- SK: Blood Work Result-2 (mm)
- TS: Blood Work Result-3 (mu U/ml)
- M11: Body Mass Index (weight in kg/(height in m)^2)
- BD2: Blood Work Result-4 (mu U/ml)
- Age: Patient's Age (years)
- Insurance: If a patient holds a valid insurance card

Output:
- Sepsis: Positive if a patient in ICU will develop sepsis, Negative if a patient in ICU will not develop sepsis.
"""

# APP
app = FastAPI(
    title='Sepsis Prediction App',
    description= Util_info
)

origins = [
    "*",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
#load pipeline
pipeline  = joblib.load('toolkit/pipeline.joblib')
encoder  = joblib.load('toolkit/encoder.joblib')

# Configurer les logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#Create class to define our input
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

@app.get("/")
async def home():
    return 'hello word'

@app.post('/predict',status_code=status.HTTP_201_CREATED)
async def PredictSepsi(input:SepsiFeature):
    "function that receive the posted input data,do the operation and return an output /error message"
    # output ={}   
    #try to execute the operation
    try: 
        
        df = pd.DataFrame([input.model_dump()])
        prediction = pipeline.predict(df)
        predict_proba = pipeline.predict_proba(df) 
        # print(f"[iNFO] Input data as dataframe:\n{prediction}")
        decoder_prediction = encoder.inverse_transform([prediction])
        #Ml part
        print(f"[iNFO] Input data as dataframe:\n{decoder_prediction.tolist()}")
        #format output
        return {
            "data" : input,
            "operation" : "Addition",
            "way": "Sendind a data to predict",
            "proba_predict" : predict_proba[0].tolist(),
            "result":decoder_prediction.tolist() 
        } 
    except ValueError as e :
        logger.error(f"ValueError: {e}") 
        return { "error":str(e)}
        
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f'this is a server error contact administrator {str(e)}')     

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0" ,port=8000,reload=True)