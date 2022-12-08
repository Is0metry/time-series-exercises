import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from importlib import reload
import requests

def get_all_api(api:str,req:str)->pd.DataFrame:
    json = requests.get(api + req).json()
    results = json['results']
    while json['next'] is not None:
        json = requests.get(json['next']).json()
        results += json['results']
    return pd.DataFrame(results)
