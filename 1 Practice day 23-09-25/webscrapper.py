import streamlit
import requests
from bs4 import BeautifulSoup


streamlit.header("Web Scrapper")
with streamlit.form("Search"):
    keyword = streamlit.text_input("Enter Your keyword")
    search = streamlit.form_submit_button("Search")
placeholder = streamlit.empty()
if search:
    page = requests.get(f"https://unsplash.com/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'lxml')
    rows = soup.find_all("div", class_='ripi6')
    col1,col2 = placeholder.columns(2)
    for row in rows:
        figures = row.find_all('figure')
        for i in range(2):
            img = figures[i].find("img", class_='YVj9w')
            print(img['srcset'].split('?'))
            print("\n\n")

            # continue to be 