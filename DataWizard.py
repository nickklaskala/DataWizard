import sublime
import sublime_plugin
import csv
import re
import pprint

import json
from random import shuffle
from random import randrange
from collections import OrderedDict
import webbrowser



def runEdit(self, edit):
	text=''
	for sel in self.view.sel():
		text=text+self.view.substr(sel)
	if text=='':
		self.view.run_command("select_all")
	for region in self.view.sel():
		inData=self.view.substr(region)
		outData=self.format(inData)
		self.view.replace(edit, region, outData)



class dataGrid:

	text=''
	delimiter=''
	grid=[]
	sampleGrid=[]
	maxColWidth=[]
	sampleMaxColWidth=[]

	def __init__(self, text):
		self.text       = text.strip()
		self.delimiter  = self.getDelimiter(text)
		self.grid       = self.getGrid(self.text,self.delimiter)


	def getDelimiter(self,text):
		dct={'|':0}
		for i in set(text.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "().[]{}'):
				dct[i]=text.splitlines()[0].count(i)
		return (max(dct,key=dct.get))

	def getGrid(self,text,delimiter):
		grid=[[l.strip() if delimiter not in l.strip() else '"'+l.strip()+'"' for l in row] for row in csv.reader(text.splitlines(), delimiter=delimiter, quotechar='"')]
		self.maxColWidth=self.getMaxColumnWidth(grid)
		return grid


	def getMaxColumnWidth(self,grid):
		maxColWidth=[]
		for i in range(len(grid[0])):
			try:
				maxColWidth.append(max([len(r[i]) for r in grid]))
			except:
				maxColWidth.append(0)
		return maxColWidth

	def getSampleGrid(self):
		self.sampleGrid= list(self.grid)
		for c in range(len(self.grid[0])):
			col=[v[c] for v in self.grid[1:]]
			col=sorted(list(set(col)))
			col.extend(['' for i in self.grid[1:]])
			col=col[0:len(self.grid)-1]
			for v in range(0,len(col)):
				self.sampleGrid[v+1][c]=col[v]
		self.sampleMaxColWidth=self.getMaxColumnWidth(self.sampleGrid)

	def constructTextFromGrid(self,grid,delimiter,maxColWidth=None):#list of list ie grid
		if maxColWidth==None:
			rst='\n'.join([delimiter.join(i) for i in grid])
		else:
			rst=[]
			for i in range(len(grid)):
				record , temp = grid[i] , []

				for c in range(len(record)):
					temp.append(record[c]+' '*(maxColWidth[c]-len(record[c])))
				rst.append(delimiter.join(temp))
			rst='\n'.join(rst)
		return rst

	def pivotGrid(self):
		self.grid=[list(x) for x in zip(*self.grid)]
		self.maxColWidth=self.getMaxColumnWidth(self.grid)

	def popGrid(self):
		for i in range(len(self.grid)):
			temp=self.grid[i].pop(1)
			self.grid[i].append(temp)
		self.maxColWidth=self.getMaxColumnWidth(self.grid)






class datawiziardjustifycolumnsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		rst=a.constructTextFromGrid(a.grid,a.delimiter,a.maxColWidth)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardcollapsecolumnsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		rst=a.constructTextFromGrid(a.grid,a.delimiter)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardpivotCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.pivotGrid()
		rst=a.constructTextFromGrid(a.grid,a.delimiter)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardpivotjustifyCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.pivotGrid()
		rst=a.constructTextFromGrid(a.grid,a.delimiter,a.maxColWidth)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardpopCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.popGrid()
		rst=a.constructTextFromGrid(a.grid,a.delimiter,a.maxColWidth)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizarddistinctcharsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		text='\n'.join(sorted(list(set(text))))
		return text

	def run(self, edit):
		runEdit(self, edit)


class datawizardkeepdelimitersCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		newtext=''.join([c for c in text if c in ('\n',a.delimiter)])
		return newtext

	def run(self, edit):
		runEdit(self, edit)


class datawizardleadingzerosaddCommand(sublime_plugin.TextCommand):
	def format(self,text):

		data=text.split('\n')

		def replace_str_index(text,index=0,replacement=''):
			return '%s%s%s'%(text[:index],replacement,text[index+1:])

		for i in range(0,len(data)):
			for c in range(0,len(data[i])):
				if data[i][c]==' ':
					data[i]=replace_str_index(data[i],c,'0')
				else:
					break

		return '\n'.join(data)

	def run(self, edit):
		runEdit(self, edit)




class datawizardleadingzerosremoveCommand(sublime_plugin.TextCommand):
	def format(self,text):

		lines=text.split('\n')

		def replace_str_index(text,index=0,replacement=''):
			return '%s%s%s'%(text[:index],replacement,text[index+1:])

		for i in range(0,len(lines)):
			for c in range(0,len(lines[i])):
				if lines[i][c]=='0':
					lines[i]=replace_str_index(lines[i],c,' ')
				else:
					break

		return '\n'.join(lines)

	def run(self, edit):
		runEdit(self, edit)





class datawizardsqltolowercaserCommand(sublime_plugin.TextCommand):
	def format(self,text):
		lines=text.splitlines()
		words = ['row_number','else','then','string_agg','returns','bit','nolock','use','go','clustered','after','nocount','on','raiserror','instead','of','enable','trigger','upper','isnull','lower','rank','over','partition','when','datediff','cast','convert','add','constraint','alter','column','table','all','and','any','as','asc','backup','database','between','case','check','create','index','or','replace','view','procedure','unique','default','delete','desc','distinct','drop','exec','exists','foreign','key','from','full','outer','join','group','by','having','in','inner','insert','into','select','is','null','not','left','like','limit','order','primary','right','rownum','top','set','truncate','union','update','values','where','cross','date','datetime','execute','max','concat','for','fetch','next','close','open','varchar','int','object','declare','end','try','print','catch','with','begin','proc']


		lowercase = lambda x: x.group(1).lower()
		test = '\b({})\b'.format('|'.join(words))
		re_replace = re.compile(r'\b({})\b'.format('|'.join(words)),re.IGNORECASE)
		cflag=0
		for i in range(0,len(lines)):
			if '/*' in lines[i] and '*/' not in lines[i]:
				cflag=1
			if '*/' in lines[i]:
				cflag=0
			if cflag==1:
				continue
			temp=lines[i].split('--')
			temp[0]=re_replace.sub(lowercase, temp[0])
			lines[i]='--'.join(temp)
		return '\n'.join(lines)

	def run(self, edit):
		runEdit(self, edit)



class datawizardpyvartotextCommand(sublime_plugin.TextCommand):
	def format(self,text):
		lines=text.splitlines()

		for i in range(0,len(lines)):
			lines[i]=lines[i].replace('\\n','\n').replace('\\t','\t')

		return '\n'.join(lines)

	def run(self, edit):
		runEdit(self, edit)


class datawizardrandomshufflecolumnverticallyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		temp=[self.view.substr(selection) for selection in self.view.sel()]

		length=len(temp)
		locsAll=[i for i in range(0,length)]
		result=[]

		locsTemp=[l for l in locsAll]
		shuffle(locsTemp)
		for r in range(0,length):
			RandomLoc=locsTemp.pop()
			result.append(temp[RandomLoc])

		cnt=0
		for selection in self.view.sel():
			self.view.insert(edit, selection.begin(),result[cnt])
			cnt+=1
		for selection in self.view.sel():
			self.view.erase(edit, selection)




class datawizardrandomshufflecharverticallyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		temp=[self.view.substr(selection) for selection in self.view.sel()]


		width=len(temp[0])
		length=len(temp)
		locsAll=[i for i in range(0,length)]

		result=['' for i in temp]

		for i in range(0,width):
			locsTemp=[l for l in locsAll]
			shuffle(locsTemp)
			for r in range(0,length):
				RandomLoc=locsTemp.pop()
				result[r]=result[r]+temp[RandomLoc][i]


		cnt=0
		for selection in self.view.sel():
			self.view.insert(edit, selection.begin(),result[cnt])
			cnt+=1
		for selection in self.view.sel():
			self.view.erase(edit, selection)








class datawizardstatisticssamplejsonCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)

		stats={}
		for i in range(len(a.grid[0])):
			row=[row[i] for row in a.grid[1:]]
			stats[a.grid[0][i]]=[(row.count(val),val) for val in set(row)]

		json_object = json.dumps(stats, indent = 4)

		return json_object

	def run(self, edit):
		runEdit(self, edit)




class datawizardstatisticssampledelimitedCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.getSampleGrid()

		rst=a.constructTextFromGrid(a.sampleGrid,a.delimiter,a.sampleMaxColWidth)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardstatisticssampledelimiteddiffsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.pivotGrid()
		
		temp=[]
		for row in a.grid:
			if len(set(row[1:]))!=1:
				temp.append(row)
		a.grid=temp
		a.pivotGrid()
		a.getSampleGrid()
		a.pivotGrid()

		rst=a.constructTextFromGrid(a.grid,a.delimiter,a.maxColWidth)
		return rst

	def run(self, edit):
		runEdit(self, edit)



class datawizardconverttosqlinsertCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		headers=a.grid[0]

		sql='--drop table if exists #TempTable\ngo\n\ncreate table #TempTable\n(\n\trow_id int identity(1,1),\n'

		for index,columHeader in enumerate(headers):
			sql+='\t'+'['+columHeader+']'+' nvarchar('+str(a.maxColWidth[index])+'),\n'

		sql+=')\ngo\n\n'

		for index,row in enumerate(a.grid[1:]):

			if index%1000==0:
				sql+='\ninsert into #TempTable ('+','.join(['['+col+']' for col in headers])+')\nvalues '
			else:
				sql+=','

			sql+='('+','.join(["'"+f.replace("'","''")+"'" if f!='' else 'NULL' for f in row])+')\n'

		for index,row in enumerate(a.grid):
			if len(a.grid[index])!=len(a.grid[0]):
				sql+='\n{1} UNEQUAL NUMBER OF COLUMNS ON ORIGINAL DATASET LINE {0} PLEASE CORRECT AND RE-RUN {1}'.format(index+1,'*'*50)

		return sql

	def run(self, edit):
		runEdit(self, edit)




class datawizardopenchrometabCommand(sublime_plugin.TextCommand):
	def format(self,text):
		links=text.split()
		for link in links:
			webbrowser.open_new_tab(link)
		return text

	def run(self, edit):
		runEdit(self, edit)






class datawizardcrosstabCommand(sublime_plugin.TextCommand):
	def format(self,text):
		import pandas as pd #todo - currently not available
		text=text.strip()
		delimiter=getDelimiter(data)
		data=getDatagrid(text,delimiter)

		# Create the pandas DataFrame
		df = pd.DataFrame(data[1:], columns = data[0])

		return eval("print(pd.crosstab(df.{0},[{1}]))".format(data[0][0],','.join(['df.'+c for c in data[0][1:]])))

	def run(self, edit):
		runEdit(self, edit)

