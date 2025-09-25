import streamlit
import pandas as pd

with streamlit.form("form_key"):
    streamlit.write("my form")
    appe = streamlit.selectbox("Appetizer", options=['options1','options2','options3.'])
    main = streamlit.selectbox("Main", options=['options1','options2','options3.'])
    dessert = streamlit.selectbox("Dessert", options=['options1','options2','options3.'])

    wine = streamlit.checkbox('Are you bringning wine?')
    visit_date = streamlit.date_input("When are you coming?")
    visit_time = streamlit.time_input("at what time are you coming?")
    sub_btn = streamlit.form_submit_button("Submit")
streamlit.write(f"""
                
Appetizer: {appe}

Main Course: {main}

Dessert: {dessert}

Are you bringning wine: {"yes" if wine else 'No'}

visit_date: {visit_date}

visit_time: {visit_time}

""")