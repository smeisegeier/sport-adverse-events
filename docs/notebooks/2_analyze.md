# <a id='toc1_'></a>[analyze data](#toc0_)

**Table of contents**<a id='toc0_'></a>    
- [analyze data](#toc1_)    
  - [condensed data](#toc1_1_)    
  - [🕹️ interactive](#toc1_2_)    
  - [descriptive stats](#toc1_3_)    
    - [full data](#toc1_3_1_)    
    - [only `Exercise-related`](#toc1_3_2_)    
  - [slides](#toc1_4_)    
    - [slide 1](#toc1_4_1_)    
    - [slide 2](#toc1_4_2_)    
    - [slide 3](#toc1_4_3_)    
    - [slide 4](#toc1_4_4_)    
    - [slide 5](#toc1_4_5_)    
    - [slide 6](#toc1_4_6_)    
    - [slide 7](#toc1_4_7_)    
    - [slide 8](#toc1_4_8_)    
    - [slide 9](#toc1_4_9_)    
    - [slide 10](#toc1_4_10_)    
    - [bonus - ci](#toc1_4_11_)    
  - [2025-03-18](#toc1_5_)    
  - [chi-square](#toc1_6_)    
  - [export data](#toc1_7_)    
  - [2025-05-26 diagrams](#toc1_8_)    
  - [2025-07-29 kombinationen](#toc1_9_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

    🐍 3.12.9 | 📦 pygwalker: 0.4.9.15 | 📦 pandas: 2.3.1 | 📦 numpy: 1.26.4 | 📦 duckdb: 1.3.2 | 📦 pandas-plots: 0.15.13 | 📦 connection-helper: 0.12.1


## <a id='toc1_1_'></a>[condensed data](#toc0_)
- defined columns have been transformed

    🔵 *** df: condensed ***  
    🟣 shape: (243, 38) columns: ['[01.01] CTCAE' '[01.02] Date' '[01.03] Exercise-related'
     '[02.01] CreatedOn' '[02.02] Type' '[02.03] Trigger'
     '[02.04] Affected body parts' '[03.01] Pain'
     '[03.02] With hospitalization' '[03.03] Medical follow-up treatment'
     '[03.04] With delayed therapy protocol'
     '[03.05] Life-saving intervention' '[03.06] Increased care needs'
     '[03.07] With medication administration' '[03.08.01] Affected person'
     '[03.08] Occurrence of fear and uncertainty'
     '[03.09] Structural adjustment' '[03.10.01] Approver'
     '[03.10.02] OK to proceed'
     '[03.10] Assessment of the situation by expertise'
     '[03.11] Application RICE rule (Rest, Ice, Compression, Elevation)'
     '[03.12] With observation' '[03.13.01] Stop or Break' '[03.13] Stop'
     '[03.14.01] Adaptations intensity' '[03.14.02] Adaptations duration'
     '[03.14] Adaptations' '[03.16] Death' '[05.01] Therapy phase'
     '[05.02] Group size' '[05.03] Age' '[05.04] Online'
     '[05.05] As part of testing' '[05.06] Setting' '[05.07] Main motor skill'
     '[05.08] Time point' '[05.09] Training condition'
     '[06.01] Trigger Freetext']  
    🟣 duplicates: 0  
    🟣 uniques: [{01.01 CTCAE: 4 01.02 Date: 2 01.03 Exercise-related: 2 02.01 CreatedOn: 173 02.02  
    Type: 35 02.03 Trigger: 30 02.04 Affected body parts: 23 03.01 Pain: 2 03.02 With hospitalization:  
    3 03.03 Medical follow-up treatment: 3 03.04 With delayed therapy protocol: 1 03.05  
    Life-saving intervention: 1 03.06 Increased care needs: 2 03.07 With medication administration:  
    3 03.08.01 Affected person: 11 03.08 Occurrence of fear and uncertainty: 2 03.09 Structural  
    adjustment: 3 03.10.01 Approver: 7 03.10.02 OK to proceed: 1 03.10 Assessment of the  
    situation by expertise: 1 03.11 Application RICE rule (Rest Ice Compression Elevation):  
    2 03.12 With observation: 3 03.13.01 Stop or Break: 3 03.13 Stop: 2 03.14.01 Adaptations  
    intensity: 12 03.14.02 Adaptations duration: 4 03.14 Adaptations: 1 03.16 Death:  
    1 05.01 Therapy phase: 4 05.02 Group size: 4 05.03 Age: 5 05.04 Online: 2 05.05 As part  
    of testing: 2 05.06 Setting: 6 05.07 Main motor skill: 18 05.08 Time point: 3 05.09 Training  
    condition: 5 06.01 Trigger Freetext: 239}]  
    🟣 missings: [{01.01 CTCAE: 3 01.02 Date: 0 01.03 Exercise-related: 1 02.01 CreatedOn: 0 02.02 Type:  
    0 02.03 Trigger: 0 02.04 Affected body parts: 1 03.01 Pain: 0 03.02 With hospitalization:  
    0 03.03 Medical follow-up treatment: 0 03.04 With delayed therapy protocol: 1 03.05  
    Life-saving intervention: 1 03.06 Increased care needs: 0 03.07 With medication administration:  
    6 03.08.01 Affected person: 165 03.08 Occurrence of fear and uncertainty: 2 03.09 Structural  
    adjustment: 1 03.10.01 Approver: 0 03.10.02 OK to proceed: 0 03.10 Assessment of the  
    situation by expertise: 0 03.11 Application RICE rule (Rest Ice Compression Elevation):  
    1 03.12 With observation: 0 03.13.01 Stop or Break: 25 03.13 Stop: 0 03.14.01 Adaptations  
    intensity: 191 03.14.02 Adaptations duration: 191 03.14 Adaptations: 0 03.16 Death:  
    0 05.01 Therapy phase: 0 05.02 Group size: 4 05.03 Age: 45 05.04 Online: 1 05.05 As part  
    of testing: 1 05.06 Setting: 16 05.07 Main motor skill: 13 05.08 Time point: 48 05.09  
    Training condition: 54 06.01 Trigger Freetext: 4}]  
    --- column uniques (all)  
    🟠 index [0, 1, 2, 3, 4,]  
    🟠 [01.01] CTCAE(5|object)   ['1', '2', '3', '4', '<NA>',]  
    🟠 [01.02] Date(2|object)   ['Already present', 'First occurrence',]  
    🟠 [01.03] Exercise-related(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [02.01] CreatedOn(173|object)   ['2021-01-11', '2021-01-12', '2021-01-18', '2021-02-01', '2021-02-19',]  
    🟠 [02.02] Type(35|object)   ['Bone injuries', 'Circulatory problems', 'Circulatory problems|Muscle cramps',  
    'Circulatory problems|Psychological stress reaction', 'Circulatory problems|Severe exhaustion',]  
    🟠 [02.03] Trigger(30|object)   ['Coordination problems', 'Coordination problems|Kollision', 'Environmental conditions',  
    'Environmental conditions|Kollision', 'Kollision',]  
    🟠 [02.04] Affected body parts(24|object)   ['<NA>', 'Abdomen', 'Abdomen|Coccyx', 'Abdomen|Intestine', 'Back',]  
    🟠 [03.01] Pain(2|object)   ['Ja', 'Nein',]  
    🟠 [03.02] With hospitalization(3|object)   ['No', 'Weiß nicht', 'Yes',]  
    🟠 [03.03] Medical follow-up treatment(3|object)   ['No', 'Weiß nicht', 'Yes',]  
    🟠 [03.04] With delayed therapy protocol(2|object)   ['<NA>', 'No',]  
    🟠 [03.05] Life-saving intervention(2|object)   ['<NA>', 'No',]  
    🟠 [03.06] Increased care needs(2|object)   ['No', 'Yes',]  
    🟠 [03.07] With medication administration(4|object)   ['<NA>', 'No', 'Weiß nicht', 'Yes',]  
    🟠 [03.08.01] Affected person(12|object)   ['<NA>', 'For affected individuals', 'For affected individuals|BeIn the treatment team',  
    'For affected individuals|BeIn the treatment team|For the excercise experts',  
    'For affected individuals|BeIn the treatment team|Mit der Ablehnung weiterer sporttherapheutischer Angebote',]  
    🟠 [03.08] Occurrence of fear and uncertainty(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.09] Structural adjustment(4|object)   ['<NA>', 'Ja', 'Nein', 'Weiß nicht',]  
    🟠 [03.10.01] Approver(7|object)   ['-', 'Eltern', 'Medizin', 'Medizin|Psychosozialer Dienst', 'Pflege',]  
    🟠 [03.10.02] OK to proceed(1|object)   ['-',]  
    🟠 [03.10] Assessment of the situation by expertise(1|object)   ['nan',]  
    🟠 [03.11] Application RICE rule (Rest, Ice, Compression, Elevation)(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.12] With observation(3|object)   ['Ja', 'Nein', 'U',]  
    🟠 [03.13.01] Stop or Break(4|object)   ['<NA>', 'Break', 'Cessation', 'Einheit war sowieso vorbei',]  
    🟠 [03.13] Stop(2|object)   ['No', 'Yes',]  
    🟠 [03.14.01] Adaptations intensity(13|object)   ['<NA>', 'Communication strategy', 'Equipment', 'Equipment|Communication strategy',  
    'Exercise selection',]  
    🟠 [03.14.02] Adaptations duration(5|object)   ['<NA>', 'Ab jetzt für alle Bewegungseinheiten mit allen Patient*innen',  
    'Für die gesamte Therapiephase', 'Für die nächsten Einheiten (da das AE rückwirkend auftrat',  
    'Nur für diese Einheit',]  
    🟠 [03.14] Adaptations(1|object)   ['-',]  
    🟠 [03.16] Death(1|object)   ['No',]  
    🟠 [05.01] Therapy phase(4|object)   ['Acute therapy', 'Aftercare', 'Long-term therapy', 'Weiß nicht',]  
    🟠 [05.02] Group size(5|object)   ['<NA>', 'Group 2-5', 'Group 5 to 10', 'Group over 10', 'Individual',]  
    🟠 [05.03] Age(6|object)   ['02 to 05 years', '06 to 09 years', '10 to 14 years', '15 to 18 years', '18+ years',]  
    🟠 [05.04] Online(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [05.05] As part of testing(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [05.06] Setting(7|object)   ['<NA>', 'At home (via telemedicine)', 'Gym', 'Hospital corridor', 'Outside',]  
    🟠 [05.07] Main motor skill(19|object)   ['<NA>', 'Coordination', 'Coordination|Speed', 'Coordination|Strength', 'Endurance',]  
    🟠 [05.08] Time point(4|object)   ['1. Time point', '2. Time point', '<NA>', 'Nach Abschluß der Therapie',]  
    🟠 [05.09] Training condition(6|object)   ['<NA>', 'Average', 'Average|Moderate', 'Good', 'Moderate',]  
    🟠 [06.01] Trigger Freetext(240|object)   [' -	Niedrigintensive, kraftorientierte Trainingseinheit UEx (Einzeltraining im Stationszimmer)  -	Kind entwickelt Bauchkrämpfe (Schmerzskala 5-6) nach ca. 15min, möchte sich daraufhin lieber wieder hinlegen; Stundenabbruch aber sonst keine direkten Konsequenzen  -	Beschwerden wurden zuvor nicht angegeben, sind also im Verlauf der Einheit neu aufgetreten, aber fraglich, ob durch Sport induziert - kein konkreter Auslöser ersichtlich  -	Kind hatte später am Tag einen Krampfanfall, vermutlich durch therapiebedingte Hirnvolumenminderung ohne Zusammenhang mit Sport  ',  
    '15-Jähriger pat mit Keimzelltumor: 10min radergometer, anschließend Ringefangen- und Werfen; dann Schwindel und Kreislaufbeschwerden',  
    '2. Einheit am Tag (Hanteltraining) und anschließendes plötzliches Übergeben; zum Schluss gab es eine Rotationsübung (Sitzend an der Bettkante und Oberkörper von rechts nach links bewegend) und daraufhin passierte es ',  
    '5 min leichtes Fahrradfahren, bei anschließenden Ballspiel kam es zu starken Kopfschmerzen (Kopfschmerz Leitsymptom des Patienten in der Therapie)',  
    '8 min leichtes Fahrradfahren, Kräftigung Oberkörper mit Hanteln - Schwindel  ',]  
    --- column stats (numeric)  



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>[01.01] CTCAE</th>
      <th>[01.02] Date</th>
      <th>[01.03] Exercise-related</th>
      <th>[02.01] CreatedOn</th>
      <th>[02.02] Type</th>
      <th>[02.03] Trigger</th>
      <th>[02.04] Affected body parts</th>
      <th>[03.01] Pain</th>
      <th>[03.02] With hospitalization</th>
      <th>[03.03] Medical follow-up treatment</th>
      <th>...</th>
      <th>[05.01] Therapy phase</th>
      <th>[05.02] Group size</th>
      <th>[05.03] Age</th>
      <th>[05.04] Online</th>
      <th>[05.05] As part of testing</th>
      <th>[05.06] Setting</th>
      <th>[05.07] Main motor skill</th>
      <th>[05.08] Time point</th>
      <th>[05.09] Training condition</th>
      <th>[06.01] Trigger Freetext</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Already present</td>
      <td>No</td>
      <td>2022-10-01</td>
      <td>Übelkeit / Erbrechen</td>
      <td>Physical strain|Medical therapy</td>
      <td>Innere Medizin</td>
      <td>Nein</td>
      <td>No</td>
      <td>No</td>
      <td>...</td>
      <td>Acute therapy</td>
      <td>Individual</td>
      <td>10 to 14 years</td>
      <td>No</td>
      <td>No</td>
      <td>Hospital corridor</td>
      <td>Coordination</td>
      <td>2. Time point</td>
      <td>Average</td>
      <td>Beim moderaten Tischtennisspielen wurde der Pa...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>First occurrence</td>
      <td>Yes</td>
      <td>2022-10-01</td>
      <td>Pain</td>
      <td>Coordination problems</td>
      <td>Back|Buttocks</td>
      <td>Ja</td>
      <td>No</td>
      <td>No</td>
      <td>...</td>
      <td>Acute therapy</td>
      <td>Individual</td>
      <td>06 to 09 years</td>
      <td>No</td>
      <td>No</td>
      <td>Hospital corridor</td>
      <td>Coordination</td>
      <td>1. Time point</td>
      <td>Good</td>
      <td>Luftballonspiel im Stehen; Kind hat sich gestr...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Already present</td>
      <td>No</td>
      <td>2022-11-01</td>
      <td>Circulatory problems</td>
      <td>Medical therapy</td>
      <td>Innere Medizin</td>
      <td>Nein</td>
      <td>No</td>
      <td>Yes</td>
      <td>...</td>
      <td>Acute therapy</td>
      <td>Individual</td>
      <td>10 to 14 years</td>
      <td>No</td>
      <td>No</td>
      <td>Patients room</td>
      <td>Coordination</td>
      <td>2. Time point</td>
      <td>Moderate</td>
      <td>Beim leichter Mobilisation und Aktivierung hat...</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 38 columns</p>
</div>



    
![svg](2_analyze_files/output_4_2.svg)
    



    
![png](2_analyze_files/output_4_3.png)
    


## <a id='toc1_2_'></a>[🕹️ interactive](#toc0_)

## <a id='toc1_3_'></a>[descriptive stats](#toc0_)




    ['[01.01] CTCAE',
     '[01.02] Date',
     '[01.03] Exercise-related',
     '[02.02] Type',
     '[02.03] Trigger',
     '[02.04] Affected body parts',
     '[03.02] With hospitalization',
     '[03.03] Medical follow-up treatment',
     '[03.04] With delayed therapy protocol',
     '[03.06] Increased care needs',
     '[03.07] With medication administration',
     '[03.08] Occurrence of fear and uncertainty',
     '[03.08.01] Affected person',
     '[03.09] Structural adjustment',
     '[03.10] Assessment of the situation by expertise',
     '[03.10.01] Approver',
     '[03.11] Application RICE rule (Rest, Ice, Compression, Elevation)',
     '[03.12] With observation',
     '[03.13] Stop',
     '[03.13.01] Stop or Break',
     '[03.14] Adaptations',
     '[03.14.01] Adaptations intensity',
     '[03.14.02] Adaptations duration',
     '[05.01] Therapy phase',
     '[05.02] Group size',
     '[05.03] Age',
     '[05.04] Online',
     '[05.05] As part of testing',
     '[05.06] Setting',
     '[05.07] Main motor skill',
     '[05.08] Time point',
     '[05.09] Training condition']



### <a id='toc1_3_1_'></a>[full data](#toc0_)


<style type="text/css">
#T_4557f th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_4557f  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_4557f_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.8%, transparent 22.8%);
  font-family: Courier;
}
#T_4557f_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_4557f_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_4557f_row0_col3 {
  width: 10em;
  font-family: Courier;
}
#T_4557f_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.2%, transparent 21.2%);
  font-family: Courier;
}
#T_4557f_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 77.2%, transparent 77.2%);
  font-family: Courier;
}
#T_4557f_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 84.6%, transparent 84.6%);
  font-family: Courier;
}
#T_4557f_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_4557f_row1_col3, #T_4557f_row2_col0, #T_4557f_row2_col1, #T_4557f_row2_col2, #T_4557f_row2_col3, #T_4557f_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_4557f_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 78.8%, transparent 78.8%);
  font-family: Courier;
}
</style>
<table id="T_4557f">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_4557f_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_4557f_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_4557f_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_4557f_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_4557f_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_4557f_level0_row0" class="row_heading level0 row0" >Already present</th>
      <td id="T_4557f_row0_col0" class="data row0 col0" >42 <span style="color: grey">(17.5%) </span></td>
      <td id="T_4557f_row0_col1" class="data row0 col1" >8 <span style="color: grey">(3.3%) </span></td>
      <td id="T_4557f_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_4557f_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_4557f_row0_col4" class="data row0 col4" >51 <span style="color: grey">(21.2%) </span></td>
    </tr>
    <tr>
      <th id="T_4557f_level0_row1" class="row_heading level0 row1" >First occurrence</th>
      <td id="T_4557f_row1_col0" class="data row1 col0" >142 <span style="color: grey">(59.2%) </span></td>
      <td id="T_4557f_row1_col1" class="data row1 col1" >44 <span style="color: grey">(18.3%) </span></td>
      <td id="T_4557f_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_4557f_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_4557f_row1_col4" class="data row1 col4" >189 <span style="color: grey">(78.8%) </span></td>
    </tr>
    <tr>
      <th id="T_4557f_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_4557f_row2_col0" class="data row2 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_4557f_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_4557f_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_4557f_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_4557f_row2_col4" class="data row2 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_197b6 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_197b6  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_197b6_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_197b6_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.5%, transparent 13.5%);
  font-family: Courier;
}
#T_197b6_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_197b6_row0_col3 {
  width: 10em;
  font-family: Courier;
}
#T_197b6_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.6%, transparent 12.6%);
  font-family: Courier;
}
#T_197b6_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 88.0%, transparent 88.0%);
  font-family: Courier;
}
#T_197b6_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.5%, transparent 86.5%);
  font-family: Courier;
}
#T_197b6_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_197b6_row1_col3, #T_197b6_row2_col0, #T_197b6_row2_col1, #T_197b6_row2_col2, #T_197b6_row2_col3, #T_197b6_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_197b6_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 87.4%, transparent 87.4%);
  font-family: Courier;
}
</style>
<table id="T_197b6">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_197b6_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_197b6_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_197b6_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_197b6_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_197b6_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_197b6_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_197b6_row0_col0" class="data row0 col0" >22 <span style="color: grey">(9.2%) </span></td>
      <td id="T_197b6_row0_col1" class="data row0 col1" >7 <span style="color: grey">(2.9%) </span></td>
      <td id="T_197b6_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_197b6_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_197b6_row0_col4" class="data row0 col4" >30 <span style="color: grey">(12.6%) </span></td>
    </tr>
    <tr>
      <th id="T_197b6_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_197b6_row1_col0" class="data row1 col0" >161 <span style="color: grey">(67.4%) </span></td>
      <td id="T_197b6_row1_col1" class="data row1 col1" >45 <span style="color: grey">(18.8%) </span></td>
      <td id="T_197b6_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_197b6_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_197b6_row1_col4" class="data row1 col4" >209 <span style="color: grey">(87.4%) </span></td>
    </tr>
    <tr>
      <th id="T_197b6_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_197b6_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_197b6_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_197b6_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_197b6_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_197b6_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_c2707 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c2707  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c2707_row0_col0, #T_c2707_row0_col1, #T_c2707_row0_col3, #T_c2707_row1_col2, #T_c2707_row1_col3, #T_c2707_row2_col1, #T_c2707_row2_col2, #T_c2707_row2_col3, #T_c2707_row3_col1, #T_c2707_row3_col2, #T_c2707_row3_col3, #T_c2707_row4_col2, #T_c2707_row4_col3, #T_c2707_row5_col1, #T_c2707_row5_col2, #T_c2707_row5_col3, #T_c2707_row6_col2, #T_c2707_row6_col3, #T_c2707_row7_col2, #T_c2707_row7_col3, #T_c2707_row9_col2, #T_c2707_row9_col3, #T_c2707_row10_col1, #T_c2707_row10_col2, #T_c2707_row10_col3, #T_c2707_row11_col1, #T_c2707_row11_col2, #T_c2707_row11_col3, #T_c2707_row12_col2, #T_c2707_row12_col3, #T_c2707_row13_col2, #T_c2707_row14_col2, #T_c2707_row14_col3 {
  width: 10em;
  font-family: Courier;
}
#T_c2707_row0_col2, #T_c2707_row8_col2, #T_c2707_row8_col3, #T_c2707_row13_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_c2707_row0_col4, #T_c2707_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_c2707_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.4%, transparent 16.4%);
  font-family: Courier;
}
#T_c2707_row1_col1, #T_c2707_row6_col1, #T_c2707_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_c2707_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_c2707_row2_col0, #T_c2707_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_c2707_row2_col4, #T_c2707_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_c2707_row3_col0, #T_c2707_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_c2707_row4_col0, #T_c2707_row10_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_c2707_row4_col1, #T_c2707_row5_col0, #T_c2707_row7_col1, #T_c2707_row9_col1, #T_c2707_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_c2707_row5_col4, #T_c2707_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_c2707_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_c2707_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.1%, transparent 39.1%);
  font-family: Courier;
}
#T_c2707_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.7%, transparent 50.7%);
  font-family: Courier;
}
#T_c2707_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.2%, transparent 42.2%);
  font-family: Courier;
}
#T_c2707_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_c2707_row9_col4, #T_c2707_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_c2707_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_c2707_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_c2707_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_c2707_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_c2707_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.7%, transparent 22.7%);
  font-family: Courier;
}
#T_c2707_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.2%, transparent 8.2%);
  font-family: Courier;
}
#T_c2707_row14_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.6%, transparent 19.6%);
  font-family: Courier;
}
#T_c2707_row14_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_c2707_row14_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
#T_c2707_row15_col0, #T_c2707_row15_col1, #T_c2707_row15_col2, #T_c2707_row15_col3, #T_c2707_row15_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_c2707">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_c2707_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_c2707_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_c2707_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_c2707_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_c2707_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_c2707_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_c2707_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_c2707_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row0_col4" class="data row0 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_c2707_row1_col0" class="data row1 col0" >37 <span style="color: grey">(12.1%) </span></td>
      <td id="T_c2707_row1_col1" class="data row1 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_c2707_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row1_col4" class="data row1 col4" >39 <span style="color: grey">(12.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_c2707_row2_col0" class="data row2 col0" >5 <span style="color: grey">(1.6%) </span></td>
      <td id="T_c2707_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row2_col4" class="data row2 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_c2707_row3_col0" class="data row3 col0" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_c2707_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row3_col4" class="data row3 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_c2707_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_c2707_row4_col1" class="data row4 col1" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_c2707_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row4_col4" class="data row4 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_c2707_row5_col0" class="data row5 col0" >3 <span style="color: grey">(1.0%) </span></td>
      <td id="T_c2707_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row5_col4" class="data row5 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_c2707_row6_col0" class="data row6 col0" >5 <span style="color: grey">(1.6%) </span></td>
      <td id="T_c2707_row6_col1" class="data row6 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_c2707_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row6_col4" class="data row6 col4" >7 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_c2707_row7_col0" class="data row7 col0" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_c2707_row7_col1" class="data row7 col1" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_c2707_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row7_col4" class="data row7 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_c2707_row8_col0" class="data row8 col0" >88 <span style="color: grey">(28.8%) </span></td>
      <td id="T_c2707_row8_col1" class="data row8 col1" >38 <span style="color: grey">(12.4%) </span></td>
      <td id="T_c2707_row8_col2" class="data row8 col2" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_c2707_row8_col3" class="data row8 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_c2707_row8_col4" class="data row8 col4" >129 <span style="color: grey">(42.2%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_c2707_row9_col0" class="data row9 col0" >10 <span style="color: grey">(3.3%) </span></td>
      <td id="T_c2707_row9_col1" class="data row9 col1" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_c2707_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row9_col4" class="data row9 col4" >11 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_c2707_row10_col0" class="data row10 col0" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_c2707_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row10_col4" class="data row10 col4" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_c2707_row11_col0" class="data row11 col0" >6 <span style="color: grey">(2.0%) </span></td>
      <td id="T_c2707_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row11_col4" class="data row11 col4" >6 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_c2707_row12_col0" class="data row12 col0" >8 <span style="color: grey">(2.6%) </span></td>
      <td id="T_c2707_row12_col1" class="data row12 col1" >9 <span style="color: grey">(2.9%) </span></td>
      <td id="T_c2707_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row12_col4" class="data row12 col4" >17 <span style="color: grey">(5.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_c2707_row13_col0" class="data row13 col0" >7 <span style="color: grey">(2.3%) </span></td>
      <td id="T_c2707_row13_col1" class="data row13 col1" >17 <span style="color: grey">(5.6%) </span></td>
      <td id="T_c2707_row13_col2" class="data row13 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row13_col3" class="data row13 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_c2707_row13_col4" class="data row13 col4" >25 <span style="color: grey">(8.2%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_c2707_row14_col0" class="data row14 col0" >44 <span style="color: grey">(14.4%) </span></td>
      <td id="T_c2707_row14_col1" class="data row14 col1" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_c2707_row14_col2" class="data row14 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row14_col3" class="data row14 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c2707_row14_col4" class="data row14 col4" >48 <span style="color: grey">(15.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c2707_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_c2707_row15_col0" class="data row15 col0" >225 <span style="color: grey">(73.5%) </span></td>
      <td id="T_c2707_row15_col1" class="data row15 col1" >75 <span style="color: grey">(24.5%) </span></td>
      <td id="T_c2707_row15_col2" class="data row15 col2" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_c2707_row15_col3" class="data row15 col3" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_c2707_row15_col4" class="data row15 col4" >306 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_608b7 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_608b7  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_608b7_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.6%, transparent 6.6%);
  font-family: Courier;
}
#T_608b7_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.5%, transparent 13.5%);
  font-family: Courier;
}
#T_608b7_row0_col2, #T_608b7_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_608b7_row0_col3, #T_608b7_row5_col2, #T_608b7_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_608b7_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_608b7_row1_col0, #T_608b7_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_608b7_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_608b7_row1_col2, #T_608b7_row1_col3, #T_608b7_row2_col2, #T_608b7_row2_col3, #T_608b7_row3_col2, #T_608b7_row3_col3, #T_608b7_row4_col1, #T_608b7_row4_col2, #T_608b7_row4_col3, #T_608b7_row5_col3, #T_608b7_row6_col2, #T_608b7_row6_col3 {
  width: 10em;
  font-family: Courier;
}
#T_608b7_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_608b7_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_608b7_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_608b7_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.5%, transparent 30.5%);
  font-family: Courier;
}
#T_608b7_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.9%, transparent 14.9%);
  font-family: Courier;
}
#T_608b7_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.0%, transparent 27.0%);
  font-family: Courier;
}
#T_608b7_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_608b7_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_608b7_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.6%, transparent 41.6%);
  font-family: Courier;
}
#T_608b7_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.4%, transparent 28.4%);
  font-family: Courier;
}
#T_608b7_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.0%, transparent 39.0%);
  font-family: Courier;
}
#T_608b7_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.2%, transparent 5.2%);
  font-family: Courier;
}
#T_608b7_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.1%, transparent 4.1%);
  font-family: Courier;
}
#T_608b7_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_608b7_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.8%, transparent 9.8%);
  font-family: Courier;
}
#T_608b7_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.1%, transparent 31.1%);
  font-family: Courier;
}
#T_608b7_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_608b7_row8_col0, #T_608b7_row8_col1, #T_608b7_row8_col2, #T_608b7_row8_col3, #T_608b7_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_608b7">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_608b7_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_608b7_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_608b7_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_608b7_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_608b7_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_608b7_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_608b7_row0_col0" class="data row0 col0" >20 <span style="color: grey">(5.2%) </span></td>
      <td id="T_608b7_row0_col1" class="data row0 col1" >10 <span style="color: grey">(2.6%) </span></td>
      <td id="T_608b7_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_608b7_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_608b7_row0_col4" class="data row0 col4" >32 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_608b7_row1_col0" class="data row1 col0" >8 <span style="color: grey">(2.1%) </span></td>
      <td id="T_608b7_row1_col1" class="data row1 col1" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_608b7_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row1_col4" class="data row1 col4" >10 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_608b7_row2_col0" class="data row2 col0" >9 <span style="color: grey">(2.3%) </span></td>
      <td id="T_608b7_row2_col1" class="data row2 col1" >4 <span style="color: grey">(1.0%) </span></td>
      <td id="T_608b7_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row2_col4" class="data row2 col4" >13 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_608b7_row3_col0" class="data row3 col0" >93 <span style="color: grey">(24.2%) </span></td>
      <td id="T_608b7_row3_col1" class="data row3 col1" >11 <span style="color: grey">(2.9%) </span></td>
      <td id="T_608b7_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row3_col4" class="data row3 col4" >104 <span style="color: grey">(27.0%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_608b7_row4_col0" class="data row4 col0" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_608b7_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row4_col4" class="data row4 col4" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_608b7_row5_col0" class="data row5 col0" >127 <span style="color: grey">(33.0%) </span></td>
      <td id="T_608b7_row5_col1" class="data row5 col1" >21 <span style="color: grey">(5.5%) </span></td>
      <td id="T_608b7_row5_col2" class="data row5 col2" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_608b7_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row5_col4" class="data row5 col4" >150 <span style="color: grey">(39.0%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_608b7_row6_col0" class="data row6 col0" >16 <span style="color: grey">(4.2%) </span></td>
      <td id="T_608b7_row6_col1" class="data row6 col1" >3 <span style="color: grey">(0.8%) </span></td>
      <td id="T_608b7_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_608b7_row6_col4" class="data row6 col4" >19 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_608b7_row7_col0" class="data row7 col0" >30 <span style="color: grey">(7.8%) </span></td>
      <td id="T_608b7_row7_col1" class="data row7 col1" >23 <span style="color: grey">(6.0%) </span></td>
      <td id="T_608b7_row7_col2" class="data row7 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_608b7_row7_col3" class="data row7 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_608b7_row7_col4" class="data row7 col4" >55 <span style="color: grey">(14.3%) </span></td>
    </tr>
    <tr>
      <th id="T_608b7_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_608b7_row8_col0" class="data row8 col0" >305 <span style="color: grey">(79.2%) </span></td>
      <td id="T_608b7_row8_col1" class="data row8 col1" >74 <span style="color: grey">(19.2%) </span></td>
      <td id="T_608b7_row8_col2" class="data row8 col2" >4 <span style="color: grey">(1.0%) </span></td>
      <td id="T_608b7_row8_col3" class="data row8 col3" >2 <span style="color: grey">(0.5%) </span></td>
      <td id="T_608b7_row8_col4" class="data row8 col4" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_8abe6 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8abe6  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8abe6_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_8abe6_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.8%, transparent 8.8%);
  font-family: Courier;
}
#T_8abe6_row0_col2, #T_8abe6_row0_col3, #T_8abe6_row1_col2, #T_8abe6_row1_col3, #T_8abe6_row2_col2, #T_8abe6_row2_col3, #T_8abe6_row3_col2, #T_8abe6_row3_col3, #T_8abe6_row4_col1, #T_8abe6_row4_col2, #T_8abe6_row4_col3, #T_8abe6_row5_col3, #T_8abe6_row6_col0, #T_8abe6_row6_col1, #T_8abe6_row6_col2, #T_8abe6_row7_col2, #T_8abe6_row7_col3, #T_8abe6_row8_col2, #T_8abe6_row8_col3, #T_8abe6_row9_col1, #T_8abe6_row9_col2, #T_8abe6_row9_col3, #T_8abe6_row10_col0, #T_8abe6_row10_col2, #T_8abe6_row10_col3, #T_8abe6_row11_col3, #T_8abe6_row12_col2, #T_8abe6_row12_col3 {
  width: 10em;
  font-family: Courier;
}
#T_8abe6_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_8abe6_row1_col0, #T_8abe6_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.7%, transparent 4.7%);
  font-family: Courier;
}
#T_8abe6_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.0%, transparent 7.0%);
  font-family: Courier;
}
#T_8abe6_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.1%, transparent 5.1%);
  font-family: Courier;
}
#T_8abe6_row2_col1, #T_8abe6_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.5%, transparent 3.5%);
  font-family: Courier;
}
#T_8abe6_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_8abe6_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
#T_8abe6_row3_col1, #T_8abe6_row10_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_8abe6_row3_col4, #T_8abe6_row9_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_8abe6_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_8abe6_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_8abe6_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_8abe6_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_8abe6_row5_col4, #T_8abe6_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_8abe6_row6_col3, #T_8abe6_row13_col0, #T_8abe6_row13_col1, #T_8abe6_row13_col2, #T_8abe6_row13_col3, #T_8abe6_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_8abe6_row6_col4, #T_8abe6_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_8abe6_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_8abe6_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.1%, transparent 28.1%);
  font-family: Courier;
}
#T_8abe6_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_8abe6_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.8%, transparent 44.8%);
  font-family: Courier;
}
#T_8abe6_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.5%, transparent 10.5%);
  font-family: Courier;
}
#T_8abe6_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.4%, transparent 36.4%);
  font-family: Courier;
}
#T_8abe6_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_8abe6_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.8%, transparent 19.8%);
  font-family: Courier;
}
#T_8abe6_row11_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.8%, transparent 22.8%);
  font-family: Courier;
}
#T_8abe6_row11_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_8abe6_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.9%, transparent 20.9%);
  font-family: Courier;
}
#T_8abe6_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.3%, transparent 12.3%);
  font-family: Courier;
}
#T_8abe6_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
</style>
<table id="T_8abe6">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_8abe6_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_8abe6_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_8abe6_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_8abe6_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_8abe6_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_8abe6_level0_row0" class="row_heading level0 row0" >Abdomen</th>
      <td id="T_8abe6_row0_col0" class="data row0 col0" >12 <span style="color: grey">(4.7%) </span></td>
      <td id="T_8abe6_row0_col1" class="data row0 col1" >5 <span style="color: grey">(2.0%) </span></td>
      <td id="T_8abe6_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row0_col4" class="data row0 col4" >17 <span style="color: grey">(6.7%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row1" class="row_heading level0 row1" >Back</th>
      <td id="T_8abe6_row1_col0" class="data row1 col0" >9 <span style="color: grey">(3.6%) </span></td>
      <td id="T_8abe6_row1_col1" class="data row1 col1" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_8abe6_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row1_col4" class="data row1 col4" >13 <span style="color: grey">(5.1%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row2" class="row_heading level0 row2" >Buttocks</th>
      <td id="T_8abe6_row2_col0" class="data row2 col0" >9 <span style="color: grey">(3.6%) </span></td>
      <td id="T_8abe6_row2_col1" class="data row2 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_8abe6_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row2_col4" class="data row2 col4" >11 <span style="color: grey">(4.3%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row3" class="row_heading level0 row3" >Chest</th>
      <td id="T_8abe6_row3_col0" class="data row3 col0" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_8abe6_row3_col1" class="data row3 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_8abe6_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row3_col4" class="data row3 col4" >5 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row4" class="row_heading level0 row4" >Coccyx</th>
      <td id="T_8abe6_row4_col0" class="data row4 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_8abe6_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row4_col4" class="data row4 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row5" class="row_heading level0 row5" >Full body</th>
      <td id="T_8abe6_row5_col0" class="data row5 col0" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_8abe6_row5_col1" class="data row5 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_8abe6_row5_col2" class="data row5 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_8abe6_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row5_col4" class="data row5 col4" >9 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row6" class="row_heading level0 row6" >Hals</th>
      <td id="T_8abe6_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_8abe6_row6_col4" class="data row6 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row7" class="row_heading level0 row7" >Head</th>
      <td id="T_8abe6_row7_col0" class="data row7 col0" >13 <span style="color: grey">(5.1%) </span></td>
      <td id="T_8abe6_row7_col1" class="data row7 col1" >16 <span style="color: grey">(6.3%) </span></td>
      <td id="T_8abe6_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row7_col4" class="data row7 col4" >29 <span style="color: grey">(11.5%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row8" class="row_heading level0 row8" >Innere Medizin</th>
      <td id="T_8abe6_row8_col0" class="data row8 col0" >86 <span style="color: grey">(34.0%) </span></td>
      <td id="T_8abe6_row8_col1" class="data row8 col1" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_8abe6_row8_col2" class="data row8 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row8_col3" class="data row8 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row8_col4" class="data row8 col4" >92 <span style="color: grey">(36.4%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row9" class="row_heading level0 row9" >Intestine</th>
      <td id="T_8abe6_row9_col0" class="data row9 col0" >5 <span style="color: grey">(2.0%) </span></td>
      <td id="T_8abe6_row9_col1" class="data row9 col1" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row9_col4" class="data row9 col4" >5 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row10" class="row_heading level0 row10" >Intimate area</th>
      <td id="T_8abe6_row10_col0" class="data row10 col0" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row10_col1" class="data row10 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_8abe6_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row10_col4" class="data row10 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row11" class="row_heading level0 row11" >Lower extremities</th>
      <td id="T_8abe6_row11_col0" class="data row11 col0" >38 <span style="color: grey">(15.0%) </span></td>
      <td id="T_8abe6_row11_col1" class="data row11 col1" >13 <span style="color: grey">(5.1%) </span></td>
      <td id="T_8abe6_row11_col2" class="data row11 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_8abe6_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row11_col4" class="data row11 col4" >53 <span style="color: grey">(20.9%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row12" class="row_heading level0 row12" >Upper extremities</th>
      <td id="T_8abe6_row12_col0" class="data row12 col0" >7 <span style="color: grey">(2.8%) </span></td>
      <td id="T_8abe6_row12_col1" class="data row12 col1" >7 <span style="color: grey">(2.8%) </span></td>
      <td id="T_8abe6_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8abe6_row12_col4" class="data row12 col4" >14 <span style="color: grey">(5.5%) </span></td>
    </tr>
    <tr>
      <th id="T_8abe6_level0_row13" class="row_heading level0 row13" >Total</th>
      <td id="T_8abe6_row13_col0" class="data row13 col0" >192 <span style="color: grey">(75.9%) </span></td>
      <td id="T_8abe6_row13_col1" class="data row13 col1" >57 <span style="color: grey">(22.5%) </span></td>
      <td id="T_8abe6_row13_col2" class="data row13 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_8abe6_row13_col3" class="data row13 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_8abe6_row13_col4" class="data row13 col4" >253 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_a8254 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a8254  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a8254_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 99.5%, transparent 99.5%);
  font-family: Courier;
}
#T_a8254_row0_col1, #T_a8254_row2_col3, #T_a8254_row3_col0, #T_a8254_row3_col1, #T_a8254_row3_col2, #T_a8254_row3_col3, #T_a8254_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_a8254_row0_col2, #T_a8254_row1_col2, #T_a8254_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_a8254_row0_col3, #T_a8254_row1_col0, #T_a8254_row1_col1, #T_a8254_row1_col3, #T_a8254_row2_col1 {
  width: 10em;
  font-family: Courier;
}
#T_a8254_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.3%, transparent 98.3%);
  font-family: Courier;
}
#T_a8254_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_a8254_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_a8254_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
</style>
<table id="T_a8254">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_a8254_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_a8254_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_a8254_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_a8254_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_a8254_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_a8254_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_a8254_row0_col0" class="data row0 col0" >183 <span style="color: grey">(76.2%) </span></td>
      <td id="T_a8254_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_a8254_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a8254_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_a8254_row0_col4" class="data row0 col4" >236 <span style="color: grey">(98.3%) </span></td>
    </tr>
    <tr>
      <th id="T_a8254_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_a8254_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_a8254_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_a8254_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a8254_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_a8254_row1_col4" class="data row1 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_a8254_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_a8254_row2_col0" class="data row2 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a8254_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_a8254_row2_col2" class="data row2 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a8254_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a8254_row2_col4" class="data row2 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_a8254_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_a8254_row3_col0" class="data row3 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_a8254_row3_col1" class="data row3 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_a8254_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_a8254_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a8254_row3_col4" class="data row3 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_dc82f th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dc82f  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dc82f_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 92.9%, transparent 92.9%);
  font-family: Courier;
}
#T_dc82f_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.2%, transparent 19.2%);
  font-family: Courier;
}
#T_dc82f_row0_col2, #T_dc82f_row0_col3, #T_dc82f_row1_col1, #T_dc82f_row1_col2, #T_dc82f_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_dc82f_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.4%, transparent 75.4%);
  font-family: Courier;
}
#T_dc82f_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_dc82f_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_dc82f_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_dc82f_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.8%, transparent 80.8%);
  font-family: Courier;
}
#T_dc82f_row2_col2, #T_dc82f_row2_col3, #T_dc82f_row3_col0, #T_dc82f_row3_col1, #T_dc82f_row3_col2, #T_dc82f_row3_col3, #T_dc82f_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_dc82f_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.9%, transparent 22.9%);
  font-family: Courier;
}
</style>
<table id="T_dc82f">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_dc82f_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_dc82f_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_dc82f_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_dc82f_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_dc82f_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_dc82f_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_dc82f_row0_col0" class="data row0 col0" >171 <span style="color: grey">(71.2%) </span></td>
      <td id="T_dc82f_row0_col1" class="data row0 col1" >10 <span style="color: grey">(4.2%) </span></td>
      <td id="T_dc82f_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dc82f_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dc82f_row0_col4" class="data row0 col4" >181 <span style="color: grey">(75.4%) </span></td>
    </tr>
    <tr>
      <th id="T_dc82f_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_dc82f_row1_col0" class="data row1 col0" >4 <span style="color: grey">(1.7%) </span></td>
      <td id="T_dc82f_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_dc82f_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dc82f_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dc82f_row1_col4" class="data row1 col4" >4 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_dc82f_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_dc82f_row2_col0" class="data row2 col0" >9 <span style="color: grey">(3.8%) </span></td>
      <td id="T_dc82f_row2_col1" class="data row2 col1" >42 <span style="color: grey">(17.5%) </span></td>
      <td id="T_dc82f_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_dc82f_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dc82f_row2_col4" class="data row2 col4" >55 <span style="color: grey">(22.9%) </span></td>
    </tr>
    <tr>
      <th id="T_dc82f_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_dc82f_row3_col0" class="data row3 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_dc82f_row3_col1" class="data row3 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_dc82f_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_dc82f_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_dc82f_row3_col4" class="data row3 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_227a9 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_227a9  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_227a9_row0_col0, #T_227a9_row0_col1, #T_227a9_row0_col2, #T_227a9_row0_col3, #T_227a9_row0_col4, #T_227a9_row1_col0, #T_227a9_row1_col1, #T_227a9_row1_col2, #T_227a9_row1_col3, #T_227a9_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_227a9">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_227a9_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_227a9_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_227a9_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_227a9_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_227a9_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_227a9_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_227a9_row0_col0" class="data row0 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_227a9_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_227a9_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_227a9_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_227a9_row0_col4" class="data row0 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_227a9_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_227a9_row1_col0" class="data row1 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_227a9_row1_col1" class="data row1 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_227a9_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_227a9_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_227a9_row1_col4" class="data row1 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e2d33 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2d33  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2d33_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 99.5%, transparent 99.5%);
  font-family: Courier;
}
#T_e2d33_row0_col1, #T_e2d33_row0_col3, #T_e2d33_row1_col2, #T_e2d33_row2_col0, #T_e2d33_row2_col1, #T_e2d33_row2_col2, #T_e2d33_row2_col3, #T_e2d33_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e2d33_row0_col2, #T_e2d33_row1_col1, #T_e2d33_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_e2d33_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.3%, transparent 98.3%);
  font-family: Courier;
}
#T_e2d33_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_e2d33_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
</style>
<table id="T_e2d33">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e2d33_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e2d33_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e2d33_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e2d33_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_e2d33_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_e2d33_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_e2d33_row0_col0" class="data row0 col0" >183 <span style="color: grey">(76.2%) </span></td>
      <td id="T_e2d33_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_e2d33_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e2d33_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e2d33_row0_col4" class="data row0 col4" >236 <span style="color: grey">(98.3%) </span></td>
    </tr>
    <tr>
      <th id="T_e2d33_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_e2d33_row1_col0" class="data row1 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e2d33_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e2d33_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_e2d33_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e2d33_row1_col4" class="data row1 col4" >4 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_e2d33_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_e2d33_row2_col0" class="data row2 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_e2d33_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_e2d33_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_e2d33_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e2d33_row2_col4" class="data row2 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_6c1eb th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_6c1eb  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_6c1eb_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.3%, transparent 86.3%);
  font-family: Courier;
}
#T_6c1eb_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.1%, transparent 68.1%);
  font-family: Courier;
}
#T_6c1eb_row0_col2, #T_6c1eb_row0_col3, #T_6c1eb_row1_col2, #T_6c1eb_row1_col3, #T_6c1eb_row2_col0 {
  width: 10em;
  font-family: Courier;
}
#T_6c1eb_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.2%, transparent 81.2%);
  font-family: Courier;
}
#T_6c1eb_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.7%, transparent 13.7%);
  font-family: Courier;
}
#T_6c1eb_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.5%, transparent 25.5%);
  font-family: Courier;
}
#T_6c1eb_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.8%, transparent 15.8%);
  font-family: Courier;
}
#T_6c1eb_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.4%, transparent 6.4%);
  font-family: Courier;
}
#T_6c1eb_row2_col2, #T_6c1eb_row2_col3, #T_6c1eb_row3_col0, #T_6c1eb_row3_col1, #T_6c1eb_row3_col2, #T_6c1eb_row3_col3, #T_6c1eb_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_6c1eb_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
</style>
<table id="T_6c1eb">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_6c1eb_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_6c1eb_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_6c1eb_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_6c1eb_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_6c1eb_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_6c1eb_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_6c1eb_row0_col0" class="data row0 col0" >158 <span style="color: grey">(67.5%) </span></td>
      <td id="T_6c1eb_row0_col1" class="data row0 col1" >32 <span style="color: grey">(13.7%) </span></td>
      <td id="T_6c1eb_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_6c1eb_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_6c1eb_row0_col4" class="data row0 col4" >190 <span style="color: grey">(81.2%) </span></td>
    </tr>
    <tr>
      <th id="T_6c1eb_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_6c1eb_row1_col0" class="data row1 col0" >25 <span style="color: grey">(10.7%) </span></td>
      <td id="T_6c1eb_row1_col1" class="data row1 col1" >12 <span style="color: grey">(5.1%) </span></td>
      <td id="T_6c1eb_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_6c1eb_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_6c1eb_row1_col4" class="data row1 col4" >37 <span style="color: grey">(15.8%) </span></td>
    </tr>
    <tr>
      <th id="T_6c1eb_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_6c1eb_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_6c1eb_row2_col1" class="data row2 col1" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_6c1eb_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_6c1eb_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_6c1eb_row2_col4" class="data row2 col4" >7 <span style="color: grey">(3.0%) </span></td>
    </tr>
    <tr>
      <th id="T_6c1eb_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_6c1eb_row3_col0" class="data row3 col0" >183 <span style="color: grey">(78.2%) </span></td>
      <td id="T_6c1eb_row3_col1" class="data row3 col1" >47 <span style="color: grey">(20.1%) </span></td>
      <td id="T_6c1eb_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_6c1eb_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_6c1eb_row3_col4" class="data row3 col4" >234 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e6651 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e6651  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e6651_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.3%, transparent 27.3%);
  font-family: Courier;
}
#T_e6651_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 48.1%, transparent 48.1%);
  font-family: Courier;
}
#T_e6651_row0_col2, #T_e6651_row0_col3, #T_e6651_row2_col0, #T_e6651_row2_col1, #T_e6651_row2_col2, #T_e6651_row2_col3, #T_e6651_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e6651_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 32.8%, transparent 32.8%);
  font-family: Courier;
}
#T_e6651_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 72.7%, transparent 72.7%);
  font-family: Courier;
}
#T_e6651_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 51.9%, transparent 51.9%);
  font-family: Courier;
}
#T_e6651_row1_col2, #T_e6651_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_e6651_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 67.2%, transparent 67.2%);
  font-family: Courier;
}
</style>
<table id="T_e6651">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e6651_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e6651_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e6651_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e6651_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_e6651_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_e6651_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_e6651_row0_col0" class="data row0 col0" >50 <span style="color: grey">(21.0%) </span></td>
      <td id="T_e6651_row0_col1" class="data row0 col1" >25 <span style="color: grey">(10.5%) </span></td>
      <td id="T_e6651_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_e6651_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e6651_row0_col4" class="data row0 col4" >78 <span style="color: grey">(32.8%) </span></td>
    </tr>
    <tr>
      <th id="T_e6651_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_e6651_row1_col0" class="data row1 col0" >133 <span style="color: grey">(55.9%) </span></td>
      <td id="T_e6651_row1_col1" class="data row1 col1" >27 <span style="color: grey">(11.3%) </span></td>
      <td id="T_e6651_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e6651_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e6651_row1_col4" class="data row1 col4" >160 <span style="color: grey">(67.2%) </span></td>
    </tr>
    <tr>
      <th id="T_e6651_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_e6651_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.9%) </span></td>
      <td id="T_e6651_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_e6651_row2_col2" class="data row2 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_e6651_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_e6651_row2_col4" class="data row2 col4" >238 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_834db th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_834db  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_834db_row0_col0, #T_834db_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.3%, transparent 12.3%);
  font-family: Courier;
}
#T_834db_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_834db_row0_col2, #T_834db_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_834db_row0_col3, #T_834db_row1_col3, #T_834db_row2_col3, #T_834db_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_834db_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.7%, transparent 11.7%);
  font-family: Courier;
}
#T_834db_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 63.0%, transparent 63.0%);
  font-family: Courier;
}
#T_834db_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 59.5%, transparent 59.5%);
  font-family: Courier;
}
#T_834db_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 59.2%, transparent 59.2%);
  font-family: Courier;
}
#T_834db_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_834db_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.8%, transparent 10.8%);
  font-family: Courier;
}
#T_834db_row2_col2, #T_834db_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_834db_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_834db_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.2%, transparent 16.2%);
  font-family: Courier;
}
#T_834db_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.2%, transparent 14.2%);
  font-family: Courier;
}
#T_834db_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.8%, transparent 6.8%);
  font-family: Courier;
}
#T_834db_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.1%, transparent 8.1%);
  font-family: Courier;
}
#T_834db_row4_col2, #T_834db_row4_col3 {
  width: 10em;
  font-family: Courier;
}
#T_834db_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_834db_row5_col0, #T_834db_row5_col1, #T_834db_row5_col2, #T_834db_row5_col3, #T_834db_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_834db">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_834db_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_834db_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_834db_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_834db_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_834db_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_834db_level0_row0" class="row_heading level0 row0" >BeIn the treatment team</th>
      <td id="T_834db_row0_col0" class="data row0 col0" >9 <span style="color: grey">(7.5%) </span></td>
      <td id="T_834db_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.7%) </span></td>
      <td id="T_834db_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.7%) </span></td>
      <td id="T_834db_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_834db_row0_col4" class="data row0 col4" >14 <span style="color: grey">(11.7%) </span></td>
    </tr>
    <tr>
      <th id="T_834db_level0_row1" class="row_heading level0 row1" >For affected individuals</th>
      <td id="T_834db_row1_col0" class="data row1 col0" >46 <span style="color: grey">(38.3%) </span></td>
      <td id="T_834db_row1_col1" class="data row1 col1" >22 <span style="color: grey">(18.3%) </span></td>
      <td id="T_834db_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.7%) </span></td>
      <td id="T_834db_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_834db_row1_col4" class="data row1 col4" >71 <span style="color: grey">(59.2%) </span></td>
    </tr>
    <tr>
      <th id="T_834db_level0_row2" class="row_heading level0 row2" >For parents des Betroffenen</th>
      <td id="T_834db_row2_col0" class="data row2 col0" >4 <span style="color: grey">(3.3%) </span></td>
      <td id="T_834db_row2_col1" class="data row2 col1" >4 <span style="color: grey">(3.3%) </span></td>
      <td id="T_834db_row2_col2" class="data row2 col2" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_834db_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_834db_row2_col4" class="data row2 col4" >10 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_834db_level0_row3" class="row_heading level0 row3" >For the excercise experts</th>
      <td id="T_834db_row3_col0" class="data row3 col0" >9 <span style="color: grey">(7.5%) </span></td>
      <td id="T_834db_row3_col1" class="data row3 col1" >6 <span style="color: grey">(5.0%) </span></td>
      <td id="T_834db_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_834db_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_834db_row3_col4" class="data row3 col4" >17 <span style="color: grey">(14.2%) </span></td>
    </tr>
    <tr>
      <th id="T_834db_level0_row4" class="row_heading level0 row4" >Mit der Ablehnung weiterer sporttherapheutischer Angebote</th>
      <td id="T_834db_row4_col0" class="data row4 col0" >5 <span style="color: grey">(4.2%) </span></td>
      <td id="T_834db_row4_col1" class="data row4 col1" >3 <span style="color: grey">(2.5%) </span></td>
      <td id="T_834db_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_834db_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_834db_row4_col4" class="data row4 col4" >8 <span style="color: grey">(6.7%) </span></td>
    </tr>
    <tr>
      <th id="T_834db_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_834db_row5_col0" class="data row5 col0" >73 <span style="color: grey">(60.8%) </span></td>
      <td id="T_834db_row5_col1" class="data row5 col1" >37 <span style="color: grey">(30.8%) </span></td>
      <td id="T_834db_row5_col2" class="data row5 col2" >6 <span style="color: grey">(5.0%) </span></td>
      <td id="T_834db_row5_col3" class="data row5 col3" >4 <span style="color: grey">(3.3%) </span></td>
      <td id="T_834db_row5_col4" class="data row5 col4" >120 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_cc5fb th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cc5fb  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cc5fb_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_cc5fb_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.8%, transparent 11.8%);
  font-family: Courier;
}
#T_cc5fb_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_cc5fb_row0_col3, #T_cc5fb_row1_col3, #T_cc5fb_row2_col0, #T_cc5fb_row2_col1, #T_cc5fb_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_cc5fb_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.1%, transparent 7.1%);
  font-family: Courier;
}
#T_cc5fb_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 94.6%, transparent 94.6%);
  font-family: Courier;
}
#T_cc5fb_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 88.2%, transparent 88.2%);
  font-family: Courier;
}
#T_cc5fb_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_cc5fb_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 92.5%, transparent 92.5%);
  font-family: Courier;
}
#T_cc5fb_row2_col3, #T_cc5fb_row3_col0, #T_cc5fb_row3_col1, #T_cc5fb_row3_col2, #T_cc5fb_row3_col3, #T_cc5fb_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_cc5fb_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_cc5fb">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_cc5fb_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_cc5fb_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_cc5fb_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_cc5fb_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_cc5fb_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_cc5fb_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_cc5fb_row0_col0" class="data row0 col0" >10 <span style="color: grey">(4.2%) </span></td>
      <td id="T_cc5fb_row0_col1" class="data row0 col1" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_cc5fb_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_cc5fb_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cc5fb_row0_col4" class="data row0 col4" >17 <span style="color: grey">(7.1%) </span></td>
    </tr>
    <tr>
      <th id="T_cc5fb_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_cc5fb_row1_col0" class="data row1 col0" >174 <span style="color: grey">(72.8%) </span></td>
      <td id="T_cc5fb_row1_col1" class="data row1 col1" >45 <span style="color: grey">(18.8%) </span></td>
      <td id="T_cc5fb_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_cc5fb_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cc5fb_row1_col4" class="data row1 col4" >221 <span style="color: grey">(92.5%) </span></td>
    </tr>
    <tr>
      <th id="T_cc5fb_level0_row2" class="row_heading level0 row2" >Weiß nicht</th>
      <td id="T_cc5fb_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_cc5fb_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cc5fb_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cc5fb_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_cc5fb_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_cc5fb_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_cc5fb_row3_col0" class="data row3 col0" >184 <span style="color: grey">(77.0%) </span></td>
      <td id="T_cc5fb_row3_col1" class="data row3 col1" >51 <span style="color: grey">(21.3%) </span></td>
      <td id="T_cc5fb_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cc5fb_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_cc5fb_row3_col4" class="data row3 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_630a0 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_630a0  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_630a0_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.4%, transparent 80.4%);
  font-family: Courier;
}
#T_630a0_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.4%, transparent 43.4%);
  font-family: Courier;
}
#T_630a0_row0_col2, #T_630a0_row0_col3, #T_630a0_row1_col1, #T_630a0_row1_col2, #T_630a0_row1_col3, #T_630a0_row3_col2, #T_630a0_row3_col3, #T_630a0_row4_col2, #T_630a0_row4_col3, #T_630a0_row5_col2, #T_630a0_row5_col3 {
  width: 10em;
  font-family: Courier;
}
#T_630a0_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 71.0%, transparent 71.0%);
  font-family: Courier;
}
#T_630a0_row1_col0, #T_630a0_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_630a0_row1_col4, #T_630a0_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_630a0_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.5%, transparent 6.5%);
  font-family: Courier;
}
#T_630a0_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.7%, transparent 37.7%);
  font-family: Courier;
}
#T_630a0_row2_col2, #T_630a0_row2_col3, #T_630a0_row6_col0, #T_630a0_row6_col1, #T_630a0_row6_col2, #T_630a0_row6_col3, #T_630a0_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_630a0_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.9%, transparent 14.9%);
  font-family: Courier;
}
#T_630a0_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.2%, transparent 9.2%);
  font-family: Courier;
}
#T_630a0_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.2%, transparent 13.2%);
  font-family: Courier;
}
#T_630a0_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_630a0_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_630a0_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_630a0_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_630a0_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
</style>
<table id="T_630a0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_630a0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_630a0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_630a0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_630a0_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_630a0_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_630a0_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_630a0_row0_col0" class="data row0 col0" >148 <span style="color: grey">(61.4%) </span></td>
      <td id="T_630a0_row0_col1" class="data row0 col1" >23 <span style="color: grey">(9.5%) </span></td>
      <td id="T_630a0_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row0_col4" class="data row0 col4" >171 <span style="color: grey">(71.0%) </span></td>
    </tr>
    <tr>
      <th id="T_630a0_level0_row1" class="row_heading level0 row1" >Eltern</th>
      <td id="T_630a0_row1_col0" class="data row1 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_630a0_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row1_col4" class="data row1 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_630a0_level0_row2" class="row_heading level0 row2" >Medizin</th>
      <td id="T_630a0_row2_col0" class="data row2 col0" >12 <span style="color: grey">(5.0%) </span></td>
      <td id="T_630a0_row2_col1" class="data row2 col1" >20 <span style="color: grey">(8.3%) </span></td>
      <td id="T_630a0_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_630a0_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_630a0_row2_col4" class="data row2 col4" >36 <span style="color: grey">(14.9%) </span></td>
    </tr>
    <tr>
      <th id="T_630a0_level0_row3" class="row_heading level0 row3" >Pflege</th>
      <td id="T_630a0_row3_col0" class="data row3 col0" >17 <span style="color: grey">(7.1%) </span></td>
      <td id="T_630a0_row3_col1" class="data row3 col1" >7 <span style="color: grey">(2.9%) </span></td>
      <td id="T_630a0_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row3_col4" class="data row3 col4" >24 <span style="color: grey">(10.0%) </span></td>
    </tr>
    <tr>
      <th id="T_630a0_level0_row4" class="row_heading level0 row4" >Physiotherapie</th>
      <td id="T_630a0_row4_col0" class="data row4 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_630a0_row4_col1" class="data row4 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_630a0_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row4_col4" class="data row4 col4" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_630a0_level0_row5" class="row_heading level0 row5" >Psychosozialer Dienst</th>
      <td id="T_630a0_row5_col0" class="data row5 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_630a0_row5_col1" class="data row5 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_630a0_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_630a0_row5_col4" class="data row5 col4" >4 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_630a0_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_630a0_row6_col0" class="data row6 col0" >184 <span style="color: grey">(76.3%) </span></td>
      <td id="T_630a0_row6_col1" class="data row6 col1" >53 <span style="color: grey">(22.0%) </span></td>
      <td id="T_630a0_row6_col2" class="data row6 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_630a0_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_630a0_row6_col4" class="data row6 col4" >241 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_ec384 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ec384  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ec384_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_ec384_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.6%, transparent 34.6%);
  font-family: Courier;
}
#T_ec384_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_ec384_row0_col3 {
  width: 10em;
  font-family: Courier;
}
#T_ec384_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.2%, transparent 9.2%);
  font-family: Courier;
}
#T_ec384_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.9%, transparent 98.9%);
  font-family: Courier;
}
#T_ec384_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 65.4%, transparent 65.4%);
  font-family: Courier;
}
#T_ec384_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_ec384_row1_col3, #T_ec384_row2_col0, #T_ec384_row2_col1, #T_ec384_row2_col2, #T_ec384_row2_col3, #T_ec384_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_ec384_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.8%, transparent 90.8%);
  font-family: Courier;
}
</style>
<table id="T_ec384">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_ec384_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_ec384_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_ec384_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_ec384_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_ec384_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_ec384_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_ec384_row0_col0" class="data row0 col0" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_ec384_row0_col1" class="data row0 col1" >18 <span style="color: grey">(7.5%) </span></td>
      <td id="T_ec384_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_ec384_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ec384_row0_col4" class="data row0 col4" >22 <span style="color: grey">(9.2%) </span></td>
    </tr>
    <tr>
      <th id="T_ec384_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_ec384_row1_col0" class="data row1 col0" >181 <span style="color: grey">(75.7%) </span></td>
      <td id="T_ec384_row1_col1" class="data row1 col1" >34 <span style="color: grey">(14.2%) </span></td>
      <td id="T_ec384_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ec384_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ec384_row1_col4" class="data row1 col4" >217 <span style="color: grey">(90.8%) </span></td>
    </tr>
    <tr>
      <th id="T_ec384_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_ec384_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_ec384_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_ec384_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_ec384_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_ec384_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_2bc00 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2bc00  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2bc00_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_2bc00_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_2bc00_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_2bc00_row0_col3, #T_2bc00_row2_col1, #T_2bc00_row2_col2, #T_2bc00_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_2bc00_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_2bc00_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.8%, transparent 97.8%);
  font-family: Courier;
}
#T_2bc00_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_2bc00_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_2bc00_row1_col3, #T_2bc00_row3_col0, #T_2bc00_row3_col1, #T_2bc00_row3_col2, #T_2bc00_row3_col3, #T_2bc00_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_2bc00_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.1%, transparent 97.1%);
  font-family: Courier;
}
#T_2bc00_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_2bc00_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_2bc00">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_2bc00_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_2bc00_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_2bc00_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_2bc00_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_2bc00_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_2bc00_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_2bc00_row0_col0" class="data row0 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_2bc00_row0_col1" class="data row0 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_2bc00_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2bc00_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2bc00_row0_col4" class="data row0 col4" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_2bc00_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_2bc00_row1_col0" class="data row1 col0" >180 <span style="color: grey">(75.0%) </span></td>
      <td id="T_2bc00_row1_col1" class="data row1 col1" >50 <span style="color: grey">(20.8%) </span></td>
      <td id="T_2bc00_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_2bc00_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2bc00_row1_col4" class="data row1 col4" >233 <span style="color: grey">(97.1%) </span></td>
    </tr>
    <tr>
      <th id="T_2bc00_level0_row2" class="row_heading level0 row2" >U</th>
      <td id="T_2bc00_row2_col0" class="data row2 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2bc00_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_2bc00_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2bc00_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2bc00_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_2bc00_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_2bc00_row3_col0" class="data row3 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_2bc00_row3_col1" class="data row3 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_2bc00_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_2bc00_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2bc00_row3_col4" class="data row3 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_7ce9c th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_7ce9c  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_7ce9c_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.7%, transparent 8.7%);
  font-family: Courier;
}
#T_7ce9c_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.5%, transparent 13.5%);
  font-family: Courier;
}
#T_7ce9c_row0_col2, #T_7ce9c_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_7ce9c_row0_col3, #T_7ce9c_row1_col2, #T_7ce9c_row2_col0, #T_7ce9c_row2_col1, #T_7ce9c_row2_col2, #T_7ce9c_row2_col3, #T_7ce9c_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_7ce9c_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_7ce9c_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.3%, transparent 91.3%);
  font-family: Courier;
}
#T_7ce9c_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.5%, transparent 86.5%);
  font-family: Courier;
}
#T_7ce9c_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.0%, transparent 90.0%);
  font-family: Courier;
}
</style>
<table id="T_7ce9c">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_7ce9c_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_7ce9c_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_7ce9c_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_7ce9c_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_7ce9c_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_7ce9c_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_7ce9c_row0_col0" class="data row0 col0" >16 <span style="color: grey">(6.7%) </span></td>
      <td id="T_7ce9c_row0_col1" class="data row0 col1" >7 <span style="color: grey">(2.9%) </span></td>
      <td id="T_7ce9c_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_7ce9c_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_7ce9c_row0_col4" class="data row0 col4" >24 <span style="color: grey">(10.0%) </span></td>
    </tr>
    <tr>
      <th id="T_7ce9c_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_7ce9c_row1_col0" class="data row1 col0" >168 <span style="color: grey">(70.0%) </span></td>
      <td id="T_7ce9c_row1_col1" class="data row1 col1" >45 <span style="color: grey">(18.8%) </span></td>
      <td id="T_7ce9c_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_7ce9c_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_7ce9c_row1_col4" class="data row1 col4" >216 <span style="color: grey">(90.0%) </span></td>
    </tr>
    <tr>
      <th id="T_7ce9c_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_7ce9c_row2_col0" class="data row2 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_7ce9c_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_7ce9c_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_7ce9c_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_7ce9c_row2_col4" class="data row2 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_55a6f th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_55a6f  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_55a6f_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.7%, transparent 41.7%);
  font-family: Courier;
}
#T_55a6f_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_55a6f_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_55a6f_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.2%, transparent 41.2%);
  font-family: Courier;
}
#T_55a6f_row1_col0, #T_55a6f_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.3%, transparent 58.3%);
  font-family: Courier;
}
#T_55a6f_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.8%, transparent 57.8%);
  font-family: Courier;
}
#T_55a6f_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_55a6f_row2_col0, #T_55a6f_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_55a6f_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_55a6f_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_55a6f_row3_col0, #T_55a6f_row3_col1, #T_55a6f_row3_col2, #T_55a6f_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_55a6f">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_55a6f_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_55a6f_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_55a6f_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_55a6f_level0_col3" class="col_heading level0 col3" >Total</th>
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
      <th id="T_55a6f_level0_row0" class="row_heading level0 row0" >Break</th>
      <td id="T_55a6f_row0_col0" class="data row0 col0" >70 <span style="color: grey">(32.4%) </span></td>
      <td id="T_55a6f_row0_col1" class="data row0 col1" >18 <span style="color: grey">(8.3%) </span></td>
      <td id="T_55a6f_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_55a6f_row0_col3" class="data row0 col3" >89 <span style="color: grey">(41.2%) </span></td>
    </tr>
    <tr>
      <th id="T_55a6f_level0_row1" class="row_heading level0 row1" >Cessation</th>
      <td id="T_55a6f_row1_col0" class="data row1 col0" >98 <span style="color: grey">(45.4%) </span></td>
      <td id="T_55a6f_row1_col1" class="data row1 col1" >26 <span style="color: grey">(12.0%) </span></td>
      <td id="T_55a6f_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_55a6f_row1_col3" class="data row1 col3" >126 <span style="color: grey">(58.3%) </span></td>
    </tr>
    <tr>
      <th id="T_55a6f_level0_row2" class="row_heading level0 row2" >Einheit war sowieso vorbei</th>
      <td id="T_55a6f_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_55a6f_row2_col1" class="data row2 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_55a6f_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_55a6f_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_55a6f_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_55a6f_row3_col0" class="data row3 col0" >168 <span style="color: grey">(77.8%) </span></td>
      <td id="T_55a6f_row3_col1" class="data row3 col1" >45 <span style="color: grey">(20.8%) </span></td>
      <td id="T_55a6f_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.4%) </span></td>
      <td id="T_55a6f_row3_col3" class="data row3 col3" >216 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_2147c th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2147c  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2147c_row0_col0, #T_2147c_row0_col1, #T_2147c_row0_col2, #T_2147c_row0_col3, #T_2147c_row0_col4, #T_2147c_row1_col0, #T_2147c_row1_col1, #T_2147c_row1_col2, #T_2147c_row1_col3, #T_2147c_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_2147c">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_2147c_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_2147c_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_2147c_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_2147c_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_2147c_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_2147c_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_2147c_row0_col0" class="data row0 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_2147c_row0_col1" class="data row0 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_2147c_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_2147c_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2147c_row0_col4" class="data row0 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_2147c_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_2147c_row1_col0" class="data row1 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_2147c_row1_col1" class="data row1 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_2147c_row1_col2" class="data row1 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_2147c_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2147c_row1_col4" class="data row1 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_2d138 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2d138  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2d138_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.0%, transparent 7.0%);
  font-family: Courier;
}
#T_2d138_row0_col1, #T_2d138_row3_col1, #T_2d138_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_2d138_row0_col2, #T_2d138_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.6%, transparent 7.6%);
  font-family: Courier;
}
#T_2d138_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_2d138_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_2d138_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.9%, transparent 47.9%);
  font-family: Courier;
}
#T_2d138_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.5%, transparent 37.5%);
  font-family: Courier;
}
#T_2d138_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 46.8%, transparent 46.8%);
  font-family: Courier;
}
#T_2d138_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.8%, transparent 33.8%);
  font-family: Courier;
}
#T_2d138_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.6%, transparent 31.6%);
  font-family: Courier;
}
#T_2d138_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.4%, transparent 1.4%);
  font-family: Courier;
}
#T_2d138_row4_col1, #T_2d138_row5_col1, #T_2d138_row6_col0 {
  width: 10em;
  font-family: Courier;
}
#T_2d138_row4_col2, #T_2d138_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_2d138_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.2%, transparent 4.2%);
  font-family: Courier;
}
#T_2d138_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_2d138_row7_col0, #T_2d138_row7_col1, #T_2d138_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_2d138">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_2d138_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_2d138_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_2d138_level0_col2" class="col_heading level0 col2" >Total</th>
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
      <th id="T_2d138_level0_row0" class="row_heading level0 row0" >Communication strategy</th>
      <td id="T_2d138_row0_col0" class="data row0 col0" >5 <span style="color: grey">(6.3%) </span></td>
      <td id="T_2d138_row0_col1" class="data row0 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_2d138_row0_col2" class="data row0 col2" >6 <span style="color: grey">(7.6%) </span></td>
    </tr>
    <tr>
      <th id="T_2d138_level0_row1" class="row_heading level0 row1" >Equipment</th>
      <td id="T_2d138_row1_col0" class="data row1 col0" >4 <span style="color: grey">(5.1%) </span></td>
      <td id="T_2d138_row1_col1" class="data row1 col1" >2 <span style="color: grey">(2.5%) </span></td>
      <td id="T_2d138_row1_col2" class="data row1 col2" >6 <span style="color: grey">(7.6%) </span></td>
    </tr>
    <tr>
      <th id="T_2d138_level0_row2" class="row_heading level0 row2" >Exercise selection</th>
      <td id="T_2d138_row2_col0" class="data row2 col0" >34 <span style="color: grey">(43.0%) </span></td>
      <td id="T_2d138_row2_col1" class="data row2 col1" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_2d138_row2_col2" class="data row2 col2" >37 <span style="color: grey">(46.8%) </span></td>
    </tr>
    <tr>
      <th id="T_2d138_level0_row3" class="row_heading level0 row3" >Intensity</th>
      <td id="T_2d138_row3_col0" class="data row3 col0" >24 <span style="color: grey">(30.4%) </span></td>
      <td id="T_2d138_row3_col1" class="data row3 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_2d138_row3_col2" class="data row3 col2" >25 <span style="color: grey">(31.6%) </span></td>
    </tr>
    <tr>
      <th id="T_2d138_level0_row4" class="row_heading level0 row4" >Motivationsstrategie</th>
      <td id="T_2d138_row4_col0" class="data row4 col0" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_2d138_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_2d138_row4_col2" class="data row4 col2" >1 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_2d138_level0_row5" class="row_heading level0 row5" >Setting</th>
      <td id="T_2d138_row5_col0" class="data row5 col0" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_2d138_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_2d138_row5_col2" class="data row5 col2" >3 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_2d138_level0_row6" class="row_heading level0 row6" >Weiteres</th>
      <td id="T_2d138_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2d138_row6_col1" class="data row6 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_2d138_row6_col2" class="data row6 col2" >1 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_2d138_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_2d138_row7_col0" class="data row7 col0" >71 <span style="color: grey">(89.9%) </span></td>
      <td id="T_2d138_row7_col1" class="data row7 col1" >8 <span style="color: grey">(10.1%) </span></td>
      <td id="T_2d138_row7_col2" class="data row7 col2" >79 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_51bbb th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_51bbb  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_51bbb_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.0%, transparent 13.0%);
  font-family: Courier;
}
#T_51bbb_row0_col1, #T_51bbb_row2_col0 {
  width: 10em;
  font-family: Courier;
}
#T_51bbb_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_51bbb_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.4%, transparent 17.4%);
  font-family: Courier;
}
#T_51bbb_row1_col1, #T_51bbb_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_51bbb_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.3%, transparent 17.3%);
  font-family: Courier;
}
#T_51bbb_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_51bbb_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.6%, transparent 69.6%);
  font-family: Courier;
}
#T_51bbb_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_51bbb_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.2%, transparent 69.2%);
  font-family: Courier;
}
#T_51bbb_row4_col0, #T_51bbb_row4_col1, #T_51bbb_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_51bbb">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_51bbb_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_51bbb_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_51bbb_level0_col2" class="col_heading level0 col2" >Total</th>
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
      <th id="T_51bbb_level0_row0" class="row_heading level0 row0" >Ab jetzt für alle Bewegungseinheiten mit allen Patient*innen</th>
      <td id="T_51bbb_row0_col0" class="data row0 col0" >6 <span style="color: grey">(11.5%) </span></td>
      <td id="T_51bbb_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_51bbb_row0_col2" class="data row0 col2" >6 <span style="color: grey">(11.5%) </span></td>
    </tr>
    <tr>
      <th id="T_51bbb_level0_row1" class="row_heading level0 row1" >Für die gesamte Therapiephase</th>
      <td id="T_51bbb_row1_col0" class="data row1 col0" >8 <span style="color: grey">(15.4%) </span></td>
      <td id="T_51bbb_row1_col1" class="data row1 col1" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_51bbb_row1_col2" class="data row1 col2" >9 <span style="color: grey">(17.3%) </span></td>
    </tr>
    <tr>
      <th id="T_51bbb_level0_row2" class="row_heading level0 row2" >Für die nächsten Einheiten (da das AE rückwirkend auftrat</th>
      <td id="T_51bbb_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_51bbb_row2_col1" class="data row2 col1" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_51bbb_row2_col2" class="data row2 col2" >1 <span style="color: grey">(1.9%) </span></td>
    </tr>
    <tr>
      <th id="T_51bbb_level0_row3" class="row_heading level0 row3" >Nur für diese Einheit</th>
      <td id="T_51bbb_row3_col0" class="data row3 col0" >32 <span style="color: grey">(61.5%) </span></td>
      <td id="T_51bbb_row3_col1" class="data row3 col1" >4 <span style="color: grey">(7.7%) </span></td>
      <td id="T_51bbb_row3_col2" class="data row3 col2" >36 <span style="color: grey">(69.2%) </span></td>
    </tr>
    <tr>
      <th id="T_51bbb_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_51bbb_row4_col0" class="data row4 col0" >46 <span style="color: grey">(88.5%) </span></td>
      <td id="T_51bbb_row4_col1" class="data row4 col1" >6 <span style="color: grey">(11.5%) </span></td>
      <td id="T_51bbb_row4_col2" class="data row4 col2" >52 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_a86d1 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a86d1  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a86d1_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.2%, transparent 90.2%);
  font-family: Courier;
}
#T_a86d1_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 65.4%, transparent 65.4%);
  font-family: Courier;
}
#T_a86d1_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_a86d1_row0_col3, #T_a86d1_row2_col2, #T_a86d1_row2_col3, #T_a86d1_row3_col1, #T_a86d1_row3_col2, #T_a86d1_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_a86d1_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 83.8%, transparent 83.8%);
  font-family: Courier;
}
#T_a86d1_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.0%, transparent 6.0%);
  font-family: Courier;
}
#T_a86d1_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_a86d1_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_a86d1_row1_col3, #T_a86d1_row4_col0, #T_a86d1_row4_col1, #T_a86d1_row4_col2, #T_a86d1_row4_col3, #T_a86d1_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_a86d1_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_a86d1_row2_col0, #T_a86d1_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_a86d1_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_a86d1_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_a86d1_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_a86d1">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_a86d1_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_a86d1_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_a86d1_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_a86d1_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_a86d1_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_a86d1_level0_row0" class="row_heading level0 row0" >Acute therapy</th>
      <td id="T_a86d1_row0_col0" class="data row0 col0" >166 <span style="color: grey">(69.2%) </span></td>
      <td id="T_a86d1_row0_col1" class="data row0 col1" >34 <span style="color: grey">(14.2%) </span></td>
      <td id="T_a86d1_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a86d1_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_a86d1_row0_col4" class="data row0 col4" >201 <span style="color: grey">(83.8%) </span></td>
    </tr>
    <tr>
      <th id="T_a86d1_level0_row1" class="row_heading level0 row1" >Aftercare</th>
      <td id="T_a86d1_row1_col0" class="data row1 col0" >11 <span style="color: grey">(4.6%) </span></td>
      <td id="T_a86d1_row1_col1" class="data row1 col1" >16 <span style="color: grey">(6.7%) </span></td>
      <td id="T_a86d1_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_a86d1_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a86d1_row1_col4" class="data row1 col4" >30 <span style="color: grey">(12.5%) </span></td>
    </tr>
    <tr>
      <th id="T_a86d1_level0_row2" class="row_heading level0 row2" >Long-term therapy</th>
      <td id="T_a86d1_row2_col0" class="data row2 col0" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_a86d1_row2_col1" class="data row2 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_a86d1_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_a86d1_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_a86d1_row2_col4" class="data row2 col4" >8 <span style="color: grey">(3.3%) </span></td>
    </tr>
    <tr>
      <th id="T_a86d1_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_a86d1_row3_col0" class="data row3 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a86d1_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_a86d1_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_a86d1_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_a86d1_row3_col4" class="data row3 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_a86d1_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_a86d1_row4_col0" class="data row4 col0" >184 <span style="color: grey">(76.7%) </span></td>
      <td id="T_a86d1_row4_col1" class="data row4 col1" >52 <span style="color: grey">(21.7%) </span></td>
      <td id="T_a86d1_row4_col2" class="data row4 col2" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_a86d1_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_a86d1_row4_col4" class="data row4 col4" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_88a1d th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_88a1d  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_88a1d_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_88a1d_row0_col1, #T_88a1d_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_88a1d_row0_col2, #T_88a1d_row0_col3, #T_88a1d_row1_col3, #T_88a1d_row2_col0, #T_88a1d_row2_col2, #T_88a1d_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_88a1d_row0_col4, #T_88a1d_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_88a1d_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_88a1d_row1_col1, #T_88a1d_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_88a1d_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_88a1d_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.7%, transparent 96.7%);
  font-family: Courier;
}
#T_88a1d_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 73.1%, transparent 73.1%);
  font-family: Courier;
}
#T_88a1d_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_88a1d_row3_col3, #T_88a1d_row4_col0, #T_88a1d_row4_col1, #T_88a1d_row4_col2, #T_88a1d_row4_col3, #T_88a1d_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_88a1d_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.1%, transparent 91.1%);
  font-family: Courier;
}
</style>
<table id="T_88a1d">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_88a1d_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_88a1d_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_88a1d_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_88a1d_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_88a1d_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_88a1d_level0_row0" class="row_heading level0 row0" >Group 2-5</th>
      <td id="T_88a1d_row0_col0" class="data row0 col0" >4 <span style="color: grey">(1.7%) </span></td>
      <td id="T_88a1d_row0_col1" class="data row0 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_88a1d_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_88a1d_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88a1d_row0_col4" class="data row0 col4" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_88a1d_level0_row1" class="row_heading level0 row1" >Group 5 to 10</th>
      <td id="T_88a1d_row1_col0" class="data row1 col0" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_88a1d_row1_col1" class="data row1 col1" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_88a1d_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_88a1d_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88a1d_row1_col4" class="data row1 col4" >9 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_88a1d_level0_row2" class="row_heading level0 row2" >Group over 10</th>
      <td id="T_88a1d_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_88a1d_row2_col1" class="data row2 col1" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_88a1d_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_88a1d_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88a1d_row2_col4" class="data row2 col4" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_88a1d_level0_row3" class="row_heading level0 row3" >Individual</th>
      <td id="T_88a1d_row3_col0" class="data row3 col0" >174 <span style="color: grey">(73.7%) </span></td>
      <td id="T_88a1d_row3_col1" class="data row3 col1" >38 <span style="color: grey">(16.1%) </span></td>
      <td id="T_88a1d_row3_col2" class="data row3 col2" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_88a1d_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_88a1d_row3_col4" class="data row3 col4" >215 <span style="color: grey">(91.1%) </span></td>
    </tr>
    <tr>
      <th id="T_88a1d_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_88a1d_row4_col0" class="data row4 col0" >180 <span style="color: grey">(76.3%) </span></td>
      <td id="T_88a1d_row4_col1" class="data row4 col1" >52 <span style="color: grey">(22.0%) </span></td>
      <td id="T_88a1d_row4_col2" class="data row4 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_88a1d_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_88a1d_row4_col4" class="data row4 col4" >236 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e3665 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e3665  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e3665_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_e3665_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.9%, transparent 27.9%);
  font-family: Courier;
}
#T_e3665_row0_col2, #T_e3665_row0_col3, #T_e3665_row1_col2, #T_e3665_row1_col3, #T_e3665_row2_col2, #T_e3665_row2_col3, #T_e3665_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_e3665_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.9%, transparent 14.9%);
  font-family: Courier;
}
#T_e3665_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.8%, transparent 37.8%);
  font-family: Courier;
}
#T_e3665_row1_col1, #T_e3665_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.6%, transparent 25.6%);
  font-family: Courier;
}
#T_e3665_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.4%, transparent 34.4%);
  font-family: Courier;
}
#T_e3665_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.1%, transparent 31.1%);
  font-family: Courier;
}
#T_e3665_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.2%, transparent 29.2%);
  font-family: Courier;
}
#T_e3665_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.9%, transparent 16.9%);
  font-family: Courier;
}
#T_e3665_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
#T_e3665_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_e3665_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.4%, transparent 16.4%);
  font-family: Courier;
}
#T_e3665_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_e3665_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.0%, transparent 7.0%);
  font-family: Courier;
}
#T_e3665_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_e3665_row4_col3, #T_e3665_row5_col0, #T_e3665_row5_col1, #T_e3665_row5_col2, #T_e3665_row5_col3, #T_e3665_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e3665_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.1%, transparent 5.1%);
  font-family: Courier;
}
</style>
<table id="T_e3665">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e3665_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e3665_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e3665_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e3665_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_e3665_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_e3665_level0_row0" class="row_heading level0 row0" >02 to 05 years</th>
      <td id="T_e3665_row0_col0" class="data row0 col0" >17 <span style="color: grey">(8.7%) </span></td>
      <td id="T_e3665_row0_col1" class="data row0 col1" >12 <span style="color: grey">(6.2%) </span></td>
      <td id="T_e3665_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e3665_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e3665_row0_col4" class="data row0 col4" >29 <span style="color: grey">(14.9%) </span></td>
    </tr>
    <tr>
      <th id="T_e3665_level0_row1" class="row_heading level0 row1" >06 to 09 years</th>
      <td id="T_e3665_row1_col0" class="data row1 col0" >56 <span style="color: grey">(28.7%) </span></td>
      <td id="T_e3665_row1_col1" class="data row1 col1" >11 <span style="color: grey">(5.6%) </span></td>
      <td id="T_e3665_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e3665_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e3665_row1_col4" class="data row1 col4" >67 <span style="color: grey">(34.4%) </span></td>
    </tr>
    <tr>
      <th id="T_e3665_level0_row2" class="row_heading level0 row2" >10 to 14 years</th>
      <td id="T_e3665_row2_col0" class="data row2 col0" >46 <span style="color: grey">(23.6%) </span></td>
      <td id="T_e3665_row2_col1" class="data row2 col1" >11 <span style="color: grey">(5.6%) </span></td>
      <td id="T_e3665_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e3665_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e3665_row2_col4" class="data row2 col4" >57 <span style="color: grey">(29.2%) </span></td>
    </tr>
    <tr>
      <th id="T_e3665_level0_row3" class="row_heading level0 row3" >15 to 18 years</th>
      <td id="T_e3665_row3_col0" class="data row3 col0" >25 <span style="color: grey">(12.8%) </span></td>
      <td id="T_e3665_row3_col1" class="data row3 col1" >6 <span style="color: grey">(3.1%) </span></td>
      <td id="T_e3665_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e3665_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e3665_row3_col4" class="data row3 col4" >32 <span style="color: grey">(16.4%) </span></td>
    </tr>
    <tr>
      <th id="T_e3665_level0_row4" class="row_heading level0 row4" >18+ years</th>
      <td id="T_e3665_row4_col0" class="data row4 col0" >4 <span style="color: grey">(2.1%) </span></td>
      <td id="T_e3665_row4_col1" class="data row4 col1" >3 <span style="color: grey">(1.5%) </span></td>
      <td id="T_e3665_row4_col2" class="data row4 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_e3665_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e3665_row4_col4" class="data row4 col4" >10 <span style="color: grey">(5.1%) </span></td>
    </tr>
    <tr>
      <th id="T_e3665_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_e3665_row5_col0" class="data row5 col0" >148 <span style="color: grey">(75.9%) </span></td>
      <td id="T_e3665_row5_col1" class="data row5 col1" >43 <span style="color: grey">(22.1%) </span></td>
      <td id="T_e3665_row5_col2" class="data row5 col2" >3 <span style="color: grey">(1.5%) </span></td>
      <td id="T_e3665_row5_col3" class="data row5 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e3665_row5_col4" class="data row5 col4" >195 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_cd253 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cd253  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_cd253_row0_col0, #T_cd253_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.7%, transparent 96.7%);
  font-family: Courier;
}
#T_cd253_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_cd253_row0_col2, #T_cd253_row0_col3, #T_cd253_row2_col0, #T_cd253_row2_col1, #T_cd253_row2_col2, #T_cd253_row2_col3, #T_cd253_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_cd253_row1_col0, #T_cd253_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_cd253_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_cd253_row1_col2, #T_cd253_row1_col3 {
  width: 10em;
  font-family: Courier;
}
</style>
<table id="T_cd253">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_cd253_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_cd253_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_cd253_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_cd253_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_cd253_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_cd253_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_cd253_row0_col0" class="data row0 col0" >177 <span style="color: grey">(74.1%) </span></td>
      <td id="T_cd253_row0_col1" class="data row0 col1" >50 <span style="color: grey">(20.9%) </span></td>
      <td id="T_cd253_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cd253_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_cd253_row0_col4" class="data row0 col4" >231 <span style="color: grey">(96.7%) </span></td>
    </tr>
    <tr>
      <th id="T_cd253_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_cd253_row1_col0" class="data row1 col0" >6 <span style="color: grey">(2.5%) </span></td>
      <td id="T_cd253_row1_col1" class="data row1 col1" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_cd253_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cd253_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cd253_row1_col4" class="data row1 col4" >8 <span style="color: grey">(3.3%) </span></td>
    </tr>
    <tr>
      <th id="T_cd253_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_cd253_row2_col0" class="data row2 col0" >183 <span style="color: grey">(76.6%) </span></td>
      <td id="T_cd253_row2_col1" class="data row2 col1" >52 <span style="color: grey">(21.8%) </span></td>
      <td id="T_cd253_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cd253_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_cd253_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_4d9a7 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_4d9a7  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_4d9a7_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.3%, transparent 97.3%);
  font-family: Courier;
}
#T_4d9a7_row0_col1, #T_4d9a7_row0_col2, #T_4d9a7_row0_col3, #T_4d9a7_row2_col0, #T_4d9a7_row2_col1, #T_4d9a7_row2_col2, #T_4d9a7_row2_col3, #T_4d9a7_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_4d9a7_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.9%, transparent 97.9%);
  font-family: Courier;
}
#T_4d9a7_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_4d9a7_row1_col1, #T_4d9a7_row1_col2, #T_4d9a7_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_4d9a7_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
</style>
<table id="T_4d9a7">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_4d9a7_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_4d9a7_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_4d9a7_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_4d9a7_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_4d9a7_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_4d9a7_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_4d9a7_row0_col0" class="data row0 col0" >179 <span style="color: grey">(74.9%) </span></td>
      <td id="T_4d9a7_row0_col1" class="data row0 col1" >51 <span style="color: grey">(21.3%) </span></td>
      <td id="T_4d9a7_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_4d9a7_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_4d9a7_row0_col4" class="data row0 col4" >234 <span style="color: grey">(97.9%) </span></td>
    </tr>
    <tr>
      <th id="T_4d9a7_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_4d9a7_row1_col0" class="data row1 col0" >5 <span style="color: grey">(2.1%) </span></td>
      <td id="T_4d9a7_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_4d9a7_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_4d9a7_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_4d9a7_row1_col4" class="data row1 col4" >5 <span style="color: grey">(2.1%) </span></td>
    </tr>
    <tr>
      <th id="T_4d9a7_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_4d9a7_row2_col0" class="data row2 col0" >184 <span style="color: grey">(77.0%) </span></td>
      <td id="T_4d9a7_row2_col1" class="data row2 col1" >51 <span style="color: grey">(21.3%) </span></td>
      <td id="T_4d9a7_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_4d9a7_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_4d9a7_row2_col4" class="data row2 col4" >239 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_59c0a th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_59c0a  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_59c0a_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_59c0a_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_59c0a_row0_col2, #T_59c0a_row0_col3, #T_59c0a_row1_col3, #T_59c0a_row2_col2, #T_59c0a_row2_col3, #T_59c0a_row4_col2, #T_59c0a_row4_col3, #T_59c0a_row5_col1, #T_59c0a_row5_col2, #T_59c0a_row5_col3 {
  width: 10em;
  font-family: Courier;
}
#T_59c0a_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_59c0a_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.6%, transparent 37.6%);
  font-family: Courier;
}
#T_59c0a_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 48.0%, transparent 48.0%);
  font-family: Courier;
}
#T_59c0a_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_59c0a_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.2%, transparent 40.2%);
  font-family: Courier;
}
#T_59c0a_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.3%, transparent 25.3%);
  font-family: Courier;
}
#T_59c0a_row2_col1, #T_59c0a_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.0%, transparent 18.0%);
  font-family: Courier;
}
#T_59c0a_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.2%, transparent 23.2%);
  font-family: Courier;
}
#T_59c0a_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.1%, transparent 4.1%);
  font-family: Courier;
}
#T_59c0a_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_59c0a_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_59c0a_row3_col3, #T_59c0a_row6_col0, #T_59c0a_row6_col1, #T_59c0a_row6_col2, #T_59c0a_row6_col3, #T_59c0a_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_59c0a_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_59c0a_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.4%, transparent 29.4%);
  font-family: Courier;
}
#T_59c0a_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.3%, transparent 26.3%);
  font-family: Courier;
}
#T_59c0a_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_59c0a_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_59c0a">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_59c0a_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_59c0a_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_59c0a_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_59c0a_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_59c0a_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_59c0a_level0_row0" class="row_heading level0 row0" >At home (via telemedicine)</th>
      <td id="T_59c0a_row0_col0" class="data row0 col0" >5 <span style="color: grey">(2.2%) </span></td>
      <td id="T_59c0a_row0_col1" class="data row0 col1" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_59c0a_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row0_col4" class="data row0 col4" >7 <span style="color: grey">(3.1%) </span></td>
    </tr>
    <tr>
      <th id="T_59c0a_level0_row1" class="row_heading level0 row1" >Gym</th>
      <td id="T_59c0a_row1_col0" class="data row1 col0" >64 <span style="color: grey">(28.6%) </span></td>
      <td id="T_59c0a_row1_col1" class="data row1 col1" >24 <span style="color: grey">(10.7%) </span></td>
      <td id="T_59c0a_row1_col2" class="data row1 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_59c0a_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row1_col4" class="data row1 col4" >90 <span style="color: grey">(40.2%) </span></td>
    </tr>
    <tr>
      <th id="T_59c0a_level0_row2" class="row_heading level0 row2" >Hospital corridor</th>
      <td id="T_59c0a_row2_col0" class="data row2 col0" >43 <span style="color: grey">(19.2%) </span></td>
      <td id="T_59c0a_row2_col1" class="data row2 col1" >9 <span style="color: grey">(4.0%) </span></td>
      <td id="T_59c0a_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row2_col4" class="data row2 col4" >52 <span style="color: grey">(23.2%) </span></td>
    </tr>
    <tr>
      <th id="T_59c0a_level0_row3" class="row_heading level0 row3" >Outside</th>
      <td id="T_59c0a_row3_col0" class="data row3 col0" >7 <span style="color: grey">(3.1%) </span></td>
      <td id="T_59c0a_row3_col1" class="data row3 col1" >6 <span style="color: grey">(2.7%) </span></td>
      <td id="T_59c0a_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_59c0a_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_59c0a_row3_col4" class="data row3 col4" >15 <span style="color: grey">(6.7%) </span></td>
    </tr>
    <tr>
      <th id="T_59c0a_level0_row4" class="row_heading level0 row4" >Patients room</th>
      <td id="T_59c0a_row4_col0" class="data row4 col0" >50 <span style="color: grey">(22.3%) </span></td>
      <td id="T_59c0a_row4_col1" class="data row4 col1" >9 <span style="color: grey">(4.0%) </span></td>
      <td id="T_59c0a_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row4_col4" class="data row4 col4" >59 <span style="color: grey">(26.3%) </span></td>
    </tr>
    <tr>
      <th id="T_59c0a_level0_row5" class="row_heading level0 row5" >Weiteres</th>
      <td id="T_59c0a_row5_col0" class="data row5 col0" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_59c0a_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_59c0a_row5_col4" class="data row5 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_59c0a_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_59c0a_row6_col0" class="data row6 col0" >170 <span style="color: grey">(75.9%) </span></td>
      <td id="T_59c0a_row6_col1" class="data row6 col1" >50 <span style="color: grey">(22.3%) </span></td>
      <td id="T_59c0a_row6_col2" class="data row6 col2" >3 <span style="color: grey">(1.3%) </span></td>
      <td id="T_59c0a_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_59c0a_row6_col4" class="data row6 col4" >224 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_88334 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_88334  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_88334_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.6%, transparent 36.6%);
  font-family: Courier;
}
#T_88334_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.3%, transparent 35.3%);
  font-family: Courier;
}
#T_88334_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.0%, transparent 75.0%);
  font-family: Courier;
}
#T_88334_row0_col3, #T_88334_row7_col0, #T_88334_row7_col1, #T_88334_row7_col2, #T_88334_row7_col3, #T_88334_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_88334_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.0%, transparent 37.0%);
  font-family: Courier;
}
#T_88334_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.8%, transparent 21.8%);
  font-family: Courier;
}
#T_88334_row1_col1, #T_88334_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.6%, transparent 20.6%);
  font-family: Courier;
}
#T_88334_row1_col2, #T_88334_row1_col3, #T_88334_row2_col2, #T_88334_row2_col3, #T_88334_row3_col2, #T_88334_row3_col3, #T_88334_row4_col1, #T_88334_row4_col2, #T_88334_row4_col3, #T_88334_row5_col2, #T_88334_row5_col3, #T_88334_row6_col3 {
  width: 10em;
  font-family: Courier;
}
#T_88334_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.2%, transparent 21.2%);
  font-family: Courier;
}
#T_88334_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.7%, transparent 9.7%);
  font-family: Courier;
}
#T_88334_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_88334_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.4%, transparent 8.4%);
  font-family: Courier;
}
#T_88334_row3_col0, #T_88334_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.8%, transparent 11.8%);
  font-family: Courier;
}
#T_88334_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.6%, transparent 11.6%);
  font-family: Courier;
}
#T_88334_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_88334_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_88334_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_88334_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.4%, transparent 7.4%);
  font-family: Courier;
}
#T_88334_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.5%, transparent 3.5%);
  font-family: Courier;
}
#T_88334_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.0%, transparent 16.0%);
  font-family: Courier;
}
#T_88334_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_88334_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.0%, transparent 17.0%);
  font-family: Courier;
}
</style>
<table id="T_88334">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_88334_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_88334_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_88334_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_88334_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_88334_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_88334_level0_row0" class="row_heading level0 row0" >Coordination</th>
      <td id="T_88334_row0_col0" class="data row0 col0" >87 <span style="color: grey">(28.0%) </span></td>
      <td id="T_88334_row0_col1" class="data row0 col1" >24 <span style="color: grey">(7.7%) </span></td>
      <td id="T_88334_row0_col2" class="data row0 col2" >3 <span style="color: grey">(1.0%) </span></td>
      <td id="T_88334_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_88334_row0_col4" class="data row0 col4" >115 <span style="color: grey">(37.0%) </span></td>
    </tr>
    <tr>
      <th id="T_88334_level0_row1" class="row_heading level0 row1" >Endurance</th>
      <td id="T_88334_row1_col0" class="data row1 col0" >52 <span style="color: grey">(16.7%) </span></td>
      <td id="T_88334_row1_col1" class="data row1 col1" >14 <span style="color: grey">(4.5%) </span></td>
      <td id="T_88334_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row1_col4" class="data row1 col4" >66 <span style="color: grey">(21.2%) </span></td>
    </tr>
    <tr>
      <th id="T_88334_level0_row2" class="row_heading level0 row2" >Flexibility</th>
      <td id="T_88334_row2_col0" class="data row2 col0" >23 <span style="color: grey">(7.4%) </span></td>
      <td id="T_88334_row2_col1" class="data row2 col1" >3 <span style="color: grey">(1.0%) </span></td>
      <td id="T_88334_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row2_col4" class="data row2 col4" >26 <span style="color: grey">(8.4%) </span></td>
    </tr>
    <tr>
      <th id="T_88334_level0_row3" class="row_heading level0 row3" >Full body</th>
      <td id="T_88334_row3_col0" class="data row3 col0" >28 <span style="color: grey">(9.0%) </span></td>
      <td id="T_88334_row3_col1" class="data row3 col1" >8 <span style="color: grey">(2.6%) </span></td>
      <td id="T_88334_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row3_col4" class="data row3 col4" >36 <span style="color: grey">(11.6%) </span></td>
    </tr>
    <tr>
      <th id="T_88334_level0_row4" class="row_heading level0 row4" >Relaxation</th>
      <td id="T_88334_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_88334_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row4_col4" class="data row4 col4" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_88334_level0_row5" class="row_heading level0 row5" >Speed</th>
      <td id="T_88334_row5_col0" class="data row5 col0" >6 <span style="color: grey">(1.9%) </span></td>
      <td id="T_88334_row5_col1" class="data row5 col1" >5 <span style="color: grey">(1.6%) </span></td>
      <td id="T_88334_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row5_col4" class="data row5 col4" >11 <span style="color: grey">(3.5%) </span></td>
    </tr>
    <tr>
      <th id="T_88334_level0_row6" class="row_heading level0 row6" >Strength</th>
      <td id="T_88334_row6_col0" class="data row6 col0" >38 <span style="color: grey">(12.2%) </span></td>
      <td id="T_88334_row6_col1" class="data row6 col1" >14 <span style="color: grey">(4.5%) </span></td>
      <td id="T_88334_row6_col2" class="data row6 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_88334_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_88334_row6_col4" class="data row6 col4" >53 <span style="color: grey">(17.0%) </span></td>
    </tr>
    <tr>
      <th id="T_88334_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_88334_row7_col0" class="data row7 col0" >238 <span style="color: grey">(76.5%) </span></td>
      <td id="T_88334_row7_col1" class="data row7 col1" >68 <span style="color: grey">(21.9%) </span></td>
      <td id="T_88334_row7_col2" class="data row7 col2" >4 <span style="color: grey">(1.3%) </span></td>
      <td id="T_88334_row7_col3" class="data row7 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_88334_row7_col4" class="data row7 col4" >311 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_15821 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_15821  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_15821_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.3%, transparent 47.3%);
  font-family: Courier;
}
#T_15821_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_15821_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_15821_row0_col3, #T_15821_row2_col0, #T_15821_row2_col2, #T_15821_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_15821_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.6%, transparent 40.6%);
  font-family: Courier;
}
#T_15821_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.7%, transparent 52.7%);
  font-family: Courier;
}
#T_15821_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.0%, transparent 81.0%);
  font-family: Courier;
}
#T_15821_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_15821_row1_col3, #T_15821_row3_col0, #T_15821_row3_col1, #T_15821_row3_col2, #T_15821_row3_col3, #T_15821_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_15821_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.9%, transparent 58.9%);
  font-family: Courier;
}
#T_15821_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_15821_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_15821">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_15821_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_15821_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_15821_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_15821_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_15821_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_15821_level0_row0" class="row_heading level0 row0" >1. Time point</th>
      <td id="T_15821_row0_col0" class="data row0 col0" >69 <span style="color: grey">(35.9%) </span></td>
      <td id="T_15821_row0_col1" class="data row0 col1" >7 <span style="color: grey">(3.6%) </span></td>
      <td id="T_15821_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_15821_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_15821_row0_col4" class="data row0 col4" >78 <span style="color: grey">(40.6%) </span></td>
    </tr>
    <tr>
      <th id="T_15821_level0_row1" class="row_heading level0 row1" >2. Time point</th>
      <td id="T_15821_row1_col0" class="data row1 col0" >77 <span style="color: grey">(40.1%) </span></td>
      <td id="T_15821_row1_col1" class="data row1 col1" >34 <span style="color: grey">(17.7%) </span></td>
      <td id="T_15821_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_15821_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_15821_row1_col4" class="data row1 col4" >113 <span style="color: grey">(58.9%) </span></td>
    </tr>
    <tr>
      <th id="T_15821_level0_row2" class="row_heading level0 row2" >Nach Abschluß der Therapie</th>
      <td id="T_15821_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_15821_row2_col1" class="data row2 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_15821_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_15821_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_15821_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_15821_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_15821_row3_col0" class="data row3 col0" >146 <span style="color: grey">(76.0%) </span></td>
      <td id="T_15821_row3_col1" class="data row3 col1" >42 <span style="color: grey">(21.9%) </span></td>
      <td id="T_15821_row3_col2" class="data row3 col2" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_15821_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_15821_row3_col4" class="data row3 col4" >192 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_df009 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_df009  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_df009_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.6%, transparent 27.6%);
  font-family: Courier;
}
#T_df009_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_df009_row0_col2, #T_df009_row1_col2, #T_df009_row1_col3, #T_df009_row2_col3, #T_df009_row3_col1, #T_df009_row3_col2, #T_df009_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_df009_row0_col3, #T_df009_row2_col2, #T_df009_row4_col0, #T_df009_row4_col1, #T_df009_row4_col2, #T_df009_row4_col3, #T_df009_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_df009_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.2%, transparent 28.2%);
  font-family: Courier;
}
#T_df009_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.9%, transparent 15.9%);
  font-family: Courier;
}
#T_df009_row1_col1, #T_df009_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_df009_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 54.5%, transparent 54.5%);
  font-family: Courier;
}
#T_df009_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 53.8%, transparent 53.8%);
  font-family: Courier;
}
#T_df009_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 54.8%, transparent 54.8%);
  font-family: Courier;
}
#T_df009_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
#T_df009_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
</style>
<table id="T_df009">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_df009_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_df009_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_df009_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_df009_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_df009_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_df009_level0_row0" class="row_heading level0 row0" >Average</th>
      <td id="T_df009_row0_col0" class="data row0 col0" >40 <span style="color: grey">(21.3%) </span></td>
      <td id="T_df009_row0_col1" class="data row0 col1" >12 <span style="color: grey">(6.4%) </span></td>
      <td id="T_df009_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_df009_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_df009_row0_col4" class="data row0 col4" >53 <span style="color: grey">(28.2%) </span></td>
    </tr>
    <tr>
      <th id="T_df009_level0_row1" class="row_heading level0 row1" >Good</th>
      <td id="T_df009_row1_col0" class="data row1 col0" >23 <span style="color: grey">(12.2%) </span></td>
      <td id="T_df009_row1_col1" class="data row1 col1" >6 <span style="color: grey">(3.2%) </span></td>
      <td id="T_df009_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_df009_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_df009_row1_col4" class="data row1 col4" >29 <span style="color: grey">(15.4%) </span></td>
    </tr>
    <tr>
      <th id="T_df009_level0_row2" class="row_heading level0 row2" >Moderate</th>
      <td id="T_df009_row2_col0" class="data row2 col0" >79 <span style="color: grey">(42.0%) </span></td>
      <td id="T_df009_row2_col1" class="data row2 col1" >21 <span style="color: grey">(11.2%) </span></td>
      <td id="T_df009_row2_col2" class="data row2 col2" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_df009_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_df009_row2_col4" class="data row2 col4" >103 <span style="color: grey">(54.8%) </span></td>
    </tr>
    <tr>
      <th id="T_df009_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_df009_row3_col0" class="data row3 col0" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_df009_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_df009_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_df009_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_df009_row3_col4" class="data row3 col4" >3 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_df009_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_df009_row4_col0" class="data row4 col0" >145 <span style="color: grey">(77.1%) </span></td>
      <td id="T_df009_row4_col1" class="data row4 col1" >39 <span style="color: grey">(20.7%) </span></td>
      <td id="T_df009_row4_col2" class="data row4 col2" >3 <span style="color: grey">(1.6%) </span></td>
      <td id="T_df009_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_df009_row4_col4" class="data row4 col4" >188 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_3_2_'></a>[only `Exercise-related`](#toc0_)


<style type="text/css">
#T_32090 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_32090  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_32090_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.5%, transparent 20.5%);
  font-family: Courier;
}
#T_32090_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_32090_row0_col2, #T_32090_row0_col3 {
  width: 10em;
  font-family: Courier;
}
#T_32090_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_32090_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 79.5%, transparent 79.5%);
  font-family: Courier;
}
#T_32090_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 95.6%, transparent 95.6%);
  font-family: Courier;
}
#T_32090_row1_col2, #T_32090_row1_col3, #T_32090_row2_col0, #T_32090_row2_col1, #T_32090_row2_col2, #T_32090_row2_col3, #T_32090_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_32090_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 83.3%, transparent 83.3%);
  font-family: Courier;
}
</style>
<table id="T_32090">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_32090_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_32090_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_32090_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_32090_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_32090_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_32090_level0_row0" class="row_heading level0 row0" >Already present</th>
      <td id="T_32090_row0_col0" class="data row0 col0" >33 <span style="color: grey">(15.8%) </span></td>
      <td id="T_32090_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_32090_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_32090_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_32090_row0_col4" class="data row0 col4" >35 <span style="color: grey">(16.7%) </span></td>
    </tr>
    <tr>
      <th id="T_32090_level0_row1" class="row_heading level0 row1" >First occurrence</th>
      <td id="T_32090_row1_col0" class="data row1 col0" >128 <span style="color: grey">(61.2%) </span></td>
      <td id="T_32090_row1_col1" class="data row1 col1" >43 <span style="color: grey">(20.6%) </span></td>
      <td id="T_32090_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_32090_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_32090_row1_col4" class="data row1 col4" >174 <span style="color: grey">(83.3%) </span></td>
    </tr>
    <tr>
      <th id="T_32090_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_32090_row2_col0" class="data row2 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_32090_row2_col1" class="data row2 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_32090_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_32090_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_32090_row2_col4" class="data row2 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_d13e3 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d13e3  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d13e3_row0_col0, #T_d13e3_row0_col1, #T_d13e3_row0_col2, #T_d13e3_row0_col3, #T_d13e3_row0_col4, #T_d13e3_row1_col0, #T_d13e3_row1_col1, #T_d13e3_row1_col2, #T_d13e3_row1_col3, #T_d13e3_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_d13e3">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_d13e3_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_d13e3_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_d13e3_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_d13e3_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_d13e3_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_d13e3_level0_row0" class="row_heading level0 row0" >Yes</th>
      <td id="T_d13e3_row0_col0" class="data row0 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_d13e3_row0_col1" class="data row0 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_d13e3_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_d13e3_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_d13e3_row0_col4" class="data row0 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_d13e3_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_d13e3_row1_col0" class="data row1 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_d13e3_row1_col1" class="data row1 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_d13e3_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_d13e3_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_d13e3_row1_col4" class="data row1 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_9b475 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_9b475  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_9b475_row0_col0, #T_9b475_row0_col1, #T_9b475_row0_col3, #T_9b475_row1_col2, #T_9b475_row1_col3, #T_9b475_row2_col1, #T_9b475_row2_col2, #T_9b475_row2_col3, #T_9b475_row3_col1, #T_9b475_row3_col2, #T_9b475_row3_col3, #T_9b475_row4_col2, #T_9b475_row4_col3, #T_9b475_row5_col1, #T_9b475_row5_col2, #T_9b475_row5_col3, #T_9b475_row6_col2, #T_9b475_row6_col3, #T_9b475_row7_col0, #T_9b475_row7_col2, #T_9b475_row7_col3, #T_9b475_row9_col1, #T_9b475_row9_col2, #T_9b475_row9_col3, #T_9b475_row10_col1, #T_9b475_row10_col2, #T_9b475_row10_col3, #T_9b475_row11_col1, #T_9b475_row11_col2, #T_9b475_row11_col3, #T_9b475_row12_col2, #T_9b475_row12_col3, #T_9b475_row13_col2, #T_9b475_row14_col2, #T_9b475_row14_col3 {
  width: 10em;
  font-family: Courier;
}
#T_9b475_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_9b475_row0_col4, #T_9b475_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_9b475_row1_col0, #T_9b475_row14_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.6%, transparent 17.6%);
  font-family: Courier;
}
#T_9b475_row1_col1, #T_9b475_row2_col4, #T_9b475_row4_col1, #T_9b475_row5_col0, #T_9b475_row7_col1, #T_9b475_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_9b475_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.4%, transparent 13.4%);
  font-family: Courier;
}
#T_9b475_row2_col0, #T_9b475_row4_col0, #T_9b475_row10_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_9b475_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_9b475_row4_col4, #T_9b475_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_9b475_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_9b475_row6_col0, #T_9b475_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_9b475_row6_col1, #T_9b475_row14_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_9b475_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_9b475_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_9b475_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.7%, transparent 39.7%);
  font-family: Courier;
}
#T_9b475_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.3%, transparent 52.3%);
  font-family: Courier;
}
#T_9b475_row8_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_9b475_row8_col3, #T_9b475_row13_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_9b475_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.8%, transparent 42.8%);
  font-family: Courier;
}
#T_9b475_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.5%, transparent 4.5%);
  font-family: Courier;
}
#T_9b475_row9_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_9b475_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_9b475_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.3%, transparent 12.3%);
  font-family: Courier;
}
#T_9b475_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.9%, transparent 5.9%);
  font-family: Courier;
}
#T_9b475_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_9b475_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.6%, transparent 24.6%);
  font-family: Courier;
}
#T_9b475_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.6%, transparent 8.6%);
  font-family: Courier;
}
#T_9b475_row14_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.8%, transparent 13.8%);
  font-family: Courier;
}
#T_9b475_row15_col0, #T_9b475_row15_col1, #T_9b475_row15_col2, #T_9b475_row15_col3, #T_9b475_row15_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_9b475">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_9b475_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_9b475_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_9b475_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_9b475_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_9b475_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_9b475_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_9b475_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_9b475_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row0_col4" class="data row0 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_9b475_row1_col0" class="data row1 col0" >35 <span style="color: grey">(13.0%) </span></td>
      <td id="T_9b475_row1_col1" class="data row1 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9b475_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row1_col4" class="data row1 col4" >36 <span style="color: grey">(13.4%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_9b475_row2_col0" class="data row2 col0" >4 <span style="color: grey">(1.5%) </span></td>
      <td id="T_9b475_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row2_col4" class="data row2 col4" >4 <span style="color: grey">(1.5%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_9b475_row3_col0" class="data row3 col0" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_9b475_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row3_col4" class="data row3 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_9b475_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.5%) </span></td>
      <td id="T_9b475_row4_col1" class="data row4 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9b475_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row4_col4" class="data row4 col4" >5 <span style="color: grey">(1.9%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_9b475_row5_col0" class="data row5 col0" >3 <span style="color: grey">(1.1%) </span></td>
      <td id="T_9b475_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row5_col4" class="data row5 col4" >3 <span style="color: grey">(1.1%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_9b475_row6_col0" class="data row6 col0" >5 <span style="color: grey">(1.9%) </span></td>
      <td id="T_9b475_row6_col1" class="data row6 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_9b475_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row6_col4" class="data row6 col4" >7 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_9b475_row7_col0" class="data row7 col0" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row7_col1" class="data row7 col1" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9b475_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row7_col4" class="data row7 col4" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_9b475_row8_col0" class="data row8 col0" >79 <span style="color: grey">(29.4%) </span></td>
      <td id="T_9b475_row8_col1" class="data row8 col1" >34 <span style="color: grey">(12.6%) </span></td>
      <td id="T_9b475_row8_col2" class="data row8 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9b475_row8_col3" class="data row8 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9b475_row8_col4" class="data row8 col4" >115 <span style="color: grey">(42.8%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_9b475_row9_col0" class="data row9 col0" >9 <span style="color: grey">(3.3%) </span></td>
      <td id="T_9b475_row9_col1" class="data row9 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row9_col4" class="data row9 col4" >9 <span style="color: grey">(3.3%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_9b475_row10_col0" class="data row10 col0" >4 <span style="color: grey">(1.5%) </span></td>
      <td id="T_9b475_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row10_col4" class="data row10 col4" >4 <span style="color: grey">(1.5%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_9b475_row11_col0" class="data row11 col0" >5 <span style="color: grey">(1.9%) </span></td>
      <td id="T_9b475_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row11_col4" class="data row11 col4" >5 <span style="color: grey">(1.9%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_9b475_row12_col0" class="data row12 col0" >8 <span style="color: grey">(3.0%) </span></td>
      <td id="T_9b475_row12_col1" class="data row12 col1" >8 <span style="color: grey">(3.0%) </span></td>
      <td id="T_9b475_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row12_col4" class="data row12 col4" >16 <span style="color: grey">(5.9%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_9b475_row13_col0" class="data row13 col0" >6 <span style="color: grey">(2.2%) </span></td>
      <td id="T_9b475_row13_col1" class="data row13 col1" >16 <span style="color: grey">(5.9%) </span></td>
      <td id="T_9b475_row13_col2" class="data row13 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row13_col3" class="data row13 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_9b475_row13_col4" class="data row13 col4" >23 <span style="color: grey">(8.6%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_9b475_row14_col0" class="data row14 col0" >35 <span style="color: grey">(13.0%) </span></td>
      <td id="T_9b475_row14_col1" class="data row14 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_9b475_row14_col2" class="data row14 col2" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row14_col3" class="data row14 col3" ><span style="color: grey">0 </span></td>
      <td id="T_9b475_row14_col4" class="data row14 col4" >37 <span style="color: grey">(13.8%) </span></td>
    </tr>
    <tr>
      <th id="T_9b475_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_9b475_row15_col0" class="data row15 col0" >199 <span style="color: grey">(74.0%) </span></td>
      <td id="T_9b475_row15_col1" class="data row15 col1" >65 <span style="color: grey">(24.2%) </span></td>
      <td id="T_9b475_row15_col2" class="data row15 col2" >3 <span style="color: grey">(1.1%) </span></td>
      <td id="T_9b475_row15_col3" class="data row15 col3" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_9b475_row15_col4" class="data row15 col4" >269 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_8ffa6 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8ffa6  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_8ffa6_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.5%, transparent 7.5%);
  font-family: Courier;
}
#T_8ffa6_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.8%, transparent 14.8%);
  font-family: Courier;
}
#T_8ffa6_row0_col2, #T_8ffa6_row4_col2, #T_8ffa6_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_8ffa6_row0_col3, #T_8ffa6_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_8ffa6_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.3%, transparent 9.3%);
  font-family: Courier;
}
#T_8ffa6_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_8ffa6_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_8ffa6_row1_col2, #T_8ffa6_row1_col3, #T_8ffa6_row2_col2, #T_8ffa6_row2_col3, #T_8ffa6_row3_col2, #T_8ffa6_row3_col3, #T_8ffa6_row4_col3, #T_8ffa6_row5_col2, #T_8ffa6_row5_col3 {
  width: 10em;
  font-family: Courier;
}
#T_8ffa6_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.7%, transparent 2.7%);
  font-family: Courier;
}
#T_8ffa6_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_8ffa6_row2_col1, #T_8ffa6_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_8ffa6_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_8ffa6_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.4%, transparent 27.4%);
  font-family: Courier;
}
#T_8ffa6_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_8ffa6_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.1%, transparent 24.1%);
  font-family: Courier;
}
#T_8ffa6_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.5%, transparent 42.5%);
  font-family: Courier;
}
#T_8ffa6_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.9%, transparent 27.9%);
  font-family: Courier;
}
#T_8ffa6_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.5%, transparent 39.5%);
  font-family: Courier;
}
#T_8ffa6_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_8ffa6_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.5%, transparent 4.5%);
  font-family: Courier;
}
#T_8ffa6_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.3%, transparent 11.3%);
  font-family: Courier;
}
#T_8ffa6_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.1%, transparent 36.1%);
  font-family: Courier;
}
#T_8ffa6_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.3%, transparent 16.3%);
  font-family: Courier;
}
#T_8ffa6_row7_col0, #T_8ffa6_row7_col1, #T_8ffa6_row7_col2, #T_8ffa6_row7_col3, #T_8ffa6_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_8ffa6">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_8ffa6_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_8ffa6_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_8ffa6_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_8ffa6_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_8ffa6_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_8ffa6_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_8ffa6_row0_col0" class="data row0 col0" >20 <span style="color: grey">(6.0%) </span></td>
      <td id="T_8ffa6_row0_col1" class="data row0 col1" >9 <span style="color: grey">(2.7%) </span></td>
      <td id="T_8ffa6_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_8ffa6_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_8ffa6_row0_col4" class="data row0 col4" >31 <span style="color: grey">(9.3%) </span></td>
    </tr>
    <tr>
      <th id="T_8ffa6_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_8ffa6_row1_col0" class="data row1 col0" >8 <span style="color: grey">(2.4%) </span></td>
      <td id="T_8ffa6_row1_col1" class="data row1 col1" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_8ffa6_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row1_col4" class="data row1 col4" >9 <span style="color: grey">(2.7%) </span></td>
    </tr>
    <tr>
      <th id="T_8ffa6_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_8ffa6_row2_col0" class="data row2 col0" >9 <span style="color: grey">(2.7%) </span></td>
      <td id="T_8ffa6_row2_col1" class="data row2 col1" >3 <span style="color: grey">(0.9%) </span></td>
      <td id="T_8ffa6_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row2_col4" class="data row2 col4" >12 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_8ffa6_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_8ffa6_row3_col0" class="data row3 col0" >73 <span style="color: grey">(22.0%) </span></td>
      <td id="T_8ffa6_row3_col1" class="data row3 col1" >7 <span style="color: grey">(2.1%) </span></td>
      <td id="T_8ffa6_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row3_col4" class="data row3 col4" >80 <span style="color: grey">(24.1%) </span></td>
    </tr>
    <tr>
      <th id="T_8ffa6_level0_row4" class="row_heading level0 row4" >Physical strain</th>
      <td id="T_8ffa6_row4_col0" class="data row4 col0" >113 <span style="color: grey">(34.0%) </span></td>
      <td id="T_8ffa6_row4_col1" class="data row4 col1" >17 <span style="color: grey">(5.1%) </span></td>
      <td id="T_8ffa6_row4_col2" class="data row4 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_8ffa6_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row4_col4" class="data row4 col4" >131 <span style="color: grey">(39.5%) </span></td>
    </tr>
    <tr>
      <th id="T_8ffa6_level0_row5" class="row_heading level0 row5" >Psychological strain</th>
      <td id="T_8ffa6_row5_col0" class="data row5 col0" >13 <span style="color: grey">(3.9%) </span></td>
      <td id="T_8ffa6_row5_col1" class="data row5 col1" >2 <span style="color: grey">(0.6%) </span></td>
      <td id="T_8ffa6_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_8ffa6_row5_col4" class="data row5 col4" >15 <span style="color: grey">(4.5%) </span></td>
    </tr>
    <tr>
      <th id="T_8ffa6_level0_row6" class="row_heading level0 row6" >Sturzereignis</th>
      <td id="T_8ffa6_row6_col0" class="data row6 col0" >30 <span style="color: grey">(9.0%) </span></td>
      <td id="T_8ffa6_row6_col1" class="data row6 col1" >22 <span style="color: grey">(6.6%) </span></td>
      <td id="T_8ffa6_row6_col2" class="data row6 col2" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_8ffa6_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.3%) </span></td>
      <td id="T_8ffa6_row6_col4" class="data row6 col4" >54 <span style="color: grey">(16.3%) </span></td>
    </tr>
    <tr>
      <th id="T_8ffa6_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_8ffa6_row7_col0" class="data row7 col0" >266 <span style="color: grey">(80.1%) </span></td>
      <td id="T_8ffa6_row7_col1" class="data row7 col1" >61 <span style="color: grey">(18.4%) </span></td>
      <td id="T_8ffa6_row7_col2" class="data row7 col2" >3 <span style="color: grey">(0.9%) </span></td>
      <td id="T_8ffa6_row7_col3" class="data row7 col3" >2 <span style="color: grey">(0.6%) </span></td>
      <td id="T_8ffa6_row7_col4" class="data row7 col4" >332 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_66d22 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_66d22  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_66d22_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_66d22_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.0%, transparent 8.0%);
  font-family: Courier;
}
#T_66d22_row0_col2, #T_66d22_row0_col3, #T_66d22_row1_col2, #T_66d22_row1_col3, #T_66d22_row2_col2, #T_66d22_row2_col3, #T_66d22_row3_col2, #T_66d22_row3_col3, #T_66d22_row4_col1, #T_66d22_row4_col2, #T_66d22_row4_col3, #T_66d22_row5_col2, #T_66d22_row5_col3, #T_66d22_row6_col0, #T_66d22_row6_col1, #T_66d22_row6_col2, #T_66d22_row7_col2, #T_66d22_row7_col3, #T_66d22_row8_col2, #T_66d22_row8_col3, #T_66d22_row9_col1, #T_66d22_row9_col2, #T_66d22_row9_col3, #T_66d22_row10_col0, #T_66d22_row10_col2, #T_66d22_row10_col3, #T_66d22_row11_col3, #T_66d22_row12_col2, #T_66d22_row12_col3 {
  width: 10em;
  font-family: Courier;
}
#T_66d22_row0_col4, #T_66d22_row1_col4, #T_66d22_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_66d22_row1_col0, #T_66d22_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
#T_66d22_row1_col1, #T_66d22_row7_col0, #T_66d22_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.0%, transparent 6.0%);
  font-family: Courier;
}
#T_66d22_row2_col1, #T_66d22_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_66d22_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.0%, transparent 5.0%);
  font-family: Courier;
}
#T_66d22_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_66d22_row3_col1, #T_66d22_row10_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_66d22_row3_col4, #T_66d22_row9_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_66d22_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_66d22_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_66d22_row5_col0, #T_66d22_row9_col0, #T_66d22_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_66d22_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.2%, transparent 3.2%);
  font-family: Courier;
}
#T_66d22_row6_col3, #T_66d22_row11_col2, #T_66d22_row13_col0, #T_66d22_row13_col1, #T_66d22_row13_col2, #T_66d22_row13_col3, #T_66d22_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_66d22_row6_col4, #T_66d22_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_66d22_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.0%, transparent 30.0%);
  font-family: Courier;
}
#T_66d22_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.4%, transparent 11.4%);
  font-family: Courier;
}
#T_66d22_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.7%, transparent 43.7%);
  font-family: Courier;
}
#T_66d22_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.5%, transparent 34.5%);
  font-family: Courier;
}
#T_66d22_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_66d22_row11_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.0%, transparent 24.0%);
  font-family: Courier;
}
#T_66d22_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.2%, transparent 23.2%);
  font-family: Courier;
}
#T_66d22_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
</style>
<table id="T_66d22">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_66d22_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_66d22_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_66d22_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_66d22_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_66d22_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_66d22_level0_row0" class="row_heading level0 row0" >Abdomen</th>
      <td id="T_66d22_row0_col0" class="data row0 col0" >8 <span style="color: grey">(3.6%) </span></td>
      <td id="T_66d22_row0_col1" class="data row0 col1" >4 <span style="color: grey">(1.8%) </span></td>
      <td id="T_66d22_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row0_col4" class="data row0 col4" >12 <span style="color: grey">(5.5%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row1" class="row_heading level0 row1" >Back</th>
      <td id="T_66d22_row1_col0" class="data row1 col0" >9 <span style="color: grey">(4.1%) </span></td>
      <td id="T_66d22_row1_col1" class="data row1 col1" >3 <span style="color: grey">(1.4%) </span></td>
      <td id="T_66d22_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row1_col4" class="data row1 col4" >12 <span style="color: grey">(5.5%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row2" class="row_heading level0 row2" >Buttocks</th>
      <td id="T_66d22_row2_col0" class="data row2 col0" >9 <span style="color: grey">(4.1%) </span></td>
      <td id="T_66d22_row2_col1" class="data row2 col1" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_66d22_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row2_col4" class="data row2 col4" >11 <span style="color: grey">(5.0%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row3" class="row_heading level0 row3" >Chest</th>
      <td id="T_66d22_row3_col0" class="data row3 col0" >4 <span style="color: grey">(1.8%) </span></td>
      <td id="T_66d22_row3_col1" class="data row3 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_66d22_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row3_col4" class="data row3 col4" >5 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row4" class="row_heading level0 row4" >Coccyx</th>
      <td id="T_66d22_row4_col0" class="data row4 col0" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_66d22_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row4_col4" class="data row4 col4" >2 <span style="color: grey">(0.9%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row5" class="row_heading level0 row5" >Full body</th>
      <td id="T_66d22_row5_col0" class="data row5 col0" >5 <span style="color: grey">(2.3%) </span></td>
      <td id="T_66d22_row5_col1" class="data row5 col1" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_66d22_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row5_col4" class="data row5 col4" >7 <span style="color: grey">(3.2%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row6" class="row_heading level0 row6" >Hals</th>
      <td id="T_66d22_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_66d22_row6_col4" class="data row6 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row7" class="row_heading level0 row7" >Head</th>
      <td id="T_66d22_row7_col0" class="data row7 col0" >10 <span style="color: grey">(4.5%) </span></td>
      <td id="T_66d22_row7_col1" class="data row7 col1" >15 <span style="color: grey">(6.8%) </span></td>
      <td id="T_66d22_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row7_col4" class="data row7 col4" >25 <span style="color: grey">(11.4%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row8" class="row_heading level0 row8" >Innere Medizin</th>
      <td id="T_66d22_row8_col0" class="data row8 col0" >73 <span style="color: grey">(33.2%) </span></td>
      <td id="T_66d22_row8_col1" class="data row8 col1" >3 <span style="color: grey">(1.4%) </span></td>
      <td id="T_66d22_row8_col2" class="data row8 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row8_col3" class="data row8 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row8_col4" class="data row8 col4" >76 <span style="color: grey">(34.5%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row9" class="row_heading level0 row9" >Intestine</th>
      <td id="T_66d22_row9_col0" class="data row9 col0" >5 <span style="color: grey">(2.3%) </span></td>
      <td id="T_66d22_row9_col1" class="data row9 col1" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row9_col4" class="data row9 col4" >5 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row10" class="row_heading level0 row10" >Intimate area</th>
      <td id="T_66d22_row10_col0" class="data row10 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row10_col1" class="data row10 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_66d22_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row10_col4" class="data row10 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row11" class="row_heading level0 row11" >Lower extremities</th>
      <td id="T_66d22_row11_col0" class="data row11 col0" >37 <span style="color: grey">(16.8%) </span></td>
      <td id="T_66d22_row11_col1" class="data row11 col1" >12 <span style="color: grey">(5.5%) </span></td>
      <td id="T_66d22_row11_col2" class="data row11 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_66d22_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row11_col4" class="data row11 col4" >51 <span style="color: grey">(23.2%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row12" class="row_heading level0 row12" >Upper extremities</th>
      <td id="T_66d22_row12_col0" class="data row12 col0" >5 <span style="color: grey">(2.3%) </span></td>
      <td id="T_66d22_row12_col1" class="data row12 col1" >7 <span style="color: grey">(3.2%) </span></td>
      <td id="T_66d22_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66d22_row12_col4" class="data row12 col4" >12 <span style="color: grey">(5.5%) </span></td>
    </tr>
    <tr>
      <th id="T_66d22_level0_row13" class="row_heading level0 row13" >Total</th>
      <td id="T_66d22_row13_col0" class="data row13 col0" >167 <span style="color: grey">(75.9%) </span></td>
      <td id="T_66d22_row13_col1" class="data row13 col1" >50 <span style="color: grey">(22.7%) </span></td>
      <td id="T_66d22_row13_col2" class="data row13 col2" >2 <span style="color: grey">(0.9%) </span></td>
      <td id="T_66d22_row13_col3" class="data row13 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_66d22_row13_col4" class="data row13 col4" >220 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e2b7f th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2b7f  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e2b7f_row0_col0, #T_e2b7f_row0_col1, #T_e2b7f_row2_col3, #T_e2b7f_row3_col0, #T_e2b7f_row3_col1, #T_e2b7f_row3_col2, #T_e2b7f_row3_col3, #T_e2b7f_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e2b7f_row0_col2, #T_e2b7f_row0_col3, #T_e2b7f_row1_col0, #T_e2b7f_row1_col1, #T_e2b7f_row1_col3, #T_e2b7f_row2_col0, #T_e2b7f_row2_col1 {
  width: 10em;
  font-family: Courier;
}
#T_e2b7f_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.6%, transparent 98.6%);
  font-family: Courier;
}
#T_e2b7f_row1_col2, #T_e2b7f_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_e2b7f_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_e2b7f_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
</style>
<table id="T_e2b7f">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e2b7f_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e2b7f_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e2b7f_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e2b7f_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_e2b7f_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_e2b7f_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_e2b7f_row0_col0" class="data row0 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_e2b7f_row0_col1" class="data row0 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_e2b7f_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e2b7f_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e2b7f_row0_col4" class="data row0 col4" >206 <span style="color: grey">(98.6%) </span></td>
    </tr>
    <tr>
      <th id="T_e2b7f_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_e2b7f_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_e2b7f_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e2b7f_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e2b7f_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e2b7f_row1_col4" class="data row1 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_e2b7f_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_e2b7f_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_e2b7f_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e2b7f_row2_col2" class="data row2 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e2b7f_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e2b7f_row2_col4" class="data row2 col4" >2 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_e2b7f_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_e2b7f_row3_col0" class="data row3 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_e2b7f_row3_col1" class="data row3 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_e2b7f_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_e2b7f_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e2b7f_row3_col4" class="data row3 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_1815c th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_1815c  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_1815c_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 95.0%, transparent 95.0%);
  font-family: Courier;
}
#T_1815c_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.8%, transparent 17.8%);
  font-family: Courier;
}
#T_1815c_row0_col2, #T_1815c_row0_col3, #T_1815c_row1_col1, #T_1815c_row1_col2, #T_1815c_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_1815c_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 77.0%, transparent 77.0%);
  font-family: Courier;
}
#T_1815c_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_1815c_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_1815c_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_1815c_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.2%, transparent 82.2%);
  font-family: Courier;
}
#T_1815c_row2_col2, #T_1815c_row2_col3, #T_1815c_row3_col0, #T_1815c_row3_col1, #T_1815c_row3_col2, #T_1815c_row3_col3, #T_1815c_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_1815c_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.5%, transparent 22.5%);
  font-family: Courier;
}
</style>
<table id="T_1815c">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_1815c_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_1815c_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_1815c_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_1815c_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_1815c_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_1815c_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_1815c_row0_col0" class="data row0 col0" >153 <span style="color: grey">(73.2%) </span></td>
      <td id="T_1815c_row0_col1" class="data row0 col1" >8 <span style="color: grey">(3.8%) </span></td>
      <td id="T_1815c_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1815c_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1815c_row0_col4" class="data row0 col4" >161 <span style="color: grey">(77.0%) </span></td>
    </tr>
    <tr>
      <th id="T_1815c_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_1815c_row1_col0" class="data row1 col0" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_1815c_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1815c_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1815c_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1815c_row1_col4" class="data row1 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_1815c_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_1815c_row2_col0" class="data row2 col0" >7 <span style="color: grey">(3.3%) </span></td>
      <td id="T_1815c_row2_col1" class="data row2 col1" >37 <span style="color: grey">(17.7%) </span></td>
      <td id="T_1815c_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_1815c_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_1815c_row2_col4" class="data row2 col4" >47 <span style="color: grey">(22.5%) </span></td>
    </tr>
    <tr>
      <th id="T_1815c_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_1815c_row3_col0" class="data row3 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_1815c_row3_col1" class="data row3 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_1815c_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_1815c_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_1815c_row3_col4" class="data row3 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_b65b0 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_b65b0  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_b65b0_row0_col0, #T_b65b0_row0_col1, #T_b65b0_row0_col2, #T_b65b0_row0_col3, #T_b65b0_row0_col4, #T_b65b0_row1_col0, #T_b65b0_row1_col1, #T_b65b0_row1_col2, #T_b65b0_row1_col3, #T_b65b0_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_b65b0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_b65b0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_b65b0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_b65b0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_b65b0_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_b65b0_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_b65b0_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_b65b0_row0_col0" class="data row0 col0" >160 <span style="color: grey">(76.9%) </span></td>
      <td id="T_b65b0_row0_col1" class="data row0 col1" >45 <span style="color: grey">(21.6%) </span></td>
      <td id="T_b65b0_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_b65b0_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_b65b0_row0_col4" class="data row0 col4" >208 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_b65b0_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_b65b0_row1_col0" class="data row1 col0" >160 <span style="color: grey">(76.9%) </span></td>
      <td id="T_b65b0_row1_col1" class="data row1 col1" >45 <span style="color: grey">(21.6%) </span></td>
      <td id="T_b65b0_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_b65b0_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_b65b0_row1_col4" class="data row1 col4" >208 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_d6093 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d6093  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d6093_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 99.4%, transparent 99.4%);
  font-family: Courier;
}
#T_d6093_row0_col1, #T_d6093_row0_col3, #T_d6093_row1_col2, #T_d6093_row2_col0, #T_d6093_row2_col1, #T_d6093_row2_col2, #T_d6093_row2_col3, #T_d6093_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_d6093_row0_col2, #T_d6093_row1_col1, #T_d6093_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_d6093_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.6%, transparent 98.6%);
  font-family: Courier;
}
#T_d6093_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_d6093_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.4%, transparent 1.4%);
  font-family: Courier;
}
</style>
<table id="T_d6093">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_d6093_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_d6093_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_d6093_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_d6093_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_d6093_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_d6093_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_d6093_row0_col0" class="data row0 col0" >160 <span style="color: grey">(76.6%) </span></td>
      <td id="T_d6093_row0_col1" class="data row0 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_d6093_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_d6093_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_d6093_row0_col4" class="data row0 col4" >206 <span style="color: grey">(98.6%) </span></td>
    </tr>
    <tr>
      <th id="T_d6093_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_d6093_row1_col0" class="data row1 col0" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_d6093_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_d6093_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_d6093_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_d6093_row1_col4" class="data row1 col4" >3 <span style="color: grey">(1.4%) </span></td>
    </tr>
    <tr>
      <th id="T_d6093_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_d6093_row2_col0" class="data row2 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_d6093_row2_col1" class="data row2 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_d6093_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_d6093_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_d6093_row2_col4" class="data row2 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_84445 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_84445  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_84445_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 87.5%, transparent 87.5%);
  font-family: Courier;
}
#T_84445_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.0%, transparent 69.0%);
  font-family: Courier;
}
#T_84445_row0_col2, #T_84445_row0_col3, #T_84445_row1_col2, #T_84445_row1_col3, #T_84445_row2_col0 {
  width: 10em;
  font-family: Courier;
}
#T_84445_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.4%, transparent 82.4%);
  font-family: Courier;
}
#T_84445_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_84445_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.2%, transparent 26.2%);
  font-family: Courier;
}
#T_84445_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.1%, transparent 15.1%);
  font-family: Courier;
}
#T_84445_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_84445_row2_col2, #T_84445_row2_col3, #T_84445_row3_col0, #T_84445_row3_col1, #T_84445_row3_col2, #T_84445_row3_col3, #T_84445_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_84445_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
</style>
<table id="T_84445">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_84445_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_84445_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_84445_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_84445_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_84445_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_84445_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_84445_row0_col0" class="data row0 col0" >140 <span style="color: grey">(68.3%) </span></td>
      <td id="T_84445_row0_col1" class="data row0 col1" >29 <span style="color: grey">(14.1%) </span></td>
      <td id="T_84445_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_84445_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_84445_row0_col4" class="data row0 col4" >169 <span style="color: grey">(82.4%) </span></td>
    </tr>
    <tr>
      <th id="T_84445_level0_row1" class="row_heading level0 row1" >Weiß nicht</th>
      <td id="T_84445_row1_col0" class="data row1 col0" >20 <span style="color: grey">(9.8%) </span></td>
      <td id="T_84445_row1_col1" class="data row1 col1" >11 <span style="color: grey">(5.4%) </span></td>
      <td id="T_84445_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_84445_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_84445_row1_col4" class="data row1 col4" >31 <span style="color: grey">(15.1%) </span></td>
    </tr>
    <tr>
      <th id="T_84445_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_84445_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_84445_row2_col1" class="data row2 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_84445_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_84445_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_84445_row2_col4" class="data row2 col4" >5 <span style="color: grey">(2.4%) </span></td>
    </tr>
    <tr>
      <th id="T_84445_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_84445_row3_col0" class="data row3 col0" >160 <span style="color: grey">(78.0%) </span></td>
      <td id="T_84445_row3_col1" class="data row3 col1" >42 <span style="color: grey">(20.5%) </span></td>
      <td id="T_84445_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_84445_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_84445_row3_col4" class="data row3 col4" >205 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_21e92 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_21e92  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_21e92_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.9%, transparent 26.9%);
  font-family: Courier;
}
#T_21e92_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_21e92_row0_col2, #T_21e92_row0_col3, #T_21e92_row2_col0, #T_21e92_row2_col1, #T_21e92_row2_col2, #T_21e92_row2_col3, #T_21e92_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_21e92_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_21e92_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 73.1%, transparent 73.1%);
  font-family: Courier;
}
#T_21e92_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 60.0%, transparent 60.0%);
  font-family: Courier;
}
#T_21e92_row1_col2, #T_21e92_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_21e92_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.2%, transparent 69.2%);
  font-family: Courier;
}
</style>
<table id="T_21e92">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_21e92_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_21e92_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_21e92_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_21e92_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_21e92_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_21e92_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_21e92_row0_col0" class="data row0 col0" >43 <span style="color: grey">(20.7%) </span></td>
      <td id="T_21e92_row0_col1" class="data row0 col1" >18 <span style="color: grey">(8.7%) </span></td>
      <td id="T_21e92_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_21e92_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_21e92_row0_col4" class="data row0 col4" >64 <span style="color: grey">(30.8%) </span></td>
    </tr>
    <tr>
      <th id="T_21e92_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_21e92_row1_col0" class="data row1 col0" >117 <span style="color: grey">(56.2%) </span></td>
      <td id="T_21e92_row1_col1" class="data row1 col1" >27 <span style="color: grey">(13.0%) </span></td>
      <td id="T_21e92_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_21e92_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_21e92_row1_col4" class="data row1 col4" >144 <span style="color: grey">(69.2%) </span></td>
    </tr>
    <tr>
      <th id="T_21e92_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_21e92_row2_col0" class="data row2 col0" >160 <span style="color: grey">(76.9%) </span></td>
      <td id="T_21e92_row2_col1" class="data row2 col1" >45 <span style="color: grey">(21.6%) </span></td>
      <td id="T_21e92_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_21e92_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_21e92_row2_col4" class="data row2 col4" >208 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_5fc44 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_5fc44  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_5fc44_row0_col0, #T_5fc44_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_5fc44_row0_col1, #T_5fc44_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.1%, transparent 7.1%);
  font-family: Courier;
}
#T_5fc44_row0_col2, #T_5fc44_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_5fc44_row0_col3, #T_5fc44_row1_col3, #T_5fc44_row2_col3, #T_5fc44_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_5fc44_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_5fc44_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 62.5%, transparent 62.5%);
  font-family: Courier;
}
#T_5fc44_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.1%, transparent 57.1%);
  font-family: Courier;
}
#T_5fc44_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.8%, transparent 57.8%);
  font-family: Courier;
}
#T_5fc44_row2_col0, #T_5fc44_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_5fc44_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.7%, transparent 10.7%);
  font-family: Courier;
}
#T_5fc44_row2_col2, #T_5fc44_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_5fc44_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.8%, transparent 8.8%);
  font-family: Courier;
}
#T_5fc44_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.9%, transparent 17.9%);
  font-family: Courier;
}
#T_5fc44_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.7%, transparent 14.7%);
  font-family: Courier;
}
#T_5fc44_row4_col2, #T_5fc44_row4_col3 {
  width: 10em;
  font-family: Courier;
}
#T_5fc44_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.9%, transparent 5.9%);
  font-family: Courier;
}
#T_5fc44_row5_col0, #T_5fc44_row5_col1, #T_5fc44_row5_col2, #T_5fc44_row5_col3, #T_5fc44_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_5fc44">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_5fc44_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_5fc44_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_5fc44_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_5fc44_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_5fc44_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_5fc44_level0_row0" class="row_heading level0 row0" >BeIn the treatment team</th>
      <td id="T_5fc44_row0_col0" class="data row0 col0" >8 <span style="color: grey">(7.8%) </span></td>
      <td id="T_5fc44_row0_col1" class="data row0 col1" >2 <span style="color: grey">(2.0%) </span></td>
      <td id="T_5fc44_row0_col2" class="data row0 col2" >2 <span style="color: grey">(2.0%) </span></td>
      <td id="T_5fc44_row0_col3" class="data row0 col3" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fc44_row0_col4" class="data row0 col4" >13 <span style="color: grey">(12.7%) </span></td>
    </tr>
    <tr>
      <th id="T_5fc44_level0_row1" class="row_heading level0 row1" >For affected individuals</th>
      <td id="T_5fc44_row1_col0" class="data row1 col0" >40 <span style="color: grey">(39.2%) </span></td>
      <td id="T_5fc44_row1_col1" class="data row1 col1" >16 <span style="color: grey">(15.7%) </span></td>
      <td id="T_5fc44_row1_col2" class="data row1 col2" >2 <span style="color: grey">(2.0%) </span></td>
      <td id="T_5fc44_row1_col3" class="data row1 col3" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fc44_row1_col4" class="data row1 col4" >59 <span style="color: grey">(57.8%) </span></td>
    </tr>
    <tr>
      <th id="T_5fc44_level0_row2" class="row_heading level0 row2" >For parents des Betroffenen</th>
      <td id="T_5fc44_row2_col0" class="data row2 col0" >4 <span style="color: grey">(3.9%) </span></td>
      <td id="T_5fc44_row2_col1" class="data row2 col1" >3 <span style="color: grey">(2.9%) </span></td>
      <td id="T_5fc44_row2_col2" class="data row2 col2" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fc44_row2_col3" class="data row2 col3" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fc44_row2_col4" class="data row2 col4" >9 <span style="color: grey">(8.8%) </span></td>
    </tr>
    <tr>
      <th id="T_5fc44_level0_row3" class="row_heading level0 row3" >For the excercise experts</th>
      <td id="T_5fc44_row3_col0" class="data row3 col0" >8 <span style="color: grey">(7.8%) </span></td>
      <td id="T_5fc44_row3_col1" class="data row3 col1" >5 <span style="color: grey">(4.9%) </span></td>
      <td id="T_5fc44_row3_col2" class="data row3 col2" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fc44_row3_col3" class="data row3 col3" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fc44_row3_col4" class="data row3 col4" >15 <span style="color: grey">(14.7%) </span></td>
    </tr>
    <tr>
      <th id="T_5fc44_level0_row4" class="row_heading level0 row4" >Mit der Ablehnung weiterer sporttherapheutischer Angebote</th>
      <td id="T_5fc44_row4_col0" class="data row4 col0" >4 <span style="color: grey">(3.9%) </span></td>
      <td id="T_5fc44_row4_col1" class="data row4 col1" >2 <span style="color: grey">(2.0%) </span></td>
      <td id="T_5fc44_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_5fc44_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_5fc44_row4_col4" class="data row4 col4" >6 <span style="color: grey">(5.9%) </span></td>
    </tr>
    <tr>
      <th id="T_5fc44_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_5fc44_row5_col0" class="data row5 col0" >64 <span style="color: grey">(62.7%) </span></td>
      <td id="T_5fc44_row5_col1" class="data row5 col1" >28 <span style="color: grey">(27.5%) </span></td>
      <td id="T_5fc44_row5_col2" class="data row5 col2" >6 <span style="color: grey">(5.9%) </span></td>
      <td id="T_5fc44_row5_col3" class="data row5 col3" >4 <span style="color: grey">(3.9%) </span></td>
      <td id="T_5fc44_row5_col4" class="data row5 col4" >102 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_c6f21 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c6f21  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c6f21_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_c6f21_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.6%, transparent 13.6%);
  font-family: Courier;
}
#T_c6f21_row0_col2, #T_c6f21_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_c6f21_row0_col3, #T_c6f21_row1_col3, #T_c6f21_row2_col0, #T_c6f21_row2_col1, #T_c6f21_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_c6f21_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_c6f21_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 94.4%, transparent 94.4%);
  font-family: Courier;
}
#T_c6f21_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.4%, transparent 86.4%);
  font-family: Courier;
}
#T_c6f21_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.8%, transparent 91.8%);
  font-family: Courier;
}
#T_c6f21_row2_col3, #T_c6f21_row3_col0, #T_c6f21_row3_col1, #T_c6f21_row3_col2, #T_c6f21_row3_col3, #T_c6f21_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_c6f21_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_c6f21">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_c6f21_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_c6f21_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_c6f21_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_c6f21_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_c6f21_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_c6f21_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_c6f21_row0_col0" class="data row0 col0" >9 <span style="color: grey">(4.3%) </span></td>
      <td id="T_c6f21_row0_col1" class="data row0 col1" >6 <span style="color: grey">(2.9%) </span></td>
      <td id="T_c6f21_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c6f21_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c6f21_row0_col4" class="data row0 col4" >16 <span style="color: grey">(7.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c6f21_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_c6f21_row1_col0" class="data row1 col0" >152 <span style="color: grey">(73.1%) </span></td>
      <td id="T_c6f21_row1_col1" class="data row1 col1" >38 <span style="color: grey">(18.3%) </span></td>
      <td id="T_c6f21_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c6f21_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c6f21_row1_col4" class="data row1 col4" >191 <span style="color: grey">(91.8%) </span></td>
    </tr>
    <tr>
      <th id="T_c6f21_level0_row2" class="row_heading level0 row2" >Weiß nicht</th>
      <td id="T_c6f21_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c6f21_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c6f21_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c6f21_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c6f21_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_c6f21_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_c6f21_row3_col0" class="data row3 col0" >161 <span style="color: grey">(77.4%) </span></td>
      <td id="T_c6f21_row3_col1" class="data row3 col1" >44 <span style="color: grey">(21.2%) </span></td>
      <td id="T_c6f21_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_c6f21_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c6f21_row3_col4" class="data row3 col4" >208 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_dc940 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dc940  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_dc940_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.4%, transparent 81.4%);
  font-family: Courier;
}
#T_dc940_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.5%, transparent 43.5%);
  font-family: Courier;
}
#T_dc940_row0_col2, #T_dc940_row0_col3, #T_dc940_row1_col1, #T_dc940_row1_col2, #T_dc940_row1_col3, #T_dc940_row3_col2, #T_dc940_row3_col3, #T_dc940_row4_col2, #T_dc940_row4_col3, #T_dc940_row5_col2, #T_dc940_row5_col3 {
  width: 10em;
  font-family: Courier;
}
#T_dc940_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 71.9%, transparent 71.9%);
  font-family: Courier;
}
#T_dc940_row1_col0, #T_dc940_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_dc940_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_dc940_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_dc940_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.1%, transparent 39.1%);
  font-family: Courier;
}
#T_dc940_row2_col2, #T_dc940_row2_col3, #T_dc940_row6_col0, #T_dc940_row6_col1, #T_dc940_row6_col2, #T_dc940_row6_col3, #T_dc940_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_dc940_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_dc940_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.9%, transparent 9.9%);
  font-family: Courier;
}
#T_dc940_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.9%, transparent 10.9%);
  font-family: Courier;
}
#T_dc940_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_dc940_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_dc940_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_dc940_row4_col4, #T_dc940_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.4%, transparent 1.4%);
  font-family: Courier;
}
#T_dc940_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
</style>
<table id="T_dc940">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_dc940_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_dc940_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_dc940_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_dc940_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_dc940_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_dc940_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_dc940_row0_col0" class="data row0 col0" >131 <span style="color: grey">(62.4%) </span></td>
      <td id="T_dc940_row0_col1" class="data row0 col1" >20 <span style="color: grey">(9.5%) </span></td>
      <td id="T_dc940_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row0_col4" class="data row0 col4" >151 <span style="color: grey">(71.9%) </span></td>
    </tr>
    <tr>
      <th id="T_dc940_level0_row1" class="row_heading level0 row1" >Eltern</th>
      <td id="T_dc940_row1_col0" class="data row1 col0" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_dc940_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row1_col4" class="data row1 col4" >2 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_dc940_level0_row2" class="row_heading level0 row2" >Medizin</th>
      <td id="T_dc940_row2_col0" class="data row2 col0" >9 <span style="color: grey">(4.3%) </span></td>
      <td id="T_dc940_row2_col1" class="data row2 col1" >18 <span style="color: grey">(8.6%) </span></td>
      <td id="T_dc940_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_dc940_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_dc940_row2_col4" class="data row2 col4" >30 <span style="color: grey">(14.3%) </span></td>
    </tr>
    <tr>
      <th id="T_dc940_level0_row3" class="row_heading level0 row3" >Pflege</th>
      <td id="T_dc940_row3_col0" class="data row3 col0" >16 <span style="color: grey">(7.6%) </span></td>
      <td id="T_dc940_row3_col1" class="data row3 col1" >5 <span style="color: grey">(2.4%) </span></td>
      <td id="T_dc940_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row3_col4" class="data row3 col4" >21 <span style="color: grey">(10.0%) </span></td>
    </tr>
    <tr>
      <th id="T_dc940_level0_row4" class="row_heading level0 row4" >Physiotherapie</th>
      <td id="T_dc940_row4_col0" class="data row4 col0" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_dc940_row4_col1" class="data row4 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_dc940_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row4_col4" class="data row4 col4" >3 <span style="color: grey">(1.4%) </span></td>
    </tr>
    <tr>
      <th id="T_dc940_level0_row5" class="row_heading level0 row5" >Psychosozialer Dienst</th>
      <td id="T_dc940_row5_col0" class="data row5 col0" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_dc940_row5_col1" class="data row5 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_dc940_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_dc940_row5_col4" class="data row5 col4" >3 <span style="color: grey">(1.4%) </span></td>
    </tr>
    <tr>
      <th id="T_dc940_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_dc940_row6_col0" class="data row6 col0" >161 <span style="color: grey">(76.7%) </span></td>
      <td id="T_dc940_row6_col1" class="data row6 col1" >46 <span style="color: grey">(21.9%) </span></td>
      <td id="T_dc940_row6_col2" class="data row6 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_dc940_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_dc940_row6_col4" class="data row6 col4" >210 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_5fe81 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_5fe81  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_5fe81_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_5fe81_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_5fe81_row0_col2, #T_5fe81_row1_col3, #T_5fe81_row2_col0, #T_5fe81_row2_col1, #T_5fe81_row2_col2, #T_5fe81_row2_col3, #T_5fe81_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_5fe81_row0_col3, #T_5fe81_row1_col2 {
  width: 10em;
  font-family: Courier;
}
#T_5fe81_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.6%, transparent 10.6%);
  font-family: Courier;
}
#T_5fe81_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.8%, transparent 98.8%);
  font-family: Courier;
}
#T_5fe81_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 60.0%, transparent 60.0%);
  font-family: Courier;
}
#T_5fe81_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 89.4%, transparent 89.4%);
  font-family: Courier;
}
</style>
<table id="T_5fe81">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_5fe81_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_5fe81_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_5fe81_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_5fe81_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_5fe81_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_5fe81_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_5fe81_row0_col0" class="data row0 col0" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fe81_row0_col1" class="data row0 col1" >18 <span style="color: grey">(8.7%) </span></td>
      <td id="T_5fe81_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fe81_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_5fe81_row0_col4" class="data row0 col4" >22 <span style="color: grey">(10.6%) </span></td>
    </tr>
    <tr>
      <th id="T_5fe81_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_5fe81_row1_col0" class="data row1 col0" >158 <span style="color: grey">(76.0%) </span></td>
      <td id="T_5fe81_row1_col1" class="data row1 col1" >27 <span style="color: grey">(13.0%) </span></td>
      <td id="T_5fe81_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_5fe81_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_5fe81_row1_col4" class="data row1 col4" >186 <span style="color: grey">(89.4%) </span></td>
    </tr>
    <tr>
      <th id="T_5fe81_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_5fe81_row2_col0" class="data row2 col0" >160 <span style="color: grey">(76.9%) </span></td>
      <td id="T_5fe81_row2_col1" class="data row2 col1" >45 <span style="color: grey">(21.6%) </span></td>
      <td id="T_5fe81_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_5fe81_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_5fe81_row2_col4" class="data row2 col4" >208 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_3040e th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3040e  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3040e_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_3040e_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_3040e_row0_col2, #T_3040e_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_3040e_row0_col3, #T_3040e_row2_col1, #T_3040e_row2_col2, #T_3040e_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_3040e_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_3040e_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.1%, transparent 98.1%);
  font-family: Courier;
}
#T_3040e_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 95.6%, transparent 95.6%);
  font-family: Courier;
}
#T_3040e_row1_col3, #T_3040e_row3_col0, #T_3040e_row3_col1, #T_3040e_row3_col2, #T_3040e_row3_col3, #T_3040e_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_3040e_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.1%, transparent 97.1%);
  font-family: Courier;
}
#T_3040e_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_3040e_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_3040e">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_3040e_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_3040e_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_3040e_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_3040e_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_3040e_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_3040e_level0_row0" class="row_heading level0 row0" >Ja</th>
      <td id="T_3040e_row0_col0" class="data row0 col0" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_3040e_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_3040e_row0_col2" class="data row0 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_3040e_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3040e_row0_col4" class="data row0 col4" >5 <span style="color: grey">(2.4%) </span></td>
    </tr>
    <tr>
      <th id="T_3040e_level0_row1" class="row_heading level0 row1" >Nein</th>
      <td id="T_3040e_row1_col0" class="data row1 col0" >158 <span style="color: grey">(75.6%) </span></td>
      <td id="T_3040e_row1_col1" class="data row1 col1" >43 <span style="color: grey">(20.6%) </span></td>
      <td id="T_3040e_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_3040e_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_3040e_row1_col4" class="data row1 col4" >203 <span style="color: grey">(97.1%) </span></td>
    </tr>
    <tr>
      <th id="T_3040e_level0_row2" class="row_heading level0 row2" >U</th>
      <td id="T_3040e_row2_col0" class="data row2 col0" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_3040e_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_3040e_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_3040e_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3040e_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_3040e_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_3040e_row3_col0" class="data row3 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_3040e_row3_col1" class="data row3 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_3040e_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_3040e_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_3040e_row3_col4" class="data row3 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_347bb th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_347bb  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_347bb_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.7%, transparent 8.7%);
  font-family: Courier;
}
#T_347bb_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.3%, transparent 13.3%);
  font-family: Courier;
}
#T_347bb_row0_col2, #T_347bb_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_347bb_row0_col3, #T_347bb_row1_col2, #T_347bb_row2_col0, #T_347bb_row2_col1, #T_347bb_row2_col2, #T_347bb_row2_col3, #T_347bb_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_347bb_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_347bb_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.3%, transparent 91.3%);
  font-family: Courier;
}
#T_347bb_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.7%, transparent 86.7%);
  font-family: Courier;
}
#T_347bb_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.0%, transparent 90.0%);
  font-family: Courier;
}
</style>
<table id="T_347bb">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_347bb_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_347bb_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_347bb_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_347bb_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_347bb_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_347bb_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_347bb_row0_col0" class="data row0 col0" >14 <span style="color: grey">(6.7%) </span></td>
      <td id="T_347bb_row0_col1" class="data row0 col1" >6 <span style="color: grey">(2.9%) </span></td>
      <td id="T_347bb_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_347bb_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_347bb_row0_col4" class="data row0 col4" >21 <span style="color: grey">(10.0%) </span></td>
    </tr>
    <tr>
      <th id="T_347bb_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_347bb_row1_col0" class="data row1 col0" >147 <span style="color: grey">(70.3%) </span></td>
      <td id="T_347bb_row1_col1" class="data row1 col1" >39 <span style="color: grey">(18.7%) </span></td>
      <td id="T_347bb_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_347bb_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_347bb_row1_col4" class="data row1 col4" >188 <span style="color: grey">(90.0%) </span></td>
    </tr>
    <tr>
      <th id="T_347bb_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_347bb_row2_col0" class="data row2 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_347bb_row2_col1" class="data row2 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_347bb_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_347bb_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_347bb_row2_col4" class="data row2 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_231ad th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_231ad  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_231ad_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.9%, transparent 44.9%);
  font-family: Courier;
}
#T_231ad_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.6%, transparent 43.6%);
  font-family: Courier;
}
#T_231ad_row0_col2, #T_231ad_row2_col0, #T_231ad_row2_col2 {
  width: 10em;
  font-family: Courier;
}
#T_231ad_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.1%, transparent 44.1%);
  font-family: Courier;
}
#T_231ad_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 55.1%, transparent 55.1%);
  font-family: Courier;
}
#T_231ad_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 53.8%, transparent 53.8%);
  font-family: Courier;
}
#T_231ad_row1_col2, #T_231ad_row3_col0, #T_231ad_row3_col1, #T_231ad_row3_col2, #T_231ad_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_231ad_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 55.3%, transparent 55.3%);
  font-family: Courier;
}
#T_231ad_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_231ad_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_231ad">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_231ad_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_231ad_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_231ad_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_231ad_level0_col3" class="col_heading level0 col3" >Total</th>
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
      <th id="T_231ad_level0_row0" class="row_heading level0 row0" >Break</th>
      <td id="T_231ad_row0_col0" class="data row0 col0" >66 <span style="color: grey">(35.1%) </span></td>
      <td id="T_231ad_row0_col1" class="data row0 col1" >17 <span style="color: grey">(9.0%) </span></td>
      <td id="T_231ad_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_231ad_row0_col3" class="data row0 col3" >83 <span style="color: grey">(44.1%) </span></td>
    </tr>
    <tr>
      <th id="T_231ad_level0_row1" class="row_heading level0 row1" >Cessation</th>
      <td id="T_231ad_row1_col0" class="data row1 col0" >81 <span style="color: grey">(43.1%) </span></td>
      <td id="T_231ad_row1_col1" class="data row1 col1" >21 <span style="color: grey">(11.2%) </span></td>
      <td id="T_231ad_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_231ad_row1_col3" class="data row1 col3" >104 <span style="color: grey">(55.3%) </span></td>
    </tr>
    <tr>
      <th id="T_231ad_level0_row2" class="row_heading level0 row2" >Einheit war sowieso vorbei</th>
      <td id="T_231ad_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_231ad_row2_col1" class="data row2 col1" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_231ad_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_231ad_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_231ad_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_231ad_row3_col0" class="data row3 col0" >147 <span style="color: grey">(78.2%) </span></td>
      <td id="T_231ad_row3_col1" class="data row3 col1" >39 <span style="color: grey">(20.7%) </span></td>
      <td id="T_231ad_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_231ad_row3_col3" class="data row3 col3" >188 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_a74f4 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a74f4  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_a74f4_row0_col0, #T_a74f4_row0_col1, #T_a74f4_row0_col2, #T_a74f4_row0_col3, #T_a74f4_row0_col4, #T_a74f4_row1_col0, #T_a74f4_row1_col1, #T_a74f4_row1_col2, #T_a74f4_row1_col3, #T_a74f4_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_a74f4">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_a74f4_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_a74f4_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_a74f4_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_a74f4_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_a74f4_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_a74f4_level0_row0" class="row_heading level0 row0" >-</th>
      <td id="T_a74f4_row0_col0" class="data row0 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_a74f4_row0_col1" class="data row0 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_a74f4_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_a74f4_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_a74f4_row0_col4" class="data row0 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
    <tr>
      <th id="T_a74f4_level0_row1" class="row_heading level0 row1" >Total</th>
      <td id="T_a74f4_row1_col0" class="data row1 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_a74f4_row1_col1" class="data row1 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_a74f4_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_a74f4_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_a74f4_row1_col4" class="data row1 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_fc345 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_fc345  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_fc345_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.1%, transparent 7.1%);
  font-family: Courier;
}
#T_fc345_row0_col1, #T_fc345_row3_col1, #T_fc345_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_fc345_row0_col2, #T_fc345_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_fc345_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.7%, transparent 5.7%);
  font-family: Courier;
}
#T_fc345_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_fc345_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.1%, transparent 47.1%);
  font-family: Courier;
}
#T_fc345_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.5%, transparent 37.5%);
  font-family: Courier;
}
#T_fc345_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 46.2%, transparent 46.2%);
  font-family: Courier;
}
#T_fc345_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.3%, transparent 34.3%);
  font-family: Courier;
}
#T_fc345_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 32.1%, transparent 32.1%);
  font-family: Courier;
}
#T_fc345_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.4%, transparent 1.4%);
  font-family: Courier;
}
#T_fc345_row4_col1, #T_fc345_row5_col1, #T_fc345_row6_col0 {
  width: 10em;
  font-family: Courier;
}
#T_fc345_row4_col2, #T_fc345_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_fc345_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_fc345_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_fc345_row7_col0, #T_fc345_row7_col1, #T_fc345_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_fc345">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_fc345_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_fc345_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_fc345_level0_col2" class="col_heading level0 col2" >Total</th>
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
      <th id="T_fc345_level0_row0" class="row_heading level0 row0" >Communication strategy</th>
      <td id="T_fc345_row0_col0" class="data row0 col0" >5 <span style="color: grey">(6.4%) </span></td>
      <td id="T_fc345_row0_col1" class="data row0 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_fc345_row0_col2" class="data row0 col2" >6 <span style="color: grey">(7.7%) </span></td>
    </tr>
    <tr>
      <th id="T_fc345_level0_row1" class="row_heading level0 row1" >Equipment</th>
      <td id="T_fc345_row1_col0" class="data row1 col0" >4 <span style="color: grey">(5.1%) </span></td>
      <td id="T_fc345_row1_col1" class="data row1 col1" >2 <span style="color: grey">(2.6%) </span></td>
      <td id="T_fc345_row1_col2" class="data row1 col2" >6 <span style="color: grey">(7.7%) </span></td>
    </tr>
    <tr>
      <th id="T_fc345_level0_row2" class="row_heading level0 row2" >Exercise selection</th>
      <td id="T_fc345_row2_col0" class="data row2 col0" >33 <span style="color: grey">(42.3%) </span></td>
      <td id="T_fc345_row2_col1" class="data row2 col1" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_fc345_row2_col2" class="data row2 col2" >36 <span style="color: grey">(46.2%) </span></td>
    </tr>
    <tr>
      <th id="T_fc345_level0_row3" class="row_heading level0 row3" >Intensity</th>
      <td id="T_fc345_row3_col0" class="data row3 col0" >24 <span style="color: grey">(30.8%) </span></td>
      <td id="T_fc345_row3_col1" class="data row3 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_fc345_row3_col2" class="data row3 col2" >25 <span style="color: grey">(32.1%) </span></td>
    </tr>
    <tr>
      <th id="T_fc345_level0_row4" class="row_heading level0 row4" >Motivationsstrategie</th>
      <td id="T_fc345_row4_col0" class="data row4 col0" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_fc345_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_fc345_row4_col2" class="data row4 col2" >1 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_fc345_level0_row5" class="row_heading level0 row5" >Setting</th>
      <td id="T_fc345_row5_col0" class="data row5 col0" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_fc345_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_fc345_row5_col2" class="data row5 col2" >3 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_fc345_level0_row6" class="row_heading level0 row6" >Weiteres</th>
      <td id="T_fc345_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_fc345_row6_col1" class="data row6 col1" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_fc345_row6_col2" class="data row6 col2" >1 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_fc345_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_fc345_row7_col0" class="data row7 col0" >70 <span style="color: grey">(89.7%) </span></td>
      <td id="T_fc345_row7_col1" class="data row7 col1" >8 <span style="color: grey">(10.3%) </span></td>
      <td id="T_fc345_row7_col2" class="data row7 col2" >78 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_3b289 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3b289  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_3b289_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.3%, transparent 13.3%);
  font-family: Courier;
}
#T_3b289_row0_col1, #T_3b289_row2_col0 {
  width: 10em;
  font-family: Courier;
}
#T_3b289_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.8%, transparent 11.8%);
  font-family: Courier;
}
#T_3b289_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.8%, transparent 17.8%);
  font-family: Courier;
}
#T_3b289_row1_col1, #T_3b289_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_3b289_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.6%, transparent 17.6%);
  font-family: Courier;
}
#T_3b289_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_3b289_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.9%, transparent 68.9%);
  font-family: Courier;
}
#T_3b289_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_3b289_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.6%, transparent 68.6%);
  font-family: Courier;
}
#T_3b289_row4_col0, #T_3b289_row4_col1, #T_3b289_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_3b289">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_3b289_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_3b289_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_3b289_level0_col2" class="col_heading level0 col2" >Total</th>
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
      <th id="T_3b289_level0_row0" class="row_heading level0 row0" >Ab jetzt für alle Bewegungseinheiten mit allen Patient*innen</th>
      <td id="T_3b289_row0_col0" class="data row0 col0" >6 <span style="color: grey">(11.8%) </span></td>
      <td id="T_3b289_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_3b289_row0_col2" class="data row0 col2" >6 <span style="color: grey">(11.8%) </span></td>
    </tr>
    <tr>
      <th id="T_3b289_level0_row1" class="row_heading level0 row1" >Für die gesamte Therapiephase</th>
      <td id="T_3b289_row1_col0" class="data row1 col0" >8 <span style="color: grey">(15.7%) </span></td>
      <td id="T_3b289_row1_col1" class="data row1 col1" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_3b289_row1_col2" class="data row1 col2" >9 <span style="color: grey">(17.6%) </span></td>
    </tr>
    <tr>
      <th id="T_3b289_level0_row2" class="row_heading level0 row2" >Für die nächsten Einheiten (da das AE rückwirkend auftrat</th>
      <td id="T_3b289_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_3b289_row2_col1" class="data row2 col1" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_3b289_row2_col2" class="data row2 col2" >1 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_3b289_level0_row3" class="row_heading level0 row3" >Nur für diese Einheit</th>
      <td id="T_3b289_row3_col0" class="data row3 col0" >31 <span style="color: grey">(60.8%) </span></td>
      <td id="T_3b289_row3_col1" class="data row3 col1" >4 <span style="color: grey">(7.8%) </span></td>
      <td id="T_3b289_row3_col2" class="data row3 col2" >35 <span style="color: grey">(68.6%) </span></td>
    </tr>
    <tr>
      <th id="T_3b289_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_3b289_row4_col0" class="data row4 col0" >45 <span style="color: grey">(88.2%) </span></td>
      <td id="T_3b289_row4_col1" class="data row4 col1" >6 <span style="color: grey">(11.8%) </span></td>
      <td id="T_3b289_row4_col2" class="data row4 col2" >51 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_98df0 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_98df0  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_98df0_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 89.4%, transparent 89.4%);
  font-family: Courier;
}
#T_98df0_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 60.0%, transparent 60.0%);
  font-family: Courier;
}
#T_98df0_row0_col2, #T_98df0_row0_col3, #T_98df0_row2_col2, #T_98df0_row2_col3, #T_98df0_row3_col1, #T_98df0_row3_col2, #T_98df0_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_98df0_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 81.8%, transparent 81.8%);
  font-family: Courier;
}
#T_98df0_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_98df0_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.6%, transparent 35.6%);
  font-family: Courier;
}
#T_98df0_row1_col2, #T_98df0_row1_col3, #T_98df0_row4_col0, #T_98df0_row4_col1, #T_98df0_row4_col2, #T_98df0_row4_col3, #T_98df0_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_98df0_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.9%, transparent 13.9%);
  font-family: Courier;
}
#T_98df0_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.7%, transparent 3.7%);
  font-family: Courier;
}
#T_98df0_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_98df0_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_98df0_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_98df0_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_98df0">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_98df0_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_98df0_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_98df0_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_98df0_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_98df0_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_98df0_level0_row0" class="row_heading level0 row0" >Acute therapy</th>
      <td id="T_98df0_row0_col0" class="data row0 col0" >144 <span style="color: grey">(68.9%) </span></td>
      <td id="T_98df0_row0_col1" class="data row0 col1" >27 <span style="color: grey">(12.9%) </span></td>
      <td id="T_98df0_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_98df0_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_98df0_row0_col4" class="data row0 col4" >171 <span style="color: grey">(81.8%) </span></td>
    </tr>
    <tr>
      <th id="T_98df0_level0_row1" class="row_heading level0 row1" >Aftercare</th>
      <td id="T_98df0_row1_col0" class="data row1 col0" >10 <span style="color: grey">(4.8%) </span></td>
      <td id="T_98df0_row1_col1" class="data row1 col1" >16 <span style="color: grey">(7.7%) </span></td>
      <td id="T_98df0_row1_col2" class="data row1 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_98df0_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_98df0_row1_col4" class="data row1 col4" >29 <span style="color: grey">(13.9%) </span></td>
    </tr>
    <tr>
      <th id="T_98df0_level0_row2" class="row_heading level0 row2" >Long-term therapy</th>
      <td id="T_98df0_row2_col0" class="data row2 col0" >6 <span style="color: grey">(2.9%) </span></td>
      <td id="T_98df0_row2_col1" class="data row2 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_98df0_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_98df0_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_98df0_row2_col4" class="data row2 col4" >8 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_98df0_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_98df0_row3_col0" class="data row3 col0" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_98df0_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_98df0_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_98df0_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_98df0_row3_col4" class="data row3 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_98df0_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_98df0_row4_col0" class="data row4 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_98df0_row4_col1" class="data row4 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_98df0_row4_col2" class="data row4 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_98df0_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_98df0_row4_col4" class="data row4 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_c1bb8 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c1bb8  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_c1bb8_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_c1bb8_row0_col1, #T_c1bb8_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_c1bb8_row0_col2, #T_c1bb8_row0_col3, #T_c1bb8_row1_col3, #T_c1bb8_row2_col0, #T_c1bb8_row2_col2, #T_c1bb8_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_c1bb8_row0_col4, #T_c1bb8_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_c1bb8_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_c1bb8_row1_col1, #T_c1bb8_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.3%, transparent 13.3%);
  font-family: Courier;
}
#T_c1bb8_row1_col2, #T_c1bb8_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_c1bb8_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_c1bb8_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.9%, transparent 68.9%);
  font-family: Courier;
}
#T_c1bb8_row3_col3, #T_c1bb8_row4_col0, #T_c1bb8_row4_col1, #T_c1bb8_row4_col2, #T_c1bb8_row4_col3, #T_c1bb8_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_c1bb8_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 89.8%, transparent 89.8%);
  font-family: Courier;
}
</style>
<table id="T_c1bb8">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_c1bb8_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_c1bb8_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_c1bb8_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_c1bb8_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_c1bb8_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_c1bb8_level0_row0" class="row_heading level0 row0" >Group 2-5</th>
      <td id="T_c1bb8_row0_col0" class="data row0 col0" >4 <span style="color: grey">(2.0%) </span></td>
      <td id="T_c1bb8_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_c1bb8_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c1bb8_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c1bb8_row0_col4" class="data row0 col4" >6 <span style="color: grey">(2.9%) </span></td>
    </tr>
    <tr>
      <th id="T_c1bb8_level0_row1" class="row_heading level0 row1" >Group 5 to 10</th>
      <td id="T_c1bb8_row1_col0" class="data row1 col0" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_c1bb8_row1_col1" class="data row1 col1" >6 <span style="color: grey">(2.9%) </span></td>
      <td id="T_c1bb8_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c1bb8_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c1bb8_row1_col4" class="data row1 col4" >9 <span style="color: grey">(4.4%) </span></td>
    </tr>
    <tr>
      <th id="T_c1bb8_level0_row2" class="row_heading level0 row2" >Group over 10</th>
      <td id="T_c1bb8_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c1bb8_row2_col1" class="data row2 col1" >6 <span style="color: grey">(2.9%) </span></td>
      <td id="T_c1bb8_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c1bb8_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c1bb8_row2_col4" class="data row2 col4" >6 <span style="color: grey">(2.9%) </span></td>
    </tr>
    <tr>
      <th id="T_c1bb8_level0_row3" class="row_heading level0 row3" >Individual</th>
      <td id="T_c1bb8_row3_col0" class="data row3 col0" >151 <span style="color: grey">(73.7%) </span></td>
      <td id="T_c1bb8_row3_col1" class="data row3 col1" >31 <span style="color: grey">(15.1%) </span></td>
      <td id="T_c1bb8_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c1bb8_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c1bb8_row3_col4" class="data row3 col4" >184 <span style="color: grey">(89.8%) </span></td>
    </tr>
    <tr>
      <th id="T_c1bb8_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_c1bb8_row4_col0" class="data row4 col0" >157 <span style="color: grey">(76.6%) </span></td>
      <td id="T_c1bb8_row4_col1" class="data row4 col1" >45 <span style="color: grey">(22.0%) </span></td>
      <td id="T_c1bb8_row4_col2" class="data row4 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_c1bb8_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_c1bb8_row4_col4" class="data row4 col4" >205 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_fe0e8 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_fe0e8  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_fe0e8_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.9%, transparent 10.9%);
  font-family: Courier;
}
#T_fe0e8_row0_col1, #T_fe0e8_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_fe0e8_row0_col2, #T_fe0e8_row0_col3, #T_fe0e8_row1_col2, #T_fe0e8_row1_col3, #T_fe0e8_row2_col2, #T_fe0e8_row2_col3, #T_fe0e8_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_fe0e8_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.2%, transparent 13.2%);
  font-family: Courier;
}
#T_fe0e8_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.1%, transparent 39.1%);
  font-family: Courier;
}
#T_fe0e8_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.6%, transparent 30.6%);
  font-family: Courier;
}
#T_fe0e8_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.5%, transparent 36.5%);
  font-family: Courier;
}
#T_fe0e8_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.2%, transparent 31.2%);
  font-family: Courier;
}
#T_fe0e8_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.7%, transparent 28.7%);
  font-family: Courier;
}
#T_fe0e8_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.6%, transparent 15.6%);
  font-family: Courier;
}
#T_fe0e8_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_fe0e8_row3_col2, #T_fe0e8_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_fe0e8_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.2%, transparent 16.2%);
  font-family: Courier;
}
#T_fe0e8_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_fe0e8_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_fe0e8_row4_col3, #T_fe0e8_row5_col0, #T_fe0e8_row5_col1, #T_fe0e8_row5_col2, #T_fe0e8_row5_col3, #T_fe0e8_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_fe0e8_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.4%, transparent 5.4%);
  font-family: Courier;
}
</style>
<table id="T_fe0e8">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_fe0e8_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_fe0e8_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_fe0e8_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_fe0e8_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_fe0e8_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_fe0e8_level0_row0" class="row_heading level0 row0" >02 to 05 years</th>
      <td id="T_fe0e8_row0_col0" class="data row0 col0" >14 <span style="color: grey">(8.4%) </span></td>
      <td id="T_fe0e8_row0_col1" class="data row0 col1" >8 <span style="color: grey">(4.8%) </span></td>
      <td id="T_fe0e8_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_fe0e8_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_fe0e8_row0_col4" class="data row0 col4" >22 <span style="color: grey">(13.2%) </span></td>
    </tr>
    <tr>
      <th id="T_fe0e8_level0_row1" class="row_heading level0 row1" >06 to 09 years</th>
      <td id="T_fe0e8_row1_col0" class="data row1 col0" >50 <span style="color: grey">(29.9%) </span></td>
      <td id="T_fe0e8_row1_col1" class="data row1 col1" >11 <span style="color: grey">(6.6%) </span></td>
      <td id="T_fe0e8_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_fe0e8_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_fe0e8_row1_col4" class="data row1 col4" >61 <span style="color: grey">(36.5%) </span></td>
    </tr>
    <tr>
      <th id="T_fe0e8_level0_row2" class="row_heading level0 row2" >10 to 14 years</th>
      <td id="T_fe0e8_row2_col0" class="data row2 col0" >40 <span style="color: grey">(24.0%) </span></td>
      <td id="T_fe0e8_row2_col1" class="data row2 col1" >8 <span style="color: grey">(4.8%) </span></td>
      <td id="T_fe0e8_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_fe0e8_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_fe0e8_row2_col4" class="data row2 col4" >48 <span style="color: grey">(28.7%) </span></td>
    </tr>
    <tr>
      <th id="T_fe0e8_level0_row3" class="row_heading level0 row3" >15 to 18 years</th>
      <td id="T_fe0e8_row3_col0" class="data row3 col0" >20 <span style="color: grey">(12.0%) </span></td>
      <td id="T_fe0e8_row3_col1" class="data row3 col1" >6 <span style="color: grey">(3.6%) </span></td>
      <td id="T_fe0e8_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_fe0e8_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_fe0e8_row3_col4" class="data row3 col4" >27 <span style="color: grey">(16.2%) </span></td>
    </tr>
    <tr>
      <th id="T_fe0e8_level0_row4" class="row_heading level0 row4" >18+ years</th>
      <td id="T_fe0e8_row4_col0" class="data row4 col0" >4 <span style="color: grey">(2.4%) </span></td>
      <td id="T_fe0e8_row4_col1" class="data row4 col1" >3 <span style="color: grey">(1.8%) </span></td>
      <td id="T_fe0e8_row4_col2" class="data row4 col2" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_fe0e8_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_fe0e8_row4_col4" class="data row4 col4" >9 <span style="color: grey">(5.4%) </span></td>
    </tr>
    <tr>
      <th id="T_fe0e8_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_fe0e8_row5_col0" class="data row5 col0" >128 <span style="color: grey">(76.6%) </span></td>
      <td id="T_fe0e8_row5_col1" class="data row5 col1" >36 <span style="color: grey">(21.6%) </span></td>
      <td id="T_fe0e8_row5_col2" class="data row5 col2" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_fe0e8_row5_col3" class="data row5 col3" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_fe0e8_row5_col4" class="data row5 col4" >167 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_d9256 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d9256  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_d9256_row0_col0, #T_d9256_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.2%, transparent 96.2%);
  font-family: Courier;
}
#T_d9256_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 95.6%, transparent 95.6%);
  font-family: Courier;
}
#T_d9256_row0_col2, #T_d9256_row0_col3, #T_d9256_row2_col0, #T_d9256_row2_col1, #T_d9256_row2_col2, #T_d9256_row2_col3, #T_d9256_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_d9256_row1_col0, #T_d9256_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_d9256_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_d9256_row1_col2, #T_d9256_row1_col3 {
  width: 10em;
  font-family: Courier;
}
</style>
<table id="T_d9256">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_d9256_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_d9256_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_d9256_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_d9256_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_d9256_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_d9256_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_d9256_row0_col0" class="data row0 col0" >154 <span style="color: grey">(74.0%) </span></td>
      <td id="T_d9256_row0_col1" class="data row0 col1" >43 <span style="color: grey">(20.7%) </span></td>
      <td id="T_d9256_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_d9256_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_d9256_row0_col4" class="data row0 col4" >200 <span style="color: grey">(96.2%) </span></td>
    </tr>
    <tr>
      <th id="T_d9256_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_d9256_row1_col0" class="data row1 col0" >6 <span style="color: grey">(2.9%) </span></td>
      <td id="T_d9256_row1_col1" class="data row1 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_d9256_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_d9256_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_d9256_row1_col4" class="data row1 col4" >8 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_d9256_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_d9256_row2_col0" class="data row2 col0" >160 <span style="color: grey">(76.9%) </span></td>
      <td id="T_d9256_row2_col1" class="data row2 col1" >45 <span style="color: grey">(21.6%) </span></td>
      <td id="T_d9256_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_d9256_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_d9256_row2_col4" class="data row2 col4" >208 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_e296e th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e296e  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_e296e_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.9%, transparent 96.9%);
  font-family: Courier;
}
#T_e296e_row0_col1, #T_e296e_row0_col2, #T_e296e_row0_col3, #T_e296e_row2_col0, #T_e296e_row2_col1, #T_e296e_row2_col2, #T_e296e_row2_col3, #T_e296e_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e296e_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 97.6%, transparent 97.6%);
  font-family: Courier;
}
#T_e296e_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_e296e_row1_col1, #T_e296e_row1_col2, #T_e296e_row1_col3 {
  width: 10em;
  font-family: Courier;
}
#T_e296e_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
</style>
<table id="T_e296e">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_e296e_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_e296e_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_e296e_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_e296e_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_e296e_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_e296e_level0_row0" class="row_heading level0 row0" >No</th>
      <td id="T_e296e_row0_col0" class="data row0 col0" >156 <span style="color: grey">(74.6%) </span></td>
      <td id="T_e296e_row0_col1" class="data row0 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_e296e_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_e296e_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e296e_row0_col4" class="data row0 col4" >204 <span style="color: grey">(97.6%) </span></td>
    </tr>
    <tr>
      <th id="T_e296e_level0_row1" class="row_heading level0 row1" >Yes</th>
      <td id="T_e296e_row1_col0" class="data row1 col0" >5 <span style="color: grey">(2.4%) </span></td>
      <td id="T_e296e_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e296e_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e296e_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e296e_row1_col4" class="data row1 col4" >5 <span style="color: grey">(2.4%) </span></td>
    </tr>
    <tr>
      <th id="T_e296e_level0_row2" class="row_heading level0 row2" >Total</th>
      <td id="T_e296e_row2_col0" class="data row2 col0" >161 <span style="color: grey">(77.0%) </span></td>
      <td id="T_e296e_row2_col1" class="data row2 col1" >45 <span style="color: grey">(21.5%) </span></td>
      <td id="T_e296e_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_e296e_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_e296e_row2_col4" class="data row2 col4" >209 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_ea658 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ea658  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_ea658_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_ea658_row0_col1, #T_ea658_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.7%, transparent 4.7%);
  font-family: Courier;
}
#T_ea658_row0_col2, #T_ea658_row0_col3, #T_ea658_row1_col3, #T_ea658_row2_col2, #T_ea658_row2_col3, #T_ea658_row4_col2, #T_ea658_row4_col3, #T_ea658_row5_col1, #T_ea658_row5_col2, #T_ea658_row5_col3 {
  width: 10em;
  font-family: Courier;
}
#T_ea658_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_ea658_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.9%, transparent 40.9%);
  font-family: Courier;
}
#T_ea658_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 53.5%, transparent 53.5%);
  font-family: Courier;
}
#T_ea658_row1_col2, #T_ea658_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_ea658_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.6%, transparent 43.6%);
  font-family: Courier;
}
#T_ea658_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.8%, transparent 24.8%);
  font-family: Courier;
}
#T_ea658_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.6%, transparent 11.6%);
  font-family: Courier;
}
#T_ea658_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.5%, transparent 21.5%);
  font-family: Courier;
}
#T_ea658_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
#T_ea658_row3_col3, #T_ea658_row6_col0, #T_ea658_row6_col1, #T_ea658_row6_col2, #T_ea658_row6_col3, #T_ea658_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_ea658_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_ea658_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.5%, transparent 25.5%);
  font-family: Courier;
}
#T_ea658_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.3%, transparent 16.3%);
  font-family: Courier;
}
#T_ea658_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.1%, transparent 23.1%);
  font-family: Courier;
}
#T_ea658_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_ea658_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_ea658">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_ea658_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_ea658_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_ea658_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_ea658_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_ea658_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_ea658_level0_row0" class="row_heading level0 row0" >At home (via telemedicine)</th>
      <td id="T_ea658_row0_col0" class="data row0 col0" >5 <span style="color: grey">(2.6%) </span></td>
      <td id="T_ea658_row0_col1" class="data row0 col1" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_ea658_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row0_col4" class="data row0 col4" >7 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_ea658_level0_row1" class="row_heading level0 row1" >Gym</th>
      <td id="T_ea658_row1_col0" class="data row1 col0" >61 <span style="color: grey">(31.3%) </span></td>
      <td id="T_ea658_row1_col1" class="data row1 col1" >23 <span style="color: grey">(11.8%) </span></td>
      <td id="T_ea658_row1_col2" class="data row1 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_ea658_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row1_col4" class="data row1 col4" >85 <span style="color: grey">(43.6%) </span></td>
    </tr>
    <tr>
      <th id="T_ea658_level0_row2" class="row_heading level0 row2" >Hospital corridor</th>
      <td id="T_ea658_row2_col0" class="data row2 col0" >37 <span style="color: grey">(19.0%) </span></td>
      <td id="T_ea658_row2_col1" class="data row2 col1" >5 <span style="color: grey">(2.6%) </span></td>
      <td id="T_ea658_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row2_col4" class="data row2 col4" >42 <span style="color: grey">(21.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ea658_level0_row3" class="row_heading level0 row3" >Outside</th>
      <td id="T_ea658_row3_col0" class="data row3 col0" >7 <span style="color: grey">(3.6%) </span></td>
      <td id="T_ea658_row3_col1" class="data row3 col1" >6 <span style="color: grey">(3.1%) </span></td>
      <td id="T_ea658_row3_col2" class="data row3 col2" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_ea658_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_ea658_row3_col4" class="data row3 col4" >15 <span style="color: grey">(7.7%) </span></td>
    </tr>
    <tr>
      <th id="T_ea658_level0_row4" class="row_heading level0 row4" >Patients room</th>
      <td id="T_ea658_row4_col0" class="data row4 col0" >38 <span style="color: grey">(19.5%) </span></td>
      <td id="T_ea658_row4_col1" class="data row4 col1" >7 <span style="color: grey">(3.6%) </span></td>
      <td id="T_ea658_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row4_col4" class="data row4 col4" >45 <span style="color: grey">(23.1%) </span></td>
    </tr>
    <tr>
      <th id="T_ea658_level0_row5" class="row_heading level0 row5" >Weiteres</th>
      <td id="T_ea658_row5_col0" class="data row5 col0" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_ea658_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ea658_row5_col4" class="data row5 col4" >1 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ea658_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_ea658_row6_col0" class="data row6 col0" >149 <span style="color: grey">(76.4%) </span></td>
      <td id="T_ea658_row6_col1" class="data row6 col1" >43 <span style="color: grey">(22.1%) </span></td>
      <td id="T_ea658_row6_col2" class="data row6 col2" >2 <span style="color: grey">(1.0%) </span></td>
      <td id="T_ea658_row6_col3" class="data row6 col3" >1 <span style="color: grey">(0.5%) </span></td>
      <td id="T_ea658_row6_col4" class="data row6 col4" >195 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_2f126 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2f126  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_2f126_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.7%, transparent 36.7%);
  font-family: Courier;
}
#T_2f126_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.6%, transparent 35.6%);
  font-family: Courier;
}
#T_2f126_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_2f126_row0_col3, #T_2f126_row7_col0, #T_2f126_row7_col1, #T_2f126_row7_col2, #T_2f126_row7_col3, #T_2f126_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_2f126_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.0%, transparent 37.0%);
  font-family: Courier;
}
#T_2f126_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.4%, transparent 21.4%);
  font-family: Courier;
}
#T_2f126_row1_col1, #T_2f126_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.3%, transparent 20.3%);
  font-family: Courier;
}
#T_2f126_row1_col2, #T_2f126_row1_col3, #T_2f126_row2_col2, #T_2f126_row2_col3, #T_2f126_row3_col2, #T_2f126_row3_col3, #T_2f126_row4_col1, #T_2f126_row4_col2, #T_2f126_row4_col3, #T_2f126_row5_col2, #T_2f126_row5_col3, #T_2f126_row6_col3 {
  width: 10em;
  font-family: Courier;
}
#T_2f126_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.9%, transparent 20.9%);
  font-family: Courier;
}
#T_2f126_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.1%, transparent 7.1%);
  font-family: Courier;
}
#T_2f126_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_2f126_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_2f126_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.9%, transparent 12.9%);
  font-family: Courier;
}
#T_2f126_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.9%, transparent 11.9%);
  font-family: Courier;
}
#T_2f126_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_2f126_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_2f126_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_2f126_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_2f126_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.5%, transparent 8.5%);
  font-family: Courier;
}
#T_2f126_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_2f126_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.1%, transparent 17.1%);
  font-family: Courier;
}
#T_2f126_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_2f126_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.9%, transparent 17.9%);
  font-family: Courier;
}
</style>
<table id="T_2f126">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_2f126_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_2f126_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_2f126_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_2f126_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_2f126_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_2f126_level0_row0" class="row_heading level0 row0" >Coordination</th>
      <td id="T_2f126_row0_col0" class="data row0 col0" >77 <span style="color: grey">(28.2%) </span></td>
      <td id="T_2f126_row0_col1" class="data row0 col1" >21 <span style="color: grey">(7.7%) </span></td>
      <td id="T_2f126_row0_col2" class="data row0 col2" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_2f126_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2f126_row0_col4" class="data row0 col4" >101 <span style="color: grey">(37.0%) </span></td>
    </tr>
    <tr>
      <th id="T_2f126_level0_row1" class="row_heading level0 row1" >Endurance</th>
      <td id="T_2f126_row1_col0" class="data row1 col0" >45 <span style="color: grey">(16.5%) </span></td>
      <td id="T_2f126_row1_col1" class="data row1 col1" >12 <span style="color: grey">(4.4%) </span></td>
      <td id="T_2f126_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row1_col4" class="data row1 col4" >57 <span style="color: grey">(20.9%) </span></td>
    </tr>
    <tr>
      <th id="T_2f126_level0_row2" class="row_heading level0 row2" >Flexibility</th>
      <td id="T_2f126_row2_col0" class="data row2 col0" >15 <span style="color: grey">(5.5%) </span></td>
      <td id="T_2f126_row2_col1" class="data row2 col1" >2 <span style="color: grey">(0.7%) </span></td>
      <td id="T_2f126_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row2_col4" class="data row2 col4" >17 <span style="color: grey">(6.2%) </span></td>
    </tr>
    <tr>
      <th id="T_2f126_level0_row3" class="row_heading level0 row3" >Full body</th>
      <td id="T_2f126_row3_col0" class="data row3 col0" >27 <span style="color: grey">(9.9%) </span></td>
      <td id="T_2f126_row3_col1" class="data row3 col1" >7 <span style="color: grey">(2.6%) </span></td>
      <td id="T_2f126_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row3_col4" class="data row3 col4" >34 <span style="color: grey">(12.5%) </span></td>
    </tr>
    <tr>
      <th id="T_2f126_level0_row4" class="row_heading level0 row4" >Relaxation</th>
      <td id="T_2f126_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.5%) </span></td>
      <td id="T_2f126_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row4_col4" class="data row4 col4" >4 <span style="color: grey">(1.5%) </span></td>
    </tr>
    <tr>
      <th id="T_2f126_level0_row5" class="row_heading level0 row5" >Speed</th>
      <td id="T_2f126_row5_col0" class="data row5 col0" >6 <span style="color: grey">(2.2%) </span></td>
      <td id="T_2f126_row5_col1" class="data row5 col1" >5 <span style="color: grey">(1.8%) </span></td>
      <td id="T_2f126_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row5_col4" class="data row5 col4" >11 <span style="color: grey">(4.0%) </span></td>
    </tr>
    <tr>
      <th id="T_2f126_level0_row6" class="row_heading level0 row6" >Strength</th>
      <td id="T_2f126_row6_col0" class="data row6 col0" >36 <span style="color: grey">(13.2%) </span></td>
      <td id="T_2f126_row6_col1" class="data row6 col1" >12 <span style="color: grey">(4.4%) </span></td>
      <td id="T_2f126_row6_col2" class="data row6 col2" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2f126_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2f126_row6_col4" class="data row6 col4" >49 <span style="color: grey">(17.9%) </span></td>
    </tr>
    <tr>
      <th id="T_2f126_level0_row7" class="row_heading level0 row7" >Total</th>
      <td id="T_2f126_row7_col0" class="data row7 col0" >210 <span style="color: grey">(76.9%) </span></td>
      <td id="T_2f126_row7_col1" class="data row7 col1" >59 <span style="color: grey">(21.6%) </span></td>
      <td id="T_2f126_row7_col2" class="data row7 col2" >3 <span style="color: grey">(1.1%) </span></td>
      <td id="T_2f126_row7_col3" class="data row7 col3" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_2f126_row7_col4" class="data row7 col4" >273 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_36c37 th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_36c37  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_36c37_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.0%, transparent 44.0%);
  font-family: Courier;
}
#T_36c37_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_36c37_row0_col2, #T_36c37_row1_col3, #T_36c37_row3_col0, #T_36c37_row3_col1, #T_36c37_row3_col2, #T_36c37_row3_col3, #T_36c37_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_36c37_row0_col3, #T_36c37_row1_col2, #T_36c37_row2_col0, #T_36c37_row2_col2, #T_36c37_row2_col3 {
  width: 10em;
  font-family: Courier;
}
#T_36c37_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.0%, transparent 38.0%);
  font-family: Courier;
}
#T_36c37_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 56.0%, transparent 56.0%);
  font-family: Courier;
}
#T_36c37_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.9%, transparent 82.9%);
  font-family: Courier;
}
#T_36c37_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 61.3%, transparent 61.3%);
  font-family: Courier;
}
#T_36c37_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_36c37_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
</style>
<table id="T_36c37">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_36c37_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_36c37_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_36c37_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_36c37_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_36c37_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_36c37_level0_row0" class="row_heading level0 row0" >1. Time point</th>
      <td id="T_36c37_row0_col0" class="data row0 col0" >55 <span style="color: grey">(33.7%) </span></td>
      <td id="T_36c37_row0_col1" class="data row0 col1" >5 <span style="color: grey">(3.1%) </span></td>
      <td id="T_36c37_row0_col2" class="data row0 col2" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_36c37_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_36c37_row0_col4" class="data row0 col4" >62 <span style="color: grey">(38.0%) </span></td>
    </tr>
    <tr>
      <th id="T_36c37_level0_row1" class="row_heading level0 row1" >2. Time point</th>
      <td id="T_36c37_row1_col0" class="data row1 col0" >70 <span style="color: grey">(42.9%) </span></td>
      <td id="T_36c37_row1_col1" class="data row1 col1" >29 <span style="color: grey">(17.8%) </span></td>
      <td id="T_36c37_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_36c37_row1_col3" class="data row1 col3" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_36c37_row1_col4" class="data row1 col4" >100 <span style="color: grey">(61.3%) </span></td>
    </tr>
    <tr>
      <th id="T_36c37_level0_row2" class="row_heading level0 row2" >Nach Abschluß der Therapie</th>
      <td id="T_36c37_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_36c37_row2_col1" class="data row2 col1" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_36c37_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_36c37_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_36c37_row2_col4" class="data row2 col4" >1 <span style="color: grey">(0.6%) </span></td>
    </tr>
    <tr>
      <th id="T_36c37_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_36c37_row3_col0" class="data row3 col0" >125 <span style="color: grey">(76.7%) </span></td>
      <td id="T_36c37_row3_col1" class="data row3 col1" >35 <span style="color: grey">(21.5%) </span></td>
      <td id="T_36c37_row3_col2" class="data row3 col2" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_36c37_row3_col3" class="data row3 col3" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_36c37_row3_col4" class="data row3 col4" >163 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




<style type="text/css">
#T_08bdd th:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_08bdd  td:first-child {
  min-width: 600px !important;
  max-width: 600px !important;
  white-space: nowrap;
  overflow: hidden;
}
#T_08bdd_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.6%, transparent 29.6%);
  font-family: Courier;
}
#T_08bdd_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.2%, transparent 31.2%);
  font-family: Courier;
}
#T_08bdd_row0_col2, #T_08bdd_row1_col2, #T_08bdd_row1_col3, #T_08bdd_row2_col3, #T_08bdd_row3_col1, #T_08bdd_row3_col2, #T_08bdd_row3_col3 {
  width: 10em;
  font-family: Courier;
}
#T_08bdd_row0_col3, #T_08bdd_row2_col2, #T_08bdd_row4_col0, #T_08bdd_row4_col1, #T_08bdd_row4_col2, #T_08bdd_row4_col3, #T_08bdd_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_08bdd_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.0%, transparent 30.0%);
  font-family: Courier;
}
#T_08bdd_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.0%, transparent 16.0%);
  font-family: Courier;
}
#T_08bdd_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.8%, transparent 18.8%);
  font-family: Courier;
}
#T_08bdd_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.2%, transparent 16.2%);
  font-family: Courier;
}
#T_08bdd_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.8%, transparent 52.8%);
  font-family: Courier;
}
#T_08bdd_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_08bdd_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.5%, transparent 52.5%);
  font-family: Courier;
}
#T_08bdd_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_08bdd_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
</style>
<table id="T_08bdd">
  <thead>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th id="T_08bdd_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_08bdd_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_08bdd_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_08bdd_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_08bdd_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_08bdd_level0_row0" class="row_heading level0 row0" >Average</th>
      <td id="T_08bdd_row0_col0" class="data row0 col0" >37 <span style="color: grey">(23.1%) </span></td>
      <td id="T_08bdd_row0_col1" class="data row0 col1" >10 <span style="color: grey">(6.2%) </span></td>
      <td id="T_08bdd_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_08bdd_row0_col3" class="data row0 col3" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_08bdd_row0_col4" class="data row0 col4" >48 <span style="color: grey">(30.0%) </span></td>
    </tr>
    <tr>
      <th id="T_08bdd_level0_row1" class="row_heading level0 row1" >Good</th>
      <td id="T_08bdd_row1_col0" class="data row1 col0" >20 <span style="color: grey">(12.5%) </span></td>
      <td id="T_08bdd_row1_col1" class="data row1 col1" >6 <span style="color: grey">(3.8%) </span></td>
      <td id="T_08bdd_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_08bdd_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_08bdd_row1_col4" class="data row1 col4" >26 <span style="color: grey">(16.2%) </span></td>
    </tr>
    <tr>
      <th id="T_08bdd_level0_row2" class="row_heading level0 row2" >Moderate</th>
      <td id="T_08bdd_row2_col0" class="data row2 col0" >66 <span style="color: grey">(41.2%) </span></td>
      <td id="T_08bdd_row2_col1" class="data row2 col1" >16 <span style="color: grey">(10.0%) </span></td>
      <td id="T_08bdd_row2_col2" class="data row2 col2" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_08bdd_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_08bdd_row2_col4" class="data row2 col4" >84 <span style="color: grey">(52.5%) </span></td>
    </tr>
    <tr>
      <th id="T_08bdd_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_08bdd_row3_col0" class="data row3 col0" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_08bdd_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_08bdd_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_08bdd_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_08bdd_row3_col4" class="data row3 col4" >2 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_08bdd_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_08bdd_row4_col0" class="data row4 col0" >125 <span style="color: grey">(78.1%) </span></td>
      <td id="T_08bdd_row4_col1" class="data row4 col1" >32 <span style="color: grey">(20.0%) </span></td>
      <td id="T_08bdd_row4_col2" class="data row4 col2" >2 <span style="color: grey">(1.2%) </span></td>
      <td id="T_08bdd_row4_col3" class="data row4 col3" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_08bdd_row4_col4" class="data row4 col4" >160 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



## <a id='toc1_4_'></a>[slides](#toc0_)

### <a id='toc1_4_1_'></a>[slide 1](#toc0_)


    
![svg](2_analyze_files/output_20_0.svg)
    



<style type="text/css">
#T_66b18 th {
  text-align: right;
}
#T_66b18 td {
  text-align: right;
}
#T_66b18_row0_col0, #T_66b18_row0_col2, #T_66b18_row0_col4, #T_66b18_row0_col5, #T_66b18_row0_col6, #T_66b18_row0_col7, #T_66b18_row0_col9, #T_66b18_row0_col10, #T_66b18_row0_col11, #T_66b18_row0_col13, #T_66b18_row1_col3, #T_66b18_row1_col6, #T_66b18_row1_col7, #T_66b18_row2_col0, #T_66b18_row2_col3, #T_66b18_row2_col5, #T_66b18_row2_col11, #T_66b18_row3_col0, #T_66b18_row3_col5, #T_66b18_row3_col6, #T_66b18_row3_col7, #T_66b18_row3_col12, #T_66b18_row4_col0, #T_66b18_row4_col3, #T_66b18_row4_col5, #T_66b18_row4_col9, #T_66b18_row4_col12, #T_66b18_row5_col0, #T_66b18_row5_col1, #T_66b18_row5_col2, #T_66b18_row5_col3, #T_66b18_row5_col4, #T_66b18_row5_col5, #T_66b18_row5_col6, #T_66b18_row5_col7, #T_66b18_row5_col11, #T_66b18_row5_col12, #T_66b18_row5_col13, #T_66b18_row6_col0, #T_66b18_row6_col1, #T_66b18_row6_col2, #T_66b18_row6_col3, #T_66b18_row6_col4, #T_66b18_row6_col5, #T_66b18_row6_col6, #T_66b18_row6_col7, #T_66b18_row6_col9, #T_66b18_row6_col10, #T_66b18_row6_col11, #T_66b18_row7_col2, #T_66b18_row7_col3, #T_66b18_row7_col10 {
  width: 10em;
  font-family: Courier;
}
#T_66b18_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_66b18_row0_col3, #T_66b18_row3_col3, #T_66b18_row7_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_66b18_row0_col8, #T_66b18_row0_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_66b18_row0_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.7%, transparent 3.7%);
  font-family: Courier;
}
#T_66b18_row0_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.7%, transparent 4.7%);
  font-family: Courier;
}
#T_66b18_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_66b18_row1_col1, #T_66b18_row1_col11, #T_66b18_row2_col7, #T_66b18_row3_col11, #T_66b18_row4_col7, #T_66b18_row7_col0, #T_66b18_row7_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_66b18_row1_col2, #T_66b18_row1_col4, #T_66b18_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.6%, transparent 28.6%);
  font-family: Courier;
}
#T_66b18_row1_col5, #T_66b18_row1_col10, #T_66b18_row2_col6, #T_66b18_row3_col10, #T_66b18_row4_col6, #T_66b18_row4_col10 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_66b18_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.4%, transparent 40.4%);
  font-family: Courier;
}
#T_66b18_row1_col9, #T_66b18_row3_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_66b18_row1_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.7%, transparent 40.7%);
  font-family: Courier;
}
#T_66b18_row1_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.2%, transparent 47.2%);
  font-family: Courier;
}
#T_66b18_row1_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.9%, transparent 21.9%);
  font-family: Courier;
}
#T_66b18_row1_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.0%, transparent 35.0%);
  font-family: Courier;
}
#T_66b18_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.1%, transparent 27.1%);
  font-family: Courier;
}
#T_66b18_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.9%, transparent 42.9%);
  font-family: Courier;
}
#T_66b18_row2_col4, #T_66b18_row3_col2, #T_66b18_row4_col2, #T_66b18_row4_col4, #T_66b18_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_66b18_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.7%, transparent 19.7%);
  font-family: Courier;
}
#T_66b18_row2_col9, #T_66b18_row7_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_66b18_row2_col10, #T_66b18_row4_col1, #T_66b18_row5_col10 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_66b18_row2_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.6%, transparent 29.6%);
  font-family: Courier;
}
#T_66b18_row2_col13, #T_66b18_row6_col13, #T_66b18_row7_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_66b18_row2_col14, #T_66b18_row4_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.8%, transparent 18.8%);
  font-family: Courier;
}
#T_66b18_row2_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.8%, transparent 19.8%);
  font-family: Courier;
}
#T_66b18_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.2%, transparent 4.2%);
  font-family: Courier;
}
#T_66b18_row3_col8, #T_66b18_row6_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_66b18_row3_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.8%, transparent 2.8%);
  font-family: Courier;
}
#T_66b18_row3_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.1%, transparent 14.1%);
  font-family: Courier;
}
#T_66b18_row3_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.2%, transparent 8.2%);
  font-family: Courier;
}
#T_66b18_row4_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.0%, transparent 9.0%);
  font-family: Courier;
}
#T_66b18_row4_col11, #T_66b18_row7_col1, #T_66b18_row7_col11 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_66b18_row4_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_66b18_row4_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.9%, transparent 10.9%);
  font-family: Courier;
}
#T_66b18_row5_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_66b18_row5_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_66b18_row5_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_66b18_row5_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_66b18_row6_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.8%, transparent 14.8%);
  font-family: Courier;
}
#T_66b18_row6_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_66b18_row6_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.6%, transparent 4.6%);
  font-family: Courier;
}
#T_66b18_row7_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.0%, transparent 75.0%);
  font-family: Courier;
}
#T_66b18_row7_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
#T_66b18_row7_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.4%, transparent 19.4%);
  font-family: Courier;
}
#T_66b18_row7_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.2%, transparent 17.2%);
  font-family: Courier;
}
#T_66b18_row7_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.9%, transparent 16.9%);
  font-family: Courier;
}
#T_66b18_row8_col0, #T_66b18_row8_col1, #T_66b18_row8_col2, #T_66b18_row8_col3, #T_66b18_row8_col4, #T_66b18_row8_col5, #T_66b18_row8_col6, #T_66b18_row8_col7, #T_66b18_row8_col8, #T_66b18_row8_col9, #T_66b18_row8_col10, #T_66b18_row8_col11, #T_66b18_row8_col12, #T_66b18_row8_col13, #T_66b18_row8_col14, #T_66b18_row8_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_66b18">
  <thead>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th id="T_66b18_level0_col0" class="col_heading level0 col0" >Bone injuries</th>
      <th id="T_66b18_level0_col1" class="col_heading level0 col1" >Circulatory problems</th>
      <th id="T_66b18_level0_col2" class="col_heading level0 col2" >Coughing fit</th>
      <th id="T_66b18_level0_col3" class="col_heading level0 col3" >Enuresis</th>
      <th id="T_66b18_level0_col4" class="col_heading level0 col4" >Itching</th>
      <th id="T_66b18_level0_col5" class="col_heading level0 col5" >Muscle cramps</th>
      <th id="T_66b18_level0_col6" class="col_heading level0 col6" >Muscle soreness</th>
      <th id="T_66b18_level0_col7" class="col_heading level0 col7" >Nosebleed</th>
      <th id="T_66b18_level0_col8" class="col_heading level0 col8" >Pain</th>
      <th id="T_66b18_level0_col9" class="col_heading level0 col9" >Psychological stress reaction</th>
      <th id="T_66b18_level0_col10" class="col_heading level0 col10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <th id="T_66b18_level0_col11" class="col_heading level0 col11" >Severe exhaustion</th>
      <th id="T_66b18_level0_col12" class="col_heading level0 col12" >Superficial injuries</th>
      <th id="T_66b18_level0_col13" class="col_heading level0 col13" >Weichteil-/Gewebeverletzung</th>
      <th id="T_66b18_level0_col14" class="col_heading level0 col14" >Übelkeit / Erbrechen</th>
      <th id="T_66b18_level0_col15" class="col_heading level0 col15" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.07] Main motor skill</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
      <th class="blank col12" >&nbsp;</th>
      <th class="blank col13" >&nbsp;</th>
      <th class="blank col14" >&nbsp;</th>
      <th class="blank col15" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_66b18_level0_row0" class="row_heading level0 row0" ><NA></th>
      <td id="T_66b18_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col1" class="data row0 col1" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_66b18_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col3" class="data row0 col3" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_66b18_row0_col4" class="data row0 col4" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col5" class="data row0 col5" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col6" class="data row0 col6" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col7" class="data row0 col7" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col8" class="data row0 col8" >6 <span style="color: grey">(3.4%) </span></td>
      <td id="T_66b18_row0_col9" class="data row0 col9" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col10" class="data row0 col10" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col11" class="data row0 col11" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col12" class="data row0 col12" >1 <span style="color: grey">(3.7%) </span></td>
      <td id="T_66b18_row0_col13" class="data row0 col13" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row0_col14" class="data row0 col14" >3 <span style="color: grey">(4.7%) </span></td>
      <td id="T_66b18_row0_col15" class="data row0 col15" >14 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row1" class="row_heading level0 row1" >Coordination</th>
      <td id="T_66b18_row1_col0" class="data row1 col0" >2 <span style="color: grey">(66.7%) </span></td>
      <td id="T_66b18_row1_col1" class="data row1 col1" >16 <span style="color: grey">(33.3%) </span></td>
      <td id="T_66b18_row1_col2" class="data row1 col2" >2 <span style="color: grey">(28.6%) </span></td>
      <td id="T_66b18_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row1_col4" class="data row1 col4" >2 <span style="color: grey">(28.6%) </span></td>
      <td id="T_66b18_row1_col5" class="data row1 col5" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_66b18_row1_col6" class="data row1 col6" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row1_col7" class="data row1 col7" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row1_col8" class="data row1 col8" >72 <span style="color: grey">(40.4%) </span></td>
      <td id="T_66b18_row1_col9" class="data row1 col9" >4 <span style="color: grey">(30.8%) </span></td>
      <td id="T_66b18_row1_col10" class="data row1 col10" >2 <span style="color: grey">(25.0%) </span></td>
      <td id="T_66b18_row1_col11" class="data row1 col11" >2 <span style="color: grey">(33.3%) </span></td>
      <td id="T_66b18_row1_col12" class="data row1 col12" >11 <span style="color: grey">(40.7%) </span></td>
      <td id="T_66b18_row1_col13" class="data row1 col13" >17 <span style="color: grey">(47.2%) </span></td>
      <td id="T_66b18_row1_col14" class="data row1 col14" >14 <span style="color: grey">(21.9%) </span></td>
      <td id="T_66b18_row1_col15" class="data row1 col15" >145 <span style="color: grey">(35.0%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row2" class="row_heading level0 row2" >Endurance</th>
      <td id="T_66b18_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row2_col1" class="data row2 col1" >13 <span style="color: grey">(27.1%) </span></td>
      <td id="T_66b18_row2_col2" class="data row2 col2" >3 <span style="color: grey">(42.9%) </span></td>
      <td id="T_66b18_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row2_col4" class="data row2 col4" >1 <span style="color: grey">(14.3%) </span></td>
      <td id="T_66b18_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row2_col6" class="data row2 col6" >2 <span style="color: grey">(25.0%) </span></td>
      <td id="T_66b18_row2_col7" class="data row2 col7" >1 <span style="color: grey">(33.3%) </span></td>
      <td id="T_66b18_row2_col8" class="data row2 col8" >35 <span style="color: grey">(19.7%) </span></td>
      <td id="T_66b18_row2_col9" class="data row2 col9" >2 <span style="color: grey">(15.4%) </span></td>
      <td id="T_66b18_row2_col10" class="data row2 col10" >1 <span style="color: grey">(12.5%) </span></td>
      <td id="T_66b18_row2_col11" class="data row2 col11" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row2_col12" class="data row2 col12" >8 <span style="color: grey">(29.6%) </span></td>
      <td id="T_66b18_row2_col13" class="data row2 col13" >4 <span style="color: grey">(11.1%) </span></td>
      <td id="T_66b18_row2_col14" class="data row2 col14" >12 <span style="color: grey">(18.8%) </span></td>
      <td id="T_66b18_row2_col15" class="data row2 col15" >82 <span style="color: grey">(19.8%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row3" class="row_heading level0 row3" >Flexibility</th>
      <td id="T_66b18_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row3_col1" class="data row3 col1" >2 <span style="color: grey">(4.2%) </span></td>
      <td id="T_66b18_row3_col2" class="data row3 col2" >1 <span style="color: grey">(14.3%) </span></td>
      <td id="T_66b18_row3_col3" class="data row3 col3" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_66b18_row3_col4" class="data row3 col4" >2 <span style="color: grey">(28.6%) </span></td>
      <td id="T_66b18_row3_col5" class="data row3 col5" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row3_col6" class="data row3 col6" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row3_col7" class="data row3 col7" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row3_col8" class="data row3 col8" >10 <span style="color: grey">(5.6%) </span></td>
      <td id="T_66b18_row3_col9" class="data row3 col9" >4 <span style="color: grey">(30.8%) </span></td>
      <td id="T_66b18_row3_col10" class="data row3 col10" >2 <span style="color: grey">(25.0%) </span></td>
      <td id="T_66b18_row3_col11" class="data row3 col11" >2 <span style="color: grey">(33.3%) </span></td>
      <td id="T_66b18_row3_col12" class="data row3 col12" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row3_col13" class="data row3 col13" >1 <span style="color: grey">(2.8%) </span></td>
      <td id="T_66b18_row3_col14" class="data row3 col14" >9 <span style="color: grey">(14.1%) </span></td>
      <td id="T_66b18_row3_col15" class="data row3 col15" >34 <span style="color: grey">(8.2%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row4" class="row_heading level0 row4" >Full body</th>
      <td id="T_66b18_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row4_col1" class="data row4 col1" >6 <span style="color: grey">(12.5%) </span></td>
      <td id="T_66b18_row4_col2" class="data row4 col2" >1 <span style="color: grey">(14.3%) </span></td>
      <td id="T_66b18_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row4_col4" class="data row4 col4" >1 <span style="color: grey">(14.3%) </span></td>
      <td id="T_66b18_row4_col5" class="data row4 col5" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row4_col6" class="data row4 col6" >2 <span style="color: grey">(25.0%) </span></td>
      <td id="T_66b18_row4_col7" class="data row4 col7" >1 <span style="color: grey">(33.3%) </span></td>
      <td id="T_66b18_row4_col8" class="data row4 col8" >16 <span style="color: grey">(9.0%) </span></td>
      <td id="T_66b18_row4_col9" class="data row4 col9" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row4_col10" class="data row4 col10" >2 <span style="color: grey">(25.0%) </span></td>
      <td id="T_66b18_row4_col11" class="data row4 col11" >1 <span style="color: grey">(16.7%) </span></td>
      <td id="T_66b18_row4_col12" class="data row4 col12" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row4_col13" class="data row4 col13" >3 <span style="color: grey">(8.3%) </span></td>
      <td id="T_66b18_row4_col14" class="data row4 col14" >12 <span style="color: grey">(18.8%) </span></td>
      <td id="T_66b18_row4_col15" class="data row4 col15" >45 <span style="color: grey">(10.9%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row5" class="row_heading level0 row5" >Relaxation</th>
      <td id="T_66b18_row5_col0" class="data row5 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col4" class="data row5 col4" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col5" class="data row5 col5" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col6" class="data row5 col6" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col7" class="data row5 col7" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col8" class="data row5 col8" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_66b18_row5_col9" class="data row5 col9" >1 <span style="color: grey">(7.7%) </span></td>
      <td id="T_66b18_row5_col10" class="data row5 col10" >1 <span style="color: grey">(12.5%) </span></td>
      <td id="T_66b18_row5_col11" class="data row5 col11" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col12" class="data row5 col12" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col13" class="data row5 col13" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row5_col14" class="data row5 col14" >2 <span style="color: grey">(3.1%) </span></td>
      <td id="T_66b18_row5_col15" class="data row5 col15" >5 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row6" class="row_heading level0 row6" >Speed</th>
      <td id="T_66b18_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col4" class="data row6 col4" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col5" class="data row6 col5" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col6" class="data row6 col6" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col7" class="data row6 col7" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col8" class="data row6 col8" >10 <span style="color: grey">(5.6%) </span></td>
      <td id="T_66b18_row6_col9" class="data row6 col9" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col10" class="data row6 col10" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col11" class="data row6 col11" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row6_col12" class="data row6 col12" >4 <span style="color: grey">(14.8%) </span></td>
      <td id="T_66b18_row6_col13" class="data row6 col13" >4 <span style="color: grey">(11.1%) </span></td>
      <td id="T_66b18_row6_col14" class="data row6 col14" >1 <span style="color: grey">(1.6%) </span></td>
      <td id="T_66b18_row6_col15" class="data row6 col15" >19 <span style="color: grey">(4.6%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row7" class="row_heading level0 row7" >Strength</th>
      <td id="T_66b18_row7_col0" class="data row7 col0" >1 <span style="color: grey">(33.3%) </span></td>
      <td id="T_66b18_row7_col1" class="data row7 col1" >8 <span style="color: grey">(16.7%) </span></td>
      <td id="T_66b18_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row7_col4" class="data row7 col4" >1 <span style="color: grey">(14.3%) </span></td>
      <td id="T_66b18_row7_col5" class="data row7 col5" >3 <span style="color: grey">(75.0%) </span></td>
      <td id="T_66b18_row7_col6" class="data row7 col6" >4 <span style="color: grey">(50.0%) </span></td>
      <td id="T_66b18_row7_col7" class="data row7 col7" >1 <span style="color: grey">(33.3%) </span></td>
      <td id="T_66b18_row7_col8" class="data row7 col8" >28 <span style="color: grey">(15.7%) </span></td>
      <td id="T_66b18_row7_col9" class="data row7 col9" >2 <span style="color: grey">(15.4%) </span></td>
      <td id="T_66b18_row7_col10" class="data row7 col10" ><span style="color: grey">0 </span></td>
      <td id="T_66b18_row7_col11" class="data row7 col11" >1 <span style="color: grey">(16.7%) </span></td>
      <td id="T_66b18_row7_col12" class="data row7 col12" >3 <span style="color: grey">(11.1%) </span></td>
      <td id="T_66b18_row7_col13" class="data row7 col13" >7 <span style="color: grey">(19.4%) </span></td>
      <td id="T_66b18_row7_col14" class="data row7 col14" >11 <span style="color: grey">(17.2%) </span></td>
      <td id="T_66b18_row7_col15" class="data row7 col15" >70 <span style="color: grey">(16.9%) </span></td>
    </tr>
    <tr>
      <th id="T_66b18_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_66b18_row8_col0" class="data row8 col0" >3 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col1" class="data row8 col1" >48 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col2" class="data row8 col2" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col3" class="data row8 col3" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col4" class="data row8 col4" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col5" class="data row8 col5" >4 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col6" class="data row8 col6" >8 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col7" class="data row8 col7" >3 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col8" class="data row8 col8" >178 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col9" class="data row8 col9" >13 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col10" class="data row8 col10" >8 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col11" class="data row8 col11" >6 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col12" class="data row8 col12" >27 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col13" class="data row8 col13" >36 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col14" class="data row8 col14" >64 <span style="color: grey">(100.0%) </span></td>
      <td id="T_66b18_row8_col15" class="data row8 col15" >414 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_2_'></a>[slide 2](#toc0_)


    
![svg](2_analyze_files/output_22_0.svg)
    



<style type="text/css">
#T_e8e16 th {
  text-align: right;
}
#T_e8e16 td {
  text-align: right;
}
#T_e8e16_row0_col0, #T_e8e16_row0_col3, #T_e8e16_row1_col3, #T_e8e16_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.1%, transparent 7.1%);
  font-family: Courier;
}
#T_e8e16_row0_col1, #T_e8e16_row0_col6, #T_e8e16_row1_col1, #T_e8e16_row1_col2, #T_e8e16_row1_col6, #T_e8e16_row2_col0, #T_e8e16_row2_col1, #T_e8e16_row2_col6, #T_e8e16_row3_col4, #T_e8e16_row3_col6, #T_e8e16_row4_col0, #T_e8e16_row4_col1, #T_e8e16_row4_col3, #T_e8e16_row4_col4, #T_e8e16_row4_col6, #T_e8e16_row5_col6, #T_e8e16_row6_col0, #T_e8e16_row6_col6, #T_e8e16_row7_col1 {
  width: 10em;
  font-family: Courier;
}
#T_e8e16_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.1%, transparent 5.1%);
  font-family: Courier;
}
#T_e8e16_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_e8e16_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.2%, transparent 9.2%);
  font-family: Courier;
}
#T_e8e16_row0_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_e8e16_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_e8e16_row1_col4, #T_e8e16_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_e8e16_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_e8e16_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_e8e16_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.9%, transparent 2.9%);
  font-family: Courier;
}
#T_e8e16_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.5%, transparent 3.5%);
  font-family: Courier;
}
#T_e8e16_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_e8e16_row2_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.1%, transparent 4.1%);
  font-family: Courier;
}
#T_e8e16_row2_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_e8e16_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.7%, transparent 35.7%);
  font-family: Courier;
}
#T_e8e16_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_e8e16_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.3%, transparent 26.3%);
  font-family: Courier;
}
#T_e8e16_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.1%, transparent 27.1%);
  font-family: Courier;
}
#T_e8e16_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.7%, transparent 33.7%);
  font-family: Courier;
}
#T_e8e16_row3_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.0%, transparent 27.0%);
  font-family: Courier;
}
#T_e8e16_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_e8e16_row4_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_e8e16_row4_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_e8e16_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 46.4%, transparent 46.4%);
  font-family: Courier;
}
#T_e8e16_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 70.0%, transparent 70.0%);
  font-family: Courier;
}
#T_e8e16_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.5%, transparent 44.5%);
  font-family: Courier;
}
#T_e8e16_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 32.9%, transparent 32.9%);
  font-family: Courier;
}
#T_e8e16_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_e8e16_row5_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.8%, transparent 37.8%);
  font-family: Courier;
}
#T_e8e16_row5_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.0%, transparent 39.0%);
  font-family: Courier;
}
#T_e8e16_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_e8e16_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_e8e16_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.9%, transparent 5.9%);
  font-family: Courier;
}
#T_e8e16_row6_col5, #T_e8e16_row7_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.1%, transparent 6.1%);
  font-family: Courier;
}
#T_e8e16_row6_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_e8e16_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.1%, transparent 16.1%);
  font-family: Courier;
}
#T_e8e16_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.5%, transparent 16.5%);
  font-family: Courier;
}
#T_e8e16_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.5%, transparent 38.5%);
  font-family: Courier;
}
#T_e8e16_row7_col6, #T_e8e16_row8_col0, #T_e8e16_row8_col1, #T_e8e16_row8_col2, #T_e8e16_row8_col3, #T_e8e16_row8_col4, #T_e8e16_row8_col5, #T_e8e16_row8_col6, #T_e8e16_row8_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_e8e16_row7_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
</style>
<table id="T_e8e16">
  <thead>
    <tr>
      <th class="index_name level0" >[05.06] Setting</th>
      <th id="T_e8e16_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_e8e16_level0_col1" class="col_heading level0 col1" >At home (via telemedicine)</th>
      <th id="T_e8e16_level0_col2" class="col_heading level0 col2" >Gym</th>
      <th id="T_e8e16_level0_col3" class="col_heading level0 col3" >Hospital corridor</th>
      <th id="T_e8e16_level0_col4" class="col_heading level0 col4" >Outside</th>
      <th id="T_e8e16_level0_col5" class="col_heading level0 col5" >Patients room</th>
      <th id="T_e8e16_level0_col6" class="col_heading level0 col6" >Weiteres</th>
      <th id="T_e8e16_level0_col7" class="col_heading level0 col7" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e8e16_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_e8e16_row0_col0" class="data row0 col0" >2 <span style="color: grey">(7.1%) </span></td>
      <td id="T_e8e16_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row0_col2" class="data row0 col2" >7 <span style="color: grey">(5.1%) </span></td>
      <td id="T_e8e16_row0_col3" class="data row0 col3" >6 <span style="color: grey">(7.1%) </span></td>
      <td id="T_e8e16_row0_col4" class="data row0 col4" >8 <span style="color: grey">(30.8%) </span></td>
      <td id="T_e8e16_row0_col5" class="data row0 col5" >9 <span style="color: grey">(9.2%) </span></td>
      <td id="T_e8e16_row0_col6" class="data row0 col6" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row0_col7" class="data row0 col7" >32 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_e8e16_row1_col0" class="data row1 col0" >1 <span style="color: grey">(3.6%) </span></td>
      <td id="T_e8e16_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row1_col3" class="data row1 col3" >6 <span style="color: grey">(7.1%) </span></td>
      <td id="T_e8e16_row1_col4" class="data row1 col4" >1 <span style="color: grey">(3.8%) </span></td>
      <td id="T_e8e16_row1_col5" class="data row1 col5" >2 <span style="color: grey">(2.0%) </span></td>
      <td id="T_e8e16_row1_col6" class="data row1 col6" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row1_col7" class="data row1 col7" >10 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_e8e16_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row2_col2" class="data row2 col2" >4 <span style="color: grey">(2.9%) </span></td>
      <td id="T_e8e16_row2_col3" class="data row2 col3" >3 <span style="color: grey">(3.5%) </span></td>
      <td id="T_e8e16_row2_col4" class="data row2 col4" >2 <span style="color: grey">(7.7%) </span></td>
      <td id="T_e8e16_row2_col5" class="data row2 col5" >4 <span style="color: grey">(4.1%) </span></td>
      <td id="T_e8e16_row2_col6" class="data row2 col6" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row2_col7" class="data row2 col7" >13 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_e8e16_row3_col0" class="data row3 col0" >10 <span style="color: grey">(35.7%) </span></td>
      <td id="T_e8e16_row3_col1" class="data row3 col1" >2 <span style="color: grey">(20.0%) </span></td>
      <td id="T_e8e16_row3_col2" class="data row3 col2" >36 <span style="color: grey">(26.3%) </span></td>
      <td id="T_e8e16_row3_col3" class="data row3 col3" >23 <span style="color: grey">(27.1%) </span></td>
      <td id="T_e8e16_row3_col4" class="data row3 col4" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row3_col5" class="data row3 col5" >33 <span style="color: grey">(33.7%) </span></td>
      <td id="T_e8e16_row3_col6" class="data row3 col6" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row3_col7" class="data row3 col7" >104 <span style="color: grey">(27.0%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_e8e16_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row4_col2" class="data row4 col2" >1 <span style="color: grey">(0.7%) </span></td>
      <td id="T_e8e16_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row4_col5" class="data row4 col5" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_e8e16_row4_col6" class="data row4 col6" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row4_col7" class="data row4 col7" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_e8e16_row5_col0" class="data row5 col0" >13 <span style="color: grey">(46.4%) </span></td>
      <td id="T_e8e16_row5_col1" class="data row5 col1" >7 <span style="color: grey">(70.0%) </span></td>
      <td id="T_e8e16_row5_col2" class="data row5 col2" >61 <span style="color: grey">(44.5%) </span></td>
      <td id="T_e8e16_row5_col3" class="data row5 col3" >28 <span style="color: grey">(32.9%) </span></td>
      <td id="T_e8e16_row5_col4" class="data row5 col4" >4 <span style="color: grey">(15.4%) </span></td>
      <td id="T_e8e16_row5_col5" class="data row5 col5" >37 <span style="color: grey">(37.8%) </span></td>
      <td id="T_e8e16_row5_col6" class="data row5 col6" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row5_col7" class="data row5 col7" >150 <span style="color: grey">(39.0%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_e8e16_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row6_col1" class="data row6 col1" >1 <span style="color: grey">(10.0%) </span></td>
      <td id="T_e8e16_row6_col2" class="data row6 col2" >6 <span style="color: grey">(4.4%) </span></td>
      <td id="T_e8e16_row6_col3" class="data row6 col3" >5 <span style="color: grey">(5.9%) </span></td>
      <td id="T_e8e16_row6_col4" class="data row6 col4" >1 <span style="color: grey">(3.8%) </span></td>
      <td id="T_e8e16_row6_col5" class="data row6 col5" >6 <span style="color: grey">(6.1%) </span></td>
      <td id="T_e8e16_row6_col6" class="data row6 col6" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row6_col7" class="data row6 col7" >19 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_e8e16_row7_col0" class="data row7 col0" >2 <span style="color: grey">(7.1%) </span></td>
      <td id="T_e8e16_row7_col1" class="data row7 col1" ><span style="color: grey">0 </span></td>
      <td id="T_e8e16_row7_col2" class="data row7 col2" >22 <span style="color: grey">(16.1%) </span></td>
      <td id="T_e8e16_row7_col3" class="data row7 col3" >14 <span style="color: grey">(16.5%) </span></td>
      <td id="T_e8e16_row7_col4" class="data row7 col4" >10 <span style="color: grey">(38.5%) </span></td>
      <td id="T_e8e16_row7_col5" class="data row7 col5" >6 <span style="color: grey">(6.1%) </span></td>
      <td id="T_e8e16_row7_col6" class="data row7 col6" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row7_col7" class="data row7 col7" >55 <span style="color: grey">(14.3%) </span></td>
    </tr>
    <tr>
      <th id="T_e8e16_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_e8e16_row8_col0" class="data row8 col0" >28 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row8_col1" class="data row8 col1" >10 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row8_col2" class="data row8 col2" >137 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row8_col3" class="data row8 col3" >85 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row8_col4" class="data row8 col4" >26 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row8_col5" class="data row8 col5" >98 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row8_col6" class="data row8 col6" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_e8e16_row8_col7" class="data row8 col7" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_3_'></a>[slide 3](#toc0_)


    
![svg](2_analyze_files/output_24_0.svg)
    



<style type="text/css">
#T_2a5ae th {
  text-align: right;
}
#T_2a5ae td {
  text-align: right;
}
#T_2a5ae_row0_col0, #T_2a5ae_row0_col2, #T_2a5ae_row0_col5, #T_2a5ae_row0_col7, #T_2a5ae_row0_col9, #T_2a5ae_row0_col10, #T_2a5ae_row0_col11, #T_2a5ae_row1_col0, #T_2a5ae_row1_col7, #T_2a5ae_row1_col10, #T_2a5ae_row2_col0, #T_2a5ae_row2_col2, #T_2a5ae_row2_col3, #T_2a5ae_row2_col4, #T_2a5ae_row2_col5, #T_2a5ae_row2_col6, #T_2a5ae_row2_col11, #T_2a5ae_row3_col3, #T_2a5ae_row4_col0, #T_2a5ae_row4_col1, #T_2a5ae_row4_col2, #T_2a5ae_row4_col3, #T_2a5ae_row4_col4, #T_2a5ae_row4_col5, #T_2a5ae_row4_col6, #T_2a5ae_row4_col7, #T_2a5ae_row4_col9, #T_2a5ae_row4_col11, #T_2a5ae_row4_col12, #T_2a5ae_row4_col13, #T_2a5ae_row4_col14 {
  width: 10em;
  font-family: Courier;
}
#T_2a5ae_row0_col1, #T_2a5ae_row0_col14, #T_2a5ae_row3_col10, #T_2a5ae_row4_col10 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_2a5ae_row0_col3, #T_2a5ae_row1_col3, #T_2a5ae_row2_col10, #T_2a5ae_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_2a5ae_row0_col4, #T_2a5ae_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_2a5ae_row0_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_2a5ae_row0_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.3%, transparent 23.3%);
  font-family: Courier;
}
#T_2a5ae_row0_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.5%, transparent 23.5%);
  font-family: Courier;
}
#T_2a5ae_row0_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.0%, transparent 24.0%);
  font-family: Courier;
}
#T_2a5ae_row0_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.1%, transparent 21.1%);
  font-family: Courier;
}
#T_2a5ae_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.5%, transparent 17.5%);
  font-family: Courier;
}
#T_2a5ae_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_2a5ae_row1_col5, #T_2a5ae_row2_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_2a5ae_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.6%, transparent 28.6%);
  font-family: Courier;
}
#T_2a5ae_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.2%, transparent 20.2%);
  font-family: Courier;
}
#T_2a5ae_row1_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 45.5%, transparent 45.5%);
  font-family: Courier;
}
#T_2a5ae_row1_col11 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.9%, transparent 42.9%);
  font-family: Courier;
}
#T_2a5ae_row1_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.6%, transparent 17.6%);
  font-family: Courier;
}
#T_2a5ae_row1_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.0%, transparent 36.0%);
  font-family: Courier;
}
#T_2a5ae_row1_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.9%, transparent 22.9%);
  font-family: Courier;
}
#T_2a5ae_row1_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.1%, transparent 23.1%);
  font-family: Courier;
}
#T_2a5ae_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.5%, transparent 7.5%);
  font-family: Courier;
}
#T_2a5ae_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.6%, transparent 11.6%);
  font-family: Courier;
}
#T_2a5ae_row2_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.2%, transparent 18.2%);
  font-family: Courier;
}
#T_2a5ae_row2_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.8%, transparent 11.8%);
  font-family: Courier;
}
#T_2a5ae_row2_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_2a5ae_row2_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.6%, transparent 14.6%);
  font-family: Courier;
}
#T_2a5ae_row2_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.4%, transparent 11.4%);
  font-family: Courier;
}
#T_2a5ae_row3_col0, #T_2a5ae_row5_col0, #T_2a5ae_row5_col1, #T_2a5ae_row5_col2, #T_2a5ae_row5_col3, #T_2a5ae_row5_col4, #T_2a5ae_row5_col5, #T_2a5ae_row5_col6, #T_2a5ae_row5_col7, #T_2a5ae_row5_col8, #T_2a5ae_row5_col9, #T_2a5ae_row5_col10, #T_2a5ae_row5_col11, #T_2a5ae_row5_col12, #T_2a5ae_row5_col13, #T_2a5ae_row5_col14, #T_2a5ae_row5_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_2a5ae_row3_col2, #T_2a5ae_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 60.0%, transparent 60.0%);
  font-family: Courier;
}
#T_2a5ae_row3_col5, #T_2a5ae_row3_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_2a5ae_row3_col6, #T_2a5ae_row3_col11 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.1%, transparent 57.1%);
  font-family: Courier;
}
#T_2a5ae_row3_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.6%, transparent 42.6%);
  font-family: Courier;
}
#T_2a5ae_row3_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.4%, transparent 36.4%);
  font-family: Courier;
}
#T_2a5ae_row3_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.1%, transparent 47.1%);
  font-family: Courier;
}
#T_2a5ae_row3_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.0%, transparent 28.0%);
  font-family: Courier;
}
#T_2a5ae_row3_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.5%, transparent 37.5%);
  font-family: Courier;
}
#T_2a5ae_row3_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 43.2%, transparent 43.2%);
  font-family: Courier;
}
#T_2a5ae_row4_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_2a5ae_row4_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
</style>
<table id="T_2a5ae">
  <thead>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th id="T_2a5ae_level0_col0" class="col_heading level0 col0" >Bone injuries</th>
      <th id="T_2a5ae_level0_col1" class="col_heading level0 col1" >Circulatory problems</th>
      <th id="T_2a5ae_level0_col2" class="col_heading level0 col2" >Coughing fit</th>
      <th id="T_2a5ae_level0_col3" class="col_heading level0 col3" >Enuresis</th>
      <th id="T_2a5ae_level0_col4" class="col_heading level0 col4" >Itching</th>
      <th id="T_2a5ae_level0_col5" class="col_heading level0 col5" >Muscle cramps</th>
      <th id="T_2a5ae_level0_col6" class="col_heading level0 col6" >Muscle soreness</th>
      <th id="T_2a5ae_level0_col7" class="col_heading level0 col7" >Nosebleed</th>
      <th id="T_2a5ae_level0_col8" class="col_heading level0 col8" >Pain</th>
      <th id="T_2a5ae_level0_col9" class="col_heading level0 col9" >Psychological stress reaction</th>
      <th id="T_2a5ae_level0_col10" class="col_heading level0 col10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <th id="T_2a5ae_level0_col11" class="col_heading level0 col11" >Severe exhaustion</th>
      <th id="T_2a5ae_level0_col12" class="col_heading level0 col12" >Superficial injuries</th>
      <th id="T_2a5ae_level0_col13" class="col_heading level0 col13" >Weichteil-/Gewebeverletzung</th>
      <th id="T_2a5ae_level0_col14" class="col_heading level0 col14" >Übelkeit / Erbrechen</th>
      <th id="T_2a5ae_level0_col15" class="col_heading level0 col15" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.09] Training condition</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
      <th class="blank col12" >&nbsp;</th>
      <th class="blank col13" >&nbsp;</th>
      <th class="blank col14" >&nbsp;</th>
      <th class="blank col15" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2a5ae_level0_row0" class="row_heading level0 row0" ><NA></th>
      <td id="T_2a5ae_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row0_col1" class="data row0 col1" >10 <span style="color: grey">(25.0%) </span></td>
      <td id="T_2a5ae_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row0_col3" class="data row0 col3" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_2a5ae_row0_col4" class="data row0 col4" >1 <span style="color: grey">(20.0%) </span></td>
      <td id="T_2a5ae_row0_col5" class="data row0 col5" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row0_col6" class="data row0 col6" >1 <span style="color: grey">(14.3%) </span></td>
      <td id="T_2a5ae_row0_col7" class="data row0 col7" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row0_col8" class="data row0 col8" >30 <span style="color: grey">(23.3%) </span></td>
      <td id="T_2a5ae_row0_col9" class="data row0 col9" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row0_col10" class="data row0 col10" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row0_col11" class="data row0 col11" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row0_col12" class="data row0 col12" >4 <span style="color: grey">(23.5%) </span></td>
      <td id="T_2a5ae_row0_col13" class="data row0 col13" >6 <span style="color: grey">(24.0%) </span></td>
      <td id="T_2a5ae_row0_col14" class="data row0 col14" >12 <span style="color: grey">(25.0%) </span></td>
      <td id="T_2a5ae_row0_col15" class="data row0 col15" >65 <span style="color: grey">(21.1%) </span></td>
    </tr>
    <tr>
      <th id="T_2a5ae_level0_row1" class="row_heading level0 row1" >Average</th>
      <td id="T_2a5ae_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row1_col1" class="data row1 col1" >7 <span style="color: grey">(17.5%) </span></td>
      <td id="T_2a5ae_row1_col2" class="data row1 col2" >2 <span style="color: grey">(40.0%) </span></td>
      <td id="T_2a5ae_row1_col3" class="data row1 col3" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_2a5ae_row1_col4" class="data row1 col4" >1 <span style="color: grey">(20.0%) </span></td>
      <td id="T_2a5ae_row1_col5" class="data row1 col5" >1 <span style="color: grey">(33.3%) </span></td>
      <td id="T_2a5ae_row1_col6" class="data row1 col6" >2 <span style="color: grey">(28.6%) </span></td>
      <td id="T_2a5ae_row1_col7" class="data row1 col7" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row1_col8" class="data row1 col8" >26 <span style="color: grey">(20.2%) </span></td>
      <td id="T_2a5ae_row1_col9" class="data row1 col9" >5 <span style="color: grey">(45.5%) </span></td>
      <td id="T_2a5ae_row1_col10" class="data row1 col10" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row1_col11" class="data row1 col11" >3 <span style="color: grey">(42.9%) </span></td>
      <td id="T_2a5ae_row1_col12" class="data row1 col12" >3 <span style="color: grey">(17.6%) </span></td>
      <td id="T_2a5ae_row1_col13" class="data row1 col13" >9 <span style="color: grey">(36.0%) </span></td>
      <td id="T_2a5ae_row1_col14" class="data row1 col14" >11 <span style="color: grey">(22.9%) </span></td>
      <td id="T_2a5ae_row1_col15" class="data row1 col15" >71 <span style="color: grey">(23.1%) </span></td>
    </tr>
    <tr>
      <th id="T_2a5ae_level0_row2" class="row_heading level0 row2" >Good</th>
      <td id="T_2a5ae_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row2_col1" class="data row2 col1" >3 <span style="color: grey">(7.5%) </span></td>
      <td id="T_2a5ae_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row2_col6" class="data row2 col6" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row2_col7" class="data row2 col7" >1 <span style="color: grey">(33.3%) </span></td>
      <td id="T_2a5ae_row2_col8" class="data row2 col8" >15 <span style="color: grey">(11.6%) </span></td>
      <td id="T_2a5ae_row2_col9" class="data row2 col9" >2 <span style="color: grey">(18.2%) </span></td>
      <td id="T_2a5ae_row2_col10" class="data row2 col10" >2 <span style="color: grey">(50.0%) </span></td>
      <td id="T_2a5ae_row2_col11" class="data row2 col11" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row2_col12" class="data row2 col12" >2 <span style="color: grey">(11.8%) </span></td>
      <td id="T_2a5ae_row2_col13" class="data row2 col13" >3 <span style="color: grey">(12.0%) </span></td>
      <td id="T_2a5ae_row2_col14" class="data row2 col14" >7 <span style="color: grey">(14.6%) </span></td>
      <td id="T_2a5ae_row2_col15" class="data row2 col15" >35 <span style="color: grey">(11.4%) </span></td>
    </tr>
    <tr>
      <th id="T_2a5ae_level0_row3" class="row_heading level0 row3" >Moderate</th>
      <td id="T_2a5ae_row3_col0" class="data row3 col0" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row3_col1" class="data row3 col1" >20 <span style="color: grey">(50.0%) </span></td>
      <td id="T_2a5ae_row3_col2" class="data row3 col2" >3 <span style="color: grey">(60.0%) </span></td>
      <td id="T_2a5ae_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row3_col4" class="data row3 col4" >3 <span style="color: grey">(60.0%) </span></td>
      <td id="T_2a5ae_row3_col5" class="data row3 col5" >2 <span style="color: grey">(66.7%) </span></td>
      <td id="T_2a5ae_row3_col6" class="data row3 col6" >4 <span style="color: grey">(57.1%) </span></td>
      <td id="T_2a5ae_row3_col7" class="data row3 col7" >2 <span style="color: grey">(66.7%) </span></td>
      <td id="T_2a5ae_row3_col8" class="data row3 col8" >55 <span style="color: grey">(42.6%) </span></td>
      <td id="T_2a5ae_row3_col9" class="data row3 col9" >4 <span style="color: grey">(36.4%) </span></td>
      <td id="T_2a5ae_row3_col10" class="data row3 col10" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_2a5ae_row3_col11" class="data row3 col11" >4 <span style="color: grey">(57.1%) </span></td>
      <td id="T_2a5ae_row3_col12" class="data row3 col12" >8 <span style="color: grey">(47.1%) </span></td>
      <td id="T_2a5ae_row3_col13" class="data row3 col13" >7 <span style="color: grey">(28.0%) </span></td>
      <td id="T_2a5ae_row3_col14" class="data row3 col14" >18 <span style="color: grey">(37.5%) </span></td>
      <td id="T_2a5ae_row3_col15" class="data row3 col15" >133 <span style="color: grey">(43.2%) </span></td>
    </tr>
    <tr>
      <th id="T_2a5ae_level0_row4" class="row_heading level0 row4" >Weiß nicht</th>
      <td id="T_2a5ae_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col5" class="data row4 col5" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col6" class="data row4 col6" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col7" class="data row4 col7" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col8" class="data row4 col8" >3 <span style="color: grey">(2.3%) </span></td>
      <td id="T_2a5ae_row4_col9" class="data row4 col9" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col10" class="data row4 col10" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_2a5ae_row4_col11" class="data row4 col11" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col12" class="data row4 col12" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col13" class="data row4 col13" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col14" class="data row4 col14" ><span style="color: grey">0 </span></td>
      <td id="T_2a5ae_row4_col15" class="data row4 col15" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_2a5ae_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_2a5ae_row5_col0" class="data row5 col0" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col1" class="data row5 col1" >40 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col2" class="data row5 col2" >5 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col3" class="data row5 col3" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col4" class="data row5 col4" >5 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col5" class="data row5 col5" >3 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col6" class="data row5 col6" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col7" class="data row5 col7" >3 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col8" class="data row5 col8" >129 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col9" class="data row5 col9" >11 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col10" class="data row5 col10" >4 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col11" class="data row5 col11" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col12" class="data row5 col12" >17 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col13" class="data row5 col13" >25 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col14" class="data row5 col14" >48 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2a5ae_row5_col15" class="data row5 col15" >308 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_4_'></a>[slide 4](#toc0_)


    
![svg](2_analyze_files/output_26_0.svg)
    



<style type="text/css">
#T_ae8ab th {
  text-align: right;
}
#T_ae8ab td {
  text-align: right;
}
#T_ae8ab_row0_col0, #T_ae8ab_row0_col1, #T_ae8ab_row0_col5, #T_ae8ab_row0_col6, #T_ae8ab_row0_col10, #T_ae8ab_row0_col11, #T_ae8ab_row1_col0, #T_ae8ab_row1_col1, #T_ae8ab_row1_col2, #T_ae8ab_row1_col3, #T_ae8ab_row1_col4, #T_ae8ab_row1_col5, #T_ae8ab_row1_col6, #T_ae8ab_row1_col7, #T_ae8ab_row1_col10, #T_ae8ab_row1_col11, #T_ae8ab_row2_col0, #T_ae8ab_row2_col1, #T_ae8ab_row2_col3, #T_ae8ab_row2_col4, #T_ae8ab_row2_col6, #T_ae8ab_row2_col7, #T_ae8ab_row2_col9, #T_ae8ab_row2_col10, #T_ae8ab_row3_col0, #T_ae8ab_row3_col3, #T_ae8ab_row3_col7, #T_ae8ab_row3_col11, #T_ae8ab_row4_col0, #T_ae8ab_row4_col1, #T_ae8ab_row4_col2, #T_ae8ab_row4_col3, #T_ae8ab_row4_col4, #T_ae8ab_row4_col5, #T_ae8ab_row4_col6, #T_ae8ab_row4_col7, #T_ae8ab_row4_col10, #T_ae8ab_row4_col11, #T_ae8ab_row4_col12, #T_ae8ab_row4_col13, #T_ae8ab_row5_col7, #T_ae8ab_row5_col11, #T_ae8ab_row6_col2, #T_ae8ab_row6_col3, #T_ae8ab_row6_col5, #T_ae8ab_row6_col7, #T_ae8ab_row6_col10, #T_ae8ab_row6_col11, #T_ae8ab_row7_col0, #T_ae8ab_row7_col1, #T_ae8ab_row7_col6, #T_ae8ab_row7_col10, #T_ae8ab_row7_col11 {
  width: 10em;
  font-family: Courier;
}
#T_ae8ab_row0_col2, #T_ae8ab_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_ae8ab_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.2%, transparent 41.2%);
  font-family: Courier;
}
#T_ae8ab_row0_col4, #T_ae8ab_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_ae8ab_row0_col7, #T_ae8ab_row3_col10, #T_ae8ab_row5_col0, #T_ae8ab_row5_col2, #T_ae8ab_row5_col10, #T_ae8ab_row6_col0, #T_ae8ab_row7_col7, #T_ae8ab_row7_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_ae8ab_row0_col8, #T_ae8ab_row5_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.3%, transparent 16.3%);
  font-family: Courier;
}
#T_ae8ab_row0_col9, #T_ae8ab_row4_col9, #T_ae8ab_row7_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_ae8ab_row0_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.7%, transparent 19.7%);
  font-family: Courier;
}
#T_ae8ab_row0_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_ae8ab_row0_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.8%, transparent 8.8%);
  font-family: Courier;
}
#T_ae8ab_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.7%, transparent 4.7%);
  font-family: Courier;
}
#T_ae8ab_row1_col9, #T_ae8ab_row1_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_ae8ab_row1_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.9%, transparent 3.9%);
  font-family: Courier;
}
#T_ae8ab_row1_col13, #T_ae8ab_row3_col13, #T_ae8ab_row5_col13, #T_ae8ab_row6_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_ae8ab_row2_col5, #T_ae8ab_row3_col5, #T_ae8ab_row5_col4, #T_ae8ab_row7_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_ae8ab_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.3%, transparent 9.3%);
  font-family: Courier;
}
#T_ae8ab_row2_col11, #T_ae8ab_row8_col0, #T_ae8ab_row8_col1, #T_ae8ab_row8_col2, #T_ae8ab_row8_col3, #T_ae8ab_row8_col4, #T_ae8ab_row8_col5, #T_ae8ab_row8_col6, #T_ae8ab_row8_col7, #T_ae8ab_row8_col8, #T_ae8ab_row8_col9, #T_ae8ab_row8_col10, #T_ae8ab_row8_col11, #T_ae8ab_row8_col12, #T_ae8ab_row8_col13, #T_ae8ab_row8_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_ae8ab_row2_col12, #T_ae8ab_row3_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_ae8ab_row2_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_ae8ab_row2_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.2%, transparent 3.2%);
  font-family: Courier;
}
#T_ae8ab_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.4%, transparent 39.4%);
  font-family: Courier;
}
#T_ae8ab_row3_col2, #T_ae8ab_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.8%, transparent 18.8%);
  font-family: Courier;
}
#T_ae8ab_row3_col4, #T_ae8ab_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.0%, transparent 30.0%);
  font-family: Courier;
}
#T_ae8ab_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.2%, transparent 18.2%);
  font-family: Courier;
}
#T_ae8ab_row3_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.6%, transparent 18.6%);
  font-family: Courier;
}
#T_ae8ab_row3_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.7%, transparent 41.7%);
  font-family: Courier;
}
#T_ae8ab_row3_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.5%, transparent 26.5%);
  font-family: Courier;
}
#T_ae8ab_row4_col8, #T_ae8ab_row6_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_ae8ab_row4_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_ae8ab_row5_col1, #T_ae8ab_row5_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 48.5%, transparent 48.5%);
  font-family: Courier;
}
#T_ae8ab_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.8%, transparent 11.8%);
  font-family: Courier;
}
#T_ae8ab_row5_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_ae8ab_row5_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 72.7%, transparent 72.7%);
  font-family: Courier;
}
#T_ae8ab_row5_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.2%, transparent 34.2%);
  font-family: Courier;
}
#T_ae8ab_row5_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.6%, transparent 38.6%);
  font-family: Courier;
}
#T_ae8ab_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.1%, transparent 12.1%);
  font-family: Courier;
}
#T_ae8ab_row6_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.1%, transparent 9.1%);
  font-family: Courier;
}
#T_ae8ab_row6_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_ae8ab_row6_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_ae8ab_row6_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_ae8ab_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.1%, transparent 47.1%);
  font-family: Courier;
}
#T_ae8ab_row7_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.2%, transparent 30.2%);
  font-family: Courier;
}
#T_ae8ab_row7_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.9%, transparent 28.9%);
  font-family: Courier;
}
#T_ae8ab_row7_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.0%, transparent 15.0%);
  font-family: Courier;
}
</style>
<table id="T_ae8ab">
  <thead>
    <tr>
      <th class="index_name level0" >[02.04] Affected body parts</th>
      <th id="T_ae8ab_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_ae8ab_level0_col1" class="col_heading level0 col1" >Abdomen</th>
      <th id="T_ae8ab_level0_col2" class="col_heading level0 col2" >Back</th>
      <th id="T_ae8ab_level0_col3" class="col_heading level0 col3" >Buttocks</th>
      <th id="T_ae8ab_level0_col4" class="col_heading level0 col4" >Chest</th>
      <th id="T_ae8ab_level0_col5" class="col_heading level0 col5" >Coccyx</th>
      <th id="T_ae8ab_level0_col6" class="col_heading level0 col6" >Full body</th>
      <th id="T_ae8ab_level0_col7" class="col_heading level0 col7" >Hals</th>
      <th id="T_ae8ab_level0_col8" class="col_heading level0 col8" >Head</th>
      <th id="T_ae8ab_level0_col9" class="col_heading level0 col9" >Innere Medizin</th>
      <th id="T_ae8ab_level0_col10" class="col_heading level0 col10" >Intestine</th>
      <th id="T_ae8ab_level0_col11" class="col_heading level0 col11" >Intimate area</th>
      <th id="T_ae8ab_level0_col12" class="col_heading level0 col12" >Lower extremities</th>
      <th id="T_ae8ab_level0_col13" class="col_heading level0 col13" >Upper extremities</th>
      <th id="T_ae8ab_level0_col14" class="col_heading level0 col14" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
      <th class="blank col12" >&nbsp;</th>
      <th class="blank col13" >&nbsp;</th>
      <th class="blank col14" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ae8ab_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_ae8ab_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row0_col2" class="data row0 col2" >1 <span style="color: grey">(6.2%) </span></td>
      <td id="T_ae8ab_row0_col3" class="data row0 col3" >7 <span style="color: grey">(41.2%) </span></td>
      <td id="T_ae8ab_row0_col4" class="data row0 col4" >1 <span style="color: grey">(10.0%) </span></td>
      <td id="T_ae8ab_row0_col5" class="data row0 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row0_col6" class="data row0 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row0_col7" class="data row0 col7" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row0_col8" class="data row0 col8" >7 <span style="color: grey">(16.3%) </span></td>
      <td id="T_ae8ab_row0_col9" class="data row0 col9" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_ae8ab_row0_col10" class="data row0 col10" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row0_col11" class="data row0 col11" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row0_col12" class="data row0 col12" >15 <span style="color: grey">(19.7%) </span></td>
      <td id="T_ae8ab_row0_col13" class="data row0 col13" >3 <span style="color: grey">(16.7%) </span></td>
      <td id="T_ae8ab_row0_col14" class="data row0 col14" >36 <span style="color: grey">(8.8%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_ae8ab_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col5" class="data row1 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col6" class="data row1 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col7" class="data row1 col7" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col8" class="data row1 col8" >2 <span style="color: grey">(4.7%) </span></td>
      <td id="T_ae8ab_row1_col9" class="data row1 col9" >4 <span style="color: grey">(2.5%) </span></td>
      <td id="T_ae8ab_row1_col10" class="data row1 col10" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col11" class="data row1 col11" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row1_col12" class="data row1 col12" >3 <span style="color: grey">(3.9%) </span></td>
      <td id="T_ae8ab_row1_col13" class="data row1 col13" >1 <span style="color: grey">(5.6%) </span></td>
      <td id="T_ae8ab_row1_col14" class="data row1 col14" >10 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_ae8ab_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col2" class="data row2 col2" >1 <span style="color: grey">(6.2%) </span></td>
      <td id="T_ae8ab_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col5" class="data row2 col5" >1 <span style="color: grey">(20.0%) </span></td>
      <td id="T_ae8ab_row2_col6" class="data row2 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col7" class="data row2 col7" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col8" class="data row2 col8" >4 <span style="color: grey">(9.3%) </span></td>
      <td id="T_ae8ab_row2_col9" class="data row2 col9" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col10" class="data row2 col10" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row2_col11" class="data row2 col11" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row2_col12" class="data row2 col12" >4 <span style="color: grey">(5.3%) </span></td>
      <td id="T_ae8ab_row2_col13" class="data row2 col13" >2 <span style="color: grey">(11.1%) </span></td>
      <td id="T_ae8ab_row2_col14" class="data row2 col14" >13 <span style="color: grey">(3.2%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_ae8ab_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row3_col1" class="data row3 col1" >13 <span style="color: grey">(39.4%) </span></td>
      <td id="T_ae8ab_row3_col2" class="data row3 col2" >3 <span style="color: grey">(18.8%) </span></td>
      <td id="T_ae8ab_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row3_col4" class="data row3 col4" >3 <span style="color: grey">(30.0%) </span></td>
      <td id="T_ae8ab_row3_col5" class="data row3 col5" >1 <span style="color: grey">(20.0%) </span></td>
      <td id="T_ae8ab_row3_col6" class="data row3 col6" >2 <span style="color: grey">(18.2%) </span></td>
      <td id="T_ae8ab_row3_col7" class="data row3 col7" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row3_col8" class="data row3 col8" >8 <span style="color: grey">(18.6%) </span></td>
      <td id="T_ae8ab_row3_col9" class="data row3 col9" >68 <span style="color: grey">(41.7%) </span></td>
      <td id="T_ae8ab_row3_col10" class="data row3 col10" >5 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row3_col11" class="data row3 col11" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row3_col12" class="data row3 col12" >4 <span style="color: grey">(5.3%) </span></td>
      <td id="T_ae8ab_row3_col13" class="data row3 col13" >1 <span style="color: grey">(5.6%) </span></td>
      <td id="T_ae8ab_row3_col14" class="data row3 col14" >108 <span style="color: grey">(26.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_ae8ab_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col5" class="data row4 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col6" class="data row4 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col7" class="data row4 col7" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col8" class="data row4 col8" >1 <span style="color: grey">(2.3%) </span></td>
      <td id="T_ae8ab_row4_col9" class="data row4 col9" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_ae8ab_row4_col10" class="data row4 col10" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col11" class="data row4 col11" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col12" class="data row4 col12" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col13" class="data row4 col13" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row4_col14" class="data row4 col14" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_ae8ab_row5_col0" class="data row5 col0" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row5_col1" class="data row5 col1" >16 <span style="color: grey">(48.5%) </span></td>
      <td id="T_ae8ab_row5_col2" class="data row5 col2" >8 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row5_col3" class="data row5 col3" >2 <span style="color: grey">(11.8%) </span></td>
      <td id="T_ae8ab_row5_col4" class="data row5 col4" >2 <span style="color: grey">(20.0%) </span></td>
      <td id="T_ae8ab_row5_col5" class="data row5 col5" >2 <span style="color: grey">(40.0%) </span></td>
      <td id="T_ae8ab_row5_col6" class="data row5 col6" >8 <span style="color: grey">(72.7%) </span></td>
      <td id="T_ae8ab_row5_col7" class="data row5 col7" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row5_col8" class="data row5 col8" >7 <span style="color: grey">(16.3%) </span></td>
      <td id="T_ae8ab_row5_col9" class="data row5 col9" >79 <span style="color: grey">(48.5%) </span></td>
      <td id="T_ae8ab_row5_col10" class="data row5 col10" >5 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row5_col11" class="data row5 col11" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row5_col12" class="data row5 col12" >26 <span style="color: grey">(34.2%) </span></td>
      <td id="T_ae8ab_row5_col13" class="data row5 col13" >1 <span style="color: grey">(5.6%) </span></td>
      <td id="T_ae8ab_row5_col14" class="data row5 col14" >157 <span style="color: grey">(38.6%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_ae8ab_row6_col0" class="data row6 col0" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row6_col1" class="data row6 col1" >4 <span style="color: grey">(12.1%) </span></td>
      <td id="T_ae8ab_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row6_col4" class="data row6 col4" >1 <span style="color: grey">(10.0%) </span></td>
      <td id="T_ae8ab_row6_col5" class="data row6 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row6_col6" class="data row6 col6" >1 <span style="color: grey">(9.1%) </span></td>
      <td id="T_ae8ab_row6_col7" class="data row6 col7" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row6_col8" class="data row6 col8" >1 <span style="color: grey">(2.3%) </span></td>
      <td id="T_ae8ab_row6_col9" class="data row6 col9" >9 <span style="color: grey">(5.5%) </span></td>
      <td id="T_ae8ab_row6_col10" class="data row6 col10" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row6_col11" class="data row6 col11" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row6_col12" class="data row6 col12" >2 <span style="color: grey">(2.6%) </span></td>
      <td id="T_ae8ab_row6_col13" class="data row6 col13" >1 <span style="color: grey">(5.6%) </span></td>
      <td id="T_ae8ab_row6_col14" class="data row6 col14" >20 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_ae8ab_row7_col0" class="data row7 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row7_col1" class="data row7 col1" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row7_col2" class="data row7 col2" >3 <span style="color: grey">(18.8%) </span></td>
      <td id="T_ae8ab_row7_col3" class="data row7 col3" >8 <span style="color: grey">(47.1%) </span></td>
      <td id="T_ae8ab_row7_col4" class="data row7 col4" >3 <span style="color: grey">(30.0%) </span></td>
      <td id="T_ae8ab_row7_col5" class="data row7 col5" >1 <span style="color: grey">(20.0%) </span></td>
      <td id="T_ae8ab_row7_col6" class="data row7 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row7_col7" class="data row7 col7" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row7_col8" class="data row7 col8" >13 <span style="color: grey">(30.2%) </span></td>
      <td id="T_ae8ab_row7_col9" class="data row7 col9" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_ae8ab_row7_col10" class="data row7 col10" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row7_col11" class="data row7 col11" ><span style="color: grey">0 </span></td>
      <td id="T_ae8ab_row7_col12" class="data row7 col12" >22 <span style="color: grey">(28.9%) </span></td>
      <td id="T_ae8ab_row7_col13" class="data row7 col13" >9 <span style="color: grey">(50.0%) </span></td>
      <td id="T_ae8ab_row7_col14" class="data row7 col14" >61 <span style="color: grey">(15.0%) </span></td>
    </tr>
    <tr>
      <th id="T_ae8ab_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_ae8ab_row8_col0" class="data row8 col0" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col1" class="data row8 col1" >33 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col2" class="data row8 col2" >16 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col3" class="data row8 col3" >17 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col4" class="data row8 col4" >10 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col5" class="data row8 col5" >5 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col6" class="data row8 col6" >11 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col7" class="data row8 col7" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col8" class="data row8 col8" >43 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col9" class="data row8 col9" >163 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col10" class="data row8 col10" >10 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col11" class="data row8 col11" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col12" class="data row8 col12" >76 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col13" class="data row8 col13" >18 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae8ab_row8_col14" class="data row8 col14" >407 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_5_'></a>[slide 5](#toc0_)


    
![svg](2_analyze_files/output_28_0.svg)
    



<style type="text/css">
#T_592d5 th {
  text-align: right;
}
#T_592d5 td {
  text-align: right;
}
#T_592d5_row0_col0, #T_592d5_row5_col0, #T_592d5_row5_col1, #T_592d5_row5_col2, #T_592d5_row5_col3, #T_592d5_row5_col4, #T_592d5_row5_col5, #T_592d5_row5_col6, #T_592d5_row5_col7, #T_592d5_row5_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_592d5_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.0%, transparent 19.0%);
  font-family: Courier;
}
#T_592d5_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.4%, transparent 22.4%);
  font-family: Courier;
}
#T_592d5_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.9%, transparent 26.9%);
  font-family: Courier;
}
#T_592d5_row0_col4, #T_592d5_row1_col4, #T_592d5_row1_col5, #T_592d5_row4_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_592d5_row0_col5, #T_592d5_row1_col0, #T_592d5_row2_col0, #T_592d5_row2_col5, #T_592d5_row2_col6, #T_592d5_row3_col0, #T_592d5_row4_col0, #T_592d5_row4_col2, #T_592d5_row4_col4, #T_592d5_row4_col7 {
  width: 10em;
  font-family: Courier;
}
#T_592d5_row0_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.2%, transparent 18.2%);
  font-family: Courier;
}
#T_592d5_row0_col7, #T_592d5_row2_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.3%, transparent 11.3%);
  font-family: Courier;
}
#T_592d5_row0_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.7%, transparent 22.7%);
  font-family: Courier;
}
#T_592d5_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.1%, transparent 24.1%);
  font-family: Courier;
}
#T_592d5_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.9%, transparent 14.9%);
  font-family: Courier;
}
#T_592d5_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_592d5_row1_col6, #T_592d5_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.4%, transparent 36.4%);
  font-family: Courier;
}
#T_592d5_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.6%, transparent 22.6%);
  font-family: Courier;
}
#T_592d5_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.9%, transparent 20.9%);
  font-family: Courier;
}
#T_592d5_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.1%, transparent 12.1%);
  font-family: Courier;
}
#T_592d5_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.9%, transparent 17.9%);
  font-family: Courier;
}
#T_592d5_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_592d5_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.9%, transparent 13.9%);
  font-family: Courier;
}
#T_592d5_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.3%, transparent 12.3%);
  font-family: Courier;
}
#T_592d5_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.2%, transparent 42.2%);
  font-family: Courier;
}
#T_592d5_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 44.8%, transparent 44.8%);
  font-family: Courier;
}
#T_592d5_row3_col3, #T_592d5_row3_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.3%, transparent 42.3%);
  font-family: Courier;
}
#T_592d5_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.1%, transparent 36.1%);
  font-family: Courier;
}
#T_592d5_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_592d5_row3_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 54.7%, transparent 54.7%);
  font-family: Courier;
}
#T_592d5_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_592d5_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_592d5_row4_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.1%, transparent 9.1%);
  font-family: Courier;
}
#T_592d5_row4_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
</style>
<table id="T_592d5">
  <thead>
    <tr>
      <th class="index_name level0" >[05.07] Main motor skill</th>
      <th id="T_592d5_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_592d5_level0_col1" class="col_heading level0 col1" >Coordination</th>
      <th id="T_592d5_level0_col2" class="col_heading level0 col2" >Endurance</th>
      <th id="T_592d5_level0_col3" class="col_heading level0 col3" >Flexibility</th>
      <th id="T_592d5_level0_col4" class="col_heading level0 col4" >Full body</th>
      <th id="T_592d5_level0_col5" class="col_heading level0 col5" >Relaxation</th>
      <th id="T_592d5_level0_col6" class="col_heading level0 col6" >Speed</th>
      <th id="T_592d5_level0_col7" class="col_heading level0 col7" >Strength</th>
      <th id="T_592d5_level0_col8" class="col_heading level0 col8" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.09] Training condition</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_592d5_level0_row0" class="row_heading level0 row0" ><NA></th>
      <td id="T_592d5_row0_col0" class="data row0 col0" >13 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row0_col1" class="data row0 col1" >22 <span style="color: grey">(19.0%) </span></td>
      <td id="T_592d5_row0_col2" class="data row0 col2" >15 <span style="color: grey">(22.4%) </span></td>
      <td id="T_592d5_row0_col3" class="data row0 col3" >7 <span style="color: grey">(26.9%) </span></td>
      <td id="T_592d5_row0_col4" class="data row0 col4" >9 <span style="color: grey">(25.0%) </span></td>
      <td id="T_592d5_row0_col5" class="data row0 col5" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row0_col6" class="data row0 col6" >2 <span style="color: grey">(18.2%) </span></td>
      <td id="T_592d5_row0_col7" class="data row0 col7" >6 <span style="color: grey">(11.3%) </span></td>
      <td id="T_592d5_row0_col8" class="data row0 col8" >74 <span style="color: grey">(22.7%) </span></td>
    </tr>
    <tr>
      <th id="T_592d5_level0_row1" class="row_heading level0 row1" >Average</th>
      <td id="T_592d5_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row1_col1" class="data row1 col1" >28 <span style="color: grey">(24.1%) </span></td>
      <td id="T_592d5_row1_col2" class="data row1 col2" >10 <span style="color: grey">(14.9%) </span></td>
      <td id="T_592d5_row1_col3" class="data row1 col3" >4 <span style="color: grey">(15.4%) </span></td>
      <td id="T_592d5_row1_col4" class="data row1 col4" >9 <span style="color: grey">(25.0%) </span></td>
      <td id="T_592d5_row1_col5" class="data row1 col5" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_592d5_row1_col6" class="data row1 col6" >4 <span style="color: grey">(36.4%) </span></td>
      <td id="T_592d5_row1_col7" class="data row1 col7" >12 <span style="color: grey">(22.6%) </span></td>
      <td id="T_592d5_row1_col8" class="data row1 col8" >68 <span style="color: grey">(20.9%) </span></td>
    </tr>
    <tr>
      <th id="T_592d5_level0_row2" class="row_heading level0 row2" >Good</th>
      <td id="T_592d5_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row2_col1" class="data row2 col1" >14 <span style="color: grey">(12.1%) </span></td>
      <td id="T_592d5_row2_col2" class="data row2 col2" >12 <span style="color: grey">(17.9%) </span></td>
      <td id="T_592d5_row2_col3" class="data row2 col3" >3 <span style="color: grey">(11.5%) </span></td>
      <td id="T_592d5_row2_col4" class="data row2 col4" >5 <span style="color: grey">(13.9%) </span></td>
      <td id="T_592d5_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row2_col6" class="data row2 col6" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row2_col7" class="data row2 col7" >6 <span style="color: grey">(11.3%) </span></td>
      <td id="T_592d5_row2_col8" class="data row2 col8" >40 <span style="color: grey">(12.3%) </span></td>
    </tr>
    <tr>
      <th id="T_592d5_level0_row3" class="row_heading level0 row3" >Moderate</th>
      <td id="T_592d5_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row3_col1" class="data row3 col1" >49 <span style="color: grey">(42.2%) </span></td>
      <td id="T_592d5_row3_col2" class="data row3 col2" >30 <span style="color: grey">(44.8%) </span></td>
      <td id="T_592d5_row3_col3" class="data row3 col3" >11 <span style="color: grey">(42.3%) </span></td>
      <td id="T_592d5_row3_col4" class="data row3 col4" >13 <span style="color: grey">(36.1%) </span></td>
      <td id="T_592d5_row3_col5" class="data row3 col5" >2 <span style="color: grey">(50.0%) </span></td>
      <td id="T_592d5_row3_col6" class="data row3 col6" >4 <span style="color: grey">(36.4%) </span></td>
      <td id="T_592d5_row3_col7" class="data row3 col7" >29 <span style="color: grey">(54.7%) </span></td>
      <td id="T_592d5_row3_col8" class="data row3 col8" >138 <span style="color: grey">(42.3%) </span></td>
    </tr>
    <tr>
      <th id="T_592d5_level0_row4" class="row_heading level0 row4" >Weiß nicht</th>
      <td id="T_592d5_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row4_col1" class="data row4 col1" >3 <span style="color: grey">(2.6%) </span></td>
      <td id="T_592d5_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row4_col3" class="data row4 col3" >1 <span style="color: grey">(3.8%) </span></td>
      <td id="T_592d5_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row4_col5" class="data row4 col5" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_592d5_row4_col6" class="data row4 col6" >1 <span style="color: grey">(9.1%) </span></td>
      <td id="T_592d5_row4_col7" class="data row4 col7" ><span style="color: grey">0 </span></td>
      <td id="T_592d5_row4_col8" class="data row4 col8" >6 <span style="color: grey">(1.8%) </span></td>
    </tr>
    <tr>
      <th id="T_592d5_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_592d5_row5_col0" class="data row5 col0" >13 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col1" class="data row5 col1" >116 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col2" class="data row5 col2" >67 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col3" class="data row5 col3" >26 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col4" class="data row5 col4" >36 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col5" class="data row5 col5" >4 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col6" class="data row5 col6" >11 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col7" class="data row5 col7" >53 <span style="color: grey">(100.0%) </span></td>
      <td id="T_592d5_row5_col8" class="data row5 col8" >326 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_6_'></a>[slide 6](#toc0_)


    
![svg](2_analyze_files/output_30_0.svg)
    



<style type="text/css">
#T_c0add th {
  text-align: right;
}
#T_c0add td {
  text-align: right;
}
#T_c0add_row0_col0, #T_c0add_row2_col0, #T_c0add_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_c0add_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_c0add_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_c0add_row0_col3, #T_c0add_row2_col3, #T_c0add_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_c0add_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_c0add_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.9%, transparent 5.9%);
  font-family: Courier;
}
#T_c0add_row0_col6, #T_c0add_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_c0add_row1_col1, #T_c0add_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_c0add_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_c0add_row1_col3, #T_c0add_row1_col4, #T_c0add_row2_col4, #T_c0add_row2_col5, #T_c0add_row4_col0, #T_c0add_row4_col2, #T_c0add_row4_col4, #T_c0add_row4_col5, #T_c0add_row6_col4 {
  width: 10em;
  font-family: Courier;
}
#T_c0add_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_c0add_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_c0add_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_c0add_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_c0add_row2_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_c0add_row3_col0, #T_c0add_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_c0add_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.5%, transparent 25.5%);
  font-family: Courier;
}
#T_c0add_row3_col2, #T_c0add_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.8%, transparent 27.8%);
  font-family: Courier;
}
#T_c0add_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.3%, transparent 37.3%);
  font-family: Courier;
}
#T_c0add_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_c0add_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.5%, transparent 26.5%);
  font-family: Courier;
}
#T_c0add_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.0%, transparent 27.0%);
  font-family: Courier;
}
#T_c0add_row4_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_c0add_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.9%, transparent 22.9%);
  font-family: Courier;
}
#T_c0add_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.5%, transparent 34.5%);
  font-family: Courier;
}
#T_c0add_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 45.6%, transparent 45.6%);
  font-family: Courier;
}
#T_c0add_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 49.0%, transparent 49.0%);
  font-family: Courier;
}
#T_c0add_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.9%, transparent 38.9%);
  font-family: Courier;
}
#T_c0add_row5_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.2%, transparent 41.2%);
  font-family: Courier;
}
#T_c0add_row5_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.0%, transparent 39.0%);
  font-family: Courier;
}
#T_c0add_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.5%, transparent 4.5%);
  font-family: Courier;
}
#T_c0add_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.9%, transparent 8.9%);
  font-family: Courier;
}
#T_c0add_row6_col3, #T_c0add_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.9%, transparent 3.9%);
  font-family: Courier;
}
#T_c0add_row6_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_c0add_row6_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_c0add_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.5%, transparent 15.5%);
  font-family: Courier;
}
#T_c0add_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_c0add_row7_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.6%, transparent 20.6%);
  font-family: Courier;
}
#T_c0add_row7_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_c0add_row8_col0, #T_c0add_row8_col1, #T_c0add_row8_col2, #T_c0add_row8_col3, #T_c0add_row8_col4, #T_c0add_row8_col5, #T_c0add_row8_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_c0add">
  <thead>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th id="T_c0add_level0_col0" class="col_heading level0 col0" >02 to 05 years</th>
      <th id="T_c0add_level0_col1" class="col_heading level0 col1" >06 to 09 years</th>
      <th id="T_c0add_level0_col2" class="col_heading level0 col2" >10 to 14 years</th>
      <th id="T_c0add_level0_col3" class="col_heading level0 col3" >15 to 18 years</th>
      <th id="T_c0add_level0_col4" class="col_heading level0 col4" >18+ years</th>
      <th id="T_c0add_level0_col5" class="col_heading level0 col5" ><NA></th>
      <th id="T_c0add_level0_col6" class="col_heading level0 col6" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c0add_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_c0add_row0_col0" class="data row0 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_c0add_row0_col1" class="data row0 col1" >14 <span style="color: grey">(12.7%) </span></td>
      <td id="T_c0add_row0_col2" class="data row0 col2" >6 <span style="color: grey">(6.7%) </span></td>
      <td id="T_c0add_row0_col3" class="data row0 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_c0add_row0_col4" class="data row0 col4" >4 <span style="color: grey">(22.2%) </span></td>
      <td id="T_c0add_row0_col5" class="data row0 col5" >4 <span style="color: grey">(5.9%) </span></td>
      <td id="T_c0add_row0_col6" class="data row0 col6" >32 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_c0add_row1_col0" class="data row1 col0" >4 <span style="color: grey">(8.3%) </span></td>
      <td id="T_c0add_row1_col1" class="data row1 col1" >1 <span style="color: grey">(0.9%) </span></td>
      <td id="T_c0add_row1_col2" class="data row1 col2" >2 <span style="color: grey">(2.2%) </span></td>
      <td id="T_c0add_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row1_col5" class="data row1 col5" >3 <span style="color: grey">(4.4%) </span></td>
      <td id="T_c0add_row1_col6" class="data row1 col6" >10 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_c0add_row2_col0" class="data row2 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_c0add_row2_col1" class="data row2 col1" >6 <span style="color: grey">(5.5%) </span></td>
      <td id="T_c0add_row2_col2" class="data row2 col2" >3 <span style="color: grey">(3.3%) </span></td>
      <td id="T_c0add_row2_col3" class="data row2 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_c0add_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row2_col6" class="data row2 col6" >13 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_c0add_row3_col0" class="data row3 col0" >12 <span style="color: grey">(25.0%) </span></td>
      <td id="T_c0add_row3_col1" class="data row3 col1" >28 <span style="color: grey">(25.5%) </span></td>
      <td id="T_c0add_row3_col2" class="data row3 col2" >25 <span style="color: grey">(27.8%) </span></td>
      <td id="T_c0add_row3_col3" class="data row3 col3" >19 <span style="color: grey">(37.3%) </span></td>
      <td id="T_c0add_row3_col4" class="data row3 col4" >2 <span style="color: grey">(11.1%) </span></td>
      <td id="T_c0add_row3_col5" class="data row3 col5" >18 <span style="color: grey">(26.5%) </span></td>
      <td id="T_c0add_row3_col6" class="data row3 col6" >104 <span style="color: grey">(27.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_c0add_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row4_col1" class="data row4 col1" >1 <span style="color: grey">(0.9%) </span></td>
      <td id="T_c0add_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row4_col3" class="data row4 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_c0add_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row4_col5" class="data row4 col5" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row4_col6" class="data row4 col6" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_c0add_row5_col0" class="data row5 col0" >11 <span style="color: grey">(22.9%) </span></td>
      <td id="T_c0add_row5_col1" class="data row5 col1" >38 <span style="color: grey">(34.5%) </span></td>
      <td id="T_c0add_row5_col2" class="data row5 col2" >41 <span style="color: grey">(45.6%) </span></td>
      <td id="T_c0add_row5_col3" class="data row5 col3" >25 <span style="color: grey">(49.0%) </span></td>
      <td id="T_c0add_row5_col4" class="data row5 col4" >7 <span style="color: grey">(38.9%) </span></td>
      <td id="T_c0add_row5_col5" class="data row5 col5" >28 <span style="color: grey">(41.2%) </span></td>
      <td id="T_c0add_row5_col6" class="data row5 col6" >150 <span style="color: grey">(39.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_c0add_row6_col0" class="data row6 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_c0add_row6_col1" class="data row6 col1" >5 <span style="color: grey">(4.5%) </span></td>
      <td id="T_c0add_row6_col2" class="data row6 col2" >8 <span style="color: grey">(8.9%) </span></td>
      <td id="T_c0add_row6_col3" class="data row6 col3" >2 <span style="color: grey">(3.9%) </span></td>
      <td id="T_c0add_row6_col4" class="data row6 col4" ><span style="color: grey">0 </span></td>
      <td id="T_c0add_row6_col5" class="data row6 col5" >1 <span style="color: grey">(1.5%) </span></td>
      <td id="T_c0add_row6_col6" class="data row6 col6" >19 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_c0add_row7_col0" class="data row7 col0" >12 <span style="color: grey">(25.0%) </span></td>
      <td id="T_c0add_row7_col1" class="data row7 col1" >17 <span style="color: grey">(15.5%) </span></td>
      <td id="T_c0add_row7_col2" class="data row7 col2" >5 <span style="color: grey">(5.6%) </span></td>
      <td id="T_c0add_row7_col3" class="data row7 col3" >2 <span style="color: grey">(3.9%) </span></td>
      <td id="T_c0add_row7_col4" class="data row7 col4" >5 <span style="color: grey">(27.8%) </span></td>
      <td id="T_c0add_row7_col5" class="data row7 col5" >14 <span style="color: grey">(20.6%) </span></td>
      <td id="T_c0add_row7_col6" class="data row7 col6" >55 <span style="color: grey">(14.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c0add_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_c0add_row8_col0" class="data row8 col0" >48 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c0add_row8_col1" class="data row8 col1" >110 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c0add_row8_col2" class="data row8 col2" >90 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c0add_row8_col3" class="data row8 col3" >51 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c0add_row8_col4" class="data row8 col4" >18 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c0add_row8_col5" class="data row8 col5" >68 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c0add_row8_col6" class="data row8 col6" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_7_'></a>[slide 7](#toc0_)


    
![svg](2_analyze_files/output_32_0.svg)
    



<style type="text/css">
#T_65fb6 th {
  text-align: right;
}
#T_65fb6 td {
  text-align: right;
}
#T_65fb6_row0_col0, #T_65fb6_row0_col1, #T_65fb6_row0_col2, #T_65fb6_row0_col5, #T_65fb6_row2_col0, #T_65fb6_row2_col3, #T_65fb6_row2_col4, #T_65fb6_row2_col5, #T_65fb6_row3_col1, #T_65fb6_row3_col3, #T_65fb6_row3_col4, #T_65fb6_row3_col5, #T_65fb6_row4_col2, #T_65fb6_row4_col4, #T_65fb6_row5_col0, #T_65fb6_row5_col1, #T_65fb6_row5_col4, #T_65fb6_row5_col5, #T_65fb6_row6_col0, #T_65fb6_row6_col4, #T_65fb6_row7_col0, #T_65fb6_row7_col2, #T_65fb6_row7_col4, #T_65fb6_row9_col4, #T_65fb6_row10_col3, #T_65fb6_row10_col4, #T_65fb6_row10_col5, #T_65fb6_row11_col0, #T_65fb6_row11_col3, #T_65fb6_row11_col4, #T_65fb6_row11_col5, #T_65fb6_row12_col3, #T_65fb6_row14_col4 {
  width: 10em;
  font-family: Courier;
}
#T_65fb6_row0_col3, #T_65fb6_row2_col1, #T_65fb6_row5_col3, #T_65fb6_row7_col3, #T_65fb6_row9_col3, #T_65fb6_row10_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_65fb6_row0_col4, #T_65fb6_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_65fb6_row0_col6, #T_65fb6_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_65fb6_row1_col0, #T_65fb6_row3_col0, #T_65fb6_row4_col0, #T_65fb6_row5_col2, #T_65fb6_row9_col0, #T_65fb6_row10_col0, #T_65fb6_row13_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_65fb6_row1_col1, #T_65fb6_row12_col1, #T_65fb6_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.2%, transparent 7.2%);
  font-family: Courier;
}
#T_65fb6_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_65fb6_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.1%, transparent 17.1%);
  font-family: Courier;
}
#T_65fb6_row1_col4, #T_65fb6_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_65fb6_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.5%, transparent 18.5%);
  font-family: Courier;
}
#T_65fb6_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_65fb6_row2_col2, #T_65fb6_row6_col2, #T_65fb6_row11_col2, #T_65fb6_row12_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_65fb6_row2_col6, #T_65fb6_row4_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_65fb6_row3_col2, #T_65fb6_row10_col2, #T_65fb6_row10_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_65fb6_row4_col1, #T_65fb6_row6_col1, #T_65fb6_row7_col1, #T_65fb6_row9_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_65fb6_row4_col3, #T_65fb6_row6_col3, #T_65fb6_row13_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_65fb6_row4_col5, #T_65fb6_row6_col5, #T_65fb6_row7_col5, #T_65fb6_row9_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_65fb6_row5_col6, #T_65fb6_row7_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_65fb6_row6_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_65fb6_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.6%, transparent 52.6%);
  font-family: Courier;
}
#T_65fb6_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 48.2%, transparent 48.2%);
  font-family: Courier;
}
#T_65fb6_row8_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.9%, transparent 35.9%);
  font-family: Courier;
}
#T_65fb6_row8_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.1%, transparent 34.1%);
  font-family: Courier;
}
#T_65fb6_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_65fb6_row8_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.6%, transparent 42.6%);
  font-family: Courier;
}
#T_65fb6_row8_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.2%, transparent 42.2%);
  font-family: Courier;
}
#T_65fb6_row9_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.0%, transparent 9.0%);
  font-family: Courier;
}
#T_65fb6_row9_col6, #T_65fb6_row11_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_65fb6_row11_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_65fb6_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.9%, transparent 7.9%);
  font-family: Courier;
}
#T_65fb6_row12_col5, #T_65fb6_row13_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.4%, transparent 7.4%);
  font-family: Courier;
}
#T_65fb6_row12_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_65fb6_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.1%, transparent 21.1%);
  font-family: Courier;
}
#T_65fb6_row13_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.2%, transparent 8.2%);
  font-family: Courier;
}
#T_65fb6_row14_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_65fb6_row14_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.9%, transparent 16.9%);
  font-family: Courier;
}
#T_65fb6_row14_col2, #T_65fb6_row14_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_65fb6_row14_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.4%, transparent 24.4%);
  font-family: Courier;
}
#T_65fb6_row14_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
#T_65fb6_row15_col0, #T_65fb6_row15_col1, #T_65fb6_row15_col2, #T_65fb6_row15_col3, #T_65fb6_row15_col4, #T_65fb6_row15_col5, #T_65fb6_row15_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_65fb6">
  <thead>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th id="T_65fb6_level0_col0" class="col_heading level0 col0" >02 to 05 years</th>
      <th id="T_65fb6_level0_col1" class="col_heading level0 col1" >06 to 09 years</th>
      <th id="T_65fb6_level0_col2" class="col_heading level0 col2" >10 to 14 years</th>
      <th id="T_65fb6_level0_col3" class="col_heading level0 col3" >15 to 18 years</th>
      <th id="T_65fb6_level0_col4" class="col_heading level0 col4" >18+ years</th>
      <th id="T_65fb6_level0_col5" class="col_heading level0 col5" ><NA></th>
      <th id="T_65fb6_level0_col6" class="col_heading level0 col6" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_65fb6_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_65fb6_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row0_col3" class="data row0 col3" >1 <span style="color: grey">(2.4%) </span></td>
      <td id="T_65fb6_row0_col4" class="data row0 col4" >1 <span style="color: grey">(8.3%) </span></td>
      <td id="T_65fb6_row0_col5" class="data row0 col5" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row0_col6" class="data row0 col6" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_65fb6_row1_col0" class="data row1 col0" >1 <span style="color: grey">(2.6%) </span></td>
      <td id="T_65fb6_row1_col1" class="data row1 col1" >6 <span style="color: grey">(7.2%) </span></td>
      <td id="T_65fb6_row1_col2" class="data row1 col2" >12 <span style="color: grey">(15.4%) </span></td>
      <td id="T_65fb6_row1_col3" class="data row1 col3" >7 <span style="color: grey">(17.1%) </span></td>
      <td id="T_65fb6_row1_col4" class="data row1 col4" >3 <span style="color: grey">(25.0%) </span></td>
      <td id="T_65fb6_row1_col5" class="data row1 col5" >10 <span style="color: grey">(18.5%) </span></td>
      <td id="T_65fb6_row1_col6" class="data row1 col6" >39 <span style="color: grey">(12.7%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_65fb6_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row2_col1" class="data row2 col1" >2 <span style="color: grey">(2.4%) </span></td>
      <td id="T_65fb6_row2_col2" class="data row2 col2" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_65fb6_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row2_col6" class="data row2 col6" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_65fb6_row3_col0" class="data row3 col0" >1 <span style="color: grey">(2.6%) </span></td>
      <td id="T_65fb6_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row3_col2" class="data row3 col2" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_65fb6_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row3_col4" class="data row3 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row3_col5" class="data row3 col5" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row3_col6" class="data row3 col6" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_65fb6_row4_col0" class="data row4 col0" >1 <span style="color: grey">(2.6%) </span></td>
      <td id="T_65fb6_row4_col1" class="data row4 col1" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_65fb6_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row4_col3" class="data row4 col3" >2 <span style="color: grey">(4.9%) </span></td>
      <td id="T_65fb6_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row4_col5" class="data row4 col5" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_65fb6_row4_col6" class="data row4 col6" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_65fb6_row5_col0" class="data row5 col0" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row5_col2" class="data row5 col2" >2 <span style="color: grey">(2.6%) </span></td>
      <td id="T_65fb6_row5_col3" class="data row5 col3" >1 <span style="color: grey">(2.4%) </span></td>
      <td id="T_65fb6_row5_col4" class="data row5 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row5_col5" class="data row5 col5" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row5_col6" class="data row5 col6" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_65fb6_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row6_col1" class="data row6 col1" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_65fb6_row6_col2" class="data row6 col2" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_65fb6_row6_col3" class="data row6 col3" >2 <span style="color: grey">(4.9%) </span></td>
      <td id="T_65fb6_row6_col4" class="data row6 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row6_col5" class="data row6 col5" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_65fb6_row6_col6" class="data row6 col6" >7 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_65fb6_row7_col0" class="data row7 col0" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row7_col1" class="data row7 col1" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_65fb6_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row7_col3" class="data row7 col3" >1 <span style="color: grey">(2.4%) </span></td>
      <td id="T_65fb6_row7_col4" class="data row7 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row7_col5" class="data row7 col5" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_65fb6_row7_col6" class="data row7 col6" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_65fb6_row8_col0" class="data row8 col0" >20 <span style="color: grey">(52.6%) </span></td>
      <td id="T_65fb6_row8_col1" class="data row8 col1" >40 <span style="color: grey">(48.2%) </span></td>
      <td id="T_65fb6_row8_col2" class="data row8 col2" >28 <span style="color: grey">(35.9%) </span></td>
      <td id="T_65fb6_row8_col3" class="data row8 col3" >14 <span style="color: grey">(34.1%) </span></td>
      <td id="T_65fb6_row8_col4" class="data row8 col4" >4 <span style="color: grey">(33.3%) </span></td>
      <td id="T_65fb6_row8_col5" class="data row8 col5" >23 <span style="color: grey">(42.6%) </span></td>
      <td id="T_65fb6_row8_col6" class="data row8 col6" >129 <span style="color: grey">(42.2%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_65fb6_row9_col0" class="data row9 col0" >1 <span style="color: grey">(2.6%) </span></td>
      <td id="T_65fb6_row9_col1" class="data row9 col1" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_65fb6_row9_col2" class="data row9 col2" >7 <span style="color: grey">(9.0%) </span></td>
      <td id="T_65fb6_row9_col3" class="data row9 col3" >1 <span style="color: grey">(2.4%) </span></td>
      <td id="T_65fb6_row9_col4" class="data row9 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row9_col5" class="data row9 col5" >1 <span style="color: grey">(1.9%) </span></td>
      <td id="T_65fb6_row9_col6" class="data row9 col6" >11 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_65fb6_row10_col0" class="data row10 col0" >1 <span style="color: grey">(2.6%) </span></td>
      <td id="T_65fb6_row10_col1" class="data row10 col1" >2 <span style="color: grey">(2.4%) </span></td>
      <td id="T_65fb6_row10_col2" class="data row10 col2" >1 <span style="color: grey">(1.3%) </span></td>
      <td id="T_65fb6_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row10_col4" class="data row10 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row10_col5" class="data row10 col5" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row10_col6" class="data row10 col6" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_65fb6_row11_col0" class="data row11 col0" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row11_col1" class="data row11 col1" >3 <span style="color: grey">(3.6%) </span></td>
      <td id="T_65fb6_row11_col2" class="data row11 col2" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_65fb6_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row11_col4" class="data row11 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row11_col5" class="data row11 col5" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row11_col6" class="data row11 col6" >6 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_65fb6_row12_col0" class="data row12 col0" >3 <span style="color: grey">(7.9%) </span></td>
      <td id="T_65fb6_row12_col1" class="data row12 col1" >6 <span style="color: grey">(7.2%) </span></td>
      <td id="T_65fb6_row12_col2" class="data row12 col2" >3 <span style="color: grey">(3.8%) </span></td>
      <td id="T_65fb6_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row12_col4" class="data row12 col4" >1 <span style="color: grey">(8.3%) </span></td>
      <td id="T_65fb6_row12_col5" class="data row12 col5" >4 <span style="color: grey">(7.4%) </span></td>
      <td id="T_65fb6_row12_col6" class="data row12 col6" >17 <span style="color: grey">(5.6%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_65fb6_row13_col0" class="data row13 col0" >8 <span style="color: grey">(21.1%) </span></td>
      <td id="T_65fb6_row13_col1" class="data row13 col1" >6 <span style="color: grey">(7.2%) </span></td>
      <td id="T_65fb6_row13_col2" class="data row13 col2" >2 <span style="color: grey">(2.6%) </span></td>
      <td id="T_65fb6_row13_col3" class="data row13 col3" >2 <span style="color: grey">(4.9%) </span></td>
      <td id="T_65fb6_row13_col4" class="data row13 col4" >3 <span style="color: grey">(25.0%) </span></td>
      <td id="T_65fb6_row13_col5" class="data row13 col5" >4 <span style="color: grey">(7.4%) </span></td>
      <td id="T_65fb6_row13_col6" class="data row13 col6" >25 <span style="color: grey">(8.2%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_65fb6_row14_col0" class="data row14 col0" >2 <span style="color: grey">(5.3%) </span></td>
      <td id="T_65fb6_row14_col1" class="data row14 col1" >14 <span style="color: grey">(16.9%) </span></td>
      <td id="T_65fb6_row14_col2" class="data row14 col2" >13 <span style="color: grey">(16.7%) </span></td>
      <td id="T_65fb6_row14_col3" class="data row14 col3" >10 <span style="color: grey">(24.4%) </span></td>
      <td id="T_65fb6_row14_col4" class="data row14 col4" ><span style="color: grey">0 </span></td>
      <td id="T_65fb6_row14_col5" class="data row14 col5" >9 <span style="color: grey">(16.7%) </span></td>
      <td id="T_65fb6_row14_col6" class="data row14 col6" >48 <span style="color: grey">(15.7%) </span></td>
    </tr>
    <tr>
      <th id="T_65fb6_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_65fb6_row15_col0" class="data row15 col0" >38 <span style="color: grey">(100.0%) </span></td>
      <td id="T_65fb6_row15_col1" class="data row15 col1" >83 <span style="color: grey">(100.0%) </span></td>
      <td id="T_65fb6_row15_col2" class="data row15 col2" >78 <span style="color: grey">(100.0%) </span></td>
      <td id="T_65fb6_row15_col3" class="data row15 col3" >41 <span style="color: grey">(100.0%) </span></td>
      <td id="T_65fb6_row15_col4" class="data row15 col4" >12 <span style="color: grey">(100.0%) </span></td>
      <td id="T_65fb6_row15_col5" class="data row15 col5" >54 <span style="color: grey">(100.0%) </span></td>
      <td id="T_65fb6_row15_col6" class="data row15 col6" >306 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_8_'></a>[slide 8](#toc0_)


    
![svg](2_analyze_files/output_34_0.svg)
    



<style type="text/css">
#T_ae82e th {
  text-align: right;
}
#T_ae82e td {
  text-align: right;
}
#T_ae82e_row0_col0, #T_ae82e_row2_col0, #T_ae82e_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_ae82e_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_ae82e_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_ae82e_row0_col3, #T_ae82e_row2_col3, #T_ae82e_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_ae82e_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_ae82e_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.9%, transparent 5.9%);
  font-family: Courier;
}
#T_ae82e_row0_col6, #T_ae82e_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_ae82e_row1_col1, #T_ae82e_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_ae82e_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_ae82e_row1_col3, #T_ae82e_row1_col4, #T_ae82e_row2_col4, #T_ae82e_row2_col5, #T_ae82e_row4_col0, #T_ae82e_row4_col2, #T_ae82e_row4_col4, #T_ae82e_row4_col5, #T_ae82e_row6_col4 {
  width: 10em;
  font-family: Courier;
}
#T_ae82e_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_ae82e_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_ae82e_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_ae82e_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_ae82e_row2_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_ae82e_row3_col0, #T_ae82e_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_ae82e_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.5%, transparent 25.5%);
  font-family: Courier;
}
#T_ae82e_row3_col2, #T_ae82e_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.8%, transparent 27.8%);
  font-family: Courier;
}
#T_ae82e_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.3%, transparent 37.3%);
  font-family: Courier;
}
#T_ae82e_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_ae82e_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.5%, transparent 26.5%);
  font-family: Courier;
}
#T_ae82e_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.0%, transparent 27.0%);
  font-family: Courier;
}
#T_ae82e_row4_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_ae82e_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.9%, transparent 22.9%);
  font-family: Courier;
}
#T_ae82e_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.5%, transparent 34.5%);
  font-family: Courier;
}
#T_ae82e_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 45.6%, transparent 45.6%);
  font-family: Courier;
}
#T_ae82e_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 49.0%, transparent 49.0%);
  font-family: Courier;
}
#T_ae82e_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.9%, transparent 38.9%);
  font-family: Courier;
}
#T_ae82e_row5_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.2%, transparent 41.2%);
  font-family: Courier;
}
#T_ae82e_row5_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.0%, transparent 39.0%);
  font-family: Courier;
}
#T_ae82e_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.5%, transparent 4.5%);
  font-family: Courier;
}
#T_ae82e_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.9%, transparent 8.9%);
  font-family: Courier;
}
#T_ae82e_row6_col3, #T_ae82e_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.9%, transparent 3.9%);
  font-family: Courier;
}
#T_ae82e_row6_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_ae82e_row6_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_ae82e_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.5%, transparent 15.5%);
  font-family: Courier;
}
#T_ae82e_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_ae82e_row7_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.6%, transparent 20.6%);
  font-family: Courier;
}
#T_ae82e_row7_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_ae82e_row8_col0, #T_ae82e_row8_col1, #T_ae82e_row8_col2, #T_ae82e_row8_col3, #T_ae82e_row8_col4, #T_ae82e_row8_col5, #T_ae82e_row8_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_ae82e">
  <thead>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th id="T_ae82e_level0_col0" class="col_heading level0 col0" >02 to 05 years</th>
      <th id="T_ae82e_level0_col1" class="col_heading level0 col1" >06 to 09 years</th>
      <th id="T_ae82e_level0_col2" class="col_heading level0 col2" >10 to 14 years</th>
      <th id="T_ae82e_level0_col3" class="col_heading level0 col3" >15 to 18 years</th>
      <th id="T_ae82e_level0_col4" class="col_heading level0 col4" >18+ years</th>
      <th id="T_ae82e_level0_col5" class="col_heading level0 col5" ><NA></th>
      <th id="T_ae82e_level0_col6" class="col_heading level0 col6" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ae82e_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_ae82e_row0_col0" class="data row0 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_ae82e_row0_col1" class="data row0 col1" >14 <span style="color: grey">(12.7%) </span></td>
      <td id="T_ae82e_row0_col2" class="data row0 col2" >6 <span style="color: grey">(6.7%) </span></td>
      <td id="T_ae82e_row0_col3" class="data row0 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_ae82e_row0_col4" class="data row0 col4" >4 <span style="color: grey">(22.2%) </span></td>
      <td id="T_ae82e_row0_col5" class="data row0 col5" >4 <span style="color: grey">(5.9%) </span></td>
      <td id="T_ae82e_row0_col6" class="data row0 col6" >32 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_ae82e_row1_col0" class="data row1 col0" >4 <span style="color: grey">(8.3%) </span></td>
      <td id="T_ae82e_row1_col1" class="data row1 col1" >1 <span style="color: grey">(0.9%) </span></td>
      <td id="T_ae82e_row1_col2" class="data row1 col2" >2 <span style="color: grey">(2.2%) </span></td>
      <td id="T_ae82e_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row1_col5" class="data row1 col5" >3 <span style="color: grey">(4.4%) </span></td>
      <td id="T_ae82e_row1_col6" class="data row1 col6" >10 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_ae82e_row2_col0" class="data row2 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_ae82e_row2_col1" class="data row2 col1" >6 <span style="color: grey">(5.5%) </span></td>
      <td id="T_ae82e_row2_col2" class="data row2 col2" >3 <span style="color: grey">(3.3%) </span></td>
      <td id="T_ae82e_row2_col3" class="data row2 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_ae82e_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row2_col6" class="data row2 col6" >13 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_ae82e_row3_col0" class="data row3 col0" >12 <span style="color: grey">(25.0%) </span></td>
      <td id="T_ae82e_row3_col1" class="data row3 col1" >28 <span style="color: grey">(25.5%) </span></td>
      <td id="T_ae82e_row3_col2" class="data row3 col2" >25 <span style="color: grey">(27.8%) </span></td>
      <td id="T_ae82e_row3_col3" class="data row3 col3" >19 <span style="color: grey">(37.3%) </span></td>
      <td id="T_ae82e_row3_col4" class="data row3 col4" >2 <span style="color: grey">(11.1%) </span></td>
      <td id="T_ae82e_row3_col5" class="data row3 col5" >18 <span style="color: grey">(26.5%) </span></td>
      <td id="T_ae82e_row3_col6" class="data row3 col6" >104 <span style="color: grey">(27.0%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_ae82e_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row4_col1" class="data row4 col1" >1 <span style="color: grey">(0.9%) </span></td>
      <td id="T_ae82e_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row4_col3" class="data row4 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_ae82e_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row4_col5" class="data row4 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row4_col6" class="data row4 col6" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_ae82e_row5_col0" class="data row5 col0" >11 <span style="color: grey">(22.9%) </span></td>
      <td id="T_ae82e_row5_col1" class="data row5 col1" >38 <span style="color: grey">(34.5%) </span></td>
      <td id="T_ae82e_row5_col2" class="data row5 col2" >41 <span style="color: grey">(45.6%) </span></td>
      <td id="T_ae82e_row5_col3" class="data row5 col3" >25 <span style="color: grey">(49.0%) </span></td>
      <td id="T_ae82e_row5_col4" class="data row5 col4" >7 <span style="color: grey">(38.9%) </span></td>
      <td id="T_ae82e_row5_col5" class="data row5 col5" >28 <span style="color: grey">(41.2%) </span></td>
      <td id="T_ae82e_row5_col6" class="data row5 col6" >150 <span style="color: grey">(39.0%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_ae82e_row6_col0" class="data row6 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_ae82e_row6_col1" class="data row6 col1" >5 <span style="color: grey">(4.5%) </span></td>
      <td id="T_ae82e_row6_col2" class="data row6 col2" >8 <span style="color: grey">(8.9%) </span></td>
      <td id="T_ae82e_row6_col3" class="data row6 col3" >2 <span style="color: grey">(3.9%) </span></td>
      <td id="T_ae82e_row6_col4" class="data row6 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ae82e_row6_col5" class="data row6 col5" >1 <span style="color: grey">(1.5%) </span></td>
      <td id="T_ae82e_row6_col6" class="data row6 col6" >19 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_ae82e_row7_col0" class="data row7 col0" >12 <span style="color: grey">(25.0%) </span></td>
      <td id="T_ae82e_row7_col1" class="data row7 col1" >17 <span style="color: grey">(15.5%) </span></td>
      <td id="T_ae82e_row7_col2" class="data row7 col2" >5 <span style="color: grey">(5.6%) </span></td>
      <td id="T_ae82e_row7_col3" class="data row7 col3" >2 <span style="color: grey">(3.9%) </span></td>
      <td id="T_ae82e_row7_col4" class="data row7 col4" >5 <span style="color: grey">(27.8%) </span></td>
      <td id="T_ae82e_row7_col5" class="data row7 col5" >14 <span style="color: grey">(20.6%) </span></td>
      <td id="T_ae82e_row7_col6" class="data row7 col6" >55 <span style="color: grey">(14.3%) </span></td>
    </tr>
    <tr>
      <th id="T_ae82e_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_ae82e_row8_col0" class="data row8 col0" >48 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae82e_row8_col1" class="data row8 col1" >110 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae82e_row8_col2" class="data row8 col2" >90 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae82e_row8_col3" class="data row8 col3" >51 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae82e_row8_col4" class="data row8 col4" >18 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae82e_row8_col5" class="data row8 col5" >68 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ae82e_row8_col6" class="data row8 col6" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_9_'></a>[slide 9](#toc0_)


    
![svg](2_analyze_files/output_36_0.svg)
    



<style type="text/css">
#T_1d4e6 th {
  text-align: right;
}
#T_1d4e6 td {
  text-align: right;
}
#T_1d4e6_row0_col0, #T_1d4e6_row0_col2, #T_1d4e6_row0_col3, #T_1d4e6_row2_col1, #T_1d4e6_row2_col2, #T_1d4e6_row2_col3, #T_1d4e6_row3_col1, #T_1d4e6_row3_col2, #T_1d4e6_row3_col3, #T_1d4e6_row4_col2, #T_1d4e6_row4_col3, #T_1d4e6_row5_col1, #T_1d4e6_row5_col2, #T_1d4e6_row5_col3, #T_1d4e6_row6_col1, #T_1d4e6_row6_col3, #T_1d4e6_row7_col1, #T_1d4e6_row7_col2, #T_1d4e6_row7_col3, #T_1d4e6_row8_col3, #T_1d4e6_row9_col2, #T_1d4e6_row9_col3, #T_1d4e6_row10_col1, #T_1d4e6_row10_col2, #T_1d4e6_row10_col3, #T_1d4e6_row11_col1, #T_1d4e6_row11_col2, #T_1d4e6_row11_col3, #T_1d4e6_row12_col2, #T_1d4e6_row12_col3, #T_1d4e6_row13_col3, #T_1d4e6_row14_col1, #T_1d4e6_row14_col3 {
  width: 10em;
  font-family: Courier;
}
#T_1d4e6_row0_col1, #T_1d4e6_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_1d4e6_row0_col4, #T_1d4e6_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_1d4e6_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
#T_1d4e6_row1_col2, #T_1d4e6_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_1d4e6_row1_col3, #T_1d4e6_row15_col0, #T_1d4e6_row15_col1, #T_1d4e6_row15_col2, #T_1d4e6_row15_col3, #T_1d4e6_row15_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_1d4e6_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_1d4e6_row2_col0, #T_1d4e6_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_1d4e6_row2_col4, #T_1d4e6_row4_col0, #T_1d4e6_row4_col4, #T_1d4e6_row10_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_1d4e6_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_1d4e6_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_1d4e6_row5_col0, #T_1d4e6_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_1d4e6_row5_col4, #T_1d4e6_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_1d4e6_row6_col0, #T_1d4e6_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_1d4e6_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_1d4e6_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.0%, transparent 42.0%);
  font-family: Courier;
}
#T_1d4e6_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 45.7%, transparent 45.7%);
  font-family: Courier;
}
#T_1d4e6_row8_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_1d4e6_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.2%, transparent 42.2%);
  font-family: Courier;
}
#T_1d4e6_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.2%, transparent 3.2%);
  font-family: Courier;
}
#T_1d4e6_row9_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.5%, transparent 6.5%);
  font-family: Courier;
}
#T_1d4e6_row9_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_1d4e6_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_1d4e6_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_1d4e6_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.9%, transparent 10.9%);
  font-family: Courier;
}
#T_1d4e6_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_1d4e6_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_1d4e6_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.1%, transparent 26.1%);
  font-family: Courier;
}
#T_1d4e6_row13_col2, #T_1d4e6_row14_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_1d4e6_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.2%, transparent 8.2%);
  font-family: Courier;
}
#T_1d4e6_row14_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.4%, transparent 18.4%);
  font-family: Courier;
}
#T_1d4e6_row14_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
</style>
<table id="T_1d4e6">
  <thead>
    <tr>
      <th class="index_name level0" >[05.01] Therapy phase</th>
      <th id="T_1d4e6_level0_col0" class="col_heading level0 col0" >Acute therapy</th>
      <th id="T_1d4e6_level0_col1" class="col_heading level0 col1" >Aftercare</th>
      <th id="T_1d4e6_level0_col2" class="col_heading level0 col2" >Long-term therapy</th>
      <th id="T_1d4e6_level0_col3" class="col_heading level0 col3" >Weiß nicht</th>
      <th id="T_1d4e6_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_1d4e6_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_1d4e6_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row0_col1" class="data row0 col1" >2 <span style="color: grey">(4.3%) </span></td>
      <td id="T_1d4e6_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row0_col4" class="data row0 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_1d4e6_row1_col0" class="data row1 col0" >35 <span style="color: grey">(14.0%) </span></td>
      <td id="T_1d4e6_row1_col1" class="data row1 col1" >2 <span style="color: grey">(4.3%) </span></td>
      <td id="T_1d4e6_row1_col2" class="data row1 col2" >1 <span style="color: grey">(11.1%) </span></td>
      <td id="T_1d4e6_row1_col3" class="data row1 col3" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_1d4e6_row1_col4" class="data row1 col4" >39 <span style="color: grey">(12.7%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_1d4e6_row2_col0" class="data row2 col0" >5 <span style="color: grey">(2.0%) </span></td>
      <td id="T_1d4e6_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row2_col4" class="data row2 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_1d4e6_row3_col0" class="data row3 col0" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_1d4e6_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row3_col4" class="data row3 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_1d4e6_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_1d4e6_row4_col1" class="data row4 col1" >1 <span style="color: grey">(2.2%) </span></td>
      <td id="T_1d4e6_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row4_col4" class="data row4 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_1d4e6_row5_col0" class="data row5 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_1d4e6_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row5_col4" class="data row5 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_1d4e6_row6_col0" class="data row6 col0" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_1d4e6_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row6_col2" class="data row6 col2" >1 <span style="color: grey">(11.1%) </span></td>
      <td id="T_1d4e6_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row6_col4" class="data row6 col4" >7 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_1d4e6_row7_col0" class="data row7 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_1d4e6_row7_col1" class="data row7 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row7_col4" class="data row7 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_1d4e6_row8_col0" class="data row8 col0" >105 <span style="color: grey">(42.0%) </span></td>
      <td id="T_1d4e6_row8_col1" class="data row8 col1" >21 <span style="color: grey">(45.7%) </span></td>
      <td id="T_1d4e6_row8_col2" class="data row8 col2" >3 <span style="color: grey">(33.3%) </span></td>
      <td id="T_1d4e6_row8_col3" class="data row8 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row8_col4" class="data row8 col4" >129 <span style="color: grey">(42.2%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_1d4e6_row9_col0" class="data row9 col0" >8 <span style="color: grey">(3.2%) </span></td>
      <td id="T_1d4e6_row9_col1" class="data row9 col1" >3 <span style="color: grey">(6.5%) </span></td>
      <td id="T_1d4e6_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row9_col4" class="data row9 col4" >11 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_1d4e6_row10_col0" class="data row10 col0" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_1d4e6_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row10_col4" class="data row10 col4" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_1d4e6_row11_col0" class="data row11 col0" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_1d4e6_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row11_col4" class="data row11 col4" >6 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_1d4e6_row12_col0" class="data row12 col0" >12 <span style="color: grey">(4.8%) </span></td>
      <td id="T_1d4e6_row12_col1" class="data row12 col1" >5 <span style="color: grey">(10.9%) </span></td>
      <td id="T_1d4e6_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row12_col4" class="data row12 col4" >17 <span style="color: grey">(5.6%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_1d4e6_row13_col0" class="data row13 col0" >11 <span style="color: grey">(4.4%) </span></td>
      <td id="T_1d4e6_row13_col1" class="data row13 col1" >12 <span style="color: grey">(26.1%) </span></td>
      <td id="T_1d4e6_row13_col2" class="data row13 col2" >2 <span style="color: grey">(22.2%) </span></td>
      <td id="T_1d4e6_row13_col3" class="data row13 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row13_col4" class="data row13 col4" >25 <span style="color: grey">(8.2%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_1d4e6_row14_col0" class="data row14 col0" >46 <span style="color: grey">(18.4%) </span></td>
      <td id="T_1d4e6_row14_col1" class="data row14 col1" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row14_col2" class="data row14 col2" >2 <span style="color: grey">(22.2%) </span></td>
      <td id="T_1d4e6_row14_col3" class="data row14 col3" ><span style="color: grey">0 </span></td>
      <td id="T_1d4e6_row14_col4" class="data row14 col4" >48 <span style="color: grey">(15.7%) </span></td>
    </tr>
    <tr>
      <th id="T_1d4e6_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_1d4e6_row15_col0" class="data row15 col0" >250 <span style="color: grey">(100.0%) </span></td>
      <td id="T_1d4e6_row15_col1" class="data row15 col1" >46 <span style="color: grey">(100.0%) </span></td>
      <td id="T_1d4e6_row15_col2" class="data row15 col2" >9 <span style="color: grey">(100.0%) </span></td>
      <td id="T_1d4e6_row15_col3" class="data row15 col3" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_1d4e6_row15_col4" class="data row15 col4" >306 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_10_'></a>[slide 10](#toc0_)


    
![svg](2_analyze_files/output_38_0.svg)
    



<style type="text/css">
#T_be241 th {
  text-align: right;
}
#T_be241 td {
  text-align: right;
}
#T_be241_row0_col0, #T_be241_row8_col0, #T_be241_row8_col1, #T_be241_row8_col2, #T_be241_row8_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_be241_row0_col1, #T_be241_row1_col0, #T_be241_row2_col0, #T_be241_row3_col0, #T_be241_row4_col0, #T_be241_row5_col0, #T_be241_row5_col1, #T_be241_row6_col0, #T_be241_row6_col1, #T_be241_row7_col0 {
  width: 10em;
  font-family: Courier;
}
#T_be241_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.2%, transparent 4.2%);
  font-family: Courier;
}
#T_be241_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_be241_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.8%, transparent 36.8%);
  font-family: Courier;
}
#T_be241_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.4%, transparent 35.4%);
  font-family: Courier;
}
#T_be241_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.5%, transparent 35.5%);
  font-family: Courier;
}
#T_be241_row2_col1, #T_be241_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.7%, transparent 23.7%);
  font-family: Courier;
}
#T_be241_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_be241_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.4%, transparent 20.4%);
  font-family: Courier;
}
#T_be241_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.0%, transparent 6.0%);
  font-family: Courier;
}
#T_be241_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.0%, transparent 8.0%);
  font-family: Courier;
}
#T_be241_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_be241_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.9%, transparent 11.9%);
  font-family: Courier;
}
#T_be241_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_be241_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.4%, transparent 1.4%);
  font-family: Courier;
}
#T_be241_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_be241_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.9%, transparent 3.9%);
  font-family: Courier;
}
#T_be241_row6_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_be241_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.5%, transparent 10.5%);
  font-family: Courier;
}
#T_be241_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.2%, transparent 17.2%);
  font-family: Courier;
}
#T_be241_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.4%, transparent 16.4%);
  font-family: Courier;
}
</style>
<table id="T_be241">
  <thead>
    <tr>
      <th class="index_name level0" >[01.03] Exercise-related</th>
      <th id="T_be241_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_be241_level0_col1" class="col_heading level0 col1" >No</th>
      <th id="T_be241_level0_col2" class="col_heading level0 col2" >Yes</th>
      <th id="T_be241_level0_col3" class="col_heading level0 col3" >Total</th>
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
      <th id="T_be241_level0_row0" class="row_heading level0 row0" ><NA></th>
      <td id="T_be241_row0_col0" class="data row0 col0" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_be241_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row0_col2" class="data row0 col2" >12 <span style="color: grey">(4.2%) </span></td>
      <td id="T_be241_row0_col3" class="data row0 col3" >13 <span style="color: grey">(4.0%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row1" class="row_heading level0 row1" >Coordination</th>
      <td id="T_be241_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row1_col1" class="data row1 col1" >14 <span style="color: grey">(36.8%) </span></td>
      <td id="T_be241_row1_col2" class="data row1 col2" >101 <span style="color: grey">(35.4%) </span></td>
      <td id="T_be241_row1_col3" class="data row1 col3" >115 <span style="color: grey">(35.5%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row2" class="row_heading level0 row2" >Endurance</th>
      <td id="T_be241_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row2_col1" class="data row2 col1" >9 <span style="color: grey">(23.7%) </span></td>
      <td id="T_be241_row2_col2" class="data row2 col2" >57 <span style="color: grey">(20.0%) </span></td>
      <td id="T_be241_row2_col3" class="data row2 col3" >66 <span style="color: grey">(20.4%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row3" class="row_heading level0 row3" >Flexibility</th>
      <td id="T_be241_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row3_col1" class="data row3 col1" >9 <span style="color: grey">(23.7%) </span></td>
      <td id="T_be241_row3_col2" class="data row3 col2" >17 <span style="color: grey">(6.0%) </span></td>
      <td id="T_be241_row3_col3" class="data row3 col3" >26 <span style="color: grey">(8.0%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row4" class="row_heading level0 row4" >Full body</th>
      <td id="T_be241_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row4_col1" class="data row4 col1" >2 <span style="color: grey">(5.3%) </span></td>
      <td id="T_be241_row4_col2" class="data row4 col2" >34 <span style="color: grey">(11.9%) </span></td>
      <td id="T_be241_row4_col3" class="data row4 col3" >36 <span style="color: grey">(11.1%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row5" class="row_heading level0 row5" >Relaxation</th>
      <td id="T_be241_row5_col0" class="data row5 col0" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row5_col2" class="data row5 col2" >4 <span style="color: grey">(1.4%) </span></td>
      <td id="T_be241_row5_col3" class="data row5 col3" >4 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row6" class="row_heading level0 row6" >Speed</th>
      <td id="T_be241_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row6_col2" class="data row6 col2" >11 <span style="color: grey">(3.9%) </span></td>
      <td id="T_be241_row6_col3" class="data row6 col3" >11 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row7" class="row_heading level0 row7" >Strength</th>
      <td id="T_be241_row7_col0" class="data row7 col0" ><span style="color: grey">0 </span></td>
      <td id="T_be241_row7_col1" class="data row7 col1" >4 <span style="color: grey">(10.5%) </span></td>
      <td id="T_be241_row7_col2" class="data row7 col2" >49 <span style="color: grey">(17.2%) </span></td>
      <td id="T_be241_row7_col3" class="data row7 col3" >53 <span style="color: grey">(16.4%) </span></td>
    </tr>
    <tr>
      <th id="T_be241_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_be241_row8_col0" class="data row8 col0" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_be241_row8_col1" class="data row8 col1" >38 <span style="color: grey">(100.0%) </span></td>
      <td id="T_be241_row8_col2" class="data row8 col2" >285 <span style="color: grey">(100.0%) </span></td>
      <td id="T_be241_row8_col3" class="data row8 col3" >324 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



### <a id='toc1_4_11_'></a>[bonus - ci](#toc0_)


    
![svg](2_analyze_files/output_40_0.svg)
    


## <a id='toc1_5_'></a>[2025-03-18](#toc0_)


    
![png](2_analyze_files/output_42_0.png)
    



    
![svg](2_analyze_files/output_43_0.svg)
    



    
![svg](2_analyze_files/output_44_0.svg)
    



    
![svg](2_analyze_files/output_45_0.svg)
    


    ❌ df must have exactly 2 or 3 columns



    
![svg](2_analyze_files/output_47_0.svg)
    


## <a id='toc1_6_'></a>[chi-square](#toc0_)
steps:
- create subset of 2 cat variables each
- derive exploded dataset
- transform to 2x2 contingency table

    Chi-square statistic: 123.99178996951123
    p-value: 0.002995689777128063
    degrees of freedom: 84
    cells < 5: 85 | total cells: 105 | share of cells < 5% (should be <20%): 80.95%


## <a id='toc1_7_'></a>[export data](#toc0_)

## <a id='toc1_8_'></a>[2025-05-26 diagrams](#toc0_)


    
![svg](2_analyze_files/output_53_0.svg)
    



<style type="text/css">
#T_3c17e th {
  text-align: right;
}
#T_3c17e td {
  text-align: right;
}
#T_3c17e_row0_col0, #T_3c17e_row1_col0, #T_3c17e_row1_col2, #T_3c17e_row1_col3, #T_3c17e_row1_col5, #T_3c17e_row1_col10, #T_3c17e_row1_col11, #T_3c17e_row2_col1, #T_3c17e_row2_col2, #T_3c17e_row2_col3, #T_3c17e_row2_col4, #T_3c17e_row2_col5, #T_3c17e_row2_col6, #T_3c17e_row2_col7, #T_3c17e_row2_col9, #T_3c17e_row2_col10, #T_3c17e_row2_col11, #T_3c17e_row2_col12, #T_3c17e_row2_col13, #T_3c17e_row2_col14, #T_3c17e_row3_col0, #T_3c17e_row3_col1, #T_3c17e_row3_col2, #T_3c17e_row3_col3, #T_3c17e_row3_col4, #T_3c17e_row3_col5, #T_3c17e_row3_col6, #T_3c17e_row3_col7, #T_3c17e_row3_col9, #T_3c17e_row3_col10, #T_3c17e_row3_col11, #T_3c17e_row3_col12, #T_3c17e_row3_col14 {
  width: 10em;
  font-family: Courier;
}
#T_3c17e_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 94.9%, transparent 94.9%);
  font-family: Courier;
}
#T_3c17e_row0_col2, #T_3c17e_row0_col3, #T_3c17e_row0_col5, #T_3c17e_row0_col10, #T_3c17e_row0_col11, #T_3c17e_row2_col0, #T_3c17e_row4_col0, #T_3c17e_row4_col1, #T_3c17e_row4_col2, #T_3c17e_row4_col3, #T_3c17e_row4_col4, #T_3c17e_row4_col5, #T_3c17e_row4_col6, #T_3c17e_row4_col7, #T_3c17e_row4_col8, #T_3c17e_row4_col9, #T_3c17e_row4_col10, #T_3c17e_row4_col11, #T_3c17e_row4_col12, #T_3c17e_row4_col13, #T_3c17e_row4_col14, #T_3c17e_row4_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_3c17e_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.0%, transparent 80.0%);
  font-family: Courier;
}
#T_3c17e_row0_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 71.4%, transparent 71.4%);
  font-family: Courier;
}
#T_3c17e_row0_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 66.7%, transparent 66.7%);
  font-family: Courier;
}
#T_3c17e_row0_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.2%, transparent 68.2%);
  font-family: Courier;
}
#T_3c17e_row0_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.9%, transparent 90.9%);
  font-family: Courier;
}
#T_3c17e_row0_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 47.1%, transparent 47.1%);
  font-family: Courier;
}
#T_3c17e_row0_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.0%, transparent 28.0%);
  font-family: Courier;
}
#T_3c17e_row0_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 91.7%, transparent 91.7%);
  font-family: Courier;
}
#T_3c17e_row0_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 73.5%, transparent 73.5%);
  font-family: Courier;
}
#T_3c17e_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.1%, transparent 5.1%);
  font-family: Courier;
}
#T_3c17e_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_3c17e_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.6%, transparent 28.6%);
  font-family: Courier;
}
#T_3c17e_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_3c17e_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.5%, transparent 29.5%);
  font-family: Courier;
}
#T_3c17e_row1_col9 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.1%, transparent 9.1%);
  font-family: Courier;
}
#T_3c17e_row1_col12 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 52.9%, transparent 52.9%);
  font-family: Courier;
}
#T_3c17e_row1_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 68.0%, transparent 68.0%);
  font-family: Courier;
}
#T_3c17e_row1_col14 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_3c17e_row1_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.5%, transparent 24.5%);
  font-family: Courier;
}
#T_3c17e_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_3c17e_row2_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_3c17e_row3_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_3c17e_row3_col13 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_3c17e_row3_col15 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
</style>
<table id="T_3c17e">
  <thead>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th id="T_3c17e_level0_col0" class="col_heading level0 col0" >Bone injuries</th>
      <th id="T_3c17e_level0_col1" class="col_heading level0 col1" >Circulatory problems</th>
      <th id="T_3c17e_level0_col2" class="col_heading level0 col2" >Coughing fit</th>
      <th id="T_3c17e_level0_col3" class="col_heading level0 col3" >Enuresis</th>
      <th id="T_3c17e_level0_col4" class="col_heading level0 col4" >Itching</th>
      <th id="T_3c17e_level0_col5" class="col_heading level0 col5" >Muscle cramps</th>
      <th id="T_3c17e_level0_col6" class="col_heading level0 col6" >Muscle soreness</th>
      <th id="T_3c17e_level0_col7" class="col_heading level0 col7" >Nosebleed</th>
      <th id="T_3c17e_level0_col8" class="col_heading level0 col8" >Pain</th>
      <th id="T_3c17e_level0_col9" class="col_heading level0 col9" >Psychological stress reaction</th>
      <th id="T_3c17e_level0_col10" class="col_heading level0 col10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <th id="T_3c17e_level0_col11" class="col_heading level0 col11" >Severe exhaustion</th>
      <th id="T_3c17e_level0_col12" class="col_heading level0 col12" >Superficial injuries</th>
      <th id="T_3c17e_level0_col13" class="col_heading level0 col13" >Weichteil-/Gewebeverletzung</th>
      <th id="T_3c17e_level0_col14" class="col_heading level0 col14" >Übelkeit / Erbrechen</th>
      <th id="T_3c17e_level0_col15" class="col_heading level0 col15" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
      <th class="blank col12" >&nbsp;</th>
      <th class="blank col13" >&nbsp;</th>
      <th class="blank col14" >&nbsp;</th>
      <th class="blank col15" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_3c17e_level0_row0" class="row_heading level0 row0" >1</th>
      <td id="T_3c17e_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row0_col1" class="data row0 col1" >37 <span style="color: grey">(94.9%) </span></td>
      <td id="T_3c17e_row0_col2" class="data row0 col2" >5 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row0_col3" class="data row0 col3" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row0_col4" class="data row0 col4" >4 <span style="color: grey">(80.0%) </span></td>
      <td id="T_3c17e_row0_col5" class="data row0 col5" >3 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row0_col6" class="data row0 col6" >5 <span style="color: grey">(71.4%) </span></td>
      <td id="T_3c17e_row0_col7" class="data row0 col7" >2 <span style="color: grey">(66.7%) </span></td>
      <td id="T_3c17e_row0_col8" class="data row0 col8" >88 <span style="color: grey">(68.2%) </span></td>
      <td id="T_3c17e_row0_col9" class="data row0 col9" >10 <span style="color: grey">(90.9%) </span></td>
      <td id="T_3c17e_row0_col10" class="data row0 col10" >4 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row0_col11" class="data row0 col11" >6 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row0_col12" class="data row0 col12" >8 <span style="color: grey">(47.1%) </span></td>
      <td id="T_3c17e_row0_col13" class="data row0 col13" >7 <span style="color: grey">(28.0%) </span></td>
      <td id="T_3c17e_row0_col14" class="data row0 col14" >44 <span style="color: grey">(91.7%) </span></td>
      <td id="T_3c17e_row0_col15" class="data row0 col15" >225 <span style="color: grey">(73.5%) </span></td>
    </tr>
    <tr>
      <th id="T_3c17e_level0_row1" class="row_heading level0 row1" >2</th>
      <td id="T_3c17e_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row1_col1" class="data row1 col1" >2 <span style="color: grey">(5.1%) </span></td>
      <td id="T_3c17e_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row1_col4" class="data row1 col4" >1 <span style="color: grey">(20.0%) </span></td>
      <td id="T_3c17e_row1_col5" class="data row1 col5" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row1_col6" class="data row1 col6" >2 <span style="color: grey">(28.6%) </span></td>
      <td id="T_3c17e_row1_col7" class="data row1 col7" >1 <span style="color: grey">(33.3%) </span></td>
      <td id="T_3c17e_row1_col8" class="data row1 col8" >38 <span style="color: grey">(29.5%) </span></td>
      <td id="T_3c17e_row1_col9" class="data row1 col9" >1 <span style="color: grey">(9.1%) </span></td>
      <td id="T_3c17e_row1_col10" class="data row1 col10" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row1_col11" class="data row1 col11" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row1_col12" class="data row1 col12" >9 <span style="color: grey">(52.9%) </span></td>
      <td id="T_3c17e_row1_col13" class="data row1 col13" >17 <span style="color: grey">(68.0%) </span></td>
      <td id="T_3c17e_row1_col14" class="data row1 col14" >4 <span style="color: grey">(8.3%) </span></td>
      <td id="T_3c17e_row1_col15" class="data row1 col15" >75 <span style="color: grey">(24.5%) </span></td>
    </tr>
    <tr>
      <th id="T_3c17e_level0_row2" class="row_heading level0 row2" >3</th>
      <td id="T_3c17e_row2_col0" class="data row2 col0" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col6" class="data row2 col6" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col7" class="data row2 col7" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col8" class="data row2 col8" >2 <span style="color: grey">(1.6%) </span></td>
      <td id="T_3c17e_row2_col9" class="data row2 col9" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col10" class="data row2 col10" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col11" class="data row2 col11" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col12" class="data row2 col12" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col13" class="data row2 col13" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col14" class="data row2 col14" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row2_col15" class="data row2 col15" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_3c17e_level0_row3" class="row_heading level0 row3" >4</th>
      <td id="T_3c17e_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col4" class="data row3 col4" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col5" class="data row3 col5" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col6" class="data row3 col6" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col7" class="data row3 col7" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col8" class="data row3 col8" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_3c17e_row3_col9" class="data row3 col9" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col10" class="data row3 col10" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col11" class="data row3 col11" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col12" class="data row3 col12" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col13" class="data row3 col13" >1 <span style="color: grey">(4.0%) </span></td>
      <td id="T_3c17e_row3_col14" class="data row3 col14" ><span style="color: grey">0 </span></td>
      <td id="T_3c17e_row3_col15" class="data row3 col15" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_3c17e_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_3c17e_row4_col0" class="data row4 col0" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col1" class="data row4 col1" >39 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col2" class="data row4 col2" >5 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col3" class="data row4 col3" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col4" class="data row4 col4" >5 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col5" class="data row4 col5" >3 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col6" class="data row4 col6" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col7" class="data row4 col7" >3 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col8" class="data row4 col8" >129 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col9" class="data row4 col9" >11 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col10" class="data row4 col10" >4 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col11" class="data row4 col11" >6 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col12" class="data row4 col12" >17 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col13" class="data row4 col13" >25 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col14" class="data row4 col14" >48 <span style="color: grey">(100.0%) </span></td>
      <td id="T_3c17e_row4_col15" class="data row4 col15" >306 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_54_0.svg)
    



<style type="text/css">
#T_cf80a th {
  text-align: right;
}
#T_cf80a td {
  text-align: right;
}
#T_cf80a_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 62.5%, transparent 62.5%);
  font-family: Courier;
}
#T_cf80a_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.0%, transparent 80.0%);
  font-family: Courier;
}
#T_cf80a_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.2%, transparent 69.2%);
  font-family: Courier;
}
#T_cf80a_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 89.4%, transparent 89.4%);
  font-family: Courier;
}
#T_cf80a_row0_col4, #T_cf80a_row4_col0, #T_cf80a_row4_col1, #T_cf80a_row4_col2, #T_cf80a_row4_col3, #T_cf80a_row4_col4, #T_cf80a_row4_col5, #T_cf80a_row4_col6, #T_cf80a_row4_col7, #T_cf80a_row4_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_cf80a_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 84.7%, transparent 84.7%);
  font-family: Courier;
}
#T_cf80a_row0_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 84.2%, transparent 84.2%);
  font-family: Courier;
}
#T_cf80a_row0_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 54.5%, transparent 54.5%);
  font-family: Courier;
}
#T_cf80a_row0_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 79.2%, transparent 79.2%);
  font-family: Courier;
}
#T_cf80a_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.2%, transparent 31.2%);
  font-family: Courier;
}
#T_cf80a_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_cf80a_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.8%, transparent 30.8%);
  font-family: Courier;
}
#T_cf80a_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.6%, transparent 10.6%);
  font-family: Courier;
}
#T_cf80a_row1_col4, #T_cf80a_row2_col1, #T_cf80a_row2_col2, #T_cf80a_row2_col3, #T_cf80a_row2_col4, #T_cf80a_row2_col6, #T_cf80a_row3_col1, #T_cf80a_row3_col2, #T_cf80a_row3_col3, #T_cf80a_row3_col4, #T_cf80a_row3_col5, #T_cf80a_row3_col6 {
  width: 10em;
  font-family: Courier;
}
#T_cf80a_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
#T_cf80a_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.8%, transparent 15.8%);
  font-family: Courier;
}
#T_cf80a_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.8%, transparent 41.8%);
  font-family: Courier;
}
#T_cf80a_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.2%, transparent 19.2%);
  font-family: Courier;
}
#T_cf80a_row2_col0, #T_cf80a_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_cf80a_row2_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_cf80a_row2_col7, #T_cf80a_row3_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_cf80a_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_cf80a_row3_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
</style>
<table id="T_cf80a">
  <thead>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th id="T_cf80a_level0_col0" class="col_heading level0 col0" >Coordination problems</th>
      <th id="T_cf80a_level0_col1" class="col_heading level0 col1" >Environmental conditions</th>
      <th id="T_cf80a_level0_col2" class="col_heading level0 col2" >Kollision</th>
      <th id="T_cf80a_level0_col3" class="col_heading level0 col3" >Medical therapy</th>
      <th id="T_cf80a_level0_col4" class="col_heading level0 col4" >Other</th>
      <th id="T_cf80a_level0_col5" class="col_heading level0 col5" >Physical strain</th>
      <th id="T_cf80a_level0_col6" class="col_heading level0 col6" >Psychological strain</th>
      <th id="T_cf80a_level0_col7" class="col_heading level0 col7" >Sturzereignis</th>
      <th id="T_cf80a_level0_col8" class="col_heading level0 col8" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_cf80a_level0_row0" class="row_heading level0 row0" >1</th>
      <td id="T_cf80a_row0_col0" class="data row0 col0" >20 <span style="color: grey">(62.5%) </span></td>
      <td id="T_cf80a_row0_col1" class="data row0 col1" >8 <span style="color: grey">(80.0%) </span></td>
      <td id="T_cf80a_row0_col2" class="data row0 col2" >9 <span style="color: grey">(69.2%) </span></td>
      <td id="T_cf80a_row0_col3" class="data row0 col3" >93 <span style="color: grey">(89.4%) </span></td>
      <td id="T_cf80a_row0_col4" class="data row0 col4" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row0_col5" class="data row0 col5" >127 <span style="color: grey">(84.7%) </span></td>
      <td id="T_cf80a_row0_col6" class="data row0 col6" >16 <span style="color: grey">(84.2%) </span></td>
      <td id="T_cf80a_row0_col7" class="data row0 col7" >30 <span style="color: grey">(54.5%) </span></td>
      <td id="T_cf80a_row0_col8" class="data row0 col8" >305 <span style="color: grey">(79.2%) </span></td>
    </tr>
    <tr>
      <th id="T_cf80a_level0_row1" class="row_heading level0 row1" >2</th>
      <td id="T_cf80a_row1_col0" class="data row1 col0" >10 <span style="color: grey">(31.2%) </span></td>
      <td id="T_cf80a_row1_col1" class="data row1 col1" >2 <span style="color: grey">(20.0%) </span></td>
      <td id="T_cf80a_row1_col2" class="data row1 col2" >4 <span style="color: grey">(30.8%) </span></td>
      <td id="T_cf80a_row1_col3" class="data row1 col3" >11 <span style="color: grey">(10.6%) </span></td>
      <td id="T_cf80a_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row1_col5" class="data row1 col5" >21 <span style="color: grey">(14.0%) </span></td>
      <td id="T_cf80a_row1_col6" class="data row1 col6" >3 <span style="color: grey">(15.8%) </span></td>
      <td id="T_cf80a_row1_col7" class="data row1 col7" >23 <span style="color: grey">(41.8%) </span></td>
      <td id="T_cf80a_row1_col8" class="data row1 col8" >74 <span style="color: grey">(19.2%) </span></td>
    </tr>
    <tr>
      <th id="T_cf80a_level0_row2" class="row_heading level0 row2" >3</th>
      <td id="T_cf80a_row2_col0" class="data row2 col0" >1 <span style="color: grey">(3.1%) </span></td>
      <td id="T_cf80a_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row2_col5" class="data row2 col5" >2 <span style="color: grey">(1.3%) </span></td>
      <td id="T_cf80a_row2_col6" class="data row2 col6" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row2_col7" class="data row2 col7" >1 <span style="color: grey">(1.8%) </span></td>
      <td id="T_cf80a_row2_col8" class="data row2 col8" >4 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_cf80a_level0_row3" class="row_heading level0 row3" >4</th>
      <td id="T_cf80a_row3_col0" class="data row3 col0" >1 <span style="color: grey">(3.1%) </span></td>
      <td id="T_cf80a_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row3_col4" class="data row3 col4" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row3_col5" class="data row3 col5" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row3_col6" class="data row3 col6" ><span style="color: grey">0 </span></td>
      <td id="T_cf80a_row3_col7" class="data row3 col7" >1 <span style="color: grey">(1.8%) </span></td>
      <td id="T_cf80a_row3_col8" class="data row3 col8" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_cf80a_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_cf80a_row4_col0" class="data row4 col0" >32 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col1" class="data row4 col1" >10 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col2" class="data row4 col2" >13 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col3" class="data row4 col3" >104 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col4" class="data row4 col4" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col5" class="data row4 col5" >150 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col6" class="data row4 col6" >19 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col7" class="data row4 col7" >55 <span style="color: grey">(100.0%) </span></td>
      <td id="T_cf80a_row4_col8" class="data row4 col8" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_55_0.svg)
    



<style type="text/css">
#T_2d67a th {
  text-align: right;
}
#T_2d67a td {
  text-align: right;
}
#T_2d67a_row0_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.6%, transparent 58.6%);
  font-family: Courier;
}
#T_2d67a_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 83.6%, transparent 83.6%);
  font-family: Courier;
}
#T_2d67a_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.7%, transparent 80.7%);
  font-family: Courier;
}
#T_2d67a_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 78.1%, transparent 78.1%);
  font-family: Courier;
}
#T_2d67a_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_2d67a_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.0%, transparent 80.0%);
  font-family: Courier;
}
#T_2d67a_row0_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 76.7%, transparent 76.7%);
  font-family: Courier;
}
#T_2d67a_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.4%, transparent 41.4%);
  font-family: Courier;
}
#T_2d67a_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.4%, transparent 16.4%);
  font-family: Courier;
}
#T_2d67a_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.3%, transparent 19.3%);
  font-family: Courier;
}
#T_2d67a_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.8%, transparent 18.8%);
  font-family: Courier;
}
#T_2d67a_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.0%, transparent 30.0%);
  font-family: Courier;
}
#T_2d67a_row1_col5, #T_2d67a_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_2d67a_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.7%, transparent 21.7%);
  font-family: Courier;
}
#T_2d67a_row2_col0, #T_2d67a_row2_col1, #T_2d67a_row2_col2, #T_2d67a_row2_col5, #T_2d67a_row3_col0, #T_2d67a_row3_col1, #T_2d67a_row3_col2, #T_2d67a_row3_col3, #T_2d67a_row3_col5 {
  width: 10em;
  font-family: Courier;
}
#T_2d67a_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_2d67a_row2_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_2d67a_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_2d67a_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_2d67a_row4_col0, #T_2d67a_row4_col1, #T_2d67a_row4_col2, #T_2d67a_row4_col3, #T_2d67a_row4_col4, #T_2d67a_row4_col5, #T_2d67a_row4_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_2d67a">
  <thead>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th id="T_2d67a_level0_col0" class="col_heading level0 col0" >02 to 05 years</th>
      <th id="T_2d67a_level0_col1" class="col_heading level0 col1" >06 to 09 years</th>
      <th id="T_2d67a_level0_col2" class="col_heading level0 col2" >10 to 14 years</th>
      <th id="T_2d67a_level0_col3" class="col_heading level0 col3" >15 to 18 years</th>
      <th id="T_2d67a_level0_col4" class="col_heading level0 col4" >18+ years</th>
      <th id="T_2d67a_level0_col5" class="col_heading level0 col5" ><NA></th>
      <th id="T_2d67a_level0_col6" class="col_heading level0 col6" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.01] CTCAE</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_2d67a_level0_row0" class="row_heading level0 row0" >1</th>
      <td id="T_2d67a_row0_col0" class="data row0 col0" >17 <span style="color: grey">(58.6%) </span></td>
      <td id="T_2d67a_row0_col1" class="data row0 col1" >56 <span style="color: grey">(83.6%) </span></td>
      <td id="T_2d67a_row0_col2" class="data row0 col2" >46 <span style="color: grey">(80.7%) </span></td>
      <td id="T_2d67a_row0_col3" class="data row0 col3" >25 <span style="color: grey">(78.1%) </span></td>
      <td id="T_2d67a_row0_col4" class="data row0 col4" >4 <span style="color: grey">(40.0%) </span></td>
      <td id="T_2d67a_row0_col5" class="data row0 col5" >36 <span style="color: grey">(80.0%) </span></td>
      <td id="T_2d67a_row0_col6" class="data row0 col6" >184 <span style="color: grey">(76.7%) </span></td>
    </tr>
    <tr>
      <th id="T_2d67a_level0_row1" class="row_heading level0 row1" >2</th>
      <td id="T_2d67a_row1_col0" class="data row1 col0" >12 <span style="color: grey">(41.4%) </span></td>
      <td id="T_2d67a_row1_col1" class="data row1 col1" >11 <span style="color: grey">(16.4%) </span></td>
      <td id="T_2d67a_row1_col2" class="data row1 col2" >11 <span style="color: grey">(19.3%) </span></td>
      <td id="T_2d67a_row1_col3" class="data row1 col3" >6 <span style="color: grey">(18.8%) </span></td>
      <td id="T_2d67a_row1_col4" class="data row1 col4" >3 <span style="color: grey">(30.0%) </span></td>
      <td id="T_2d67a_row1_col5" class="data row1 col5" >9 <span style="color: grey">(20.0%) </span></td>
      <td id="T_2d67a_row1_col6" class="data row1 col6" >52 <span style="color: grey">(21.7%) </span></td>
    </tr>
    <tr>
      <th id="T_2d67a_level0_row2" class="row_heading level0 row2" >3</th>
      <td id="T_2d67a_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row2_col3" class="data row2 col3" >1 <span style="color: grey">(3.1%) </span></td>
      <td id="T_2d67a_row2_col4" class="data row2 col4" >2 <span style="color: grey">(20.0%) </span></td>
      <td id="T_2d67a_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row2_col6" class="data row2 col6" >3 <span style="color: grey">(1.2%) </span></td>
    </tr>
    <tr>
      <th id="T_2d67a_level0_row3" class="row_heading level0 row3" >4</th>
      <td id="T_2d67a_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row3_col4" class="data row3 col4" >1 <span style="color: grey">(10.0%) </span></td>
      <td id="T_2d67a_row3_col5" class="data row3 col5" ><span style="color: grey">0 </span></td>
      <td id="T_2d67a_row3_col6" class="data row3 col6" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_2d67a_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_2d67a_row4_col0" class="data row4 col0" >29 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2d67a_row4_col1" class="data row4 col1" >67 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2d67a_row4_col2" class="data row4 col2" >57 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2d67a_row4_col3" class="data row4 col3" >32 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2d67a_row4_col4" class="data row4 col4" >10 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2d67a_row4_col5" class="data row4 col5" >45 <span style="color: grey">(100.0%) </span></td>
      <td id="T_2d67a_row4_col6" class="data row4 col6" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_56_0.svg)
    



<style type="text/css">
#T_82ebc th {
  text-align: right;
}
#T_82ebc td {
  text-align: right;
}
#T_82ebc_row0_col0, #T_82ebc_row0_col1, #T_82ebc_row0_col2, #T_82ebc_row0_col4, #T_82ebc_row0_col6, #T_82ebc_row0_col7, #T_82ebc_row2_col4 {
  width: 10em;
  font-family: Courier;
}
#T_82ebc_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_82ebc_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_82ebc_row0_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_82ebc_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_82ebc_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.0%, transparent 10.0%);
  font-family: Courier;
}
#T_82ebc_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_82ebc_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.1%, transparent 22.1%);
  font-family: Courier;
}
#T_82ebc_row1_col4, #T_82ebc_row3_col0, #T_82ebc_row3_col1, #T_82ebc_row3_col2, #T_82ebc_row3_col3, #T_82ebc_row3_col4, #T_82ebc_row3_col5, #T_82ebc_row3_col6, #T_82ebc_row3_col7, #T_82ebc_row3_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_82ebc_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.0%, transparent 12.0%);
  font-family: Courier;
}
#T_82ebc_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.1%, transparent 21.1%);
  font-family: Courier;
}
#T_82ebc_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_82ebc_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.2%, transparent 13.2%);
  font-family: Courier;
}
#T_82ebc_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.9%, transparent 96.9%);
  font-family: Courier;
}
#T_82ebc_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 90.0%, transparent 90.0%);
  font-family: Courier;
}
#T_82ebc_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 92.3%, transparent 92.3%);
  font-family: Courier;
}
#T_82ebc_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 76.9%, transparent 76.9%);
  font-family: Courier;
}
#T_82ebc_row2_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 87.3%, transparent 87.3%);
  font-family: Courier;
}
#T_82ebc_row2_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 78.9%, transparent 78.9%);
  font-family: Courier;
}
#T_82ebc_row2_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.2%, transparent 98.2%);
  font-family: Courier;
}
#T_82ebc_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.2%, transparent 86.2%);
  font-family: Courier;
}
</style>
<table id="T_82ebc">
  <thead>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th id="T_82ebc_level0_col0" class="col_heading level0 col0" >Coordination problems</th>
      <th id="T_82ebc_level0_col1" class="col_heading level0 col1" >Environmental conditions</th>
      <th id="T_82ebc_level0_col2" class="col_heading level0 col2" >Kollision</th>
      <th id="T_82ebc_level0_col3" class="col_heading level0 col3" >Medical therapy</th>
      <th id="T_82ebc_level0_col4" class="col_heading level0 col4" >Other</th>
      <th id="T_82ebc_level0_col5" class="col_heading level0 col5" >Physical strain</th>
      <th id="T_82ebc_level0_col6" class="col_heading level0 col6" >Psychological strain</th>
      <th id="T_82ebc_level0_col7" class="col_heading level0 col7" >Sturzereignis</th>
      <th id="T_82ebc_level0_col8" class="col_heading level0 col8" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.03] Exercise-related</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_82ebc_level0_row0" class="row_heading level0 row0" ><NA></th>
      <td id="T_82ebc_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_82ebc_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_82ebc_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_82ebc_row0_col3" class="data row0 col3" >1 <span style="color: grey">(1.0%) </span></td>
      <td id="T_82ebc_row0_col4" class="data row0 col4" ><span style="color: grey">0 </span></td>
      <td id="T_82ebc_row0_col5" class="data row0 col5" >1 <span style="color: grey">(0.7%) </span></td>
      <td id="T_82ebc_row0_col6" class="data row0 col6" ><span style="color: grey">0 </span></td>
      <td id="T_82ebc_row0_col7" class="data row0 col7" ><span style="color: grey">0 </span></td>
      <td id="T_82ebc_row0_col8" class="data row0 col8" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_82ebc_level0_row1" class="row_heading level0 row1" >No</th>
      <td id="T_82ebc_row1_col0" class="data row1 col0" >1 <span style="color: grey">(3.1%) </span></td>
      <td id="T_82ebc_row1_col1" class="data row1 col1" >1 <span style="color: grey">(10.0%) </span></td>
      <td id="T_82ebc_row1_col2" class="data row1 col2" >1 <span style="color: grey">(7.7%) </span></td>
      <td id="T_82ebc_row1_col3" class="data row1 col3" >23 <span style="color: grey">(22.1%) </span></td>
      <td id="T_82ebc_row1_col4" class="data row1 col4" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row1_col5" class="data row1 col5" >18 <span style="color: grey">(12.0%) </span></td>
      <td id="T_82ebc_row1_col6" class="data row1 col6" >4 <span style="color: grey">(21.1%) </span></td>
      <td id="T_82ebc_row1_col7" class="data row1 col7" >1 <span style="color: grey">(1.8%) </span></td>
      <td id="T_82ebc_row1_col8" class="data row1 col8" >51 <span style="color: grey">(13.2%) </span></td>
    </tr>
    <tr>
      <th id="T_82ebc_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_82ebc_row2_col0" class="data row2 col0" >31 <span style="color: grey">(96.9%) </span></td>
      <td id="T_82ebc_row2_col1" class="data row2 col1" >9 <span style="color: grey">(90.0%) </span></td>
      <td id="T_82ebc_row2_col2" class="data row2 col2" >12 <span style="color: grey">(92.3%) </span></td>
      <td id="T_82ebc_row2_col3" class="data row2 col3" >80 <span style="color: grey">(76.9%) </span></td>
      <td id="T_82ebc_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_82ebc_row2_col5" class="data row2 col5" >131 <span style="color: grey">(87.3%) </span></td>
      <td id="T_82ebc_row2_col6" class="data row2 col6" >15 <span style="color: grey">(78.9%) </span></td>
      <td id="T_82ebc_row2_col7" class="data row2 col7" >54 <span style="color: grey">(98.2%) </span></td>
      <td id="T_82ebc_row2_col8" class="data row2 col8" >332 <span style="color: grey">(86.2%) </span></td>
    </tr>
    <tr>
      <th id="T_82ebc_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_82ebc_row3_col0" class="data row3 col0" >32 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col1" class="data row3 col1" >10 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col2" class="data row3 col2" >13 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col3" class="data row3 col3" >104 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col4" class="data row3 col4" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col5" class="data row3 col5" >150 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col6" class="data row3 col6" >19 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col7" class="data row3 col7" >55 <span style="color: grey">(100.0%) </span></td>
      <td id="T_82ebc_row3_col8" class="data row3 col8" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_57_0.svg)
    



<style type="text/css">
#T_01a6f th {
  text-align: right;
}
#T_01a6f td {
  text-align: right;
}
#T_01a6f_row0_col0, #T_01a6f_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_01a6f_row0_col1, #T_01a6f_row0_col2, #T_01a6f_row0_col3, #T_01a6f_row0_col4, #T_01a6f_row0_col5, #T_01a6f_row0_col6, #T_01a6f_row1_col1, #T_01a6f_row1_col4, #T_01a6f_row1_col6 {
  width: 10em;
  font-family: Courier;
}
#T_01a6f_row0_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_01a6f_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_01a6f_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.2%, transparent 19.2%);
  font-family: Courier;
}
#T_01a6f_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.7%, transparent 23.7%);
  font-family: Courier;
}
#T_01a6f_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_01a6f_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 87.5%, transparent 87.5%);
  font-family: Courier;
}
#T_01a6f_row2_col1, #T_01a6f_row2_col4, #T_01a6f_row2_col6, #T_01a6f_row3_col0, #T_01a6f_row3_col1, #T_01a6f_row3_col2, #T_01a6f_row3_col3, #T_01a6f_row3_col4, #T_01a6f_row3_col5, #T_01a6f_row3_col6, #T_01a6f_row3_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_01a6f_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 94.4%, transparent 94.4%);
  font-family: Courier;
}
#T_01a6f_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 80.8%, transparent 80.8%);
  font-family: Courier;
}
#T_01a6f_row2_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 76.3%, transparent 76.3%);
  font-family: Courier;
}
#T_01a6f_row2_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 87.1%, transparent 87.1%);
  font-family: Courier;
}
</style>
<table id="T_01a6f">
  <thead>
    <tr>
      <th class="index_name level0" >[05.06] Setting</th>
      <th id="T_01a6f_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_01a6f_level0_col1" class="col_heading level0 col1" >At home (via telemedicine)</th>
      <th id="T_01a6f_level0_col2" class="col_heading level0 col2" >Gym</th>
      <th id="T_01a6f_level0_col3" class="col_heading level0 col3" >Hospital corridor</th>
      <th id="T_01a6f_level0_col4" class="col_heading level0 col4" >Outside</th>
      <th id="T_01a6f_level0_col5" class="col_heading level0 col5" >Patients room</th>
      <th id="T_01a6f_level0_col6" class="col_heading level0 col6" >Weiteres</th>
      <th id="T_01a6f_level0_col7" class="col_heading level0 col7" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[01.03] Exercise-related</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_01a6f_level0_row0" class="row_heading level0 row0" ><NA></th>
      <td id="T_01a6f_row0_col0" class="data row0 col0" >1 <span style="color: grey">(6.2%) </span></td>
      <td id="T_01a6f_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row0_col4" class="data row0 col4" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row0_col5" class="data row0 col5" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row0_col6" class="data row0 col6" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row0_col7" class="data row0 col7" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_01a6f_level0_row1" class="row_heading level0 row1" >No</th>
      <td id="T_01a6f_row1_col0" class="data row1 col0" >1 <span style="color: grey">(6.2%) </span></td>
      <td id="T_01a6f_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row1_col2" class="data row1 col2" >5 <span style="color: grey">(5.6%) </span></td>
      <td id="T_01a6f_row1_col3" class="data row1 col3" >10 <span style="color: grey">(19.2%) </span></td>
      <td id="T_01a6f_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row1_col5" class="data row1 col5" >14 <span style="color: grey">(23.7%) </span></td>
      <td id="T_01a6f_row1_col6" class="data row1 col6" ><span style="color: grey">0 </span></td>
      <td id="T_01a6f_row1_col7" class="data row1 col7" >30 <span style="color: grey">(12.5%) </span></td>
    </tr>
    <tr>
      <th id="T_01a6f_level0_row2" class="row_heading level0 row2" >Yes</th>
      <td id="T_01a6f_row2_col0" class="data row2 col0" >14 <span style="color: grey">(87.5%) </span></td>
      <td id="T_01a6f_row2_col1" class="data row2 col1" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row2_col2" class="data row2 col2" >85 <span style="color: grey">(94.4%) </span></td>
      <td id="T_01a6f_row2_col3" class="data row2 col3" >42 <span style="color: grey">(80.8%) </span></td>
      <td id="T_01a6f_row2_col4" class="data row2 col4" >15 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row2_col5" class="data row2 col5" >45 <span style="color: grey">(76.3%) </span></td>
      <td id="T_01a6f_row2_col6" class="data row2 col6" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row2_col7" class="data row2 col7" >209 <span style="color: grey">(87.1%) </span></td>
    </tr>
    <tr>
      <th id="T_01a6f_level0_row3" class="row_heading level0 row3" >Total</th>
      <td id="T_01a6f_row3_col0" class="data row3 col0" >16 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row3_col1" class="data row3 col1" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row3_col2" class="data row3 col2" >90 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row3_col3" class="data row3 col3" >52 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row3_col4" class="data row3 col4" >15 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row3_col5" class="data row3 col5" >59 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row3_col6" class="data row3 col6" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_01a6f_row3_col7" class="data row3 col7" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_58_0.svg)
    



<style type="text/css">
#T_20512 th {
  text-align: right;
}
#T_20512 td {
  text-align: right;
}
#T_20512_row0_col0, #T_20512_row1_col0, #T_20512_row4_col0, #T_20512_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.1%, transparent 2.1%);
  font-family: Courier;
}
#T_20512_row0_col1, #T_20512_row0_col2, #T_20512_row0_col3, #T_20512_row0_col4, #T_20512_row0_col6, #T_20512_row1_col2, #T_20512_row1_col4, #T_20512_row2_col0, #T_20512_row2_col1, #T_20512_row2_col2, #T_20512_row2_col4, #T_20512_row2_col7, #T_20512_row3_col0, #T_20512_row3_col1, #T_20512_row3_col2, #T_20512_row3_col4, #T_20512_row3_col6, #T_20512_row3_col7, #T_20512_row4_col1, #T_20512_row4_col4, #T_20512_row5_col0, #T_20512_row5_col1, #T_20512_row5_col2, #T_20512_row5_col4, #T_20512_row5_col6, #T_20512_row5_col7, #T_20512_row6_col0, #T_20512_row6_col1, #T_20512_row6_col2, #T_20512_row6_col3, #T_20512_row6_col4, #T_20512_row7_col0, #T_20512_row7_col1, #T_20512_row7_col2, #T_20512_row7_col6, #T_20512_row7_col7, #T_20512_row9_col1, #T_20512_row9_col2, #T_20512_row9_col4, #T_20512_row10_col0, #T_20512_row10_col1, #T_20512_row10_col2, #T_20512_row10_col4, #T_20512_row10_col6, #T_20512_row10_col7, #T_20512_row11_col1, #T_20512_row11_col2, #T_20512_row11_col4, #T_20512_row11_col6, #T_20512_row11_col7, #T_20512_row12_col3, #T_20512_row12_col4, #T_20512_row12_col5, #T_20512_row12_col6, #T_20512_row13_col4, #T_20512_row14_col0, #T_20512_row14_col2, #T_20512_row14_col4, #T_20512_row14_col7 {
  width: 10em;
  font-family: Courier;
}
#T_20512_row0_col5, #T_20512_row0_col8, #T_20512_row7_col5, #T_20512_row7_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.6%, transparent 0.6%);
  font-family: Courier;
}
#T_20512_row0_col7, #T_20512_row1_col7, #T_20512_row4_col7, #T_20512_row6_col7, #T_20512_row9_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_20512_row1_col1, #T_20512_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 21.4%, transparent 21.4%);
  font-family: Courier;
}
#T_20512_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.0%, transparent 18.0%);
  font-family: Courier;
}
#T_20512_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.8%, transparent 18.8%);
  font-family: Courier;
}
#T_20512_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.9%, transparent 17.9%);
  font-family: Courier;
}
#T_20512_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.2%, transparent 13.2%);
  font-family: Courier;
}
#T_20512_row2_col3, #T_20512_row3_col8, #T_20512_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_20512_row2_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.8%, transparent 2.8%);
  font-family: Courier;
}
#T_20512_row2_col6, #T_20512_row4_col6, #T_20512_row6_col6, #T_20512_row13_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_20512_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.4%, transparent 1.4%);
  font-family: Courier;
}
#T_20512_row3_col3, #T_20512_row4_col3, #T_20512_row5_col3, #T_20512_row6_col8, #T_20512_row10_col8, #T_20512_row13_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_20512_row3_col5, #T_20512_row13_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_20512_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.3%, transparent 5.3%);
  font-family: Courier;
}
#T_20512_row4_col5, #T_20512_row9_col5, #T_20512_row10_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_20512_row4_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_20512_row5_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_20512_row5_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_20512_row6_col5, #T_20512_row11_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_20512_row7_col4, #T_20512_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_20512_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 58.3%, transparent 58.3%);
  font-family: Courier;
}
#T_20512_row8_col1, #T_20512_row8_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.6%, transparent 28.6%);
  font-family: Courier;
}
#T_20512_row8_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.9%, transparent 57.9%);
  font-family: Courier;
}
#T_20512_row8_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.0%, transparent 27.0%);
  font-family: Courier;
}
#T_20512_row8_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 35.8%, transparent 35.8%);
  font-family: Courier;
}
#T_20512_row8_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.3%, transparent 57.3%);
  font-family: Courier;
}
#T_20512_row8_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.7%, transparent 39.7%);
  font-family: Courier;
}
#T_20512_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_20512_row9_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_20512_row9_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 32.1%, transparent 32.1%);
  font-family: Courier;
}
#T_20512_row9_col8, #T_20512_row11_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.1%, transparent 4.1%);
  font-family: Courier;
}
#T_20512_row10_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_20512_row11_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_20512_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.4%, transparent 10.4%);
  font-family: Courier;
}
#T_20512_row12_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.5%, transparent 10.5%);
  font-family: Courier;
}
#T_20512_row12_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.1%, transparent 17.1%);
  font-family: Courier;
}
#T_20512_row12_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_20512_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_20512_row13_col1, #T_20512_row14_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_20512_row13_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.3%, transparent 26.3%);
  font-family: Courier;
}
#T_20512_row13_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.5%, transparent 19.5%);
  font-family: Courier;
}
#T_20512_row13_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.3%, transparent 7.3%);
  font-family: Courier;
}
#T_20512_row14_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 36.9%, transparent 36.9%);
  font-family: Courier;
}
#T_20512_row14_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 23.9%, transparent 23.9%);
  font-family: Courier;
}
#T_20512_row14_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.1%, transparent 7.1%);
  font-family: Courier;
}
#T_20512_row14_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.5%, transparent 18.5%);
  font-family: Courier;
}
#T_20512_row15_col0, #T_20512_row15_col1, #T_20512_row15_col2, #T_20512_row15_col3, #T_20512_row15_col4, #T_20512_row15_col5, #T_20512_row15_col6, #T_20512_row15_col7, #T_20512_row15_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_20512">
  <thead>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th id="T_20512_level0_col0" class="col_heading level0 col0" >Coordination problems</th>
      <th id="T_20512_level0_col1" class="col_heading level0 col1" >Environmental conditions</th>
      <th id="T_20512_level0_col2" class="col_heading level0 col2" >Kollision</th>
      <th id="T_20512_level0_col3" class="col_heading level0 col3" >Medical therapy</th>
      <th id="T_20512_level0_col4" class="col_heading level0 col4" >Other</th>
      <th id="T_20512_level0_col5" class="col_heading level0 col5" >Physical strain</th>
      <th id="T_20512_level0_col6" class="col_heading level0 col6" >Psychological strain</th>
      <th id="T_20512_level0_col7" class="col_heading level0 col7" >Sturzereignis</th>
      <th id="T_20512_level0_col8" class="col_heading level0 col8" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_20512_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_20512_row0_col0" class="data row0 col0" >1 <span style="color: grey">(2.1%) </span></td>
      <td id="T_20512_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row0_col4" class="data row0 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row0_col5" class="data row0 col5" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_20512_row0_col6" class="data row0 col6" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row0_col7" class="data row0 col7" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_20512_row0_col8" class="data row0 col8" >3 <span style="color: grey">(0.6%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_20512_row1_col0" class="data row1 col0" >1 <span style="color: grey">(2.1%) </span></td>
      <td id="T_20512_row1_col1" class="data row1 col1" >3 <span style="color: grey">(21.4%) </span></td>
      <td id="T_20512_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row1_col3" class="data row1 col3" >22 <span style="color: grey">(18.0%) </span></td>
      <td id="T_20512_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row1_col5" class="data row1 col5" >33 <span style="color: grey">(18.8%) </span></td>
      <td id="T_20512_row1_col6" class="data row1 col6" >5 <span style="color: grey">(17.9%) </span></td>
      <td id="T_20512_row1_col7" class="data row1 col7" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_20512_row1_col8" class="data row1 col8" >65 <span style="color: grey">(13.2%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_20512_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row2_col3" class="data row2 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_20512_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row2_col5" class="data row2 col5" >5 <span style="color: grey">(2.8%) </span></td>
      <td id="T_20512_row2_col6" class="data row2 col6" >1 <span style="color: grey">(3.6%) </span></td>
      <td id="T_20512_row2_col7" class="data row2 col7" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row2_col8" class="data row2 col8" >7 <span style="color: grey">(1.4%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_20512_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row3_col3" class="data row3 col3" >2 <span style="color: grey">(1.6%) </span></td>
      <td id="T_20512_row3_col4" class="data row3 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row3_col5" class="data row3 col5" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_20512_row3_col6" class="data row3 col6" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row3_col7" class="data row3 col7" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row3_col8" class="data row3 col8" >4 <span style="color: grey">(0.8%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_20512_row4_col0" class="data row4 col0" >1 <span style="color: grey">(2.1%) </span></td>
      <td id="T_20512_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row4_col2" class="data row4 col2" >1 <span style="color: grey">(5.3%) </span></td>
      <td id="T_20512_row4_col3" class="data row4 col3" >2 <span style="color: grey">(1.6%) </span></td>
      <td id="T_20512_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row4_col5" class="data row4 col5" >4 <span style="color: grey">(2.3%) </span></td>
      <td id="T_20512_row4_col6" class="data row4 col6" >1 <span style="color: grey">(3.6%) </span></td>
      <td id="T_20512_row4_col7" class="data row4 col7" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_20512_row4_col8" class="data row4 col8" >10 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_20512_row5_col0" class="data row5 col0" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row5_col3" class="data row5 col3" >2 <span style="color: grey">(1.6%) </span></td>
      <td id="T_20512_row5_col4" class="data row5 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row5_col5" class="data row5 col5" >3 <span style="color: grey">(1.7%) </span></td>
      <td id="T_20512_row5_col6" class="data row5 col6" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row5_col7" class="data row5 col7" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row5_col8" class="data row5 col8" >5 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_20512_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row6_col4" class="data row6 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row6_col5" class="data row6 col5" >6 <span style="color: grey">(3.4%) </span></td>
      <td id="T_20512_row6_col6" class="data row6 col6" >1 <span style="color: grey">(3.6%) </span></td>
      <td id="T_20512_row6_col7" class="data row6 col7" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_20512_row6_col8" class="data row6 col8" >8 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_20512_row7_col0" class="data row7 col0" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row7_col1" class="data row7 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row7_col3" class="data row7 col3" >1 <span style="color: grey">(0.8%) </span></td>
      <td id="T_20512_row7_col4" class="data row7 col4" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_20512_row7_col5" class="data row7 col5" >1 <span style="color: grey">(0.6%) </span></td>
      <td id="T_20512_row7_col6" class="data row7 col6" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row7_col7" class="data row7 col7" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row7_col8" class="data row7 col8" >3 <span style="color: grey">(0.6%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_20512_row8_col0" class="data row8 col0" >28 <span style="color: grey">(58.3%) </span></td>
      <td id="T_20512_row8_col1" class="data row8 col1" >4 <span style="color: grey">(28.6%) </span></td>
      <td id="T_20512_row8_col2" class="data row8 col2" >11 <span style="color: grey">(57.9%) </span></td>
      <td id="T_20512_row8_col3" class="data row8 col3" >33 <span style="color: grey">(27.0%) </span></td>
      <td id="T_20512_row8_col4" class="data row8 col4" >1 <span style="color: grey">(50.0%) </span></td>
      <td id="T_20512_row8_col5" class="data row8 col5" >63 <span style="color: grey">(35.8%) </span></td>
      <td id="T_20512_row8_col6" class="data row8 col6" >8 <span style="color: grey">(28.6%) </span></td>
      <td id="T_20512_row8_col7" class="data row8 col7" >47 <span style="color: grey">(57.3%) </span></td>
      <td id="T_20512_row8_col8" class="data row8 col8" >195 <span style="color: grey">(39.7%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_20512_row9_col0" class="data row9 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_20512_row9_col1" class="data row9 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row9_col3" class="data row9 col3" >3 <span style="color: grey">(2.5%) </span></td>
      <td id="T_20512_row9_col4" class="data row9 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row9_col5" class="data row9 col5" >4 <span style="color: grey">(2.3%) </span></td>
      <td id="T_20512_row9_col6" class="data row9 col6" >9 <span style="color: grey">(32.1%) </span></td>
      <td id="T_20512_row9_col7" class="data row9 col7" >1 <span style="color: grey">(1.2%) </span></td>
      <td id="T_20512_row9_col8" class="data row9 col8" >20 <span style="color: grey">(4.1%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_20512_row10_col0" class="data row10 col0" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row10_col3" class="data row10 col3" >4 <span style="color: grey">(3.3%) </span></td>
      <td id="T_20512_row10_col4" class="data row10 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row10_col5" class="data row10 col5" >4 <span style="color: grey">(2.3%) </span></td>
      <td id="T_20512_row10_col6" class="data row10 col6" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row10_col7" class="data row10 col7" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row10_col8" class="data row10 col8" >8 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_20512_row11_col0" class="data row11 col0" >1 <span style="color: grey">(2.1%) </span></td>
      <td id="T_20512_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row11_col3" class="data row11 col3" >5 <span style="color: grey">(4.1%) </span></td>
      <td id="T_20512_row11_col4" class="data row11 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row11_col5" class="data row11 col5" >6 <span style="color: grey">(3.4%) </span></td>
      <td id="T_20512_row11_col6" class="data row11 col6" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row11_col7" class="data row11 col7" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row11_col8" class="data row11 col8" >12 <span style="color: grey">(2.4%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_20512_row12_col0" class="data row12 col0" >5 <span style="color: grey">(10.4%) </span></td>
      <td id="T_20512_row12_col1" class="data row12 col1" >3 <span style="color: grey">(21.4%) </span></td>
      <td id="T_20512_row12_col2" class="data row12 col2" >2 <span style="color: grey">(10.5%) </span></td>
      <td id="T_20512_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row12_col4" class="data row12 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row12_col5" class="data row12 col5" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row12_col6" class="data row12 col6" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row12_col7" class="data row12 col7" >14 <span style="color: grey">(17.1%) </span></td>
      <td id="T_20512_row12_col8" class="data row12 col8" >24 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_20512_row13_col0" class="data row13 col0" >8 <span style="color: grey">(16.7%) </span></td>
      <td id="T_20512_row13_col1" class="data row13 col1" >2 <span style="color: grey">(14.3%) </span></td>
      <td id="T_20512_row13_col2" class="data row13 col2" >5 <span style="color: grey">(26.3%) </span></td>
      <td id="T_20512_row13_col3" class="data row13 col3" >2 <span style="color: grey">(1.6%) </span></td>
      <td id="T_20512_row13_col4" class="data row13 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row13_col5" class="data row13 col5" >2 <span style="color: grey">(1.1%) </span></td>
      <td id="T_20512_row13_col6" class="data row13 col6" >1 <span style="color: grey">(3.6%) </span></td>
      <td id="T_20512_row13_col7" class="data row13 col7" >16 <span style="color: grey">(19.5%) </span></td>
      <td id="T_20512_row13_col8" class="data row13 col8" >36 <span style="color: grey">(7.3%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_20512_row14_col0" class="data row14 col0" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row14_col1" class="data row14 col1" >2 <span style="color: grey">(14.3%) </span></td>
      <td id="T_20512_row14_col2" class="data row14 col2" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row14_col3" class="data row14 col3" >45 <span style="color: grey">(36.9%) </span></td>
      <td id="T_20512_row14_col4" class="data row14 col4" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row14_col5" class="data row14 col5" >42 <span style="color: grey">(23.9%) </span></td>
      <td id="T_20512_row14_col6" class="data row14 col6" >2 <span style="color: grey">(7.1%) </span></td>
      <td id="T_20512_row14_col7" class="data row14 col7" ><span style="color: grey">0 </span></td>
      <td id="T_20512_row14_col8" class="data row14 col8" >91 <span style="color: grey">(18.5%) </span></td>
    </tr>
    <tr>
      <th id="T_20512_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_20512_row15_col0" class="data row15 col0" >48 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col1" class="data row15 col1" >14 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col2" class="data row15 col2" >19 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col3" class="data row15 col3" >122 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col4" class="data row15 col4" >2 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col5" class="data row15 col5" >176 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col6" class="data row15 col6" >28 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col7" class="data row15 col7" >82 <span style="color: grey">(100.0%) </span></td>
      <td id="T_20512_row15_col8" class="data row15 col8" >491 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_59_0.svg)
    



<style type="text/css">
#T_c4e93 th {
  text-align: right;
}
#T_c4e93 td {
  text-align: right;
}
#T_c4e93_row0_col0, #T_c4e93_row0_col2, #T_c4e93_row0_col3, #T_c4e93_row2_col1, #T_c4e93_row2_col2, #T_c4e93_row2_col3, #T_c4e93_row3_col1, #T_c4e93_row3_col2, #T_c4e93_row3_col3, #T_c4e93_row4_col2, #T_c4e93_row4_col3, #T_c4e93_row5_col1, #T_c4e93_row5_col2, #T_c4e93_row5_col3, #T_c4e93_row6_col1, #T_c4e93_row6_col3, #T_c4e93_row7_col1, #T_c4e93_row7_col2, #T_c4e93_row7_col3, #T_c4e93_row8_col3, #T_c4e93_row9_col2, #T_c4e93_row9_col3, #T_c4e93_row10_col1, #T_c4e93_row10_col2, #T_c4e93_row10_col3, #T_c4e93_row11_col1, #T_c4e93_row11_col2, #T_c4e93_row11_col3, #T_c4e93_row12_col2, #T_c4e93_row12_col3, #T_c4e93_row13_col3, #T_c4e93_row14_col1, #T_c4e93_row14_col3 {
  width: 10em;
  font-family: Courier;
}
#T_c4e93_row0_col1, #T_c4e93_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.3%, transparent 4.3%);
  font-family: Courier;
}
#T_c4e93_row0_col4, #T_c4e93_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_c4e93_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.0%, transparent 14.0%);
  font-family: Courier;
}
#T_c4e93_row1_col2, #T_c4e93_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_c4e93_row1_col3, #T_c4e93_row15_col0, #T_c4e93_row15_col1, #T_c4e93_row15_col2, #T_c4e93_row15_col3, #T_c4e93_row15_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_c4e93_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_c4e93_row2_col0, #T_c4e93_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_c4e93_row2_col4, #T_c4e93_row4_col0, #T_c4e93_row4_col4, #T_c4e93_row10_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_c4e93_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_c4e93_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_c4e93_row5_col0, #T_c4e93_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.2%, transparent 1.2%);
  font-family: Courier;
}
#T_c4e93_row5_col4, #T_c4e93_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_c4e93_row6_col0, #T_c4e93_row11_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.4%, transparent 2.4%);
  font-family: Courier;
}
#T_c4e93_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_c4e93_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.0%, transparent 42.0%);
  font-family: Courier;
}
#T_c4e93_row8_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 45.7%, transparent 45.7%);
  font-family: Courier;
}
#T_c4e93_row8_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_c4e93_row8_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.2%, transparent 42.2%);
  font-family: Courier;
}
#T_c4e93_row9_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.2%, transparent 3.2%);
  font-family: Courier;
}
#T_c4e93_row9_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.5%, transparent 6.5%);
  font-family: Courier;
}
#T_c4e93_row9_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_c4e93_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_c4e93_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.8%, transparent 4.8%);
  font-family: Courier;
}
#T_c4e93_row12_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.9%, transparent 10.9%);
  font-family: Courier;
}
#T_c4e93_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_c4e93_row13_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_c4e93_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.1%, transparent 26.1%);
  font-family: Courier;
}
#T_c4e93_row13_col2, #T_c4e93_row14_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_c4e93_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.2%, transparent 8.2%);
  font-family: Courier;
}
#T_c4e93_row14_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.4%, transparent 18.4%);
  font-family: Courier;
}
#T_c4e93_row14_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
</style>
<table id="T_c4e93">
  <thead>
    <tr>
      <th class="index_name level0" >[05.01] Therapy phase</th>
      <th id="T_c4e93_level0_col0" class="col_heading level0 col0" >Acute therapy</th>
      <th id="T_c4e93_level0_col1" class="col_heading level0 col1" >Aftercare</th>
      <th id="T_c4e93_level0_col2" class="col_heading level0 col2" >Long-term therapy</th>
      <th id="T_c4e93_level0_col3" class="col_heading level0 col3" >Weiß nicht</th>
      <th id="T_c4e93_level0_col4" class="col_heading level0 col4" >Total</th>
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
      <th id="T_c4e93_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_c4e93_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row0_col1" class="data row0 col1" >2 <span style="color: grey">(4.3%) </span></td>
      <td id="T_c4e93_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row0_col4" class="data row0 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_c4e93_row1_col0" class="data row1 col0" >35 <span style="color: grey">(14.0%) </span></td>
      <td id="T_c4e93_row1_col1" class="data row1 col1" >2 <span style="color: grey">(4.3%) </span></td>
      <td id="T_c4e93_row1_col2" class="data row1 col2" >1 <span style="color: grey">(11.1%) </span></td>
      <td id="T_c4e93_row1_col3" class="data row1 col3" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c4e93_row1_col4" class="data row1 col4" >39 <span style="color: grey">(12.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_c4e93_row2_col0" class="data row2 col0" >5 <span style="color: grey">(2.0%) </span></td>
      <td id="T_c4e93_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row2_col4" class="data row2 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_c4e93_row3_col0" class="data row3 col0" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_c4e93_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row3_col4" class="data row3 col4" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_c4e93_row4_col0" class="data row4 col0" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_c4e93_row4_col1" class="data row4 col1" >1 <span style="color: grey">(2.2%) </span></td>
      <td id="T_c4e93_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row4_col4" class="data row4 col4" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_c4e93_row5_col0" class="data row5 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_c4e93_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row5_col4" class="data row5 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_c4e93_row6_col0" class="data row6 col0" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_c4e93_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row6_col2" class="data row6 col2" >1 <span style="color: grey">(11.1%) </span></td>
      <td id="T_c4e93_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row6_col4" class="data row6 col4" >7 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_c4e93_row7_col0" class="data row7 col0" >3 <span style="color: grey">(1.2%) </span></td>
      <td id="T_c4e93_row7_col1" class="data row7 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row7_col4" class="data row7 col4" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_c4e93_row8_col0" class="data row8 col0" >105 <span style="color: grey">(42.0%) </span></td>
      <td id="T_c4e93_row8_col1" class="data row8 col1" >21 <span style="color: grey">(45.7%) </span></td>
      <td id="T_c4e93_row8_col2" class="data row8 col2" >3 <span style="color: grey">(33.3%) </span></td>
      <td id="T_c4e93_row8_col3" class="data row8 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row8_col4" class="data row8 col4" >129 <span style="color: grey">(42.2%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_c4e93_row9_col0" class="data row9 col0" >8 <span style="color: grey">(3.2%) </span></td>
      <td id="T_c4e93_row9_col1" class="data row9 col1" >3 <span style="color: grey">(6.5%) </span></td>
      <td id="T_c4e93_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row9_col4" class="data row9 col4" >11 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_c4e93_row10_col0" class="data row10 col0" >4 <span style="color: grey">(1.6%) </span></td>
      <td id="T_c4e93_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row10_col4" class="data row10 col4" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_c4e93_row11_col0" class="data row11 col0" >6 <span style="color: grey">(2.4%) </span></td>
      <td id="T_c4e93_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row11_col4" class="data row11 col4" >6 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_c4e93_row12_col0" class="data row12 col0" >12 <span style="color: grey">(4.8%) </span></td>
      <td id="T_c4e93_row12_col1" class="data row12 col1" >5 <span style="color: grey">(10.9%) </span></td>
      <td id="T_c4e93_row12_col2" class="data row12 col2" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row12_col3" class="data row12 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row12_col4" class="data row12 col4" >17 <span style="color: grey">(5.6%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_c4e93_row13_col0" class="data row13 col0" >11 <span style="color: grey">(4.4%) </span></td>
      <td id="T_c4e93_row13_col1" class="data row13 col1" >12 <span style="color: grey">(26.1%) </span></td>
      <td id="T_c4e93_row13_col2" class="data row13 col2" >2 <span style="color: grey">(22.2%) </span></td>
      <td id="T_c4e93_row13_col3" class="data row13 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row13_col4" class="data row13 col4" >25 <span style="color: grey">(8.2%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_c4e93_row14_col0" class="data row14 col0" >46 <span style="color: grey">(18.4%) </span></td>
      <td id="T_c4e93_row14_col1" class="data row14 col1" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row14_col2" class="data row14 col2" >2 <span style="color: grey">(22.2%) </span></td>
      <td id="T_c4e93_row14_col3" class="data row14 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c4e93_row14_col4" class="data row14 col4" >48 <span style="color: grey">(15.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c4e93_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_c4e93_row15_col0" class="data row15 col0" >250 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c4e93_row15_col1" class="data row15 col1" >46 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c4e93_row15_col2" class="data row15 col2" >9 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c4e93_row15_col3" class="data row15 col3" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c4e93_row15_col4" class="data row15 col4" >306 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_60_0.svg)
    



<style type="text/css">
#T_f184d th {
  text-align: right;
}
#T_f184d td {
  text-align: right;
}
#T_f184d_row0_col0, #T_f184d_row0_col1, #T_f184d_row0_col3, #T_f184d_row1_col0, #T_f184d_row1_col1, #T_f184d_row1_col2, #T_f184d_row1_col3, #T_f184d_row2_col0, #T_f184d_row2_col1, #T_f184d_row2_col2, #T_f184d_row2_col3, #T_f184d_row3_col0, #T_f184d_row3_col1, #T_f184d_row3_col2, #T_f184d_row3_col3, #T_f184d_row4_col0, #T_f184d_row4_col1, #T_f184d_row4_col2, #T_f184d_row4_col3, #T_f184d_row5_col0, #T_f184d_row5_col1, #T_f184d_row5_col2, #T_f184d_row5_col3, #T_f184d_row6_col0, #T_f184d_row6_col1, #T_f184d_row6_col2, #T_f184d_row6_col3, #T_f184d_row7_col0, #T_f184d_row7_col1, #T_f184d_row7_col2, #T_f184d_row7_col3, #T_f184d_row9_col0, #T_f184d_row9_col2, #T_f184d_row9_col3, #T_f184d_row10_col0, #T_f184d_row10_col1, #T_f184d_row10_col2, #T_f184d_row10_col3, #T_f184d_row11_col0, #T_f184d_row11_col1, #T_f184d_row11_col2, #T_f184d_row11_col3, #T_f184d_row12_col1, #T_f184d_row13_col0, #T_f184d_row14_col0, #T_f184d_row14_col2, #T_f184d_row14_col3 {
  width: 10em;
  font-family: Courier;
}
#T_f184d_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_f184d_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
#T_f184d_row0_col5, #T_f184d_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.7%, transparent 0.7%);
  font-family: Courier;
}
#T_f184d_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.7%, transparent 14.7%);
  font-family: Courier;
}
#T_f184d_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_f184d_row2_col4, #T_f184d_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.9%, transparent 1.9%);
  font-family: Courier;
}
#T_f184d_row2_col5, #T_f184d_row4_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.6%, transparent 1.6%);
  font-family: Courier;
}
#T_f184d_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.8%, transparent 0.8%);
  font-family: Courier;
}
#T_f184d_row5_col4, #T_f184d_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.1%, transparent 1.1%);
  font-family: Courier;
}
#T_f184d_row5_col5, #T_f184d_row7_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.0%, transparent 1.0%);
  font-family: Courier;
}
#T_f184d_row6_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_f184d_row6_col5, #T_f184d_row11_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.3%, transparent 2.3%);
  font-family: Courier;
}
#T_f184d_row8_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 75.0%, transparent 75.0%);
  font-family: Courier;
}
#T_f184d_row8_col1, #T_f184d_row13_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 33.3%, transparent 33.3%);
  font-family: Courier;
}
#T_f184d_row8_col2, #T_f184d_row13_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 40.0%, transparent 40.0%);
  font-family: Courier;
}
#T_f184d_row8_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_f184d_row8_col4, #T_f184d_row13_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.7%, transparent 41.7%);
  font-family: Courier;
}
#T_f184d_row8_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 42.2%, transparent 42.2%);
  font-family: Courier;
}
#T_f184d_row9_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_f184d_row9_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_f184d_row9_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.6%, transparent 3.6%);
  font-family: Courier;
}
#T_f184d_row10_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_f184d_row10_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.3%, transparent 1.3%);
  font-family: Courier;
}
#T_f184d_row11_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_f184d_row12_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_f184d_row12_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.3%, transparent 13.3%);
  font-family: Courier;
}
#T_f184d_row12_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_f184d_row12_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_f184d_row12_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_f184d_row13_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.1%, transparent 4.1%);
  font-family: Courier;
}
#T_f184d_row13_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.2%, transparent 8.2%);
  font-family: Courier;
}
#T_f184d_row14_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_f184d_row14_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 17.7%, transparent 17.7%);
  font-family: Courier;
}
#T_f184d_row14_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
#T_f184d_row15_col0, #T_f184d_row15_col1, #T_f184d_row15_col2, #T_f184d_row15_col3, #T_f184d_row15_col4, #T_f184d_row15_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_f184d">
  <thead>
    <tr>
      <th class="index_name level0" >[05.02] Group size</th>
      <th id="T_f184d_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_f184d_level0_col1" class="col_heading level0 col1" >Group 2-5</th>
      <th id="T_f184d_level0_col2" class="col_heading level0 col2" >Group 5 to 10</th>
      <th id="T_f184d_level0_col3" class="col_heading level0 col3" >Group over 10</th>
      <th id="T_f184d_level0_col4" class="col_heading level0 col4" >Individual</th>
      <th id="T_f184d_level0_col5" class="col_heading level0 col5" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.02] Type</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_f184d_level0_row0" class="row_heading level0 row0" >Bone injuries</th>
      <td id="T_f184d_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row0_col2" class="data row0 col2" >1 <span style="color: grey">(6.7%) </span></td>
      <td id="T_f184d_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row0_col4" class="data row0 col4" >1 <span style="color: grey">(0.4%) </span></td>
      <td id="T_f184d_row0_col5" class="data row0 col5" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row1" class="row_heading level0 row1" >Circulatory problems</th>
      <td id="T_f184d_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row1_col1" class="data row1 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row1_col2" class="data row1 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row1_col4" class="data row1 col4" >39 <span style="color: grey">(14.7%) </span></td>
      <td id="T_f184d_row1_col5" class="data row1 col5" >39 <span style="color: grey">(12.7%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row2" class="row_heading level0 row2" >Coughing fit</th>
      <td id="T_f184d_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row2_col1" class="data row2 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row2_col2" class="data row2 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row2_col4" class="data row2 col4" >5 <span style="color: grey">(1.9%) </span></td>
      <td id="T_f184d_row2_col5" class="data row2 col5" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row3" class="row_heading level0 row3" >Enuresis</th>
      <td id="T_f184d_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row3_col4" class="data row3 col4" >2 <span style="color: grey">(0.8%) </span></td>
      <td id="T_f184d_row3_col5" class="data row3 col5" >2 <span style="color: grey">(0.7%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row4" class="row_heading level0 row4" >Itching</th>
      <td id="T_f184d_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row4_col1" class="data row4 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row4_col4" class="data row4 col4" >5 <span style="color: grey">(1.9%) </span></td>
      <td id="T_f184d_row4_col5" class="data row4 col5" >5 <span style="color: grey">(1.6%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row5" class="row_heading level0 row5" >Muscle cramps</th>
      <td id="T_f184d_row5_col0" class="data row5 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row5_col1" class="data row5 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row5_col2" class="data row5 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row5_col3" class="data row5 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row5_col4" class="data row5 col4" >3 <span style="color: grey">(1.1%) </span></td>
      <td id="T_f184d_row5_col5" class="data row5 col5" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row6" class="row_heading level0 row6" >Muscle soreness</th>
      <td id="T_f184d_row6_col0" class="data row6 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row6_col1" class="data row6 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row6_col2" class="data row6 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row6_col3" class="data row6 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row6_col4" class="data row6 col4" >7 <span style="color: grey">(2.6%) </span></td>
      <td id="T_f184d_row6_col5" class="data row6 col5" >7 <span style="color: grey">(2.3%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row7" class="row_heading level0 row7" >Nosebleed</th>
      <td id="T_f184d_row7_col0" class="data row7 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row7_col1" class="data row7 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row7_col2" class="data row7 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row7_col3" class="data row7 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row7_col4" class="data row7 col4" >3 <span style="color: grey">(1.1%) </span></td>
      <td id="T_f184d_row7_col5" class="data row7 col5" >3 <span style="color: grey">(1.0%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row8" class="row_heading level0 row8" >Pain</th>
      <td id="T_f184d_row8_col0" class="data row8 col0" >3 <span style="color: grey">(75.0%) </span></td>
      <td id="T_f184d_row8_col1" class="data row8 col1" >3 <span style="color: grey">(33.3%) </span></td>
      <td id="T_f184d_row8_col2" class="data row8 col2" >6 <span style="color: grey">(40.0%) </span></td>
      <td id="T_f184d_row8_col3" class="data row8 col3" >6 <span style="color: grey">(50.0%) </span></td>
      <td id="T_f184d_row8_col4" class="data row8 col4" >111 <span style="color: grey">(41.7%) </span></td>
      <td id="T_f184d_row8_col5" class="data row8 col5" >129 <span style="color: grey">(42.2%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row9" class="row_heading level0 row9" >Psychological stress reaction</th>
      <td id="T_f184d_row9_col0" class="data row9 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row9_col1" class="data row9 col1" >2 <span style="color: grey">(22.2%) </span></td>
      <td id="T_f184d_row9_col2" class="data row9 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row9_col3" class="data row9 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row9_col4" class="data row9 col4" >9 <span style="color: grey">(3.4%) </span></td>
      <td id="T_f184d_row9_col5" class="data row9 col5" >11 <span style="color: grey">(3.6%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row10" class="row_heading level0 row10" >Schmerzhafter Spontaneous painful bowel movement</th>
      <td id="T_f184d_row10_col0" class="data row10 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row10_col1" class="data row10 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row10_col2" class="data row10 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row10_col3" class="data row10 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row10_col4" class="data row10 col4" >4 <span style="color: grey">(1.5%) </span></td>
      <td id="T_f184d_row10_col5" class="data row10 col5" >4 <span style="color: grey">(1.3%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row11" class="row_heading level0 row11" >Severe exhaustion</th>
      <td id="T_f184d_row11_col0" class="data row11 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row11_col1" class="data row11 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row11_col2" class="data row11 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row11_col3" class="data row11 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row11_col4" class="data row11 col4" >6 <span style="color: grey">(2.3%) </span></td>
      <td id="T_f184d_row11_col5" class="data row11 col5" >6 <span style="color: grey">(2.0%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row12" class="row_heading level0 row12" >Superficial injuries</th>
      <td id="T_f184d_row12_col0" class="data row12 col0" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_f184d_row12_col1" class="data row12 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row12_col2" class="data row12 col2" >2 <span style="color: grey">(13.3%) </span></td>
      <td id="T_f184d_row12_col3" class="data row12 col3" >1 <span style="color: grey">(8.3%) </span></td>
      <td id="T_f184d_row12_col4" class="data row12 col4" >13 <span style="color: grey">(4.9%) </span></td>
      <td id="T_f184d_row12_col5" class="data row12 col5" >17 <span style="color: grey">(5.6%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row13" class="row_heading level0 row13" >Weichteil-/Gewebeverletzung</th>
      <td id="T_f184d_row13_col0" class="data row13 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row13_col1" class="data row13 col1" >3 <span style="color: grey">(33.3%) </span></td>
      <td id="T_f184d_row13_col2" class="data row13 col2" >6 <span style="color: grey">(40.0%) </span></td>
      <td id="T_f184d_row13_col3" class="data row13 col3" >5 <span style="color: grey">(41.7%) </span></td>
      <td id="T_f184d_row13_col4" class="data row13 col4" >11 <span style="color: grey">(4.1%) </span></td>
      <td id="T_f184d_row13_col5" class="data row13 col5" >25 <span style="color: grey">(8.2%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row14" class="row_heading level0 row14" >Übelkeit / Erbrechen</th>
      <td id="T_f184d_row14_col0" class="data row14 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row14_col1" class="data row14 col1" >1 <span style="color: grey">(11.1%) </span></td>
      <td id="T_f184d_row14_col2" class="data row14 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row14_col3" class="data row14 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f184d_row14_col4" class="data row14 col4" >47 <span style="color: grey">(17.7%) </span></td>
      <td id="T_f184d_row14_col5" class="data row14 col5" >48 <span style="color: grey">(15.7%) </span></td>
    </tr>
    <tr>
      <th id="T_f184d_level0_row15" class="row_heading level0 row15" >Total</th>
      <td id="T_f184d_row15_col0" class="data row15 col0" >4 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f184d_row15_col1" class="data row15 col1" >9 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f184d_row15_col2" class="data row15 col2" >15 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f184d_row15_col3" class="data row15 col3" >12 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f184d_row15_col4" class="data row15 col4" >266 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f184d_row15_col5" class="data row15 col5" >306 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_61_0.svg)
    



<style type="text/css">
#T_5f0c4 th {
  text-align: right;
}
#T_5f0c4 td {
  text-align: right;
}
#T_5f0c4_row0_col0, #T_5f0c4_row2_col0, #T_5f0c4_row6_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.2%, transparent 6.2%);
  font-family: Courier;
}
#T_5f0c4_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.7%, transparent 12.7%);
  font-family: Courier;
}
#T_5f0c4_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_5f0c4_row0_col3, #T_5f0c4_row2_col3, #T_5f0c4_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.0%, transparent 2.0%);
  font-family: Courier;
}
#T_5f0c4_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.2%, transparent 22.2%);
  font-family: Courier;
}
#T_5f0c4_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.9%, transparent 5.9%);
  font-family: Courier;
}
#T_5f0c4_row0_col6, #T_5f0c4_row1_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.3%, transparent 8.3%);
  font-family: Courier;
}
#T_5f0c4_row1_col1, #T_5f0c4_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.9%, transparent 0.9%);
  font-family: Courier;
}
#T_5f0c4_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_5f0c4_row1_col3, #T_5f0c4_row1_col4, #T_5f0c4_row2_col4, #T_5f0c4_row2_col5, #T_5f0c4_row4_col0, #T_5f0c4_row4_col2, #T_5f0c4_row4_col4, #T_5f0c4_row4_col5, #T_5f0c4_row6_col4 {
  width: 10em;
  font-family: Courier;
}
#T_5f0c4_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.4%, transparent 4.4%);
  font-family: Courier;
}
#T_5f0c4_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.6%, transparent 2.6%);
  font-family: Courier;
}
#T_5f0c4_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.5%, transparent 5.5%);
  font-family: Courier;
}
#T_5f0c4_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_5f0c4_row2_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_5f0c4_row3_col0, #T_5f0c4_row7_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_5f0c4_row3_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.5%, transparent 25.5%);
  font-family: Courier;
}
#T_5f0c4_row3_col2, #T_5f0c4_row7_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.8%, transparent 27.8%);
  font-family: Courier;
}
#T_5f0c4_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 37.3%, transparent 37.3%);
  font-family: Courier;
}
#T_5f0c4_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.1%, transparent 11.1%);
  font-family: Courier;
}
#T_5f0c4_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.5%, transparent 26.5%);
  font-family: Courier;
}
#T_5f0c4_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.0%, transparent 27.0%);
  font-family: Courier;
}
#T_5f0c4_row4_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.5%, transparent 0.5%);
  font-family: Courier;
}
#T_5f0c4_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.9%, transparent 22.9%);
  font-family: Courier;
}
#T_5f0c4_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 34.5%, transparent 34.5%);
  font-family: Courier;
}
#T_5f0c4_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 45.6%, transparent 45.6%);
  font-family: Courier;
}
#T_5f0c4_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 49.0%, transparent 49.0%);
  font-family: Courier;
}
#T_5f0c4_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.9%, transparent 38.9%);
  font-family: Courier;
}
#T_5f0c4_row5_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 41.2%, transparent 41.2%);
  font-family: Courier;
}
#T_5f0c4_row5_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 39.0%, transparent 39.0%);
  font-family: Courier;
}
#T_5f0c4_row6_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.5%, transparent 4.5%);
  font-family: Courier;
}
#T_5f0c4_row6_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.9%, transparent 8.9%);
  font-family: Courier;
}
#T_5f0c4_row6_col3, #T_5f0c4_row7_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.9%, transparent 3.9%);
  font-family: Courier;
}
#T_5f0c4_row6_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_5f0c4_row6_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.9%, transparent 4.9%);
  font-family: Courier;
}
#T_5f0c4_row7_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.5%, transparent 15.5%);
  font-family: Courier;
}
#T_5f0c4_row7_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_5f0c4_row7_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.6%, transparent 20.6%);
  font-family: Courier;
}
#T_5f0c4_row7_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_5f0c4_row8_col0, #T_5f0c4_row8_col1, #T_5f0c4_row8_col2, #T_5f0c4_row8_col3, #T_5f0c4_row8_col4, #T_5f0c4_row8_col5, #T_5f0c4_row8_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_5f0c4">
  <thead>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th id="T_5f0c4_level0_col0" class="col_heading level0 col0" >02 to 05 years</th>
      <th id="T_5f0c4_level0_col1" class="col_heading level0 col1" >06 to 09 years</th>
      <th id="T_5f0c4_level0_col2" class="col_heading level0 col2" >10 to 14 years</th>
      <th id="T_5f0c4_level0_col3" class="col_heading level0 col3" >15 to 18 years</th>
      <th id="T_5f0c4_level0_col4" class="col_heading level0 col4" >18+ years</th>
      <th id="T_5f0c4_level0_col5" class="col_heading level0 col5" ><NA></th>
      <th id="T_5f0c4_level0_col6" class="col_heading level0 col6" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[02.03] Trigger</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_5f0c4_level0_row0" class="row_heading level0 row0" >Coordination problems</th>
      <td id="T_5f0c4_row0_col0" class="data row0 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_5f0c4_row0_col1" class="data row0 col1" >14 <span style="color: grey">(12.7%) </span></td>
      <td id="T_5f0c4_row0_col2" class="data row0 col2" >6 <span style="color: grey">(6.7%) </span></td>
      <td id="T_5f0c4_row0_col3" class="data row0 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_5f0c4_row0_col4" class="data row0 col4" >4 <span style="color: grey">(22.2%) </span></td>
      <td id="T_5f0c4_row0_col5" class="data row0 col5" >4 <span style="color: grey">(5.9%) </span></td>
      <td id="T_5f0c4_row0_col6" class="data row0 col6" >32 <span style="color: grey">(8.3%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row1" class="row_heading level0 row1" >Environmental conditions</th>
      <td id="T_5f0c4_row1_col0" class="data row1 col0" >4 <span style="color: grey">(8.3%) </span></td>
      <td id="T_5f0c4_row1_col1" class="data row1 col1" >1 <span style="color: grey">(0.9%) </span></td>
      <td id="T_5f0c4_row1_col2" class="data row1 col2" >2 <span style="color: grey">(2.2%) </span></td>
      <td id="T_5f0c4_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row1_col5" class="data row1 col5" >3 <span style="color: grey">(4.4%) </span></td>
      <td id="T_5f0c4_row1_col6" class="data row1 col6" >10 <span style="color: grey">(2.6%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row2" class="row_heading level0 row2" >Kollision</th>
      <td id="T_5f0c4_row2_col0" class="data row2 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_5f0c4_row2_col1" class="data row2 col1" >6 <span style="color: grey">(5.5%) </span></td>
      <td id="T_5f0c4_row2_col2" class="data row2 col2" >3 <span style="color: grey">(3.3%) </span></td>
      <td id="T_5f0c4_row2_col3" class="data row2 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_5f0c4_row2_col4" class="data row2 col4" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row2_col6" class="data row2 col6" >13 <span style="color: grey">(3.4%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row3" class="row_heading level0 row3" >Medical therapy</th>
      <td id="T_5f0c4_row3_col0" class="data row3 col0" >12 <span style="color: grey">(25.0%) </span></td>
      <td id="T_5f0c4_row3_col1" class="data row3 col1" >28 <span style="color: grey">(25.5%) </span></td>
      <td id="T_5f0c4_row3_col2" class="data row3 col2" >25 <span style="color: grey">(27.8%) </span></td>
      <td id="T_5f0c4_row3_col3" class="data row3 col3" >19 <span style="color: grey">(37.3%) </span></td>
      <td id="T_5f0c4_row3_col4" class="data row3 col4" >2 <span style="color: grey">(11.1%) </span></td>
      <td id="T_5f0c4_row3_col5" class="data row3 col5" >18 <span style="color: grey">(26.5%) </span></td>
      <td id="T_5f0c4_row3_col6" class="data row3 col6" >104 <span style="color: grey">(27.0%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row4" class="row_heading level0 row4" >Other</th>
      <td id="T_5f0c4_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row4_col1" class="data row4 col1" >1 <span style="color: grey">(0.9%) </span></td>
      <td id="T_5f0c4_row4_col2" class="data row4 col2" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row4_col3" class="data row4 col3" >1 <span style="color: grey">(2.0%) </span></td>
      <td id="T_5f0c4_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row4_col5" class="data row4 col5" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row4_col6" class="data row4 col6" >2 <span style="color: grey">(0.5%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row5" class="row_heading level0 row5" >Physical strain</th>
      <td id="T_5f0c4_row5_col0" class="data row5 col0" >11 <span style="color: grey">(22.9%) </span></td>
      <td id="T_5f0c4_row5_col1" class="data row5 col1" >38 <span style="color: grey">(34.5%) </span></td>
      <td id="T_5f0c4_row5_col2" class="data row5 col2" >41 <span style="color: grey">(45.6%) </span></td>
      <td id="T_5f0c4_row5_col3" class="data row5 col3" >25 <span style="color: grey">(49.0%) </span></td>
      <td id="T_5f0c4_row5_col4" class="data row5 col4" >7 <span style="color: grey">(38.9%) </span></td>
      <td id="T_5f0c4_row5_col5" class="data row5 col5" >28 <span style="color: grey">(41.2%) </span></td>
      <td id="T_5f0c4_row5_col6" class="data row5 col6" >150 <span style="color: grey">(39.0%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row6" class="row_heading level0 row6" >Psychological strain</th>
      <td id="T_5f0c4_row6_col0" class="data row6 col0" >3 <span style="color: grey">(6.2%) </span></td>
      <td id="T_5f0c4_row6_col1" class="data row6 col1" >5 <span style="color: grey">(4.5%) </span></td>
      <td id="T_5f0c4_row6_col2" class="data row6 col2" >8 <span style="color: grey">(8.9%) </span></td>
      <td id="T_5f0c4_row6_col3" class="data row6 col3" >2 <span style="color: grey">(3.9%) </span></td>
      <td id="T_5f0c4_row6_col4" class="data row6 col4" ><span style="color: grey">0 </span></td>
      <td id="T_5f0c4_row6_col5" class="data row6 col5" >1 <span style="color: grey">(1.5%) </span></td>
      <td id="T_5f0c4_row6_col6" class="data row6 col6" >19 <span style="color: grey">(4.9%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row7" class="row_heading level0 row7" >Sturzereignis</th>
      <td id="T_5f0c4_row7_col0" class="data row7 col0" >12 <span style="color: grey">(25.0%) </span></td>
      <td id="T_5f0c4_row7_col1" class="data row7 col1" >17 <span style="color: grey">(15.5%) </span></td>
      <td id="T_5f0c4_row7_col2" class="data row7 col2" >5 <span style="color: grey">(5.6%) </span></td>
      <td id="T_5f0c4_row7_col3" class="data row7 col3" >2 <span style="color: grey">(3.9%) </span></td>
      <td id="T_5f0c4_row7_col4" class="data row7 col4" >5 <span style="color: grey">(27.8%) </span></td>
      <td id="T_5f0c4_row7_col5" class="data row7 col5" >14 <span style="color: grey">(20.6%) </span></td>
      <td id="T_5f0c4_row7_col6" class="data row7 col6" >55 <span style="color: grey">(14.3%) </span></td>
    </tr>
    <tr>
      <th id="T_5f0c4_level0_row8" class="row_heading level0 row8" >Total</th>
      <td id="T_5f0c4_row8_col0" class="data row8 col0" >48 <span style="color: grey">(100.0%) </span></td>
      <td id="T_5f0c4_row8_col1" class="data row8 col1" >110 <span style="color: grey">(100.0%) </span></td>
      <td id="T_5f0c4_row8_col2" class="data row8 col2" >90 <span style="color: grey">(100.0%) </span></td>
      <td id="T_5f0c4_row8_col3" class="data row8 col3" >51 <span style="color: grey">(100.0%) </span></td>
      <td id="T_5f0c4_row8_col4" class="data row8 col4" >18 <span style="color: grey">(100.0%) </span></td>
      <td id="T_5f0c4_row8_col5" class="data row8 col5" >68 <span style="color: grey">(100.0%) </span></td>
      <td id="T_5f0c4_row8_col6" class="data row8 col6" >385 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_62_0.svg)
    



<style type="text/css">
#T_ee278 th {
  text-align: right;
}
#T_ee278 td {
  text-align: right;
}
#T_ee278_row0_col0, #T_ee278_row0_col6, #T_ee278_row4_col0, #T_ee278_row4_col1, #T_ee278_row4_col2, #T_ee278_row4_col3, #T_ee278_row4_col4, #T_ee278_row4_col5, #T_ee278_row4_col6, #T_ee278_row4_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
#T_ee278_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 28.6%, transparent 28.6%);
  font-family: Courier;
}
#T_ee278_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 84.4%, transparent 84.4%);
  font-family: Courier;
}
#T_ee278_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 86.5%, transparent 86.5%);
  font-family: Courier;
}
#T_ee278_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.0%, transparent 20.0%);
  font-family: Courier;
}
#T_ee278_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 98.3%, transparent 98.3%);
  font-family: Courier;
}
#T_ee278_row0_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 83.8%, transparent 83.8%);
  font-family: Courier;
}
#T_ee278_row1_col0, #T_ee278_row1_col5, #T_ee278_row1_col6, #T_ee278_row2_col0, #T_ee278_row2_col5, #T_ee278_row2_col6, #T_ee278_row3_col0, #T_ee278_row3_col1, #T_ee278_row3_col2, #T_ee278_row3_col3, #T_ee278_row3_col4, #T_ee278_row3_col6 {
  width: 10em;
  font-family: Courier;
}
#T_ee278_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 57.1%, transparent 57.1%);
  font-family: Courier;
}
#T_ee278_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.2%, transparent 12.2%);
  font-family: Courier;
}
#T_ee278_row1_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_ee278_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 73.3%, transparent 73.3%);
  font-family: Courier;
}
#T_ee278_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.5%, transparent 12.5%);
  font-family: Courier;
}
#T_ee278_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.3%, transparent 14.3%);
  font-family: Courier;
}
#T_ee278_row2_col2, #T_ee278_row2_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.3%, transparent 3.3%);
  font-family: Courier;
}
#T_ee278_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.8%, transparent 5.8%);
  font-family: Courier;
}
#T_ee278_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_ee278_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_ee278_row3_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 0.4%, transparent 0.4%);
  font-family: Courier;
}
</style>
<table id="T_ee278">
  <thead>
    <tr>
      <th class="index_name level0" >[05.06] Setting</th>
      <th id="T_ee278_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_ee278_level0_col1" class="col_heading level0 col1" >At home (via telemedicine)</th>
      <th id="T_ee278_level0_col2" class="col_heading level0 col2" >Gym</th>
      <th id="T_ee278_level0_col3" class="col_heading level0 col3" >Hospital corridor</th>
      <th id="T_ee278_level0_col4" class="col_heading level0 col4" >Outside</th>
      <th id="T_ee278_level0_col5" class="col_heading level0 col5" >Patients room</th>
      <th id="T_ee278_level0_col6" class="col_heading level0 col6" >Weiteres</th>
      <th id="T_ee278_level0_col7" class="col_heading level0 col7" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.01] Therapy phase</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ee278_level0_row0" class="row_heading level0 row0" >Acute therapy</th>
      <td id="T_ee278_row0_col0" class="data row0 col0" >16 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row0_col1" class="data row0 col1" >2 <span style="color: grey">(28.6%) </span></td>
      <td id="T_ee278_row0_col2" class="data row0 col2" >76 <span style="color: grey">(84.4%) </span></td>
      <td id="T_ee278_row0_col3" class="data row0 col3" >45 <span style="color: grey">(86.5%) </span></td>
      <td id="T_ee278_row0_col4" class="data row0 col4" >3 <span style="color: grey">(20.0%) </span></td>
      <td id="T_ee278_row0_col5" class="data row0 col5" >58 <span style="color: grey">(98.3%) </span></td>
      <td id="T_ee278_row0_col6" class="data row0 col6" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row0_col7" class="data row0 col7" >201 <span style="color: grey">(83.8%) </span></td>
    </tr>
    <tr>
      <th id="T_ee278_level0_row1" class="row_heading level0 row1" >Aftercare</th>
      <td id="T_ee278_row1_col0" class="data row1 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row1_col1" class="data row1 col1" >4 <span style="color: grey">(57.1%) </span></td>
      <td id="T_ee278_row1_col2" class="data row1 col2" >11 <span style="color: grey">(12.2%) </span></td>
      <td id="T_ee278_row1_col3" class="data row1 col3" >4 <span style="color: grey">(7.7%) </span></td>
      <td id="T_ee278_row1_col4" class="data row1 col4" >11 <span style="color: grey">(73.3%) </span></td>
      <td id="T_ee278_row1_col5" class="data row1 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row1_col6" class="data row1 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row1_col7" class="data row1 col7" >30 <span style="color: grey">(12.5%) </span></td>
    </tr>
    <tr>
      <th id="T_ee278_level0_row2" class="row_heading level0 row2" >Long-term therapy</th>
      <td id="T_ee278_row2_col0" class="data row2 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row2_col1" class="data row2 col1" >1 <span style="color: grey">(14.3%) </span></td>
      <td id="T_ee278_row2_col2" class="data row2 col2" >3 <span style="color: grey">(3.3%) </span></td>
      <td id="T_ee278_row2_col3" class="data row2 col3" >3 <span style="color: grey">(5.8%) </span></td>
      <td id="T_ee278_row2_col4" class="data row2 col4" >1 <span style="color: grey">(6.7%) </span></td>
      <td id="T_ee278_row2_col5" class="data row2 col5" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row2_col6" class="data row2 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row2_col7" class="data row2 col7" >8 <span style="color: grey">(3.3%) </span></td>
    </tr>
    <tr>
      <th id="T_ee278_level0_row3" class="row_heading level0 row3" >Weiß nicht</th>
      <td id="T_ee278_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row3_col2" class="data row3 col2" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row3_col3" class="data row3 col3" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row3_col4" class="data row3 col4" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row3_col5" class="data row3 col5" >1 <span style="color: grey">(1.7%) </span></td>
      <td id="T_ee278_row3_col6" class="data row3 col6" ><span style="color: grey">0 </span></td>
      <td id="T_ee278_row3_col7" class="data row3 col7" >1 <span style="color: grey">(0.4%) </span></td>
    </tr>
    <tr>
      <th id="T_ee278_level0_row4" class="row_heading level0 row4" >Total</th>
      <td id="T_ee278_row4_col0" class="data row4 col0" >16 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row4_col1" class="data row4 col1" >7 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row4_col2" class="data row4 col2" >90 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row4_col3" class="data row4 col3" >52 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row4_col4" class="data row4 col4" >15 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row4_col5" class="data row4 col5" >59 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row4_col6" class="data row4 col6" >1 <span style="color: grey">(100.0%) </span></td>
      <td id="T_ee278_row4_col7" class="data row4 col7" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_63_0.svg)
    



<style type="text/css">
#T_f240b th {
  text-align: right;
}
#T_f240b td {
  text-align: right;
}
#T_f240b_row0_col0, #T_f240b_row0_col1, #T_f240b_row0_col2, #T_f240b_row0_col3, #T_f240b_row0_col4, #T_f240b_row1_col3, #T_f240b_row1_col4, #T_f240b_row1_col5, #T_f240b_row2_col3, #T_f240b_row3_col1, #T_f240b_row3_col4 {
  width: 10em;
  font-family: Courier;
}
#T_f240b_row0_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 8.9%, transparent 8.9%);
  font-family: Courier;
}
#T_f240b_row0_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.7%, transparent 1.7%);
  font-family: Courier;
}
#T_f240b_row1_col0, #T_f240b_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.9%, transparent 6.9%);
  font-family: Courier;
}
#T_f240b_row1_col1, #T_f240b_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.0%, transparent 3.0%);
  font-family: Courier;
}
#T_f240b_row1_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.5%, transparent 3.5%);
  font-family: Courier;
}
#T_f240b_row1_col6, #T_f240b_row3_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.5%, transparent 2.5%);
  font-family: Courier;
}
#T_f240b_row2_col2, #T_f240b_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.8%, transparent 1.8%);
  font-family: Courier;
}
#T_f240b_row2_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.0%, transparent 30.0%);
  font-family: Courier;
}
#T_f240b_row2_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 2.2%, transparent 2.2%);
  font-family: Courier;
}
#T_f240b_row2_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.8%, transparent 3.8%);
  font-family: Courier;
}
#T_f240b_row3_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.4%, transparent 3.4%);
  font-family: Courier;
}
#T_f240b_row3_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 3.1%, transparent 3.1%);
  font-family: Courier;
}
#T_f240b_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 6.7%, transparent 6.7%);
  font-family: Courier;
}
#T_f240b_row4_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.8%, transparent 82.8%);
  font-family: Courier;
}
#T_f240b_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 94.0%, transparent 94.0%);
  font-family: Courier;
}
#T_f240b_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 93.0%, transparent 93.0%);
  font-family: Courier;
}
#T_f240b_row4_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 96.9%, transparent 96.9%);
  font-family: Courier;
}
#T_f240b_row4_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 70.0%, transparent 70.0%);
  font-family: Courier;
}
#T_f240b_row4_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 82.2%, transparent 82.2%);
  font-family: Courier;
}
#T_f240b_row4_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 89.6%, transparent 89.6%);
  font-family: Courier;
}
#T_f240b_row5_col0, #T_f240b_row5_col1, #T_f240b_row5_col2, #T_f240b_row5_col3, #T_f240b_row5_col4, #T_f240b_row5_col5, #T_f240b_row5_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_f240b">
  <thead>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th id="T_f240b_level0_col0" class="col_heading level0 col0" >02 to 05 years</th>
      <th id="T_f240b_level0_col1" class="col_heading level0 col1" >06 to 09 years</th>
      <th id="T_f240b_level0_col2" class="col_heading level0 col2" >10 to 14 years</th>
      <th id="T_f240b_level0_col3" class="col_heading level0 col3" >15 to 18 years</th>
      <th id="T_f240b_level0_col4" class="col_heading level0 col4" >18+ years</th>
      <th id="T_f240b_level0_col5" class="col_heading level0 col5" ><NA></th>
      <th id="T_f240b_level0_col6" class="col_heading level0 col6" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.02] Group size</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_f240b_level0_row0" class="row_heading level0 row0" ><NA></th>
      <td id="T_f240b_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row0_col1" class="data row0 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row0_col2" class="data row0 col2" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row0_col3" class="data row0 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row0_col4" class="data row0 col4" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row0_col5" class="data row0 col5" >4 <span style="color: grey">(8.9%) </span></td>
      <td id="T_f240b_row0_col6" class="data row0 col6" >4 <span style="color: grey">(1.7%) </span></td>
    </tr>
    <tr>
      <th id="T_f240b_level0_row1" class="row_heading level0 row1" >Group 2-5</th>
      <td id="T_f240b_row1_col0" class="data row1 col0" >2 <span style="color: grey">(6.9%) </span></td>
      <td id="T_f240b_row1_col1" class="data row1 col1" >2 <span style="color: grey">(3.0%) </span></td>
      <td id="T_f240b_row1_col2" class="data row1 col2" >2 <span style="color: grey">(3.5%) </span></td>
      <td id="T_f240b_row1_col3" class="data row1 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row1_col4" class="data row1 col4" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row1_col5" class="data row1 col5" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row1_col6" class="data row1 col6" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_f240b_level0_row2" class="row_heading level0 row2" >Group 5 to 10</th>
      <td id="T_f240b_row2_col0" class="data row2 col0" >2 <span style="color: grey">(6.9%) </span></td>
      <td id="T_f240b_row2_col1" class="data row2 col1" >2 <span style="color: grey">(3.0%) </span></td>
      <td id="T_f240b_row2_col2" class="data row2 col2" >1 <span style="color: grey">(1.8%) </span></td>
      <td id="T_f240b_row2_col3" class="data row2 col3" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row2_col4" class="data row2 col4" >3 <span style="color: grey">(30.0%) </span></td>
      <td id="T_f240b_row2_col5" class="data row2 col5" >1 <span style="color: grey">(2.2%) </span></td>
      <td id="T_f240b_row2_col6" class="data row2 col6" >9 <span style="color: grey">(3.8%) </span></td>
    </tr>
    <tr>
      <th id="T_f240b_level0_row3" class="row_heading level0 row3" >Group over 10</th>
      <td id="T_f240b_row3_col0" class="data row3 col0" >1 <span style="color: grey">(3.4%) </span></td>
      <td id="T_f240b_row3_col1" class="data row3 col1" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row3_col2" class="data row3 col2" >1 <span style="color: grey">(1.8%) </span></td>
      <td id="T_f240b_row3_col3" class="data row3 col3" >1 <span style="color: grey">(3.1%) </span></td>
      <td id="T_f240b_row3_col4" class="data row3 col4" ><span style="color: grey">0 </span></td>
      <td id="T_f240b_row3_col5" class="data row3 col5" >3 <span style="color: grey">(6.7%) </span></td>
      <td id="T_f240b_row3_col6" class="data row3 col6" >6 <span style="color: grey">(2.5%) </span></td>
    </tr>
    <tr>
      <th id="T_f240b_level0_row4" class="row_heading level0 row4" >Individual</th>
      <td id="T_f240b_row4_col0" class="data row4 col0" >24 <span style="color: grey">(82.8%) </span></td>
      <td id="T_f240b_row4_col1" class="data row4 col1" >63 <span style="color: grey">(94.0%) </span></td>
      <td id="T_f240b_row4_col2" class="data row4 col2" >53 <span style="color: grey">(93.0%) </span></td>
      <td id="T_f240b_row4_col3" class="data row4 col3" >31 <span style="color: grey">(96.9%) </span></td>
      <td id="T_f240b_row4_col4" class="data row4 col4" >7 <span style="color: grey">(70.0%) </span></td>
      <td id="T_f240b_row4_col5" class="data row4 col5" >37 <span style="color: grey">(82.2%) </span></td>
      <td id="T_f240b_row4_col6" class="data row4 col6" >215 <span style="color: grey">(89.6%) </span></td>
    </tr>
    <tr>
      <th id="T_f240b_level0_row5" class="row_heading level0 row5" >Total</th>
      <td id="T_f240b_row5_col0" class="data row5 col0" >29 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f240b_row5_col1" class="data row5 col1" >67 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f240b_row5_col2" class="data row5 col2" >57 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f240b_row5_col3" class="data row5 col3" >32 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f240b_row5_col4" class="data row5 col4" >10 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f240b_row5_col5" class="data row5 col5" >45 <span style="color: grey">(100.0%) </span></td>
      <td id="T_f240b_row5_col6" class="data row5 col6" >240 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>




    
![svg](2_analyze_files/output_64_0.svg)
    



<style type="text/css">
#T_c8b8e th {
  text-align: right;
}
#T_c8b8e td {
  text-align: right;
}
#T_c8b8e_row0_col0, #T_c8b8e_row0_col5, #T_c8b8e_row3_col0, #T_c8b8e_row3_col6, #T_c8b8e_row4_col0, #T_c8b8e_row4_col3, #T_c8b8e_row4_col4, #T_c8b8e_row4_col5, #T_c8b8e_row4_col6, #T_c8b8e_row5_col5 {
  width: 10em;
  font-family: Courier;
}
#T_c8b8e_row0_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 14.8%, transparent 14.8%);
  font-family: Courier;
}
#T_c8b8e_row0_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 12.1%, transparent 12.1%);
  font-family: Courier;
}
#T_c8b8e_row0_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.7%, transparent 7.7%);
  font-family: Courier;
}
#T_c8b8e_row0_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 16.7%, transparent 16.7%);
  font-family: Courier;
}
#T_c8b8e_row0_col6, #T_c8b8e_row2_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 9.1%, transparent 9.1%);
  font-family: Courier;
}
#T_c8b8e_row0_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.5%, transparent 7.5%);
  font-family: Courier;
}
#T_c8b8e_row0_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.7%, transparent 11.7%);
  font-family: Courier;
}
#T_c8b8e_row1_col0, #T_c8b8e_row2_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.4%, transparent 15.4%);
  font-family: Courier;
}
#T_c8b8e_row1_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 31.3%, transparent 31.3%);
  font-family: Courier;
}
#T_c8b8e_row1_col2, #T_c8b8e_row5_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 24.2%, transparent 24.2%);
  font-family: Courier;
}
#T_c8b8e_row1_col3, #T_c8b8e_row3_col3, #T_c8b8e_row5_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 26.9%, transparent 26.9%);
  font-family: Courier;
}
#T_c8b8e_row1_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 38.9%, transparent 38.9%);
  font-family: Courier;
}
#T_c8b8e_row1_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 50.0%, transparent 50.0%);
  font-family: Courier;
}
#T_c8b8e_row1_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 63.6%, transparent 63.6%);
  font-family: Courier;
}
#T_c8b8e_row1_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 20.8%, transparent 20.8%);
  font-family: Courier;
}
#T_c8b8e_row1_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 29.3%, transparent 29.3%);
  font-family: Courier;
}
#T_c8b8e_row2_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.6%, transparent 22.6%);
  font-family: Courier;
}
#T_c8b8e_row2_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 27.3%, transparent 27.3%);
  font-family: Courier;
}
#T_c8b8e_row2_col3 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 11.5%, transparent 11.5%);
  font-family: Courier;
}
#T_c8b8e_row2_col4, #T_c8b8e_row5_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.4%, transparent 19.4%);
  font-family: Courier;
}
#T_c8b8e_row2_col5, #T_c8b8e_row3_col5 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 25.0%, transparent 25.0%);
  font-family: Courier;
}
#T_c8b8e_row2_col7, #T_c8b8e_row3_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 30.2%, transparent 30.2%);
  font-family: Courier;
}
#T_c8b8e_row2_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 22.8%, transparent 22.8%);
  font-family: Courier;
}
#T_c8b8e_row3_col1, #T_c8b8e_row4_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 7.8%, transparent 7.8%);
  font-family: Courier;
}
#T_c8b8e_row3_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 10.6%, transparent 10.6%);
  font-family: Courier;
}
#T_c8b8e_row3_col4 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.6%, transparent 5.6%);
  font-family: Courier;
}
#T_c8b8e_row3_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 13.0%, transparent 13.0%);
  font-family: Courier;
}
#T_c8b8e_row4_col2 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 1.5%, transparent 1.5%);
  font-family: Courier;
}
#T_c8b8e_row4_col7, #T_c8b8e_row5_col7 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 5.7%, transparent 5.7%);
  font-family: Courier;
}
#T_c8b8e_row4_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 4.0%, transparent 4.0%);
  font-family: Courier;
}
#T_c8b8e_row5_col0 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 69.2%, transparent 69.2%);
  font-family: Courier;
}
#T_c8b8e_row5_col1 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 15.7%, transparent 15.7%);
  font-family: Courier;
}
#T_c8b8e_row5_col6 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 18.2%, transparent 18.2%);
  font-family: Courier;
}
#T_c8b8e_row5_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 19.1%, transparent 19.1%);
  font-family: Courier;
}
#T_c8b8e_row6_col0, #T_c8b8e_row6_col1, #T_c8b8e_row6_col2, #T_c8b8e_row6_col3, #T_c8b8e_row6_col4, #T_c8b8e_row6_col5, #T_c8b8e_row6_col6, #T_c8b8e_row6_col7, #T_c8b8e_row6_col8 {
  width: 10em;
  background: linear-gradient(90deg, lightblue 100.0%, transparent 100.0%);
  font-family: Courier;
}
</style>
<table id="T_c8b8e">
  <thead>
    <tr>
      <th class="index_name level0" >[05.07] Main motor skill</th>
      <th id="T_c8b8e_level0_col0" class="col_heading level0 col0" ><NA></th>
      <th id="T_c8b8e_level0_col1" class="col_heading level0 col1" >Coordination</th>
      <th id="T_c8b8e_level0_col2" class="col_heading level0 col2" >Endurance</th>
      <th id="T_c8b8e_level0_col3" class="col_heading level0 col3" >Flexibility</th>
      <th id="T_c8b8e_level0_col4" class="col_heading level0 col4" >Full body</th>
      <th id="T_c8b8e_level0_col5" class="col_heading level0 col5" >Relaxation</th>
      <th id="T_c8b8e_level0_col6" class="col_heading level0 col6" >Speed</th>
      <th id="T_c8b8e_level0_col7" class="col_heading level0 col7" >Strength</th>
      <th id="T_c8b8e_level0_col8" class="col_heading level0 col8" >Total</th>
    </tr>
    <tr>
      <th class="index_name level0" >[05.03] Age</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_c8b8e_level0_row0" class="row_heading level0 row0" >02 to 05 years</th>
      <td id="T_c8b8e_row0_col0" class="data row0 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row0_col1" class="data row0 col1" >17 <span style="color: grey">(14.8%) </span></td>
      <td id="T_c8b8e_row0_col2" class="data row0 col2" >8 <span style="color: grey">(12.1%) </span></td>
      <td id="T_c8b8e_row0_col3" class="data row0 col3" >2 <span style="color: grey">(7.7%) </span></td>
      <td id="T_c8b8e_row0_col4" class="data row0 col4" >6 <span style="color: grey">(16.7%) </span></td>
      <td id="T_c8b8e_row0_col5" class="data row0 col5" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row0_col6" class="data row0 col6" >1 <span style="color: grey">(9.1%) </span></td>
      <td id="T_c8b8e_row0_col7" class="data row0 col7" >4 <span style="color: grey">(7.5%) </span></td>
      <td id="T_c8b8e_row0_col8" class="data row0 col8" >38 <span style="color: grey">(11.7%) </span></td>
    </tr>
    <tr>
      <th id="T_c8b8e_level0_row1" class="row_heading level0 row1" >06 to 09 years</th>
      <td id="T_c8b8e_row1_col0" class="data row1 col0" >2 <span style="color: grey">(15.4%) </span></td>
      <td id="T_c8b8e_row1_col1" class="data row1 col1" >36 <span style="color: grey">(31.3%) </span></td>
      <td id="T_c8b8e_row1_col2" class="data row1 col2" >16 <span style="color: grey">(24.2%) </span></td>
      <td id="T_c8b8e_row1_col3" class="data row1 col3" >7 <span style="color: grey">(26.9%) </span></td>
      <td id="T_c8b8e_row1_col4" class="data row1 col4" >14 <span style="color: grey">(38.9%) </span></td>
      <td id="T_c8b8e_row1_col5" class="data row1 col5" >2 <span style="color: grey">(50.0%) </span></td>
      <td id="T_c8b8e_row1_col6" class="data row1 col6" >7 <span style="color: grey">(63.6%) </span></td>
      <td id="T_c8b8e_row1_col7" class="data row1 col7" >11 <span style="color: grey">(20.8%) </span></td>
      <td id="T_c8b8e_row1_col8" class="data row1 col8" >95 <span style="color: grey">(29.3%) </span></td>
    </tr>
    <tr>
      <th id="T_c8b8e_level0_row2" class="row_heading level0 row2" >10 to 14 years</th>
      <td id="T_c8b8e_row2_col0" class="data row2 col0" >2 <span style="color: grey">(15.4%) </span></td>
      <td id="T_c8b8e_row2_col1" class="data row2 col1" >26 <span style="color: grey">(22.6%) </span></td>
      <td id="T_c8b8e_row2_col2" class="data row2 col2" >18 <span style="color: grey">(27.3%) </span></td>
      <td id="T_c8b8e_row2_col3" class="data row2 col3" >3 <span style="color: grey">(11.5%) </span></td>
      <td id="T_c8b8e_row2_col4" class="data row2 col4" >7 <span style="color: grey">(19.4%) </span></td>
      <td id="T_c8b8e_row2_col5" class="data row2 col5" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_c8b8e_row2_col6" class="data row2 col6" >1 <span style="color: grey">(9.1%) </span></td>
      <td id="T_c8b8e_row2_col7" class="data row2 col7" >16 <span style="color: grey">(30.2%) </span></td>
      <td id="T_c8b8e_row2_col8" class="data row2 col8" >74 <span style="color: grey">(22.8%) </span></td>
    </tr>
    <tr>
      <th id="T_c8b8e_level0_row3" class="row_heading level0 row3" >15 to 18 years</th>
      <td id="T_c8b8e_row3_col0" class="data row3 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row3_col1" class="data row3 col1" >9 <span style="color: grey">(7.8%) </span></td>
      <td id="T_c8b8e_row3_col2" class="data row3 col2" >7 <span style="color: grey">(10.6%) </span></td>
      <td id="T_c8b8e_row3_col3" class="data row3 col3" >7 <span style="color: grey">(26.9%) </span></td>
      <td id="T_c8b8e_row3_col4" class="data row3 col4" >2 <span style="color: grey">(5.6%) </span></td>
      <td id="T_c8b8e_row3_col5" class="data row3 col5" >1 <span style="color: grey">(25.0%) </span></td>
      <td id="T_c8b8e_row3_col6" class="data row3 col6" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row3_col7" class="data row3 col7" >16 <span style="color: grey">(30.2%) </span></td>
      <td id="T_c8b8e_row3_col8" class="data row3 col8" >42 <span style="color: grey">(13.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c8b8e_level0_row4" class="row_heading level0 row4" >18+ years</th>
      <td id="T_c8b8e_row4_col0" class="data row4 col0" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row4_col1" class="data row4 col1" >9 <span style="color: grey">(7.8%) </span></td>
      <td id="T_c8b8e_row4_col2" class="data row4 col2" >1 <span style="color: grey">(1.5%) </span></td>
      <td id="T_c8b8e_row4_col3" class="data row4 col3" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row4_col4" class="data row4 col4" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row4_col5" class="data row4 col5" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row4_col6" class="data row4 col6" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row4_col7" class="data row4 col7" >3 <span style="color: grey">(5.7%) </span></td>
      <td id="T_c8b8e_row4_col8" class="data row4 col8" >13 <span style="color: grey">(4.0%) </span></td>
    </tr>
    <tr>
      <th id="T_c8b8e_level0_row5" class="row_heading level0 row5" ><NA></th>
      <td id="T_c8b8e_row5_col0" class="data row5 col0" >9 <span style="color: grey">(69.2%) </span></td>
      <td id="T_c8b8e_row5_col1" class="data row5 col1" >18 <span style="color: grey">(15.7%) </span></td>
      <td id="T_c8b8e_row5_col2" class="data row5 col2" >16 <span style="color: grey">(24.2%) </span></td>
      <td id="T_c8b8e_row5_col3" class="data row5 col3" >7 <span style="color: grey">(26.9%) </span></td>
      <td id="T_c8b8e_row5_col4" class="data row5 col4" >7 <span style="color: grey">(19.4%) </span></td>
      <td id="T_c8b8e_row5_col5" class="data row5 col5" ><span style="color: grey">0 </span></td>
      <td id="T_c8b8e_row5_col6" class="data row5 col6" >2 <span style="color: grey">(18.2%) </span></td>
      <td id="T_c8b8e_row5_col7" class="data row5 col7" >3 <span style="color: grey">(5.7%) </span></td>
      <td id="T_c8b8e_row5_col8" class="data row5 col8" >62 <span style="color: grey">(19.1%) </span></td>
    </tr>
    <tr>
      <th id="T_c8b8e_level0_row6" class="row_heading level0 row6" >Total</th>
      <td id="T_c8b8e_row6_col0" class="data row6 col0" >13 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col1" class="data row6 col1" >115 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col2" class="data row6 col2" >66 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col3" class="data row6 col3" >26 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col4" class="data row6 col4" >36 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col5" class="data row6 col5" >4 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col6" class="data row6 col6" >11 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col7" class="data row6 col7" >53 <span style="color: grey">(100.0%) </span></td>
      <td id="T_c8b8e_row6_col8" class="data row6 col8" >324 <span style="color: grey">(100.0%) </span></td>
    </tr>
  </tbody>
</table>



## <a id='toc1_9_'></a>[2025-07-29 kombinationen](#toc0_)


    
![svg](2_analyze_files/output_67_0.svg)
    


    [02.02] Type                                                           
    Pain                                                                       71
    Übelkeit / Erbrechen                                                       30
    Circulatory problems                                                       23
    Pain|Weichteil-/Gewebeverletzung                                           17
    Pain|Superficial injuries                                                  10
    Weichteil-/Gewebeverletzung                                                 5
    Superficial injuries                                                        5
    Severe exhaustion                                                           4
    Pain|Schmerzhafter Spontaneous painful bowel movement                       4
    Übelkeit / Erbrechen|Circulatory problems                                   4
    Muscle soreness                                                             3
    Itching                                                                     3
    Coughing fit                                                                3
    Psychological stress reaction                                               3
    Pain|Muscle soreness                                                        3
    Enuresis                                                                    2
    Circulatory problems|Psychological stress reaction                          2
    Pain|Itching                                                                2
    Pain|Übelkeit / Erbrechen|Circulatory problems                              1
    Übelkeit / Erbrechen|Circulatory problems|Psychological stress reaction     1
    Pain|Superficial injuries|Weichteil-/Gewebeverletzung                       1
    Bone injuries                                                               1
    Pain|Psychological stress reaction                                          1
    Pain|Muscle cramps                                                          1
    Pain|Circulatory problems|Muscle soreness                                   1
    Pain|Circulatory problems|Muscle cramps                                     1
    Pain|Circulatory problems                                                   1
    Pain|Bone injuries                                                          1
    Nosebleed                                                                   1
    Coughing fit|Psychological stress reaction                                  1
    Circulatory problems|Severe exhaustion                                      1
    Circulatory problems|Muscle cramps                                          1
    Übelkeit / Erbrechen|Psychological stress reaction                          1
    Name: count, dtype: int64



    
![svg](2_analyze_files/output_68_0.svg)
    


    [02.03] Trigger                                         
    Physical strain|Medical therapy                             69
    Physical strain                                             41
    Sturzereignis                                               28
    Sturzereignis|Coordination problems                         15
    Coordination problems                                        8
    Kollision                                                    7
    Physical strain|Psychological strain                         4
    Physical strain|Coordination problems                        3
    Physical strain|Environmental conditions                     3
    Sturzereignis|Physical strain                                3
    Sturzereignis|Environmental conditions                       3
    Medical therapy                                              3
    Psychological strain                                         3
    Sturzereignis|Physical strain|Coordination problems          2
    Environmental conditions                                     2
    Psychological strain|Medical therapy                         2
    Sturzereignis|Psychological strain                           2
    Physical strain|Psychological strain|Medical therapy         2
    Physical strain|Kollision                                    2
    Psychological strain|Kollision                               1
    Coordination problems|Kollision                              1
    Physical strain|Medical therapy|Coordination problems        1
    Medical therapy|Kollision                                    1
    Sturzereignis|Medical therapy                                1
    Physical strain|Environmental conditions|Medical therapy     1
    Psychological strain|Coordination problems                   1
    Name: count, dtype: int64



    
![svg](2_analyze_files/output_69_0.svg)
    


    [03.14.01] Adaptations intensity                                        
    Exercise selection                                                          15
    Exercise selection|Intensity                                                15
    Intensity                                                                    6
    Communication strategy                                                       3
    Setting                                                                      3
    Exercise selection|Equipment                                                 2
    Exercise selection|Intensity|Equipment                                       2
    Equipment                                                                    1
    Equipment|Communication strategy                                             1
    Exercise selection|Intensity|Communication strategy                          1
    Exercise selection|Intensity|Motivationsstrategie|Communication strategy     1
    Weiteres                                                                     1
    Name: count, dtype: int64

