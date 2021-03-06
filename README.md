# DataWizard
ST3/ST4 package for advanced data manipulation in delimited flat files (.csv, .psv, .tsv, .txt, .dat .etc). Supports auto detection of delimiters, Justification of delimited file, collapsing delimited files, pivoting delimited files, pop columns to end (cycling first column to end in pivoted data sets, see example), data masking(shuffle list, shuffle characters), data sampling, and converting datagrid to sql insert statements. This Package is especially helpful for ETL or any task that interfaces with delimited flat files in which you are constantly opening files and inspecting them. Allows for instant human readability and analysis.
Notes: it's strongly recommended to key bind the justify, collapse, pivot, and pop commands.
Recommended Key Bindings

	//recommended bindings
	// { "keys": ["alt+\\"],           "command": "datawizardjustifycolumns"},
	// { "keys": ["alt+shift+\\"],     "command": "datawizardcollapsecolumns"},
	// { "keys": ["alt+p"],            "command": "datawizardpivot"},
	// { "keys": ["alt+shift+p"],      "command": "datawizardpivotjustify"},
	// { "keys": ["alt+l"],            "command": "datawizardpop"},
	// { "keys": ["alt+s"],            "command": "datawizarddistinctcolumns"},
	// { "keys": ["alt+shift+s"],      "command": "datawizarddistinctcolumnformats"},
	// { "keys": ["alt+j"],            "command": "datawizarddistinctcolumnstojson"},
	// { "keys": ["alt+shift+j"],      "command": "datawizarddistinctcolumnformatstojson"},
	// { "keys": ["alt+i"],            "command": "datawizardstatisticssampledelimiteddiffs"},
	// { "keys": ["alt+q"],            "command": "datawizardconverttosqlinsertpostgres"},


	//not neccessary to map these but you can if wanted.
	//sense these are less common i really just use the context menu for these actions by right clicking in the canvas

	// {"keys":["alt+?"],"command":"datawizarddistinctchars"},
	// {"keys":["alt+?"],"command":"datawizardkeepdelimiters"},
	// {"keys":["alt+?"],"command":"datawizardleadingzerosadd"},
	// {"keys":["alt+?"],"command":"datawizardleadingzerosremove"},
	// {"keys":["alt+?"],"command":"datawizardsqltolowercaser"},
	// {"keys":["alt+?"],"command":"datawizardpyvartotext"},
	// {"keys":["alt+?"],"command":"datawizardrandomshufflecolumnvertically"},
	// {"keys":["alt+?"],"command":"datawizardrandomshufflecharvertically"},
	// {"keys":["alt+?"],"command":"datawizardconverttosqlinsert"},
	// {"keys":["alt+?"],"command":"datawizardopenchrometab"},
	// {"keys":["alt+?"],"command":"datawizardformatjson"},



Justify Collapse Columns (auto detects delimiters)
![Justify_Collapse](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Justify_Collapse.gif)

Pivot and Justify
![Pivot_Justify](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Pivot_Justify.gif)

Pop
![pop](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Pop.gif)

Distinct Columns
![Distinct_Columns](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Distinct_Columns.gif)

Distinct Columns into Json
![Distinct_Columns_JSON](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/Distinct_Columns_JSON.gif)

SQL Inserts(batched in groups of 1000) now supporting sql server and postgres syntax
![SQLInserts](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/SQLInserts.gif)

LeadingZerosAddRemove
![LeadingZerosAddRemove](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/LeadingZerosAddRemove.gif)

Shuffle Columns
![ShuffleColumnVertically](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/ShuffleColumnVertically.gif)

Shuffle Characters vertically within equal length strings
![ShuffleCharsVertically](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/ShuffleCharsVertically.gif)

Distinct Characters
![Sample](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/DistinctChars.gif)

Other misc function
Read Py Variables
![PyVarToText](https://raw.githubusercontent.com/nickklaskala/DataWizard/main/Media/PyVarToText.gif)
