import pandas as pd

def handle_uploaded_file(file):
    df = pd.read_excel(file,sheet_name='DATA')
    if df[pd.isnull(df['NRO_DNI'])].shape[0] == 0 and df[df['NRO_DNI'].duplicated()].shape[0] == 0:
        return True
    else:
        return False
