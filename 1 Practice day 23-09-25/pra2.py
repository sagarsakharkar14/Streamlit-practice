import streamlit
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tenants.csv')

streamlit.dataframe(df)
streamlit.write(df)

# streamlit.table(df)

streamlit.metric("Total", value=10000, delta=-100, delta_color='normal')

streamlit.line_chart(df, x='Rent', y='total')
# streamlit.area_chart(df, x='Rent', y='total')
streamlit.bar_chart(df, x='Tenant Name', y=['total','Rent'])
streamlit.map()

fig, ax = plt.subplots()
ax.plot(df.Rent, df.total)
ax.set_title("My Fig")
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
fig.autofmt_xdate()

streamlit.pyplot(fig)