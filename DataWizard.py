import re
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
from csv import DictReader
import io
import itertools
# import datetime
import os
# from dateutil.tz import tzutc
import time

def getDelimiter(text):
	dct={'|':0}
	for i in set(text.splitlines()[0]):
		if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789''=:_- "().[]{}/\\'):
			dct[i]=text.splitlines()[0].count(i)
	print((max(dct,key=dct.get)))
	return (max(dct,key=dct.get))

def to_list(ob):
	return ob if isinstance(ob,list) else [ob]

def maske(element):
	if isinstance(element,list):
		return [maske(el) for el in element]
	elif isinstance(element,str):
		# newElement=re.sub('[0-9]', '9',re.sub('[a-z]', 'a',re.sub('[A-Z]', 'A', element)))
		newElement=''
		for char in element:
			if char in ('abcdefghijklmnopqrstuvwxqyz'):
				newElement+='a'
			elif char in ('ABCDEFGHIJKLMNOPQRSTUVWXQYZ'):
				newElement+='A'
			elif char in ('0123456789'):
				newElement+='9'
			else:
				newElement+=char
		return newElement

def runEdit(self, edit):
	# st = time.time()

	text=''
	for sel in self.view.sel():
		text=text+self.view.substr(sel)
	if text=='':
		self.view.run_command("select_all")
	for region in self.view.sel():
		inData=self.view.substr(region)
		outData=self.format(inData)
		self.view.replace(edit, region, outData)

	# et = time.time()
	# elapsed_time = et - st
	# print('Execution time:', elapsed_time, 'seconds')



def splitSpecial(line,delimiter,quotechar):

	maxPosition=len(line)-1
	outList=[]
	cell=''
	qouted=False

	def deqoute(cell,delimiter,qouted):
		if len(cell)>0 and cell[0]=='"' and cell[-1]=='"' and delimiter not in cell:
			cell=cell[1:-1]
		return cell


	for i,c in enumerate(line):
		if c!=delimiter and c!=quotechar and i !=maxPosition:
			cell+=c
			continue
		if i==maxPosition and c!=delimiter:
			cell+=c
			cell=deqoute(cell,delimiter,qouted)
			outList.append(cell)
			cell=''
			continue
		if i==maxPosition and c==delimiter:
			cell=deqoute(cell,delimiter,qouted)
			outList.append(cell)
			cell=''
			outList.append('')
			continue
		if c==quotechar and qouted==False and cell=='':
			qouted=True
			cell+=c
			continue
		if c==quotechar and i==maxPosition:
			cell+=c
			cell=deqoute(cell,delimiter,qouted)
			outList.append(cell)
			cell=''
			break
		if c==quotechar and qouted==True and i!=maxPosition and line[i+1]==delimiter:
			cell+=c
			qouted=False
			continue
		if c==delimiter and qouted==False:
			cell=deqoute(cell,delimiter,qouted)
			outList.append(cell)
			cell=''
			continue
		cell+=c

	return [cell.strip() for cell in outList]

def flatten_json(hunk):
	'''
	flattens json  and returns json as string
	or 
	flattens py-dictionary and returns pydict
	'''

	def _flatten(x, name=''):
		if type(x) is dict:
			for a in x:
				_flatten(x[a], name + a + '__')
		elif type(x) is list:
			i = 0
			for a in x:
				_flatten(a, name + str(i) + '__')
				i += 1
		else:
			rst[name[:-2]] = x


	hunk_type='unknown'
	if type(hunk) is str:
		hunk_type='json'
		hunk=json.loads(hunk)

	rst = {}
	_flatten(hunk)

	return json.dumps(rst) if hunk_type=='json' else rst 


class dataGrid:

	text=''
	delimiter=''
	grid=[]
	sampleGrid=[]
	maxColWidth=[]
	sampleMaxColWidth=[]

	def __init__(self, text):
		self.text       = re.sub("   +", "", text.strip('\n'))
		self.delimiter  = self.getDelimiter(self.text)
		self.grid       = self.getGrid(self.text,self.delimiter,'"')
		self.len        = len(self.grid)
		self.headers    = self.grid[0]
		# self.body       = self.grid[1:]

		for i in range(len(self.grid)):
			if len(self.grid[i])!=len(self.grid[0]):
				print('\n\n{1} UNEQUAL NUMBER OF COLUMNS ON LINE {0} IN FILE  PLEASE CORRECT AND RE-RUN {1}\n'.format(i,'*'*50))

	def getDelimiter(self,text):
		dct={'|':0}
		for i in set(text.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789\'=:_- "().[]{}/\\'):
				dct[i]=text.splitlines()[0].count(i)
		print((max(dct,key=dct.get)))
		return (max(dct,key=dct.get))

	def getGrid(self,text,delimiter,quotechar):
		# grid=[[col.strip().replace('"','""') if delimiter not in col.strip() else '"'+col.strip().replace('"','""')+'"' for col in row] for row in csv.reader(text.splitlines(), delimiter=delimiter, quotechar=quotechar)]
		grid=[[col.strip()  if delimiter not in col.strip() else '"'+col.strip().replace('"','""')+'"' for col in row] for row in csv.reader(text.splitlines(), delimiter=delimiter, quotechar=quotechar)]
		# grid=[[col  if delimiter not in col else '"'+col.strip().replace('"','""')+'"' for col in row] for row in csv.reader(text.splitlines(), delimiter=delimiter, quotechar=quotechar)]
		# maxColWidth=self.getMaxColumnWidth(grid)################################
		return grid

	def formatGrid(self):
		for row in self.grid:
			for i,col in enumerate(row):
				if col and self.delimiter in col and col[-1]!='"':
					row[i]='"'+col+'"'


	def getMaxColumnWidth(self,grid):
		maxColWidth=[]
		temp=[list(x) for x in zip(*self.grid)]
		for i in temp:
			maxColWidth.append(max([len(r) for r in i]))
		return maxColWidth

	def getSampleGrid(self,masked=False):
		data=[list(set(x)) for x in zip(*self.grid[1:])]
		if masked==True:
			data=maske(data)
			data=[set(i) for i in data]
		data=[[header]+sorted(data[i]) for i,header in enumerate(self.headers)]
		data=list(map(list, itertools.zip_longest(*data, fillvalue='')))
		self.sampleGrid=data
		# self.sampleMaxColWidth=self.getMaxColumnWidth(self.sampleGrid)

	def constructTextFromGrid(self,grid,delimiter,maxColWidth=None):#list of list ie grid
		if maxColWidth==None:
			rst='\n'.join([delimiter.join(i) for i in grid])
		else:
			maxColWidth=self.getMaxColumnWidth(grid)
			rst= '\n'.join([delimiter.join("{:<{width}}".format(col, width=maxColWidth[index]) for index, col in enumerate(row)) for row in grid])
		return rst

	def pivotGrid(self):
		self.grid=[list(x) for x in zip(*self.grid)]
		# self.maxColWidth=self.getMaxColumnWidth(self.grid)

	def popGrid(self,direction='left'):
		for i in range(len(self.grid)):
			if direction=='left':
				temp=self.grid[i].pop(1)
				self.grid[i].append(temp)
			else:
				temp=self.grid[i].pop(-1)
				self.grid[i].insert(1,temp)
		# self.maxColWidth=self.getMaxColumnWidth(self.grid)


class datawizardjustifycolumnsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		rst=a.constructTextFromGrid(a.grid,a.delimiter,True)
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
		rst=a.constructTextFromGrid(a.grid,a.delimiter,True)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardpopleftCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.popGrid()
		rst=a.constructTextFromGrid(a.grid,a.delimiter,True)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardpoprightCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.popGrid(direction='right')
		rst=a.constructTextFromGrid(a.grid,a.delimiter,True)
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
	def run(self,text):

		lines=[]
		for region in self.view.sel():
			lines.append(self.view.substr(region).strip(' '))

			maxlen = max(map(len, lines))
			new=[]
			for line in lines:
				new.append(line.zfill(maxlen))
			outData= new

		for region in self.view.sel():
			self.view.replace(text, region, outData.pop(0))






class datawizardleadingzerosremoveCommand(sublime_plugin.TextCommand):
	def format(self,text):

		lines=text.split('\n')

		def replace_str_index(text,index=0,replacement=''):
			return '%s%s%s'%(text[:index],replacement,text[index+1:])

		for y in range(0,len(lines)):
			for x in range(0,len(lines[y])):
				if lines[y][x]=='0':
					lines[y]=replace_str_index(lines[y],x,' ')
				else:
					break

		return '\n'.join(lines)

	def run(self, edit):
		runEdit(self, edit)


class datawizardlowercasesqlkeywordsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		lines=text.splitlines()
		#sql server
		# words = ['if','cascade','serial','integer','owner','to','grant','serial','integer','while','deallocate','row_number','else','then','string_agg','returns','bit','nolock','use','go','clustered','after','nocount','on','raiserror','instead','of','enable','trigger','upper','isnull','lower','rank','over','partition','when','datediff','cast','convert','add','constraint','alter','column','table','all','and','any','as','asc','backup','database','between','case','check','create','index','or','replace','view','procedure','unique','default','delete','desc','distinct','drop','exec','exists','foreign','key','from','full','outer','join','group','by','having','in','inner','insert','into','select','is','null','not','left','like','limit','order','primary','right','rownum','top','set','truncate','union','update','values','where','cross','date','datetime','execute','max','concat','for','fetch','next','close','open','varchar','int','object','declare','end','try','print','catch','with','begin','proc']
		#postgres
		words=['abort','abs','absent','absolute','access','according','acos','action','ada','add','admin','after','aggregate','all','allocate','also','alter','always','analyse','analyze','and','any','are','array','array_agg','array_max_cardinality','as','asc','asensitive','asin','assertion','assignment','asymmetric','at','atan','atomic','attach','attribute','attributes','authorization','avg','backward','base64','before','begin','begin_frame','begin_partition','bernoulli','between','bigint','binary','bit','bit_length','blob','blocked','bom','boolean','both','breadth','by','cache','call','called','cardinality','cascade','cascaded','case','cast','catalog','catalog_name','ceil','ceiling','chain','chaining','char','char_length','character','character_length','character_set_catalog','character_set_name','character_set_schema','characteristics','characters','check','checkpoint','class','class_origin','classifier','clob','close','cluster','coalesce','cobol','collate','collation','collation_catalog','collation_name','collation_schema','collect','column','column_name','columns','command_function','command_function_code','comment','comments','commit','committed','compression','concurrently','condition','condition_number','conditional','configuration','conflict','connect','connection','connection_name','constraint','constraint_catalog','constraint_name','constraint_schema','constraints','constructor','contains','content','continue','control','conversion','convert','copy','corr','corresponding','cos','cosh','cost','count','covar_pop','covar_samp','create','cross','cube','cume_dist','current','current_catalog','current_date','current_default_transform_group','current_path','current_role','current_row','current_schema','current_time','current_timestamp','current_transform_group_for_type','current_user','cursor','cursor_name','cycle','data','database','datalink','date','datetime_interval_code','datetime_interval_precision','day','db','deallocate','dec','decfloat','decimal','declare','default','defaults','deferrable','deferred','define','defined','definer','degree','delete','delimiter','delimiters','dense_rank','depends','depth','deref','derived','desc','describe','descriptor','detach','deterministic','diagnostics','dictionary','disable','discard','disconnect','dispatch','distinct','dlnewcopy','dlpreviouscopy','dlurlcomplete','dlurlcompleteonly','dlurlcompletewrite','dlurlpath','dlurlpathonly','dlurlpathwrite','dlurlscheme','dlurlserver','dlvalue','do','document','domain','double','drop','dynamic','dynamic_function','dynamic_function_code','each','element','else','empty','enable','encoding','encrypted','end','end_frame','end_partition','enforced','enum','equals','error','escape','event','every','except','exception','exclude','excluding','exclusive','exec','execute','exists','exp','explain','expression','extension','external','extract','false','family','fetch','file','filter','final','finalize','finish','first','first_value','flag','float','floor','following','for','force','foreign','format','fortran','forward','found','frame_row','free','freeze','from','fs','fulfill','full','function','functions','fusion','general','generated','get','global','go','goto','grant','granted','greatest','group','grouping','groups','handler','having','header','hex','hierarchy','hold','hour','id','identity','if','ignore','ilike','immediate','immediately','immutable','implementation','implicit','import','in','include','including','increment','indent','index','indexes','indicator','inherit','inherits','initial','initially','inline','inner','inout','input','insensitive','insert','instance','instantiable','instead','int','integer','integrity','intersect','intersection','interval','into','invoker','is','isnull','isolation','join','json','json_array','json_arrayagg','json_exists','json_object','json_objectagg','json_query','json_table','json_table_primitive','json_value','keep','key','key_member','key_type','keys','label','lag','language','large','last','last_value','lateral','lead','leading','leakproof','least','left','length','level','library','like','like_regex','limit','link','listagg','listen','ln','load','local','localtime','localtimestamp','location','locator','lock','locked','log','log10','logged','lower','map','mapping','match','match_number','match_recognize','matched','matches','materialized','max','maxvalue','measures','member','merge','message_length','message_octet_length','message_text','method','min','minute','minvalue','mod','mode','modifies','module','month','more','move','multiset','mumps','name','names','namespace','national','natural','nchar','nclob','nested','nesting','new','next','nfc','nfd','nfkc','nfkd','nil','no','none','normalize','normalized','not','nothing','notify','notnull','nowait','nth_value','ntile','nullif','nulls','number','numeric','object','occurrences_regex','octet_length','octets','of','off','offset','oids','old','omit','on','one','only','open','operator','option','options','or','order','ordering','ordinality','others','out','outer','output','over','overflow','overlaps','overlay','overriding','owned','owner','pad','parallel','parameter','parameter_mode','parameter_name','parameter_ordinal_position','parameter_specific_catalog','parameter_specific_name','parameter_specific_schema','parser','partial','partition','pascal','pass','passing','passthrough','password','past','path','pattern','per','percent','percent_rank','percentile_cont','percentile_disc','period','permission','permute','placing','plan','plans','pli','policy','portion','position','position_regex','power','precedes','preceding','precision','prepare','prepared','preserve','primary','prior','private','privileges','procedural','procedure','procedures','program','prune','ptf','public','publication','quote','quotes','range','rank','read','reads','real','reassign','recheck','recovery','recursive','ref','references','referencing','refresh','regr_avgx','regr_avgy','regr_count','regr_intercept','regr_r2','regr_slope','regr_sxx','regr_sxy','regr_syy','reindex','relative','release','rename','repeatable','replace','replica','requiring','reset','respect','restart','restore','restrict','result','return','returned_cardinality','returned_length','returned_octet_length','returned_sqlstate','returning','returns','revoke','right','role','rollback','rollup','routine','routine_catalog','routine_name','routine_schema','routines','row','row_count','row_number','rows','rule','running','savepoint','scalar','scale','schema','schema_name','schemas','scope','scope_catalog','scope_name','scope_schema','scroll','search','second','section','security','seek','select','selective','self','sensitive','sequence','sequences','serializable','server','server_name','session','session_user','set','setof','sets','share','show','similar','simple','sin','sinh','size','skip','smallint','snapshot','some','source','space','specific','specific_name','specifictype','sql','sqlcode','sqlerror','sqlexception','sqlstate','sqlwarning','sqrt','stable','standalone','start','state','statement','static','statistics','stddev_pop','stddev_samp','stdin','stdout','storage','stored','strict','string','strip','structure','style','subclass_origin','submultiset','subscription','subset','substring','substring_regex','succeeds','sum','support','symmetric','sysid','system','system_time','system_user','table','table_name','tables','tablesample','tablespace','tan','tanh','temp','template','temporary','text','then','through','ties','time','timestamp','timezone_hour','timezone_minute','to','token','top_level_count','trailing','transaction','transaction_active','transactions_committed','transactions_rolled_back','transform','transforms','translate','translate_regex','translation','treat','trigger','trigger_catalog','trigger_name','trigger_schema','trim','trim_array','true','truncate','trusted','type','types','uescape','unbounded','uncommitted','unconditional','under','unencrypted','union','unique','unknown','unlink','unlisten','unlogged','unmatched','unnamed','unnest','until','untyped','update','upper','uri','usage','user','user_defined_type_catalog','user_defined_type_code','user_defined_type_name','user_defined_type_schema','using','utf16','utf32','utf8','vacuum','valid','validate','validator','value','value_of','values','var_pop','var_samp','varbinary','varchar','variadic','varying','verbose','version','versioning','view','views','volatile','when','whenever','where','whitespace','width_bucket','window','with','within','without','work','wrapper','write','xml','xmlagg','xmlattributes','xmlbinary','xmlcast','xmlcomment','xmlconcat','xmldeclaration','xmldocument','xmlelement','xmlexists','xmlforest','xmliterate','xmlnamespaces','xmlparse','xmlpi','xmlquery','xmlroot','xmlschema','xmlserialize','xmltable','xmltext','xmlvalidate','year','yes','zone']

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



class datawizarduppercasesqlkeywordsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		lines=text.splitlines()
		#sql server
		# words = ['if','cascade','serial','integer','owner','to','grant','serial','integer','while','deallocate','row_number','else','then','string_agg','returns','bit','nolock','use','go','clustered','after','nocount','on','raiserror','instead','of','enable','trigger','upper','isnull','lower','rank','over','partition','when','datediff','cast','convert','add','constraint','alter','column','table','all','and','any','as','asc','backup','database','between','case','check','create','index','or','replace','view','procedure','unique','default','delete','desc','distinct','drop','exec','exists','foreign','key','from','full','outer','join','group','by','having','in','inner','insert','into','select','is','null','not','left','like','limit','order','primary','right','rownum','top','set','truncate','union','update','values','where','cross','date','datetime','execute','max','concat','for','fetch','next','close','open','varchar','int','object','declare','end','try','print','catch','with','begin','proc']
		#postgres
		words=['abort','abs','absent','absolute','access','according','acos','action','ada','add','admin','after','aggregate','all','allocate','also','alter','always','analyse','analyze','and','any','are','array','array_agg','array_max_cardinality','as','asc','asensitive','asin','assertion','assignment','asymmetric','at','atan','atomic','attach','attribute','attributes','authorization','avg','backward','base64','before','begin','begin_frame','begin_partition','bernoulli','between','bigint','binary','bit','bit_length','blob','blocked','bom','boolean','both','breadth','by','cache','call','called','cardinality','cascade','cascaded','case','cast','catalog','catalog_name','ceil','ceiling','chain','chaining','char','char_length','character','character_length','character_set_catalog','character_set_name','character_set_schema','characteristics','characters','check','checkpoint','class','class_origin','classifier','clob','close','cluster','coalesce','cobol','collate','collation','collation_catalog','collation_name','collation_schema','collect','column','column_name','columns','command_function','command_function_code','comment','comments','commit','committed','compression','concurrently','condition','condition_number','conditional','configuration','conflict','connect','connection','connection_name','constraint','constraint_catalog','constraint_name','constraint_schema','constraints','constructor','contains','content','continue','control','conversion','convert','copy','corr','corresponding','cos','cosh','cost','count','covar_pop','covar_samp','create','cross','cube','cume_dist','current','current_catalog','current_date','current_default_transform_group','current_path','current_role','current_row','current_schema','current_time','current_timestamp','current_transform_group_for_type','current_user','cursor','cursor_name','cycle','data','database','datalink','date','datetime_interval_code','datetime_interval_precision','day','db','deallocate','dec','decfloat','decimal','declare','default','defaults','deferrable','deferred','define','defined','definer','degree','delete','delimiter','delimiters','dense_rank','depends','depth','deref','derived','desc','describe','descriptor','detach','deterministic','diagnostics','dictionary','disable','discard','disconnect','dispatch','distinct','dlnewcopy','dlpreviouscopy','dlurlcomplete','dlurlcompleteonly','dlurlcompletewrite','dlurlpath','dlurlpathonly','dlurlpathwrite','dlurlscheme','dlurlserver','dlvalue','do','document','domain','double','drop','dynamic','dynamic_function','dynamic_function_code','each','element','else','empty','enable','encoding','encrypted','end','end_frame','end_partition','enforced','enum','equals','error','escape','event','every','except','exception','exclude','excluding','exclusive','exec','execute','exists','exp','explain','expression','extension','external','extract','false','family','fetch','file','filter','final','finalize','finish','first','first_value','flag','float','floor','following','for','force','foreign','format','fortran','forward','found','frame_row','free','freeze','from','fs','fulfill','full','function','functions','fusion','general','generated','get','global','go','goto','grant','granted','greatest','group','grouping','groups','handler','having','header','hex','hierarchy','hold','hour','id','identity','if','ignore','ilike','immediate','immediately','immutable','implementation','implicit','import','in','include','including','increment','indent','index','indexes','indicator','inherit','inherits','initial','initially','inline','inner','inout','input','insensitive','insert','instance','instantiable','instead','int','integer','integrity','intersect','intersection','interval','into','invoker','is','isnull','isolation','join','json','json_array','json_arrayagg','json_exists','json_object','json_objectagg','json_query','json_table','json_table_primitive','json_value','keep','key','key_member','key_type','keys','label','lag','language','large','last','last_value','lateral','lead','leading','leakproof','least','left','length','level','library','like','like_regex','limit','link','listagg','listen','ln','load','local','localtime','localtimestamp','location','locator','lock','locked','log','log10','logged','lower','map','mapping','match','match_number','match_recognize','matched','matches','materialized','max','maxvalue','measures','member','merge','message_length','message_octet_length','message_text','method','min','minute','minvalue','mod','mode','modifies','module','month','more','move','multiset','mumps','name','names','namespace','national','natural','nchar','nclob','nested','nesting','new','next','nfc','nfd','nfkc','nfkd','nil','no','none','normalize','normalized','not','nothing','notify','notnull','nowait','nth_value','ntile','nullif','nulls','number','numeric','object','occurrences_regex','octet_length','octets','of','off','offset','oids','old','omit','on','one','only','open','operator','option','options','or','order','ordering','ordinality','others','out','outer','output','over','overflow','overlaps','overlay','overriding','owned','owner','pad','parallel','parameter','parameter_mode','parameter_name','parameter_ordinal_position','parameter_specific_catalog','parameter_specific_name','parameter_specific_schema','parser','partial','partition','pascal','pass','passing','passthrough','password','past','path','pattern','per','percent','percent_rank','percentile_cont','percentile_disc','period','permission','permute','placing','plan','plans','pli','policy','portion','position','position_regex','power','precedes','preceding','precision','prepare','prepared','preserve','primary','prior','private','privileges','procedural','procedure','procedures','program','prune','ptf','public','publication','quote','quotes','range','rank','read','reads','real','reassign','recheck','recovery','recursive','ref','references','referencing','refresh','regr_avgx','regr_avgy','regr_count','regr_intercept','regr_r2','regr_slope','regr_sxx','regr_sxy','regr_syy','reindex','relative','release','rename','repeatable','replace','replica','requiring','reset','respect','restart','restore','restrict','result','return','returned_cardinality','returned_length','returned_octet_length','returned_sqlstate','returning','returns','revoke','right','role','rollback','rollup','routine','routine_catalog','routine_name','routine_schema','routines','row','row_count','row_number','rows','rule','running','savepoint','scalar','scale','schema','schema_name','schemas','scope','scope_catalog','scope_name','scope_schema','scroll','search','second','section','security','seek','select','selective','self','sensitive','sequence','sequences','serializable','server','server_name','session','session_user','set','setof','sets','share','show','similar','simple','sin','sinh','size','skip','smallint','snapshot','some','source','space','specific','specific_name','specifictype','sql','sqlcode','sqlerror','sqlexception','sqlstate','sqlwarning','sqrt','stable','standalone','start','state','statement','static','statistics','stddev_pop','stddev_samp','stdin','stdout','storage','stored','strict','string','strip','structure','style','subclass_origin','submultiset','subscription','subset','substring','substring_regex','succeeds','sum','support','symmetric','sysid','system','system_time','system_user','table','table_name','tables','tablesample','tablespace','tan','tanh','temp','template','temporary','text','then','through','ties','time','timestamp','timezone_hour','timezone_minute','to','token','top_level_count','trailing','transaction','transaction_active','transactions_committed','transactions_rolled_back','transform','transforms','translate','translate_regex','translation','treat','trigger','trigger_catalog','trigger_name','trigger_schema','trim','trim_array','true','truncate','trusted','type','types','uescape','unbounded','uncommitted','unconditional','under','unencrypted','union','unique','unknown','unlink','unlisten','unlogged','unmatched','unnamed','unnest','until','untyped','update','upper','uri','usage','user','user_defined_type_catalog','user_defined_type_code','user_defined_type_name','user_defined_type_schema','using','utf16','utf32','utf8','vacuum','valid','validate','validator','value','value_of','values','var_pop','var_samp','varbinary','varchar','variadic','varying','verbose','version','versioning','view','views','volatile','when','whenever','where','whitespace','width_bucket','window','with','within','without','work','wrapper','write','xml','xmlagg','xmlattributes','xmlbinary','xmlcast','xmlcomment','xmlconcat','xmldeclaration','xmldocument','xmlelement','xmlexists','xmlforest','xmliterate','xmlnamespaces','xmlparse','xmlpi','xmlquery','xmlroot','xmlschema','xmlserialize','xmltable','xmltext','xmlvalidate','year','yes','zone']

		uppercase = lambda x: x.group(1).upper()
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
			temp[0]=re_replace.sub(uppercase, temp[0])
			lines[i]='--'.join(temp)
		return '\n'.join(lines)

	def run(self, edit):
		runEdit(self, edit)


class datawizardpyvartotextCommand(sublime_plugin.TextCommand):
	def format(self,text):
		return text.replace('\\n','\n').replace('\\t','\t')

	def run(self, edit):
		runEdit(self, edit)


class datawizardshufflecolumnverticallyCommand(sublime_plugin.TextCommand):
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


class datawizardshufflecharverticallyCommand(sublime_plugin.TextCommand):
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


class datawizarddistinctcolumnstojsonCommand(sublime_plugin.TextCommand):
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


class datawizarddistinctcolumnformatstojsonCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.grid=[a.grid[0]]+[maske(i) for i in a.grid[1:]]

		stats={}
		for i in range(len(a.grid[0])):
			row=[row[i] for row in a.grid[1:]]
			stats[a.grid[0][i]]=[(row.count(val),val) for val in set(row)]

		json_object = json.dumps(stats, indent = 4)

		return json_object

	def run(self, edit):
		runEdit(self, edit)


class datawizarddistinctcolumnsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.getSampleGrid()

		rst=a.constructTextFromGrid(a.sampleGrid,a.delimiter,a.sampleMaxColWidth)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizarddistinctcolumnformatsCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.getSampleGrid(masked=True)

		rst=a.constructTextFromGrid(a.sampleGrid,a.delimiter,a.sampleMaxColWidth)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardstatisticsjsonCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.pivotGrid()

		def _numeric(input):
			input=input.strip('"').strip('$').replace(',','')
			try:
				rst=int(input) 
				return rst
			except:
				rst=float(input)
				return rst

		def _try(func ,input):
			try:
				rst=func(input)
				return rst
			except:
				return False


		def median(lst):
			lst.sort()
			mid = len(lst) // 2
			res = (lst[mid] + lst[~mid]) / 2
			return res
		from functools import reduce
		def mean(lst):
			return reduce(lambda a, b: a + b, lst) / len(lst)

		rst=OrderedDict()
		for col in a.grid:
			col_name=col.pop(0)
			rst[col_name]=OrderedDict() 

			tmp=[_numeric(n) for n in col if _try(_numeric,n)]
			rst[col_name]['min']=min(tmp) if tmp else min(col)
			rst[col_name]['max']=max(tmp) if tmp else max(col)
			try: 
				rst[col_name]['sum']=sum(tmp)
			except:
				pass
			try:
				rst[col_name]['mean']=mean(tmp)
			except:
				pass
			try:
				rst[col_name]['median']=median(tmp)
			except:
				pass

			
			try:
				rst[col_name]['percent_blank']=col.count('')/len(col)
			except:
				pass
			try:
				rst[col_name]['percent_distinct']=len(set(col))/len(col)
			except:
				pass
			try:
				rst[col_name]['percent_dupe']=(len(col)-len(set(col)))/len(col)
			except:
				pass
			col.sort()
			distinct_col=set(col)
			if len(distinct_col)<100:
				counts=[(val,col.count(val)) for val in distinct_col]
				temp=OrderedDict()
				for i,item in enumerate(sorted(counts, key=lambda item: item[1],reverse=True)):
					temp[item[0]]=item[1]
				rst[col_name]['distribution_top_100']=temp
			else:
				rst[col_name]['distribution_top_100']=None


		return json.dumps(rst, indent = 4,default='str')


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

		rst=a.constructTextFromGrid(a.grid,a.delimiter,True)
		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardconverttosqlinsertsqlserverCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.maxColWidth=a.getMaxColumnWidth(a.grid)
		headers=a.grid[0]
		def unqoute(value):
			try:
				if value[0]=='"' and value[-1]=='"' and a.delimiter in value:
					return value[1:-1]
				else:
					return value
			except:
				return value
		def formatvalue(value):
			return "'"+unqoute(value).replace("'","''")+"'" if value!='' else 'NULL' 

		table=[[formatvalue(f) for f in row] for row in a.grid[1:] ]
		table=[',('+','.join(row)+')\n' for row in table]

		filename=self.view.file_name() or 'temptable'
		table_name=os.path.basename(filename).replace('.csv','').replace('.txt','').replace('.CSV','').replace('.TXT','').replace('-','_').replace('/','_').replace('\\','_')

		sql='--drop table if exists #{table_name}\ngo\n\ncreate table #{table_name}\n(\n\trow_id int identity(1,1),\n'.format(table_name=table_name)

		for i in range(len(headers)):
			sql+='\t'+'['+headers[i]+']'+' nvarchar('+str(a.maxColWidth[i])+'),\n'
		sql+='\n)\n'
		insert='\n\ngo\n\ninsert into #{table_name} ('.format(table_name=table_name)+','.join(['['+i+']' for i in headers])+')\nvaluesx'

		if len(table)>1000:
			tableInsertLocs=[1000*i-1 for i in range(1,int(len(table)/1000)+1)]
			while tableInsertLocs:
				loc=tableInsertLocs.pop()
				table.insert(loc,insert)
		table.insert(0,insert)

		sql+=''.join(table)
		sql=sql.replace('valuesx,','values ')
		return sql

	def run(self, edit):
		runEdit(self, edit)


class datawizardconverttosqlinsertoracleCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		a.maxColWidth=a.getMaxColumnWidth(a.grid)
		headers=a.grid[0]

		def unqoute(value):
			try:
				if value[0]=='"' and value[-1]=='"' and a.delimiter in value:
					return value[1:-1]
				else:
					return value
			except:
				return value

		def formatvalue(value):
			return "'"+unqoute(value).replace("'","''")+"'" if value!='' else 'NULL' 

		table=[[formatvalue(val)+' as '+headers[i] for i,val in enumerate(row)] for row in a.grid[1:] ]
		table=['\t select '+','.join(row)+' from dual' for row in table]

		filename=self.view.file_name() or 'temptable'
		table_name=os.path.basename(filename).replace('.csv','').replace('.txt','').replace('.CSV','').replace('.TXT','').replace('-','_').replace('/','_').replace('\\','_')

		sql='--drop table {table_name};\n\ncreate global temporary table {table_name}\n(\n\t'.format(table_name=table_name)

		for i in range(len(headers)):
			sql+='\t,' if i !=0 else ' '
			sql+=headers[i]+' varchar2('+str(a.maxColWidth[i])+')\n'
		sql+=')on commit preserve rows;'


		insert='\n\n\ninsert into {table_name} ('.format(table_name=table_name)+','.join([i for i in headers])+')\n with tempdata as (<table>\n)\nselect * from tempdata;\n'

		chunks=[table[i:i + 1000] for i in range(0, len(table), 1000) ]
		for chunk in chunks:
			sql+=insert.replace('<table>','\n\tunion all '.join(chunk) )


		return sql

	def run(self, edit):
		runEdit(self, edit)


 

class datawizardconverttosqlinsertpostgresCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		
		headers=a.grid[0]
		def unqoute(value):
			try:
				if value[0]=='"' and value[-1]=='"' and a.delimiter in value:
					return value[1:-1]
				else:
					return value
			except:
				return value
		def formatvalue(value):
			return "'"+unqoute(value).replace("'","''")+"'" if value!='' else 'NULL' 

		table=[[formatvalue(f) for f in row] for row in a.grid[1:] ]
		table=[',('+','.join(row)+')\n' for row in table]
		filename=self.view.file_name() or 'temptable'
		table_name=os.path.basename(filename).replace('.csv','').replace('.txt','').replace('.CSV','').replace('.TXT','').replace('-','_').replace('/','_').replace('\\','_')

		sql='--drop table if exists {table_name};\n\ncreate table {table_name}\n(\n'.format(table_name=table_name)

		c={x:',' for x in range(1000)}
		c[0]=' '
		for i in range(len(headers)):
			sql+='\t'+c[i]+'"'+headers[i]+'"'+' text\n'
		sql+='\n);\n'
		insert='\n\n\n\n;insert into {table_name} ('.format(table_name=table_name)+','.join(['"'+i+'"' for i in headers])+')\nvaluesx'

		if len(table)>1000:
			tableInsertLocs=[1000*i-1 for i in range(1,int(len(table)/1000)+1)]
			while tableInsertLocs:
				loc=tableInsertLocs.pop()
				table.insert(loc,insert)
		table.insert(0,insert)

		sql+=''.join(table)
		sql=sql.replace('valuesx,','values ')
		return sql

	def run(self, edit):
		runEdit(self, edit)


class datawizardopenlinestochrometabsCommand(sublime_plugin.TextCommand):
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


class datawizardformatjsonCommand(sublime_plugin.TextCommand):
	from collections import OrderedDict
	def format(self,text):
		parsed = json.loads(text,object_pairs_hook=OrderedDict)
		formatted =json.dumps(parsed, indent=4, sort_keys=False)
		return formatted.replace('    ','\t')

	def run(self, edit):
		runEdit(self, edit)


class datawizardformatcsvtojsonCommand(sublime_plugin.TextCommand):
	def format(self,text):
		delimiter=getDelimiter(text)
		data=list(DictReader(text.splitlines(),delimiter=delimiter))

		data2=[]
		for key in data[0]:
			new=[]
			flag=True
			for d in data:
				if d[key]=='':
					temp=None
				else:
					try:
						temp=int(d[key])
					except:
						try:
							temp=float(d[key])
						except:
							flag=False
							break
				new.append(temp)

			if flag:
				for i,v in enumerate(new):
					data[i][key]=v

		formatted = json.dumps(data,default=str,indent=4).replace('": ""','": null')
		formatted_special = formatted.replace('\n    {','<nl>   {').replace('    ','').replace('\n','').replace('<nl>   {','\n    {').replace('}]','}\n]')
		return formatted_special

	def run(self, edit):
		runEdit(self, edit)


class datawizardformatcsvtonestedjsonCommand(sublime_plugin.TextCommand):
	def format(self,text):

		a=dataGrid(text)
		grid=a.grid
		nested_json = {}
		for row in grid:
			current_level = nested_json
			for i, column in enumerate(row[:-2]):
				if column not in current_level:
					current_level[column] = {}
				current_level = current_level[column]
			if row[-2] not in current_level:
				current_level[row[-2]] = []
			if row[-1] not in current_level[row[-2]]:
				current_level[row[-2]].append(row[-1])

		return json.dumps(nested_json, indent=4,sort_keys=True)

	def run(self, edit):
		runEdit(self, edit)


class datawizardjsontodictCommand(sublime_plugin.TextCommand):
	def format(self,text):
		json_data=json.loads(text)
		return str(json_data)

	def run(self, edit):
		runEdit(self, edit)


class datawizarddicttojsonCommand(sublime_plugin.TextCommand):
	def format(self,text):
		dict_data=eval(text)
		return json.dumps(dict_data,default=str,indent=4)

	def run(self, edit):
		runEdit(self, edit)


class datawizardjsontocsvCommand(sublime_plugin.TextCommand):
	def format(self,text):
		try:
			dict_list=to_list(json.loads(text))
		except:
			text=text.strip().strip('[').strip(']').strip()
			dict_list=[json.loads(line.strip(',')) for line in text.splitlines()]
		fieldnames = set()
		for d in dict_list:
			fieldnames.update(d.keys())

		# produce the csv file 
		mem_file = io.StringIO()
		wr = csv.DictWriter(mem_file, fieldnames)
		wr.writeheader()
		wr.writerows(dict_list)

		rst=mem_file.getvalue().replace('\r','')

		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardjsontocsvCommand(sublime_plugin.TextCommand):
	def format(self,text):
		try:
			dict_list=to_list(json.loads(text))
		except:
			text=text.strip().strip('[').strip(']').strip()
			dict_list=[json.loads(line.strip(',')) for line in text.splitlines()]

		fieldnames = []
		for d in dict_list:
			for key in d.keys():
				if key not in fieldnames:
					fieldnames.append(key)

		# produce the csv file 
		mem_file = io.StringIO()
		wr = csv.DictWriter(mem_file, fieldnames)
		wr.writeheader()
		wr.writerows(dict_list)

		rst=mem_file.getvalue().replace('\r','')

		return rst

	def run(self, edit):
		runEdit(self, edit)

class datawizardjsontocsvflattenedCommand(sublime_plugin.TextCommand):
	def format(self,text):
		try:
			dict_list=to_list(json.loads(text))
		except:
			text=text.strip().strip('[').strip(']').strip()
			dict_list=[json.loads(line.strip(',')) for line in text.splitlines()]

		dict_list=[flatten_json(d) for d in dict_list]

		fieldnames = []
		for d in dict_list:
			for key in d.keys():
				if key not in fieldnames:
					fieldnames.append(key)
		fieldnames.sort()


		# produce the csv file 
		mem_file = io.StringIO()
		wr = csv.DictWriter(mem_file, fieldnames)
		wr.writeheader()
		wr.writerows(dict_list)

		rst=mem_file.getvalue().replace('\r','')

		return rst

	def run(self, edit):
		runEdit(self, edit)


class datawizardcsvtotsvtopsvCommand(sublime_plugin.TextCommand):
	def format(self,text):
		a=dataGrid(text)
		delimiters=['|',',','\t']*2
		current_delimiter_index=delimiters.index(a.delimiter)
		a.delimiter=delimiters[current_delimiter_index+1]
		a.formatGrid()
		return a.constructTextFromGrid(a.grid,a.delimiter)

	def run(self, edit):
		runEdit(self, edit)



class datawizardflattenjsonCommand(sublime_plugin.TextCommand):
	def format(self,text):
		rst=flatten_json(text)
		return rst

	def run(self, edit):
		runEdit(self, edit)

class datawizardsortlinesbylengthCommand(sublime_plugin.TextCommand):
	def format(self,text):
		lines=[line.rstrip(' ') for line in text.splitlines()]
		lines.sort(key=len, reverse=True)
		return '\n'.join(lines)

	def run(self, edit):
		runEdit(self, edit)
