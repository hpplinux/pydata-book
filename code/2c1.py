import pandas as pd;

years=range(1880,2011)

pieces=[]
columns=['name','sex','birth']

for year in years:
	path='../ch02/names/yob%d.txt'%year
	frame=pd.read_csv(path,names=columns)

	frame['year']=year
	pieces.append(frame)
	#print pieces[:20]


def add_prop(group):
	birth=group.birth.astype(float)
	group['prop']=birth/birth.sum()
	return group


	
names=pd.concat(pieces,ignore_index=True)

print names.head()

total_birth=names.pivot_table('birth',index='year',columns='sex',aggfunc=sum)

print "\n\n\ntotal_birth\n",total_birth

names=names.groupby(['year','sex']).apply(add_prop)

print "\n---------------------------------\n"
print names

#print "\n birth.sum()====",names.birth.sum()

print "\n---------------111111-----------------\n"

#print list(names.groupby(['year','sex']))[1]

print "\n---------------222222222------------------\n"

def get_top1000(group):
	return group.sort_values(by='birth',ascending=False)[:100]
	#return group

groupd=names.groupby(['year','sex'])
top1000=groupd.apply(get_top1000)
#print top1000

pieces=[]

for year,group in names.groupby(['year','sex']):
	pieces.append(group.sort_values(by='birth',ascending=False)[:100])

top1000=pd.concat(pieces,ignore_index=True)
#print top1000[top1000.sex=='M']



print "\n---------------------------------\n"

#print top1000.pivot_table('birth',index='year',columns='sex',aggfunc=sum)

print "\n---------------------------------\n"

boys=top1000[top1000.sex=='F']
df=boys[boys.year==2000]

print df


print "\n---------------------------------\n"
print "\n---------------------------------\n"
