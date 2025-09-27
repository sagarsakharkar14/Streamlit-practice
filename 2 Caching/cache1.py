import streamlit
import time
import numpy as np
from sklearn.linear_model import LinearRegression

streamlit.title("Casching Demo")

streamlit.button('Test cache')

streamlit.subheader('st.cache_data')

@streamlit.cache_data
def cache_this_function():
    time.sleep(10)
    out = "I'm done running"
    return out

out = cache_this_function()
streamlit.write(out)

streamlit.subheader('st.chache_resource')