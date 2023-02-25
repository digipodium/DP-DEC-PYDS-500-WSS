'''
1. pip install streamlit --upgrade
2. create a python file 
3. write your code
4. streamlit run 'data_science\wapp.py'
'''

# libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# loading the dataset
@st.cache_data
def load():
    df = pd.read_csv('data_science/Pokemon.csv', index_col=1)
    df.drop(columns=['#'], inplace=True)
    return df

# main ui code

st.set_page_config(
    page_title='Pokemon Data Viz',
    layout='wide'
)

# - get the data 
with st.spinner('Loading Data...'):
    df = load()
    # st.snow()

# 2 columns 
c1, c2  = st.columns([6,4])
c1.header('Pokemon Dataset')
c1.dataframe(df)

c2.header("Pokemon Stats")
cnt_legendary = df['Legendary'].value_counts()[1]
cnt_types = df['Type 1'].value_counts()[1]
mst_cmn_type = df['Type 1'].value_counts().index[0]

c11, c12, c13 = c2.columns(3)
c11.metric('Total Pokemon', df.shape[0],'👻')
c12.metric('Legendary', cnt_legendary, '👻🦕🦖')
c13.metric('Most Common Type', cnt_types, mst_cmn_type)
c11.metric('Max Attack', df['Attack'].max(), '👻')
c12.metric('Max Defense', df['Defense'].max(), '👻')
c13.metric('Max HP', df['HP'].max(), '👻')
c11.metric('Max Sp. Atk', df['Sp. Atk'].max(), '👻')
c12.metric('Max Sp. Def', df['Sp. Def'].max(), '👻')
c13.metric('Max Speed', df['Speed'].max(), '👻')

# viz
st.header('Pokemon Graphically')
c1, c2 = st.columns([4,9])

# - select box
col1 = c1.selectbox('Select X-Axis Data', df.select_dtypes(exclude=['object']).columns)
col2 = c1.selectbox('Select Y-Axis Data', df.select_dtypes(exclude=['object']).columns)
col3 = c1.selectbox('Select Z-Axis Data', df.select_dtypes(exclude=['object']).columns)
color = c1.selectbox('Select Color', df.select_dtypes(include=['object',bool]).columns)

fig = px.scatter_3d(df, x=col1, y=col2, z=col3, color=color)
c2.plotly_chart(fig, use_container_width=True)

fig = px.area(df, x=df.index, y=col1, color=color, title=f'Pokemon Stats {col1} ')
st.plotly_chart(fig, use_container_width=True)
fig = px.area(df, x=df.index, y=col2, color=color, title=f'Pokemon Stats {col2} ')
st.plotly_chart(fig, use_container_width=True)
fig = px.area(df, x=df.index, y=col3, color=color, title=f'Pokemon Stats {col3} ')
st.plotly_chart(fig, use_container_width=True)