# making a streamlit app to visualize any kind of dataset an user wants to visualize

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Title of the app
st.title("Dataset Visualizer")

# App settings
st.set_option('deprecation.showPyplotGlobalUse', False)


# asking user to upload the dataset, defaul value iris.csv
uploaded_file = st.file_uploader("Choose a CSV file", type="csv", key="1")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("iris.csv")

# asking user whether to visualize the dataset or not
if st.checkbox("Visualize the dataset"):
    st.write(df)


# showing the shape of the dataset
st.write("Shape of the dataset")
st.write(df.shape)

# show the dataset statistics and summary
if st.checkbox("Show the dataset statistics and summary"):
    st.write(df.describe())

# asking user to select the columns to visualize
st.write("Select the columns to visualize")
cols = st.multiselect("Columns", df.columns.tolist())

if cols:
    st.write(df[cols])

# show checkboxes to show values and datatype of the columns
if st.checkbox("Show datatypes of the columns"):
    st.write(df.dtypes)

# Summarize the dataset
if st.checkbox("Summarize the dataset"):
    st.write(df.describe())

# show the correlation matrix
if st.checkbox("Show the correlation matrix"):
    st.write(df.corr())

# show the heatmap of the correlation matrix
if st.checkbox("Show the heatmap of the correlation matrix"):
    st.write(sns.heatmap(df.corr(), annot=True))
    st.pyplot()

# Data visualization
st.header("Graphs and Plots")

# Correlation plot for any dataset
if st.checkbox("Correlation plot"):
    st.write(sns.pairplot(df))
    st.pyplot()

# Histogram for any dataset
if st.checkbox("Histogram"):
    st.write(df.hist())
    st.pyplot()

# Bar plot for any dataset
if st.checkbox("Bar plot"):
    # asking user for the data range to plot the bar plot
    st.write("Select the range of data to plot the bar plot")
    x = st.number_input("Start", min_value=0, max_value=df.shape[0], value=0)
    y = st.number_input("End", min_value=0, max_value=df.shape[0], value=df.shape[0])
    # making a plotly bar plot for the data range
    st.plotly_chart(px.bar(df.iloc[x:y, :], x=df.columns.tolist()[0], y=df.columns.tolist()[1]), use_container_width=True)

# Count plot, plot of value count of a column of any dataset
if st.checkbox("Count plot"):
    x = st.selectbox("Select the column", df.columns.tolist())
    # converting x to its corrosponding index
    x = df.columns.tolist().index(x)
    # asking user for the data range to plot the count plot
    st.write("Select the range of data to plot the count plot")

    # DuplicateWidgetID: There are multiple identical st.number_input widgets with the same generated key.
    # Workaround: use key to differentiate them.
    x1 = st.number_input("Start", min_value=0, max_value=df.shape[0], value=0, key="4")
    y1 = st.number_input("End", min_value=0, max_value=df.shape[0], value=df.shape[0], key="5")
    
    # making a count plot for the data range using plotly
    st.plotly_chart(px.bar(df.iloc[x1:y1, x].value_counts(), x=df.iloc[x1:y1, x].value_counts().index, y=df.iloc[x1:y1, x].value_counts().values), use_container_width=True)

# Heatmap for any dataset
if st.checkbox("Heatmap"):
    st.write(sns.heatmap(df.corr(), annot=True))
    st.pyplot()