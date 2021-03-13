import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    wdata =  (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={'FISCAL_YEAR':'year', 'HEALTH_AUTHORITY': 'h_a', 'HOSPITAL_NAME':'hosp', 'PROCEDURE_GROUP': 'prcd', 'WAITING':'waiting', 'COMPLETED': 'comp', 'COMPLETED_50TH_PERCENTILE': 'wait_med', 'COMPLETED_90TH_PERCENTILE':'wait_90'})
        .dropna()
)
    
    wdata['waiting'] = (
                  wdata['waiting'].str.replace(',','')
                                .str.replace('<5','3')
)

    wdata['comp'] = (
               wdata['comp'].str.replace(',','')
                          .str.replace('<5','3')
)

    wdata['waiting'] = pd.to_numeric(wdata['waiting'])
    wdata['comp'] = pd.to_numeric(wdata['comp'])
    

    ddata = wdata.assign(wait_median_d = wdata['wait_med']*7)
    ddata = ddata.assign(wait_90_d = wdata['wait_90']*7)
    
    return ddata


<<<<<<< HEAD
def no_summation_base_data(df):
    df_base = df[~(df['h_a'] == 'All Health Authorities')] 
    df_base = df_base[~(df_base['hosp'] == 'All Facilities')] 
    df_base = df_base[~(df_base['prcd'] == 'All Procedures')]
    
    return df_base

def no_duplicates_all_h_a(df):
    df_h_a = df[(df['h_a'] == 'All Health Authorities')]
    df_h_a = df_h_a[~(df_h_a['prcd'] == 'All Procedures')]
    #This is to remove the duplicate summation data of "All Procedures"
    
    return df_h_a

def no_duplicates_all_prcd(df):
    # This gives us the "All Procedure" data for each hospital
    df_prcd = df[(df['prcd'] == 'All Procedures')]
    df_prcd = df_prcd[~(df['hosp'] == 'All Facilities')] 
    
    return df_prcd
=======

def main_Allsummary_data(wd):
    wd_all = wd[(wd['h_a'] == 'All Health Authorities') & (wd['prcd'] == 'All Procedures')]
    return wd_all



def basic_data(wd):
    wd = wd[~(wd['h_a'] == 'All Health Authorities')] 
    wd = wd[~(wd['hosp'] == 'All Facilities')] 
    wd = wd[~(wd['prcd'] == 'All Procedures')]
    return wd



def all_procd(wd):
    wd_all_prcd = wd[(wd['prcd'] == 'All Procedures')]
    wd_all_prcd = wd_all_prcd[~(wd_all_prcd['hosp'] == 'All Facilities')] 
    return wd_all_prcd
    
    
    
def all_h_a:
    wd_all_ha = wd[(wd['h_a'] == 'All Health Authorities')]
    wd_all_ha = wd_all_ha[~(wd_all_ha['prcd'] == 'All Procedures')]
    return wd_all_ha
>>>>>>> f195a1c3371d2ff9e6c0019895f5caece905a49c
