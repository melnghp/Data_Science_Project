import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import joblib
from streamlit_option_menu import option_menu

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(page_title = "My Webpage", layout="wide")

header = st.container()
dataset = st.container()
attack = st.container()

graph = st.container()
IP = st.container()
predict = st.container()

with st.sidebar:
    choose = option_menu(None, ["Intro", "Data","EDA", "Model & Evaluation", "Let's Try", "Conclusion"],
                        icons=['hdd-rack-fill', "server", 'bar-chart-fill','graph-up', 'nintendo-switch','ethernet'],
                        menu_icon="app-indicator", default_index=0, orientation="horizontal",
                        styles={
                            "container": {"padding": "5!important", "background-color": "#fafafa"},
                            "icon": {"color": "orange", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#02ab21"},
                        }
    )

if choose == "Intro":
    with header:
        st.title("Intrusion Detection System - Classification of Network Traffic")
        st.subheader("Background")
        st.markdown("""
        With increasing cases of cyber attacks, it is important to identity irregular or abnormal network traffic. 
        A network-based intrusion detection system (NIDS) is usually in place after the firewall to analyse inbound and outbound network packets 
        for patterns of malicious behavior. The NIDS passively collects data and analyse to determine whether the information falls outside normal 
        activity based on a knowledge base. If so, an alert is sent ([source](https://ukdiss.com/examples/intrusion-prevention-security.php)).
        """)    
        st.markdown(""" As such, it is important for NIDS to be accurate in classifying network traffic as high false positive (classifying normal 
        traffic as attacks) may result in operational overhead whereas high false negative (classifying attacks as normal traffic) may lead to 
        prolonged attack continue to go undetected and further conpromising the environment.
        """)
        
        st.subheader("Problem Statement")


        st.write("")

elif choose == "Data":

    with dataset:
        st.header("Data Source and Cleaning")
        
        st.subheader("Data selection")

        st.write("The raw dataset is made up of 4 CSV files with a total of 2,540,044 records.")

        data = {'Date': ['18-02-2015', '22-01-2015', '23-01-2015'], 
        'Records': ['1,035,294', '989,104', '33,930'],
        'Normal': ['91.8%', '98.6%', '100%'],
        'Attack': ['8.22%', '1.44%', '0%']}    
        
        tb = pd.DataFrame(data)

        st.table(tb)


        #load and remove space
        raw = joblib.load('dataset/combined_df.pickle')
        df_obj = raw.select_dtypes(['object'])
        raw[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    
        st.subheader("Missing Values")
        percent_null = round(raw.isnull().sum() * 100 / len(raw),2)
        missing_value_df = pd.DataFrame({'count_null': raw.isnull().sum(), 'percent_null': percent_null}).sort_values("percent_null", ascending = False).reset_index()
        
        mv = px.bar(missing_value_df, x='index',y='percent_null')
        mv.xlabel(None)
        mv.ylabel(None)

        st.write(mv)

        st.markdown("Impute missing values")

  

elif choose == "EDA":
    
    df = joblib.load('dataset/train.pickle')

    with attack:
        
        st.header("Data Exploration")

        pie, time = st.columns((1,2))

        with pie:
            st.subheader("Distribution of Network Types")

            fig, ax = plt.subplots(figsize = (10,4))

            p1 = joblib.load('chart/pie.pickle')

            ax = px.pie(p1, values='label', names='index', hole=0.4, color ='index', color_discrete_map={'normal':'green', 'attack':'firebrick'})
            ax.update_layout(showlegend=False, autosize= True,
            # Add annotations in the center of the donut pies.
            annotations=[dict(text='Traffic Type', x=0.5, y=0.5, font_size=15, showarrow=False)])

            ax.update_traces(textposition='inside', textinfo='percent+label')

            st.write(ax)

        with time:

            st.subheader("Number of traffic per hour by type")

            fig, ax = plt.subplots(figsize = (10,4))

            t1 = joblib.load('chart/time.pickle')

            ax = sns.barplot(data=t1, x="hour",y='attack_cat', hue="label", palette = ['tab:green', 'tab:red'])
            for container in ax.containers:
                    ax.bar_label(container)

            plt.xlabel(None)
            plt.ylabel(None)
            #st.write(time)
            st.pyplot(fig)

            
    # dist= st.container()        
    # with dist:
        
        # selected_fea1 = st.selectbox('Select source feature:', [None, 'dur', 'sbytes', 'sloss','swin']) 
        # selected_fea2 = st.selectbox('Select destination feature:', [None,'dur', 'dbytes', 'dloss','dwin']) 
        # selected_split = st.selectbox('Select split:', [True, None])

        # fig, ax = plt.subplots(2,2,figsize = (16,4)) 

        # vp = pd.melt(df, value_vars=[selected_fea1, selected_fea2], id_vars='label')
        # ax = sns.violinplot(y='variable', x='value', hue='label', data=vp, split=selected_split, inner="quart", palette = ['tab:green', 'tab:red'])
        
        # plt.xlabel(None)
        # plt.ylabel(None)
        
        # st.pyplot(fig)

    with IP:
        
        st.subheader("Distribution")

        v1 = px.violin(df[['label','sbytes']], y="label", x="sbytes", color='label',
                    color_discrete_map={'attack':'firebrick', 'normal':'green'},
                    hover_data=df[['label','sbytes']].columns,
                    width=800, height=400)
        st.write(v1)


    with graph:

        st.subheader("Network Graph")


#elif choose == "Model & Evaluation ":


elif choose == "Let's Try":
    with predict:
        
        st.header("")
        st.subheader("Let's classify!")

        file = st.file_uploader("Choose a CSV file")

        if file is not None:
            df1=pd.read_csv(file)

        else:
            st.warning("You need to upload a csv file.")
    



#elif choose == "Conclusion":
