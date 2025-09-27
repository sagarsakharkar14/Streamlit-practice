import streamlit
import pandas as pd
from utils import load_data, save_date, plot_monthly_trends
import datetime


streamlit.set_page_config(page_title="Expense Tracker", layout="centered")
streamlit.title("💸 Expense Tracker")

df = load_data()

streamlit.subheader("Add New Expenses")
with streamlit.form("expense_form"):
    expense_date = streamlit.date_input("Date", value=datetime.date.today())
    category = streamlit.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Other"])
    amount = streamlit.number_input("Amount ($)",min_value=0.0, format="%.2f")
    note = streamlit.text_input("Note (Optional)")
    submitted = streamlit.form_submit_button("Add expense")

if submitted:
    save_date(expense_date, category, amount, note)
    streamlit.success("Expense added!")

streamlit.subheader("📊 Monthly Expense Trends")
if not df.empty:
    streamlit.plotly_chart(plot_monthly_trends(df), use_container_width=True)
    streamlit.dataframe(df.sort_values('Date', ascending=False))

    streamlit.download_button("📥 Export to CSV", data=df.to_csv(index=False), file_name="expenses.csv", mime="text/csv")
else:
    streamlit.info("No expenses recorded yet.")

