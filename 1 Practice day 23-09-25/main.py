import streamlit as st
st.markdown("""
<style>
    .st-emotion-cache-pkm19r.e1haskxa15   
    {
            visibility: hidden}     
</style>
""", unsafe_allow_html=True)
st.title("Hi! I am Streamlit web app")
st.header('I am header')
st.subheader("HI I am subheader")
st.text("""What is Streamlit?
Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps. Once you’ve created an app, you can use our Community Cloud platform to deploy, manage, and share your app.""")
st.markdown("**Hello** world *sagar*")
st.markdown("# H1 Heading")
st.markdown("> Heading")
st.markdown("---")
st.markdown("[Google](www.google.com)")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json = {"a":"1,2,3",}
st.json(json)
code = """
print("hello")
def func():
    return 0"""
st.code(code, language="python")

st.write("## H2")
st.metric(label="Wind speed", value="120km⁻¹", delta="-1.4km⁻¹")
st.button("jh")

import pandas as pd
table = pd.DataFrame({"columns1":[1,2,3,4,5],
                      "columns2":[11,21,31,41,51],})
st.table(table)
st.dataframe(table)
st.image("zedge.jpg", caption="My cat")
st.audio("cat.mp3")
# st.video("video.mp4")

def chenge():
    print(st.session_state.checker)

state = st.checkbox("Savi", value=True, on_change=chenge, key='checker')
radio_button=st.radio("Your country?", options=("India", "US", "UK"))
if state:
    st.write("Hi ")
else:
    pass
# print(radio_button)
def btn_click():
    print("button clicked!")
btn = st.button("Submit", on_click=btn_click)
sel = st.selectbox("What you likes?", options=(1,2,3,4))
# print(sel)
sel_multi = st.multiselect("Your likes", options=(1,2,3,4))
# print(sel_multi)
st.write(sel_multi)