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

@streamlit.cache_resource
def create_simpole_limner_regression():
    time.sleep(2)
    X= np.array([1,2,3,4,5,6,7]).reshape(-1,1)
    y = np.array([1,2,3,4,5,6,7])

    model = LinearRegression().fit(X,y)
    return model

lr = create_simpole_limner_regression()
X_pred = np.array([7]).reshape(-1,1)
pred = lr.predict(X_pred)

streamlit.write(f"{pred[0]}")