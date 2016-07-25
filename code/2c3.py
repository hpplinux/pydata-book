import pandas as pd
import numpy as np

df=pd.DataFrame({'key1':['a','b','b','a','a','b'],
		'key2':['one','two','one','one','two','one'],
		'data1':np.random.randn(6),
		'data2':np.random.randn(6)})


print df
print "\n\n\n",df['data1']
sums=df['data1'].groupby([df['key1'],df['key2']]).sum()
print "\n\n\n",sums

print "\n----------------------------------\n"
print sums.unstack()

states = np.array(['Ohio', 'California','Ohio', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006,2006])

print "\n\n",df['data1'].groupby([states,years]).sum()	


print "\n----------------------------------\n"
print df.groupby(['key1','key2']).mean()


print "\n----------------------------------\n"
for name,group in df.groupby('key1'):
	print name,"\n",group


print "\n----------------------------------\n"

print type(df.groupby('key1'))

pieces=dict(list(df.groupby('key1')))

print pieces['b']

print "\n----------------------------------\n"
print df.dtypes


print "\n----------------------------------\n"
print df.groupby('key1')['data1'].mean()

print "\n----------------------------------\n"
print "\n----------------------------------\n"
print "\n----------------------------------\n"

