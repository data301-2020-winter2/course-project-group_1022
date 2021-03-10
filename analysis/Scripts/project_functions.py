import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    wdata =  (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={'FISCAL_YEAR':'year', 'HEALTH_AUTHORITY': 'h_a', 'HOSPITAL_NAME':'hosp', 'PROCEDURE_GROUP': 'prcd', 'WAITING':'waiting', 'COMPLETED': 'comp', 'COMPLETED_50TH_PERCENTILE': 'wait_med', 'COMPLETED_90TH_PERCENTILE':'wait_90'})
        .dropna()
)

    ddata = wdata.assign(wait_median_d = wdata['wait_med']*7)
    ddata = ddata.assign(wait_90_d = wdata['wait_90']*7)
    
    return ddata


