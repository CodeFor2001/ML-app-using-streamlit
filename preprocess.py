# -*- coding: utf-8 -*-
"""
Created on Wed May 12 06:56:02 2021

@author: saniy
"""

import  streamlit as st
import pandas as pd



#layout 
st.set_page_config(page_title= "Data Preprocessing", layout = 'wide')

st.title("Data Preprocessing")

# Sidebar - Collects user input features into dataframe
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV or Excel file", type=["csv","xlsx"])
    
df = pd.read_csv(uploaded_file)
 #([col],dtype)


def drop_col(df):
    col_list = df.columns
    options = st.multiselect("Select the columns you wanna drop", col_list)
    df  = df.drop(options,axis = 'columns')
    st.write("Dataset after dropping selected columns")
    st.write(df.head(5))
    return df
    
def replace_null(df):
    col_list = df.columns
    rep_col = st.selectbox("Select the columns you want to replace null values in", col_list)
    value = st.text_input("Replace null values with : ")
    values = {rep_col:value}
    df = df.fillna(value = values)
    return df

def rename_col(df):
    col_list = df.columns
    old_col = st.multiselect("Select the column you want to rename", col_list)
    for i in range(len(old_col)):
        new_col = st.text_input("Enter the new column name for column: ",old_col[i])
        df = df.rename(columns = {old_col[i]:new_col})
    st.write("Dataset after renaming the column")
    st.write(df.head(5))
    return df
    
# def split_column(df):
#     split_col = st.selectbox("Select the columns you want to split based on a delimiter", col_list)
#     delim = st.text_input("Enter the delimiter: ",value = ",")
#     new_col = st.text_input("Enter the name of new column: ")
#     df[[split_col,new_col]] = df[split_col].str.split(delim,expand=True)
#     st.write("Dataset after renaming the column")
#     st.write(df.head(5)) 

    
# Displays the dataset
st.subheader('1. Dataset')

if uploaded_file is not None:
    
    st.markdown('**1.1. Glimpse of dataset**')
    st.write("Below table contains first and last five rows of the dataset")
    st.write(df.head(5))
    st.write(df.tail(5))
    
    st.markdown('**1.2 Shape of the dataset (rows,columns)**')
    st.info(df.shape)
    
    st.markdown('**1.3 Description of the dataset**')
    st.write(df.describe())
    
    st.markdown("**1.4 Drop the duplicates**")
    df = df.drop_duplicates()
    st.write("After dropping the duplicates the shape of the dataset is", df.shape)
    
    
    st.markdown("**1.5 Do you want to drop any columns ?**")
    yes = st.checkbox("Yes", value=False)
    if yes:
        df = drop_col(df)
        
    st.markdown("**1.6 Number of Null values in the dataset columns**")
    st.write("*** There are null values in ***")
    col_list = df.columns
    for i in range(len(col_list)):
        if pd.isnull(col_list[i]):
            st.write(col_list[i])
    
    st.markdown("**1.7 Replace the null values**")
    Yes = st.checkbox("Yes  ", value=False)
    if Yes:
        df = replace_null(df)
        
    st.markdown("**1.8 Rename the columns**")
    Yes = st.checkbox("Yes ", value = False)
    if Yes:
        df =  rename_col(df) 
    
    # st.markdown("**1.5 Do you want to drop any columns ?**")
    # yes = st.checkbox(" Yes", value=False)
    # if yes:
    #     df = drop_col(df)
        
        
    # st.markdown("**1.9 Split a column based on a delimiter**")
    # Yes = st.checkbox("Yes   ", value = False)
    # if Yes:
    #     split_column(df) 
    
        
else:
    st.write("Awaiting the upload of the dataset")
    
    
    
    
    

    
