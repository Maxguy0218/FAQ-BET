import streamlit as st
import pandas as pd

# Title of the page
st.title("FAQ")

# Dropdown for selecting the FAQ set
faq_set = st.selectbox("Select the FAQ you want to view:", ("Test Folder 1", "Test Folder 2"))


@st.cache
def load_data(faq_set):
    if faq_set == "Test Folder 1":
        return pd.read_csv('faq.csv')
    elif faq_set == "Test Folder 2":
        return pd.read_csv('faq2.csv')

# Load the selected FAQ
df = load_data(faq_set)

# Display FAQs dynamically using collapsible sections
for index, row in df.iterrows():
    with st.expander(row['QUESTIONS']):
        st.write(row['ANSWER'])
