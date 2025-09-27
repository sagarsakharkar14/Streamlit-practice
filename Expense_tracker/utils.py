import pandas as pd
import plotly.express as px

CSV_FILE = 'expenses.csv'

def load_data():
    try: 
        return pd.read_csv(CSV_FILE, parse_dates=['Date'])
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
    
def save_date(date, category, amount, note):
    df = load_data()
    new_entry = pd.DataFrame([[str(date), category, amount, note]], columns=df.columns)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(CSV_FILE, index=-False)

def plot_monthly_trends(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset = ['Date'])

    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    monthly = df.groupby(['Month', 'Category'])['Amount'].sum().reset_index()
    return px.bar(monthly, x="Month", y="Amount", color="Category", barmode="group", title="Monthly Expenses")


# new_entry = pd.DataFrame([['01:01:2025', "category", 95, "note"]], columns=["Date", "Category", "Amount", "Note"])
# print(new_entry)