import matplotlib.pyplot as plt
import seaborn as sns
import os

def plt_qlt(df, path='datavisualization'):
    
    os.makedirs(path, exist_ok=True)
