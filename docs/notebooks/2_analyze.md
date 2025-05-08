# <a id='toc1_'></a>[analyze data](#toc0_)

**Table of contents**<a id='toc0_'></a>    
- [analyze data](#toc1_)    
  - [condensed data](#toc1_1_)    
  - [🕹️ interactive](#toc1_2_)    
  - [descriptive stats](#toc1_3_)    
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

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

    🐍 3.12.2 | 📦 pygwalker: 0.4.9.14 | 📦 pandas: 2.2.3 | 📦 numpy: 1.26.4 | 📦 duckdb: 1.2.1 | 📦 pandas-plots: 0.12.22 | 📦 connection_helper: 0.8.15


## <a id='toc1_1_'></a>[condensed data](#toc0_)
- defined columns have been transformed

    🔵 *** df: condensed ***  
    🟣 shape: (195, 34) columns: ['[01.01] CTCAE' '[01.02] Date' '[01.03] Exercise-related' '[02.02] Type'
     '[02.03] Trigger' '[02.04] Affected body parts' '[03.01] Pain'
     '[03.02]  With hospitalization' '[03.03] Medical follow-up treatment'
     '[03.04] With delayed therapy protocol'
     '[03.05] Life-saving intervention' '[03.06] Increased care needs'
     '[03.07] With medication administration' '[03.08.01] Affected person'
     '[03.08] Occurrence of fear and uncertainty'
     '[03.09] Structural adjustment' '[03.10.01] Approver'
     '[03.10.02] OK to proceed'
     '[03.10] Assessment of the situation by expertise'
     '[03.11] Application RICE rule (Rest, Ice, Compression, Elevation)'
     '[03.12] With observation' '[03.13.01] Stop or Break' '[03.13] Stop'
     '[03.14] Adaptations' '[03.16] Death' '[05.01] Therapy phase'
     '[05.02] Group size' '[05.03] Age' '[05.04] Online'
     '[05.05] As part of testing' '[05.06] Setting' '[05.07] Main motor skill'
     '[05.08] Time point' '[05.09] Training condition']  
    🟣 duplicates: 1  
    🟣 uniques: [{01.01 CTCAE: 3 01.02 Date: 2 01.03 Exercise-related: 2 02.02 Type: 34 02.03 Trigger:  
    25 02.04 Affected body parts: 20 03.01 Pain: 2 03.02  With hospitalization: 3 03.03 Medical  
    follow-up treatment: 3 03.04 With delayed therapy protocol: 1 03.05 Life-saving intervention:  
    1 03.06 Increased care needs: 2 03.07 With medication administration: 3 03.08.01 Affected  
    person: 10 03.08 Occurrence of fear and uncertainty: 2 03.09 Structural adjustment:  
    2 03.10.01 Approver: 5 03.10.02 OK to proceed: 2 03.10 Assessment of the situation by  
    expertise: 2 03.11 Application RICE rule (Rest Ice Compression Elevation): 2 03.12  
    With observation: 3 03.13.01 Stop or Break: 2 03.13 Stop: 2 03.14 Adaptations: 1 03.16  
    Death: 2 05.01 Therapy phase: 3 05.02 Group size: 4 05.03 Age: 5 05.04 Online: 2 05.05  
    As part of testing: 2 05.06 Setting: 6 05.07 Main motor skill: 17 05.08 Time point: 2 05.09  
    Training condition: 4}]  
    🟣 missings: [{01.01 CTCAE: 17 01.02 Date: 0 01.03 Exercise-related: 1 02.02 Type: 0 02.03 Trigger:  
    0 02.04 Affected body parts: 1 03.01 Pain: 0 03.02  With hospitalization: 0 03.03 Medical  
    follow-up treatment: 0 03.04 With delayed therapy protocol: 0 03.05 Life-saving intervention:  
    2 03.06 Increased care needs: 0 03.07 With medication administration: 6 03.08.01 Affected  
    person: 133 03.08 Occurrence of fear and uncertainty: 1 03.09 Structural adjustment:  
    1 03.10.01 Approver: 138 03.10.02 OK to proceed: 138 03.10 Assessment of the situation  
    by expertise: 1 03.11 Application RICE rule (Rest Ice Compression Elevation): 1 03.12  
    With observation: 0 03.13.01 Stop or Break: 20 03.13 Stop: 0 03.14 Adaptations: 0 03.16  
    Death: 0 05.01 Therapy phase: 0 05.02 Group size: 4 05.03 Age: 45 05.04 Online: 1 05.05  
    As part of testing: 1 05.06 Setting: 16 05.07 Main motor skill: 13 05.08 Time point: 47  
    05.09 Training condition: 54}]  
    --- column uniques (all)  
    🟠 index [0, 1, 2, 3, 4,]  
    🟠 [01.01] CTCAE(4|object)   ['1', '2', '3', '<NA>',]  
    🟠 [01.02] Date(2|object)   ['Already present', 'First occurrence',]  
    🟠 [01.03] Exercise-related(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [02.02] Type(34|object)   ['Bone injuries', 'Circulatory problems', 'Circulatory problems|Muscle cramps',  
    'Circulatory problems|Psychological stress reaction', 'Circulatory problems|Severe exhaustion',]  
    🟠 [02.03] Trigger(25|object)   ['Colliding', 'Coordination problems', 'Environmental conditions', 'Environmental conditions|Colliding',  
    'Fall event',]  
    🟠 [02.04] Affected body parts(21|object)   ['<NA>', 'Abdomen', 'Abdomen|Coccyx', 'Abdomen|Intestine', 'Back',]  
    🟠 [03.01] Pain(2|object)   ['Ja', 'Nein',]  
    🟠 [03.02]  With hospitalization(3|object)   ['No', 'U', 'Yes',]  
    🟠 [03.03] Medical follow-up treatment(3|object)   ['No', 'U', 'Yes',]  
    🟠 [03.04] With delayed therapy protocol(1|object)   ['No',]  
    🟠 [03.05] Life-saving intervention(2|object)   ['<NA>', 'No',]  
    🟠 [03.06] Increased care needs(2|object)   ['No', 'Yes',]  
    🟠 [03.07] With medication administration(4|object)   ['<NA>', 'No', 'Yes', 'weiß nicht',]  
    🟠 [03.08.01] Affected person(11|object)   ['<NA>', 'For affected individuals', 'For affected individuals|For parents des Betroffenen',  
    'For affected individuals|For parents des Betroffenen|In the treatment team',  
    'For affected individuals|For the excercise experts',]  
    🟠 [03.08] Occurrence of fear and uncertainty(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.09] Structural adjustment(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.10.01] Approver(6|object)   ['<NA>', 'Eltern', 'Medizin', 'Pflege', 'Physiotherapie',]  
    🟠 [03.10.02] OK to proceed(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.10] Assessment of the situation by expertise(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [03.11] Application RICE rule (Rest, Ice, Compression, Elevation)(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.12] With observation(3|object)   ['Ja', 'Nein', 'U',]  
    🟠 [03.13.01] Stop or Break(3|object)   ['<NA>', 'Break', 'Cessation',]  
    🟠 [03.13] Stop(2|object)   ['No', 'Yes',]  
    🟠 [03.14] Adaptations(1|object)   ['-',]  
    🟠 [03.16] Death(2|object)   ['No', 'Yes',]  
    🟠 [05.01] Therapy phase(3|object)   ['Acute therapy', 'Aftercare', 'Long-term therapy',]  
    🟠 [05.02] Group size(5|object)   ['<NA>', 'Group 2-5', 'Group 5 to 10', 'Group over 10', 'Individual',]  
    🟠 [05.03] Age(6|object)   ['10 to 14 years', '15 to 18 years', '6 to 9 years', '<5 years', '<NA>',]  
    🟠 [05.04] Online(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [05.05] As part of testing(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [05.06] Setting(7|object)   ['<NA>', 'At home (via telemedicine)', 'Gym', 'Hospital corridor', 'Outside',]  
    🟠 [05.07] Main motor skill(18|object)   ['<NA>', 'Coordination', 'Coordination|Speed', 'Coordination|Strength', 'Endurance',]  
    🟠 [05.08] Time point(3|object)   ['1. Time point', '2. Time point', '<NA>',]  
    🟠 [05.09] Training condition(5|object)   ['<NA>', 'Average', 'Good', 'Moderate', 'Weiß nicht',]  
    --- column stats (numeric)  



    
![png](2_analyze_files/output_4_1.png)
    



    
![png](2_analyze_files/output_4_2.png)
    



    
![png](2_analyze_files/output_4_3.png)
    


## <a id='toc1_2_'></a>[🕹️ interactive](#toc0_)

## <a id='toc1_3_'></a>[descriptive stats](#toc0_)




    ['[01.01] CTCAE',
     '[01.02] Date',
     '[01.03] Exercise-related',
     '[02.02] Type',
     '[02.03] Trigger',
     '[02.04] Affected body parts',
     '[03.02]  With hospitalization',
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
     '[05.01] Therapy phase',
     '[05.02] Group size',
     '[05.03] Age',
     '[05.04] Online',
     '[05.05] As part of testing',
     '[05.06] Setting',
     '[05.07] Main motor skill',
     '[05.08] Time point',
     '[05.09] Training condition']




    
![png](2_analyze_files/output_11_0.png)
    



    
![png](2_analyze_files/output_11_1.png)
    



    
![png](2_analyze_files/output_11_2.png)
    



    
![png](2_analyze_files/output_11_3.png)
    



    
![png](2_analyze_files/output_11_4.png)
    



    
![png](2_analyze_files/output_11_5.png)
    



    
![png](2_analyze_files/output_11_6.png)
    



    
![png](2_analyze_files/output_11_7.png)
    



    
![png](2_analyze_files/output_11_8.png)
    



    
![png](2_analyze_files/output_11_9.png)
    



    
![png](2_analyze_files/output_11_10.png)
    



    
![png](2_analyze_files/output_11_11.png)
    



    
![png](2_analyze_files/output_11_12.png)
    



    
![png](2_analyze_files/output_11_13.png)
    



    
![png](2_analyze_files/output_11_14.png)
    



    
![png](2_analyze_files/output_11_15.png)
    



    
![png](2_analyze_files/output_11_16.png)
    



    
![png](2_analyze_files/output_11_17.png)
    



    
![png](2_analyze_files/output_11_18.png)
    



    
![png](2_analyze_files/output_11_19.png)
    



    
![png](2_analyze_files/output_11_20.png)
    



    
![png](2_analyze_files/output_11_21.png)
    



    
![png](2_analyze_files/output_11_22.png)
    



    
![png](2_analyze_files/output_11_23.png)
    



    
![png](2_analyze_files/output_11_24.png)
    



    
![png](2_analyze_files/output_11_25.png)
    



    
![png](2_analyze_files/output_11_26.png)
    



    
![png](2_analyze_files/output_11_27.png)
    



    
![png](2_analyze_files/output_11_28.png)
    


## <a id='toc1_4_'></a>[slides](#toc0_)

### <a id='toc1_4_1_'></a>[slide 1](#toc0_)


    
![png](2_analyze_files/output_16_0.png)
    



    
![png](2_analyze_files/output_16_1.png)
    



    
![png](2_analyze_files/output_16_2.png)
    


### <a id='toc1_4_2_'></a>[slide 2](#toc0_)


    
![png](2_analyze_files/output_18_0.png)
    



    
![png](2_analyze_files/output_18_1.png)
    



    
![png](2_analyze_files/output_18_2.png)
    


### <a id='toc1_4_3_'></a>[slide 3](#toc0_)


    
![png](2_analyze_files/output_20_0.png)
    



    
![png](2_analyze_files/output_20_1.png)
    



    
![png](2_analyze_files/output_20_2.png)
    


### <a id='toc1_4_4_'></a>[slide 4](#toc0_)


    
![png](2_analyze_files/output_22_0.png)
    



    
![png](2_analyze_files/output_22_1.png)
    



    
![png](2_analyze_files/output_22_2.png)
    


### <a id='toc1_4_5_'></a>[slide 5](#toc0_)


    
![png](2_analyze_files/output_24_0.png)
    



    
![png](2_analyze_files/output_24_1.png)
    



    
![png](2_analyze_files/output_24_2.png)
    


### <a id='toc1_4_6_'></a>[slide 6](#toc0_)


    
![png](2_analyze_files/output_26_0.png)
    



    
![png](2_analyze_files/output_26_1.png)
    



    
![png](2_analyze_files/output_26_2.png)
    


### <a id='toc1_4_7_'></a>[slide 7](#toc0_)


    
![png](2_analyze_files/output_28_0.png)
    



    
![png](2_analyze_files/output_28_1.png)
    



    
![png](2_analyze_files/output_28_2.png)
    


### <a id='toc1_4_8_'></a>[slide 8](#toc0_)


    
![png](2_analyze_files/output_30_0.png)
    



    
![png](2_analyze_files/output_30_1.png)
    



    
![png](2_analyze_files/output_30_2.png)
    


### <a id='toc1_4_9_'></a>[slide 9](#toc0_)


    
![png](2_analyze_files/output_32_0.png)
    



    
![png](2_analyze_files/output_32_1.png)
    



    
![png](2_analyze_files/output_32_2.png)
    


### <a id='toc1_4_10_'></a>[slide 10](#toc0_)


    
![png](2_analyze_files/output_34_0.png)
    



    
![png](2_analyze_files/output_34_1.png)
    



    
![png](2_analyze_files/output_34_2.png)
    


### <a id='toc1_4_11_'></a>[bonus - ci](#toc0_)


    
![png](2_analyze_files/output_36_0.png)
    


## <a id='toc1_5_'></a>[2025-03-18](#toc0_)


    
![png](2_analyze_files/output_38_0.png)
    



    
![png](2_analyze_files/output_39_0.png)
    



    
![png](2_analyze_files/output_40_0.png)
    



    
![png](2_analyze_files/output_41_0.png)
    


    ❌ df must have exactly 2 or 3 columns



    
![png](2_analyze_files/output_43_0.png)
    

