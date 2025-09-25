import streamlit

streamlit.title("Uploading files")
streamlit.markdown("---")
image = streamlit.file_uploader("Please uploiad the file", type=['jpg','png'])
audio = streamlit.file_uploader("Please uploiad the file", type=['mp3'], accept_multiple_files=True)
if image is not None:
    streamlit.image(image)
# if audio is not None:
#     for a in audio:
#         streamlit.audio(audio)

val = streamlit.slider("Thisi a slider ", min_value=50, max_value=100, value=70)
val = streamlit.slider("Thisi a slider ")
streamlit.write(val)

user_input = streamlit.text_input("A short label explaining to the user what this input: ")
streamlit.write(user_input)

us_in = streamlit.text_area("Write an eassy below|")

import time
from datetime import time as tm

date_input = streamlit.date_input('Enter DOB:')
date_input = streamlit.time_input('Enter timer:', value=tm(0,0,0))

def date_to_sec(dateinput):
    m,s,ms=dateinput.split(":")
    t_s = int(m)*60+int(s)+int(ms)/1000
    return t_s

if str(date_input)=="00:00:00":
    streamlit.write("Please set time")
else:
    sec = date_to_sec(str(date_input))
    bar = streamlit.progress(0)
    pers = sec/100
    progress_status = streamlit.empty()
    for i in range(100):
        bar.progress((i+1))
        progress_status.write(str(i)+"%")
        time.sleep(pers)

