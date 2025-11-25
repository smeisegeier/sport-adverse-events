import re
import pandas as pd
from pandas_plots import tbl

def replace_vectorized(df_source, df_target):
    # * Build the column-wise mapping: {col: {val_old: val_new}}
    mapping = df_source.groupby('col').apply(
        lambda g: dict(zip(g['val_old'], g['val_new']))
    ).to_dict()

    return df_target.replace(mapping)

# todo add to pandas-plots
def replace_substring_vectorized(df_mapping: pd.DataFrame, df_target: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces substrings in specified columns of `df_target` based on a mapping defined in `df_mapping`.

    Each row in `df_mapping` must contain:
    - 'col': the name of the column in `df_target`
    - 'val_old': the substring to search for (case-insensitive, trimmed)
    - 'val_new': the substring to replace with (trimmed)

    Parameters:
        df_mapping (pd.DataFrame): A DataFrame containing columns 'col', 'val_old', and 'val_new'.
        df_target (pd.DataFrame): The target DataFrame where replacements will be applied.

    Returns:
        pd.DataFrame: A copy of `df_target` with specified substring replacements applied.

    Raises:
        ValueError: If inputs are not DataFrames or required columns are missing.
    """
    if not isinstance(df_mapping, pd.DataFrame):
        raise ValueError("`df_mapping` must be a pandas DataFrame.")
    if not isinstance(df_target, pd.DataFrame):
        raise ValueError("`df_target` must be a pandas DataFrame.")
    if df_mapping.empty or df_target.empty:
        raise ValueError("empty df.")

    required_columns = {'col', 'val_old', 'val_new'}
    if not required_columns.issubset(df_mapping.columns):
        missing = required_columns - set(df_mapping.columns)
        raise ValueError(f"`df_mapping` is missing required columns: {missing}")

    df_result = df_target.copy()

    # * Clean and normalize the mapping data
    df_mapping = df_mapping.copy()
    df_mapping['col'] = df_mapping['col'].astype(str).str.strip()
    df_mapping['val_old'] = df_mapping['val_old'].astype(str).str.strip()
    df_mapping['val_new'] = df_mapping['val_new'].astype(str).str.strip()

    for col in df_mapping['col'].unique():
        if col in df_result.columns:
            replacements = df_mapping[df_mapping['col'] == col][['val_old', 'val_new']]
            df_result[col] = df_result[col].astype(str)

            for val_old, val_new in zip(replacements['val_old'], replacements['val_new']):
                pattern = re.compile(re.escape(val_old), flags=re.IGNORECASE)
                df_result[col] = df_result[col].str.replace(pattern, val_new, regex=True)

    return df_result

# # * loop over all selected columns
def print_survey(df_in: pd.DataFrame, cols: list[str], CTCAE: str) -> None:
    for col in cols[:]:
        # * skip CTCAE and columns that are not str
        if col != CTCAE and df_in[col].dtype.kind in ("O"):

            # * slice
            df = df_in.copy()
            df = df[[col, CTCAE]].dropna()
            # print(col)
            df.iloc[:,0]= df.iloc[:,0].str.strip()#.str.ljust(70, fillchar=".")

            # * split to create arrays in cells, then explode to have atomic values
            df[col] = df[col].str.split("|")
            df = df.explode(col)

            # * to pivot
            _ =(
                tbl.pivot_df(
                    df=df.sort_values(df.columns[-1], ascending=False),
                    dropna=False,
                    data_bar_axis="x",
                    col1_width=600,
                )
                # .format(lambda x: f"{x}")
            )
            display(_)
            # display(
            #     tbl.pivot_df(
            #         df=df,
            #         dropna=False,
            #         data_bar_axis="x",
            #     )
            # )