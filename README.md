# DataWizard
ST3 package for advance data manipulation of flat files. supports pivot datagird, pop columns to end (cycle), justify columns, collapse columns, data masking(suffle list, suffle characters in column vertically to preserve format string), generating random first name/last names/address/state codes/citys/phone numbers. This Package is especially helpful for ETL or any task that interfaces with delimited flat files in which you are constantly opening files and inspecting them. Allows for instant human readability and analysis.

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
![Justify](https://github.com/nickklaskala/DataWizard/blob/main/Media/Justify.gif)

Collapse Columns
![Collapse](https://github.com/nickklaskala/DataWizard/blob/main/Media/Collapse.gif)

Pivot
![Pivot](https://github.com/nickklaskala/DataWizard/blob/main/Media/Pivot.gif)

Pivot and Justify
![PivotAndJustify](https://github.com/nickklaskala/DataWizard/blob/main/Media/PivotAndJustify.gif)

Pop
![pop](https://github.com/nickklaskala/DataWizard/blob/main/Media/Pop.gif)

LeadingZerosAddRemove
![LeadingZerosAddRemove](https://github.com/nickklaskala/DataWizard/blob/main/Media/LeadingZerosAddRemove.gif)

Random data
![Random](https://github.com/nickklaskala/DataWizard/blob/main/Media/Random.gif)

Shuffle Columns
![ShuffleColumnVertically](https://github.com/nickklaskala/DataWizard/blob/main/Media/ShuffleColumnVertically.gif)

Shuffle Characters vertically within equal length strings
![ShuffleCharsVertically](https://github.com/nickklaskala/DataWizard/blob/main/Media/ShuffleCharsVertically.gif)

Sample File
![Sample](https://github.com/nickklaskala/DataWizard/blob/main/Media/Sample.gif)

Distinct Characters
![Sample](https://github.com/nickklaskala/DataWizard/blob/main/Media/DistinctChars.gif)

Other misc function
Read Py Variables
![PyVarToText](https://github.com/nickklaskala/DataWizard/blob/main/Media/PyVarToText.gif)

Recommended Key Bindings
[
	{ "keys": ["alt+\\"], "command": "datawiziardjustifycolumns"},
	{ "keys": ["alt+shift+\\"], "command": "datawizardcollapsecolumns"},
	{ "keys": ["alt+shift+p"], "command": "datawizardpivotjustify"},
	{ "keys": ["alt+p"], "command": "datawizardpivot"},
	{ "keys": ["alt+o"], "command": "datawizardpop"}
]