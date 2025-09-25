import streamlit
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tenants.csv')

#
pri_btn = streamlit.button(label="Primary", type="primary")
sec_btn = streamlit.button(label="Secondary", type="secondary")

if pri_btn:
    streamlit.write("Hello From Primary")
if sec_btn:
    streamlit.write("Hello From Secondary")

streamlit.divider()
checkbox = streamlit.checkbox("Remember me")
if checkbox:
    streamlit.write("I will Rembemer you")
else:
    streamlit.write("I will forgot you")

streamlit.divider()
df = pd.read_csv('tenants.csv')
radio = streamlit.radio('Choose a column', options=df.columns[1:], index=1, horizontal=True)
streamlit.write(radio)
streamlit.divider()
select = streamlit.selectbox('Choose a column', options=df.columns[1:], index=1)
streamlit.write(select)

streamlit.divider()
multiselect = streamlit.multiselect('Choose a column', options=df.columns[1:], max_selections=2)
streamlit.write(multiselect)

streamlit.divider()
slider = streamlit.slider("My slider", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
streamlit.write(slider)

streamlit.divider()
text_input = streamlit.text_input('whats your name?', placeholder='Sagaa don')
streamlit.write(f"Your name is {text_input}")

streamlit.divider()
num_input = streamlit.number_input("pick a number",min_value=0, max_value=10)
streamlit.write(f"Your number is {num_input}")

streamlit.divider()
text_area = streamlit.text_area("Write an eassay", height=200, placeholder='Write your message here')
streamlit.write(text_area)

