import pandas as pd
import os

def load_data():
    slv = pd.read_csv('../solvers.csv')
    tsc = pd.read_csv('../testcases.csv')
    df = pd.merge(slv, tsc, on='testcase', how='left')

    df['slv_type'] = df['solver'].str.split().str[0]
    df['eps'] = df['solver'].str.extract(r'(\d+\.?\d*)').astype(float)

    df['ratio'] = df['answer_x']/df['answer_y']
    df['relative_error'] = ((df['answer_y']-df['answer_x'])/df['answer_y']).abs()
    
    df['size'] = df['testcase'].str[0].map(lambda x: 'small' if x =='f' else 'large')

    return df

