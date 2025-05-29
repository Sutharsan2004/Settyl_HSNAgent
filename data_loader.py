import pandas as pd

def load_hsn_data(file_path='hsn_master.xlsx'):
    df = pd.read_excel(file_path, dtype=str)
    df.columns = df.columns.str.strip()  # ✅ Strip spaces from column headers
    df.dropna(inplace=True)
    return df
