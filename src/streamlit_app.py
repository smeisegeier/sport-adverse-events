import os
import pandas as pd
from pathlib import Path
import streamlit as st

# import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

# os.environ["THEME"]="dark"

# Adjust the width of the Streamlit page
st.set_page_config(page_title="Use Pygwalker In Streamlit", layout="wide")

# Add Title
st.title("Use Pygwalker In Streamlit")

# def get_cols(all_cols: list[str], stubs = list[str]):
#     return [col for col in all_cols if any(match in col for match in stubs)]


df_csv_condensed = pd.read_csv(
    "https://raw.githubusercontent.com/smeisegeier/sport-adverse-events/refs/heads/main/data/out/df_csv_condensed.csv",
    sep=";",
    encoding="utf-8-sig",
    index_col=None,
)

# * mark columns that should be str instead of float, fuzzy
# col_int = get_cols(all_cols=df_csv_condensed.columns, stubs=["[01.01]"])

# # *
# df_csv_condensed = (df_csv_condensed
#         .astype({col_int[0]:"Int64"})
#         .astype({col_int[0]:str})
# )


# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df_csv_condensed = pd.read_csv(
        "https://raw.githubusercontent.com/smeisegeier/sport-adverse-events/refs/heads/main/data/out/df_csv_condensed.csv",
        sep=";",
        encoding="utf-8-sig",
        index_col=None,
    )

    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(
        dataset=df_csv_condensed,
        # spec="./gw_config.json",
        spec_io_mode="rw",
    )


renderer = get_pyg_renderer()

renderer.explorer()


# # Render PyGWalker widget
# pyg_app = pyg.walk(
#     df_csv_condensed,
#     kernel_computation=True,
# ).to_html()

# # Embed the PyGWalker app in Streamlit
# # st.components.v1.html(pyg_app)
# st.components.v1.html(pyg_app, height=1000, scrolling=True)
