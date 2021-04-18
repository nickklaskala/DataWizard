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




class datawizardrandomaddressCommand(sublime_plugin.TextCommand):
	def format(self,data):
		addresses=['576 Buell Place','94866 Grayhawk Place','162 Rowland Pass','90839 Mendota Pass','07 Toban Junction','8 Grayhawk Parkway','76157 Glacier Hill Junction','90 Hayes Street','63833 Bobwhite Hill','22494 Susan Pass','3124 High Crossing Court','08 American Drive','69 Lukken Pass','20121 Mosinee Place','8844 Lotheville Park','603 Larry Lane','8187 Daystar Point','0 Sloan Avenue','2620 East Circle','1088 Spohn Place','0 Village Way','19194 Sloan Terrace','7030 Kim Place','7 Ridge Oak Road','673 Merchant Terrace','86 Monterey Alley','89 Fallview Pass','31313 Menomonie Road','07456 Larry Trail','687 Sage Plaza','96551 Spenser Avenue','7 Green Ridge Crossing','104 Rowland Junction','04 Larry Place','7801 Mcbride Point','674 Dwight Alley','573 Dayton Park','1 Stang Lane','26733 Fairview Road','45 Lillian Circle','3235 Park Meadow Pass','98 American Way','34 Holmberg Avenue','2206 Gateway Terrace','1 Atwood Pass','3 Declaration Parkway','5 Bonner Avenue','11710 Northridge Hill','40 Towne Street','7 Lakewood Gardens Park','949 Prentice Junction','848 Banding Place','1144 Arrowood Street','40 Troy Parkway','81211 Corscot Way','20263 School Circle','753 Delladonna Circle','17 Oakridge Center','0 Maryland Court','8739 Troy Drive','5 Farwell Crossing','7024 Delladonna Lane','1751 Bashford Avenue','09 Shoshone Terrace','377 Sutteridge Parkway','624 Montana Alley','0644 Londonderry Park','8046 Hovde Parkway','2 Longview Court','2 Raven Circle','9974 Pond Parkway','1 Lighthouse Bay Park','237 Memorial Circle','5490 Monica Avenue','69964 Dixon Parkway','69330 Dunning Trail','3 Acker Way','461 Golf Course Center','7 Toban Junction','597 Russell Avenue','5635 Summit Court','9 Darwin Lane','0384 Mccormick Way','77633 Union Drive','8913 Melrose Trail','2341 Johnson Lane','54 Dovetail Circle','9 Johnson Terrace','53 Rowland Place','257 Sherman Center','779 Northfield Junction','18214 Stang Terrace','62697 Miller Crossing','46 Dunning Avenue','289 Longview Lane','8618 Ryan Drive','299 Veith Lane','9 East Parkway','477 Ilene Lane','1 Kensington Center','6 Ryan Place','94605 Bartelt Center','8 Petterle Parkway','49418 Oneill Avenue','5 Twin Pines Court','4432 Nancy Drive','95 Holy Cross Parkway','77576 Truax Parkway','2 Mayer Trail','772 Reinke Parkway','00854 2nd Plaza','128 Northview Terrace','8 Continental Junction','70086 Lake View Alley','4607 Maywood Lane','9157 Mesta Circle','8 Lyons Center','42 Talisman Point','4821 Glendale Pass','9 Warner Alley','60 Parkside Center','1004 Washington Point','93 Eastwood Trail','850 Cardinal Way','5290 Paget Hill','967 Straubel Park','70194 Northridge Point','09720 Heffernan Plaza','1 Paget Pass','03256 Heath Point','8 Fulton Junction','51818 Loomis Pass','69053 Eggendart Hill','9 Maple Wood Circle','3526 Rutledge Road','54089 Oneill Center','6 Pearson Avenue','79 Algoma Hill','49 Browning Road','800 Riverside Lane','0776 Scott Hill','52998 Eggendart Avenue','2 Chive Street','6 Schmedeman Crossing','041 Forster Avenue','08618 Memorial Circle','7721 Autumn Leaf Plaza','5260 Russell Place','99965 Larry Street','59 Rowland Junction','3 Oxford Road','20004 Pankratz Point','2 Havey Drive','4 Spohn Avenue','2408 Columbus Pass','89 Shasta Point','0476 Crest Line Place','12 Corry Drive','00933 Magdeline Point','4421 Shoshone Street','48291 Merry Lane','167 Sommers Park','197 Hayes Road','53722 Eastlawn Parkway','8 Laurel Plaza','4 Nancy Terrace','60532 Sachs Street','384 Mockingbird Pass','55 Garrison Alley','849 Vahlen Court','1 Eggendart Drive','22622 Merchant Lane','77293 Eagle Crest Road','127 Claremont Pass','01284 Valley Edge Court','1 Esker Crossing','0356 Sutherland Center','25466 Karstens Way','4692 Rusk Street','21 Pawling Park','778 Warrior Way','538 Hoffman Parkway','7 Sullivan Alley','297 Grayhawk Lane','9417 Crownhardt Parkway','686 Barnett Park','568 Drewry Point','94476 Morning Hill','0739 Burning Wood Place','8 Elmside Road','94 Knutson Hill','82 Comanche Street','668 Main Street','94918 Forest Dale Place','1 Blaine Alley','9615 Rusk Place','304 Prairieview Alley','3 Bay Circle','624 Oakridge Circle','3 Farwell Crossing','421 Artisan Way','0535 Brown Junction','67 Sherman Alley','86460 Pennsylvania Terrace','3654 Paget Point','610 Sachs Alley','14 Brown Crossing','27 Bluestem Way','8 Dakota Pass','1756 Springview Point','4210 Amoth Place','42 Mallory Lane','59 Southridge Drive','51 Carpenter Pass','821 Jana Trail','38742 Portage Place','8 Garrison Trail','7 Meadow Valley Way','4 Havey Plaza','7839 Anniversary Street','20 Bowman Street','95118 Pepper Wood Crossing','71 Autumn Leaf Avenue','5 Sachtjen Drive','36685 Fulton Court','9 Jana Drive','76921 Merchant Street','19413 Crescent Oaks Trail','55642 Hauk Street','8461 Mendota Trail','774 Havey Pass','2 Grayhawk Center','366 Dorton Plaza','8 Buhler Park','591 Stuart Drive','9385 Londonderry Crossing','8907 Nelson Court','3 Northfield Way','78 Clove Lane','5 Blaine Way','65108 Maple Wood Terrace','25 Northland Point','9422 Eagle Crest Pass','0303 East Terrace','9641 Waywood Center','0 Boyd Park','1 Lunder Alley','92705 Towne Way','2 Center Crossing','5058 Forster Plaza','7 Jana Avenue','130 Novick Avenue','68 Eggendart Terrace','6 Milwaukee Trail','430 Mockingbird Lane','310 Roxbury Alley','678 Sherman Place','3 Bay Parkway','30 Heath Point','3 Maple Center','90 Walton Lane','44181 Mitchell Circle','68976 Riverside Plaza','70 Birchwood Street','8 Hooker Parkway','0 Pine View Lane','50955 Gale Parkway','938 Bartillon Place','72 Veith Avenue','14 Fuller Way','62610 Brown Parkway','5187 Dapin Place','03769 Roxbury Point','63937 Bartelt Crossing','2 Hooker Circle','0 Ludington Place','273 Farragut Street','7664 Evergreen Lane','01 Mendota Center','35 Doe Crossing Center','995 Troy Drive','574 Delaware Way','92103 Valley Edge Drive','09846 Vernon Road','6305 Lindbergh Plaza','7238 Merchant Circle','846 Linden Alley','2 John Wall Crossing','99698 Almo Crossing','0 Sachs Crossing','22410 Glendale Place','4955 Dexter Crossing','78 Maryland Terrace','18 Onsgard Point','3 Texas Point','82872 Manley Road','88471 Armistice Crossing','23 Brickson Park Center','5 American Circle','1438 Myrtle Avenue','862 Delladonna Point','95 Becker Center','9629 Sunbrook Road','508 Colorado Terrace','1573 Lotheville Park','3101 Merchant Alley','8 Barnett Alley','44 Sheridan Street','0 Grim Pass','6658 Union Court','2581 Hintze Road','9 Surrey Hill','96 Sheridan Pass','0 Oak Valley Parkway','3151 Tennessee Parkway','7 Sheridan Parkway','8845 Donald Hill','21 Oak Pass','0 Steensland Crossing','64171 Nelson Hill','04615 Anniversary Way','84 Buell Point','19043 Barby Way','7070 Roxbury Avenue','04 Coolidge Court','0 Center Center','73 Sunfield Pass','3782 Schmedeman Parkway','55 Tennessee Terrace','10795 Lukken Lane','25359 Calypso Road','31 Dwight Place','29 Sullivan Plaza','59462 Northfield Circle','59476 Elmside Place','1597 Hayes Place','1814 Clyde Gallagher Way','445 Pankratz Lane','59 Troy Drive','2796 Kensington Park','775 Pearson Lane','9 Jackson Crossing','72496 Eagan Circle','75 Hoard Parkway','62 Sauthoff Park','8 Village Place','9 Kim Drive','40635 Starling Way','497 Sachtjen Pass','04806 Raven Terrace','7605 Almo Parkway','5 Anthes Avenue','74082 Glendale Road','5430 Grasskamp Court','32 Jenifer Park','70 Clyde Gallagher Point','6393 Vera Park','18 Hooker Hill','5249 Meadow Vale Drive','436 Moose Drive','2596 David Avenue','154 Weeping Birch Park','58 Thierer Trail','13269 Glendale Lane','6230 Lotheville Parkway','63 Oxford Court','98938 Darwin Crossing','09966 Autumn Leaf Park','59615 Hanson Street','98344 Hoard Point','1 Eastlawn Circle','33771 Atwood Park','93714 International Junction','99712 Superior Place','001 Commercial Junction','605 Lakewood Gardens Terrace','2901 Novick Way','294 Gerald Street','73 New Castle Point','53 Tennyson Parkway','499 Manitowish Parkway','01 Marcy Drive','62 Nobel Place','4 Starling Pass','8 Vahlen Trail','0745 Menomonie Road','7630 Bartillon Lane','70 Packers Road','84 Crowley Trail','3 Manufacturers Circle','1 Elka Pass','03566 Hollow Ridge Circle','933 Trailsway Avenue','79 Reindahl Terrace','092 Moland Pass','388 Vahlen Hill','04 Cascade Center','032 Blue Bill Park Drive','69 Thierer Drive','1424 Union Circle','08 Green Parkway','92 Delaware Alley','9 Trailsway Point','0 4th Pass','407 Fair Oaks Center','5056 Washington Court','7758 Corscot Pass','14 Red Cloud Junction','48204 Eastwood Center','7 Springs Lane','51 Lindbergh Circle','36655 Fremont Plaza','9 Division Plaza','614 Brown Crossing','1178 Birchwood Point','58 Oneill Circle','200 Loeprich Lane','46 Riverside Terrace','36442 Cambridge Way','087 Leroy Terrace','020 Golf Course Hill','4 Messerschmidt Plaza','26 Karstens Alley','29238 Kim Avenue','0634 Vidon Point','323 2nd Pass','74840 Graceland Road','4840 Jay Point','3663 Gateway Crossing','244 Garrison Junction','1 Swallow Center','38 Elmside Circle','9 Monument Crossing','38538 Scott Place','015 Schurz Parkway','6376 Westridge Road','68 Lyons Parkway','726 Linden Parkway','90650 Stuart Street','26 Thompson Place','708 Melby Avenue','9 Eggendart Center','2 Gulseth Junction','92 Mockingbird Court','38 Crescent Oaks Road','304 Havey Plaza','677 Meadow Ridge Junction','62021 Arizona Lane','74 Barby Junction','1097 Mendota Lane','0 Hayes Court','54227 Derek Avenue','58 Crownhardt Street','534 Darwin Trail','510 Gina Plaza','5359 Fallview Park','2 Starling Plaza','9466 Corry Road','80 Sage Hill','7 Spohn Way','10 Rockefeller Terrace','1 Fuller Court','5269 Valley Edge Center','1 Tennessee Drive','359 Morningstar Terrace','50 Florence Hill','44868 Acker Center','23546 Lawn Junction','45 Clove Pass','2 Kinsman Center','921 Londonderry Avenue','3723 Kim Pass','346 Westend Trail','0302 Crescent Oaks Street','29310 Prentice Street','18162 Carioca Lane','33484 Kensington Pass','9093 Orin Way','04165 Vermont Center','6 Memorial Way','20505 Di Loreto Hill','06189 Summit Terrace','8191 Starling Road','114 Corben Court','69 Kropf Avenue','48 4th Junction','99653 Ridgeview Lane','149 Lunder Road','86942 Westridge Circle','53 Sommers Street','331 Chive Junction','31349 Elgar Parkway','738 Talmadge Pass','67294 Lukken Trail','353 Northview Court','8370 Brown Plaza','43 Sage Road','983 Dorton Terrace','032 Hallows Center','4046 Waxwing Avenue','28835 Derek Park','812 Anhalt Alley','5515 Melby Court','7990 Dryden Crossing','59026 Hooker Park','90218 Barnett Plaza','5962 Sheridan Trail','5 Scofield Way','6392 Dahle Alley','0 Thompson Circle','36 Welch Plaza','627 Dottie Crossing','66068 Brentwood Trail','0 Clove Park','062 Graedel Parkway','2 2nd Pass','66894 Sunnyside Junction','51139 Walton Street','0 Pine View Road','7328 Mallory Street','9095 Elka Court','71 Claremont Parkway','40066 Ridgeway Road','6 Kenwood Junction','7 Daystar Plaza','9088 Calypso Center','0 Havey Trail','320 Leroy Point','8642 Upham Trail','26563 6th Crossing','06 Northview Lane','88819 Haas Way','94070 Donald Place','6116 Katie Court','740 8th Court','3 Petterle Crossing','9 Pepper Wood Junction','9637 Oxford Center','97548 Ludington Trail','607 Dexter Lane','1 Miller Point','69807 Carberry Trail','51123 Thierer Place','50 Warrior Court','2265 Hazelcrest Way','3 Blue Bill Park Park','9341 Luster Street','7004 Mayfield Street','72263 Starling Crossing','76084 Pierstorff Trail','2558 Delaware Street','7 Schiller Center','2 Hintze Lane','650 Nelson Street','85 Del Sol Way','411 Sherman Terrace','97464 Sage Crossing','3352 Spaight Plaza','7602 Shopko Court','811 Logan Lane','8536 Gateway Park','9155 Sugar Place','88278 Meadow Valley Pass','7004 Prairieview Circle','8856 Ilene Trail','2031 Carpenter Point','05 Moose Pass','35 Kipling Court','598 Claremont Point','85155 Buena Vista Center','57 Muir Court','48 Oxford Lane','546 Melvin Plaza','044 Colorado Alley','933 Glacier Hill Point','6 Sherman Crossing','89527 Shasta Trail','6680 Vidon Avenue','5436 Golf Course Pass','11935 Blackbird Crossing','3290 Russell Drive','0 Corscot Junction','332 John Wall Hill','7 Hanson Hill','98735 Bunker Hill Court','08659 Hazelcrest Plaza','1 Northfield Way','233 Doe Crossing Center','84277 Sachtjen Avenue','6812 Memorial Terrace','96 Red Cloud Alley','423 Continental Park','89 Becker Court','68982 Fisk Drive','25741 Crescent Oaks Circle','1248 Elka Road','2126 Bashford Avenue','3144 Jenifer Road','851 Larry Street','0949 Waywood Park','05 Vahlen Terrace','4 Manufacturers Junction','21461 Katie Street','5454 Miller Alley','4098 Reinke Alley','79 Lakeland Alley','646 Judy Place','11305 Monica Plaza','76 Derek Hill','785 Granby Drive','95819 Blackbird Plaza','38312 Kipling Court','487 Crowley Circle','53987 Susan Street','14943 Lawn Circle','0427 Crowley Way','53 Brentwood Center','3 Trailsway Plaza','527 Dovetail Center','34 Union Center','1 Lotheville Drive','3 Lakeland Pass','96142 Eagan Drive','4 Dwight Point','23 Scott Park','9899 Straubel Lane','733 Summer Ridge Circle','7 Stuart Junction','9492 Hoffman Point','229 Linden Junction','82058 Fallview Pass','4 Emmet Parkway','9012 Fairfield Place','5822 Erie Road','80 Express Pass','99608 North Place','118 Waxwing Place','0714 Anniversary Court','864 Holy Cross Hill','81 Dorton Trail','60136 Erie Hill','674 Becker Plaza','3300 Saint Paul Circle','1 Barby Terrace','59 Express Court','09214 Maple Wood Park','291 Main Avenue','2 Stang Parkway','031 Tomscot Terrace','66 Lukken Parkway','0 Buhler Court','7180 Clyde Gallagher Road','7 Crescent Oaks Hill','52 Mallory Plaza','18785 Northwestern Point','5 Pankratz Court','655 Old Shore Way','3833 Burrows Junction','16 Golf Course Park','41842 Crownhardt Lane','2 Thierer Way','13 Fair Oaks Place','5316 Manitowish Lane','0701 Annamark Plaza','09 Elmside Parkway','532 Maywood Point','58 Schlimgen Hill','01 Carberry Road','9321 Eliot Junction','7762 Pawling Court','46 Corben Crossing','0147 Vahlen Street','906 Elka Junction','0470 Darwin Lane','732 Northland Avenue','438 Sauthoff Pass','3 Graceland Street','487 Autumn Leaf Junction','63 Sundown Park','61 Ridgeway Road','37171 Redwing Parkway','584 Dayton Drive','16150 Merchant Crossing','823 Tony Court','2175 Dawn Avenue','1208 Londonderry Junction','0 Waxwing Lane','97 Coleman Pass','1126 Warbler Drive','69 Hanover Drive','7199 Texas Circle','959 Morrow Street','66 Tomscot Place','966 Luster Terrace','7100 John Wall Avenue','1 Westport Way','469 Mccormick Point','92 Susan Street','9706 Grasskamp Hill','3611 Portage Street','8292 Karstens Lane','52227 Emmet Lane','00 Welch Pass','32 Arkansas Road','498 Jana Park','7 Superior Parkway','018 American Way','222 Springview Hill','4369 Iowa Alley','51 Ohio Lane','213 Surrey Plaza','7 Clyde Gallagher Park','2911 Truax Trail','7 Dixon Way','981 Gulseth Street','1 Mallard Terrace','7 Heath Road','33 Cordelia Lane','9098 Bultman Place','7967 Green Ridge Terrace','1 Farragut Avenue','8104 Veith Crossing','5 Linden Park','3 Cherokee Road','44364 Crescent Oaks Hill','76942 Monterey Drive','400 Ramsey Parkway','1883 Londonderry Parkway','8984 Waubesa Parkway','225 Dakota Circle','73 Dakota Plaza','05 Main Way','6 Welch Point','57 Blackbird Place','8210 Monterey Circle','5542 Schlimgen Court','6 Evergreen Pass','71 Kipling Hill','20 American Ash Street','24158 Walton Park','65 Pearson Parkway','2 Talmadge Parkway','357 Fisk Alley','0 Loftsgordon Pass','007 Crest Line Pass','76 Mosinee Trail','990 Bartelt Drive','58765 Ridgeview Center','58062 Dunning Street','49 Packers Plaza','5 Comanche Crossing','242 Saint Paul Pass','1753 La Follette Avenue','4991 Del Mar Center','37 Dorton Crossing','67768 Merrick Park','77285 Ohio Pass','7 Shasta Trail','42 Troy Way','424 Knutson Circle','5829 Union Pass','7602 Delladonna Lane','69457 Petterle Terrace','4737 Swallow Park','1376 Mallard Circle','293 Kinsman Avenue','219 Luster Circle','4 Havey Place','02 Pepper Wood Parkway','4035 Onsgard Hill','48873 Algoma Point','2 Manitowish Street','001 Sutherland Circle','120 Erie Plaza','5368 Melrose Way','41 Gale Place','90117 Stang Center','38 Caliangt Plaza','4 Porter Junction','37 Eastwood Court','4 Grover Pass','17 Brickson Park Court','00 Linden Court','59 Stoughton Trail','197 Sage Alley','043 Fulton Avenue','61960 Golf View Plaza','5 Manley Alley','31580 Commercial Lane','05 Twin Pines Terrace','474 Golden Leaf Junction','3406 Mccormick Road','81 Little Fleur Crossing','23488 Wayridge Avenue','5 Debs Plaza','7438 Mockingbird Road','074 Homewood Center','92 Riverside Circle','4 Dixon Trail','4 Fremont Plaza','8512 Dwight Circle','7157 Thierer Place','2 Old Gate Parkway','328 Onsgard Plaza','770 Fordem Lane','216 American Ash Point','73543 Myrtle Place','61779 Golf Park','727 Coleman Pass','1111 Aberg Parkway','214 Old Gate Street','266 Burning Wood Terrace','1 Tennessee Way','25212 Petterle Junction','7 Upham Parkway','59 Springs Road','220 Milwaukee Plaza','4 Merrick Point','38321 Hauk Pass','706 Mifflin Way','061 Lerdahl Center','64378 Prairie Rose Street','0745 Mallory Circle','77 Burrows Way','405 Mandrake Parkway','328 Cambridge Crossing','10 Cherokee Terrace','4414 Kropf Center','221 Hanson Lane','157 Schiller Place','84 Corben Lane','33315 Westerfield Hill','255 Farmco Hill','99233 New Castle Place','6681 Briar Crest Road','32851 Bobwhite Plaza','760 Blackbird Way','9 Hauk Alley','57822 Myrtle Way','55715 Green Lane','0 Gale Way','02 Meadow Vale Parkway','55267 Nova Road','0 Briar Crest Circle','25069 Canary Point','53 Green Ridge Trail','07 Ronald Regan Way','97 Lukken Way','3329 Beilfuss Place','57 Columbus Junction','51404 Marquette Hill','82942 Little Fleur Hill','12 Pleasure Drive','06819 Old Shore Alley','4 Macpherson Hill','13220 Rowland Pass','3177 Orin Drive','12753 Surrey Road','057 Luster Plaza','51 Roxbury Drive','6069 Warrior Terrace','682 Anthes Place','9337 Mcbride Circle','5 Roth Junction','3477 Sycamore Park','45 Daystar Lane','989 Jana Point','6409 Mayfield Court','14628 Monument Lane','494 Almo Parkway','95 Forest Crossing','331 Kennedy Center','913 Washington Plaza','939 Sauthoff Avenue','8637 Scott Terrace','0 Butterfield Lane','183 Melrose Terrace','67 Veith Way','419 Carey Trail','5845 Glendale Terrace','7231 Nelson Street','320 Larry Drive','73169 Coleman Road','10873 Sommers Circle','03284 Browning Avenue','14 Hoard Circle','91556 Loftsgordon Hill','63934 Lakeland Point','1 Corscot Trail','4214 Commercial Road','78354 Carioca Way','05 Corben Court','669 Upham Junction','6184 Hoard Street','2 Village Green Trail','54 Goodland Alley','4 Wayridge Crossing','0 Wayridge Lane','286 Lerdahl Terrace','33224 Anniversary Lane','09181 Sommers Circle','979 Thierer Terrace','40 Marcy Place','302 Jay Junction','548 Summerview Terrace','5838 Sundown Center','2 Derek Drive','0 Cardinal Parkway','07490 Southridge Way','592 Parkside Hill','63599 Shoshone Road','9032 Badeau Drive','81 Lyons Court','61634 Melby Pass','26 Paget Junction','232 Elka Lane','14288 Mifflin Plaza','08160 Boyd Alley','49 Dahle Crossing','495 3rd Parkway','86 Birchwood Hill','04 Hovde Center','52 Hintze Trail','986 Harper Street','70691 Green Ridge Junction','26 Dryden Point','799 Mitchell Alley','15420 Prairie Rose Alley','62616 Crest Line Lane','374 Blaine Drive','781 Briar Crest Lane','71050 Buell Lane','51 Kensington Pass','9778 Warrior Avenue','4 Arrowood Plaza','6 Ryan Plaza','3 Red Cloud Lane','4925 Toban Plaza','638 Derek Crossing','68 Crest Line Park','832 Anniversary Terrace','2 Thierer Park','67702 Hallows Plaza','893 Saint Paul Junction','689 Portage Drive','0270 Vermont Junction','3218 Dayton Point','62795 Scofield Junction','3422 Graedel Street','66 Gina Place','7 Dakota Circle','1 Rigney Hill','7 Heffernan Lane','07916 Gerald Street','16271 Ridgeway Lane','1303 Debra Road','7174 Cardinal Circle','496 Artisan Way','4 Straubel Court','79 New Castle Park','6 Butterfield Circle','51548 Banding Plaza','11 Fairview Way','41801 Nova Plaza','40903 Garrison Parkway','198 Park Meadow Pass','178 Redwing Park','9 Main Alley','28 Golf Place','9530 Dwight Way','903 Miller Park','653 Iowa Drive','3011 Graedel Drive','5923 Merrick Trail','18 Memorial Center','543 Burrows Parkway','03 Gale Junction','04 Rutledge Street','53 Manley Trail','26231 Sunnyside Drive','92 Delladonna Place','9 Veith Place','4494 Kenwood Court','1273 Susan Street','82421 Evergreen Parkway','670 Ilene Court','2 Crownhardt Park','5774 Fremont Parkway','3 Summer Ridge Drive','89 Vermont Hill','3 Ohio Trail','69897 Bowman Drive','095 Sullivan Lane','70 Ryan Lane','94 Elmside Alley','458 Summer Ridge Street','333 Iowa Hill','247 Surrey Plaza','3 Buell Terrace','1 Walton Court']
		if '\n' in (data):
			data=data.splitlines()
			for i in range(len(data)):
				data[i]=addresses[randrange(1000)]
			return '\n'.join(data)
		else:
			return addresses[randrange(1000)]

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardrandomcityCommand(sublime_plugin.TextCommand):
	def format(self,data):
		city=['Appleport','Casterdol','Eastfolk','Julmouth Island','Fairkarta','Hapwich','Tallworth','Angerborough','Applebury','Bridgeworth','Holtstown','Proburg','Hosley','Highcester City','Casterhampton','Hapford','Eggfolk','Freeville','Redtown','North Hoston','Winterport City','Middleburgh','Luncester','New Summerburgh','Factton','Jamesburg','Weirhampton','Auview','Southkarta','Fortdol','Sagestead','Buoyburgh','Capborough','Dodgeburgh','Queensview','Aelview','Julburg','Postwich','Northley','Mansgrad','Melley Park','Great Sagepool','Foxhampton','Mansmouth','Capham Beach','Eggstead','Clamtown','Great Eggness','East Middlefield','Westview','Melport Hills','Chatville','Gilfield Falls','North Griffinbury','Eggwich','Griffinley','Julworth','Kingness','Freedale','Emerborough','Fairdol','Kingness','Sugarcester','Roseham','Tallley','Hamford','East Strongley','Griffinstead','Faydale Falls','Seadol','Freeness Falls','Millhampton','West Winterside','North Mangrad','Holtsmouth','Manport','Redworth','Hapburg','Emerkarta','Auworth','Manham','Capcester','Manby','Norcaster','Winterley','Hapbury','New Proside','Princeley','Kettlewich','Appleford','Waterwich','Waterdol Falls','East Farmcaster','Buoydol','East Chatness','Hapley','Emerbury','Chatby','North Passmouth','Riverdale','Readingby','Pailford','New Roseview','Springview','North Sealey','Saltview','New Applecaster','Banndale','New Goldhampton','Waterland','Bellborough','Mayby','Angerton','Factpool','Holtsness City','Foxford','Massburg','Hardkarta','Eaststead','Griffinpool','Hallpool','Rivercaster','Goldley','Richburgh','Daymouth','Protown','Hapford','Sugardol','Angerfield Island','Sweetkarta','New Ashview','Masskarta','Aelfolk','Southingness','Cruxley Falls','Mannorcaster','Pinebury','Medbury','Farmfield','Saykarta','Manburgh','Castergrad','Hoskarta','Waterpool Falls','Stoneworth Falls','Winterpool','Holtsness','Sugarport','Southingkarta','Wingwich Park','Emerdol','Lunstead','Westfield','Dodgeton','Dayworth','Waltby','Hardwich','Proland','Summermouth Island','West Westwich','Weirborough','Mannorcaster Falls','New Factville','Mayby','Fishcester','Hapby','Auley','Lunport','Southingdale','Auhampton','Lunworth','Middlestead','Transmouth','Fayfolk','Skillley','Jameshampton','Highmouth','Kettledale','East Oakwich','Hallton','Hallstead','Richgrad Island','North Bannland','Farmingborough','Hosmouth Hills','Goldkarta','Backham','Milldale','Fauxton Island','Farmgrad','Riverstead','Mannorpool','Winterport','Eastbrough','Backcester','Seaburg','South Postfield','Clamgrad','Valencaster','Summerfield Island','Lexingdol','Waltbrough','Elwich','Weirborough','Riverside','Southham','Kettleside','Seaton','Eggview','Jultown','Gilford','Readingside','Waltville','Lawtown Island','Snowview','Rosedol','Proside','Melham','Fishside','Angerley','Buoyview','Richcester','East Appleness','Seabrough','Summerpool','Startown','Lexingfield Park','Northhampton','Aelstead','Gilborough','Meltown','Beachfolk','Passkarta','Fishstead','Lexingview','Proport','Lexinggrad','Emerburgh','Farmington','Kettleford','Westcaster','Great Bridgeland','Factdale','Rockpool Hills','Frostmouth','Fishdale City','Norborough','Melton','Waltmouth Island','Cruxpool','North Capmouth','Highford','Fairport City','North Highford','Sweetpool','Middlemouth','East Frostside','Farmingley','Princeville','Highcester','Jamesley','Waltwich','Melmouth','Skillland','New Foxcaster','Masston','Roseborough','Hapcester','Backfolk Island','Maystead','Waltside','Pineley','Roseford','Snowfolk','Fairton','Waltness','New Riverham','East Sandburgh','Sageville','Sanddale','Lawford','Baybury','Kingtown','Fortpool','Skillgrad','Lunatown','Fayland','Beachport','Angerworth','Waltwich','Fauxburg','Readingdol','Sayburgh','Strongland','Wheeltown','Fayville','Holtshampton','Goldborough','North Maybrough','Greencaster','Sageham','Nortown','West Lunaby','Freewich','Lawby','Northby','Lunview','Norwich','Richborough','Farmford','Sayford Beach','Maygrad Island','East Watermouth','Goldworth','Farmhampton Falls','Valenness','Applefolk','Waterbury','Beachburgh','Hapgrad','Great Factburg','Casterstead Island','South Medham','Augrad Falls','Gilpool Beach','Lunport','South Baygrad','Lawland','Westland','Sweetfield','Duckville Park','Northside','Massborough','Postwich','South Parkburg','Cloudburg','Costsmouth','Hardhampton','Springby Island','Fairstead','Starbrough','Millbury','Westham Beach','Stonestead','Lunaworth','Casterford City','Greenby','Backborough','Postgrad','Saywich','Fauxcester','South Sagefield','Hallmouth Beach','Seamouth','Great Summerworth','Duckbrough','Ashbrough','Dodgedol','Princefolk','Farmgrad','Great Mayburgh','Springdol','Mannorport','Griffinpool','Sweetside','Proby','Hallstead','Weirley','Manston','Farmingfield','Pinepool','Wheelkarta','Rockburg','Medburg','Rockgrad','Oakness','Kettleness','Factton','Seahampton Hills','Dodgeworth','Ashdale Beach','Duckcaster','New Stardol','Prostead','Snowfolk','Hardport','Kingdale','Winterford','Casterpool','Starside','Ashport','Millworth','Bridgeburg','Fairland','Hosdol','Fairdol','Highport','Stoneborough','Redfolk','West Griffintown','Oakgrad','Buoyworth','Bridgeport','Freeburgh','Redfolk','Hallburg','Pailville','Buoycester','Backview','North Hollowport','Middleworth','Great Eastcaster','Parktown','East Snowburgh','Strongdale','Bannbury','Capham','Casterland','South Eastville','New Farmfolk','Southley','Melkarta','Aelgrad','Postwich','Farmness','Seaford','Chatbury','Farmingstead','Winterham','Watermouth','New Kettleby','Farmpool','Great Hallbury','Propool','Nortown','Fishstead','Bannburg','East Stonestead','Pailwich','Lunabrough','Gilburg','Hogworth','Sandcaster','Waltford','Casterborough','Holtsport','Stonestead','Parkville','Southingview','Valenfolk Island','Mannorworth','Foxley','Cruxville','Queenspool','Jameston','Sweetview','Bannford','Medham','Kingness','Passness','Farmingby','Princeby','Hapview','Oakdale','Appleford','Sweetburgh','Haphampton','West Mansburg','Postdol','Hapby','East Hamgrad','Strongcester Beach','Factdol','South Farmingford','Great Oakgrad','East Eggside','Great Passhampton','Hollowness Park','Goldcester','Castercester','New Jamesdol','Hollowmouth','Roseport','North Sageley','Clambrough','Goldbrough','Richley','Lunness','Aelley','New Buoycester','Lexingpool','New Mansgrad','South Fairford','Melkarta','Readingby','Fortfield','Bannfolk','Mannorby Beach','Daybrough','Southingham','Postpool','Bridgeham','Aupool','Pailville','Highton Island','Postford','Sayton','North Hosness','Mannorgrad','Wintergrad','Hosland','Sweetworth','Great Holtshampton','Cruxfield','Hosham','Costshampton','Hogford Island','North Princekarta','Kingbrough Park','Starcester','Sageside','Pailmouth','Jameshampton Falls','North Southingview','Goldborough','Springville','Middleness','Emerborough Falls','Hamley','Lawhampton','Snowwich','Mankarta','Springbury','Parkcester','Hollowville','Middlegrad','Wingborough','Hardtown','Medkarta','Maywich','Mannorport','Casterbury','Northkarta','Northtown','Great Ashpool','Frostkarta','Capville','Parkcester','Cruxside','Lawhampton','Fishville','Farmingness','North Manby','Mansview','Capham','Great Northdol','Massdale','Springwich','Richmouth','Emerham','Duckpool','Stonecester','Saltpool Falls','Wheelstead','West Summerworth','Auville','Wheelgrad','Bridgemouth','Greenkarta','Sageport','Holtswich','Rockhampton','Middlewich','Angermouth','Chatville','Great Princestead','Hapworth','Great Procester','Waterdol','Jamesborough','Bellcester','Norville','Holtstown','Chatby','Eastgrad','Southgrad','East Hapwich','Eaststead','Northfolk','East Fauxville','Medport','Hardwich','Frosttown','North Proness','East Medkarta','Sweetport','East Richdale','Redby','Lunabrough','Backham','Lunawich','Baywich','Rockbury','Dayburgh','Westcester','Waterwich','Saypool','Hardborough Island','Manview','Sageford','North Westmouth','Millbrough','Waterpool','Queensfolk Island','Eggfolk Park','Valenstead','Jamesburgh Falls','North Nordol','Transley','Sweetville','Parkhampton','Belldale','Emerness','Medcester Park','New Jamesdale','Valengrad','New Kingbrough','Rivertown','South Sweetworth','Hallport Park','Bridgebrough','Winworth','Transdale','Redford','Mayport','Mancester City','New Dodgeport','Hollowton','Milltown','Backdale','Stonetown','Parktown','Manland','Griffinworth','Sageham','Easttown Park','South Clamby','Massdale Park','New Kinggrad','Fishfolk','Bannburg City','Summerness','Cloudcester','Jamesworth Park','South Hosworth','Cruxburg','Foxville','Hogdol','Clambrough Island','Waterwich','Costston','Medcester','West Rockbrough','Greendale','Aucester','Sayworth','Hoskarta','Millton','Pinebury','Clamcaster','North Saltland','Griffinburg','Richby','Kingford','Highwich','Hallford','Clamside','New Eggham','Banncaster','Casterley','Weirkarta','Oakpool City','Aelton','Elworth','Waltborough','Parkcester','Riverby','South Tallfield','Frostpool','Hardborough Falls','Baycaster','Stoneford','Farmingside','Fauxwich','Skillley','Stoneview','Greenfolk','Mayburg','Duckhampton','Mannorham','Fairham','Bannmouth','Great Casterley','Richstead','Audol','Kettlecester','Maypool','Profield','Jamesley','Tallville','Rosecaster','Sandtown','Snowworth','Lawwich','Hapby Hills','Proport','Sagekarta','Sweetton','Stonegrad Falls','Goldview','Holtsstead','Great Hardtown','North Ashfield','Kettleburgh','Eggville','East Fauxdol','Fortview Island','Hollowview Hills','Northport','Lunfolk Beach','Duckcester','Gilworth','Costsborough','New Freeville','Lunaport','West Wingport','Rockport','Casterton','Oakburgh','Griffingrad','Winmouth','Manscester','Mayfolk','Great Costsworth','Lawbrough','Elland','Pineville','Readington','Lundol','Hardgrad Beach','Gilside','Postborough','Jamesburg','Holtsland','Saltland','Baycester','Pinekarta','Hallbury','Transland','Eggburgh','West Frostcester','Wheelside','North Lexingkarta','Massview','Aeldol','Hardworth','Angerby','East Mannorness','Sayland','Clamland Park','Stonefolk Island','Lexingburgh','Princeview','Applestead','Wingford','Elley','Starby City','Fauxness','Saltstead','Proburg','Southcester','Jamesville','Kettlehampton','Riverdol Island','Appleness','Capworth','Eastburgh','Chatford','Cruxfield','Sandview','Great Cruxville','Beachfield','Factburg','Parkhampton','Great Wingcaster','Proport Park','Great Duckley','Eastmouth','Pailburgh','Hamborough','Fortville','Holtsworth','East Norkarta','New Mannorside','Bridgeside','Faykarta','Holtsby City','Sandpool','Griffinburgh','Lexingland','East Rosegrad','Capdale','Parkdol','Hallburgh','Walthampton','North Bannford','Farmstead','Passburgh','Parkmouth','Hosness Park','Backbury','West Sageham','Parkfield','East Clouddale','Pinestead','Starville','Fairby','Eggdol','Chatdale','East Medstead','Snowborough','Freepool','Winview','Cruxtown Falls','Great Buoyley','Lexingdale','Gilborough','Tallgrad','Medburg','Jamesham','Starcaster','Clamdol','Millham','Hogdol Beach','South Eastport','Ashport','Massland','Foxbrough','Masskarta Park','Springford','Readingstead','Lunburgh','Valenness','Lawwich','Frostpool Hills','Passmouth','Mannorgrad','Oakburgh','Summerby','Seakarta','East Redgrad','Richstead','Redfolk','Bannkarta','Factville','Aelburg','Clamburgh','Sagefield','Wingdale','Ashhampton','Lunadale','Beachstead','Hardcester','Mannorby','Great Southingham','Lunatown','Appleham','Sayford','Buoyley','Bayborough','Southcester','Duckton','Dodgehampton','West Westley','Capburgh','Saltland','Goldton','Banndol City','Dodgebrough','Faycaster Hills','Hoswich','East Massdol','North Proham','West Skillville','Richcaster','New Melcaster','Summertown','Costsford','Eastcaster','Norbury','New Hardpool','Angerhampton','Freedale','Melby','Sugartown','Aupool','Massburg','Medham','Talldale','Richwich','Windol','Faydale','Baybrough City','Fauxmouth','South Valenville','Capbury','New Holtston','Pineworth','Farmingby Beach','Sweetdale','Mansville Hills','Hollowwich','Buoyland','Faydol','Sweettown','Duckby','Lunafolk','Rockville','New Julley','Emerdol','Skillton','East Lawford','Kingcester','East Waltness','Pailfolk Falls','Saltside','Waterburgh','Rockbury','Princeham','New Saltland','Skillkarta','Proborough','Daydol','West Rockfolk','Cruxcaster','Aeldale City','Lexingport','Strongton','Valenford','Hallton','Jamesside','Maykarta','Julland','Hardside','Medham','Hamside','Springcaster Hills','Transside','Pineham','Posthampton','Readingfolk','Ashstead Island','Chatcester City','Riverfolk','Queensburgh Beach','Summerside','Oakburgh','Sayley','Waterfield','Queensley','Bannford','Rockbury','Fairmouth','Buoyford','Castertown','Backdol','Kettleburg','Factmouth','Oakdale','South Lawdol','Saltley','Sageville','Chatburg','Sugarley','West Eastworth','Lexingmouth Island','Readingdale','Dodgefolk','Cruxley','Faystead Island','Julfield','Julstead','Goldhampton','South Lawkarta','Southside','Bellton','Meldol','Maybury','Middleville','Jamesby']
		if '\n' in (data):
			data=data.splitlines()
			for i in range(len(data)):
				data[i]=city[randrange(1000)]
			return '\n'.join(data)
		else:
			return city[randrange(1000)]

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)




class datawizardrandomfirstnameCommand(sublime_plugin.TextCommand):
	def format(self,data):
		firstNames=['Kelwin','Quillan','Maire','Matelda','Florentia','Sherri','Gerry','Anselm','Peri','Kirstyn','Onfroi','Jasen','Jeniece','Mord','Ardelis','Consuela','Celine','Halley','Antonietta','Pattin','Domingo','Mandie','Hardy','Dorelle','Nikolas','Ninette','Jeno','Rowan','Bev','Clayborn','Fleming','Carla','Beret','Abelard','Kellen','Bee','Jess','Coretta','Rory','Willdon','Hinda','Teddy','Ebenezer','Monroe','Robbi','Kathryn','Valerye','Sheree','Judas','Remus','Shena','Cristy','Iorgo','Avictor','Roby','Linnea','Linc','Silva','Bogart','Amitie','Gavra','Michail','Elysia','Maritsa','Gayelord','Glenna','Mart','Dov','Zorana','Johna','Parry','Amelita','Fiona','Zach','Halette','Norine','Sigismond','Tannie','Lexis','Carita','Gustie','Dougie','Dana','Fiann','Helenelizabeth','Delora','Theo','Reginauld','Caro','Cecilla','Tiler','Letty','Aveline','Kenna','Cointon','Adriano','Eddi','Aubree','Tommy','Clevey','Ferdinand','Shawnee','Carita','Sayre','Calli','Gerry','Saul','Angeline','Gifford','Sylvester','Randi','Ive','Derward','Ted','Land','Jana','Alasdair','Eduardo','Karlie','Gilbertina','Darryl','Guthry','Kameko','Gillian','Donalt','Shay','Barbi','Mahmud','Minni','Sayres','Barbabas','Zorah','Darb','Jan','Elonore','Mike','Enriqueta','Noel','Jana','Forbes','Rube','Tony','Tani','Stanislas','Jordanna','Roberto','Fabio','Goddart','Quill','Claudine','Ibbie','Dwayne','Alfons','Godfrey','Chev','Uriel','Lorianne','Tanitansy','Faythe','Amii','Corri','Natividad','Elroy','Alexis','Stormi','Rosaleen','Nellie','Lodovico','Sascha','Ulrika','Giffard','Rodge','Othilia','Eward','Maud','Ashely','Roxanne','Sissie','Anny','Inger','Dahlia','Kimberley','Tiffani','Yancey','Allen','Melloney','Alidia','Hammad','Mireille','Pammie','Josee','Antony','Lorine','Tedman','Menard','Jory','Norri','Nissa','Guthrie','Heath','Danna','Hildegaard','Ely','Marigold','Shoshanna','Avis','Yuma','Ernestine','Shem','Delora','Modestia','Russ','Elisa','Timoteo','Cathie','Henri','Keefer','Mauricio','Melisenda','Dom','Alexei','Gizela','Ezekiel','Rand','Demetris','Merell','Malanie','Omar','Dacie','Tamarah','Skylar','Griswold','Eldin','Durante','Yevette','Gwenore','Laurent','Brandyn','Elfrida','Veradis','Sonny','Bea','Denny','Mort','Matilda','Chris','Dame','Godiva','Hailee','Norri','Anstice','Danya','Tildi','Welbie','Pippa','Angelica','Ryley','Krystal','Lindi','Jodie','Monty','Daphne','Freddi','Waylan','Kippie','Jeri','Hastings','Liza','Marchall','Katuscha','Karoline','Louis','Meriel','Leshia','Lukas','Edna','Abrahan','Granny','Claude','Lisette','Jermaine','Emmerich','Derron','Delmore','Noah','Nellie','Martica','Ketti','Kara-lynn','Zoe','Madelin','Suzette','Brigham','Calv','Berkly','Findley','Leeanne','Muire','Lauraine','Corina','Andrus','Kaitlynn','Fara','Jo-ann','Rutter','Patricio','Zebulen','Zoe','Sherwynd','Garfield','Monty','Curran','Renaud','Sib','Angus','Bernardina','Sergent','Eolande','Clem','Eloisa','Osbert','Carree','Latashia','Kipp','Tammie','Freddy','Berni','Fraze','Vic','Bevan','Agustin','Valry','Clari','Jaimie','Tadeas','Caitlin','Brear','Carrol','Dede','Sonnnie','Dimitry','Saloma','Blondy','Merrili','Kellie','Aura','Dominik','Vivyan','Ebba','Belvia','Elsbeth','Everett','Townsend','Trace','Corny','Markus','Cherise','Nanci','Danny','Erina','Joyan','Lilias','Johannah','Sioux','Clarabelle','Sawyere','Channa','Stu','Eartha','Esra','Rheba','Elbert','Carline','Barb','Earle','Brittany','Darryl','Roslyn','Lucia','Tiphany','Emilie','Lionel','Zsa zsa','Barty','Hartley','Cissiee','Randee','Cherilynn','Herta','Lurline','Katrinka','Trescha','Vasilis','Innis','Kinsley','Tory','Louise','Travers','Sterne','Jobyna','Leonardo','Solomon','Torey','Leyla','Rad','Netti','Lorilee','Gearard','Ferdy','Chariot','Nadia','Scarface','Catlin','Clarinda','Saundra','Oneida','Luther','Pedro','Karylin','Adele','Bondon','Alysia','Phyllys','Pierre','Peria','Mehetabel','Terri-jo','Danya','Cecelia','Rogerio','Dannie','Milly','Orelia','Berti','Hoyt','Beret','Sax','Ronica','Nicolea','Adrienne','Feodor','Vonny','Gerard','Wilmer','Rhianon','Humfried','Tally','Matt','Leroi','Chandler','Shayla','Roley','Lucio','Chariot','Jenelle','Adolphe','Jone','Hermia','Lucian','Vivianne','Nada','Sherlocke','Ansel','Seline','Amandie','Manolo','Rosalynd','Gardiner','Andre','Eba','Pepi','Happy','Dillie','Alina','Kylila','Estell','Marie-jeanne','Joete','Gibbie','Wallis','Fairlie','Haley','Tobit','Corri','Annabell','Jordon','Modestine','Donielle','Cherilyn','Claudelle','Vinson','Josie','Alanson','Glyn','Tandy','Sosanna','Melonie','Barnaby','Ernie','Bridie','Eddie','Aggy','Holli','Nicoli','Stinky','Andros','Hadley','Gilemette','Eloisa','Iris','Ivar','Rebeca','Mead','Lorelle','Hadleigh','Dalli','Flory','Jud','Faun','Nevin','Trenton','Demetre','Mari','Noel','Jenny','Tiphanie','Dillon','Lazare','Normie','Deirdre','Vanya','Blithe','Jemimah','Sean','Margette','Cordie','Hobey','Pail','Symon','Eddy','Rebeka','Doreen','Adelind','Oswell','Herta','Albina','Tiler','Kingston','Vivian','Phyllys','Camila','West','Robin','Constantia','Laverna','Kaylil','Trip','Midge','Barde','Reynard','Rafaela','Shoshanna','Winona','Fayth','Baryram','Rebecka','Nola','Tobit','Genevieve','Oran','Bernadette','Gery','Trudy','Shadow','Frank','Ulrick','Deonne','Felecia','Sandor','Hilarius','Orlando','Karlie','Madlin','Cyrillus','Nollie','Nadean','Larissa','Wilfred','Vanessa','Leesa','Irena','Donica','Averell','Gustaf','Lorain','Lilllie','Quintus','Monika','Ruperta','Carolina','Mohammed','Charline','Rancell','Sandro','Kean','Anissa','Lizette','Hedvig','Jessika','Samson','Min','Jilly','Ban','Louise','Nerita','Corenda','Brnaba','Lorain','Cobbie','Bernelle','Dierdre','Minnaminnie','Baryram','Devy','Georas','Ceil','Melitta','Marcelline','Robena','Wenda','Anneliese','Fawne','Julieta','Lou','Sherlocke','Farr','Rowena','Sallie','Shay','Gene','Shantee','Karylin','Juline','Ricki','Griffith','Aviva','Ned','Dominik','Gerry','Bibi','Adelaida','Barbabas','Rosalia','Melony','Lavina','Delilah','Rurik','Dalis','Antons','Annie','Rad','Clementius','Claudio','Lilian','Caralie','Jasmin','Erroll','Tadeas','Jamie','Perri','Cyrillus','Collete','Amelita','Mar','Florrie','Karie','Whitaker','Devland','Kippie','Graeme','Webster','Tova','Archer','Armando','Ferris','Inigo','Marty','Winn','Ilse','Tarrah','Josias','Alphonso','Coralyn','Lezlie','Melvyn','Danika','Pamelina','Jorry','Orran','Rochette','Aubree','Millie','Kinna','Christy','Morena','Susy','Maureen','Kiley','Shirl','Sapphira','Paloma','Alva','Genvieve','Elfie','Sella','Tammi','Allix','Jacquelin','Mack','Brewster','Pate','Baudoin','Alice','Alden','Corrine','Piggy','Nellie','Natalya','Lorelle','Evangeline','Darius','Emma','Gwen','Henriette','Andrew','Hanna','Laverne','Zonda','Lebbie','Clyve','Herold','Abbi','Moshe','Maryjane','Lesli','Julia','Raddie','Artair','Siward','Venus','Abe','Sherri','Orrin','Sileas','Maye','Vachel','Devan','Creighton','Wheeler','Shandy','Cristina','Etty','Keith','Eldin','Shani','Laverne','Leanor','Rolf','Barby','Philipa','Ali','Ali','Richy','Gerianne','Katine','Lonni','Verine','Ethe','Ailina','Haily','Gilberto','Rosalynd','Robbie','Julissa','Pauline','Barbabas','Albertine','Orsola','Earlie','Hurleigh','Rudolph','Corine','Farley','Brade','Sybil','Lea','Jennee','Daisie','Bellina','Ardeen','Randene','Rozelle','Mariska','Valle','Ethyl','Diahann','Barbra','Mariellen','Heall','Konstantine','Tatum','Dorrie','Cody','Berky','Kristofer','Dave','Ignacius','Gilburt','Abdel','Shay','Selma','Rabbi','Alice','Dion','Manya','Aland','Morgen','Dyana','Adaline','Terry','Glynnis','Tyson','Ameline','Willow','Joby','Wilhelmine','Damon','Manny','Molly','Katharyn','Belva','Fernande','Jesus','Job','Niven','Hillard','Mahmud','Hedvige','Jenda','Kay','Elset','Tadio','Shirlene','Paulette','Claus','Franny','Morly','Shayna','Maury','Cassie','Cassandra','Brockie','Lulita','Karlyn','Trenton','Philomena','Isadora','Michelina','Jeana','Donovan','Cammy','Rina','Katharina','Petronella','Darsie','Elle','Vikki','Grannie','Charmine','Moyra','Tracey','Burtie','Anthe','Thurstan','Petr','Tamarah','Hedda','Desmond','Cesya','Chrissy','Geno','Nora','Tillie','Meryl','Ange','Lewie','Ralph','Brody','Ricki','Ricki','Henrietta','Geordie','Garrot','Hobart','Prent','Wolf','Loise','Myra','Dane','Griffie','Willamina','Brit','Klara','Carce','Tobiah','Clemmie','Matilde','Hazel','Samuel','Daron','Teodoro','Thorndike','Sarette','Collin','Mariquilla','Gratiana','Silvie','Charla','Blair','Francesco','Ann','Aile','Cariotta','Scott','Gianina','Babs','Butch','Dewain','Maighdiln','Gustavus','Janella','Liza','Joline','Yancy','Evelyn','Jacintha','Alayne','Arte','Rosco','Pierrette','Alameda','Bren','Luz','Sallyanne','Joanie','Giacinta','Herrick','Kaleena','Kiele','Tallia','Lizette','Nikkie','Penn','Winifred','Dolley','Vivianne','Meggy','Kerwin','Elsey','Lory','Con','Gisela','Shaine','Kristin','Camile','Montgomery','Siegfried','Alric','Eran','Knox','Ingmar','Hercules','Loreen','Karney','Agnola','Barnie','Misty','Duky','Garreth','Beverlie','Dall','Elsbeth','Giralda','Starlin','Heloise','Doe','Sherie','Pavel','Orrin','Freda']
		if '\n' in (data):
			data=data.splitlines()
			for i in range(len(data)):
				data[i]=firstNames[randrange(1000)]
			return '\n'.join(data)
		else:
			return firstNames[randrange(1000)]

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardrandomlastnameCommand(sublime_plugin.TextCommand):
	def format(self,data):
		lastname=['Fulton','Billingsly','Gobell','Chamberlen','Ionnisian','Blenkiron','Bathowe','Gaven','Silver','Chsteney','MacIlory','Ramsbotham','Glasner','Micah','Bodsworth','Volette','Chadbourne','Weeden','Sucre','Callcott','Boughtflower','Iacovuzzi','McAlinion','Scollick','Gilmour','Cowie','Jacob','Derye-Barrett','Scoles','Bread','Cankett','Drews','Patesel','Lisciandro','Breslin','Roadknight','Blaksley','Aucourte','Sarll','Sanbrooke','Semens','Odom','Matts','Skurray','Shorland','Antonetti','Scrammage','Lawn','D\'Oyley','Conway','Wasylkiewicz','Haldane','Gummow','Gimblet','Zuanazzi','O\'Hallihane','Daggett','Folder','Brisley','Shepcutt','Coare','Anespie','Bewfield','Lawrie','Ryburn','Hattigan','Berndsen','Peppard','Bengall','Shotbolt','Carlyon','Riach','Cussen','Fashion','Madrell','Cowdrey','Olivie','Hanshaw','Beekmann','Leversha','Wolvey','Verni','Vasiltsov','Coronado','Arghent','Stickings','Gruszczak','Humm','Thomke','Hoggan','Greyes','Beernt','Odney','Brownell','Morfell','Gealy','Feeny','Millins','Huband','Omand','Iacovides','Greed','Heeran','Shinton','Tolomei','Manssuer','Oswal','Kinglake','Legendre','Sharpley','Lackner','Josef','Aron','Meyer','Farndale','Selburn','Murrison','Dikle','Cromack','Cotterell','Chesson','Duffil','Wollrauch','Cannings','Poller','Philbrook','Falkus','Brundall','Piercy','Boome','Ordemann','Ganny','Powder','Cheasman','Hanway','Judge','Nester','Volet','Cahani','Brigstock','MacLoughlin','Pool','Oattes','Lecount','Gateshill','de Clerq','Gunson','MacCrosson','Kayes','Preddy','McKnish','Oby','Meltetal','Lever','Hagwood','Antoni','Spilsbury','Lemin','Annis','Lyddy','Itzhayek','Smythin','Dominighi','Herkess','Elson','Rowberry','Denning','Laurence','Elloway','Ritson','Bonsale','Zukerman','Wollacott','Panner','Loram','Hares','Getty','Bourbon','Wanden','Vokes','Powter','Ellerington','Bondy','O\' Cuolahan','Easey','Aspland','Cridge','Search','McFaul','Toppas','Lindelof','Diggons','Sorby','Flaws','Craddock','Trippett','Fleis','Mollison','Berthel','Cowlas','Farmloe','Blenkhorn','Henriques','Etock','Hallut','Valens-Smith','Pendlebury','Haddrell','Burton','Plevey','Tidswell','Radborne','Dugdale','Ockland','Foulis','MacLeod','Shaxby','Bodicam','Chatterton','Synnott','Rabley','Scarlin','Pepall','Bedward','Alcalde','Sauniere','Greyes','Spedding','Bysouth','Lomb','McSherry','Pettie','Whaites','Sivier','Vreede','Moline','Brando','Meir','Heckney','Plitz','Tennick','Attwell','Fenney','Curley','Sautter','Verlinden','Rupprecht','Ginger','Braney','Brabben','Diable','Tullis','Pellett','Eagan','Muffin','Aspden','Croci','Straun','Farlambe','Negri','Barson','Broodes','Brumby','Rivel','Pardoe','Rigby','Faulks','Maw','Jouannot','Fadian','Gunton','Brideoke','Calvey','Tyson','Lantiff','Withrop','Harfleet','Tayler','Wakenshaw','Eastman','Stobbes','Covill','Gyer','Toffalo','Juanes','Liversedge','Beasley','Fitzharris','Baptista','Awcock','Grzeszczak','Bore','Eslinger','Poschel','Willingham','Brugh','Domegan','Astupenas','Vertey','Sevitt','Gouldstone','Leile','Boone','Casewell','Piddick','Carff','Astill','Riccioppo','Tregidga','Larimer','Fossitt','Pilipets','Rumsby','Balham','Baugh','Wantling','Ramiro','Gwyneth','MacKim','Pearch','Briiginshaw','Hansberry','Lucchi','Giovanizio','Gamet','Braybrookes','Grimsdike','Kiss','Leidl','Parkes','Mila','Cannam','Vasilyevski','Jell','Jurn','Rzehor','Nowakowska','Glisane','Deeming','Skrines','Dilrew','Elsop','Harly','Bignal','Archell','Myner','Angliss','Sadler','Bohling','Stocken','Lofty','Jayne','Turbayne','Pales','Basso','Handmore','Reedman','Duffell','Leney','Scotchmur','Rendell','Crumpton','Verman','Joret','Lackey','Bagwell','O\'Mullaney','Daniell','Konerding','Housen','Burcombe','Ledgister','Eakeley','Creaser','Coughlin','Marchetti','Brearley','Alleway','Streetley','Pettit','Tuffield','Denial','Stutt','Krolak','Bubb','M\'Quharg','Yuille','MacGiffin','Hamments','Luther','Lenham','Jewer','Rosenbarg','Koppen','Jepensen','Clemson','Chiommienti','Tiler','Prestidge','Parrott','Fridd','Slewcock','Sharpling','Henden','Coppen','Zannuto','Skep','Semmence','Kinig','Kobera','Sclater','Cordsen','Longdon','Goozee','Benton','Lourens','Lucock','Richard','Pauncefoot','Youson','O\'Sheilds','Hatry','Winsome','Barmby','Doret','Wallbridge','Dincke','Bellhanger','Acomb','Nelle','McIntee','Ilyunin','Tunnicliffe','Marcu','Harbin','Caren','Bouller','Donneely','Baskeyfield','Levine','Fenich','Chesshyre','Skrine','McGreay','Neale','Gobell','Bunton','Robrose','Isworth','McNeilley','Fomichyov','Colley','Newall','Glendenning','Ancliff','Varian','Sleeman','Bitcheno','Shepard','Farge','Mawd','Habershaw','Ducrow','Gillice','Brantzen','Stoppe','Konert','Sturman','Dederich','Spencley','Patten','Pales','Claiton','Gorman','Patridge','Fennick','Drysdall','Marciskewski','Gibbe','Mapledorum','McIlmurray','Mallinar','O\'Feeny','Carnelley','Broadey','Strangeway','Dominelli','Amps','Tims','Reinbeck','Conlon','MacGillacolm','Steffans','Broggetti','Tomaszkiewicz','Hurleston','Hicklingbottom','Maharry','Andreu','Eller','Curee','Armal','Andries','Legrave','Soame','Devenport','Rasper','Custard','Piken','Moloney','Bertlin','Marshallsay','Heal','Mumford','Delgardo','Pegg','Garfitt','Rasper','Milton','Cadding','Delieu','Honacker','Santostefano.','Burrow','Ayre','Jeness','Smaile','Downing','Cleugh','Firpo','Tedstone','Aldham','Buckoke','Barwick','Jest','Denisot','Woolpert','Thurgood','Dainton','Arnow','Sutter','Cumberland','Kleinplatz','Lye','Gerner','Bourget','Swede','Friedlos','Aubury','Hathorn','Gowlett','Shewon','Strutz','Mynard','Moulding','Browell','Osmant','Pendergast','Burgett','Trigg','Glasper','Basindale','Tremouille','Kyles','Soeiro','Pinsent','Hiscoe','Kinzel','Chillcot','Escolme','Alsopp','Rowthorn','Womersley','Heggie','Attack','Thorsen','Carsberg','Motten','Wade','Gallant','Hamsley','Hawkshaw','Poag','Tomsa','Pepall','Ronan','Menlove','Leece','Goodlip','Nickoles','Esplin','Davsley','Maffezzoli','Ashington','Isaksen','Dowty','Ewell','Leipnik','Coppen','Renshall','O\'Fihily','Gathwaite','Lawler','Larkkem','Heball','Copland','Studd','Casa','Congdon','Adlard','Primett','Keymar','Danat','McKendo','Greenly','Dodd','Alenichicov','Arderne','Panswick','Avramovsky','Bunstone','Tailby','Camilletti','Joslyn','Maskall','Jindacek','Staden','Corderoy','Moylan','Vedishchev','Schaffler','Bootherstone','Meriton','Andre','Kenny','Greedier','Braunton','Gavan','Lambrook','Vasic','Aucock','Claypool','Bysaker','Janicijevic','Human','Florez','McMahon','Felkin','Brunicke','Coveney','Dallmann','Horry','Tumility','McLaggan','Nowick','Chasier','Hallyburton','Houchen','Attle','Extal','Hardacre','L\' Estrange','Oiseau','Moretto','Mustin','Garr','Swannie','Goldby','Whiteoak','Shreenan','Hoble','Trahar','Dodge','Pile','Beacock','Amsberger','Campos','Ireson','Hallsworth','Sloey','Kuschek','Stevings','Maginn','Davio','Rentcome','Mills','Fakeley','Flippen','Lamers','Kemster','Mattholie','Bencher','Skeemer','Spikeings','Watchorn','Trevan','Cudby','Othick','Denkin','Strachan','Traut','Kendle','Mehaffey','O\'Cosgra','Pullin','Poon','Hartridge','O\'Sheerin','Bonds','Eudall','Balnave','Kern','Fante','Frude','Kerman','Wollaston','Brizland','Wytchard','Grimsdell','Spears','Van Der Vlies','Gilston','Dmych','Boosey','Denisot','Dennert','Ewbach','Crosseland','McDunlevy','Vargas','Gandrich','Mouland','Weldrake','Dunston','Karolowski','Tiebe','Thairs','Le Breton','Crafts','Maple','Bowlas','Suffe','Honniebal','Warr','Barrick','Steers','Von Welldun','McRoberts','Ansell','Gribbin','MacHostie','Legrice','Sepey','Fourcade','Emslie','McGowan','Adamowitz','Barlace','Boycott','Sushams','Jurasz','McTrustie','Sheldon','Beetles','Towse','Gaylor','Treacy','Gallie','Petch','Abys','Dyson','Fleetwood','Gunnell','Dulinty','D\'Adamo','Dahl','Bales','Rhyme','Deyenhardt','Smartman','Pickersgill','Sopp','Lidgey','Speariett','Teek','McDuffy','Clearley','Bakesef','Allbon','Flade','Deverson','Woollends','Pressman','Kinnear','Godon','Brosini','Doley','Colquete','Davidovsky','Brahms','Hearne','Lawes','Demsey','Harbron','Narey','Kick','Lezemere','Canton','Grisbrook','Lowrey','Mullord','Carlaw','Mackilpatrick','Scrange','Wansbury','Case','Skowcraft','Arlow','Robard','Tottem','Mitham','Shaxby','Beards','Killbey','Speller','Straffon','MacArthur','Brou','Gerrie','Dalgardno','Macieja','Posse','Bee','Tubble','Lisett','Awton','Headon','Bingle','Gallant','Vellacott','Elgood','Sagar','MacKeig','Jerrold','Sutlieff','Huws','MacIntyre','Elfe','Jenk','Sapsforde','Bryant','Hamblett','Kennett','Willingam','Elsop','Pavyer','Starte','Routhorn','Geram','Ingerman','Arthey','McNeely','Tyres','Gyrgorwicx','Golsworthy','Kittel','Mishow','Ellingford','Shillaber','Liccardo','Dermot','McAviy','Kondrachenko','Udale','Canfer','Attard','Lumsdall','Urch','Gellibrand','Spratley','Tingly','Barnaby','Northall','Collyear','Carder','Buckles','Barbe','Knaggs','Sparshatt','Moxted','Winterbottom','Tams','Shipman','Worgan','Kabsch','Beckhurst','Cheyne','Edgerly','Dossit','Ugolini','Reaveley','Skylett','Youson','Catterall','Wreath','Oxley','Drakard','Edgar','Fagge','Slocomb','Di Boldi','Elph','Drains','Binion','Croley','Klawi','Enrietto','Botting','Marcinkowski','Jolliman','Whithorn','Ellingworth','Barg','MacGillavery','O\'Donoghue','Walkden','Mylechreest','Collen','Charge','McCarrick','Colbert','Polgreen','Pudan','Shire','Kochel','McClinton','Iacovides','Abbitt','Brogini','Kynman','Selwood','Burkitt','Elcomb','Phittiplace','Dalgliesh','Falshaw','Dionis','Boolsen','Walicki','Murdoch','Simpkin','Grolle','Hartley','O\'Cooney','Cuchey','Buckel','Matisoff','Schild','Durnill','Clough','Cregg','Merchant','Basil','Blackie','Teodoro','Lars','Flaherty','Pescod','Urion','Hallows','Lechelle','Radcliffe','Letherbury','Seiter','Boscott','Jiroutek','Gilberthorpe','Richter','Sparey','Fairlaw','Hounihan','Cramer','Ketch','Bagnall','Rocco','Blakelock','Pic','Jasiak','Poolton','Loyd','McBrady','Hark','Adelsberg','Seeviour','MacTavish','Skokoe','Samson','Ioannidis','Stirton','Blackney']
		if '\n' in (data):
			data=data.splitlines()
			for i in range(len(data)):
				data[i]=lastname[randrange(1000)]
			return '\n'.join(data)
		else:
			return lastname[randrange(1000)]

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)



class datawizardrandomphonenumberCommand(sublime_plugin.TextCommand):
	def format(self,data):
		phoneNumber=['642-676-0007','885-456-5600','126-430-2362','975-569-7120','746-861-5754','416-206-2775','135-113-5860','802-143-7980','250-984-8715','674-195-4938','477-523-9602','533-275-9883','661-749-8395','199-878-4479','873-672-3637','970-145-6132','137-940-4235','899-591-7961','894-560-5600','596-948-3838','259-957-0514','732-888-0682','947-608-1769','441-868-5417','973-602-3987','221-605-3141','265-280-8717','849-917-0873','882-939-7767','136-770-6620','903-423-3337','100-342-9436','454-711-8185','176-870-5514','144-450-1496','548-216-0754','529-610-3586','325-813-4494','955-231-6936','985-876-8382','512-159-4992','768-552-1894','363-958-3438','530-818-0828','866-646-6574','934-168-9401','545-963-1570','276-372-6109','498-140-2251','396-685-9996','714-562-9836','953-684-9656','622-432-1792','534-803-3723','800-897-2346','515-928-8772','988-771-5023','923-855-9625','679-101-5193','808-827-4598','812-580-4846','812-970-7616','779-542-2898','804-583-5226','728-415-2895','914-120-9827','523-183-7118','214-254-7212','877-943-6145','963-784-1601','602-836-7706','364-613-2679','195-238-1284','860-632-5701','220-926-2632','607-980-9979','985-794-3384','335-697-9961','292-986-5943','392-707-9096','845-779-1604','351-419-3115','403-343-4629','602-796-7094','718-801-4366','369-902-3147','342-794-7106','453-391-5898','227-882-4376','850-770-4984','325-589-5808','655-210-4269','806-542-7195','792-525-8291','718-107-1222','788-238-3872','379-241-4182','993-256-6488','301-835-9403','317-304-7514','741-110-8179','774-862-5766','800-738-4931','347-751-2667','442-780-8857','999-813-1028','909-550-4943','198-171-8118','507-891-6082','743-975-0642','132-761-3145','808-693-6193','923-770-4873','850-221-6072','963-173-0444','201-704-2862','340-326-2517','649-524-9318','418-483-8040','170-628-0753','917-432-1878','227-158-4308','884-118-5084','414-153-7438','959-127-9178','982-495-4070','839-704-9094','282-542-3848','668-822-4813','300-116-5716','559-178-4556','735-338-2106','755-368-0246','623-769-1531','857-570-0583','990-244-1876','733-568-4489','312-745-6276','373-519-5492','967-609-7858','292-927-1202','770-766-0756','816-977-4835','907-247-8909','213-544-1853','411-371-0297','872-478-8284','326-506-9163','960-114-6878','519-578-1955','690-426-2577','656-150-6200','407-162-6279','940-781-1833','453-548-8139','827-994-3519','819-814-9597','486-230-4920','907-912-9052','724-886-8755','167-798-9492','617-720-1709','787-935-7358','739-202-1551','703-341-2107','413-231-6352','200-379-4581','470-300-3755','822-181-3539','859-237-7780','226-601-5917','647-605-2158','544-253-5166','497-438-9669','553-773-4038','414-809-8004','149-709-8035','971-919-1742','985-460-1306','906-476-6788','499-744-9808','995-983-1867','667-495-4356','679-842-0155','145-163-1483','889-273-7520','229-563-9657','375-104-8276','291-487-3008','511-289-4289','504-743-8925','619-974-6022','141-699-4924','714-916-8155','302-201-8796','915-689-7973','454-443-6117','979-790-8731','802-182-3107','907-408-2589','279-941-5843','288-177-8082','859-436-6648','670-614-9072','821-771-0963','477-786-0657','893-518-6108','648-771-2945','790-990-0062','292-616-1942','676-453-0605','954-337-1901','434-790-8351','212-717-2982','947-915-3616','172-516-1757','120-772-7216','147-228-5103','386-680-7555','404-649-3321','269-903-9099','180-716-1300','922-336-2786','789-522-1552','429-364-2709','162-385-9514','662-507-5853','965-866-5902','577-964-3654','857-274-8792','252-801-2686','811-744-7257','218-902-0785','945-846-7116','239-833-1166','178-931-8757','698-879-2851','420-681-0027','449-416-1897','338-160-7764','147-477-8446','198-297-4871','307-304-1950','837-218-5245','451-580-3630','143-739-5680','797-929-7250','984-116-0230','285-971-5031','773-677-6675','954-490-0089','567-760-9413','289-294-0573','167-989-7517','494-875-1336','197-344-5024','924-554-6172','717-966-3971','560-350-9044','928-862-4194','233-671-5397','483-883-3965','903-994-3854','453-799-0364','337-965-7531','462-629-7018','554-888-9253','111-773-6350','350-729-2785','810-101-0763','524-529-5890','726-937-1696','715-886-8222','250-599-0932','865-275-0137','295-891-3991','793-738-5693','468-904-3798','697-749-1168','922-651-7348','772-248-9272','946-985-5980','693-129-2504','745-959-2415','170-895-0369','137-457-9490','366-276-0785','629-385-2374','465-136-9883','132-249-3502','613-641-5540','468-994-1129','127-847-3190','178-389-3525','430-436-5930','427-549-6599','247-194-2226','328-878-6716','704-106-4812','483-343-4946','994-745-5925','549-789-4883','821-897-7640','187-121-9169','362-735-9366','271-946-7964','325-155-7157','101-834-7013','832-640-8208','324-404-6971','194-420-2480','228-816-0732','557-662-2893','784-869-8981','320-794-9243','144-419-8890','735-729-0671','639-706-8334','568-694-4641','720-843-5992','437-572-8201','733-998-9674','627-751-2900','114-602-4948','530-683-1614','480-581-2957','132-905-5248','451-587-8867','846-698-0562','722-640-1916','229-312-2966','475-349-9575','270-368-0181','660-986-0007','174-592-0666','740-191-7165','857-382-2466','634-713-8740','940-846-6880','270-662-2579','377-485-1022','618-987-6544','912-740-8569','839-121-9251','509-394-7206','696-596-2905','807-774-0901','126-599-4333','366-928-1534','155-854-2392','583-952-3931','495-835-0730','455-928-0576','139-633-7388','957-722-8647','244-765-3163','953-874-3617','936-281-4957','629-458-2045','917-867-2575','207-402-3980','173-653-4121','340-720-4839','799-633-5621','648-921-9431','716-218-1926','350-809-9100','804-215-4506','990-499-1733','912-553-2814','254-120-7717','720-669-8862','441-293-4684','516-300-8878','369-196-9991','576-385-7002','274-843-8963','861-259-5555','736-719-2286','648-300-3251','136-318-2217','361-490-1125','484-139-3751','595-749-3149','794-961-9254','313-613-3518','182-493-9176','869-437-1751','257-132-0732','122-662-9382','922-590-5664','408-957-0024','528-164-9896','360-957-6657','730-400-7490','357-434-5248','447-228-7492','314-330-7557','168-787-1930','211-604-2924','628-687-5298','694-518-4100','807-285-9739','591-890-8350','893-801-7623','887-115-5257','686-935-8163','562-364-8311','327-543-6332','204-301-3351','862-956-9580','199-209-5849','579-848-9378','765-179-8103','705-820-8428','194-444-7734','320-385-3574','315-701-1689','453-275-6519','302-697-6123','247-784-3472','835-239-8724','339-725-5601','821-279-2760','552-673-8004','358-349-5904','598-148-1989','319-443-0520','268-958-0803','940-200-6004','478-588-4625','349-396-6250','625-226-0165','277-838-2178','503-413-7772','324-216-5276','663-376-5521','846-171-5008','543-435-1159','121-700-8371','259-839-1013','225-153-0101','684-353-7902','527-511-4618','537-800-7127','912-150-6188','304-877-2771','318-557-1315','842-347-5073','100-893-3929','508-440-8861','177-646-4099','555-518-7820','982-191-8267','406-304-7294','870-554-3023','553-128-3612','222-240-8170','571-482-9585','333-399-5451','776-912-4925','791-409-8024','264-434-5989','190-666-8107','313-496-7640','202-466-6515','765-547-9282','269-658-1684','742-207-0389','995-743-4548','229-348-2811','856-341-2694','733-882-8046','192-835-5505','434-785-8533','655-839-1041','250-755-6189','151-151-4800','774-194-0496','218-449-7558','306-810-6617','919-472-5611','556-796-8500','261-649-5829','513-458-6050','138-745-2776','936-809-9927','324-974-5511','618-155-6633','295-810-4608','660-165-8894','293-583-0729','525-162-6857','236-224-4537','263-753-9041','434-172-2774','993-103-6124','392-739-8764','919-888-6748','492-597-1610','668-595-8535','709-285-1149','344-342-8788','522-296-2819','468-868-9436','326-979-7517','440-488-0526','152-163-9330','749-493-6171','312-693-5049','832-902-4045','603-984-8972','219-877-3771','577-991-8283','490-288-2097','649-139-2523','300-343-4101','776-351-3571','766-228-3291','372-389-4193','627-446-3832','311-556-1787','596-781-8878','711-293-0920','271-999-7127','699-517-1948','544-681-2806','654-641-0867','755-164-7964','798-240-2819','265-129-5883','437-194-0233','463-897-3815','534-212-6924','142-940-4097','467-243-1177','751-421-8205','869-376-5863','902-151-2583','736-836-9877','757-487-5623','627-956-8586','946-721-0354','441-110-1848','545-367-4619','761-128-3035','534-346-9989','327-152-2375','836-929-8331','298-737-7703','868-265-9149','510-222-6361','883-162-8217','212-675-1205','179-759-1070','324-102-9447','748-611-1304','750-673-9160','147-141-9736','823-705-4572','224-160-8924','257-134-8311','543-673-9686','527-179-6722','814-197-2798','224-481-6581','710-615-1849','880-395-3688','260-596-4796','904-502-6202','588-265-1575','916-823-7814','594-556-1674','102-682-8318','202-451-8671','832-325-8092','482-122-6130','706-566-5348','521-625-8624','878-782-3054','147-285-5222','148-442-0720','131-838-0520','504-297-7324','735-237-2148','680-673-4856','259-285-3737','788-538-4662','514-207-3336','201-955-3766','754-774-5860','202-586-0754','420-827-9892','539-926-2727','501-963-0492','583-351-6584','396-331-2644','239-330-3571','128-321-7258','771-175-0475','476-525-0563','652-849-7625','341-599-5109','784-268-6748','190-604-8733','588-155-0617','725-884-2385','851-628-4212','227-147-2952','724-984-0905','385-904-2208','936-521-4367','278-823-2597','753-806-4146','981-973-4210','471-363-6826','788-655-1557','417-371-6799','760-271-2056','596-711-9413','589-383-3966','792-786-2321','286-671-9259','691-611-8950','666-253-3556','239-739-7663','654-432-1350','568-304-9533','259-919-0130','289-660-6739','383-748-9539','968-265-7864','402-123-7378','646-106-1390','524-799-5657','834-426-9622','159-230-4187','150-817-7608','107-549-5509','452-111-1671','655-547-1928','198-890-0834','295-595-8623','968-175-6617','452-416-6529','612-386-5714','390-375-6714','483-168-8352','173-768-7674','288-701-9503','439-284-5414','139-143-0608','373-404-8049','965-832-0220','340-177-6349','465-741-2958','171-383-4683','740-525-1548','277-529-5321','111-513-7414','174-825-7382','199-192-8425','857-135-4583','677-319-0361','225-140-4889','224-602-9877','544-612-8473','750-495-5625','282-518-3221','484-971-9844','929-634-5364','621-379-9787','632-463-4275','812-927-5271','915-609-1849','437-303-5748','745-714-0632','924-587-8314','447-956-6610','607-796-1945','774-755-3937','537-111-0861','141-424-4555','899-848-4210','741-855-1038','553-208-3140','772-527-8868','664-496-8405','515-395-6163','637-178-8735','770-122-8812','748-610-3883','556-412-6777','959-314-0420','733-986-2527','569-461-8179','113-587-6646','182-447-1482','229-840-3238','964-331-3735','479-666-9905','400-993-1787','480-426-6575','164-499-7948','571-963-7229','361-416-6643','602-866-4483','920-196-3325','705-240-0716','853-648-9425','929-793-0896','480-363-5726','353-848-3700','674-212-6966','594-100-8826','115-181-7278','728-404-7627','563-501-6148','379-866-5480','700-245-1684','453-949-0270','542-599-9201','245-120-3717','892-530-3923','170-764-3512','347-854-6607','267-239-2069','209-500-2571','308-631-9435','190-426-2021','567-831-8462','150-194-3261','692-110-3092','493-998-4537','569-526-3510','226-748-4388','132-144-8870','404-246-1653','559-797-5994','379-418-9735','379-844-0524','981-451-0713','677-235-4430','431-936-6265','175-881-7390','775-966-8833','204-356-5704','202-887-9913','683-440-0047','247-416-7312','944-250-7260','510-398-3076','753-667-1041','916-597-7833','744-436-0825','482-552-9958','598-609-6954','988-357-7052','230-543-1202','139-973-1144','686-689-1576','515-474-0337','803-946-3010','854-253-1380','501-330-8031','612-629-0430','129-101-1347','264-756-6992','484-648-3831','923-704-3185','323-826-4002','213-877-0709','835-300-4108','965-374-3713','413-781-7411','604-396-4029','477-556-1184','914-709-8914','953-888-7542','940-192-3981','569-222-0412','959-485-3528','241-691-4148','174-639-3256','963-511-7777','729-394-9476','603-387-1694','313-701-6301','559-856-9033','562-687-7270','758-625-2151','316-262-3196','877-498-4021','453-937-4044','362-422-8738','375-236-9958','308-852-2724','791-573-5961','516-130-8074','116-753-1296','893-816-8011','842-358-0881','277-266-3795','111-530-2554','636-182-7271','119-154-7642','913-566-9973','472-296-2420','873-619-1179','395-693-5047','463-666-5005','584-133-4028','325-218-8432','824-824-1428','767-172-5121','321-899-5648','714-378-4254','666-937-7068','370-475-3892','746-330-8527','852-663-1199','455-754-6843','810-646-7929','817-164-0051','232-942-7120','417-465-2533','272-327-3758','689-693-4267','836-265-1842','555-113-1818','945-571-9841','581-704-1508','515-516-8920','364-188-8375','724-953-8233','303-258-5407','182-564-1500','887-630-1342','358-200-4177','934-246-6802','988-963-1491','596-400-0359','881-286-1787','579-530-3624','323-740-3679','419-338-7002','199-457-4353','500-763-6264','208-574-5823','949-740-2628','198-725-4175','985-328-0190','718-400-4831','673-696-4117','212-872-8832','198-683-3332','392-863-8430','243-498-1845','480-431-1642','847-162-6245','142-328-1414','278-914-8451','217-929-7679','469-730-8375','173-118-8777','779-733-1696','381-368-2627','227-171-7081','484-113-4687','366-351-1398','191-469-4766','282-691-8458','312-861-8825','636-718-7481','496-128-1243','902-873-4395','333-659-4200','426-851-9450','496-891-1362','571-734-7257','414-177-8334','241-872-8874','551-139-7548','894-488-1896','527-534-1930','917-422-5563','671-386-8009','209-640-4920','936-661-2202','149-674-6590','247-937-2028','630-806-3696','644-506-3840','383-383-0200','732-955-7146','992-282-3504','620-427-9674','160-403-0432','231-522-8829','484-781-2340','112-530-5758','626-792-2414','843-143-5203','889-752-4645','222-484-2137','894-701-4671','879-543-5126','713-534-0418','510-161-7147','911-669-8011','391-749-7614','716-673-4191','621-464-7055','595-300-9835','407-761-9151','741-996-4581','984-199-9791','299-173-2507','415-724-9376','357-419-2769','527-283-6417','262-202-5262','664-252-7408','109-984-7120','809-607-3806','928-301-6255','397-434-7897','441-302-2767','346-579-5752','181-376-3035','473-628-4963','301-568-5558','702-595-5267','581-817-3219','487-987-1311','633-255-5160','972-148-7259','385-797-7623','739-131-5613','698-827-0572','132-289-1995','225-309-7970','292-803-9592','646-806-8912','544-316-7949','782-633-8168','953-404-6102','403-502-3808','775-867-7841','711-382-6943','420-603-2601','918-136-0428','124-198-7864','962-488-9136','953-630-1812','789-529-0730','892-481-6488','990-419-6361','891-562-8931','238-260-1691','727-257-2422','421-654-1859','910-514-0356','487-639-2958','451-923-0483','936-399-6593','158-395-8322','485-146-1509','387-321-2261','432-471-4233','850-423-9847','775-781-9368','640-312-4511','466-507-5099','646-780-2329','280-157-1412','780-729-6199','439-826-1597','330-201-9678','225-897-1260','919-414-5371','840-309-1815','294-429-0461','146-636-2952','473-314-4282','268-689-7244','297-247-4856','459-834-8006','922-775-5986','803-773-1884','532-751-7822','424-812-1909','235-286-8620','500-658-1467','887-610-5789','109-187-0364','867-975-9817','579-928-6445','237-777-5993','672-224-9566']
		if '\n' in (data):
			data=data.splitlines()
			for i in range(len(data)):
				data[i]=phoneNumber[randrange(1000)]
			return '\n'.join(data)
		else:
			return phoneNumber[randrange(1000)]

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)

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




class datawizardrandomstateabbvCommand(sublime_plugin.TextCommand):
	def format(self,data):
		stateabbv=['DC','AZ','KY','IA','NC','CO','CA','MI','OH','RI','NV','OK','FL','TX','LA','FL','OH','NY','FL','NJ','NY','VA','MI','TX','NC','KS','FL','CA','LA','PA','GA','AR','KS','FL','AL','LA','SD','WI','TX','NC','AL','NY','TX','PA','CO','ND','TX','LA','TX','CT','NY','WV','CA','CA','CT','MN','TX','MD','NY','KY','FL','NE','CA','IL','CA','WI','KY','NE','TX','TX','CA','NM','TN','TX','GA','CA','KS','IL','DC','CA','IA','TX','IL','NY','PA','AK','CA','WA','PA','TN','NC','OH','MA','CA','MA','NC','OK','NE','TX','MI','OK','IA','FL','OH','DC','FL','CA','AL','TX','KS','TX','WI','CO','AK','NY','NJ','IL','NY','FL','WA','FL','PA','IN','UT','ID','DC','MS','CA','MN','UT','KY','CA','NC','VA','NY','PA','TX','VA','DC','NC','FL','WA','FL','VA','NC','CA','FL','CA','TX','NC','VA','NC','TX','ID','MI','DC','DC','PA','CA','CA','OK','ID','OH','VA','WA','NV','TN','VA','TX','VA','IL','MO','CA','OH','ND','FL','TX','CA','IL','WV','IL','TX','VA','SC','AZ','FL','CA','MA','SC','MD','DC','AZ','AR','NV','DC','VA','MO','MI','PA','FL','NC','FL','CA','CT','CA','CO','CO','AL','NC','NV','AL','IN','DC','TN','DC','IA','TX','NM','DC','TX','VA','CO','FL','CO','UT','GA','MO','KS','PA','NY','MN','DC','TX','TX','OR','GA','CA','KY','PA','IL','WA','NM','FL','IL','WA','AZ','OH','CA','MD','TX','TX','CA','FL','MO','TX','VA','AZ','AL','TX','NY','CA','TX','NY','NE','LA','SC','WI','CA','CA','OH','NC','OK','VA','AZ','MI','MO','IN','WV','FL','ID','TN','WV','KS','TX','IN','CA','NM','FL','CA','TX','CT','CO','MO','NY','MA','MN','CA','FL','OK','TX','CA','AL','CT','IL','NJ','NY','KS','MO','GA','AL','NV','OH','KS','CA','CT','MN','VA','SD','MO','MO','VA','MO','LA','CA','NY','DC','UT','NM','NY','OK','CA','TX','OH','WA','OH','NC','OH','CA','NC','MI','FL','DC','CA','FL','LA','CA','DC','IL','MO','AZ','TN','SC','WV','CA','CA','CA','LA','OK','KY','IN','OH','DC','CA','DC','AZ','GA','TX','OH','WI','TX','NE','CA','PA','TX','CA','NY','FL','TX','NY','NY','CA','AK','OH','NJ','FL','UT','MI','CA','HI','KY','MO','VA','AL','CA','OH','PA','NC','OH','AZ','VA','FL','MN','TX','GA','TX','OH','TX','PA','NV','AL','MT','FL','MI','IL','WV','MO','OR','CT','MO','NC','DC','NH','AL','OH','FL','IL','OR','MA','OH','OH','PA','IN','OH','AR','CA','WA','TN','WV','WA','CA','CA','WA','NV','FL','DE','GA','CA','MN','NY','NH','WV','MO','FL','CA','SC','AZ','TX','TX','GA','NE','GA','WV','TX','DC','MI','TX','CA','SC','NY','AZ','NV','OK','SC','TX','OH','NM','TX','VA','CA','NY','OH','KS','KS','WA','OK','TN','TX','MS','OR','CO','CO','KS','IL','NV','NE','NC','CA','MN','TX','DC','MN','CA','WI','MN','DC','TX','TN','NC','TN','CA','NH','IN','KS','MN','FL','TX','TX','VA','UT','WI','NV','WA','TX','HI','TX','MA','CA','TX','LA','KS','DC','VT','MO','LA','CA','FL','MS','OH','TX','CA','OK','MO','DC','KS','OH','NH','DC','TX','UT','AZ','AL','IL','SC','CA','NY','NC','WV','TX','OH','IN','OH','OR','CA','NJ','OR','DC','UT','NY','WV','CA','CA','LA','AZ','GA','TX','TX','KY','CA','GA','CA','CA','MD','NC','CA','MO','PA','CA','NY','FL','FL','CO','VA','VA','NY','TX','FL','NY','TN','AL','MT','CO','GA','IN','MD','DC','MO','PA','AL','NC','VA','MO','PA','DC','NY','SC','OK','TX','HI','TX','SC','NC','NE','OH','TX','TN','OK','MN','MT','MN','NY','CA','CO','TX','CA','PA','TX','AK','WA','TX','NY','TN','WV','MN','TX','TN','IN','NJ','VA','CT','FL','CA','IL','NC','TX','AZ','IL','SC','CA','MA','MI','OK','MN','FL','WA','NY','KY','TX','CA','VA','LA','WA','NJ','CO','OR','LA','CO','NC','MA','CA','NV','TX','IL','MA','VA','NE','NY','NE','CA','CA','CO','TX','NY','CA','OH','CA','NY','NY','OK','NC','WV','WV','OH','TX','MN','MA','CA','MN','FL','DC','OH','HI','NY','MI','IL','CO','MO','PA','WI','VA','CA','LA','NY','FL','GA','TN','UT','IL','CA','LA','CO','LA','MI','IN','TN','PA','NY','NY','FL','CO','FL','MA','MO','MI','NC','LA','MI','MN','NY','OK','CA','WA','VA','LA','TX','SD','MS','CT','KS','FL','FL','UT','AZ','FL','TX','OH','TX','MS','WA','TN','CA','TX','CT','GA','TN','AZ','CA','TX','IL','UT','OH','CO','CA','CA','IL','RI','MD','TX','WA','OH','CA','FL','CA','OH','TX','GA','MO','OH','MD','CA','ID','CA','TX','AL','AL','TN','MN','CA','MN','DE','CA','IN','LA','FL','FL','OK','VA','PA','CA','PA','TX','WA','ID','FL','CA','CA','CT','KS','CA','TX','AL','LA','OH','TX','FL','OH','WI','MA','PA','WV','WA','MO','PA','FL','IN','TX','HI','CA','NY','AZ','NY','OH','PA','GA','CA','VA','MI','OK','TX','CA','TX','HI','LA','OK','MI','TX','GA','GA','NY','NY','MI','LA','NY','CT','TX','CO','NC','MN','MO','CO','NE','OH','KY','NC','MO','TX','NY','TX','WV','TX','GA','NY','TX','FL','MI','CA','NC','TX','FL','LA','TX','TX','DC','AL','TN','NE','TX','CA','FL','VA','PA','KY','TX','CA','CA','TX','PA','GA','PA','NY','MI','CA','AZ','CA','AZ','CA','IL','ID','ID','LA','NY','TX','NY','NY','OK','VA','TX','IL','CO','CA','MI','WA','NC','IL','CT','KY','OK','OH','FL','DC','WA','NY','FL','CA','MA','MA','OK','PA','CO','NM','NY','NY','LA','FL','OH','TX','MI','PA','MN','FL','VA','PA','TN','PA','FL','CA','IN','NV','MD','CA','CA','CT','OH','WV','CA','CA','WV','CT','SD','CT','FL','NJ','PA','AZ','TX','PA','SC','IA','FL','FL','TX']
		if '\n' in (data):
			data=data.splitlines()
			for i in range(len(data)):
				data[i]=stateabbv[randrange(1000)]
			return '\n'.join(data)
		else:
			return stateabbv[randrange(1000)]

	def run(self, edit):
		for region in self.view.sel():
			inData=self.view.substr(region)
			outData=self.format(inData)
			self.view.replace(edit, region, outData)

class datawizardstatisticssampleCommand(sublime_plugin.TextCommand):
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

