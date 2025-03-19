import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png",width=800)


with col2:
    st.title("Rahel Saleh")

    content1 = """hi, my name is Rahel and im a programmer"""
    st.info(content1)


content2 = """below you will find some of the apps im going to build"""
st.write(content2)

csv_files = pandas.read_csv("data.csv",sep=";")
### pandas is a 3rd party library that returns a CSV sheet in a tabular form



col3,col35 ,col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index,item in csv_files[0:10].iterrows():
###  iterrows returns a Series for each row
        st.header(item["title"])
        st.write(item["description"])
        st.image("images/"+item["image"])
### the reason we put images first is because the path of the directory is different it is not the main path of python
### project 1
        st.write(f"[source code]({item["url"]})")




with col4:
    for index,item in csv_files[10:].iterrows():
###  iterrows returns a Series for each row
        st.header(item["title"])
        st.write(item["description"])
        st.image("images/"+item["image"])
        st.write(f"[source code]({item["url"]})")
