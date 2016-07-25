import json
from pandas import DataFrame,Series
import pandas

filename="../ch02/usagov_bitly_data2012-03-16-1331923249.txt"

f=open(filename)
lines = f.readlines()

records=[ json.loads(line) for line in lines]

#print json.dumps(records[:30],indent=4)

print "\n---------------\n"



dfs=DataFrame(records)

cleantz=dfs['tz'].fillna('Missing')
cleantz[cleantz=='']='Unknow'

tzcounts=cleantz.value_counts()


results=Series([x.split()[0] for x in dfs.dropna()])

print results[:20]


#print tzcounts[:20].plot(kind='barh',rot=0)


