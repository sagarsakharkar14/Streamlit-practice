import streamlit
import pandas as pd

#sidebar
with streamlit.sidebar:
    streamlit.write("text")


# Column
col1, col2, col3 = streamlit.columns(3)

col1 = streamlit.write("text i col1 ")

silder = col2.slider("Chosse a number", min_value=0, max_value=10)

col3.write(silder)


#Tabs
df = pd.read_csv('tenants.csv')
tab1, tab2, tab3 = streamlit.tabs(['Line Chart','Bar Chart', "My charts"])

with tab1:
    tab1.write('Line Plot')
    streamlit.line_chart(df, x='Rent', y=['total',])
with tab2:
    tab2.write('Bar Plot')
    streamlit.bar_chart(df, x='Rent', y=['total',])

with streamlit.expander('Click to expand'):
    streamlit.write("i am  sdad")
    streamlit.write("i am  sdad")



#container
with streamlit.container():
    streamlit.write("Inside containier")
streamlit.write("Outside containier")