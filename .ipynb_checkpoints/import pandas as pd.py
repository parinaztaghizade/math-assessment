import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pip install scipy
from scipy import stats
from scipy.stats import ttest_ind
import numpy as np

data = pd.read_csv(r"C:\Users\parin\Downloads\assessment_da25.csv")
data.head()