# SEPSIS PREDICTION AND API CREATION WITH FASTAPI


## Project Description

**Sepsis** is a medical term which refers to any “generalized inflammatory response associated with a serious infection”. This lethal transmitted response occurs when the host's response to infection, systemic and severe inflammation of the body, causes damage to its own tissues and organs. It is accompanied by a cytokine shock1.
It is a potentially life-threatening condition that arises when the body's response to infection causes injury to its own tissues and organs. Risk factors include:
 
- being very young or old
- a weakened immune system from conditions such as cancer or diabetes, major trauma, and burns.

(Source : [Wikipedia](https://en.wikipedia.org/wiki/Sepsis))

## FastAPI Setup

Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**Python version 3.11 was used**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The two long command-lines have the same structure. They pipe multiple commands using the symbol ` ; ` but you can manually execute them one after the other.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that they can be imported into the python script and notebook without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run FastAPI

- Run the API (being at the repository root):
        
  FastAPI:
    
    - Main

          uvicorn src.main:app --reload 

    <!-- - Sepsis prediction

          uvicorn src.main:app --reload  -->


  - Go to your browser at the following address, to explore the API's documentation :
        
      http://127.0.0.1:8000/docs

## FastAPI Preview

Below is a preview showcasing some features of the FastAPI:

<div style="display: flex; align-items: center;">
    <div style="flex: 33.33%; text-align: center;">
        <p>FastAPI Top</p>
             <img src="https://github.com/bambadij/Sepsi_Predict_FastAPI/blob/main/src/input.png" alt="Middle" width="90%"/>
    </div>
    <div style="flex: 33.33%; text-align: center;">
        <p>FastAPI Input</p>
             <img src="https://github.com/bambadij/Sepsi_Predict_FastAPI/blob/main/src/input.png" alt="Top" width="90%"/>
        </div>
    <div style="flex: 33.33%; text-align: center;">
        <p>FastAPI Result</p>
        <img src="https://github.com/bambadij/Sepsi_Predict_FastAPI/blob/main/src/result.png" alt="Middle" width="90%"/>
        </div>
</div>

## Resources
Here are some ressources you would read to have a good understanding of FastAPI :
- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
  

## Author
[Bambo Traore](https://www.linkedin.com/in/traore-bamba/)
