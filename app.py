import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Pygwalker In Streamlit 🐱‍🐉")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin-1')

    # Generate the HTML using Pygwalker
    pyg_html = pyg.walk(df, return_html=True)

    components.html(pyg_html, width=1300, height=1000, scrolling=True)
