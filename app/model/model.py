import pickle
import re
from pathlib import Path

# Version of model
__version__ = "0.1.0"

# get directory of current file (__file__) to make sure we find pkl file
BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl","rb") as f: 
    model = pickle.load(f)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kanada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish"
]

def predict_pipeline(text): # text is a string
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]] #access index of classes an return class