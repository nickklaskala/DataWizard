# DataWizard
ST3/ST4 package for advance data manipulation of flat files. supports pivot datagird, pop columns to end (cycle), justify columns, collapse columns, data masking(suffle list, suffle characters in column vertically to preserve format string). This Package is especially helpful for ETL or any task that interfaces with delimited flat files in which you are constantly opening files and inspecting them. Allows for instant human readability and analysis.

Notes: it is strongly recommended to key bind the pivot, pop, justify, and collapse commands.
Recommended Key Bindings

    [
        { "keys": ["alt+\\"], "command": "datawiziardjustifycolumns"},
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

Random data
![Random](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Random.gif)

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

Other misc function
Read Py Variables
![PyVarToText](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/PyVarToText.gif)

SQL Inserts
![PyVarToText](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/SQLInserts.gif)