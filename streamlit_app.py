import streamlit as st
from langchain.llms import OpenAI

st.title('My First Streamlit App')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)

import pandas as pd
import numpy as np

# Create a sample dataframe
df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])

# Add a slider
slider_val = st.slider('Select a range', 0, 10)

# Filter the dataframe
filtered_df = df[df['A'] > slider_val]

# Display the dataframe
st.write(filtered_df)
