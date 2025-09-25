import streamlit

#FORMTABLE

streamlit.markdown("<h1 style='text-align: center;'>User Registrition</h1>", unsafe_allow_html=True)
form = streamlit.form("form1")
form.text_input("First Name")
form.form_submit_button("Submit")

with streamlit.form("form 2"):
    streamlit.text_input("Lastname")
    streamlit.form_submit_button('Submit')

streamlit.markdown("<h1 style='text-align: center;'>User Registrition</h1>", unsafe_allow_html=True)

with streamlit.form("form 3", clear_on_submit=True):
    col1,col2 = streamlit.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Lastname")
    streamlit.text_input("Enter email address")
    streamlit.text_input("Password")
    streamlit.text_input("Confirm Password")
    # streamlit.form_submit_button('Submit')
    d,m,y = streamlit.columns(3)
    d.text_input("date")
    m.text_input("Month")
    y.text_input("Year")
    s_state = streamlit.form_submit_button('Submit')
    if s_state:
        if f_name=="" or l_name=='':
            streamlit.warning("Please fill above fields")
        else:
            streamlit.success("Submitted Successfully")


#SIDEBARS
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,10,100)
x_bar = np.array([1,2,3,4,5,6])

streamlit.sidebar.write("Helloo this is my side bar")
fig = plt.figure()
plt.plot(x, np.sin(x))
streamlit.write(fig)

opt = streamlit.sidebar.radio("Select any graph", options=['Line','Bar', 'H-bar'])
if opt=='Line':
    fig=plt.figure()
    fig = plt.figure()
    plt.plot(x, np.sin(x))
    streamlit.write(fig)
elif opt=='Bar':
    fig = plt.figure()
    plt.bar(x_bar,x_bar*10)
    streamlit.write(fig)
else:
    streamlit.header("No Chart")