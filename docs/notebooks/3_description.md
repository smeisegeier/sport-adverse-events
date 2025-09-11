# <a id='toc1_'></a>[descriptive analysis](#toc0_)

**Table of contents**<a id='toc0_'></a>    
- [descriptive analysis](#toc1_)    
  - [import data](#toc1_1_)    
  - [tables](#toc1_2_)    
  - [pie charts](#toc1_3_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

    🐍 3.12.9 | 📦 pygwalker: 0.4.9.15 | 📦 pandas: 2.3.2 | 📦 numpy: 1.26.4 | 📦 duckdb: 1.3.2 | 📦 pandas-plots: 0.16.0 | 📦 connection-helper: 0.13.0


## <a id='toc1_1_'></a>[import data](#toc0_)

## <a id='toc1_2_'></a>[tables](#toc0_)

    ['[01.01] CTCAE', '[01.02] Date', '[01.03] Exercise-related', '[02.02] Type', '[02.03] Trigger']



<style type="text/css">
#T_8ac82 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8ac82  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8ac82_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.3%, transparent 17.3%);
  font-family: Courier;
}
#T_8ac82_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.0%, transparent 19.0%);
  font-family: Courier;
}
#T_8ac82_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_8ac82_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.0%, transparent 18.0%);
  font-family: Courier;
}
#T_8ac82_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.7%, transparent 82.7%);
  font-family: Courier;
}
#T_8ac82_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.0%, transparent 81.0%);
  font-family: Courier;
}
#T_8ac82_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_8ac82_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.0%, transparent 82.0%);
  font-family: Courier;
}
#T_8ac82_row2_col0, #T_8ac82_row2_col1, #T_8ac82_row2_col2, #T_8ac82_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_8ac82">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_8ac82_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_8ac82_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_8ac82_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_8ac82_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.02] Date</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_8ac82_level0_row0" class="row_heading level0 row0" >Already present</th>
      <td id="T_8ac82_row0_col0" class="data row0 col0" >23 <span style="color: grey">(12.9%) </span></td>
      <td id="T_8ac82_row0_col1" class="data row0 col1" >8 <span style="color: grey">(4.5%) </span></td>
      <td id="T_8ac82_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_8ac82_row0_col3" class="data row0 col3" >32 <span style="color: grey">(18.0%) </span></td>
    </tr>
    <tr>
      <th id="T_8ac82_level0_row1" class="row_heading level0 row1" >First occurrence</th>
      <td id="T_8ac82_row1_col0" class="data row1 col0" >110 <span style="color: grey">(61.8%) </span></td>
      <td id="T_8ac82_row1_col1" class="data row1 col1" >34 <span style="color: grey">(19.1%) </span></td>
      <td id="T_8ac82_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_8ac82_row1_col3" class="data row1 col3" >146 <span style="color: grey">(82.0%) </span></td>
    </tr>
    <tr>
      <th id="T_8ac82_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_8ac82_row2_col0" class="data row2 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_8ac82_row2_col1" class="data row2 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_8ac82_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_8ac82_row2_col3" class="data row2 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_ab871 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ab871  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ab871_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.4%, transparent 14.4%);
  font-family: Courier;
}
#T_ab871_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_ab871_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_ab871_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.3%, transparent 15.3%);
  font-family: Courier;
}
#T_ab871_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 85.6%, transparent 85.6%);
  font-family: Courier;
}
#T_ab871_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 83.3%, transparent 83.3%);
  font-family: Courier;
}
#T_ab871_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_ab871_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 84.7%, transparent 84.7%);
  font-family: Courier;
}
#T_ab871_row2_col0, #T_ab871_row2_col1, #T_ab871_row2_col2, #T_ab871_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_ab871">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_ab871_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_ab871_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_ab871_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_ab871_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.03] Exercise-related</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ab871_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_ab871_row0_col0" class="data row0 col0" >19 <span style="color: grey">(10.7%) </span></td>
      <td id="T_ab871_row0_col1" class="data row0 col1" >7 <span style="color: grey">(4.0%) </span></td>
      <td id="T_ab871_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_ab871_row0_col3" class="data row0 col3" >27 <span style="color: grey">(15.3%) </span></td>
    </tr>
    <tr>
      <th id="T_ab871_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_ab871_row1_col0" class="data row1 col0" >113 <span style="color: grey">(63.8%) </span></td>
      <td id="T_ab871_row1_col1" class="data row1 col1" >35 <span style="color: grey">(19.8%) </span></td>
      <td id="T_ab871_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_ab871_row1_col3" class="data row1 col3" >150 <span style="color: grey">(84.7%) </span></td>
    </tr>
    <tr>
      <th id="T_ab871_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_ab871_row2_col0" class="data row2 col0" >132 <span style="color: grey">(74.6%) </span></td>
      <td id="T_ab871_row2_col1" class="data row2 col1" >42 <span style="color: grey">(23.7%) </span></td>
      <td id="T_ab871_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_ab871_row2_col3" class="data row2 col3" >177 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_91eda th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_91eda  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_91eda_row0_col0, #T_91eda_row0_col1, #T_91eda_row1_col2, #T_91eda_row2_col1, #T_91eda_row2_col2, #T_91eda_row3_col1, #T_91eda_row3_col2, #T_91eda_row4_col2, #T_91eda_row5_col1, #T_91eda_row5_col2, #T_91eda_row6_col2, #T_91eda_row7_col2, #T_91eda_row9_col2, #T_91eda_row10_col1, #T_91eda_row10_col2, #T_91eda_row11_col1, #T_91eda_row11_col2, #T_91eda_row12_col2, #T_91eda_row13_col2, #T_91eda_row14_col2 {
  width: 10em;
  font-family: Courier;
}
#T_91eda_row0_col2, #T_91eda_row8_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_91eda_row0_col3, #T_91eda_row3_col3, #T_91eda_row7_col3, #T_91eda_row10_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_91eda_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.3%, transparent 17.3%);
  font-family: Courier;
}
#T_91eda_row1_col1, #T_91eda_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.2%, transparent 3.2%);
  font-family: Courier;
}
#T_91eda_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.2%, transparent 13.2%);
  font-family: Courier;
}
#T_91eda_row2_col0, #T_91eda_row6_col0, #T_91eda_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_91eda_row2_col3, #T_91eda_row4_col3, #T_91eda_row11_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_91eda_row3_col0, #T_91eda_row10_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_91eda_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_91eda_row4_col1, #T_91eda_row7_col1, #T_91eda_row9_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_91eda_row5_col0, #T_91eda_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_91eda_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_91eda_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_91eda_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.3%, transparent 38.3%);
  font-family: Courier;
}
#T_91eda_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 48.4%, transparent 48.4%);
  font-family: Courier;
}
#T_91eda_row8_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.2%, transparent 41.2%);
  font-family: Courier;
}
#T_91eda_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.7%, transparent 3.7%);
  font-family: Courier;
}
#T_91eda_row9_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_91eda_row12_col0, #T_91eda_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_91eda_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.9%, transparent 12.9%);
  font-family: Courier;
}
#T_91eda_row12_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.6%, transparent 6.6%);
  font-family: Courier;
}
#T_91eda_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.0%, transparent 21.0%);
  font-family: Courier;
}
#T_91eda_row13_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.8%, transparent 8.8%);
  font-family: Courier;
}
#T_91eda_row14_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.1%, transparent 19.1%);
  font-family: Courier;
}
#T_91eda_row14_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.5%, transparent 6.5%);
  font-family: Courier;
}
#T_91eda_row14_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_91eda_row15_col0, #T_91eda_row15_col1, #T_91eda_row15_col2, #T_91eda_row15_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_91eda">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_91eda_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_91eda_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_91eda_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_91eda_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_91eda_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_91eda_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_91eda_row0_col3" class="data row0 col3" >2 <span style="color: grey">(0.9%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_91eda_row1_col0" class="data row1 col0" >28 <span style="color: grey">(12.3%) </span></td>
      <td id="T_91eda_row1_col1" class="data row1 col1" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_91eda_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row1_col3" class="data row1 col3" >30 <span style="color: grey">(13.2%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_91eda_row2_col0" class="data row2 col0" >4 <span style="color: grey">(1.8%) </span></td>
      <td id="T_91eda_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row2_col3" class="data row2 col3" >4 <span style="color: grey">(1.8%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_91eda_row3_col0" class="data row3 col0" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_91eda_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row3_col3" class="data row3 col3" >2 <span style="color: grey">(0.9%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_91eda_row4_col0" class="data row4 col0" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_91eda_row4_col1" class="data row4 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_91eda_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row4_col3" class="data row4 col3" >4 <span style="color: grey">(1.8%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_91eda_row5_col0" class="data row5 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_91eda_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row5_col3" class="data row5 col3" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_91eda_row6_col0" class="data row6 col0" >4 <span style="color: grey">(1.8%) </span></td>
      <td id="T_91eda_row6_col1" class="data row6 col1" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_91eda_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row6_col3" class="data row6 col3" >6 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_91eda_row7_col0" class="data row7 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_91eda_row7_col1" class="data row7 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_91eda_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row7_col3" class="data row7 col3" >2 <span style="color: grey">(0.9%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_91eda_row8_col0" class="data row8 col0" >62 <span style="color: grey">(27.2%) </span></td>
      <td id="T_91eda_row8_col1" class="data row8 col1" >30 <span style="color: grey">(13.2%) </span></td>
      <td id="T_91eda_row8_col2" class="data row8 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_91eda_row8_col3" class="data row8 col3" >94 <span style="color: grey">(41.2%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_91eda_row9_col0" class="data row9 col0" >6 <span style="color: grey">(2.6%) </span></td>
      <td id="T_91eda_row9_col1" class="data row9 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_91eda_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row9_col3" class="data row9 col3" >7 <span style="color: grey">(3.1%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_91eda_row10_col0" class="data row10 col0" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_91eda_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row10_col3" class="data row10 col3" >2 <span style="color: grey">(0.9%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_91eda_row11_col0" class="data row11 col0" >4 <span style="color: grey">(1.8%) </span></td>
      <td id="T_91eda_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row11_col3" class="data row11 col3" >4 <span style="color: grey">(1.8%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_91eda_row12_col0" class="data row12 col0" >7 <span style="color: grey">(3.1%) </span></td>
      <td id="T_91eda_row12_col1" class="data row12 col1" >8 <span style="color: grey">(3.5%) </span></td>
      <td id="T_91eda_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row12_col3" class="data row12 col3" >15 <span style="color: grey">(6.6%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_91eda_row13_col0" class="data row13 col0" >7 <span style="color: grey">(3.1%) </span></td>
      <td id="T_91eda_row13_col1" class="data row13 col1" >13 <span style="color: grey">(5.7%) </span></td>
      <td id="T_91eda_row13_col2" class="data row13 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row13_col3" class="data row13 col3" >20 <span style="color: grey">(8.8%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_91eda_row14_col0" class="data row14 col0" >31 <span style="color: grey">(13.6%) </span></td>
      <td id="T_91eda_row14_col1" class="data row14 col1" >4 <span style="color: grey">(1.8%) </span></td>
      <td id="T_91eda_row14_col2" class="data row14 col2" ><span style="color: grey">0 </span></td>
      <td id="T_91eda_row14_col3" class="data row14 col3" >35 <span style="color: grey">(15.4%) </span></td>
    </tr>
    <tr>
      <th id="T_91eda_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_91eda_row15_col0" class="data row15 col0" >162 <span style="color: grey">(71.1%) </span></td>
      <td id="T_91eda_row15_col1" class="data row15 col1" >62 <span style="color: grey">(27.2%) </span></td>
      <td id="T_91eda_row15_col2" class="data row15 col2" >4 <span style="color: grey">(1.8%) </span></td>
      <td id="T_91eda_row15_col3" class="data row15 col3" >228 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_440f4 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_440f4  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_440f4_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.4%, transparent 6.4%);
  font-family: Courier;
}
#T_440f4_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.3%, transparent 13.3%);
  font-family: Courier;
}
#T_440f4_row0_col2, #T_440f4_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_440f4_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.1%, transparent 8.1%);
  font-family: Courier;
}
#T_440f4_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_440f4_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_440f4_row1_col2, #T_440f4_row2_col2, #T_440f4_row3_col2, #T_440f4_row4_col1, #T_440f4_row4_col2, #T_440f4_row6_col2 {
  width: 10em;
  font-family: Courier;
}
#T_440f4_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
#T_440f4_row2_col0, #T_440f4_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.2%, transparent 3.2%);
  font-family: Courier;
}
#T_440f4_row2_col1, #T_440f4_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_440f4_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.5%, transparent 30.5%);
  font-family: Courier;
}
#T_440f4_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.3%, transparent 18.3%);
  font-family: Courier;
}
#T_440f4_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.5%, transparent 27.5%);
  font-family: Courier;
}
#T_440f4_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_440f4_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_440f4_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.7%, transparent 42.7%);
  font-family: Courier;
}
#T_440f4_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.3%, transparent 28.3%);
  font-family: Courier;
}
#T_440f4_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_440f4_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.8%, transparent 39.8%);
  font-family: Courier;
}
#T_440f4_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.0%, transparent 5.0%);
  font-family: Courier;
}
#T_440f4_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.6%, transparent 4.6%);
  font-family: Courier;
}
#T_440f4_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.5%, transparent 9.5%);
  font-family: Courier;
}
#T_440f4_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.7%, transparent 31.7%);
  font-family: Courier;
}
#T_440f4_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.4%, transparent 14.4%);
  font-family: Courier;
}
#T_440f4_row8_col0, #T_440f4_row8_col1, #T_440f4_row8_col2, #T_440f4_row8_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_440f4">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_440f4_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_440f4_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_440f4_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_440f4_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_440f4_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_440f4_row0_col0" class="data row0 col0" >14 <span style="color: grey">(4.9%) </span></td>
      <td id="T_440f4_row0_col1" class="data row0 col1" >8 <span style="color: grey">(2.8%) </span></td>
      <td id="T_440f4_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_440f4_row0_col3" class="data row0 col3" >23 <span style="color: grey">(8.1%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_440f4_row1_col0" class="data row1 col0" >5 <span style="color: grey">(1.8%) </span></td>
      <td id="T_440f4_row1_col1" class="data row1 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_440f4_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_440f4_row1_col3" class="data row1 col3" >6 <span style="color: grey">(2.1%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_440f4_row2_col0" class="data row2 col0" >7 <span style="color: grey">(2.5%) </span></td>
      <td id="T_440f4_row2_col1" class="data row2 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_440f4_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_440f4_row2_col3" class="data row2 col3" >9 <span style="color: grey">(3.2%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_440f4_row3_col0" class="data row3 col0" >67 <span style="color: grey">(23.6%) </span></td>
      <td id="T_440f4_row3_col1" class="data row3 col1" >11 <span style="color: grey">(3.9%) </span></td>
      <td id="T_440f4_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_440f4_row3_col3" class="data row3 col3" >78 <span style="color: grey">(27.5%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_440f4_row4_col0" class="data row4 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_440f4_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_440f4_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_440f4_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_440f4_row5_col0" class="data row5 col0" >94 <span style="color: grey">(33.1%) </span></td>
      <td id="T_440f4_row5_col1" class="data row5 col1" >17 <span style="color: grey">(6.0%) </span></td>
      <td id="T_440f4_row5_col2" class="data row5 col2" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_440f4_row5_col3" class="data row5 col3" >113 <span style="color: grey">(39.8%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_440f4_row6_col0" class="data row6 col0" >11 <span style="color: grey">(3.9%) </span></td>
      <td id="T_440f4_row6_col1" class="data row6 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_440f4_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_440f4_row6_col3" class="data row6 col3" >13 <span style="color: grey">(4.6%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_440f4_row7_col0" class="data row7 col0" >21 <span style="color: grey">(7.4%) </span></td>
      <td id="T_440f4_row7_col1" class="data row7 col1" >19 <span style="color: grey">(6.7%) </span></td>
      <td id="T_440f4_row7_col2" class="data row7 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_440f4_row7_col3" class="data row7 col3" >41 <span style="color: grey">(14.4%) </span></td>
    </tr>
    <tr>
      <th id="T_440f4_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_440f4_row8_col0" class="data row8 col0" >220 <span style="color: grey">(77.5%) </span></td>
      <td id="T_440f4_row8_col1" class="data row8 col1" >60 <span style="color: grey">(21.1%) </span></td>
      <td id="T_440f4_row8_col2" class="data row8 col2" >4 <span style="color: grey">(1.4%) </span></td>
      <td id="T_440f4_row8_col3" class="data row8 col3" >284 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_386ce th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_386ce  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_386ce_row0_col0, #T_386ce_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.1%, transparent 5.1%);
  font-family: Courier;
}
#T_386ce_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.7%, transparent 8.7%);
  font-family: Courier;
}
#T_386ce_row0_col2, #T_386ce_row1_col2, #T_386ce_row2_col2, #T_386ce_row3_col2, #T_386ce_row4_col1, #T_386ce_row4_col2, #T_386ce_row6_col2, #T_386ce_row7_col2, #T_386ce_row8_col1, #T_386ce_row8_col2, #T_386ce_row9_col0, #T_386ce_row9_col2, #T_386ce_row11_col2 {
  width: 10em;
  font-family: Courier;
}
#T_386ce_row0_col3, #T_386ce_row11_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.9%, transparent 5.9%);
  font-family: Courier;
}
#T_386ce_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.5%, transparent 6.5%);
  font-family: Courier;
}
#T_386ce_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_386ce_row2_col0, #T_386ce_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_386ce_row2_col1, #T_386ce_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_386ce_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_386ce_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_386ce_row3_col1, #T_386ce_row9_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_386ce_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_386ce_row4_col0, #T_386ce_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_386ce_row4_col3, #T_386ce_row8_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_386ce_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_386ce_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_386ce_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_386ce_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.3%, transparent 7.3%);
  font-family: Courier;
}
#T_386ce_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.7%, transparent 21.7%);
  font-family: Courier;
}
#T_386ce_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.8%, transparent 10.8%);
  font-family: Courier;
}
#T_386ce_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.1%, transparent 43.1%);
  font-family: Courier;
}
#T_386ce_row7_col1, #T_386ce_row11_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.0%, transparent 13.0%);
  font-family: Courier;
}
#T_386ce_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.9%, transparent 34.9%);
  font-family: Courier;
}
#T_386ce_row9_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_386ce_row10_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.9%, transparent 21.9%);
  font-family: Courier;
}
#T_386ce_row10_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.9%, transparent 23.9%);
  font-family: Courier;
}
#T_386ce_row10_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_386ce_row10_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.1%, transparent 23.1%);
  font-family: Courier;
}
#T_386ce_row12_col0, #T_386ce_row12_col1, #T_386ce_row12_col2, #T_386ce_row12_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_386ce">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_386ce_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_386ce_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_386ce_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_386ce_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.04] Affected body parts</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_386ce_level0_row0" class="row_heading level0 row0" >Abdomen</th>
      <td id="T_386ce_row0_col0" class="data row0 col0" >7 <span style="color: grey">(3.8%) </span></td>
      <td id="T_386ce_row0_col1" class="data row0 col1" >4 <span style="color: grey">(2.2%) </span></td>
      <td id="T_386ce_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row0_col3" class="data row0 col3" >11 <span style="color: grey">(5.9%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row1" class="row_heading level0 row1" >Back</th>
      <td id="T_386ce_row1_col0" class="data row1 col0" >7 <span style="color: grey">(3.8%) </span></td>
      <td id="T_386ce_row1_col1" class="data row1 col1" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_386ce_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row1_col3" class="data row1 col3" >10 <span style="color: grey">(5.4%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row2" class="row_heading level0 row2" >Buttocks</th>
      <td id="T_386ce_row2_col0" class="data row2 col0" >5 <span style="color: grey">(2.7%) </span></td>
      <td id="T_386ce_row2_col1" class="data row2 col1" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_386ce_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row2_col3" class="data row2 col3" >7 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row3" class="row_heading level0 row3" >Chest</th>
      <td id="T_386ce_row3_col0" class="data row3 col0" >4 <span style="color: grey">(2.2%) </span></td>
      <td id="T_386ce_row3_col1" class="data row3 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_386ce_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row3_col3" class="data row3 col3" >5 <span style="color: grey">(2.7%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row4" class="row_heading level0 row4" >Coccyx</th>
      <td id="T_386ce_row4_col0" class="data row4 col0" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_386ce_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row4_col3" class="data row4 col3" >2 <span style="color: grey">(1.1%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row5" class="row_heading level0 row5" >Full body</th>
      <td id="T_386ce_row5_col0" class="data row5 col0" >6 <span style="color: grey">(3.2%) </span></td>
      <td id="T_386ce_row5_col1" class="data row5 col1" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_386ce_row5_col2" class="data row5 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_386ce_row5_col3" class="data row5 col3" >9 <span style="color: grey">(4.8%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row6" class="row_heading level0 row6" >Head</th>
      <td id="T_386ce_row6_col0" class="data row6 col0" >10 <span style="color: grey">(5.4%) </span></td>
      <td id="T_386ce_row6_col1" class="data row6 col1" >10 <span style="color: grey">(5.4%) </span></td>
      <td id="T_386ce_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row6_col3" class="data row6 col3" >20 <span style="color: grey">(10.8%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row7" class="row_heading level0 row7" >Innere Medizin</th>
      <td id="T_386ce_row7_col0" class="data row7 col0" >59 <span style="color: grey">(31.7%) </span></td>
      <td id="T_386ce_row7_col1" class="data row7 col1" >6 <span style="color: grey">(3.2%) </span></td>
      <td id="T_386ce_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row7_col3" class="data row7 col3" >65 <span style="color: grey">(34.9%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row8" class="row_heading level0 row8" >Intestine</th>
      <td id="T_386ce_row8_col0" class="data row8 col0" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_386ce_row8_col1" class="data row8 col1" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row8_col2" class="data row8 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row8_col3" class="data row8 col3" >2 <span style="color: grey">(1.1%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row9" class="row_heading level0 row9" >Intimate area</th>
      <td id="T_386ce_row9_col0" class="data row9 col0" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row9_col1" class="data row9 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_386ce_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row9_col3" class="data row9 col3" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row10" class="row_heading level0 row10" >Lower extremities</th>
      <td id="T_386ce_row10_col0" class="data row10 col0" >30 <span style="color: grey">(16.1%) </span></td>
      <td id="T_386ce_row10_col1" class="data row10 col1" >11 <span style="color: grey">(5.9%) </span></td>
      <td id="T_386ce_row10_col2" class="data row10 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_386ce_row10_col3" class="data row10 col3" >43 <span style="color: grey">(23.1%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row11" class="row_heading level0 row11" >Upper extremities</th>
      <td id="T_386ce_row11_col0" class="data row11 col0" >5 <span style="color: grey">(2.7%) </span></td>
      <td id="T_386ce_row11_col1" class="data row11 col1" >6 <span style="color: grey">(3.2%) </span></td>
      <td id="T_386ce_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_386ce_row11_col3" class="data row11 col3" >11 <span style="color: grey">(5.9%) </span></td>
    </tr>
    <tr>
      <th id="T_386ce_level0_row12" class="row_heading level0 row12" >Total</th>
      <td id="T_386ce_row12_col0" class="data row12 col0" >137 <span style="color: grey">(73.7%) </span></td>
      <td id="T_386ce_row12_col1" class="data row12 col1" >46 <span style="color: grey">(24.7%) </span></td>
      <td id="T_386ce_row12_col2" class="data row12 col2" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_386ce_row12_col3" class="data row12 col3" >186 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_c6607 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c6607  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c6607_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 99.2%, transparent 99.2%);
  font-family: Courier;
}
#T_c6607_row0_col1, #T_c6607_row3_col0, #T_c6607_row3_col1, #T_c6607_row3_col2, #T_c6607_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_c6607_row0_col2, #T_c6607_row1_col2, #T_c6607_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_c6607_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.3%, transparent 98.3%);
  font-family: Courier;
}
#T_c6607_row1_col0, #T_c6607_row1_col1, #T_c6607_row2_col1 {
  width: 10em;
  font-family: Courier;
}
#T_c6607_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_c6607_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_c6607_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
</style>
<table id="T_c6607">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_c6607_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_c6607_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_c6607_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_c6607_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.02] With hospitalization</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c6607_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_c6607_row0_col0" class="data row0 col0" >132 <span style="color: grey">(74.2%) </span></td>
      <td id="T_c6607_row0_col1" class="data row0 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_c6607_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_c6607_row0_col3" class="data row0 col3" >175 <span style="color: grey">(98.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c6607_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_c6607_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c6607_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c6607_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_c6607_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c6607_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_c6607_row2_col0" class="data row2 col0" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_c6607_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c6607_row2_col2" class="data row2 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_c6607_row2_col3" class="data row2 col3" >2 <span style="color: grey">(1.1%) </span></td>
    </tr>
    <tr>
      <th id="T_c6607_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_c6607_row3_col0" class="data row3 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_c6607_row3_col1" class="data row3 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_c6607_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_c6607_row3_col3" class="data row3 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_0c9cd th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0c9cd  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0c9cd_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.0%, transparent 91.0%);
  font-family: Courier;
}
#T_0c9cd_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.0%, transparent 19.0%);
  font-family: Courier;
}
#T_0c9cd_row0_col2, #T_0c9cd_row1_col1, #T_0c9cd_row1_col2 {
  width: 10em;
  font-family: Courier;
}
#T_0c9cd_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 72.5%, transparent 72.5%);
  font-family: Courier;
}
#T_0c9cd_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_0c9cd_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_0c9cd_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_0c9cd_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.0%, transparent 81.0%);
  font-family: Courier;
}
#T_0c9cd_row2_col2, #T_0c9cd_row3_col0, #T_0c9cd_row3_col1, #T_0c9cd_row3_col2, #T_0c9cd_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_0c9cd_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.8%, transparent 25.8%);
  font-family: Courier;
}
</style>
<table id="T_0c9cd">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_0c9cd_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_0c9cd_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_0c9cd_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_0c9cd_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.03] Medical follow-up treatment</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_0c9cd_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_0c9cd_row0_col0" class="data row0 col0" >121 <span style="color: grey">(68.0%) </span></td>
      <td id="T_0c9cd_row0_col1" class="data row0 col1" >8 <span style="color: grey">(4.5%) </span></td>
      <td id="T_0c9cd_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0c9cd_row0_col3" class="data row0 col3" >129 <span style="color: grey">(72.5%) </span></td>
    </tr>
    <tr>
      <th id="T_0c9cd_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_0c9cd_row1_col0" class="data row1 col0" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_0c9cd_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_0c9cd_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0c9cd_row1_col3" class="data row1 col3" >3 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_0c9cd_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_0c9cd_row2_col0" class="data row2 col0" >9 <span style="color: grey">(5.1%) </span></td>
      <td id="T_0c9cd_row2_col1" class="data row2 col1" >34 <span style="color: grey">(19.1%) </span></td>
      <td id="T_0c9cd_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_0c9cd_row2_col3" class="data row2 col3" >46 <span style="color: grey">(25.8%) </span></td>
    </tr>
    <tr>
      <th id="T_0c9cd_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_0c9cd_row3_col0" class="data row3 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_0c9cd_row3_col1" class="data row3 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_0c9cd_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_0c9cd_row3_col3" class="data row3 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_867ff th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_867ff  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_867ff_row0_col0, #T_867ff_row0_col1, #T_867ff_row0_col2, #T_867ff_row0_col3, #T_867ff_row1_col0, #T_867ff_row1_col1, #T_867ff_row1_col2, #T_867ff_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_867ff">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_867ff_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_867ff_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_867ff_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_867ff_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.04] With delayed therapy protocol</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_867ff_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_867ff_row0_col0" class="data row0 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_867ff_row0_col1" class="data row0 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_867ff_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_867ff_row0_col3" class="data row0 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_867ff_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_867ff_row1_col0" class="data row1 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_867ff_row1_col1" class="data row1 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_867ff_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_867ff_row1_col3" class="data row1 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_bdde1 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_bdde1  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_bdde1_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 99.2%, transparent 99.2%);
  font-family: Courier;
}
#T_bdde1_row0_col1, #T_bdde1_row1_col2, #T_bdde1_row2_col0, #T_bdde1_row2_col1, #T_bdde1_row2_col2, #T_bdde1_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_bdde1_row0_col2, #T_bdde1_row1_col1 {
  width: 10em;
  font-family: Courier;
}
#T_bdde1_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.8%, transparent 97.8%);
  font-family: Courier;
}
#T_bdde1_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_bdde1_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
</style>
<table id="T_bdde1">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_bdde1_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_bdde1_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_bdde1_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_bdde1_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.06] Increased care needs</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_bdde1_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_bdde1_row0_col0" class="data row0 col0" >132 <span style="color: grey">(74.2%) </span></td>
      <td id="T_bdde1_row0_col1" class="data row0 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_bdde1_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_bdde1_row0_col3" class="data row0 col3" >174 <span style="color: grey">(97.8%) </span></td>
    </tr>
    <tr>
      <th id="T_bdde1_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_bdde1_row1_col0" class="data row1 col0" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_bdde1_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_bdde1_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_bdde1_row1_col3" class="data row1 col3" >4 <span style="color: grey">(2.2%) </span></td>
    </tr>
    <tr>
      <th id="T_bdde1_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_bdde1_row2_col0" class="data row2 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_bdde1_row2_col1" class="data row2 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_bdde1_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_bdde1_row2_col3" class="data row2 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_2919f th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2919f  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2919f_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 84.1%, transparent 84.1%);
  font-family: Courier;
}
#T_2919f_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 63.2%, transparent 63.2%);
  font-family: Courier;
}
#T_2919f_row0_col2, #T_2919f_row1_col2, #T_2919f_row2_col0 {
  width: 10em;
  font-family: Courier;
}
#T_2919f_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 78.0%, transparent 78.0%);
  font-family: Courier;
}
#T_2919f_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.9%, transparent 15.9%);
  font-family: Courier;
}
#T_2919f_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.6%, transparent 31.6%);
  font-family: Courier;
}
#T_2919f_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.1%, transparent 19.1%);
  font-family: Courier;
}
#T_2919f_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_2919f_row2_col2, #T_2919f_row3_col0, #T_2919f_row3_col1, #T_2919f_row3_col2, #T_2919f_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_2919f_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
</style>
<table id="T_2919f">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_2919f_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_2919f_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_2919f_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_2919f_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.07] With medication administration</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2919f_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_2919f_row0_col0" class="data row0 col0" >111 <span style="color: grey">(64.2%) </span></td>
      <td id="T_2919f_row0_col1" class="data row0 col1" >24 <span style="color: grey">(13.9%) </span></td>
      <td id="T_2919f_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2919f_row0_col3" class="data row0 col3" >135 <span style="color: grey">(78.0%) </span></td>
    </tr>
    <tr>
      <th id="T_2919f_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_2919f_row1_col0" class="data row1 col0" >21 <span style="color: grey">(12.1%) </span></td>
      <td id="T_2919f_row1_col1" class="data row1 col1" >12 <span style="color: grey">(6.9%) </span></td>
      <td id="T_2919f_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2919f_row1_col3" class="data row1 col3" >33 <span style="color: grey">(19.1%) </span></td>
    </tr>
    <tr>
      <th id="T_2919f_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_2919f_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2919f_row2_col1" class="data row2 col1" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_2919f_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_2919f_row2_col3" class="data row2 col3" >5 <span style="color: grey">(2.9%) </span></td>
    </tr>
    <tr>
      <th id="T_2919f_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_2919f_row3_col0" class="data row3 col0" >132 <span style="color: grey">(76.3%) </span></td>
      <td id="T_2919f_row3_col1" class="data row3 col1" >38 <span style="color: grey">(22.0%) </span></td>
      <td id="T_2919f_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_2919f_row3_col3" class="data row3 col3" >173 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e9563 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e9563  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e9563_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_e9563_row0_col1, #T_e9563_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_e9563_row0_col2, #T_e9563_row2_col0, #T_e9563_row2_col1, #T_e9563_row2_col2, #T_e9563_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e9563_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.8%, transparent 31.8%);
  font-family: Courier;
}
#T_e9563_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.0%, transparent 75.0%);
  font-family: Courier;
}
#T_e9563_row1_col2 {
  width: 10em;
  font-family: Courier;
}
#T_e9563_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.2%, transparent 68.2%);
  font-family: Courier;
}
</style>
<table id="T_e9563">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e9563_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e9563_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e9563_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e9563_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.08] Occurrence of fear and uncertainty</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e9563_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_e9563_row0_col0" class="data row0 col0" >33 <span style="color: grey">(18.8%) </span></td>
      <td id="T_e9563_row0_col1" class="data row0 col1" >21 <span style="color: grey">(11.9%) </span></td>
      <td id="T_e9563_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_e9563_row0_col3" class="data row0 col3" >56 <span style="color: grey">(31.8%) </span></td>
    </tr>
    <tr>
      <th id="T_e9563_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_e9563_row1_col0" class="data row1 col0" >99 <span style="color: grey">(56.2%) </span></td>
      <td id="T_e9563_row1_col1" class="data row1 col1" >21 <span style="color: grey">(11.9%) </span></td>
      <td id="T_e9563_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e9563_row1_col3" class="data row1 col3" >120 <span style="color: grey">(68.2%) </span></td>
    </tr>
    <tr>
      <th id="T_e9563_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_e9563_row2_col0" class="data row2 col0" >132 <span style="color: grey">(75.0%) </span></td>
      <td id="T_e9563_row2_col1" class="data row2 col1" >42 <span style="color: grey">(23.9%) </span></td>
      <td id="T_e9563_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_e9563_row2_col3" class="data row2 col3" >176 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_76e1a th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_76e1a  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_76e1a_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.3%, transparent 17.3%);
  font-family: Courier;
}
#T_76e1a_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_76e1a_row0_col2, #T_76e1a_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_76e1a_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.6%, transparent 13.6%);
  font-family: Courier;
}
#T_76e1a_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 63.5%, transparent 63.5%);
  font-family: Courier;
}
#T_76e1a_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 63.3%, transparent 63.3%);
  font-family: Courier;
}
#T_76e1a_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 61.4%, transparent 61.4%);
  font-family: Courier;
}
#T_76e1a_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_76e1a_row2_col1, #T_76e1a_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_76e1a_row2_col2, #T_76e1a_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_76e1a_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_76e1a_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.8%, transparent 5.8%);
  font-family: Courier;
}
#T_76e1a_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.3%, transparent 13.3%);
  font-family: Courier;
}
#T_76e1a_row3_col3, #T_76e1a_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.1%, transparent 9.1%);
  font-family: Courier;
}
#T_76e1a_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.6%, transparent 9.6%);
  font-family: Courier;
}
#T_76e1a_row4_col2 {
  width: 10em;
  font-family: Courier;
}
#T_76e1a_row5_col0, #T_76e1a_row5_col1, #T_76e1a_row5_col2, #T_76e1a_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_76e1a">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_76e1a_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_76e1a_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_76e1a_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_76e1a_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.08.01] Affected person</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_76e1a_level0_row0" class="row_heading level0 row0" >BeIn the treatment team</th>
      <td id="T_76e1a_row0_col0" class="data row0 col0" >9 <span style="color: grey">(10.2%) </span></td>
      <td id="T_76e1a_row0_col1" class="data row0 col1" >1 <span style="color: grey">(1.1%) </span></td>
      <td id="T_76e1a_row0_col2" class="data row0 col2" >2 <span style="color: grey">(2.3%) </span></td>
      <td id="T_76e1a_row0_col3" class="data row0 col3" >12 <span style="color: grey">(13.6%) </span></td>
    </tr>
    <tr>
      <th id="T_76e1a_level0_row1" class="row_heading level0 row1" >For affected individuals</th>
      <td id="T_76e1a_row1_col0" class="data row1 col0" >33 <span style="color: grey">(37.5%) </span></td>
      <td id="T_76e1a_row1_col1" class="data row1 col1" >19 <span style="color: grey">(21.6%) </span></td>
      <td id="T_76e1a_row1_col2" class="data row1 col2" >2 <span style="color: grey">(2.3%) </span></td>
      <td id="T_76e1a_row1_col3" class="data row1 col3" >54 <span style="color: grey">(61.4%) </span></td>
    </tr>
    <tr>
      <th id="T_76e1a_level0_row2" class="row_heading level0 row2" >For parents des Betroffenen</th>
      <td id="T_76e1a_row2_col0" class="data row2 col0" >2 <span style="color: grey">(2.3%) </span></td>
      <td id="T_76e1a_row2_col1" class="data row2 col1" >3 <span style="color: grey">(3.4%) </span></td>
      <td id="T_76e1a_row2_col2" class="data row2 col2" >1 <span style="color: grey">(1.1%) </span></td>
      <td id="T_76e1a_row2_col3" class="data row2 col3" >6 <span style="color: grey">(6.8%) </span></td>
    </tr>
    <tr>
      <th id="T_76e1a_level0_row3" class="row_heading level0 row3" >For the excercise experts</th>
      <td id="T_76e1a_row3_col0" class="data row3 col0" >3 <span style="color: grey">(3.4%) </span></td>
      <td id="T_76e1a_row3_col1" class="data row3 col1" >4 <span style="color: grey">(4.5%) </span></td>
      <td id="T_76e1a_row3_col2" class="data row3 col2" >1 <span style="color: grey">(1.1%) </span></td>
      <td id="T_76e1a_row3_col3" class="data row3 col3" >8 <span style="color: grey">(9.1%) </span></td>
    </tr>
    <tr>
      <th id="T_76e1a_level0_row4" class="row_heading level0 row4" >Mit der Ablehnung weiterer sporttherapheutischer Angebote</th>
      <td id="T_76e1a_row4_col0" class="data row4 col0" >5 <span style="color: grey">(5.7%) </span></td>
      <td id="T_76e1a_row4_col1" class="data row4 col1" >3 <span style="color: grey">(3.4%) </span></td>
      <td id="T_76e1a_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_76e1a_row4_col3" class="data row4 col3" >8 <span style="color: grey">(9.1%) </span></td>
    </tr>
    <tr>
      <th id="T_76e1a_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_76e1a_row5_col0" class="data row5 col0" >52 <span style="color: grey">(59.1%) </span></td>
      <td id="T_76e1a_row5_col1" class="data row5 col1" >30 <span style="color: grey">(34.1%) </span></td>
      <td id="T_76e1a_row5_col2" class="data row5 col2" >6 <span style="color: grey">(6.8%) </span></td>
      <td id="T_76e1a_row5_col3" class="data row5 col3" >88 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_90a4f th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_90a4f  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_90a4f_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_90a4f_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.8%, transparent 9.8%);
  font-family: Courier;
}
#T_90a4f_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_90a4f_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_90a4f_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_90a4f_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.2%, transparent 90.2%);
  font-family: Courier;
}
#T_90a4f_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_90a4f_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 94.4%, transparent 94.4%);
  font-family: Courier;
}
#T_90a4f_row2_col0, #T_90a4f_row2_col1, #T_90a4f_row2_col2, #T_90a4f_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_90a4f">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_90a4f_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_90a4f_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_90a4f_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_90a4f_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.09] Structural adjustment</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_90a4f_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_90a4f_row0_col0" class="data row0 col0" >5 <span style="color: grey">(2.8%) </span></td>
      <td id="T_90a4f_row0_col1" class="data row0 col1" >4 <span style="color: grey">(2.3%) </span></td>
      <td id="T_90a4f_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_90a4f_row0_col3" class="data row0 col3" >10 <span style="color: grey">(5.6%) </span></td>
    </tr>
    <tr>
      <th id="T_90a4f_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_90a4f_row1_col0" class="data row1 col0" >128 <span style="color: grey">(72.3%) </span></td>
      <td id="T_90a4f_row1_col1" class="data row1 col1" >37 <span style="color: grey">(20.9%) </span></td>
      <td id="T_90a4f_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_90a4f_row1_col3" class="data row1 col3" >167 <span style="color: grey">(94.4%) </span></td>
    </tr>
    <tr>
      <th id="T_90a4f_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_90a4f_row2_col0" class="data row2 col0" >133 <span style="color: grey">(75.1%) </span></td>
      <td id="T_90a4f_row2_col1" class="data row2 col1" >41 <span style="color: grey">(23.2%) </span></td>
      <td id="T_90a4f_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_90a4f_row2_col3" class="data row2 col3" >177 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_c79c2 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c79c2  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c79c2_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 78.2%, transparent 78.2%);
  font-family: Courier;
}
#T_c79c2_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 45.2%, transparent 45.2%);
  font-family: Courier;
}
#T_c79c2_row0_col2, #T_c79c2_row1_col1, #T_c79c2_row1_col2, #T_c79c2_row3_col2, #T_c79c2_row4_col2, #T_c79c2_row5_col1, #T_c79c2_row5_col2 {
  width: 10em;
  font-family: Courier;
}
#T_c79c2_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.1%, transparent 69.1%);
  font-family: Courier;
}
#T_c79c2_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_c79c2_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_c79c2_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.5%, transparent 7.5%);
  font-family: Courier;
}
#T_c79c2_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_c79c2_row2_col2, #T_c79c2_row6_col0, #T_c79c2_row6_col1, #T_c79c2_row6_col2, #T_c79c2_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_c79c2_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.2%, transparent 15.2%);
  font-family: Courier;
}
#T_c79c2_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.3%, transparent 11.3%);
  font-family: Courier;
}
#T_c79c2_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_c79c2_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.4%, transparent 12.4%);
  font-family: Courier;
}
#T_c79c2_row4_col0, #T_c79c2_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_c79c2_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_c79c2_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_c79c2_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
</style>
<table id="T_c79c2">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_c79c2_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_c79c2_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_c79c2_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_c79c2_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.10.01] Approver</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c79c2_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_c79c2_row0_col0" class="data row0 col0" >104 <span style="color: grey">(58.4%) </span></td>
      <td id="T_c79c2_row0_col1" class="data row0 col1" >19 <span style="color: grey">(10.7%) </span></td>
      <td id="T_c79c2_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c79c2_row0_col3" class="data row0 col3" >123 <span style="color: grey">(69.1%) </span></td>
    </tr>
    <tr>
      <th id="T_c79c2_level0_row1" class="row_heading level0 row1" >Eltern</th>
      <td id="T_c79c2_row1_col0" class="data row1 col0" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_c79c2_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c79c2_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c79c2_row1_col3" class="data row1 col3" >2 <span style="color: grey">(1.1%) </span></td>
    </tr>
    <tr>
      <th id="T_c79c2_level0_row2" class="row_heading level0 row2" >Medizin</th>
      <td id="T_c79c2_row2_col0" class="data row2 col0" >10 <span style="color: grey">(5.6%) </span></td>
      <td id="T_c79c2_row2_col1" class="data row2 col1" >14 <span style="color: grey">(7.9%) </span></td>
      <td id="T_c79c2_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_c79c2_row2_col3" class="data row2 col3" >27 <span style="color: grey">(15.2%) </span></td>
    </tr>
    <tr>
      <th id="T_c79c2_level0_row3" class="row_heading level0 row3" >Pflege</th>
      <td id="T_c79c2_row3_col0" class="data row3 col0" >15 <span style="color: grey">(8.4%) </span></td>
      <td id="T_c79c2_row3_col1" class="data row3 col1" >7 <span style="color: grey">(3.9%) </span></td>
      <td id="T_c79c2_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c79c2_row3_col3" class="data row3 col3" >22 <span style="color: grey">(12.4%) </span></td>
    </tr>
    <tr>
      <th id="T_c79c2_level0_row4" class="row_heading level0 row4" >Physiotherapie</th>
      <td id="T_c79c2_row4_col0" class="data row4 col0" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_c79c2_row4_col1" class="data row4 col1" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_c79c2_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c79c2_row4_col3" class="data row4 col3" >3 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c79c2_level0_row5" class="row_heading level0 row5" >Psychosozialer Dienst</th>
      <td id="T_c79c2_row5_col0" class="data row5 col0" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_c79c2_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c79c2_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c79c2_row5_col3" class="data row5 col3" >1 <span style="color: grey">(0.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c79c2_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_c79c2_row6_col0" class="data row6 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_c79c2_row6_col1" class="data row6 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_c79c2_row6_col2" class="data row6 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_c79c2_row6_col3" class="data row6 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_dc938 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dc938  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dc938_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_dc938_row0_col1, #T_dc938_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_dc938_row0_col2, #T_dc938_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_dc938_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.1%, transparent 10.1%);
  font-family: Courier;
}
#T_dc938_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.5%, transparent 98.5%);
  font-family: Courier;
}
#T_dc938_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 89.9%, transparent 89.9%);
  font-family: Courier;
}
#T_dc938_row2_col0, #T_dc938_row2_col1, #T_dc938_row2_col2, #T_dc938_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_dc938">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_dc938_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_dc938_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_dc938_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_dc938_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.11] Application RICE rule (Rest, Ice, Compression, Elevation)</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_dc938_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_dc938_row0_col0" class="data row0 col0" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_dc938_row0_col1" class="data row0 col1" >14 <span style="color: grey">(7.9%) </span></td>
      <td id="T_dc938_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_dc938_row0_col3" class="data row0 col3" >18 <span style="color: grey">(10.1%) </span></td>
    </tr>
    <tr>
      <th id="T_dc938_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_dc938_row1_col0" class="data row1 col0" >131 <span style="color: grey">(73.6%) </span></td>
      <td id="T_dc938_row1_col1" class="data row1 col1" >28 <span style="color: grey">(15.7%) </span></td>
      <td id="T_dc938_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_dc938_row1_col3" class="data row1 col3" >160 <span style="color: grey">(89.9%) </span></td>
    </tr>
    <tr>
      <th id="T_dc938_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_dc938_row2_col0" class="data row2 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_dc938_row2_col1" class="data row2 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_dc938_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_dc938_row2_col3" class="data row2 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_1e2d1 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_1e2d1  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_1e2d1_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_1e2d1_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_1e2d1_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_1e2d1_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_1e2d1_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.0%, transparent 97.0%);
  font-family: Courier;
}
#T_1e2d1_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 95.2%, transparent 95.2%);
  font-family: Courier;
}
#T_1e2d1_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_1e2d1_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.1%, transparent 96.1%);
  font-family: Courier;
}
#T_1e2d1_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_1e2d1_row2_col1, #T_1e2d1_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_1e2d1_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_1e2d1_row3_col0, #T_1e2d1_row3_col1, #T_1e2d1_row3_col2, #T_1e2d1_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_1e2d1">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_1e2d1_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_1e2d1_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_1e2d1_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_1e2d1_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.12] With observation</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_1e2d1_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_1e2d1_row0_col0" class="data row0 col0" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_1e2d1_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_1e2d1_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_1e2d1_row0_col3" class="data row0 col3" >6 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_1e2d1_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_1e2d1_row1_col0" class="data row1 col0" >129 <span style="color: grey">(72.5%) </span></td>
      <td id="T_1e2d1_row1_col1" class="data row1 col1" >40 <span style="color: grey">(22.5%) </span></td>
      <td id="T_1e2d1_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_1e2d1_row1_col3" class="data row1 col3" >171 <span style="color: grey">(96.1%) </span></td>
    </tr>
    <tr>
      <th id="T_1e2d1_level0_row2" class="row_heading level0 row2" >U</th>
      <td id="T_1e2d1_row2_col0" class="data row2 col0" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_1e2d1_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1e2d1_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1e2d1_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.6%) </span></td>
    </tr>
    <tr>
      <th id="T_1e2d1_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_1e2d1_row3_col0" class="data row3 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_1e2d1_row3_col1" class="data row3 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_1e2d1_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_1e2d1_row3_col3" class="data row3 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_76399 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_76399  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_76399_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_76399_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.9%, transparent 11.9%);
  font-family: Courier;
}
#T_76399_row0_col2 {
  width: 10em;
  font-family: Courier;
}
#T_76399_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.0%, transparent 9.0%);
  font-family: Courier;
}
#T_76399_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.7%, transparent 91.7%);
  font-family: Courier;
}
#T_76399_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 88.1%, transparent 88.1%);
  font-family: Courier;
}
#T_76399_row1_col2, #T_76399_row2_col0, #T_76399_row2_col1, #T_76399_row2_col2, #T_76399_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_76399_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.0%, transparent 91.0%);
  font-family: Courier;
}
</style>
<table id="T_76399">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_76399_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_76399_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_76399_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_76399_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.13] Stop</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_76399_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_76399_row0_col0" class="data row0 col0" >11 <span style="color: grey">(6.2%) </span></td>
      <td id="T_76399_row0_col1" class="data row0 col1" >5 <span style="color: grey">(2.8%) </span></td>
      <td id="T_76399_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_76399_row0_col3" class="data row0 col3" >16 <span style="color: grey">(9.0%) </span></td>
    </tr>
    <tr>
      <th id="T_76399_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_76399_row1_col0" class="data row1 col0" >122 <span style="color: grey">(68.5%) </span></td>
      <td id="T_76399_row1_col1" class="data row1 col1" >37 <span style="color: grey">(20.8%) </span></td>
      <td id="T_76399_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_76399_row1_col3" class="data row1 col3" >162 <span style="color: grey">(91.0%) </span></td>
    </tr>
    <tr>
      <th id="T_76399_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_76399_row2_col0" class="data row2 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_76399_row2_col1" class="data row2 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_76399_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_76399_row2_col3" class="data row2 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_00631 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_00631  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_00631_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.3%, transparent 44.3%);
  font-family: Courier;
}
#T_00631_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.5%, transparent 40.5%);
  font-family: Courier;
}
#T_00631_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_00631_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.2%, transparent 43.2%);
  font-family: Courier;
}
#T_00631_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 55.7%, transparent 55.7%);
  font-family: Courier;
}
#T_00631_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 59.5%, transparent 59.5%);
  font-family: Courier;
}
#T_00631_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_00631_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 56.8%, transparent 56.8%);
  font-family: Courier;
}
#T_00631_row2_col0, #T_00631_row2_col1, #T_00631_row2_col2, #T_00631_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_00631">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_00631_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_00631_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_00631_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_00631_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.13.01] Stop or Break</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_00631_level0_row0" class="row_heading level0 row0" >Break</th>
      <td id="T_00631_row0_col0" class="data row0 col0" >54 <span style="color: grey">(33.3%) </span></td>
      <td id="T_00631_row0_col1" class="data row0 col1" >15 <span style="color: grey">(9.3%) </span></td>
      <td id="T_00631_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_00631_row0_col3" class="data row0 col3" >70 <span style="color: grey">(43.2%) </span></td>
    </tr>
    <tr>
      <th id="T_00631_level0_row1" class="row_heading level0 row1" >Cessation</th>
      <td id="T_00631_row1_col0" class="data row1 col0" >68 <span style="color: grey">(42.0%) </span></td>
      <td id="T_00631_row1_col1" class="data row1 col1" >22 <span style="color: grey">(13.6%) </span></td>
      <td id="T_00631_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_00631_row1_col3" class="data row1 col3" >92 <span style="color: grey">(56.8%) </span></td>
    </tr>
    <tr>
      <th id="T_00631_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_00631_row2_col0" class="data row2 col0" >122 <span style="color: grey">(75.3%) </span></td>
      <td id="T_00631_row2_col1" class="data row2 col1" >37 <span style="color: grey">(22.8%) </span></td>
      <td id="T_00631_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.9%) </span></td>
      <td id="T_00631_row2_col3" class="data row2 col3" >162 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_43c01 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_43c01  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_43c01_row0_col0, #T_43c01_row0_col1, #T_43c01_row0_col2, #T_43c01_row0_col3, #T_43c01_row1_col0, #T_43c01_row1_col1, #T_43c01_row1_col2, #T_43c01_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_43c01">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_43c01_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_43c01_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_43c01_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_43c01_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.14] Adaptations</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_43c01_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_43c01_row0_col0" class="data row0 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_43c01_row0_col1" class="data row0 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_43c01_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_43c01_row0_col3" class="data row0 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_43c01_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_43c01_row1_col0" class="data row1 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_43c01_row1_col1" class="data row1 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_43c01_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_43c01_row1_col3" class="data row1 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_53d66 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_53d66  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_53d66_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.8%, transparent 5.8%);
  font-family: Courier;
}
#T_53d66_row0_col1, #T_53d66_row4_col1 {
  width: 10em;
  font-family: Courier;
}
#T_53d66_row0_col2, #T_53d66_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_53d66_row1_col0, #T_53d66_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_53d66_row1_col1, #T_53d66_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_53d66_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 51.9%, transparent 51.9%);
  font-family: Courier;
}
#T_53d66_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 60.0%, transparent 60.0%);
  font-family: Courier;
}
#T_53d66_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.6%, transparent 52.6%);
  font-family: Courier;
}
#T_53d66_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.6%, transparent 34.6%);
  font-family: Courier;
}
#T_53d66_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_53d66_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.5%, transparent 3.5%);
  font-family: Courier;
}
#T_53d66_row5_col0, #T_53d66_row5_col1, #T_53d66_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_53d66">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_53d66_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_53d66_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_53d66_level0_col2" class="col_heading level0 col2" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.14.01] Adaptations intensity</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_53d66_level0_row0" class="row_heading level0 row0" >Communication strategy</th>
      <td id="T_53d66_row0_col0" class="data row0 col0" >3 <span style="color: grey">(5.3%) </span></td>
      <td id="T_53d66_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_53d66_row0_col2" class="data row0 col2" >3 <span style="color: grey">(5.3%) </span></td>
    </tr>
    <tr>
      <th id="T_53d66_level0_row1" class="row_heading level0 row1" >Equipment</th>
      <td id="T_53d66_row1_col0" class="data row1 col0" >2 <span style="color: grey">(3.5%) </span></td>
      <td id="T_53d66_row1_col1" class="data row1 col1" >1 <span style="color: grey">(1.8%) </span></td>
      <td id="T_53d66_row1_col2" class="data row1 col2" >3 <span style="color: grey">(5.3%) </span></td>
    </tr>
    <tr>
      <th id="T_53d66_level0_row2" class="row_heading level0 row2" >Exercise selection</th>
      <td id="T_53d66_row2_col0" class="data row2 col0" >27 <span style="color: grey">(47.4%) </span></td>
      <td id="T_53d66_row2_col1" class="data row2 col1" >3 <span style="color: grey">(5.3%) </span></td>
      <td id="T_53d66_row2_col2" class="data row2 col2" >30 <span style="color: grey">(52.6%) </span></td>
    </tr>
    <tr>
      <th id="T_53d66_level0_row3" class="row_heading level0 row3" >Intensity</th>
      <td id="T_53d66_row3_col0" class="data row3 col0" >18 <span style="color: grey">(31.6%) </span></td>
      <td id="T_53d66_row3_col1" class="data row3 col1" >1 <span style="color: grey">(1.8%) </span></td>
      <td id="T_53d66_row3_col2" class="data row3 col2" >19 <span style="color: grey">(33.3%) </span></td>
    </tr>
    <tr>
      <th id="T_53d66_level0_row4" class="row_heading level0 row4" >Setting</th>
      <td id="T_53d66_row4_col0" class="data row4 col0" >2 <span style="color: grey">(3.5%) </span></td>
      <td id="T_53d66_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_53d66_row4_col2" class="data row4 col2" >2 <span style="color: grey">(3.5%) </span></td>
    </tr>
    <tr>
      <th id="T_53d66_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_53d66_row5_col0" class="data row5 col0" >52 <span style="color: grey">(91.2%) </span></td>
      <td id="T_53d66_row5_col1" class="data row5 col1" >5 <span style="color: grey">(8.8%) </span></td>
      <td id="T_53d66_row5_col2" class="data row5 col2" >57 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_324d3 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_324d3  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_324d3_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.1%, transparent 8.1%);
  font-family: Courier;
}
#T_324d3_row0_col1, #T_324d3_row1_col1 {
  width: 10em;
  font-family: Courier;
}
#T_324d3_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.3%, transparent 7.3%);
  font-family: Courier;
}
#T_324d3_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.6%, transparent 21.6%);
  font-family: Courier;
}
#T_324d3_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.5%, transparent 19.5%);
  font-family: Courier;
}
#T_324d3_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 70.3%, transparent 70.3%);
  font-family: Courier;
}
#T_324d3_row2_col1, #T_324d3_row3_col0, #T_324d3_row3_col1, #T_324d3_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_324d3_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 73.2%, transparent 73.2%);
  font-family: Courier;
}
</style>
<table id="T_324d3">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_324d3_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_324d3_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_324d3_level0_col2" class="col_heading level0 col2" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.14.02] Adaptations duration</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_324d3_level0_row0" class="row_heading level0 row0" >Ab jetzt für alle Bewegungseinheiten mit allen Patient*innen</th>
      <td id="T_324d3_row0_col0" class="data row0 col0" >3 <span style="color: grey">(7.3%) </span></td>
      <td id="T_324d3_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_324d3_row0_col2" class="data row0 col2" >3 <span style="color: grey">(7.3%) </span></td>
    </tr>
    <tr>
      <th id="T_324d3_level0_row1" class="row_heading level0 row1" >Für die gesamte Therapiephase</th>
      <td id="T_324d3_row1_col0" class="data row1 col0" >8 <span style="color: grey">(19.5%) </span></td>
      <td id="T_324d3_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_324d3_row1_col2" class="data row1 col2" >8 <span style="color: grey">(19.5%) </span></td>
    </tr>
    <tr>
      <th id="T_324d3_level0_row2" class="row_heading level0 row2" >Nur für diese Einheit</th>
      <td id="T_324d3_row2_col0" class="data row2 col0" >26 <span style="color: grey">(63.4%) </span></td>
      <td id="T_324d3_row2_col1" class="data row2 col1" >4 <span style="color: grey">(9.8%) </span></td>
      <td id="T_324d3_row2_col2" class="data row2 col2" >30 <span style="color: grey">(73.2%) </span></td>
    </tr>
    <tr>
      <th id="T_324d3_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_324d3_row3_col0" class="data row3 col0" >37 <span style="color: grey">(90.2%) </span></td>
      <td id="T_324d3_row3_col1" class="data row3 col1" >4 <span style="color: grey">(9.8%) </span></td>
      <td id="T_324d3_row3_col2" class="data row3 col2" >41 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_0e608 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0e608  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0e608_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.2%, transparent 90.2%);
  font-family: Courier;
}
#T_0e608_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 61.9%, transparent 61.9%);
  font-family: Courier;
}
#T_0e608_row0_col2, #T_0e608_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_0e608_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.6%, transparent 82.6%);
  font-family: Courier;
}
#T_0e608_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_0e608_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_0e608_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
#T_0e608_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_0e608_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_0e608_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_0e608_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_0e608_row3_col0, #T_0e608_row3_col1, #T_0e608_row3_col2, #T_0e608_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_0e608">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_0e608_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_0e608_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_0e608_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_0e608_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.01] Therapy phase</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_0e608_level0_row0" class="row_heading level0 row0" >Acute therapy</th>
      <td id="T_0e608_row0_col0" class="data row0 col0" >120 <span style="color: grey">(67.4%) </span></td>
      <td id="T_0e608_row0_col1" class="data row0 col1" >26 <span style="color: grey">(14.6%) </span></td>
      <td id="T_0e608_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_0e608_row0_col3" class="data row0 col3" >147 <span style="color: grey">(82.6%) </span></td>
    </tr>
    <tr>
      <th id="T_0e608_level0_row1" class="row_heading level0 row1" >Aftercare</th>
      <td id="T_0e608_row1_col0" class="data row1 col0" >9 <span style="color: grey">(5.1%) </span></td>
      <td id="T_0e608_row1_col1" class="data row1 col1" >14 <span style="color: grey">(7.9%) </span></td>
      <td id="T_0e608_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_0e608_row1_col3" class="data row1 col3" >25 <span style="color: grey">(14.0%) </span></td>
    </tr>
    <tr>
      <th id="T_0e608_level0_row2" class="row_heading level0 row2" >Long-term therapy</th>
      <td id="T_0e608_row2_col0" class="data row2 col0" >4 <span style="color: grey">(2.2%) </span></td>
      <td id="T_0e608_row2_col1" class="data row2 col1" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_0e608_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0e608_row2_col3" class="data row2 col3" >6 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_0e608_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_0e608_row3_col0" class="data row3 col0" >133 <span style="color: grey">(74.7%) </span></td>
      <td id="T_0e608_row3_col1" class="data row3 col1" >42 <span style="color: grey">(23.6%) </span></td>
      <td id="T_0e608_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_0e608_row3_col3" class="data row3 col3" >178 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_16ab4 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_16ab4  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_16ab4_row0_col0, #T_16ab4_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_16ab4_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_16ab4_row0_col2, #T_16ab4_row2_col0, #T_16ab4_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_16ab4_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_16ab4_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.5%, transparent 9.5%);
  font-family: Courier;
}
#T_16ab4_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_16ab4_row1_col3, #T_16ab4_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_16ab4_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_16ab4_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.4%, transparent 98.4%);
  font-family: Courier;
}
#T_16ab4_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 73.8%, transparent 73.8%);
  font-family: Courier;
}
#T_16ab4_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_16ab4_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 92.0%, transparent 92.0%);
  font-family: Courier;
}
#T_16ab4_row4_col0, #T_16ab4_row4_col1, #T_16ab4_row4_col2, #T_16ab4_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_16ab4">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_16ab4_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_16ab4_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_16ab4_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_16ab4_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.02] Group size</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_16ab4_level0_row0" class="row_heading level0 row0" >Group 2-5</th>
      <td id="T_16ab4_row0_col0" class="data row0 col0" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_16ab4_row0_col1" class="data row0 col1" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_16ab4_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_16ab4_row0_col3" class="data row0 col3" >2 <span style="color: grey">(1.1%) </span></td>
    </tr>
    <tr>
      <th id="T_16ab4_level0_row1" class="row_heading level0 row1" >Group 5 to 10</th>
      <td id="T_16ab4_row1_col0" class="data row1 col0" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_16ab4_row1_col1" class="data row1 col1" >4 <span style="color: grey">(2.3%) </span></td>
      <td id="T_16ab4_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_16ab4_row1_col3" class="data row1 col3" >6 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_16ab4_level0_row2" class="row_heading level0 row2" >Group over 10</th>
      <td id="T_16ab4_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_16ab4_row2_col1" class="data row2 col1" >6 <span style="color: grey">(3.4%) </span></td>
      <td id="T_16ab4_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_16ab4_row2_col3" class="data row2 col3" >6 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_16ab4_level0_row3" class="row_heading level0 row3" >Individual</th>
      <td id="T_16ab4_row3_col0" class="data row3 col0" >127 <span style="color: grey">(73.0%) </span></td>
      <td id="T_16ab4_row3_col1" class="data row3 col1" >31 <span style="color: grey">(17.8%) </span></td>
      <td id="T_16ab4_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_16ab4_row3_col3" class="data row3 col3" >160 <span style="color: grey">(92.0%) </span></td>
    </tr>
    <tr>
      <th id="T_16ab4_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_16ab4_row4_col0" class="data row4 col0" >129 <span style="color: grey">(74.1%) </span></td>
      <td id="T_16ab4_row4_col1" class="data row4 col1" >42 <span style="color: grey">(24.1%) </span></td>
      <td id="T_16ab4_row4_col2" class="data row4 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_16ab4_row4_col3" class="data row4 col3" >174 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_ecc4d th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ecc4d  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ecc4d_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.4%, transparent 13.4%);
  font-family: Courier;
}
#T_ecc4d_row0_col1, #T_ecc4d_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.3%, transparent 27.3%);
  font-family: Courier;
}
#T_ecc4d_row0_col2, #T_ecc4d_row1_col2, #T_ecc4d_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_ecc4d_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.5%, transparent 16.5%);
  font-family: Courier;
}
#T_ecc4d_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.1%, transparent 35.1%);
  font-family: Courier;
}
#T_ecc4d_row1_col1, #T_ecc4d_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.2%, transparent 18.2%);
  font-family: Courier;
}
#T_ecc4d_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.1%, transparent 30.1%);
  font-family: Courier;
}
#T_ecc4d_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.9%, transparent 30.9%);
  font-family: Courier;
}
#T_ecc4d_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.3%, transparent 29.3%);
  font-family: Courier;
}
#T_ecc4d_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.5%, transparent 17.5%);
  font-family: Courier;
}
#T_ecc4d_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_ecc4d_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.0%, transparent 18.0%);
  font-family: Courier;
}
#T_ecc4d_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_ecc4d_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.1%, transparent 9.1%);
  font-family: Courier;
}
#T_ecc4d_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_ecc4d_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.0%, transparent 6.0%);
  font-family: Courier;
}
#T_ecc4d_row5_col0, #T_ecc4d_row5_col1, #T_ecc4d_row5_col2, #T_ecc4d_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_ecc4d">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_ecc4d_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_ecc4d_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_ecc4d_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_ecc4d_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ecc4d_level0_row0" class="row_heading level0 row0" >02 to 05 years</th>
      <td id="T_ecc4d_row0_col0" class="data row0 col0" >13 <span style="color: grey">(9.8%) </span></td>
      <td id="T_ecc4d_row0_col1" class="data row0 col1" >9 <span style="color: grey">(6.8%) </span></td>
      <td id="T_ecc4d_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ecc4d_row0_col3" class="data row0 col3" >22 <span style="color: grey">(16.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ecc4d_level0_row1" class="row_heading level0 row1" >06 to 09 years</th>
      <td id="T_ecc4d_row1_col0" class="data row1 col0" >34 <span style="color: grey">(25.6%) </span></td>
      <td id="T_ecc4d_row1_col1" class="data row1 col1" >6 <span style="color: grey">(4.5%) </span></td>
      <td id="T_ecc4d_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ecc4d_row1_col3" class="data row1 col3" >40 <span style="color: grey">(30.1%) </span></td>
    </tr>
    <tr>
      <th id="T_ecc4d_level0_row2" class="row_heading level0 row2" >10 to 14 years</th>
      <td id="T_ecc4d_row2_col0" class="data row2 col0" >30 <span style="color: grey">(22.6%) </span></td>
      <td id="T_ecc4d_row2_col1" class="data row2 col1" >9 <span style="color: grey">(6.8%) </span></td>
      <td id="T_ecc4d_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ecc4d_row2_col3" class="data row2 col3" >39 <span style="color: grey">(29.3%) </span></td>
    </tr>
    <tr>
      <th id="T_ecc4d_level0_row3" class="row_heading level0 row3" >15 to 18 years</th>
      <td id="T_ecc4d_row3_col0" class="data row3 col0" >17 <span style="color: grey">(12.8%) </span></td>
      <td id="T_ecc4d_row3_col1" class="data row3 col1" >6 <span style="color: grey">(4.5%) </span></td>
      <td id="T_ecc4d_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_ecc4d_row3_col3" class="data row3 col3" >24 <span style="color: grey">(18.0%) </span></td>
    </tr>
    <tr>
      <th id="T_ecc4d_level0_row4" class="row_heading level0 row4" >18+ years</th>
      <td id="T_ecc4d_row4_col0" class="data row4 col0" >3 <span style="color: grey">(2.3%) </span></td>
      <td id="T_ecc4d_row4_col1" class="data row4 col1" >3 <span style="color: grey">(2.3%) </span></td>
      <td id="T_ecc4d_row4_col2" class="data row4 col2" >2 <span style="color: grey">(1.5%) </span></td>
      <td id="T_ecc4d_row4_col3" class="data row4 col3" >8 <span style="color: grey">(6.0%) </span></td>
    </tr>
    <tr>
      <th id="T_ecc4d_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_ecc4d_row5_col0" class="data row5 col0" >97 <span style="color: grey">(72.9%) </span></td>
      <td id="T_ecc4d_row5_col1" class="data row5 col1" >33 <span style="color: grey">(24.8%) </span></td>
      <td id="T_ecc4d_row5_col2" class="data row5 col2" >3 <span style="color: grey">(2.3%) </span></td>
      <td id="T_ecc4d_row5_col3" class="data row5 col3" >133 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_6f2e3 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_6f2e3  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_6f2e3_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_6f2e3_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 95.2%, transparent 95.2%);
  font-family: Courier;
}
#T_6f2e3_row0_col2, #T_6f2e3_row2_col0, #T_6f2e3_row2_col1, #T_6f2e3_row2_col2, #T_6f2e3_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_6f2e3_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.0%, transparent 96.0%);
  font-family: Courier;
}
#T_6f2e3_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_6f2e3_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_6f2e3_row1_col2 {
  width: 10em;
  font-family: Courier;
}
#T_6f2e3_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
</style>
<table id="T_6f2e3">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_6f2e3_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_6f2e3_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_6f2e3_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_6f2e3_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.04] Online</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_6f2e3_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_6f2e3_row0_col0" class="data row0 col0" >127 <span style="color: grey">(71.8%) </span></td>
      <td id="T_6f2e3_row0_col1" class="data row0 col1" >40 <span style="color: grey">(22.6%) </span></td>
      <td id="T_6f2e3_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_6f2e3_row0_col3" class="data row0 col3" >170 <span style="color: grey">(96.0%) </span></td>
    </tr>
    <tr>
      <th id="T_6f2e3_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_6f2e3_row1_col0" class="data row1 col0" >5 <span style="color: grey">(2.8%) </span></td>
      <td id="T_6f2e3_row1_col1" class="data row1 col1" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_6f2e3_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_6f2e3_row1_col3" class="data row1 col3" >7 <span style="color: grey">(4.0%) </span></td>
    </tr>
    <tr>
      <th id="T_6f2e3_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_6f2e3_row2_col0" class="data row2 col0" >132 <span style="color: grey">(74.6%) </span></td>
      <td id="T_6f2e3_row2_col1" class="data row2 col1" >42 <span style="color: grey">(23.7%) </span></td>
      <td id="T_6f2e3_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_6f2e3_row2_col3" class="data row2 col3" >177 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e2eb0 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2eb0  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2eb0_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.0%, transparent 97.0%);
  font-family: Courier;
}
#T_e2eb0_row0_col1, #T_e2eb0_row0_col2, #T_e2eb0_row2_col0, #T_e2eb0_row2_col1, #T_e2eb0_row2_col2, #T_e2eb0_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e2eb0_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.7%, transparent 97.7%);
  font-family: Courier;
}
#T_e2eb0_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_e2eb0_row1_col1, #T_e2eb0_row1_col2 {
  width: 10em;
  font-family: Courier;
}
#T_e2eb0_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
</style>
<table id="T_e2eb0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e2eb0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e2eb0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e2eb0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e2eb0_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.05] As part of testing</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e2eb0_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_e2eb0_row0_col0" class="data row0 col0" >129 <span style="color: grey">(72.9%) </span></td>
      <td id="T_e2eb0_row0_col1" class="data row0 col1" >41 <span style="color: grey">(23.2%) </span></td>
      <td id="T_e2eb0_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_e2eb0_row0_col3" class="data row0 col3" >173 <span style="color: grey">(97.7%) </span></td>
    </tr>
    <tr>
      <th id="T_e2eb0_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_e2eb0_row1_col0" class="data row1 col0" >4 <span style="color: grey">(2.3%) </span></td>
      <td id="T_e2eb0_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e2eb0_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e2eb0_row1_col3" class="data row1 col3" >4 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_e2eb0_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_e2eb0_row2_col0" class="data row2 col0" >133 <span style="color: grey">(75.1%) </span></td>
      <td id="T_e2eb0_row2_col1" class="data row2 col1" >41 <span style="color: grey">(23.2%) </span></td>
      <td id="T_e2eb0_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_e2eb0_row2_col3" class="data row2 col3" >177 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_96e77 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_96e77  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_96e77_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.2%, transparent 4.2%);
  font-family: Courier;
}
#T_96e77_row0_col1, #T_96e77_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.0%, transparent 5.0%);
  font-family: Courier;
}
#T_96e77_row0_col2, #T_96e77_row2_col2, #T_96e77_row4_col2 {
  width: 10em;
  font-family: Courier;
}
#T_96e77_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_96e77_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.5%, transparent 34.5%);
  font-family: Courier;
}
#T_96e77_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.5%, transparent 47.5%);
  font-family: Courier;
}
#T_96e77_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_96e77_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.3%, transparent 38.3%);
  font-family: Courier;
}
#T_96e77_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.6%, transparent 28.6%);
  font-family: Courier;
}
#T_96e77_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.5%, transparent 17.5%);
  font-family: Courier;
}
#T_96e77_row2_col3, #T_96e77_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.3%, transparent 25.3%);
  font-family: Courier;
}
#T_96e77_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_96e77_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_96e77_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_96e77_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.7%, transparent 27.7%);
  font-family: Courier;
}
#T_96e77_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_96e77_row5_col0, #T_96e77_row5_col1, #T_96e77_row5_col2, #T_96e77_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_96e77">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_96e77_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_96e77_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_96e77_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_96e77_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.06] Setting</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_96e77_level0_row0" class="row_heading level0 row0" >At home (via telemedicine)</th>
      <td id="T_96e77_row0_col0" class="data row0 col0" >5 <span style="color: grey">(3.1%) </span></td>
      <td id="T_96e77_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_96e77_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_96e77_row0_col3" class="data row0 col3" >7 <span style="color: grey">(4.3%) </span></td>
    </tr>
    <tr>
      <th id="T_96e77_level0_row1" class="row_heading level0 row1" >Gym</th>
      <td id="T_96e77_row1_col0" class="data row1 col0" >41 <span style="color: grey">(25.3%) </span></td>
      <td id="T_96e77_row1_col1" class="data row1 col1" >19 <span style="color: grey">(11.7%) </span></td>
      <td id="T_96e77_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_96e77_row1_col3" class="data row1 col3" >62 <span style="color: grey">(38.3%) </span></td>
    </tr>
    <tr>
      <th id="T_96e77_level0_row2" class="row_heading level0 row2" >Hospital corridor</th>
      <td id="T_96e77_row2_col0" class="data row2 col0" >34 <span style="color: grey">(21.0%) </span></td>
      <td id="T_96e77_row2_col1" class="data row2 col1" >7 <span style="color: grey">(4.3%) </span></td>
      <td id="T_96e77_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_96e77_row2_col3" class="data row2 col3" >41 <span style="color: grey">(25.3%) </span></td>
    </tr>
    <tr>
      <th id="T_96e77_level0_row3" class="row_heading level0 row3" >Outside</th>
      <td id="T_96e77_row3_col0" class="data row3 col0" >6 <span style="color: grey">(3.7%) </span></td>
      <td id="T_96e77_row3_col1" class="data row3 col1" >4 <span style="color: grey">(2.5%) </span></td>
      <td id="T_96e77_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_96e77_row3_col3" class="data row3 col3" >11 <span style="color: grey">(6.8%) </span></td>
    </tr>
    <tr>
      <th id="T_96e77_level0_row4" class="row_heading level0 row4" >Patients room</th>
      <td id="T_96e77_row4_col0" class="data row4 col0" >33 <span style="color: grey">(20.4%) </span></td>
      <td id="T_96e77_row4_col1" class="data row4 col1" >8 <span style="color: grey">(4.9%) </span></td>
      <td id="T_96e77_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_96e77_row4_col3" class="data row4 col3" >41 <span style="color: grey">(25.3%) </span></td>
    </tr>
    <tr>
      <th id="T_96e77_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_96e77_row5_col0" class="data row5 col0" >119 <span style="color: grey">(73.5%) </span></td>
      <td id="T_96e77_row5_col1" class="data row5 col1" >40 <span style="color: grey">(24.7%) </span></td>
      <td id="T_96e77_row5_col2" class="data row5 col2" >3 <span style="color: grey">(1.9%) </span></td>
      <td id="T_96e77_row5_col3" class="data row5 col3" >162 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_8b036 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8b036  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8b036_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.7%, transparent 34.7%);
  font-family: Courier;
}
#T_8b036_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.5%, transparent 34.5%);
  font-family: Courier;
}
#T_8b036_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.0%, transparent 75.0%);
  font-family: Courier;
}
#T_8b036_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.4%, transparent 35.4%);
  font-family: Courier;
}
#T_8b036_row1_col0, #T_8b036_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.8%, transparent 21.8%);
  font-family: Courier;
}
#T_8b036_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_8b036_row1_col2, #T_8b036_row2_col2, #T_8b036_row3_col2, #T_8b036_row4_col1, #T_8b036_row4_col2, #T_8b036_row5_col2 {
  width: 10em;
  font-family: Courier;
}
#T_8b036_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.0%, transparent 21.0%);
  font-family: Courier;
}
#T_8b036_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.4%, transparent 12.4%);
  font-family: Courier;
}
#T_8b036_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_8b036_row2_col3, #T_8b036_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.5%, transparent 10.5%);
  font-family: Courier;
}
#T_8b036_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.2%, transparent 11.2%);
  font-family: Courier;
}
#T_8b036_row3_col1, #T_8b036_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.1%, transparent 9.1%);
  font-family: Courier;
}
#T_8b036_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_8b036_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_8b036_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_8b036_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_8b036_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.9%, transparent 15.9%);
  font-family: Courier;
}
#T_8b036_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_8b036_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.5%, transparent 17.5%);
  font-family: Courier;
}
#T_8b036_row7_col0, #T_8b036_row7_col1, #T_8b036_row7_col2, #T_8b036_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_8b036">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_8b036_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_8b036_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_8b036_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_8b036_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.07] Main motor skill</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_8b036_level0_row0" class="row_heading level0 row0" >Coordination</th>
      <td id="T_8b036_row0_col0" class="data row0 col0" >59 <span style="color: grey">(25.8%) </span></td>
      <td id="T_8b036_row0_col1" class="data row0 col1" >19 <span style="color: grey">(8.3%) </span></td>
      <td id="T_8b036_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_8b036_row0_col3" class="data row0 col3" >81 <span style="color: grey">(35.4%) </span></td>
    </tr>
    <tr>
      <th id="T_8b036_level0_row1" class="row_heading level0 row1" >Endurance</th>
      <td id="T_8b036_row1_col0" class="data row1 col0" >37 <span style="color: grey">(16.2%) </span></td>
      <td id="T_8b036_row1_col1" class="data row1 col1" >11 <span style="color: grey">(4.8%) </span></td>
      <td id="T_8b036_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8b036_row1_col3" class="data row1 col3" >48 <span style="color: grey">(21.0%) </span></td>
    </tr>
    <tr>
      <th id="T_8b036_level0_row2" class="row_heading level0 row2" >Flexibility</th>
      <td id="T_8b036_row2_col0" class="data row2 col0" >21 <span style="color: grey">(9.2%) </span></td>
      <td id="T_8b036_row2_col1" class="data row2 col1" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_8b036_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8b036_row2_col3" class="data row2 col3" >24 <span style="color: grey">(10.5%) </span></td>
    </tr>
    <tr>
      <th id="T_8b036_level0_row3" class="row_heading level0 row3" >Full body</th>
      <td id="T_8b036_row3_col0" class="data row3 col0" >19 <span style="color: grey">(8.3%) </span></td>
      <td id="T_8b036_row3_col1" class="data row3 col1" >5 <span style="color: grey">(2.2%) </span></td>
      <td id="T_8b036_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8b036_row3_col3" class="data row3 col3" >24 <span style="color: grey">(10.5%) </span></td>
    </tr>
    <tr>
      <th id="T_8b036_level0_row4" class="row_heading level0 row4" >Relaxation</th>
      <td id="T_8b036_row4_col0" class="data row4 col0" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_8b036_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_8b036_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8b036_row4_col3" class="data row4 col3" >2 <span style="color: grey">(0.9%) </span></td>
    </tr>
    <tr>
      <th id="T_8b036_level0_row5" class="row_heading level0 row5" >Speed</th>
      <td id="T_8b036_row5_col0" class="data row5 col0" >5 <span style="color: grey">(2.2%) </span></td>
      <td id="T_8b036_row5_col1" class="data row5 col1" >5 <span style="color: grey">(2.2%) </span></td>
      <td id="T_8b036_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8b036_row5_col3" class="data row5 col3" >10 <span style="color: grey">(4.4%) </span></td>
    </tr>
    <tr>
      <th id="T_8b036_level0_row6" class="row_heading level0 row6" >Strength</th>
      <td id="T_8b036_row6_col0" class="data row6 col0" >27 <span style="color: grey">(11.8%) </span></td>
      <td id="T_8b036_row6_col1" class="data row6 col1" >12 <span style="color: grey">(5.2%) </span></td>
      <td id="T_8b036_row6_col2" class="data row6 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_8b036_row6_col3" class="data row6 col3" >40 <span style="color: grey">(17.5%) </span></td>
    </tr>
    <tr>
      <th id="T_8b036_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_8b036_row7_col0" class="data row7 col0" >170 <span style="color: grey">(74.2%) </span></td>
      <td id="T_8b036_row7_col1" class="data row7 col1" >55 <span style="color: grey">(24.0%) </span></td>
      <td id="T_8b036_row7_col2" class="data row7 col2" >4 <span style="color: grey">(1.7%) </span></td>
      <td id="T_8b036_row7_col3" class="data row7 col3" >229 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_20fa6 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_20fa6  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_20fa6_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.1%, transparent 52.1%);
  font-family: Courier;
}
#T_20fa6_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.8%, transparent 18.8%);
  font-family: Courier;
}
#T_20fa6_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_20fa6_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.3%, transparent 44.3%);
  font-family: Courier;
}
#T_20fa6_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.9%, transparent 47.9%);
  font-family: Courier;
}
#T_20fa6_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.2%, transparent 81.2%);
  font-family: Courier;
}
#T_20fa6_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_20fa6_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 55.7%, transparent 55.7%);
  font-family: Courier;
}
#T_20fa6_row2_col0, #T_20fa6_row2_col1, #T_20fa6_row2_col2, #T_20fa6_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_20fa6">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_20fa6_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_20fa6_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_20fa6_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_20fa6_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.08] Time point</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_20fa6_level0_row0" class="row_heading level0 row0" >1. Time point</th>
      <td id="T_20fa6_row0_col0" class="data row0 col0" >50 <span style="color: grey">(38.2%) </span></td>
      <td id="T_20fa6_row0_col1" class="data row0 col1" >6 <span style="color: grey">(4.6%) </span></td>
      <td id="T_20fa6_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.5%) </span></td>
      <td id="T_20fa6_row0_col3" class="data row0 col3" >58 <span style="color: grey">(44.3%) </span></td>
    </tr>
    <tr>
      <th id="T_20fa6_level0_row1" class="row_heading level0 row1" >2. Time point</th>
      <td id="T_20fa6_row1_col0" class="data row1 col0" >46 <span style="color: grey">(35.1%) </span></td>
      <td id="T_20fa6_row1_col1" class="data row1 col1" >26 <span style="color: grey">(19.8%) </span></td>
      <td id="T_20fa6_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_20fa6_row1_col3" class="data row1 col3" >73 <span style="color: grey">(55.7%) </span></td>
    </tr>
    <tr>
      <th id="T_20fa6_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_20fa6_row2_col0" class="data row2 col0" >96 <span style="color: grey">(73.3%) </span></td>
      <td id="T_20fa6_row2_col1" class="data row2 col1" >32 <span style="color: grey">(24.4%) </span></td>
      <td id="T_20fa6_row2_col2" class="data row2 col2" >3 <span style="color: grey">(2.3%) </span></td>
      <td id="T_20fa6_row2_col3" class="data row2 col3" >131 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_36041 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_36041  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_36041_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.3%, transparent 28.3%);
  font-family: Courier;
}
#T_36041_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.5%, transparent 34.5%);
  font-family: Courier;
}
#T_36041_row0_col2, #T_36041_row1_col2, #T_36041_row3_col1, #T_36041_row3_col2 {
  width: 10em;
  font-family: Courier;
}
#T_36041_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.0%, transparent 29.0%);
  font-family: Courier;
}
#T_36041_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.9%, transparent 10.9%);
  font-family: Courier;
}
#T_36041_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.9%, transparent 6.9%);
  font-family: Courier;
}
#T_36041_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.7%, transparent 9.7%);
  font-family: Courier;
}
#T_36041_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.6%, transparent 57.6%);
  font-family: Courier;
}
#T_36041_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.6%, transparent 58.6%);
  font-family: Courier;
}
#T_36041_row2_col2, #T_36041_row4_col0, #T_36041_row4_col1, #T_36041_row4_col2, #T_36041_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_36041_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.9%, transparent 58.9%);
  font-family: Courier;
}
#T_36041_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_36041_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
</style>
<table id="T_36041">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_36041_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_36041_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_36041_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_36041_level0_col3" class="col_heading level0 col3" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.09] Training condition</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_36041_level0_row0" class="row_heading level0 row0" >Average</th>
      <td id="T_36041_row0_col0" class="data row0 col0" >26 <span style="color: grey">(21.0%) </span></td>
      <td id="T_36041_row0_col1" class="data row0 col1" >10 <span style="color: grey">(8.1%) </span></td>
      <td id="T_36041_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_36041_row0_col3" class="data row0 col3" >36 <span style="color: grey">(29.0%) </span></td>
    </tr>
    <tr>
      <th id="T_36041_level0_row1" class="row_heading level0 row1" >Good</th>
      <td id="T_36041_row1_col0" class="data row1 col0" >10 <span style="color: grey">(8.1%) </span></td>
      <td id="T_36041_row1_col1" class="data row1 col1" >2 <span style="color: grey">(1.6%) </span></td>
      <td id="T_36041_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_36041_row1_col3" class="data row1 col3" >12 <span style="color: grey">(9.7%) </span></td>
    </tr>
    <tr>
      <th id="T_36041_level0_row2" class="row_heading level0 row2" >Moderate</th>
      <td id="T_36041_row2_col0" class="data row2 col0" >53 <span style="color: grey">(42.7%) </span></td>
      <td id="T_36041_row2_col1" class="data row2 col1" >17 <span style="color: grey">(13.7%) </span></td>
      <td id="T_36041_row2_col2" class="data row2 col2" >3 <span style="color: grey">(2.4%) </span></td>
      <td id="T_36041_row2_col3" class="data row2 col3" >73 <span style="color: grey">(58.9%) </span></td>
    </tr>
    <tr>
      <th id="T_36041_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_36041_row3_col0" class="data row3 col0" >3 <span style="color: grey">(2.4%) </span></td>
      <td id="T_36041_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_36041_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_36041_row3_col3" class="data row3 col3" >3 <span style="color: grey">(2.4%) </span></td>
    </tr>
    <tr>
      <th id="T_36041_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_36041_row4_col0" class="data row4 col0" >92 <span style="color: grey">(74.2%) </span></td>
      <td id="T_36041_row4_col1" class="data row4 col1" >29 <span style="color: grey">(23.4%) </span></td>
      <td id="T_36041_row4_col2" class="data row4 col2" >3 <span style="color: grey">(2.4%) </span></td>
      <td id="T_36041_row4_col3" class="data row4 col3" >124 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



## <a id='toc1_3_'></a>[pie charts](#toc0_)


    
![png](3_description_files/output_13_0.png)
    



    
![png](3_description_files/output_13_1.png)
    



    
![png](3_description_files/output_13_2.png)
    



    
![png](3_description_files/output_13_3.png)
    



    
![png](3_description_files/output_13_4.png)
    



    
![png](3_description_files/output_13_5.png)
    



    
![png](3_description_files/output_13_6.png)
    



    
![png](3_description_files/output_13_7.png)
    



    
![png](3_description_files/output_13_8.png)
    

