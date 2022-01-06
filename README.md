# DataWizard
ST3/ST4 package for advanced data manipulation in delimited flat files (.csv, .psv, .tsv, .txt, .dat .etc). Supports auto detection of delimiters, Justification of delimited file, collapsing delimited files, pivoting delimited files, pop columns to end (cycling first column to end in pivoted data sets, see example), data masking(shuffle list, shuffle characters), data sampling, and converting datagrid to sql insert statements. This Package is especially helpful for ETL or any task that interfaces with delimited flat files in which you are constantly opening files and inspecting them. Allows for instant human readability and analysis.
Notes: it's strongly recommended to key bind the justify, collapse, pivot, and pop commands.
Recommended Key Bindings

    [
        { "keys": ["alt+\\"], "command": "datawizardjustifycolumns"},
        { "keys": ["alt+shift+\\"], "command": "datawizardcollapsecolumns"},
        { "keys": ["alt+shift+p"], "command": "datawizardpivotjustify"},
        { "keys": ["alt+p"], "command": "datawizardpivot"},
        { "keys": ["alt+o"], "command": "datawizardpop"}
    ]


Justify Columns (auto detects delimiters)
![Justify](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Justify.gif)

Collapse Columns
![Collapse](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Collapse.gif)

Pivot
![Pivot](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Pivot.gif)

Pivot and Justify
![PivotAndJustify](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/PivotAndJustify.gif)

Pop
![pop](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Pop.gif)

LeadingZerosAddRemove
![LeadingZerosAddRemove](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/LeadingZerosAddRemove.gif)

Shuffle Columns
![ShuffleColumnVertically](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/ShuffleColumnVertically.gif)

Shuffle Characters vertically within equal length strings
![ShuffleCharsVertically](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/ShuffleCharsVertically.gif)

Sample Delimited
![Sample](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/SampleDelimited.gif)

Sample JSON
![Sample](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Sample.gif)

Distinct Characters
![Sample](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/DistinctChars.gif)

SQL Inserts(batched in groups of 1000)
![PyVarToText](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/SQLInserts.gif)

Other misc function
Read Py Variables
![PyVarToText](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/PyVarToText.gif)
