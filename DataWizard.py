import sublime
import sublime_plugin
import csv
import re
import pprint
import json
from random import shuffle
from random import randrange
from collections import OrderedDict






class datawiziardjustifycolumnsCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.strip()

		#get delimiter
		dct={}
		for i in set(data.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=data.splitlines()[0].count(i)
		delimiter=(max(dct,key=dct.get))

		# data=[i.split(delimiter) for i in data.splitlines() if i !='']
		data=[[l.strip() for l in row] for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]

		maxList=[]
		for i in range(len(data[0])):
			maxlen=0
			for r in range(len(data)):
				if len(data[r][i])>maxlen:
					maxlen=len(data[r][i])
			maxList.append(maxlen)


		rst=[]
		for i in range(len(data)):
			record=data[i]
			temp=[]
			for c in range(len(record)):
				temp.append(record[c]+' '*(maxList[c]-len(record[c])))


			rst.append(delimiter.join(temp))

		return '\n'.join(rst)

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)




class datawizardcollapsecolumnsCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.strip()

		fline=[i for i in data.splitlines()][0]
		dct={}
		for i in set(fline):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=fline.count(i)
		delimiter=(max(dct,key=dct.get))

		data=[[l.strip() for l in row] for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]

		maxList=[]
		for i in range(len(data)):
			data[i]=[n.strip() for n in data[i]]		
	


		return '\n'.join([delimiter.join(i) for i in data])

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardpivotCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.strip()

		fline=[i for i in data.splitlines()][0]
		dct={}
		for i in set(fline):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=fline.count(i)
		delimiter=(max(dct,key=dct.get))

		data=[[l.strip() for l in row] for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]

		data2=[]
		for i in range(len(data[0])):
			data2.append([data[0][i]])
			for n in range(len(data)):
				if n==0:
					continue
				data2[i].append(data[n][i])
		data=data2


		maxList=[]
		for i in range(len(data[0])):
			maxlen=0
			for r in range(len(data)):
				if len(data[r][i])>maxlen:
					maxlen=len(data[r][i])
			maxList.append(maxlen)


		rst=[]
		for i in range(len(data)):
			record=data[i]
			temp=[]
			for c in range(len(record)):
				temp.append(record[c]+''*(maxList[c]-len(record[c])))


			rst.append(delimiter.join(temp))

		return '\n'.join(rst)




	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardpivotjustifyCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.strip()

		fline=[i for i in data.splitlines()][0]
		dct={}
		for i in set(fline):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=fline.count(i)
		delimiter=(max(dct,key=dct.get))

		data=[[l.strip() for l in row] for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]

		data2=[]
		for i in range(len(data[0])):
			data2.append([data[0][i]])
			for n in range(len(data)):
				if n==0:
					continue
				data2[i].append(data[n][i])
		data=data2


		maxList=[]
		for i in range(len(data[0])):
			maxlen=0
			for r in range(len(data)):
				if len(data[r][i])>maxlen:
					maxlen=len(data[r][i])
			maxList.append(maxlen)


		rst=[]
		for i in range(len(data)):
			record=data[i]
			temp=[]
			for c in range(len(record)):
				temp.append(record[c]+' '*(maxList[c]-len(record[c])))


			rst.append(delimiter.join(temp))

		return '\n'.join(rst)




	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardpopCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.strip()

		fline=[i for i in data.splitlines()][0]
		dct={}
		for i in set(fline):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=fline.count(i)
		delimiter=(max(dct,key=dct.get))

		data=[row for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]

		#pop data index 0 to end
		for i in range(len(data)):
			temp=data[i].pop(1)
			data[i].append(temp)

		#measure spacing for new datagrid
		maxList=[]
		for i in range(len(data[0])):
			maxlen=0
			for r in range(len(data)):
				if len(data[r][i])>maxlen:
					maxlen=len(data[r][i])
			maxList.append(maxlen)

		#build new datagrid with proper spacing
		rst=[]
		for i in range(len(data)):
			oldLine=data[i]
			newLine=[]
			for c in range(len(oldLine)):
				newLine.append(oldLine[c]+' '*(maxList[c]-len(oldLine[c])))
			rst.append(delimiter.join(newLine))

		return '\n'.join(rst)




	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)




class datawizarddistinctcharsCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=''.join(set(data))
		data='\n'.join(sorted([i for i in data]))
		
		return data

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardkeepdelimitersCommand(sublime_plugin.TextCommand):
	def format(self,data):


		#get delimiter
		dct={}
		for i in set(data.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=data.splitlines()[0].count(i)
		delimiter=(max(dct,key=dct.get))


		new=''
		for i in range(len(data)):
			if data[i] in ('\n',delimiter):
				new+=data[i]


		return new

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)




class datawizardleadingzerosaddCommand(sublime_plugin.TextCommand):
	def format(self,data):
		
		data=data.split('\n')

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
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardleadingzerosremoveCommand(sublime_plugin.TextCommand):
	def format(self,data):
		
		data=data.split('\n')

		def replace_str_index(text,index=0,replacement=''):
			return '%s%s%s'%(text[:index],replacement,text[index+1:])
		
		for i in range(0,len(data)):
			for c in range(0,len(data[i])):
				if data[i][c]=='0':
					data[i]=replace_str_index(data[i],c,' ')
				else:
					break

		return '\n'.join(data)

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)




class datawizardsqltolowercaserCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.splitlines()
		words = ['string_agg','returns','bit','nolock','use','go','clustered','after','nocount','on','raiserror','instead','of','enable','trigger','upper','isnull','lower','rank','over','partition','when','datediff','cast','convert','add','constraint','alter','column','table','all','and','any','as','asc','backup','database','between','case','check','create','index','or','replace','view','procedure','unique','default','delete','desc','distinct','drop','exec','exists','foreign','key','from','full','outer','join','group','by','having','in','inner','insert','into','select','is','null','not','left','like','limit','order','primary','right','rownum','top','set','truncate','union','update','values','where','cross','date','datetime','execute','max','concat','for','fetch','next','close','open','varchar','int','object','declare','end','try','print','catch','with','begin','proc']
		
		
		lowercase = lambda x: x.group(1).lower()
		test = '\b({})\b'.format('|'.join(words))
		re_replace = re.compile(r'\b({})\b'.format('|'.join(words)),re.IGNORECASE)
		cflag=0
		for i in range(0,len(data)):
			if '/*' in data[i] and '*/' not in data[i]:
				cflag=1
			if '*/' in data[i]:
				cflag=0
			if cflag==1:
				continue
			temp=data[i].split('--')
			temp[0]=re_replace.sub(lowercase, temp[0])
			data[i]='--'.join(temp)
		return '\n'.join(data)

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)


class datawizardpyvartotextCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.splitlines()

		
		for i in range(0,len(data)):
			data[i]=data[i].replace('\\n','\n').replace('\\t','\t')
			
		return '\n'.join(data)

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)

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
	def format(self,data):
		data=data.strip()

		#get delimiter
		dct={}
		for i in set(data.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=data.splitlines()[0].count(i)
		delimiter=(max(dct,key=dct.get))

		# data=[i.split(delimiter) for i in data.splitlines() if i !='']
		data=[[l.strip() for l in row] for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]

		stats=OrderedDict()
		for i in range(0,len(data[0])):
			stats[data[0][i]]=list(set([x[i] for x in data[1:]]))


		json_object = json.dumps(stats, indent = 4)


		return json_object

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardstatisticssampledelimitedCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.strip()

		#get delimiter
		dct={}
		for i in set(data.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=data.splitlines()[0].count(i)
		delimiter=(max(dct,key=dct.get))

		# data=[i.split(delimiter) for i in data.splitlines() if i !='']
		data=[[l.strip() for l in row] for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]

		data2=data

		for c in range(0,len(data[0])):
			col=[v[c] for v in data[1:]]
			col=list(set(col))
			col.sort()
			col.extend(['' for i in data[1:]])
			col=col[0:len(data)-1]
			for v in range(0,len(col)):
				data2[v+1][c]=col[v]

		data=data2
		maxList=[]
		for i in range(len(data[0])):
			maxlen=0
			for r in range(len(data)):
				if len(data[r][i])>maxlen:
					maxlen=len(data[r][i])
			maxList.append(maxlen)

		rst=[]
		for i in range(len(data)):
			record=data[i]
			temp=[]
			for c in range(len(record)):
				temp.append(record[c]+' '*(maxList[c]-len(record[c])))

			rst.append(delimiter.join(temp))

		return '\n'.join(rst)

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)


class datawizardconverttosqlinsertCommand(sublime_plugin.TextCommand):
	def format(self,data):
		data=data.strip()

		#get delimiter
		dct={}
		for i in set(data.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "'):
				dct[i]=data.splitlines()[0].count(i)
		delimiter=(max(dct,key=dct.get))

		dest='#temptable'
		file=data.splitlines()

		table=[f for f in file[1:]]
		headers=file.pop(0).replace('\n','').split(delimiter)
		sql=''

		print(headers)
		for f in range(0,len(table)):
			values=table[f]
			values=[j if j!='' else 'NULL' for j in values.replace('\n','').split(delimiter)]
			values=[j.replace("'","''") for j in values]
			values=["'"+j+"'" if j !='NULL' else 'NULL' for j in values]
			table[f]=values
			sql+='('
			sql+=','.join(values)
			sql+=')\n'



		sql='--Drop Table if exists '+dest+'\ngo\n\ncreate table '+dest+'\n(\n\trow_id int identity(1,1),\n'
		for i in range(0,len(headers)):
			maxlen=0
			for r in range(0,len(table)):
				if len(table[r][i])>maxlen:
					maxlen=len(table[r][i])
			sql+='\t'+'['+headers[i]+']'+' nvarchar('+str(maxlen)+'),\n'

		sql+=')\ngo\n\n'


		for i in range(0,len(table)):

			if i%1000==0:
				sql+='\ninsert into '+dest+' ('

				for x in range(0,len(headers)):
					if x!=0:
						sql+=', '
					sql=sql+'['+headers[x]+']'

				sql+=')\nvalues '


			values=table[i]
			if i%1000!=0:
				sql+=','
			
			sql+='('
			sql+=','.join(values)
			sql+=')\n'

		return sql

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)