import json

filename="../ch02/usagov_bitly_data2012-03-16-1331923249.txt"

f=open(filename)

lines=f.readlines()

records=[ json.loads(line) for line in lines]

print len(records)

print records[0]['tz']


dict={}

for item in records:
	if item.get('tz')==None:
		continue
	if dict.get(item['tz'])==None:
		dict[item['tz']]=1
	else:
		dict[item['tz']]+=1


print '\n---------------------\n'		
print json.dumps(dict,indent=4)



#print json.dumps(records[0],indent=4)

