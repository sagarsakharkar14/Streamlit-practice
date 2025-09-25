import streamlit

streamlit.text('Hello')
streamlit.title("Title")
streamlit.header("Header")
streamlit.subheader('Subheader')
streamlit.markdown('Markdown')
streamlit.caption("Captions")
streamlit.code("""
def func():
    print('Hi')""")

streamlit.text("Preformatted text")
streamlit.latex("x=2^2")
streamlit.text("above divider")
streamlit.divider()
streamlit.text("below divider")

streamlit.write('Some text')