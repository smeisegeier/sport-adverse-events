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
    🟣 shape: (195, 62) columns: ['Participant ID' '[01.01] CTCAE' '[01.02] Datum_AE'
     '[01.03] Sportassoziation' '[02.01] Datum_Aufnahme' '[02.02] Art'
     '[02.03] Auslöser' '[02.04] Körperteil' '[03.01.01] Schmerzen_Intensität'
     '[03.01.02] Schmerzen_Dauer' '[03.01] Schmerzen_Folge'
     '[03.02.01] Krankenhaus_Intensität' '[03.02.02] Krankenhaus_Dauer'
     '[03.02] Krankenhaus_Folge' '[03.03.01] Med_Weiterbehandlung_Intensität'
     '[03.03.02] Med_Weiterbehandlung_Dauer'
     '[03.03] Med_Weiterbehandlung_Folge' '[03.04] Therapieprotokoll_Folge'
     '[03.05] Lebensnotwendige_Intenvention_Folge'
     '[03.06.01] Pflege_Intensität' '[03.06.02] Pflege_Dauer'
     '[03.06] Pflege_Folge' '[03.07.01] Medikamente_Dauer'
     '[03.07.02] Medikamente_Intensität' '[03.07] Medikamente_Folge'
     '[03.08.01] Angst_Intensität' '[03.08.02] Angst_Dauer'
     '[03.08] Angst_Folge' '[03.09.01] Strukturanpassung_Intensität'
     '[03.09.02] Strukturanpassung_Dauer' '[03.09] Strukturanpassung_Folge'
     '[03.10.01] Freigabe_OK' '[03.10.02] Freigabe_Wer'
     '[03.10] Freigabe_Folge' '[03.11.01] PECH_Intensität'
     '[03.11.02] PECH_Folge' '[03.11] PECH_Folge'
     '[03.12.01] Observierung_Intensität' '[03.12.02] Observierung_Dauer'
     '[03.12] Observierung_Folge' '[03.13.01] Ende_vs_Pause'
     '[03.13.02] Pause_Intensität' '[03.13] Stoppung_Folge'
     '[03.14.01] Anpassung_Intensität' '[03.14.02] Anpassung_Dauer'
     '[03.15.01] Trost_Intensität' '[03.15.02] Trost_Dauer'
     '[03.15] Trost_Folge' '[03.16] Tod_Folge' '[03.17.01] ADL_Intensität'
     '[03.17.02] ADL_Dauer' '[03.17] ADL_Einschränkungen'
     '[03.18] Freitext_Folgen' '[05.01] Therapiephase' '[05.02] Gruppengröße'
     '[05.03] Alter' '[05.04] Online' '[05.05] Testung' '[05.06] Setting'
     '[05.07] Motorik' '[05.08] Hälfte' '[05.09] Trainingszustand']  
    🟣 duplicates: 0  
    🟣 uniques: [{Participant ID: 195 01.01 CTCAE: 3 01.02 Datum_AE: 2 01.03 Sportassoziation: 2 02.01  
    Datum_Aufnahme: 142 02.02 Art: 34 02.03 Auslöser: 25 02.04 Körperteil: 20 03.01.01  
    Schmerzen_Intensität: 9 03.01.02 Schmerzen_Dauer: 3 03.01 Schmerzen_Folge: 2 03.02.01  
    Krankenhaus_Intensität: 1 03.02.02 Krankenhaus_Dauer: 2 03.02 Krankenhaus_Folge:  
    3 03.03.01 Med_Weiterbehandlung_Intensität: 23 03.03.02 Med_Weiterbehandlung_Dauer:  
    4 03.03 Med_Weiterbehandlung_Folge: 3 03.04 Therapieprotokoll_Folge: 1 03.05 Lebensnotwendige_Intenvention_Folge:  
    1 03.06.01 Pflege_Intensität: 4 03.06.02 Pflege_Dauer: 3 03.06 Pflege_Folge: 2 03.07.01  
    Medikamente_Dauer: 3 03.07.02 Medikamente_Intensität: 3 03.07 Medikamente_Folge:  
    3 03.08.01 Angst_Intensität: 10 03.08.02 Angst_Dauer: 3 03.08 Angst_Folge: 2 03.09.01  
    Strukturanpassung_Intensität: 4 03.09.02 Strukturanpassung_Dauer: 2 03.09 Strukturanpassung_Folge:  
    2 03.10.01 Freigabe_OK: 5 03.10.02 Freigabe_Wer: 2 03.10 Freigabe_Folge: 2 03.11.01  
    PECH_Intensität: 7 03.11.02 PECH_Folge: 4 03.11 PECH_Folge: 2 03.12.01 Observierung_Intensität:  
    5 03.12.02 Observierung_Dauer: 3 03.12 Observierung_Folge: 3 03.13.01 Ende_vs_Pause:  
    2 03.13.02 Pause_Intensität: 3 03.13 Stoppung_Folge: 2 03.14.01 Anpassung_Intensität:  
    10 03.14.02 Anpassung_Dauer: 3 03.15.01 Trost_Intensität: 2 03.15.02 Trost_Dauer:  
    3 03.15 Trost_Folge: 2 03.16 Tod_Folge: 2 03.17.01 ADL_Intensität: 3 03.17.02 ADL_Dauer:  
    3 03.17 ADL_Einschränkungen: 3 03.18 Freitext_Folgen: 9 05.01 Therapiephase: 3 05.02  
    Gruppengröße: 4 05.03 Alter: 5 05.04 Online: 2 05.05 Testung: 2 05.06 Setting: 6 05.07  
    Motorik: 17 05.08 Hälfte: 2 05.09 Trainingszustand: 4}]  
    🟣 missings: [{Participant ID: 0 01.01 CTCAE: 17 01.02 Datum_AE: 0 01.03 Sportassoziation: 1 02.01  
    Datum_Aufnahme: 0 02.02 Art: 0 02.03 Auslöser: 0 02.04 Körperteil: 1 03.01.01 Schmerzen_Intensität:  
    123 03.01.02 Schmerzen_Dauer: 123 03.01 Schmerzen_Folge: 0 03.02.01 Krankenhaus_Intensität:  
    193 03.02.02 Krankenhaus_Dauer: 193 03.02 Krankenhaus_Folge: 0 03.03.01 Med_Weiterbehandlung_Intensität:  
    0 03.03.02 Med_Weiterbehandlung_Dauer: 0 03.03 Med_Weiterbehandlung_Folge: 0  
    03.04 Therapieprotokoll_Folge: 0 03.05 Lebensnotwendige_Intenvention_Folge:  
    2 03.06.01 Pflege_Intensität: 0 03.06.02 Pflege_Dauer: 191 03.06 Pflege_Folge:  
    0 03.07.01 Medikamente_Dauer: 0 03.07.02 Medikamente_Intensität: 190 03.07 Medikamente_Folge:  
    6 03.08.01 Angst_Intensität: 133 03.08.02 Angst_Dauer: 133 03.08 Angst_Folge: 1  
    03.09.01 Strukturanpassung_Intensität: 184 03.09.02 Strukturanpassung_Dauer:  
    184 03.09 Strukturanpassung_Folge: 1 03.10.01 Freigabe_OK: 138 03.10.02 Freigabe_Wer:  
    138 03.10 Freigabe_Folge: 1 03.11.01 PECH_Intensität: 0 03.11.02 PECH_Folge: 176  
    03.11 PECH_Folge: 1 03.12.01 Observierung_Intensität: 0 03.12.02 Observierung_Dauer:  
    189 03.12 Observierung_Folge: 0 03.13.01 Ende_vs_Pause: 20 03.13.02 Pause_Intensität:  
    120 03.13 Stoppung_Folge: 0 03.14.01 Anpassung_Intensität: 150 03.14.02 Anpassung_Dauer:  
    150 03.15.01 Trost_Intensität: 187 03.15.02 Trost_Dauer: 176 03.15 Trost_Folge:  
    0 03.16 Tod_Folge: 0 03.17.01 ADL_Intensität: 0 03.17.02 ADL_Dauer: 189 03.17 ADL_Einschränkungen:  
    3 03.18 Freitext_Folgen: 186 05.01 Therapiephase: 0 05.02 Gruppengröße: 4 05.03 Alter:  
    45 05.04 Online: 1 05.05 Testung: 1 05.06 Setting: 16 05.07 Motorik: 13 05.08 Hälfte:  
    47 05.09 Trainingszustand: 54}]  
    --- column uniques (all)  
    🟠 index [0, 1, 2, 3, 4,]  
    🟠 Participant ID(195|int64)   [3, 4, 5, 6, 7,]  
    🟠 [01.01] CTCAE(4|object)   ['1', '2', '3', '<NA>',]  
    🟠 [01.02] Datum_AE(2|object)   ['Das AE ist neu aufgetreten.', 'Das AE war vor dem Sport bereits vorhanden und hat sich verstärkt.',]  
    🟠 [01.03] Sportassoziation(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [02.01] Datum_Aufnahme(142|object)   ['2021-01-11', '2021-01-12', '2021-01-18', '2021-02-01', '2021-02-19',]  
    🟠 [02.02] Art(34|object)   ['Enuresis', 'Hustenanfall', 'Hustenanfall|Psychische Stressreaktion', 'Juckreiz',  
    'Knochenverletzungen',]  
    🟠 [02.03] Auslöser(25|object)   ['Koordinationsprobleme', 'Med. Therapie', 'Med. Therapie|Stoßen, Rempeln',  
    'Med. Therapie|Weitere', 'Physische Belastung',]  
    🟠 [02.04] Körperteil(21|object)   ['<NA>', 'Bauch', 'Bauch|Darm', 'Bauch|Steiß', 'Brust',]  
    🟠 [03.01.01] Schmerzen_Intensität(9|float64)   [1.0, 2.0, 3.0, 4.0, 5.0,]  
    🟠 [03.01.02] Schmerzen_Dauer(4|object)   ['<NA>', 'Schmerzen am gleichen Tag', 'Schmerzen bis zum Folgetag', 'Schmerzen, die mindestens 3 Tage anhielten',]  
    🟠 [03.01] Schmerzen_Folge(2|object)   ['Ja', 'Nein',]  
    🟠 [03.02.01] Krankenhaus_Intensität(2|object)   ['<NA>', 'Innerhalb der ersten 30 Minuten',]  
    🟠 [03.02.02] Krankenhaus_Dauer(3|object)   ['<NA>', 'mind. 1  Tag', 'mind. 3 Tage',]  
    🟠 [03.02] Krankenhaus_Folge(3|object)   ['No', 'U', 'Yes',]  
    🟠 [03.03.01] Med_Weiterbehandlung_Intensität(23|object)   ['-', 'Manuelle Untersuchung', 'Manuelle Untersuchung|Desinfektion', 'Manuelle Untersuchung|Invasive Untersuchung|Medikamentengabe oral|Medikamentengabe intravenös|Operation|PECH-Regel-Anwendung|Observierung',  
    'Manuelle Untersuchung|Invasive Untersuchung|Medikamentengabe oral|Medikamentengabe intravenös|PECH-Regel-Anwendung',]  
    🟠 [03.03.02] Med_Weiterbehandlung_Dauer(4|object)   ['-', 'Innerhalb der ersten 24 Stunden', 'Innerhalb der ersten Woche', 'nach der ersten Woche',]  
    🟠 [03.03] Med_Weiterbehandlung_Folge(3|object)   ['No', 'U', 'Yes',]  
    🟠 [03.04] Therapieprotokoll_Folge(1|object)   ['No',]  
    🟠 [03.05] Lebensnotwendige_Intenvention_Folge(2|object)   ['<NA>', 'No',]  
    🟠 [03.06.01] Pflege_Intensität(4|object)   ['-', 'Körperhygiene (bspw.  Unterstützung beim Waschen, Zähneputzen und Ankleiden',  
    'Mobilität (bspw. Unterstützung beim An- und Ausziehen und bei der Fortbewegung (Rollstuhl etc.|Psychosoziale Unterstützung (Emotionale Unterstützung und Verhaltensinterventionen',  
    'Psychosoziale Unterstützung (Emotionale Unterstützung und Verhaltensinterventionen',]  
    🟠 [03.06.02] Pflege_Dauer(4|object)   ['<NA>', 'max. 3 Stunden', 'über 1 Woche', 'über 2 Tage',]  
    🟠 [03.06] Pflege_Folge(2|object)   ['No', 'Yes',]  
    🟠 [03.07.01] Medikamente_Dauer(3|object)   ['-', 'Analgetika (Schmerzmittel', 'Analgetika (Schmerzmittel|Antikoagulanzien (blutgerinnungshemmende Mittel',]  
    🟠 [03.07.02] Medikamente_Intensität(4|object)   ['<NA>', 'länger als 4 Tage', 'max. 3 Tage', 'weiß nicht',]  
    🟠 [03.07] Medikamente_Folge(4|object)   ['<NA>', 'No', 'Yes', 'weiß nicht',]  
    🟠 [03.08.01] Angst_Intensität(11|object)   ['<NA>', 'bei dem Betroffenen selbst', 'bei dem Betroffenen selbst|bei den Eltern des Betroffenen',  
    'bei dem Betroffenen selbst|bei den Eltern des Betroffenen|im Behandlungsteam',  
    'bei dem Betroffenen selbst|bei der Bewegungsfachkraft',]  
    🟠 [03.08.02] Angst_Dauer(4|object)   ['<NA>', 'bis zum Ende der Woche', 'bis zum Ende des Monates', 'nur noch am gleichen Tag',]  
    🟠 [03.08] Angst_Folge(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.09.01] Strukturanpassung_Intensität(5|object)   ['<NA>', 'Einarbeitungsstruktur', 'Erhöhte Achtsamkeit', 'Regeländerung', 'Räumliche Anpassung',]  
    🟠 [03.09.02] Strukturanpassung_Dauer(3|object)   ['<NA>', 'bis zum Ende des Monates', 'für immer',]  
    🟠 [03.09] Strukturanpassung_Folge(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.10.01] Freigabe_OK(6|object)   ['<NA>', 'Eltern', 'Medizin', 'Pflege', 'Physiotherapie',]  
    🟠 [03.10.02] Freigabe_Wer(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.10] Freigabe_Folge(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [03.11.01] PECH_Intensität(7|object)   ['-', 'Eis', 'Eis|Hochlagern', 'Hochlagern', 'Pause',]  
    🟠 [03.11.02] PECH_Folge(5|object)   ['<NA>', 'max. 24 Stunden', 'max. 3 Stunden', 'max. 7 Tage', 'über 7 Tage',]  
    🟠 [03.11] PECH_Folge(3|object)   ['<NA>', 'Ja', 'Nein',]  
    🟠 [03.12.01] Observierung_Intensität(5|object)   ['-', 'Beobachtung spezifischer Symptome (bspw.  neurologische Beobachtungen',  
    'Dokumentation (sorgfältige  Beobachtungen des Gesundheitszustandes|Beobachtung spezifischer Symptome (bspw.  neurologische Beobachtungen',  
    'Dokumentation (sorgfältige  Beobachtungen des Gesundheitszustandes|Weitere',  
    'Kontinuierliche Überwachung (bspw. Intensivstationen|Dokumentation (sorgfältige  Beobachtungen des Gesundheitszustandes',]  
    🟠 [03.12.02] Observierung_Dauer(4|object)   ['<NA>', 'max. 24 Stunden', 'max. 7 Tage', 'über 7 Tage',]  
    🟠 [03.12] Observierung_Folge(3|object)   ['Ja', 'Nein', 'U',]  
    🟠 [03.13.01] Ende_vs_Pause(3|object)   ['<NA>', 'Abbruch', 'Pause',]  
    🟠 [03.13.02] Pause_Intensität(4|object)   ['<NA>', 'max. 1min', 'max. 5min', 'min. 10min',]  
    🟠 [03.13] Stoppung_Folge(2|object)   ['No', 'Yes',]  
    🟠 [03.14.01] Anpassung_Intensität(11|object)   ['<NA>', 'Intensität', 'Kommunikationsstrategie', 'Material', 'Material|Kommunikationsstrategie',]  
    🟠 [03.14.02] Anpassung_Dauer(4|object)   ['<NA>', 'ab jetzt für alle bewegungseinheiten mit allen Patient*innen',  
    'für die gesamte Therapiephase', 'nur für diese Einheit',]  
    🟠 [03.15.01] Trost_Intensität(3|object)   ['<NA>', 'ja', 'nein',]  
    🟠 [03.15.02] Trost_Dauer(4|object)   ['<NA>', 'länger als 10min', 'max, 10min', 'max. 1min',]  
    🟠 [03.15] Trost_Folge(2|object)   ['No', 'Yes',]  
    🟠 [03.16] Tod_Folge(2|object)   ['No', 'Yes',]  
    🟠 [03.17.01] ADL_Intensität(3|object)   ['-', 'Liegezeit erhöhte sich', 'Teilnahme an Programmen wie Kunsttherapie etc. war nicht möglich|Liegezeit erhöhte sich',]  
    🟠 [03.17.02] ADL_Dauer(4|object)   ['<NA>', 'mindestens 24 Stundne', 'mindestens 3 Tage', 'mindestens eine Woche',]  
    🟠 [03.17] ADL_Einschränkungen(4|object)   ['<NA>', 'Ja', 'Nein', 'U',]  
    🟠 [03.18] Freitext_Folgen(10|object)   ['<NA>', 'Absprache, das Pat. ab jetzt immer gleich bescheid gibt, wenn ein Unwohlsein aufkommt und wird sich nach der Therapie vorsichtiger bewegen',  
    'Aufklärungsarbeit bei dem Kind, das der Fall nichts mit dem Sport zu tun hatte; hat dann später auch wieder normal am Sport teilgenommen',  
    'Blutige Lippe, ist für ein paar Tagen geblieben  ', 'Gespräch mit PSD',]  
    🟠 [05.01] Therapiephase(3|object)   ['Akuttherapie', 'Dauertherapie', 'Nachsorge',]  
    🟠 [05.02] Gruppengröße(5|object)   ['<NA>', 'Einzel', 'Gruppe 2 bis 5 TN', 'Gruppe 5 bis 10 TN', 'Gruppe über 10 TN',]  
    🟠 [05.03] Alter(6|object)   ['02 bis 5 Jahre', '06 bis 9 Jahre', '10 bis 14 Jahre', '15 bis 18 Jahre',  
    '18+ Jahre',]  
    🟠 [05.04] Online(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [05.05] Testung(3|object)   ['<NA>', 'No', 'Yes',]  
    🟠 [05.06] Setting(7|object)   ['<NA>', 'Draußen', 'Klinikflur', 'Pat.-Zimmer', 'Turnhalle / Sportraum / Kraftraum',]  
    🟠 [05.07] Motorik(18|object)   ['<NA>', 'Ausdauer', 'Ausdauer|Beweglichkeit', 'Ausdauer|Beweglichkeit|Koordination',  
    'Ausdauer|Koordination',]  
    🟠 [05.08] Hälfte(3|object)   ['1. Hälfte', '2. Hälfte', '<NA>',]  
    🟠 [05.09] Trainingszustand(5|object)   ['<NA>', 'Durchschnittlich', 'Gut', 'Mäßig', 'Weiß nicht',]  
    --- column stats (numeric)  
    Participant ID -> min: 3 | lower: 3 | q25: 55.5 | median: 108.0 | mean: 106.856 | q75: 157.5 | upper: 208 | max: 208 | std: 59.675 | cv: 0.558 | sum: 20_837 | skew: -0.046 | kurto: -1.167  
    [03.01.01] Schmerzen_Intensität -> min: 1.0 | lower: 1.0 | q25: 2.0 | median: 4.0 | mean: 4.181 | q75: 6.0 | upper: 9.0 | max: 9.0 | std: 2.125 | cv: 0.508 | sum: 301.0 | skew: 0.338 | kurto: -1.076  



    
![png](2_analyze_files/output_4_1.png)
    



    
![png](2_analyze_files/output_4_2.png)
    



    
![png](2_analyze_files/output_4_3.png)
    


## <a id='toc1_2_'></a>[🕹️ interactive](#toc0_)

## <a id='toc1_3_'></a>[descriptive stats](#toc0_)


    
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
    



    
![png](2_analyze_files/output_11_29.png)
    



    
![png](2_analyze_files/output_11_30.png)
    



    
![png](2_analyze_files/output_11_31.png)
    



    
![png](2_analyze_files/output_11_32.png)
    



    
![png](2_analyze_files/output_11_33.png)
    



    
![png](2_analyze_files/output_11_34.png)
    


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
    



    
![png](2_analyze_files/output_42_0.png)
    



    
![png](2_analyze_files/output_43_0.png)
    

