# descriptive analysis

    🐍 3.12.9 | 📦 pygwalker: 0.4.9.15 | 📦 pandas: 2.3.1 | 📦 numpy: 1.26.4 | 📦 duckdb: 1.3.2 | 📦 pandas-plots: 0.15.13 | 📦 connection-helper: 0.12.1


## import data

## tables

    ['[01.01] CTCAE', '[01.02] Date', '[01.03] Exercise-related', '[02.02] Type', '[02.03] Trigger']



<style type="text/css">
#T_d2cd1 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d2cd1  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d2cd1_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.8%, transparent 22.8%);
  font-family: Courier;
}
#T_d2cd1_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_d2cd1_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_d2cd1_row0_col3 {
  width: 10em;
  font-family: Courier;
}
#T_d2cd1_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.2%, transparent 21.2%);
  font-family: Courier;
}
#T_d2cd1_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 77.2%, transparent 77.2%);
  font-family: Courier;
}
#T_d2cd1_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 84.6%, transparent 84.6%);
  font-family: Courier;
}
#T_d2cd1_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_d2cd1_row1_col3, #T_d2cd1_row2_col0, #T_d2cd1_row2_col1, #T_d2cd1_row2_col2, #T_d2cd1_row2_col3, #T_d2cd1_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_d2cd1_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 78.8%, transparent 78.8%);
  font-family: Courier;
}
</style>
<table id="T_d2cd1">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_d2cd1_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_d2cd1_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_d2cd1_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_d2cd1_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_d2cd1_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.02] Date</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d2cd1_level0_row0" class="row_heading level0 row0" >Already present</th>
      <td id="T_d2cd1_row0_col0" class="data row0 col0" >42 <span style="color: grey">(17.5%) </span></td>
      <td id="T_d2cd1_row0_col1" class="data row0 col1" >8 <span style="color: grey">(3.3%) </span></td>
      <td id="T_d2cd1_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_d2cd1_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_d2cd1_row0_col4" class="data row0 col4" >51 <span style="color: grey">(21.2%) </span></td>
    </tr>
    <tr>
      <th id="T_d2cd1_level0_row1" class="row_heading level0 row1" >First occurrence</th>
      <td id="T_d2cd1_row1_col0" class="data row1 col0" >142 <span style="color: grey">(59.2%) </span></td>
      <td id="T_d2cd1_row1_col1" class="data row1 col1" >44 <span style="color: grey">(18.3%) </span></td>
      <td id="T_d2cd1_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_d2cd1_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_d2cd1_row1_col4" class="data row1 col4" >189 <span style="color: grey">(78.8%) </span></td>
    </tr>
    <tr>
      <th id="T_d2cd1_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_d2cd1_row2_col0" class="data row2 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_d2cd1_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_d2cd1_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_d2cd1_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_d2cd1_row2_col4" class="data row2 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_ce76c th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ce76c  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ce76c_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_ce76c_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.5%, transparent 13.5%);
  font-family: Courier;
}
#T_ce76c_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_ce76c_row0_col3 {
  width: 10em;
  font-family: Courier;
}
#T_ce76c_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.6%, transparent 12.6%);
  font-family: Courier;
}
#T_ce76c_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 88.0%, transparent 88.0%);
  font-family: Courier;
}
#T_ce76c_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.5%, transparent 86.5%);
  font-family: Courier;
}
#T_ce76c_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_ce76c_row1_col3, #T_ce76c_row2_col0, #T_ce76c_row2_col1, #T_ce76c_row2_col2, #T_ce76c_row2_col3, #T_ce76c_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_ce76c_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 87.4%, transparent 87.4%);
  font-family: Courier;
}
</style>
<table id="T_ce76c">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_ce76c_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_ce76c_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_ce76c_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_ce76c_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_ce76c_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.03] Exercise-related</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ce76c_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_ce76c_row0_col0" class="data row0 col0" >22 <span style="color: grey">(9.2%) </span></td>
      <td id="T_ce76c_row0_col1" class="data row0 col1" >7 <span style="color: grey">(2.9%) </span></td>
      <td id="T_ce76c_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ce76c_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ce76c_row0_col4" class="data row0 col4" >30 <span style="color: grey">(12.6%) </span></td>
    </tr>
    <tr>
      <th id="T_ce76c_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_ce76c_row1_col0" class="data row1 col0" >161 <span style="color: grey">(67.4%) </span></td>
      <td id="T_ce76c_row1_col1" class="data row1 col1" >45 <span style="color: grey">(18.8%) </span></td>
      <td id="T_ce76c_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_ce76c_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ce76c_row1_col4" class="data row1 col4" >209 <span style="color: grey">(87.4%) </span></td>
    </tr>
    <tr>
      <th id="T_ce76c_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_ce76c_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_ce76c_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_ce76c_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_ce76c_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ce76c_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_cf7a0 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cf7a0  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cf7a0_row0_col0, #T_cf7a0_row0_col1, #T_cf7a0_row0_col3, #T_cf7a0_row1_col2, #T_cf7a0_row1_col3, #T_cf7a0_row2_col1, #T_cf7a0_row2_col2, #T_cf7a0_row2_col3, #T_cf7a0_row3_col1, #T_cf7a0_row3_col2, #T_cf7a0_row3_col3, #T_cf7a0_row4_col2, #T_cf7a0_row4_col3, #T_cf7a0_row5_col1, #T_cf7a0_row5_col2, #T_cf7a0_row5_col3, #T_cf7a0_row6_col2, #T_cf7a0_row6_col3, #T_cf7a0_row7_col2, #T_cf7a0_row7_col3, #T_cf7a0_row9_col2, #T_cf7a0_row9_col3, #T_cf7a0_row10_col1, #T_cf7a0_row10_col2, #T_cf7a0_row10_col3, #T_cf7a0_row11_col1, #T_cf7a0_row11_col2, #T_cf7a0_row11_col3, #T_cf7a0_row12_col2, #T_cf7a0_row12_col3, #T_cf7a0_row13_col2, #T_cf7a0_row14_col2, #T_cf7a0_row14_col3 {
  width: 10em;
  font-family: Courier;
}
#T_cf7a0_row0_col2, #T_cf7a0_row8_col2, #T_cf7a0_row8_col3, #T_cf7a0_row13_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_cf7a0_row0_col4, #T_cf7a0_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_cf7a0_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.4%, transparent 16.4%);
  font-family: Courier;
}
#T_cf7a0_row1_col1, #T_cf7a0_row6_col1, #T_cf7a0_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_cf7a0_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_cf7a0_row2_col0, #T_cf7a0_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_cf7a0_row2_col4, #T_cf7a0_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_cf7a0_row3_col0, #T_cf7a0_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_cf7a0_row4_col0, #T_cf7a0_row10_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_cf7a0_row4_col1, #T_cf7a0_row5_col0, #T_cf7a0_row7_col1, #T_cf7a0_row9_col1, #T_cf7a0_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_cf7a0_row5_col4, #T_cf7a0_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_cf7a0_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_cf7a0_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.1%, transparent 39.1%);
  font-family: Courier;
}
#T_cf7a0_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.7%, transparent 50.7%);
  font-family: Courier;
}
#T_cf7a0_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.2%, transparent 42.2%);
  font-family: Courier;
}
#T_cf7a0_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_cf7a0_row9_col4, #T_cf7a0_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_cf7a0_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_cf7a0_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_cf7a0_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_cf7a0_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_cf7a0_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.7%, transparent 22.7%);
  font-family: Courier;
}
#T_cf7a0_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.2%, transparent 8.2%);
  font-family: Courier;
}
#T_cf7a0_row14_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.6%, transparent 19.6%);
  font-family: Courier;
}
#T_cf7a0_row14_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_cf7a0_row14_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
#T_cf7a0_row15_col0, #T_cf7a0_row15_col1, #T_cf7a0_row15_col2, #T_cf7a0_row15_col3, #T_cf7a0_row15_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_cf7a0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_cf7a0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_cf7a0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_cf7a0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_cf7a0_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_cf7a0_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_cf7a0_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_cf7a0_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_cf7a0_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row0_col4" class="data row0 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_cf7a0_row1_col0" class="data row1 col0" >37 <span style="color: grey">(12.1%) </span></td>
      <td id="T_cf7a0_row1_col1" class="data row1 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_cf7a0_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row1_col4" class="data row1 col4" >39 <span style="color: grey">(12.7%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_cf7a0_row2_col0" class="data row2 col0" >5 <span style="color: grey">(1.6%) </span></td>
      <td id="T_cf7a0_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row2_col4" class="data row2 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_cf7a0_row3_col0" class="data row3 col0" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_cf7a0_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row3_col4" class="data row3 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_cf7a0_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cf7a0_row4_col1" class="data row4 col1" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_cf7a0_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row4_col4" class="data row4 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_cf7a0_row5_col0" class="data row5 col0" >3 <span style="color: grey">(1.0%) </span></td>
      <td id="T_cf7a0_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row5_col4" class="data row5 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_cf7a0_row6_col0" class="data row6 col0" >5 <span style="color: grey">(1.6%) </span></td>
      <td id="T_cf7a0_row6_col1" class="data row6 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_cf7a0_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row6_col4" class="data row6 col4" >7 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_cf7a0_row7_col0" class="data row7 col0" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_cf7a0_row7_col1" class="data row7 col1" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_cf7a0_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row7_col4" class="data row7 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_cf7a0_row8_col0" class="data row8 col0" >88 <span style="color: grey">(28.8%) </span></td>
      <td id="T_cf7a0_row8_col1" class="data row8 col1" >38 <span style="color: grey">(12.4%) </span></td>
      <td id="T_cf7a0_row8_col2" class="data row8 col2" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_cf7a0_row8_col3" class="data row8 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_cf7a0_row8_col4" class="data row8 col4" >129 <span style="color: grey">(42.2%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_cf7a0_row9_col0" class="data row9 col0" >10 <span style="color: grey">(3.3%) </span></td>
      <td id="T_cf7a0_row9_col1" class="data row9 col1" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_cf7a0_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row9_col4" class="data row9 col4" >11 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_cf7a0_row10_col0" class="data row10 col0" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cf7a0_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row10_col4" class="data row10 col4" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_cf7a0_row11_col0" class="data row11 col0" >6 <span style="color: grey">(2.0%) </span></td>
      <td id="T_cf7a0_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row11_col4" class="data row11 col4" >6 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_cf7a0_row12_col0" class="data row12 col0" >8 <span style="color: grey">(2.6%) </span></td>
      <td id="T_cf7a0_row12_col1" class="data row12 col1" >9 <span style="color: grey">(2.9%) </span></td>
      <td id="T_cf7a0_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row12_col4" class="data row12 col4" >17 <span style="color: grey">(5.6%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_cf7a0_row13_col0" class="data row13 col0" >7 <span style="color: grey">(2.3%) </span></td>
      <td id="T_cf7a0_row13_col1" class="data row13 col1" >17 <span style="color: grey">(5.6%) </span></td>
      <td id="T_cf7a0_row13_col2" class="data row13 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row13_col3" class="data row13 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_cf7a0_row13_col4" class="data row13 col4" >25 <span style="color: grey">(8.2%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_cf7a0_row14_col0" class="data row14 col0" >44 <span style="color: grey">(14.4%) </span></td>
      <td id="T_cf7a0_row14_col1" class="data row14 col1" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cf7a0_row14_col2" class="data row14 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row14_col3" class="data row14 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf7a0_row14_col4" class="data row14 col4" >48 <span style="color: grey">(15.7%) </span></td>
    </tr>
    <tr>
      <th id="T_cf7a0_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_cf7a0_row15_col0" class="data row15 col0" >225 <span style="color: grey">(73.5%) </span></td>
      <td id="T_cf7a0_row15_col1" class="data row15 col1" >75 <span style="color: grey">(24.5%) </span></td>
      <td id="T_cf7a0_row15_col2" class="data row15 col2" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cf7a0_row15_col3" class="data row15 col3" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_cf7a0_row15_col4" class="data row15 col4" >306 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_80643 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_80643  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_80643_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.6%, transparent 6.6%);
  font-family: Courier;
}
#T_80643_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.5%, transparent 13.5%);
  font-family: Courier;
}
#T_80643_row0_col2, #T_80643_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_80643_row0_col3, #T_80643_row5_col2, #T_80643_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_80643_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_80643_row1_col0, #T_80643_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_80643_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_80643_row1_col2, #T_80643_row1_col3, #T_80643_row2_col2, #T_80643_row2_col3, #T_80643_row3_col2, #T_80643_row3_col3, #T_80643_row4_col1, #T_80643_row4_col2, #T_80643_row4_col3, #T_80643_row5_col3, #T_80643_row6_col2, #T_80643_row6_col3 {
  width: 10em;
  font-family: Courier;
}
#T_80643_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_80643_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_80643_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_80643_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.5%, transparent 30.5%);
  font-family: Courier;
}
#T_80643_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.9%, transparent 14.9%);
  font-family: Courier;
}
#T_80643_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.0%, transparent 27.0%);
  font-family: Courier;
}
#T_80643_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_80643_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_80643_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.6%, transparent 41.6%);
  font-family: Courier;
}
#T_80643_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.4%, transparent 28.4%);
  font-family: Courier;
}
#T_80643_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.0%, transparent 39.0%);
  font-family: Courier;
}
#T_80643_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.2%, transparent 5.2%);
  font-family: Courier;
}
#T_80643_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.1%, transparent 4.1%);
  font-family: Courier;
}
#T_80643_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_80643_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.8%, transparent 9.8%);
  font-family: Courier;
}
#T_80643_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.1%, transparent 31.1%);
  font-family: Courier;
}
#T_80643_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_80643_row8_col0, #T_80643_row8_col1, #T_80643_row8_col2, #T_80643_row8_col3, #T_80643_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_80643">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_80643_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_80643_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_80643_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_80643_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_80643_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_80643_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_80643_row0_col0" class="data row0 col0" >20 <span style="color: grey">(5.2%) </span></td>
      <td id="T_80643_row0_col1" class="data row0 col1" >10 <span style="color: grey">(2.6%) </span></td>
      <td id="T_80643_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_80643_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_80643_row0_col4" class="data row0 col4" >32 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_80643_row1_col0" class="data row1 col0" >8 <span style="color: grey">(2.1%) </span></td>
      <td id="T_80643_row1_col1" class="data row1 col1" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_80643_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row1_col4" class="data row1 col4" >10 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_80643_row2_col0" class="data row2 col0" >9 <span style="color: grey">(2.3%) </span></td>
      <td id="T_80643_row2_col1" class="data row2 col1" >4 <span style="color: grey">(1.0%) </span></td>
      <td id="T_80643_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row2_col4" class="data row2 col4" >13 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_80643_row3_col0" class="data row3 col0" >93 <span style="color: grey">(24.2%) </span></td>
      <td id="T_80643_row3_col1" class="data row3 col1" >11 <span style="color: grey">(2.9%) </span></td>
      <td id="T_80643_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row3_col4" class="data row3 col4" >104 <span style="color: grey">(27.0%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_80643_row4_col0" class="data row4 col0" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_80643_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row4_col4" class="data row4 col4" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_80643_row5_col0" class="data row5 col0" >127 <span style="color: grey">(33.0%) </span></td>
      <td id="T_80643_row5_col1" class="data row5 col1" >21 <span style="color: grey">(5.5%) </span></td>
      <td id="T_80643_row5_col2" class="data row5 col2" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_80643_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row5_col4" class="data row5 col4" >150 <span style="color: grey">(39.0%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_80643_row6_col0" class="data row6 col0" >16 <span style="color: grey">(4.2%) </span></td>
      <td id="T_80643_row6_col1" class="data row6 col1" >3 <span style="color: grey">(0.8%) </span></td>
      <td id="T_80643_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_80643_row6_col4" class="data row6 col4" >19 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_80643_row7_col0" class="data row7 col0" >30 <span style="color: grey">(7.8%) </span></td>
      <td id="T_80643_row7_col1" class="data row7 col1" >23 <span style="color: grey">(6.0%) </span></td>
      <td id="T_80643_row7_col2" class="data row7 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_80643_row7_col3" class="data row7 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_80643_row7_col4" class="data row7 col4" >55 <span style="color: grey">(14.3%) </span></td>
    </tr>
    <tr>
      <th id="T_80643_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_80643_row8_col0" class="data row8 col0" >305 <span style="color: grey">(79.2%) </span></td>
      <td id="T_80643_row8_col1" class="data row8 col1" >74 <span style="color: grey">(19.2%) </span></td>
      <td id="T_80643_row8_col2" class="data row8 col2" >4 <span style="color: grey">(1.0%) </span></td>
      <td id="T_80643_row8_col3" class="data row8 col3" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_80643_row8_col4" class="data row8 col4" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_7455f th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_7455f  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_7455f_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_7455f_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.8%, transparent 8.8%);
  font-family: Courier;
}
#T_7455f_row0_col2, #T_7455f_row0_col3, #T_7455f_row1_col2, #T_7455f_row1_col3, #T_7455f_row2_col2, #T_7455f_row2_col3, #T_7455f_row3_col2, #T_7455f_row3_col3, #T_7455f_row4_col1, #T_7455f_row4_col2, #T_7455f_row4_col3, #T_7455f_row5_col3, #T_7455f_row6_col0, #T_7455f_row6_col1, #T_7455f_row6_col2, #T_7455f_row7_col2, #T_7455f_row7_col3, #T_7455f_row8_col2, #T_7455f_row8_col3, #T_7455f_row9_col1, #T_7455f_row9_col2, #T_7455f_row9_col3, #T_7455f_row10_col0, #T_7455f_row10_col2, #T_7455f_row10_col3, #T_7455f_row11_col3, #T_7455f_row12_col2, #T_7455f_row12_col3 {
  width: 10em;
  font-family: Courier;
}
#T_7455f_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_7455f_row1_col0, #T_7455f_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.7%, transparent 4.7%);
  font-family: Courier;
}
#T_7455f_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.0%, transparent 7.0%);
  font-family: Courier;
}
#T_7455f_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.1%, transparent 5.1%);
  font-family: Courier;
}
#T_7455f_row2_col1, #T_7455f_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.5%, transparent 3.5%);
  font-family: Courier;
}
#T_7455f_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_7455f_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
#T_7455f_row3_col1, #T_7455f_row10_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_7455f_row3_col4, #T_7455f_row9_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_7455f_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_7455f_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_7455f_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_7455f_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_7455f_row5_col4, #T_7455f_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_7455f_row6_col3, #T_7455f_row13_col0, #T_7455f_row13_col1, #T_7455f_row13_col2, #T_7455f_row13_col3, #T_7455f_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_7455f_row6_col4, #T_7455f_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_7455f_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_7455f_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.1%, transparent 28.1%);
  font-family: Courier;
}
#T_7455f_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_7455f_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.8%, transparent 44.8%);
  font-family: Courier;
}
#T_7455f_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.5%, transparent 10.5%);
  font-family: Courier;
}
#T_7455f_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.4%, transparent 36.4%);
  font-family: Courier;
}
#T_7455f_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_7455f_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.8%, transparent 19.8%);
  font-family: Courier;
}
#T_7455f_row11_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.8%, transparent 22.8%);
  font-family: Courier;
}
#T_7455f_row11_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_7455f_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.9%, transparent 20.9%);
  font-family: Courier;
}
#T_7455f_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.3%, transparent 12.3%);
  font-family: Courier;
}
#T_7455f_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
</style>
<table id="T_7455f">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_7455f_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_7455f_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_7455f_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_7455f_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_7455f_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.04] Affected body parts</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_7455f_level0_row0" class="row_heading level0 row0" >Abdomen</th>
      <td id="T_7455f_row0_col0" class="data row0 col0" >12 <span style="color: grey">(4.7%) </span></td>
      <td id="T_7455f_row0_col1" class="data row0 col1" >5 <span style="color: grey">(2.0%) </span></td>
      <td id="T_7455f_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row0_col4" class="data row0 col4" >17 <span style="color: grey">(6.7%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row1" class="row_heading level0 row1" >Back</th>
      <td id="T_7455f_row1_col0" class="data row1 col0" >9 <span style="color: grey">(3.6%) </span></td>
      <td id="T_7455f_row1_col1" class="data row1 col1" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_7455f_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row1_col4" class="data row1 col4" >13 <span style="color: grey">(5.1%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row2" class="row_heading level0 row2" >Buttocks</th>
      <td id="T_7455f_row2_col0" class="data row2 col0" >9 <span style="color: grey">(3.6%) </span></td>
      <td id="T_7455f_row2_col1" class="data row2 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_7455f_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row2_col4" class="data row2 col4" >11 <span style="color: grey">(4.3%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row3" class="row_heading level0 row3" >Chest</th>
      <td id="T_7455f_row3_col0" class="data row3 col0" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_7455f_row3_col1" class="data row3 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_7455f_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row3_col4" class="data row3 col4" >5 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row4" class="row_heading level0 row4" >Coccyx</th>
      <td id="T_7455f_row4_col0" class="data row4 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_7455f_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row4_col4" class="data row4 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row5" class="row_heading level0 row5" >Full body</th>
      <td id="T_7455f_row5_col0" class="data row5 col0" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_7455f_row5_col1" class="data row5 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_7455f_row5_col2" class="data row5 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_7455f_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row5_col4" class="data row5 col4" >9 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row6" class="row_heading level0 row6" >Hals</th>
      <td id="T_7455f_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_7455f_row6_col4" class="data row6 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row7" class="row_heading level0 row7" >Head</th>
      <td id="T_7455f_row7_col0" class="data row7 col0" >13 <span style="color: grey">(5.1%) </span></td>
      <td id="T_7455f_row7_col1" class="data row7 col1" >16 <span style="color: grey">(6.3%) </span></td>
      <td id="T_7455f_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row7_col4" class="data row7 col4" >29 <span style="color: grey">(11.5%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row8" class="row_heading level0 row8" >Innere Medizin</th>
      <td id="T_7455f_row8_col0" class="data row8 col0" >86 <span style="color: grey">(34.0%) </span></td>
      <td id="T_7455f_row8_col1" class="data row8 col1" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_7455f_row8_col2" class="data row8 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row8_col3" class="data row8 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row8_col4" class="data row8 col4" >92 <span style="color: grey">(36.4%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row9" class="row_heading level0 row9" >Intestine</th>
      <td id="T_7455f_row9_col0" class="data row9 col0" >5 <span style="color: grey">(2.0%) </span></td>
      <td id="T_7455f_row9_col1" class="data row9 col1" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row9_col4" class="data row9 col4" >5 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row10" class="row_heading level0 row10" >Intimate area</th>
      <td id="T_7455f_row10_col0" class="data row10 col0" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row10_col1" class="data row10 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_7455f_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row10_col4" class="data row10 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row11" class="row_heading level0 row11" >Lower extremities</th>
      <td id="T_7455f_row11_col0" class="data row11 col0" >38 <span style="color: grey">(15.0%) </span></td>
      <td id="T_7455f_row11_col1" class="data row11 col1" >13 <span style="color: grey">(5.1%) </span></td>
      <td id="T_7455f_row11_col2" class="data row11 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_7455f_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row11_col4" class="data row11 col4" >53 <span style="color: grey">(20.9%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row12" class="row_heading level0 row12" >Upper extremities</th>
      <td id="T_7455f_row12_col0" class="data row12 col0" >7 <span style="color: grey">(2.8%) </span></td>
      <td id="T_7455f_row12_col1" class="data row12 col1" >7 <span style="color: grey">(2.8%) </span></td>
      <td id="T_7455f_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7455f_row12_col4" class="data row12 col4" >14 <span style="color: grey">(5.5%) </span></td>
    </tr>
    <tr>
      <th id="T_7455f_level0_row13" class="row_heading level0 row13" >Total</th>
      <td id="T_7455f_row13_col0" class="data row13 col0" >192 <span style="color: grey">(75.9%) </span></td>
      <td id="T_7455f_row13_col1" class="data row13 col1" >57 <span style="color: grey">(22.5%) </span></td>
      <td id="T_7455f_row13_col2" class="data row13 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_7455f_row13_col3" class="data row13 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_7455f_row13_col4" class="data row13 col4" >253 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_9ed4b th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_9ed4b  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_9ed4b_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 99.5%, transparent 99.5%);
  font-family: Courier;
}
#T_9ed4b_row0_col1, #T_9ed4b_row2_col3, #T_9ed4b_row3_col0, #T_9ed4b_row3_col1, #T_9ed4b_row3_col2, #T_9ed4b_row3_col3, #T_9ed4b_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_9ed4b_row0_col2, #T_9ed4b_row1_col2, #T_9ed4b_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_9ed4b_row0_col3, #T_9ed4b_row1_col0, #T_9ed4b_row1_col1, #T_9ed4b_row1_col3, #T_9ed4b_row2_col1 {
  width: 10em;
  font-family: Courier;
}
#T_9ed4b_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.3%, transparent 98.3%);
  font-family: Courier;
}
#T_9ed4b_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_9ed4b_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_9ed4b_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
</style>
<table id="T_9ed4b">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_9ed4b_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_9ed4b_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_9ed4b_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_9ed4b_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_9ed4b_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.02] With hospitalization</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_9ed4b_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_9ed4b_row0_col0" class="data row0 col0" >183 <span style="color: grey">(76.2%) </span></td>
      <td id="T_9ed4b_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_9ed4b_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9ed4b_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9ed4b_row0_col4" class="data row0 col4" >236 <span style="color: grey">(98.3%) </span></td>
    </tr>
    <tr>
      <th id="T_9ed4b_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_9ed4b_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_9ed4b_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9ed4b_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9ed4b_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9ed4b_row1_col4" class="data row1 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_9ed4b_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_9ed4b_row2_col0" class="data row2 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9ed4b_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9ed4b_row2_col2" class="data row2 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9ed4b_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9ed4b_row2_col4" class="data row2 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_9ed4b_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_9ed4b_row3_col0" class="data row3 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_9ed4b_row3_col1" class="data row3 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_9ed4b_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_9ed4b_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9ed4b_row3_col4" class="data row3 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_076c2 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_076c2  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_076c2_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 92.9%, transparent 92.9%);
  font-family: Courier;
}
#T_076c2_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.2%, transparent 19.2%);
  font-family: Courier;
}
#T_076c2_row0_col2, #T_076c2_row0_col3, #T_076c2_row1_col1, #T_076c2_row1_col2, #T_076c2_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_076c2_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.4%, transparent 75.4%);
  font-family: Courier;
}
#T_076c2_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_076c2_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_076c2_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_076c2_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.8%, transparent 80.8%);
  font-family: Courier;
}
#T_076c2_row2_col2, #T_076c2_row2_col3, #T_076c2_row3_col0, #T_076c2_row3_col1, #T_076c2_row3_col2, #T_076c2_row3_col3, #T_076c2_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_076c2_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.9%, transparent 22.9%);
  font-family: Courier;
}
</style>
<table id="T_076c2">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_076c2_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_076c2_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_076c2_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_076c2_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_076c2_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.03] Medical follow-up treatment</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_076c2_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_076c2_row0_col0" class="data row0 col0" >171 <span style="color: grey">(71.2%) </span></td>
      <td id="T_076c2_row0_col1" class="data row0 col1" >10 <span style="color: grey">(4.2%) </span></td>
      <td id="T_076c2_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_076c2_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_076c2_row0_col4" class="data row0 col4" >181 <span style="color: grey">(75.4%) </span></td>
    </tr>
    <tr>
      <th id="T_076c2_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_076c2_row1_col0" class="data row1 col0" >4 <span style="color: grey">(1.7%) </span></td>
      <td id="T_076c2_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_076c2_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_076c2_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_076c2_row1_col4" class="data row1 col4" >4 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_076c2_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_076c2_row2_col0" class="data row2 col0" >9 <span style="color: grey">(3.8%) </span></td>
      <td id="T_076c2_row2_col1" class="data row2 col1" >42 <span style="color: grey">(17.5%) </span></td>
      <td id="T_076c2_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_076c2_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_076c2_row2_col4" class="data row2 col4" >55 <span style="color: grey">(22.9%) </span></td>
    </tr>
    <tr>
      <th id="T_076c2_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_076c2_row3_col0" class="data row3 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_076c2_row3_col1" class="data row3 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_076c2_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_076c2_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_076c2_row3_col4" class="data row3 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e2964 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2964  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2964_row0_col0, #T_e2964_row0_col1, #T_e2964_row0_col2, #T_e2964_row0_col3, #T_e2964_row0_col4, #T_e2964_row1_col0, #T_e2964_row1_col1, #T_e2964_row1_col2, #T_e2964_row1_col3, #T_e2964_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_e2964">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e2964_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e2964_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e2964_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e2964_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_e2964_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.04] With delayed therapy protocol</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e2964_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_e2964_row0_col0" class="data row0 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_e2964_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_e2964_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_e2964_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e2964_row0_col4" class="data row0 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_e2964_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_e2964_row1_col0" class="data row1 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_e2964_row1_col1" class="data row1 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_e2964_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_e2964_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e2964_row1_col4" class="data row1 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e5460 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e5460  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e5460_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 99.5%, transparent 99.5%);
  font-family: Courier;
}
#T_e5460_row0_col1, #T_e5460_row0_col3, #T_e5460_row1_col2, #T_e5460_row2_col0, #T_e5460_row2_col1, #T_e5460_row2_col2, #T_e5460_row2_col3, #T_e5460_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e5460_row0_col2, #T_e5460_row1_col1, #T_e5460_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_e5460_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.3%, transparent 98.3%);
  font-family: Courier;
}
#T_e5460_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_e5460_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
</style>
<table id="T_e5460">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e5460_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e5460_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e5460_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e5460_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_e5460_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.06] Increased care needs</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e5460_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_e5460_row0_col0" class="data row0 col0" >183 <span style="color: grey">(76.2%) </span></td>
      <td id="T_e5460_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_e5460_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e5460_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e5460_row0_col4" class="data row0 col4" >236 <span style="color: grey">(98.3%) </span></td>
    </tr>
    <tr>
      <th id="T_e5460_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_e5460_row1_col0" class="data row1 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e5460_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e5460_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_e5460_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e5460_row1_col4" class="data row1 col4" >4 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_e5460_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_e5460_row2_col0" class="data row2 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_e5460_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_e5460_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_e5460_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e5460_row2_col4" class="data row2 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_606eb th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_606eb  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_606eb_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.3%, transparent 86.3%);
  font-family: Courier;
}
#T_606eb_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.1%, transparent 68.1%);
  font-family: Courier;
}
#T_606eb_row0_col2, #T_606eb_row0_col3, #T_606eb_row1_col2, #T_606eb_row1_col3, #T_606eb_row2_col0 {
  width: 10em;
  font-family: Courier;
}
#T_606eb_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.2%, transparent 81.2%);
  font-family: Courier;
}
#T_606eb_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.7%, transparent 13.7%);
  font-family: Courier;
}
#T_606eb_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.5%, transparent 25.5%);
  font-family: Courier;
}
#T_606eb_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.8%, transparent 15.8%);
  font-family: Courier;
}
#T_606eb_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.4%, transparent 6.4%);
  font-family: Courier;
}
#T_606eb_row2_col2, #T_606eb_row2_col3, #T_606eb_row3_col0, #T_606eb_row3_col1, #T_606eb_row3_col2, #T_606eb_row3_col3, #T_606eb_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_606eb_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
</style>
<table id="T_606eb">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_606eb_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_606eb_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_606eb_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_606eb_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_606eb_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.07] With medication administration</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_606eb_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_606eb_row0_col0" class="data row0 col0" >158 <span style="color: grey">(67.5%) </span></td>
      <td id="T_606eb_row0_col1" class="data row0 col1" >32 <span style="color: grey">(13.7%) </span></td>
      <td id="T_606eb_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_606eb_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_606eb_row0_col4" class="data row0 col4" >190 <span style="color: grey">(81.2%) </span></td>
    </tr>
    <tr>
      <th id="T_606eb_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_606eb_row1_col0" class="data row1 col0" >25 <span style="color: grey">(10.7%) </span></td>
      <td id="T_606eb_row1_col1" class="data row1 col1" >12 <span style="color: grey">(5.1%) </span></td>
      <td id="T_606eb_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_606eb_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_606eb_row1_col4" class="data row1 col4" >37 <span style="color: grey">(15.8%) </span></td>
    </tr>
    <tr>
      <th id="T_606eb_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_606eb_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_606eb_row2_col1" class="data row2 col1" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_606eb_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_606eb_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_606eb_row2_col4" class="data row2 col4" >7 <span style="color: grey">(3.0%) </span></td>
    </tr>
    <tr>
      <th id="T_606eb_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_606eb_row3_col0" class="data row3 col0" >183 <span style="color: grey">(78.2%) </span></td>
      <td id="T_606eb_row3_col1" class="data row3 col1" >47 <span style="color: grey">(20.1%) </span></td>
      <td id="T_606eb_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_606eb_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_606eb_row3_col4" class="data row3 col4" >234 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_ec982 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ec982  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ec982_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.3%, transparent 27.3%);
  font-family: Courier;
}
#T_ec982_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 48.1%, transparent 48.1%);
  font-family: Courier;
}
#T_ec982_row0_col2, #T_ec982_row0_col3, #T_ec982_row2_col0, #T_ec982_row2_col1, #T_ec982_row2_col2, #T_ec982_row2_col3, #T_ec982_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_ec982_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 32.8%, transparent 32.8%);
  font-family: Courier;
}
#T_ec982_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 72.7%, transparent 72.7%);
  font-family: Courier;
}
#T_ec982_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 51.9%, transparent 51.9%);
  font-family: Courier;
}
#T_ec982_row1_col2, #T_ec982_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_ec982_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 67.2%, transparent 67.2%);
  font-family: Courier;
}
</style>
<table id="T_ec982">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_ec982_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_ec982_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_ec982_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_ec982_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_ec982_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.08] Occurrence of fear and uncertainty</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ec982_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_ec982_row0_col0" class="data row0 col0" >50 <span style="color: grey">(21.0%) </span></td>
      <td id="T_ec982_row0_col1" class="data row0 col1" >25 <span style="color: grey">(10.5%) </span></td>
      <td id="T_ec982_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_ec982_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ec982_row0_col4" class="data row0 col4" >78 <span style="color: grey">(32.8%) </span></td>
    </tr>
    <tr>
      <th id="T_ec982_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_ec982_row1_col0" class="data row1 col0" >133 <span style="color: grey">(55.9%) </span></td>
      <td id="T_ec982_row1_col1" class="data row1 col1" >27 <span style="color: grey">(11.3%) </span></td>
      <td id="T_ec982_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ec982_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ec982_row1_col4" class="data row1 col4" >160 <span style="color: grey">(67.2%) </span></td>
    </tr>
    <tr>
      <th id="T_ec982_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_ec982_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.9%) </span></td>
      <td id="T_ec982_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_ec982_row2_col2" class="data row2 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_ec982_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ec982_row2_col4" class="data row2 col4" >238 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_70fe0 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_70fe0  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_70fe0_row0_col0, #T_70fe0_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.3%, transparent 12.3%);
  font-family: Courier;
}
#T_70fe0_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_70fe0_row0_col2, #T_70fe0_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_70fe0_row0_col3, #T_70fe0_row1_col3, #T_70fe0_row2_col3, #T_70fe0_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_70fe0_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.7%, transparent 11.7%);
  font-family: Courier;
}
#T_70fe0_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 63.0%, transparent 63.0%);
  font-family: Courier;
}
#T_70fe0_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 59.5%, transparent 59.5%);
  font-family: Courier;
}
#T_70fe0_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 59.2%, transparent 59.2%);
  font-family: Courier;
}
#T_70fe0_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_70fe0_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.8%, transparent 10.8%);
  font-family: Courier;
}
#T_70fe0_row2_col2, #T_70fe0_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_70fe0_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_70fe0_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.2%, transparent 16.2%);
  font-family: Courier;
}
#T_70fe0_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.2%, transparent 14.2%);
  font-family: Courier;
}
#T_70fe0_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_70fe0_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.1%, transparent 8.1%);
  font-family: Courier;
}
#T_70fe0_row4_col2, #T_70fe0_row4_col3 {
  width: 10em;
  font-family: Courier;
}
#T_70fe0_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_70fe0_row5_col0, #T_70fe0_row5_col1, #T_70fe0_row5_col2, #T_70fe0_row5_col3, #T_70fe0_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_70fe0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_70fe0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_70fe0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_70fe0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_70fe0_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_70fe0_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.08.01] Affected person</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_70fe0_level0_row0" class="row_heading level0 row0" >BeIn the treatment team</th>
      <td id="T_70fe0_row0_col0" class="data row0 col0" >9 <span style="color: grey">(7.5%) </span></td>
      <td id="T_70fe0_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.7%) </span></td>
      <td id="T_70fe0_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.7%) </span></td>
      <td id="T_70fe0_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_70fe0_row0_col4" class="data row0 col4" >14 <span style="color: grey">(11.7%) </span></td>
    </tr>
    <tr>
      <th id="T_70fe0_level0_row1" class="row_heading level0 row1" >For affected individuals</th>
      <td id="T_70fe0_row1_col0" class="data row1 col0" >46 <span style="color: grey">(38.3%) </span></td>
      <td id="T_70fe0_row1_col1" class="data row1 col1" >22 <span style="color: grey">(18.3%) </span></td>
      <td id="T_70fe0_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.7%) </span></td>
      <td id="T_70fe0_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_70fe0_row1_col4" class="data row1 col4" >71 <span style="color: grey">(59.2%) </span></td>
    </tr>
    <tr>
      <th id="T_70fe0_level0_row2" class="row_heading level0 row2" >For parents des Betroffenen</th>
      <td id="T_70fe0_row2_col0" class="data row2 col0" >4 <span style="color: grey">(3.3%) </span></td>
      <td id="T_70fe0_row2_col1" class="data row2 col1" >4 <span style="color: grey">(3.3%) </span></td>
      <td id="T_70fe0_row2_col2" class="data row2 col2" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_70fe0_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_70fe0_row2_col4" class="data row2 col4" >10 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_70fe0_level0_row3" class="row_heading level0 row3" >For the excercise experts</th>
      <td id="T_70fe0_row3_col0" class="data row3 col0" >9 <span style="color: grey">(7.5%) </span></td>
      <td id="T_70fe0_row3_col1" class="data row3 col1" >6 <span style="color: grey">(5.0%) </span></td>
      <td id="T_70fe0_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_70fe0_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_70fe0_row3_col4" class="data row3 col4" >17 <span style="color: grey">(14.2%) </span></td>
    </tr>
    <tr>
      <th id="T_70fe0_level0_row4" class="row_heading level0 row4" >Mit der Ablehnung weiterer sporttherapheutischer Angebote</th>
      <td id="T_70fe0_row4_col0" class="data row4 col0" >5 <span style="color: grey">(4.2%) </span></td>
      <td id="T_70fe0_row4_col1" class="data row4 col1" >3 <span style="color: grey">(2.5%) </span></td>
      <td id="T_70fe0_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_70fe0_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_70fe0_row4_col4" class="data row4 col4" >8 <span style="color: grey">(6.7%) </span></td>
    </tr>
    <tr>
      <th id="T_70fe0_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_70fe0_row5_col0" class="data row5 col0" >73 <span style="color: grey">(60.8%) </span></td>
      <td id="T_70fe0_row5_col1" class="data row5 col1" >37 <span style="color: grey">(30.8%) </span></td>
      <td id="T_70fe0_row5_col2" class="data row5 col2" >6 <span style="color: grey">(5.0%) </span></td>
      <td id="T_70fe0_row5_col3" class="data row5 col3" >4 <span style="color: grey">(3.3%) </span></td>
      <td id="T_70fe0_row5_col4" class="data row5 col4" >120 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_3d0a9 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3d0a9  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3d0a9_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_3d0a9_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.8%, transparent 11.8%);
  font-family: Courier;
}
#T_3d0a9_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_3d0a9_row0_col3, #T_3d0a9_row1_col3, #T_3d0a9_row2_col0, #T_3d0a9_row2_col1, #T_3d0a9_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_3d0a9_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.1%, transparent 7.1%);
  font-family: Courier;
}
#T_3d0a9_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 94.6%, transparent 94.6%);
  font-family: Courier;
}
#T_3d0a9_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 88.2%, transparent 88.2%);
  font-family: Courier;
}
#T_3d0a9_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_3d0a9_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 92.5%, transparent 92.5%);
  font-family: Courier;
}
#T_3d0a9_row2_col3, #T_3d0a9_row3_col0, #T_3d0a9_row3_col1, #T_3d0a9_row3_col2, #T_3d0a9_row3_col3, #T_3d0a9_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_3d0a9_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_3d0a9">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_3d0a9_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_3d0a9_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_3d0a9_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_3d0a9_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_3d0a9_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.09] Structural adjustment</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3d0a9_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_3d0a9_row0_col0" class="data row0 col0" >10 <span style="color: grey">(4.2%) </span></td>
      <td id="T_3d0a9_row0_col1" class="data row0 col1" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_3d0a9_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_3d0a9_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3d0a9_row0_col4" class="data row0 col4" >17 <span style="color: grey">(7.1%) </span></td>
    </tr>
    <tr>
      <th id="T_3d0a9_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_3d0a9_row1_col0" class="data row1 col0" >174 <span style="color: grey">(72.8%) </span></td>
      <td id="T_3d0a9_row1_col1" class="data row1 col1" >45 <span style="color: grey">(18.8%) </span></td>
      <td id="T_3d0a9_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_3d0a9_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3d0a9_row1_col4" class="data row1 col4" >221 <span style="color: grey">(92.5%) </span></td>
    </tr>
    <tr>
      <th id="T_3d0a9_level0_row2" class="row_heading level0 row2" >Weiß nicht</th>
      <td id="T_3d0a9_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_3d0a9_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_3d0a9_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_3d0a9_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_3d0a9_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_3d0a9_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_3d0a9_row3_col0" class="data row3 col0" >184 <span style="color: grey">(77.0%) </span></td>
      <td id="T_3d0a9_row3_col1" class="data row3 col1" >51 <span style="color: grey">(21.3%) </span></td>
      <td id="T_3d0a9_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_3d0a9_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_3d0a9_row3_col4" class="data row3 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_dfa69 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dfa69  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dfa69_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.4%, transparent 80.4%);
  font-family: Courier;
}
#T_dfa69_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.4%, transparent 43.4%);
  font-family: Courier;
}
#T_dfa69_row0_col2, #T_dfa69_row0_col3, #T_dfa69_row1_col1, #T_dfa69_row1_col2, #T_dfa69_row1_col3, #T_dfa69_row3_col2, #T_dfa69_row3_col3, #T_dfa69_row4_col2, #T_dfa69_row4_col3, #T_dfa69_row5_col2, #T_dfa69_row5_col3 {
  width: 10em;
  font-family: Courier;
}
#T_dfa69_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 71.0%, transparent 71.0%);
  font-family: Courier;
}
#T_dfa69_row1_col0, #T_dfa69_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_dfa69_row1_col4, #T_dfa69_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_dfa69_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.5%, transparent 6.5%);
  font-family: Courier;
}
#T_dfa69_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.7%, transparent 37.7%);
  font-family: Courier;
}
#T_dfa69_row2_col2, #T_dfa69_row2_col3, #T_dfa69_row6_col0, #T_dfa69_row6_col1, #T_dfa69_row6_col2, #T_dfa69_row6_col3, #T_dfa69_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_dfa69_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.9%, transparent 14.9%);
  font-family: Courier;
}
#T_dfa69_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.2%, transparent 9.2%);
  font-family: Courier;
}
#T_dfa69_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.2%, transparent 13.2%);
  font-family: Courier;
}
#T_dfa69_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_dfa69_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_dfa69_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_dfa69_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_dfa69_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
</style>
<table id="T_dfa69">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_dfa69_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_dfa69_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_dfa69_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_dfa69_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_dfa69_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.10.01] Approver</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_dfa69_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_dfa69_row0_col0" class="data row0 col0" >148 <span style="color: grey">(61.4%) </span></td>
      <td id="T_dfa69_row0_col1" class="data row0 col1" >23 <span style="color: grey">(9.5%) </span></td>
      <td id="T_dfa69_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row0_col4" class="data row0 col4" >171 <span style="color: grey">(71.0%) </span></td>
    </tr>
    <tr>
      <th id="T_dfa69_level0_row1" class="row_heading level0 row1" >Eltern</th>
      <td id="T_dfa69_row1_col0" class="data row1 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_dfa69_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row1_col4" class="data row1 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_dfa69_level0_row2" class="row_heading level0 row2" >Medizin</th>
      <td id="T_dfa69_row2_col0" class="data row2 col0" >12 <span style="color: grey">(5.0%) </span></td>
      <td id="T_dfa69_row2_col1" class="data row2 col1" >20 <span style="color: grey">(8.3%) </span></td>
      <td id="T_dfa69_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_dfa69_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dfa69_row2_col4" class="data row2 col4" >36 <span style="color: grey">(14.9%) </span></td>
    </tr>
    <tr>
      <th id="T_dfa69_level0_row3" class="row_heading level0 row3" >Pflege</th>
      <td id="T_dfa69_row3_col0" class="data row3 col0" >17 <span style="color: grey">(7.1%) </span></td>
      <td id="T_dfa69_row3_col1" class="data row3 col1" >7 <span style="color: grey">(2.9%) </span></td>
      <td id="T_dfa69_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row3_col4" class="data row3 col4" >24 <span style="color: grey">(10.0%) </span></td>
    </tr>
    <tr>
      <th id="T_dfa69_level0_row4" class="row_heading level0 row4" >Physiotherapie</th>
      <td id="T_dfa69_row4_col0" class="data row4 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dfa69_row4_col1" class="data row4 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_dfa69_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row4_col4" class="data row4 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_dfa69_level0_row5" class="row_heading level0 row5" >Psychosozialer Dienst</th>
      <td id="T_dfa69_row5_col0" class="data row5 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_dfa69_row5_col1" class="data row5 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dfa69_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dfa69_row5_col4" class="data row5 col4" >4 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_dfa69_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_dfa69_row6_col0" class="data row6 col0" >184 <span style="color: grey">(76.3%) </span></td>
      <td id="T_dfa69_row6_col1" class="data row6 col1" >53 <span style="color: grey">(22.0%) </span></td>
      <td id="T_dfa69_row6_col2" class="data row6 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_dfa69_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dfa69_row6_col4" class="data row6 col4" >241 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_b63cb th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_b63cb  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_b63cb_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_b63cb_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.6%, transparent 34.6%);
  font-family: Courier;
}
#T_b63cb_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_b63cb_row0_col3 {
  width: 10em;
  font-family: Courier;
}
#T_b63cb_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.2%, transparent 9.2%);
  font-family: Courier;
}
#T_b63cb_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.9%, transparent 98.9%);
  font-family: Courier;
}
#T_b63cb_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 65.4%, transparent 65.4%);
  font-family: Courier;
}
#T_b63cb_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_b63cb_row1_col3, #T_b63cb_row2_col0, #T_b63cb_row2_col1, #T_b63cb_row2_col2, #T_b63cb_row2_col3, #T_b63cb_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_b63cb_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.8%, transparent 90.8%);
  font-family: Courier;
}
</style>
<table id="T_b63cb">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_b63cb_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_b63cb_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_b63cb_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_b63cb_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_b63cb_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.11] Application RICE rule (Rest, Ice, Compression, Elevation)</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_b63cb_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_b63cb_row0_col0" class="data row0 col0" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_b63cb_row0_col1" class="data row0 col1" >18 <span style="color: grey">(7.5%) </span></td>
      <td id="T_b63cb_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_b63cb_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_b63cb_row0_col4" class="data row0 col4" >22 <span style="color: grey">(9.2%) </span></td>
    </tr>
    <tr>
      <th id="T_b63cb_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_b63cb_row1_col0" class="data row1 col0" >181 <span style="color: grey">(75.7%) </span></td>
      <td id="T_b63cb_row1_col1" class="data row1 col1" >34 <span style="color: grey">(14.2%) </span></td>
      <td id="T_b63cb_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_b63cb_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_b63cb_row1_col4" class="data row1 col4" >217 <span style="color: grey">(90.8%) </span></td>
    </tr>
    <tr>
      <th id="T_b63cb_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_b63cb_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_b63cb_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_b63cb_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_b63cb_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_b63cb_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_131d1 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_131d1  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_131d1_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_131d1_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_131d1_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_131d1_row0_col3, #T_131d1_row2_col1, #T_131d1_row2_col2, #T_131d1_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_131d1_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_131d1_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.8%, transparent 97.8%);
  font-family: Courier;
}
#T_131d1_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_131d1_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_131d1_row1_col3, #T_131d1_row3_col0, #T_131d1_row3_col1, #T_131d1_row3_col2, #T_131d1_row3_col3, #T_131d1_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_131d1_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.1%, transparent 97.1%);
  font-family: Courier;
}
#T_131d1_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_131d1_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_131d1">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_131d1_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_131d1_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_131d1_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_131d1_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_131d1_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.12] With observation</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_131d1_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_131d1_row0_col0" class="data row0 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_131d1_row0_col1" class="data row0 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_131d1_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_131d1_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_131d1_row0_col4" class="data row0 col4" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_131d1_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_131d1_row1_col0" class="data row1 col0" >180 <span style="color: grey">(75.0%) </span></td>
      <td id="T_131d1_row1_col1" class="data row1 col1" >50 <span style="color: grey">(20.8%) </span></td>
      <td id="T_131d1_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_131d1_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_131d1_row1_col4" class="data row1 col4" >233 <span style="color: grey">(97.1%) </span></td>
    </tr>
    <tr>
      <th id="T_131d1_level0_row2" class="row_heading level0 row2" >U</th>
      <td id="T_131d1_row2_col0" class="data row2 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_131d1_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_131d1_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_131d1_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_131d1_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_131d1_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_131d1_row3_col0" class="data row3 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_131d1_row3_col1" class="data row3 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_131d1_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_131d1_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_131d1_row3_col4" class="data row3 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_1a6a5 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_1a6a5  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_1a6a5_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.7%, transparent 8.7%);
  font-family: Courier;
}
#T_1a6a5_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.5%, transparent 13.5%);
  font-family: Courier;
}
#T_1a6a5_row0_col2, #T_1a6a5_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_1a6a5_row0_col3, #T_1a6a5_row1_col2, #T_1a6a5_row2_col0, #T_1a6a5_row2_col1, #T_1a6a5_row2_col2, #T_1a6a5_row2_col3, #T_1a6a5_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_1a6a5_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_1a6a5_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.3%, transparent 91.3%);
  font-family: Courier;
}
#T_1a6a5_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.5%, transparent 86.5%);
  font-family: Courier;
}
#T_1a6a5_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.0%, transparent 90.0%);
  font-family: Courier;
}
</style>
<table id="T_1a6a5">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_1a6a5_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_1a6a5_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_1a6a5_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_1a6a5_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_1a6a5_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.13] Stop</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_1a6a5_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_1a6a5_row0_col0" class="data row0 col0" >16 <span style="color: grey">(6.7%) </span></td>
      <td id="T_1a6a5_row0_col1" class="data row0 col1" >7 <span style="color: grey">(2.9%) </span></td>
      <td id="T_1a6a5_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1a6a5_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_1a6a5_row0_col4" class="data row0 col4" >24 <span style="color: grey">(10.0%) </span></td>
    </tr>
    <tr>
      <th id="T_1a6a5_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_1a6a5_row1_col0" class="data row1 col0" >168 <span style="color: grey">(70.0%) </span></td>
      <td id="T_1a6a5_row1_col1" class="data row1 col1" >45 <span style="color: grey">(18.8%) </span></td>
      <td id="T_1a6a5_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_1a6a5_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1a6a5_row1_col4" class="data row1 col4" >216 <span style="color: grey">(90.0%) </span></td>
    </tr>
    <tr>
      <th id="T_1a6a5_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_1a6a5_row2_col0" class="data row2 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_1a6a5_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_1a6a5_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_1a6a5_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_1a6a5_row2_col4" class="data row2 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_0a201 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0a201  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0a201_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.7%, transparent 41.7%);
  font-family: Courier;
}
#T_0a201_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_0a201_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_0a201_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.2%, transparent 41.2%);
  font-family: Courier;
}
#T_0a201_row1_col0, #T_0a201_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.3%, transparent 58.3%);
  font-family: Courier;
}
#T_0a201_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.8%, transparent 57.8%);
  font-family: Courier;
}
#T_0a201_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_0a201_row2_col0, #T_0a201_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_0a201_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_0a201_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_0a201_row3_col0, #T_0a201_row3_col1, #T_0a201_row3_col2, #T_0a201_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_0a201">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_0a201_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_0a201_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_0a201_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_0a201_level0_col3" class="col_heading level0 col3" >Total</th>
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
      <th id="T_0a201_level0_row0" class="row_heading level0 row0" >Break</th>
      <td id="T_0a201_row0_col0" class="data row0 col0" >70 <span style="color: grey">(32.4%) </span></td>
      <td id="T_0a201_row0_col1" class="data row0 col1" >18 <span style="color: grey">(8.3%) </span></td>
      <td id="T_0a201_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_0a201_row0_col3" class="data row0 col3" >89 <span style="color: grey">(41.2%) </span></td>
    </tr>
    <tr>
      <th id="T_0a201_level0_row1" class="row_heading level0 row1" >Cessation</th>
      <td id="T_0a201_row1_col0" class="data row1 col0" >98 <span style="color: grey">(45.4%) </span></td>
      <td id="T_0a201_row1_col1" class="data row1 col1" >26 <span style="color: grey">(12.0%) </span></td>
      <td id="T_0a201_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_0a201_row1_col3" class="data row1 col3" >126 <span style="color: grey">(58.3%) </span></td>
    </tr>
    <tr>
      <th id="T_0a201_level0_row2" class="row_heading level0 row2" >Einheit war sowieso vorbei</th>
      <td id="T_0a201_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_0a201_row2_col1" class="data row2 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_0a201_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0a201_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_0a201_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_0a201_row3_col0" class="data row3 col0" >168 <span style="color: grey">(77.8%) </span></td>
      <td id="T_0a201_row3_col1" class="data row3 col1" >45 <span style="color: grey">(20.8%) </span></td>
      <td id="T_0a201_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.4%) </span></td>
      <td id="T_0a201_row3_col3" class="data row3 col3" >216 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_9351c th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_9351c  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_9351c_row0_col0, #T_9351c_row0_col1, #T_9351c_row0_col2, #T_9351c_row0_col3, #T_9351c_row0_col4, #T_9351c_row1_col0, #T_9351c_row1_col1, #T_9351c_row1_col2, #T_9351c_row1_col3, #T_9351c_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_9351c">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_9351c_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_9351c_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_9351c_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_9351c_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_9351c_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[03.14] Adaptations</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_9351c_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_9351c_row0_col0" class="data row0 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_9351c_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_9351c_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_9351c_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9351c_row0_col4" class="data row0 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_9351c_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_9351c_row1_col0" class="data row1 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_9351c_row1_col1" class="data row1 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_9351c_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_9351c_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9351c_row1_col4" class="data row1 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_a7540 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a7540  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a7540_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.0%, transparent 7.0%);
  font-family: Courier;
}
#T_a7540_row0_col1, #T_a7540_row3_col1, #T_a7540_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_a7540_row0_col2, #T_a7540_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.6%, transparent 7.6%);
  font-family: Courier;
}
#T_a7540_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_a7540_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_a7540_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.9%, transparent 47.9%);
  font-family: Courier;
}
#T_a7540_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.5%, transparent 37.5%);
  font-family: Courier;
}
#T_a7540_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 46.8%, transparent 46.8%);
  font-family: Courier;
}
#T_a7540_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.8%, transparent 33.8%);
  font-family: Courier;
}
#T_a7540_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.6%, transparent 31.6%);
  font-family: Courier;
}
#T_a7540_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.4%, transparent 1.4%);
  font-family: Courier;
}
#T_a7540_row4_col1, #T_a7540_row5_col1, #T_a7540_row6_col0 {
  width: 10em;
  font-family: Courier;
}
#T_a7540_row4_col2, #T_a7540_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_a7540_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.2%, transparent 4.2%);
  font-family: Courier;
}
#T_a7540_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_a7540_row7_col0, #T_a7540_row7_col1, #T_a7540_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_a7540">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_a7540_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_a7540_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_a7540_level0_col2" class="col_heading level0 col2" >Total</th>
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
      <th id="T_a7540_level0_row0" class="row_heading level0 row0" >Communication strategy</th>
      <td id="T_a7540_row0_col0" class="data row0 col0" >5 <span style="color: grey">(6.3%) </span></td>
      <td id="T_a7540_row0_col1" class="data row0 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_a7540_row0_col2" class="data row0 col2" >6 <span style="color: grey">(7.6%) </span></td>
    </tr>
    <tr>
      <th id="T_a7540_level0_row1" class="row_heading level0 row1" >Equipment</th>
      <td id="T_a7540_row1_col0" class="data row1 col0" >4 <span style="color: grey">(5.1%) </span></td>
      <td id="T_a7540_row1_col1" class="data row1 col1" >2 <span style="color: grey">(2.5%) </span></td>
      <td id="T_a7540_row1_col2" class="data row1 col2" >6 <span style="color: grey">(7.6%) </span></td>
    </tr>
    <tr>
      <th id="T_a7540_level0_row2" class="row_heading level0 row2" >Exercise selection</th>
      <td id="T_a7540_row2_col0" class="data row2 col0" >34 <span style="color: grey">(43.0%) </span></td>
      <td id="T_a7540_row2_col1" class="data row2 col1" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_a7540_row2_col2" class="data row2 col2" >37 <span style="color: grey">(46.8%) </span></td>
    </tr>
    <tr>
      <th id="T_a7540_level0_row3" class="row_heading level0 row3" >Intensity</th>
      <td id="T_a7540_row3_col0" class="data row3 col0" >24 <span style="color: grey">(30.4%) </span></td>
      <td id="T_a7540_row3_col1" class="data row3 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_a7540_row3_col2" class="data row3 col2" >25 <span style="color: grey">(31.6%) </span></td>
    </tr>
    <tr>
      <th id="T_a7540_level0_row4" class="row_heading level0 row4" >Motivationsstrategie</th>
      <td id="T_a7540_row4_col0" class="data row4 col0" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_a7540_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_a7540_row4_col2" class="data row4 col2" >1 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_a7540_level0_row5" class="row_heading level0 row5" >Setting</th>
      <td id="T_a7540_row5_col0" class="data row5 col0" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_a7540_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_a7540_row5_col2" class="data row5 col2" >3 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_a7540_level0_row6" class="row_heading level0 row6" >Weiteres</th>
      <td id="T_a7540_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_a7540_row6_col1" class="data row6 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_a7540_row6_col2" class="data row6 col2" >1 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_a7540_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_a7540_row7_col0" class="data row7 col0" >71 <span style="color: grey">(89.9%) </span></td>
      <td id="T_a7540_row7_col1" class="data row7 col1" >8 <span style="color: grey">(10.1%) </span></td>
      <td id="T_a7540_row7_col2" class="data row7 col2" >79 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e7d42 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e7d42  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e7d42_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.0%, transparent 13.0%);
  font-family: Courier;
}
#T_e7d42_row0_col1, #T_e7d42_row2_col0 {
  width: 10em;
  font-family: Courier;
}
#T_e7d42_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_e7d42_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.4%, transparent 17.4%);
  font-family: Courier;
}
#T_e7d42_row1_col1, #T_e7d42_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_e7d42_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.3%, transparent 17.3%);
  font-family: Courier;
}
#T_e7d42_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_e7d42_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.6%, transparent 69.6%);
  font-family: Courier;
}
#T_e7d42_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_e7d42_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.2%, transparent 69.2%);
  font-family: Courier;
}
#T_e7d42_row4_col0, #T_e7d42_row4_col1, #T_e7d42_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_e7d42">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e7d42_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e7d42_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e7d42_level0_col2" class="col_heading level0 col2" >Total</th>
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
      <th id="T_e7d42_level0_row0" class="row_heading level0 row0" >Ab jetzt für alle Bewegungseinheiten mit allen Patient*innen</th>
      <td id="T_e7d42_row0_col0" class="data row0 col0" >6 <span style="color: grey">(11.5%) </span></td>
      <td id="T_e7d42_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e7d42_row0_col2" class="data row0 col2" >6 <span style="color: grey">(11.5%) </span></td>
    </tr>
    <tr>
      <th id="T_e7d42_level0_row1" class="row_heading level0 row1" >Für die gesamte Therapiephase</th>
      <td id="T_e7d42_row1_col0" class="data row1 col0" >8 <span style="color: grey">(15.4%) </span></td>
      <td id="T_e7d42_row1_col1" class="data row1 col1" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_e7d42_row1_col2" class="data row1 col2" >9 <span style="color: grey">(17.3%) </span></td>
    </tr>
    <tr>
      <th id="T_e7d42_level0_row2" class="row_heading level0 row2" >Für die nächsten Einheiten (da das AE rückwirkend auftrat</th>
      <td id="T_e7d42_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_e7d42_row2_col1" class="data row2 col1" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_e7d42_row2_col2" class="data row2 col2" >1 <span style="color: grey">(1.9%) </span></td>
    </tr>
    <tr>
      <th id="T_e7d42_level0_row3" class="row_heading level0 row3" >Nur für diese Einheit</th>
      <td id="T_e7d42_row3_col0" class="data row3 col0" >32 <span style="color: grey">(61.5%) </span></td>
      <td id="T_e7d42_row3_col1" class="data row3 col1" >4 <span style="color: grey">(7.7%) </span></td>
      <td id="T_e7d42_row3_col2" class="data row3 col2" >36 <span style="color: grey">(69.2%) </span></td>
    </tr>
    <tr>
      <th id="T_e7d42_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_e7d42_row4_col0" class="data row4 col0" >46 <span style="color: grey">(88.5%) </span></td>
      <td id="T_e7d42_row4_col1" class="data row4 col1" >6 <span style="color: grey">(11.5%) </span></td>
      <td id="T_e7d42_row4_col2" class="data row4 col2" >52 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_726bf th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_726bf  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_726bf_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.2%, transparent 90.2%);
  font-family: Courier;
}
#T_726bf_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 65.4%, transparent 65.4%);
  font-family: Courier;
}
#T_726bf_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_726bf_row0_col3, #T_726bf_row2_col2, #T_726bf_row2_col3, #T_726bf_row3_col1, #T_726bf_row3_col2, #T_726bf_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_726bf_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 83.8%, transparent 83.8%);
  font-family: Courier;
}
#T_726bf_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.0%, transparent 6.0%);
  font-family: Courier;
}
#T_726bf_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_726bf_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_726bf_row1_col3, #T_726bf_row4_col0, #T_726bf_row4_col1, #T_726bf_row4_col2, #T_726bf_row4_col3, #T_726bf_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_726bf_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_726bf_row2_col0, #T_726bf_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_726bf_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_726bf_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_726bf_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_726bf">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_726bf_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_726bf_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_726bf_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_726bf_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_726bf_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.01] Therapy phase</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_726bf_level0_row0" class="row_heading level0 row0" >Acute therapy</th>
      <td id="T_726bf_row0_col0" class="data row0 col0" >166 <span style="color: grey">(69.2%) </span></td>
      <td id="T_726bf_row0_col1" class="data row0 col1" >34 <span style="color: grey">(14.2%) </span></td>
      <td id="T_726bf_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_726bf_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_726bf_row0_col4" class="data row0 col4" >201 <span style="color: grey">(83.8%) </span></td>
    </tr>
    <tr>
      <th id="T_726bf_level0_row1" class="row_heading level0 row1" >Aftercare</th>
      <td id="T_726bf_row1_col0" class="data row1 col0" >11 <span style="color: grey">(4.6%) </span></td>
      <td id="T_726bf_row1_col1" class="data row1 col1" >16 <span style="color: grey">(6.7%) </span></td>
      <td id="T_726bf_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_726bf_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_726bf_row1_col4" class="data row1 col4" >30 <span style="color: grey">(12.5%) </span></td>
    </tr>
    <tr>
      <th id="T_726bf_level0_row2" class="row_heading level0 row2" >Long-term therapy</th>
      <td id="T_726bf_row2_col0" class="data row2 col0" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_726bf_row2_col1" class="data row2 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_726bf_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_726bf_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_726bf_row2_col4" class="data row2 col4" >8 <span style="color: grey">(3.3%) </span></td>
    </tr>
    <tr>
      <th id="T_726bf_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_726bf_row3_col0" class="data row3 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_726bf_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_726bf_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_726bf_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_726bf_row3_col4" class="data row3 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_726bf_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_726bf_row4_col0" class="data row4 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_726bf_row4_col1" class="data row4 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_726bf_row4_col2" class="data row4 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_726bf_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_726bf_row4_col4" class="data row4 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_2e3f0 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2e3f0  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2e3f0_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_2e3f0_row0_col1, #T_2e3f0_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_2e3f0_row0_col2, #T_2e3f0_row0_col3, #T_2e3f0_row1_col3, #T_2e3f0_row2_col0, #T_2e3f0_row2_col2, #T_2e3f0_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_2e3f0_row0_col4, #T_2e3f0_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_2e3f0_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_2e3f0_row1_col1, #T_2e3f0_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_2e3f0_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_2e3f0_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.7%, transparent 96.7%);
  font-family: Courier;
}
#T_2e3f0_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 73.1%, transparent 73.1%);
  font-family: Courier;
}
#T_2e3f0_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_2e3f0_row3_col3, #T_2e3f0_row4_col0, #T_2e3f0_row4_col1, #T_2e3f0_row4_col2, #T_2e3f0_row4_col3, #T_2e3f0_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_2e3f0_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.1%, transparent 91.1%);
  font-family: Courier;
}
</style>
<table id="T_2e3f0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_2e3f0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_2e3f0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_2e3f0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_2e3f0_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_2e3f0_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.02] Group size</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2e3f0_level0_row0" class="row_heading level0 row0" >Group 2-5</th>
      <td id="T_2e3f0_row0_col0" class="data row0 col0" >4 <span style="color: grey">(1.7%) </span></td>
      <td id="T_2e3f0_row0_col1" class="data row0 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_2e3f0_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2e3f0_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2e3f0_row0_col4" class="data row0 col4" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_2e3f0_level0_row1" class="row_heading level0 row1" >Group 5 to 10</th>
      <td id="T_2e3f0_row1_col0" class="data row1 col0" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_2e3f0_row1_col1" class="data row1 col1" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_2e3f0_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2e3f0_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2e3f0_row1_col4" class="data row1 col4" >9 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_2e3f0_level0_row2" class="row_heading level0 row2" >Group over 10</th>
      <td id="T_2e3f0_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2e3f0_row2_col1" class="data row2 col1" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_2e3f0_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2e3f0_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2e3f0_row2_col4" class="data row2 col4" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_2e3f0_level0_row3" class="row_heading level0 row3" >Individual</th>
      <td id="T_2e3f0_row3_col0" class="data row3 col0" >174 <span style="color: grey">(73.7%) </span></td>
      <td id="T_2e3f0_row3_col1" class="data row3 col1" >38 <span style="color: grey">(16.1%) </span></td>
      <td id="T_2e3f0_row3_col2" class="data row3 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_2e3f0_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2e3f0_row3_col4" class="data row3 col4" >215 <span style="color: grey">(91.1%) </span></td>
    </tr>
    <tr>
      <th id="T_2e3f0_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_2e3f0_row4_col0" class="data row4 col0" >180 <span style="color: grey">(76.3%) </span></td>
      <td id="T_2e3f0_row4_col1" class="data row4 col1" >52 <span style="color: grey">(22.0%) </span></td>
      <td id="T_2e3f0_row4_col2" class="data row4 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_2e3f0_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2e3f0_row4_col4" class="data row4 col4" >236 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_f3a25 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_f3a25  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_f3a25_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_f3a25_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.9%, transparent 27.9%);
  font-family: Courier;
}
#T_f3a25_row0_col2, #T_f3a25_row0_col3, #T_f3a25_row1_col2, #T_f3a25_row1_col3, #T_f3a25_row2_col2, #T_f3a25_row2_col3, #T_f3a25_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_f3a25_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.9%, transparent 14.9%);
  font-family: Courier;
}
#T_f3a25_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.8%, transparent 37.8%);
  font-family: Courier;
}
#T_f3a25_row1_col1, #T_f3a25_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.6%, transparent 25.6%);
  font-family: Courier;
}
#T_f3a25_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.4%, transparent 34.4%);
  font-family: Courier;
}
#T_f3a25_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.1%, transparent 31.1%);
  font-family: Courier;
}
#T_f3a25_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.2%, transparent 29.2%);
  font-family: Courier;
}
#T_f3a25_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.9%, transparent 16.9%);
  font-family: Courier;
}
#T_f3a25_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
#T_f3a25_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_f3a25_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.4%, transparent 16.4%);
  font-family: Courier;
}
#T_f3a25_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_f3a25_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.0%, transparent 7.0%);
  font-family: Courier;
}
#T_f3a25_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_f3a25_row4_col3, #T_f3a25_row5_col0, #T_f3a25_row5_col1, #T_f3a25_row5_col2, #T_f3a25_row5_col3, #T_f3a25_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_f3a25_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.1%, transparent 5.1%);
  font-family: Courier;
}
</style>
<table id="T_f3a25">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_f3a25_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_f3a25_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_f3a25_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_f3a25_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_f3a25_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_f3a25_level0_row0" class="row_heading level0 row0" >02 to 05 years</th>
      <td id="T_f3a25_row0_col0" class="data row0 col0" >17 <span style="color: grey">(8.7%) </span></td>
      <td id="T_f3a25_row0_col1" class="data row0 col1" >12 <span style="color: grey">(6.2%) </span></td>
      <td id="T_f3a25_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f3a25_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f3a25_row0_col4" class="data row0 col4" >29 <span style="color: grey">(14.9%) </span></td>
    </tr>
    <tr>
      <th id="T_f3a25_level0_row1" class="row_heading level0 row1" >06 to 09 years</th>
      <td id="T_f3a25_row1_col0" class="data row1 col0" >56 <span style="color: grey">(28.7%) </span></td>
      <td id="T_f3a25_row1_col1" class="data row1 col1" >11 <span style="color: grey">(5.6%) </span></td>
      <td id="T_f3a25_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f3a25_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f3a25_row1_col4" class="data row1 col4" >67 <span style="color: grey">(34.4%) </span></td>
    </tr>
    <tr>
      <th id="T_f3a25_level0_row2" class="row_heading level0 row2" >10 to 14 years</th>
      <td id="T_f3a25_row2_col0" class="data row2 col0" >46 <span style="color: grey">(23.6%) </span></td>
      <td id="T_f3a25_row2_col1" class="data row2 col1" >11 <span style="color: grey">(5.6%) </span></td>
      <td id="T_f3a25_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f3a25_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f3a25_row2_col4" class="data row2 col4" >57 <span style="color: grey">(29.2%) </span></td>
    </tr>
    <tr>
      <th id="T_f3a25_level0_row3" class="row_heading level0 row3" >15 to 18 years</th>
      <td id="T_f3a25_row3_col0" class="data row3 col0" >25 <span style="color: grey">(12.8%) </span></td>
      <td id="T_f3a25_row3_col1" class="data row3 col1" >6 <span style="color: grey">(3.1%) </span></td>
      <td id="T_f3a25_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_f3a25_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f3a25_row3_col4" class="data row3 col4" >32 <span style="color: grey">(16.4%) </span></td>
    </tr>
    <tr>
      <th id="T_f3a25_level0_row4" class="row_heading level0 row4" >18+ years</th>
      <td id="T_f3a25_row4_col0" class="data row4 col0" >4 <span style="color: grey">(2.1%) </span></td>
      <td id="T_f3a25_row4_col1" class="data row4 col1" >3 <span style="color: grey">(1.5%) </span></td>
      <td id="T_f3a25_row4_col2" class="data row4 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_f3a25_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_f3a25_row4_col4" class="data row4 col4" >10 <span style="color: grey">(5.1%) </span></td>
    </tr>
    <tr>
      <th id="T_f3a25_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_f3a25_row5_col0" class="data row5 col0" >148 <span style="color: grey">(75.9%) </span></td>
      <td id="T_f3a25_row5_col1" class="data row5 col1" >43 <span style="color: grey">(22.1%) </span></td>
      <td id="T_f3a25_row5_col2" class="data row5 col2" >3 <span style="color: grey">(1.5%) </span></td>
      <td id="T_f3a25_row5_col3" class="data row5 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_f3a25_row5_col4" class="data row5 col4" >195 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_3bc38 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3bc38  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3bc38_row0_col0, #T_3bc38_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.7%, transparent 96.7%);
  font-family: Courier;
}
#T_3bc38_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_3bc38_row0_col2, #T_3bc38_row0_col3, #T_3bc38_row2_col0, #T_3bc38_row2_col1, #T_3bc38_row2_col2, #T_3bc38_row2_col3, #T_3bc38_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_3bc38_row1_col0, #T_3bc38_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_3bc38_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_3bc38_row1_col2, #T_3bc38_row1_col3 {
  width: 10em;
  font-family: Courier;
}
</style>
<table id="T_3bc38">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_3bc38_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_3bc38_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_3bc38_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_3bc38_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_3bc38_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.04] Online</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3bc38_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_3bc38_row0_col0" class="data row0 col0" >177 <span style="color: grey">(74.1%) </span></td>
      <td id="T_3bc38_row0_col1" class="data row0 col1" >50 <span style="color: grey">(20.9%) </span></td>
      <td id="T_3bc38_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_3bc38_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_3bc38_row0_col4" class="data row0 col4" >231 <span style="color: grey">(96.7%) </span></td>
    </tr>
    <tr>
      <th id="T_3bc38_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_3bc38_row1_col0" class="data row1 col0" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_3bc38_row1_col1" class="data row1 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_3bc38_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_3bc38_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3bc38_row1_col4" class="data row1 col4" >8 <span style="color: grey">(3.3%) </span></td>
    </tr>
    <tr>
      <th id="T_3bc38_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_3bc38_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_3bc38_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_3bc38_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_3bc38_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_3bc38_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_444e0 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_444e0  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_444e0_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.3%, transparent 97.3%);
  font-family: Courier;
}
#T_444e0_row0_col1, #T_444e0_row0_col2, #T_444e0_row0_col3, #T_444e0_row2_col0, #T_444e0_row2_col1, #T_444e0_row2_col2, #T_444e0_row2_col3, #T_444e0_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_444e0_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.9%, transparent 97.9%);
  font-family: Courier;
}
#T_444e0_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_444e0_row1_col1, #T_444e0_row1_col2, #T_444e0_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_444e0_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
</style>
<table id="T_444e0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_444e0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_444e0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_444e0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_444e0_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_444e0_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.05] As part of testing</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_444e0_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_444e0_row0_col0" class="data row0 col0" >179 <span style="color: grey">(74.9%) </span></td>
      <td id="T_444e0_row0_col1" class="data row0 col1" >51 <span style="color: grey">(21.3%) </span></td>
      <td id="T_444e0_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_444e0_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_444e0_row0_col4" class="data row0 col4" >234 <span style="color: grey">(97.9%) </span></td>
    </tr>
    <tr>
      <th id="T_444e0_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_444e0_row1_col0" class="data row1 col0" >5 <span style="color: grey">(2.1%) </span></td>
      <td id="T_444e0_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_444e0_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_444e0_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_444e0_row1_col4" class="data row1 col4" >5 <span style="color: grey">(2.1%) </span></td>
    </tr>
    <tr>
      <th id="T_444e0_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_444e0_row2_col0" class="data row2 col0" >184 <span style="color: grey">(77.0%) </span></td>
      <td id="T_444e0_row2_col1" class="data row2 col1" >51 <span style="color: grey">(21.3%) </span></td>
      <td id="T_444e0_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_444e0_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_444e0_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_dd370 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dd370  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dd370_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_dd370_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_dd370_row0_col2, #T_dd370_row0_col3, #T_dd370_row1_col3, #T_dd370_row2_col2, #T_dd370_row2_col3, #T_dd370_row4_col2, #T_dd370_row4_col3, #T_dd370_row5_col1, #T_dd370_row5_col2, #T_dd370_row5_col3 {
  width: 10em;
  font-family: Courier;
}
#T_dd370_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_dd370_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.6%, transparent 37.6%);
  font-family: Courier;
}
#T_dd370_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 48.0%, transparent 48.0%);
  font-family: Courier;
}
#T_dd370_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_dd370_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.2%, transparent 40.2%);
  font-family: Courier;
}
#T_dd370_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.3%, transparent 25.3%);
  font-family: Courier;
}
#T_dd370_row2_col1, #T_dd370_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.0%, transparent 18.0%);
  font-family: Courier;
}
#T_dd370_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.2%, transparent 23.2%);
  font-family: Courier;
}
#T_dd370_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.1%, transparent 4.1%);
  font-family: Courier;
}
#T_dd370_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_dd370_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_dd370_row3_col3, #T_dd370_row6_col0, #T_dd370_row6_col1, #T_dd370_row6_col2, #T_dd370_row6_col3, #T_dd370_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_dd370_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_dd370_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.4%, transparent 29.4%);
  font-family: Courier;
}
#T_dd370_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.3%, transparent 26.3%);
  font-family: Courier;
}
#T_dd370_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_dd370_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_dd370">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_dd370_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_dd370_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_dd370_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_dd370_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_dd370_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.06] Setting</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_dd370_level0_row0" class="row_heading level0 row0" >At home (via telemedicine)</th>
      <td id="T_dd370_row0_col0" class="data row0 col0" >5 <span style="color: grey">(2.2%) </span></td>
      <td id="T_dd370_row0_col1" class="data row0 col1" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_dd370_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row0_col4" class="data row0 col4" >7 <span style="color: grey">(3.1%) </span></td>
    </tr>
    <tr>
      <th id="T_dd370_level0_row1" class="row_heading level0 row1" >Gym</th>
      <td id="T_dd370_row1_col0" class="data row1 col0" >64 <span style="color: grey">(28.6%) </span></td>
      <td id="T_dd370_row1_col1" class="data row1 col1" >24 <span style="color: grey">(10.7%) </span></td>
      <td id="T_dd370_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_dd370_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row1_col4" class="data row1 col4" >90 <span style="color: grey">(40.2%) </span></td>
    </tr>
    <tr>
      <th id="T_dd370_level0_row2" class="row_heading level0 row2" >Hospital corridor</th>
      <td id="T_dd370_row2_col0" class="data row2 col0" >43 <span style="color: grey">(19.2%) </span></td>
      <td id="T_dd370_row2_col1" class="data row2 col1" >9 <span style="color: grey">(4.0%) </span></td>
      <td id="T_dd370_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row2_col4" class="data row2 col4" >52 <span style="color: grey">(23.2%) </span></td>
    </tr>
    <tr>
      <th id="T_dd370_level0_row3" class="row_heading level0 row3" >Outside</th>
      <td id="T_dd370_row3_col0" class="data row3 col0" >7 <span style="color: grey">(3.1%) </span></td>
      <td id="T_dd370_row3_col1" class="data row3 col1" >6 <span style="color: grey">(2.7%) </span></td>
      <td id="T_dd370_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dd370_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dd370_row3_col4" class="data row3 col4" >15 <span style="color: grey">(6.7%) </span></td>
    </tr>
    <tr>
      <th id="T_dd370_level0_row4" class="row_heading level0 row4" >Patients room</th>
      <td id="T_dd370_row4_col0" class="data row4 col0" >50 <span style="color: grey">(22.3%) </span></td>
      <td id="T_dd370_row4_col1" class="data row4 col1" >9 <span style="color: grey">(4.0%) </span></td>
      <td id="T_dd370_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row4_col4" class="data row4 col4" >59 <span style="color: grey">(26.3%) </span></td>
    </tr>
    <tr>
      <th id="T_dd370_level0_row5" class="row_heading level0 row5" >Weiteres</th>
      <td id="T_dd370_row5_col0" class="data row5 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dd370_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dd370_row5_col4" class="data row5 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_dd370_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_dd370_row6_col0" class="data row6 col0" >170 <span style="color: grey">(75.9%) </span></td>
      <td id="T_dd370_row6_col1" class="data row6 col1" >50 <span style="color: grey">(22.3%) </span></td>
      <td id="T_dd370_row6_col2" class="data row6 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_dd370_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dd370_row6_col4" class="data row6 col4" >224 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_0d0f9 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0d0f9  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_0d0f9_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.6%, transparent 36.6%);
  font-family: Courier;
}
#T_0d0f9_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.3%, transparent 35.3%);
  font-family: Courier;
}
#T_0d0f9_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.0%, transparent 75.0%);
  font-family: Courier;
}
#T_0d0f9_row0_col3, #T_0d0f9_row7_col0, #T_0d0f9_row7_col1, #T_0d0f9_row7_col2, #T_0d0f9_row7_col3, #T_0d0f9_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_0d0f9_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.0%, transparent 37.0%);
  font-family: Courier;
}
#T_0d0f9_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.8%, transparent 21.8%);
  font-family: Courier;
}
#T_0d0f9_row1_col1, #T_0d0f9_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.6%, transparent 20.6%);
  font-family: Courier;
}
#T_0d0f9_row1_col2, #T_0d0f9_row1_col3, #T_0d0f9_row2_col2, #T_0d0f9_row2_col3, #T_0d0f9_row3_col2, #T_0d0f9_row3_col3, #T_0d0f9_row4_col1, #T_0d0f9_row4_col2, #T_0d0f9_row4_col3, #T_0d0f9_row5_col2, #T_0d0f9_row5_col3, #T_0d0f9_row6_col3 {
  width: 10em;
  font-family: Courier;
}
#T_0d0f9_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.2%, transparent 21.2%);
  font-family: Courier;
}
#T_0d0f9_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.7%, transparent 9.7%);
  font-family: Courier;
}
#T_0d0f9_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_0d0f9_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.4%, transparent 8.4%);
  font-family: Courier;
}
#T_0d0f9_row3_col0, #T_0d0f9_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.8%, transparent 11.8%);
  font-family: Courier;
}
#T_0d0f9_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.6%, transparent 11.6%);
  font-family: Courier;
}
#T_0d0f9_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_0d0f9_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_0d0f9_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_0d0f9_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.4%, transparent 7.4%);
  font-family: Courier;
}
#T_0d0f9_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.5%, transparent 3.5%);
  font-family: Courier;
}
#T_0d0f9_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.0%, transparent 16.0%);
  font-family: Courier;
}
#T_0d0f9_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_0d0f9_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.0%, transparent 17.0%);
  font-family: Courier;
}
</style>
<table id="T_0d0f9">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_0d0f9_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_0d0f9_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_0d0f9_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_0d0f9_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_0d0f9_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.07] Main motor skill</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_0d0f9_level0_row0" class="row_heading level0 row0" >Coordination</th>
      <td id="T_0d0f9_row0_col0" class="data row0 col0" >87 <span style="color: grey">(28.0%) </span></td>
      <td id="T_0d0f9_row0_col1" class="data row0 col1" >24 <span style="color: grey">(7.7%) </span></td>
      <td id="T_0d0f9_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.0%) </span></td>
      <td id="T_0d0f9_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_0d0f9_row0_col4" class="data row0 col4" >115 <span style="color: grey">(37.0%) </span></td>
    </tr>
    <tr>
      <th id="T_0d0f9_level0_row1" class="row_heading level0 row1" >Endurance</th>
      <td id="T_0d0f9_row1_col0" class="data row1 col0" >52 <span style="color: grey">(16.7%) </span></td>
      <td id="T_0d0f9_row1_col1" class="data row1 col1" >14 <span style="color: grey">(4.5%) </span></td>
      <td id="T_0d0f9_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row1_col4" class="data row1 col4" >66 <span style="color: grey">(21.2%) </span></td>
    </tr>
    <tr>
      <th id="T_0d0f9_level0_row2" class="row_heading level0 row2" >Flexibility</th>
      <td id="T_0d0f9_row2_col0" class="data row2 col0" >23 <span style="color: grey">(7.4%) </span></td>
      <td id="T_0d0f9_row2_col1" class="data row2 col1" >3 <span style="color: grey">(1.0%) </span></td>
      <td id="T_0d0f9_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row2_col4" class="data row2 col4" >26 <span style="color: grey">(8.4%) </span></td>
    </tr>
    <tr>
      <th id="T_0d0f9_level0_row3" class="row_heading level0 row3" >Full body</th>
      <td id="T_0d0f9_row3_col0" class="data row3 col0" >28 <span style="color: grey">(9.0%) </span></td>
      <td id="T_0d0f9_row3_col1" class="data row3 col1" >8 <span style="color: grey">(2.6%) </span></td>
      <td id="T_0d0f9_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row3_col4" class="data row3 col4" >36 <span style="color: grey">(11.6%) </span></td>
    </tr>
    <tr>
      <th id="T_0d0f9_level0_row4" class="row_heading level0 row4" >Relaxation</th>
      <td id="T_0d0f9_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_0d0f9_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row4_col4" class="data row4 col4" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_0d0f9_level0_row5" class="row_heading level0 row5" >Speed</th>
      <td id="T_0d0f9_row5_col0" class="data row5 col0" >6 <span style="color: grey">(1.9%) </span></td>
      <td id="T_0d0f9_row5_col1" class="data row5 col1" >5 <span style="color: grey">(1.6%) </span></td>
      <td id="T_0d0f9_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row5_col4" class="data row5 col4" >11 <span style="color: grey">(3.5%) </span></td>
    </tr>
    <tr>
      <th id="T_0d0f9_level0_row6" class="row_heading level0 row6" >Strength</th>
      <td id="T_0d0f9_row6_col0" class="data row6 col0" >38 <span style="color: grey">(12.2%) </span></td>
      <td id="T_0d0f9_row6_col1" class="data row6 col1" >14 <span style="color: grey">(4.5%) </span></td>
      <td id="T_0d0f9_row6_col2" class="data row6 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_0d0f9_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_0d0f9_row6_col4" class="data row6 col4" >53 <span style="color: grey">(17.0%) </span></td>
    </tr>
    <tr>
      <th id="T_0d0f9_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_0d0f9_row7_col0" class="data row7 col0" >238 <span style="color: grey">(76.5%) </span></td>
      <td id="T_0d0f9_row7_col1" class="data row7 col1" >68 <span style="color: grey">(21.9%) </span></td>
      <td id="T_0d0f9_row7_col2" class="data row7 col2" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_0d0f9_row7_col3" class="data row7 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_0d0f9_row7_col4" class="data row7 col4" >311 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_cb408 th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cb408  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cb408_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.3%, transparent 47.3%);
  font-family: Courier;
}
#T_cb408_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_cb408_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_cb408_row0_col3, #T_cb408_row2_col0, #T_cb408_row2_col2, #T_cb408_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_cb408_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.6%, transparent 40.6%);
  font-family: Courier;
}
#T_cb408_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.7%, transparent 52.7%);
  font-family: Courier;
}
#T_cb408_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.0%, transparent 81.0%);
  font-family: Courier;
}
#T_cb408_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_cb408_row1_col3, #T_cb408_row3_col0, #T_cb408_row3_col1, #T_cb408_row3_col2, #T_cb408_row3_col3, #T_cb408_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_cb408_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.9%, transparent 58.9%);
  font-family: Courier;
}
#T_cb408_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_cb408_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_cb408">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_cb408_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_cb408_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_cb408_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_cb408_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_cb408_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.08] Time point</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_cb408_level0_row0" class="row_heading level0 row0" >1. Time point</th>
      <td id="T_cb408_row0_col0" class="data row0 col0" >69 <span style="color: grey">(35.9%) </span></td>
      <td id="T_cb408_row0_col1" class="data row0 col1" >7 <span style="color: grey">(3.6%) </span></td>
      <td id="T_cb408_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_cb408_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cb408_row0_col4" class="data row0 col4" >78 <span style="color: grey">(40.6%) </span></td>
    </tr>
    <tr>
      <th id="T_cb408_level0_row1" class="row_heading level0 row1" >2. Time point</th>
      <td id="T_cb408_row1_col0" class="data row1 col0" >77 <span style="color: grey">(40.1%) </span></td>
      <td id="T_cb408_row1_col1" class="data row1 col1" >34 <span style="color: grey">(17.7%) </span></td>
      <td id="T_cb408_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_cb408_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_cb408_row1_col4" class="data row1 col4" >113 <span style="color: grey">(58.9%) </span></td>
    </tr>
    <tr>
      <th id="T_cb408_level0_row2" class="row_heading level0 row2" >Nach Abschluß der Therapie</th>
      <td id="T_cb408_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_cb408_row2_col1" class="data row2 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_cb408_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cb408_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cb408_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_cb408_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_cb408_row3_col0" class="data row3 col0" >146 <span style="color: grey">(76.0%) </span></td>
      <td id="T_cb408_row3_col1" class="data row3 col1" >42 <span style="color: grey">(21.9%) </span></td>
      <td id="T_cb408_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_cb408_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_cb408_row3_col4" class="data row3 col4" >192 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_b06ec th:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_b06ec  td:first-child {
  min-width: 400px !important;
  max-width: 400px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_b06ec_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.6%, transparent 27.6%);
  font-family: Courier;
}
#T_b06ec_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_b06ec_row0_col2, #T_b06ec_row1_col2, #T_b06ec_row1_col3, #T_b06ec_row2_col3, #T_b06ec_row3_col1, #T_b06ec_row3_col2, #T_b06ec_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_b06ec_row0_col3, #T_b06ec_row2_col2, #T_b06ec_row4_col0, #T_b06ec_row4_col1, #T_b06ec_row4_col2, #T_b06ec_row4_col3, #T_b06ec_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_b06ec_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.2%, transparent 28.2%);
  font-family: Courier;
}
#T_b06ec_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.9%, transparent 15.9%);
  font-family: Courier;
}
#T_b06ec_row1_col1, #T_b06ec_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_b06ec_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 54.5%, transparent 54.5%);
  font-family: Courier;
}
#T_b06ec_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 53.8%, transparent 53.8%);
  font-family: Courier;
}
#T_b06ec_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 54.8%, transparent 54.8%);
  font-family: Courier;
}
#T_b06ec_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
#T_b06ec_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
</style>
<table id="T_b06ec">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_b06ec_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_b06ec_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_b06ec_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_b06ec_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_b06ec_level0_col4" class="col_heading level0 col4" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.09] Training condition</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_b06ec_level0_row0" class="row_heading level0 row0" >Average</th>
      <td id="T_b06ec_row0_col0" class="data row0 col0" >40 <span style="color: grey">(21.3%) </span></td>
      <td id="T_b06ec_row0_col1" class="data row0 col1" >12 <span style="color: grey">(6.4%) </span></td>
      <td id="T_b06ec_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_b06ec_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_b06ec_row0_col4" class="data row0 col4" >53 <span style="color: grey">(28.2%) </span></td>
    </tr>
    <tr>
      <th id="T_b06ec_level0_row1" class="row_heading level0 row1" >Good</th>
      <td id="T_b06ec_row1_col0" class="data row1 col0" >23 <span style="color: grey">(12.2%) </span></td>
      <td id="T_b06ec_row1_col1" class="data row1 col1" >6 <span style="color: grey">(3.2%) </span></td>
      <td id="T_b06ec_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_b06ec_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_b06ec_row1_col4" class="data row1 col4" >29 <span style="color: grey">(15.4%) </span></td>
    </tr>
    <tr>
      <th id="T_b06ec_level0_row2" class="row_heading level0 row2" >Moderate</th>
      <td id="T_b06ec_row2_col0" class="data row2 col0" >79 <span style="color: grey">(42.0%) </span></td>
      <td id="T_b06ec_row2_col1" class="data row2 col1" >21 <span style="color: grey">(11.2%) </span></td>
      <td id="T_b06ec_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_b06ec_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_b06ec_row2_col4" class="data row2 col4" >103 <span style="color: grey">(54.8%) </span></td>
    </tr>
    <tr>
      <th id="T_b06ec_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_b06ec_row3_col0" class="data row3 col0" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_b06ec_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_b06ec_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_b06ec_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_b06ec_row3_col4" class="data row3 col4" >3 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_b06ec_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_b06ec_row4_col0" class="data row4 col0" >145 <span style="color: grey">(77.1%) </span></td>
      <td id="T_b06ec_row4_col1" class="data row4 col1" >39 <span style="color: grey">(20.7%) </span></td>
      <td id="T_b06ec_row4_col2" class="data row4 col2" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_b06ec_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_b06ec_row4_col4" class="data row4 col4" >188 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



## pie charts

    [05.03] Age




    [05.01] Therapy phase




    [05.09] Training condition




    [02.02] Type




    [02.03] Trigger




    [02.04] Affected body parts




    [05.07] Main motor skill




    [05.06] Setting




    [05.02] Group size



