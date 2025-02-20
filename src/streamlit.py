import os
import pandas as pd
from pathlib import Path
import streamlit as st
import pygwalker as pyg

os.environ["THEME"]="dark"

dir_data_out=Path("../data/out")

def get_cols(all_cols: list[str], stubs = list[str]):
    return [col for col in all_cols if any(match in col for match in stubs)]


df_csv_condensed = (
    pd.read_csv(
        dir_data_out / "df_csv_condensed.csv",
        sep=";",
        encoding="utf-8-sig",
        index_col=None,
    ))

# * mark columns that should be str instead of float, fuzzy
col_int = get_cols(all_cols=df_csv_condensed.columns, stubs=["[01.01]"])

# * 
df_csv_condensed = (df_csv_condensed
        .astype({col_int[0]:"Int64"})
        .astype({col_int[0]:str})
)


# Render PyGWalker widget
pyg_app = pyg.walk(df_csv_condensed).to_html()

# Embed the PyGWalker app in Streamlit
# st.components.v1.html(pyg_app)
st.components.v1.html(pyg_app, height=1000, scrolling=True)