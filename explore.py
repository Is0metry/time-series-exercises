import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from importlib import reload
import warnings
from typing import Tuple
warnings.simplefilter("ignore")

def split_data(df:pd.DataFrame,train_size:float)->Tuple[pd.DataFrame,pd.DataFrame]:
    train_sample = round(df.shape[0] * train_size)
    return df[:train_sample], df[train_sample:]
