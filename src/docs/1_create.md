# <a id='toc1_'></a>[create dataset](#toc0_)

**Table of contents**<a id='toc0_'></a>    
- [create dataset](#toc1_)    
  - [init code](#toc1_1_)    
  - [load data](#toc1_2_)    
    - [option clean csv](#toc1_2_1_)    
    - [ (deprecated) option dirty csv](#toc1_2_2_)    
  - [arrange data](#toc1_3_)    
    - [trim column names](#toc1_3_1_)    
    - [set date column](#toc1_3_2_)    
    - [relabeling duplicate columns](#toc1_3_3_)    
    - [remove duplicates or invalids](#toc1_3_4_)    
    - [parse dates to datetime 🕥](#toc1_3_5_)    
    - [(deprecated) remove columns w/ no or few values](#toc1_3_6_)    
  - [condensed dataset](#toc1_4_)    
    - [define functions](#toc1_4_1_)    
    - [define single, multi and misc columns](#toc1_4_2_)    
    - [concat condensed dataset from subsets](#toc1_4_3_)    
    - [create manual table for mapping](#toc1_4_4_)    
    - [column mapping from codebook](#toc1_4_5_)    
    - [value mapping for missings and unknown](#toc1_4_6_)    
    - [value mapping from codebook](#toc1_4_7_)    
  - [💾 data for pivot use](#toc1_5_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

## <a id='toc1_1_'></a>[init code](#toc0_)


```python

import io
import os
from glob import glob
import pandas as pd
from pathlib import Path
from pandas_plots import tbl, pls, hlp
from pandas_plots.hlp import add_bitmask_label
import re
hlp.show_package_version(["pygwalker"])

os.environ["THEME"]="light"

dir_data_in=Path("../data/in")
dir_data_out=Path("../data/out")
dir_data_codebooks=Path("../data/codebooks")

# ! only 1 csv file in in/ is allowed
file_csv_list=glob(f"{dir_data_in}/*.csv")
assert len(file_csv_list) == 1, f"❌ Expected 1 csv file, found {len(file_csv_list)}"

file_csv = file_csv_list[0]

# * grab choice part or eg .1
REGEX_CHOICE = r"( \(choice=.*?\)+|\.\d$)"

# * grab the code block at the start
REGEX_CODE1 = r"(^\[.*?\])"

# * grab the non-code block
REGEX_NONCODE = r"\].*"

# * grab the code block
REGEX_CODEALL = r'(\[\d{2}\.\d{2}(?:\.\d{2})?\])'

ENABLE_UPDATE=True
```

    🐍 3.12.9 | 📦 pygwalker: 0.4.9.15 | 📦 pandas: 2.3.3 | 📦 numpy: 1.26.4 | 📦 duckdb: 1.4.2 | 📦 pandas-plots: 0.22.4 | 📦 connection-helper: 0.13.2


## <a id='toc1_2_'></a>[load data](#toc0_)


### <a id='toc1_2_1_'></a>[option clean csv](#toc0_)


```python
df_csv = pd.read_csv(
    file_csv,
    sep=",",
    encoding="utf-8-sig",
    dtype={"[01.01] Bewertung - CTCAE-Bewertung": str},
)
```

### <a id='toc1_2_2_'></a>[ (deprecated) option dirty csv](#toc0_)
- ⚠️ strategy to import the csv raw data:
  - ❌ do not use default `pd.read_csv()`, its not as error tolerant as excel
  - ✅ read csv as `windows-1252` string and cleanse it
    - most (not all) lines have heading + trailing quotes, remove
    - data have a mixture of "" and ", downgrade by 1
    - delimiter "," also occurs in quotes, change to ";" only outside of quotes
    - now byte stream can be imported


```python
# # * replace delimiter *only* outside of quotes
# def replace_delimiter_outside_quotes(
#     input: str, delimiter_old: str = ",", delimiter_new: str = ";", quotechar: str = '"'
# ):
#     outside_quotes = True
#     output = ""
#     # * loop through input and toggle inside/outside status
#     for char in input:
#         if char == quotechar:
#             outside_quotes = not outside_quotes
#         elif outside_quotes and char == delimiter_old:
#             char = delimiter_new
#         output += char
#     return output

# # * downgrades quotes in string to normalize quots: " -> NA, "" -> "
# def reduce_quotes_in_string(input: str):
#     output = ""
#     len_=len(input)
#     i = 0
#     while i < len_:
#         # * check current + next char if within range
#         if input[i] == '"' and i+1 < len_ and input[i+1] != '"':
#             output += ''
#             i = i+1
#         elif input[i] == '"'and i+1 < len_ and input[i+1] == '"':
#             output+= '"'
#             i = i+2
#         else:
#             output += input[i]
#             i=i+1
#     return output

# # * read csv -> variable
# with open(file_csv, encoding="windows-1252") as f:
#     csv=f.read()

# # * selectively change , into ;
# csv_lines = csv.splitlines()
# csv_lines_new = []
# for line in csv_lines[:]:
#     # * remove first and last quotes if present
#     if line[:1] == '"':
#         line = line[1:-1]
#     # * tailor line by line
#     line=reduce_quotes_in_string(line)
#     line=replace_delimiter_outside_quotes(line)
#     # * just now quotes can be removed, not before
#     line=line.replace('"', '')
#     csv_lines_new.append(line)
#     # print(f'{line.count(";")} {line}')

# # * list -> string fo feed into df constructor
# csv_string = "\n".join(csv_lines_new).replace('\t', '')

# df_csv = pd.read_csv(
#     io.StringIO(csv_string),
#     sep=";",
#     encoding="windows-1252",
# )
```

## <a id='toc1_3_'></a>[arrange data](#toc0_)

### <a id='toc1_3_1_'></a>[trim column names](#toc0_)


```python
cols_trimmed = [col.strip() for col in df_csv.columns]
df_csv.columns = cols_trimmed
```

### <a id='toc1_3_2_'></a>[set date column](#toc0_)


```python
[print(col) for col in df_csv.columns if "Datum" in col]
col_date = "[02.01] Basics - Datum"
```

    [02.01] Basics - Datum


### <a id='toc1_3_3_'></a>[relabeling duplicate columns](#toc0_)


```python
df_csv.rename(columns={"[03.05.01] Folgen - Wie oft wurde die lebensnotwendige Intervention wiederholt?":"[03.05.02] Folgen - Wie oft wurde die lebensnotwendige Intervention wiederholt?"}, inplace=True)
```

### <a id='toc1_3_4_'></a>[remove duplicates or invalids](#toc0_)


```python
# # * remove known erroruos lines
# df_csv.drop([0,34,33], inplace=True, axis=0, errors='ignore')
# * remove "löschen" lines
df_csv = df_csv[~(df_csv[col_date] == "löschen")]

# * remove "Anmerkung"
df_csv.drop(['[05.09] Rahmenbedingungen - Welchen Trainingszustand hatte der / die Betroffene zum Zeitpunkt als das AE auftrat? (choice=5 Anmerkung)'], axis=1, inplace=True, errors='ignore')

# * remove "kein AE" from CTCAE
# df_csv.loc[df_csv["Participant ID"] == 218, df_csv.columns[4]] = pd.NA
```

### <a id='toc1_3_5_'></a>[parse dates to datetime 🕥](#toc0_)


```python
df_csv.loc[df_csv[col_date]=="2023_08_2028", col_date]="2023_08_28"
df_csv.loc[df_csv[col_date]=="2025_04_31", col_date]="2025_04_30"
df_csv.loc[df_csv[col_date]=="2024_16", col_date]="2024_06"
```


```python
# Define a list of possible date formats
formats = ['%Y_%m', '%Y_%m_%d']

# Create an empty Series to store the converted datetimes
converted_series = pd.Series(pd.NaT, index=df_csv.index)

# Iterate through the formats and convert the column
for fmt in formats:
    converted_series.fillna(pd.to_datetime(df_csv[col_date], format=fmt, errors='coerce'), inplace=True)

df_csv[col_date] = converted_series

# Convert the column to datetime
df_csv[col_date].fillna(df_csv["Survey Timestamp"], inplace=True)
```

### <a id='toc1_3_6_'></a>[(deprecated) remove columns w/ no or few values](#toc0_)


```python
# import numpy as np
# # * remove columns with no value
# cols_no_value = [col for col in df_csv.columns if df_csv[col].isna().all()]
# print("these columns have no values at all:")

# print(np.array(cols_no_value))

# # ! remove columns
# cols_after_removal = list(set(df_csv.columns) - set(cols_no_value))
# df_csv_short = df_csv[list(set(df_csv.columns) - set(cols_no_value))]
```


```python
df_csv
```


    
![png](1_create_files/output_23_0.png)
    


## <a id='toc1_4_'></a>[condensed dataset](#toc0_)
- take the cleansed (but structurally unchanged) dataset `df_csv` as a starting point
- define handling for column subsets according to column types
  - **single choice** - only 1 value is allowed per row
  - **multi choice** - multiple values are allowed per row
  - **misc** - all other columns that are selected to appear in the final dataset
- apply column mapping from manual table `codebook_columns.xlsx`
- apply value mapping for missings and unknown value
- apply value mapping from manual table `codebook_values.xlsx`

### <a id='toc1_4_1_'></a>[define functions](#toc0_)


```python
def condense_columns_single_choice(df, strict=False):
    """
    Condenses multiple columns into a single target column, extracting specific values based on
    the first occurrence of 'Checked' in each row. 

    The function processes columns named according to a pattern (e.g., 'choice=<value>') and condenses
    them into a single column. If a column contains the value 'Checked', the corresponding value (e.g., 
    'Schmerzen', 'Muskelkater') is assigned to the new target column. If multiple 'Checked' values are 
    present, only the leftmost occurrence is used.

    Parameters:
        df (pandas.DataFrame): The input DataFrame with columns to be processed. The columns should contain
                                values such as 'Checked' or 'Unchecked', and be named according to a 
                                pattern like '[02.02] Basics - Was war das AE?  (choice=<value>)'.
        strict: if an error is raised if more than 1 cell is "Checked"

    Returns:
        pandas.DataFrame: A DataFrame with the same columns as input, but with a new target column containing 
                        the extracted values based on the first occurrence of 'Checked' in each row.
                        The new column is named using the pattern found in the column names (e.g., '[02.02]').

    Notes:
        - If no 'Checked' value is found in a row, the target column is set to pd.NA for that row.
        - The new column name is derived from the first part of the first input column (i.e., the substring
        within the square brackets).
        - Only the first 'Checked' occurrence in each row is considered; any subsequent 'Checked' cells
        will be ignored.
    """

    # * Extract target column name using the updated regex pattern (substring in square brackets)
    match = re.search(r"\[\d{2}\.\d{2}(\.\d{2})?\]", df.columns[0])
    if not match:
        raise ValueError("No substring in square brackets matching the pattern found in the first column name.")
    target_col_name = match.group(0)

    # * Check for multiple "checked" cells in one row
    columns_to_check = [col for col in df.columns if re.search(r"\(choice=.*\)", col)]
    checked_counts = df[columns_to_check].apply(lambda row: (row.str.lower() == "checked").sum(), axis=1)

    if strict and (checked_counts > 1).any():
        problematic_rows = df.index[checked_counts > 1].tolist()
        raise ValueError(f"Multiple 'checked' values found in rows: {problematic_rows}")

    # * Create the target column with default pd.NA values
    df[target_col_name] = pd.NA

    # * Process each row and select the first "checked" value from left to right
    for index, row in df.iterrows():
        # * Loop over columns left to right to find the first "checked" value
        for col in columns_to_check:
            if row[col].lower() == "checked":
                # * Extract the choice label using regex. capture group is 
                match = re.search(r"\(choice=(.*?)\)", col)
                # match = re.search(r"\(choice=\d+ (.*?)\)", col)
                if match:
                    choice_label = match.group(1)
                    # Set the target column with the choice label for this row
                    df.at[index, target_col_name] = choice_label
                break  # Stop after the first "checked" value is found

    return df.iloc[:,-1]

def condense_columns_multi_choice(
    df, 
    new_col_pattern=r"^\[.*?\]", 
    choice_pattern=r"\(choice=(.*?)\)"
):
    # Extract the new column name from the first column using the provided regex pattern
    first_col = df.columns[0]
    new_col_name = re.search(new_col_pattern, first_col).group(0) if re.search(new_col_pattern, first_col) else "Unnamed"
    
    # Extract parts from original column names using the provided choice pattern
    extracted_parts = [
        re.search(choice_pattern, col).group(1) if re.search(choice_pattern, col) else None
        for col in df.columns
    ]

    # Calculate the new column using a bitmask
    def calculate_bitmask(row):
        bitmask = 0
        for i, col in enumerate(df.columns):
            if row[col] == "Checked":
                bitmask += 2**i
        return bitmask

    df[new_col_name] = df.apply(calculate_bitmask, axis=1)

    # Example placeholder for a function to add additional labels or transformations
    # Replace `add_bitmask_label` with your actual logic if needed
    # add_bitmask_label(df, new_col_name, extracted_parts)

    add_bitmask_label(df, new_col_name, extracted_parts)
    return df.iloc[:,-1]

```

### <a id='toc1_4_2_'></a>[define single, multi and misc columns](#toc0_)


```python

stubs_single = set((
'[03.01.02]',
'[03.15.01]',
'[03.10]',
))


stubs_multi = set((
'[02.02]', '[02.03]', '[02.04]', 
'[03.03.02]', '[03.03.01]', '[03.06.01]',
'[03.07.01]', '[03.08.01]', 
'[03.10.01]', '[03.10.02]',
'[03.11.01]', '[03.12.01]', '[03.14.01]',
'[03.17.01]', '[03.14]',
'[05.07]', '[05.09]',
))

stubs_misc= set((
'Participant ID', 
'[01.02]','[01.03]', '[03.01]', '[03.02]', '[03.03]',
'[03.04]', '[03.05]', '[03.06]', '[03.07]', '[03.08]', '[03.09]',
'[03.11]', '[03.12]', '[03.13]', '[03.15]', '[03.16]', '[03.17]', '[05.01]',
'[05.02]', '[05.03]', '[05.04]', '[05.05]', '[05.06]', '[05.08]',
'[03.01.01]', '[03.02.01]',
'[03.02.02]',
'[03.06.02]', '[03.07.02]', '[03.08.02]',
'[03.09.01]', '[03.09.02]', '[03.11.02]',
'[03.12.02]', '[03.13.01]', '[03.13.02]', 
'[03.15.02]', '[03.17.02]',

'[02.01]', '[01.01]', '[01.02]', '[03.01]',
'[03.02]', '[03.03]', '[03.04]', '[03.07]',
'[03.08]', '[03.08.02]',
'[03.09]', '[03.09.01]', '[03.09.02]', '[03.11]', '[03.12]',
'[03.13]', '[03.13.01]', '[03.13.02]', '[03.17]', '[05.01]', '[05.02]',
'[05.03]', '[05.04]', '[05.05]', '[05.06]', '[05.08]',
'[03.18]',
))

if stubs_misc & stubs_multi or stubs_misc & stubs_single or stubs_single & stubs_multi:
    raise ValueError("stubs must be disjoint")

cols_single = hlp.find_cols(df_csv.columns, stubs_single)
cols_multi = hlp.find_cols(df_csv.columns, stubs_multi)
cols_misc = hlp.find_cols(df_csv.columns, stubs_misc)

```


```python
# # * testing
# df_csv.find_cols(stubs=["06.01"])
```


```python
# # * derive single
df_csv_single = pd.DataFrame()
for stub in stubs_single:
    cols = [col for col in df_csv.columns if stub in col]
    print(cols)

    df = pd.DataFrame(df_csv[cols])
    ser = condense_columns_single_choice(df)
    df_csv_single[stub] = ser

df_csv_single
```

    ['[03.15.01] Folgen - War die gesamte Handlungsweise bei diesem AE rein pädagogischer Natur? (choice=Ja)', '[03.15.01] Folgen - War die gesamte Handlungsweise bei diesem AE rein pädagogischer Natur? (choice=Nein)']
    ['[03.01.02] Folgen - Wie lange dauerten die Schmerzen an? (choice=Schmerzen am gleichen Tag)', '[03.01.02] Folgen - Wie lange dauerten die Schmerzen an? (choice=Schmerzen bis zum Folgetag)', '[03.01.02] Folgen - Wie lange dauerten die Schmerzen an? (choice=Schmerzen, die mindestens 3 Tage anhielten)', '[03.01.02] Folgen - Wie lange dauerten die Schmerzen an? (choice=Weiß nicht)']
    ['[03.10] Folgen - Wurde die Situation von einer Person mit entsprechender Expertise direkt geprüft?']



    
![png](1_create_files/output_30_1.png)
    



```python
# # * derive multi
df_csv_multi = pd.DataFrame()
for stub in stubs_multi:
    cols = [col for col in df_csv.columns if stub in col]
    # print(cols)

    df = pd.DataFrame(df_csv[cols])
    ser = condense_columns_multi_choice(df)
    df_csv_multi[stub] = ser

df_csv_multi[:3]
```


    
![png](1_create_files/output_31_0.png)
    


### <a id='toc1_4_3_'></a>[concat condensed dataset from subsets](#toc0_)


```python
# # * save original columns as txt
cols_all = sorted(cols_single + cols_multi + cols_misc)

if ENABLE_UPDATE:
    pd.DataFrame(cols_all).to_csv(dir_data_out/"df_csv_condensed_columns.txt", index=False, sep=";", header=False)

# * all columns
df_csv_condensed = pd.concat(
    [
        df_csv[cols_misc],
        df_csv_single,
        df_csv_multi,
    ], 
    axis=1,
).sort_index(axis=1)
display(df_csv_condensed[:3])

# # ! prevent duplicate column names
if df_csv_condensed.columns.duplicated().any():
    raise ValueError("duplicated columns")
```


    
![png](1_create_files/output_33_0.png)
    


### <a id='toc1_4_4_'></a>[create manual table for mapping](#toc0_)


```python
if ENABLE_UPDATE and False:

    # * have all columns but remove choices from column names, isolate code
    df_csv_cols = (
        pd.DataFrame(df_csv.columns, columns=["col"])
        .assign(
            col_code=lambda x: x["col"].str.extract(REGEX_CODE1),
            col_clean=lambda x: x["col"].str.replace(REGEX_CHOICE, "", regex=True),
        )
    )
    display(df_csv_cols[:3])

    # * group and set up foe manual renaming
    df_csv_cols_condensed = (df_csv_cols
        .assign(cnt=1)
        .groupby(["col_clean","col_code"], as_index=False, dropna=False)["cnt"].sum()
    )
    display(df_csv_cols_condensed[:3])


    df_csv_cols_condensed.assign(col_new=lambda x: x["col_code"]).to_excel(dir_data_out/"codebook_columns.xlsx", index=False)
    # df_csv_cols_condensed.assign(col_new=lambda x: x["col_code"]).to_excel(dir_data_out/"df_csv_cols.ods", index=False, engine="odf")

```

### <a id='toc1_4_5_'></a>[column mapping from codebook](#toc0_)
- in `codebook_columns.xlsx`
  - col names in `col_clean` (full label) -> `col_final`
  - col names in `col_code` (code only) -> `col_new`


```python
# # * import column mapping
df_codebook_columns = (pd
        .read_excel(dir_data_codebooks/"codebook_columns.xlsx")
        # * remove leading and trailing spaces
        .applymap(lambda x: x.strip() if isinstance(x, str) else x)
)
# * ignore empty rows
df_codebook_columns = df_codebook_columns.dropna(subset=["col_final"])[:]
df_codebook_columns
```


    
![png](1_create_files/output_37_0.png)
    



```python
df_csv_condensed.rename(columns={"Participant ID": "[00.00] ParticipantID"}, inplace=True)
```


```python
# # ! get all columns from codebook, BUT ONLY COL_FINAL. rest is ignored!
cols_target = df_codebook_columns["col_final"]

# * extract codes from column names in codebook
codes_to_be_translated = sorted(
    set(
        cols_target
            .str
            .extract(REGEX_CODEALL, flags=re.IGNORECASE)
            .iloc[:, 0]
    )
)

# hack dict is not robust!
# * get all columns with these codes_to_be_translated
cols_source = sorted(df_csv_condensed.find_cols(codes_to_be_translated))

dict_cols = dict(zip(cols_source, cols_target))
display(dict_cols)
# ! rename columns
df_csv_condensed = df_csv_condensed.rename(columns= dict_cols)
df_csv_condensed[:3]
```


    {'[00.00] ParticipantID': '[00.00] ParticipantID',
     '[01.01] Bewertung - CTCAE-Bewertung': '[01.01] CTCAE classification',
     '[01.02] Wann ist das AE erstmals aufgetreten?': '[01.02] Date',
     '[01.03] Bewertung - Glauben Sie, dass das AE mit dem Sport assoziiert ist?': '[01.03] Exercise-related',
     '[02.01] Basics - Datum': '[02.01] CreatedOn',
     '[02.02]': '[02.02] Type',
     '[02.03]': '[02.03] Trigger',
     '[02.04]': '[02.04] Affected body parts',
     '[03.01] Folgen - Sind Schmerzen aufgetreten?': '[03.01] Pain',
     "[03.02] Folgen - Kam es zu einem Krankenhausaufenthalt oder zu einer Verlängerung dieses Aufenthalts?'": '[03.02] With hospitalization',
     '[03.03] - Folgen - Kam es zu einer medizinischen Weiterbehandlung?': '[03.03] Medical follow-up treatment',
     "[03.04] Folgen -Kam es zu einer deutlichen Verzögerung bei der Umsetzung des medizinischen Therapieprotokolls?'": '[03.04] With delayed therapy protocol',
     '[03.05] Folgen - Kam es zu lebensrettenden Interventionen (z.\u202fB. Beatmung, Herzdruckmassage)?': '[03.05] Life-saving intervention',
     '[03.06] Folgen - Gab es einen erhöhten Pflegebedarf?': '[03.06] Increased care needs',
     '[03.07] Konsequenzen - Mussten Medikamente eingenommen werden?': '[03.07] With medication administration',
     '[03.08.01]': '[03.08.01] Affected person',
     '[03.08] Folgen - Kam es zu Angst und Unsicherheit?': '[03.08] Occurrence of fear and uncertainty',
     '[03.09] Folgen -  Kam es zu strukturellen Anpassungen?': '[03.09] Structural adjustment',
     '[03.10.01]': '[03.10.01] Approver',
     '[03.10.02]': '[03.10.02] OK to proceed',
     '[03.10]': '[03.10] Assessment of the situation by expertise',
     '[03.11] Folgen - Wurde die PECH-Regel zur Behandlung angewendet?': '[03.11] Application RICE rule (Rest, Ice, Compression, Elevation)',
     '[03.12] Folgen - Wurde das Kind nach dem AE observiert?': '[03.12] With observation',
     '[03.13.01] Folgen - Wie wurde gestoppt?': '[03.13.01] Suspension or termination of session',
     '[03.13] Folgen - Wurde die Bewegungseinheit gestoppt?': '[03.13] Suspension and termination of session',
     '[03.14.01]': '[03.14.01] Adaptations intensity',
     '[03.14]': '[03.14] Adaptation',
     '[03.16] Folgen - Kam es zum Tod?': '[03.16] Death',
     '[05.01] Rahmenbedingung - In welcher Phase der Therapie trat das AE auf?': '[05.01] Therapy phase',
     '[05.02] Rahmenbedingungen - In welcher Gruppengröße fand die Sporteinheit statt, in der das AE auftrat?': '[05.02] Group size',
     '[05.03] Rahmenbedingungen - Wie alt war der/die Betroffene zum Zeitpunkt des AE?': '[05.03] Age',
     '[05.04] Rahmenbedingungen - Fand das Sportprogramm online statt?': '[05.04] Home (telemedicine)',
     '[05.05] Rahmenbedingungen - Fand das AE im Rahmen einer Sporttestung statt?': '[05.05] As part of testing',
     '[05.06] Rahmenbedingungen - In welchem Setting trat das AE auf?': '[05.06] Setting',
     '[05.07]': '[05.07] Main motor skill',
     '[05.08] Rahmenbedingungen - In welcher Phase der geplanten Sporteinheit trat das AE auf?': '[05.08] Time point',
     '[05.09]': '[05.09] Fitness level'}



    
![png](1_create_files/output_39_1.png)
    



```python
# # ! DEPRC

# # * coalesce columns - most right column has priority
# # * -> deprecated. only use col_final!
# # df_csv_cols_import["col_final"] = df_csv_cols_import[["col_new", "col_code", "col_clean"]].backfill(axis=1).iloc[:,0]


# # * create dict for mapping
# # * column names in target df can be full label or code only, so 2 rounds are needed
# def create_col_map(df, join_col: str):
#     # * only use rows with not NA values
#     series_source = df_csv_condensed.columns.to_series()
#     series_target = df_codebook_columns.set_index(join_col)["col_final"]
#     # * use concat to join two series
#     series_joint = (pd.concat(
#         [
#             series_source,
#             series_target
#         ],
#         axis=1, join="inner"
#         )
#         ["col_final"]
#     )
#     return series_joint.to_dict()

# col_map1 = create_col_map(df_codebook_columns, "col_clean")
# col_map2 = create_col_map(df_codebook_columns, "col_code")

# # * relabel column names in 2 rounds
# df_csv_condensed.rename(columns=col_map1, inplace=True)
# df_csv_condensed.rename(columns=col_map2, inplace=True)


# # * (deprecated) strip column names to code only
# # cols = df_csv_condensed.columns
# # df_csv_condensed.columns = [re.sub(REGEX_NONCODE, "]", col) for col in cols]

# df_csv_condensed#[df_csv_condensed.columns.sort_values()]
```

### <a id='toc1_4_6_'></a>[value mapping for missings and unknown](#toc0_)


```python
# # * target coding for missing / unknown
STR_NA = pd.NA
STR_U = "(Unknown)"

# * remove digits in [05.09]. inplace wont work, whyever
df_csv_condensed[df_csv_condensed.find_cols(["[05.09]"])] = df_csv_condensed[df_csv_condensed.find_cols(["[05.09]"])].replace(r"\d{1} ","", regex=True, inplace=False)

items = [
    ("[02.04]","-",STR_NA),
    ("[03.02]","weiß nicht",STR_U),
    ("[03.03]","weiß nicht",STR_U),
    ("[03.07]","weiß nicht",STR_U),
    ("[03.12]","Weiß nicht",STR_U),
    ("[03.14.01]","-",STR_NA),
    ("[03.17]","weiß nicht",STR_U),
    ("[05.03]","weiß nicht",STR_U),
    ("[05.07]","-",STR_NA),
    ("[05.09]","-",STR_NA),
    ("[05.09]","weiß nicht",STR_U),
    ("[03.08.01]","-",STR_NA),
]

for item in items:
    _col = df_csv_condensed.find_cols([item[0]])[0]
    print(f"in {_col}: {item[1]} -> {item[2]}")
    df_csv_condensed.loc[df_csv_condensed[_col].str.lower().str.strip()==item[1].lower().strip(),_col] = item[2]

```

    in [02.04] Affected body parts: - -> <NA>
    in [03.02] With hospitalization: weiß nicht -> (Unknown)
    in [03.03] Medical follow-up treatment: weiß nicht -> (Unknown)
    in [03.07] With medication administration: weiß nicht -> (Unknown)
    in [03.12] With observation: Weiß nicht -> (Unknown)
    in [03.14.01] Adaptations intensity: - -> <NA>
    in [03.17] Folgen - Kam es zu Einschränkungen der Aktivitäten des täglichen Lebens (ADL)?: weiß nicht -> (Unknown)
    in [05.03] Age: weiß nicht -> (Unknown)
    in [05.07] Main motor skill: - -> <NA>
    in [05.09] Fitness level: - -> <NA>
    in [05.09] Fitness level: weiß nicht -> (Unknown)
    in [03.08.01] Affected person: - -> <NA>



```python
# # * example
# print(df_csv_condensed[df_csv_condensed.find_cols(["[05.08"])].value_counts())
```

### <a id='toc1_4_7_'></a>[value mapping from codebook](#toc0_)
- in `codebook_values.xlsx`
  - col codes in `code`
  - old value in `de` -> new value in `en`


```python
from mod import helper as h
# # * import column mapping
df_codebook_values = (pd
        .read_excel(dir_data_codebooks/"codebook_values.xlsx")
        # * remove leading and trailing spaces
        .applymap(lambda x: x.strip() if isinstance(x, str) else x)
        # * ignore empty rows in code column
        .dropna(subset=["code"])
        # * rename columns for use in function
        .rename(columns={"de": "val_old", "en": "val_new"})
)

# * list all column codes should be searched in dataset
# * include duplicates, this list is added as a column later
stubs = df_codebook_values.code.to_list()

# * resulting full column names
found = hlp.find_cols(df_csv_condensed, stubs)

# * add these full names
df_codebook_values["col"]=found

# ! map values in dataset
_df = df_csv_condensed.copy()
df_csv_condensed = h.replace_substring_vectorized(df_mapping=df_codebook_values, df_target=_df)

```


```python
# display(df_codebook_values[df_codebook_values.code == '[05.08]'])
```

### reduce columns


```python
# # ! dont run this earlier before other transformations, those might crash when subjected column was already removed
df_csv_condensed = df_csv_condensed[cols_target.to_list()]
```


```python
display(df_csv_condensed)
df_csv_condensed.columns
```


    
![png](1_create_files/output_49_0.png)
    





    Index(['[00.00] ParticipantID', '[01.01] CTCAE classification', '[01.02] Date',
           '[01.03] Exercise-related', '[02.01] CreatedOn', '[02.02] Type',
           '[02.03] Trigger', '[02.04] Affected body parts', '[03.01] Pain',
           '[03.02] With hospitalization', '[03.03] Medical follow-up treatment',
           '[03.04] With delayed therapy protocol',
           '[03.05] Life-saving intervention', '[03.06] Increased care needs',
           '[03.07] With medication administration', '[03.08.01] Affected person',
           '[03.08] Occurrence of fear and uncertainty',
           '[03.09] Structural adjustment', '[03.10.01] Approver',
           '[03.10.02] OK to proceed',
           '[03.10] Assessment of the situation by expertise',
           '[03.11] Application RICE rule (Rest, Ice, Compression, Elevation)',
           '[03.12] With observation',
           '[03.13.01] Suspension or termination of session',
           '[03.13] Suspension and termination of session',
           '[03.14.01] Adaptations intensity', '[03.14] Adaptation',
           '[03.16] Death', '[05.01] Therapy phase', '[05.02] Group size',
           '[05.03] Age', '[05.04] Home (telemedicine)',
           '[05.05] As part of testing', '[05.06] Setting',
           '[05.07] Main motor skill', '[05.08] Time point',
           '[05.09] Fitness level'],
          dtype='object')



## <a id='toc1_5_'></a>[💾 data for pivot use](#toc0_)


```python
if ENABLE_UPDATE:
    # # * only show cols w/ >1 value
    # df_csv_short = df_csv.loc[:, df_csv.apply(pd.Series.nunique) > 1]
    # df_csv_short.to_csv(Path(dir_data_out/"df_csv_short.csv"),sep=";", index=False, encoding="utf-8-sig")

    df_csv.to_csv(Path(dir_data_out/"df_csv.csv"),sep=";", index=False, encoding="utf-8-sig")
    df_csv.to_excel(Path(dir_data_out/"df_csv.xlsx"),index=False)
    df_csv_condensed.sort_index(axis=1).to_csv(Path(dir_data_out/"df_csv_condensed.csv"),sep=";", index=False, encoding="utf-8-sig")
    df_csv_condensed.sort_index(axis=1).to_excel(Path(dir_data_out/"df_csv_condensed.xlsx"), index=False)
```


```python
# for col in df_csv.columns.to_list()[8]:
#     x = col
#     x1=re.search(pattern=r"^\[\d{2}\.\d{2}(\.\d{2})?\]", string=x).group()
#     x3 = re.search(pattern=r"( \(choice=.*?\)+|\.\d$)", string=x).group()
#     x4 = re.search(pattern=r"\(choice=(.*?)\)", string=x).group(1)
#     x5 = re.search(pattern=r"\](.*?)\(choice=", string=x).group(1)
#     print(f"{x} | {x1} | {x4} | {x5}")
```


```python
tbl.describe_df(df_csv_condensed, "df_csv_condensed", top_n_chars_in_columns=25, top_n_chars_in_index=15)
```

    🔵 *** df: df_csv_condensed ***  
    🟣 shape: (178, 37)
    🟣 duplicates: 0  
    🟠 column stats all (dtype | uniques | missings) [values]  
    - index [0, 1, 2, 3, 4,]  
    - [00.00] ParticipantID (int64 | 178 | 0 (0%)) [3, 4, 5, 6, 7,]  
    - [01.01] CTCAE classification (object | 3 | 0 (0%)) ['1', '2', '3',]  
    - [01.02] Date (object | 2 | 0 (0%)) ['New onset', 'Pre-existing, aggravated',]  
    - [01.03] Exercise-related (object | 3 | 0 (0%)) ['No', 'Yes', 'nan',]  
    - [02.01] CreatedOn (datetime64[ns] | 127 | 0 (0%)) [2021-01-11 00:00:00, 2021-01-12 00:00:00, 2021-01-18 00:00:00, 2021-02-01 00:00:00,  
    2021-02-19 00:00:00,]  
    - [02.02] Type (object | 32 | 0 (0%)) ['Bone injuries', 'Circulatory problems', 'Circulatory problems|Muscle cramps',  
    'Circulatory problems|Physical (Over)exertion', 'Circulatory problems|Psychological stress reaction',]  
    - [02.03] Trigger (object | 24 | 0 (0%)) ['Collision', 'Coordination problems', 'Environmental conditions|Collision',  
    'Fall-related incident', 'Fall-related incident|Coordination problems',]  
    - [02.04] Affected body parts (object | 21 | 0 (0%)) ['<NA>', 'Abdomen', 'Abdomen|Bowel', 'Abdomen|Coccyx', 'Back',]  
    - [03.01] Pain (object | 2 | 0 (0%)) ['Ja', 'Nein',]  
    - [03.02] With hospitalization (object | 3 | 0 (0%)) ['(Unknown)', 'No', 'Yes',]  
    - [03.03] Medical follow-up treatment (object | 3 | 0 (0%)) ['(Unknown)', 'No', 'Yes',]  
    - [03.04] With delayed therapy protocol (object | 1 | 0 (0%)) ['No',]  
    - [03.05] Life-saving intervention (object | 1 | 0 (0%)) ['No',]  
    - [03.06] Increased care needs (object | 2 | 0 (0%)) ['No', 'Yes',]  
    - [03.07] With medication administration (object | 4 | 5 (3%)) ['(Unknown)', '<NA>', 'No', 'Yes',]  
    - [03.08.01] Affected person (object | 10 | 0 (0%)) ['<NA>', 'For affected individuals', 'For affected individuals|For parents',  
    'For affected individuals|For parents|In the treatment team', 'For affected individuals|For the excercise experts',]  
    - [03.08] Occurrence of fear and uncertainty (object | 3 | 0 (0%)) ['No', 'Yes', 'nan',]  
    - [03.09] Structural adjustment (object | 3 | 0 (0%)) ['No', 'Yes', 'nan',]  
    - [03.10.01] Approver (object | 6 | 0 (0%)) ['-', 'Medical team', 'Nursing team', 'Parents', 'Physiotherapy',]  
    - [03.10.02] OK to proceed (object | 1 | 0 (0%)) ['-',]  
    - [03.10] Assessment of the situation by expertise (object | 1 | 178 (100%)) ['<NA>',]  
    - [03.11] Application RICE rule (Rest, Ice, Compression, Elevation) (object | 2 | 0 (0%)) ['No', 'Yes',]  
    - [03.12] With observation (object | 3 | 0 (0%)) ['(Unknown)', 'No', 'Yes',]  
    - [03.13.01] Suspension or termination of session (object | 3 | 0 (0%)) ['Suspension of session', 'Termination of session', 'nan',]  
    - [03.13] Suspension and termination of session (object | 2 | 0 (0%)) ['No', 'Yes',]  
    - [03.14.01] Adaptations intensity (object | 9 | 0 (0%)) ['<NA>', 'Communication strategy', 'Equipment', 'Exercise selection', 'Exercise selection|Equipment',]  
    - [03.14] Adaptation (object | 1 | 0 (0%)) ['-',]  
    - [03.16] Death (object | 1 | 0 (0%)) ['No',]  
    - [05.01] Therapy phase (object | 3 | 0 (0%)) ['Acute therapy', 'Long-term therapy', 'Post-treatment care',]  
    - [05.02] Group size (object | 5 | 0 (0%)) ['Group 2-5', 'Group 5 to 10', 'Group over 10', 'Individual', 'nan',]  
    - [05.03] Age (object | 6 | 0 (0%)) ['02 to 05 years', '06 to 09 years', '10 to 14 years', '15 to 18 years', '18+ years',]  
    - [05.04] Home (telemedicine) (object | 3 | 1 (1%)) ['<NA>', 'No', 'Yes',]  
    - [05.05] As part of testing (object | 3 | 0 (0%)) ['No', 'Yes', 'nan',]  
    - [05.06] Setting (object | 6 | 0 (0%)) ['At home (via telemedicine)', 'Exercise room', 'Hospital corridor', 'Outdoors',  
    'Patient room',]  
    - [05.07] Main motor skill (object | 16 | 0 (0%)) ['<NA>', 'Coordination', 'Coordination|Speed', 'Coordination|Strength', 'Endurance',]  
    - [05.08] Time point (object | 3 | 0 (0%)) ['First Half', 'Second Half', 'nan',]  
    - [05.09] Fitness level (object | 5 | 0 (0%)) ['(Unknown)', '<NA>', 'Average', 'Good', 'Moderate',]  
    🟠 column stats numeric  
    
    column (n = 178)      |  present   | min | lower |  q25   | median  |  mean   |   q75   | upper | max |  std   |  cv  
    ----------------------+------------+-----+-------+--------+---------+---------+---------+-------+-----+--------+------
    [00.00] ParticipantID | 178 (100%) |   3 |     3 | 51.250 | 111.500 | 105.500 | 156.750 |   213 | 213 | 60.527 | 0.574
    



    
![png](1_create_files/output_53_1.png)
    



