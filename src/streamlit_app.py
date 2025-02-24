import os
import pandas as pd
from pathlib import Path
import streamlit as st
from pandas_plots import hlp

# test locally with:
# streamlit run src/streamlit_app.py

# import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

# os.environ["THEME"]="dark"
title ="sport-adverse-events"

# Adjust the width of the Streamlit page
st.set_page_config(page_title=title, layout="wide")

# Add Title
st.title(title)

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df_csv_condensed = (pd.read_csv(
        "https://raw.githubusercontent.com/smeisegeier/sport-adverse-events/refs/heads/main/data/out/df_csv_condensed.csv",
        sep=";",
        encoding="utf-8-sig",
        index_col=None,
    )
    .iloc[:,1:]     # omit first column, which is just the id
    )

    # * mark columns that should be str instead of float, fuzzy
    col_int = hlp.find_cols(all_cols=df_csv_condensed.columns, stubs=["[01.01]"])

    cols_to_str = hlp.find_cols(all_cols=df_csv_condensed.columns, stubs = ["[03.04.02]", "[07.04]", "[03.01.01]", "[01.01]"])

    # * change the type of the columns
    # df_csv_condensed = (df_csv_condensed
    #         .astype({col_int[0]:"Int64"})
    #         .astype({col_int[0]:str})
    # )
    df_csv_condensed[col_int] = df_csv_condensed[col_int].astype("Int64")
    df_csv_condensed[col_int] = df_csv_condensed[col_int].astype(str)
    
    df_csv_condensed[cols_to_str] = df_csv_condensed[cols_to_str].astype(str)

    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(
        dataset=df_csv_condensed,
        spec="./streamlit_config.json",
        kernel_computation=True,
        spec_io_mode="r",
    )


renderer = get_pyg_renderer()

renderer.explorer()