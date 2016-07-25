import json

filename="../ch02/usagov_bitly_data2012-03-16-1331923249.txt"

f=open(filename)
lines=f.readlines()

records=[json.loads(line) for line in lines]

print records[0]

timezone=[rec['tz'] for rec in records if 'tz' in rec]

cout={}

for tz in timezone:
	if tz in cout:
		cout[tz]+=1
	else:
		cout[tz]=1

vk_pair=[(count,tz) for tz,count in cout.items()]
vk_pair.sort()



print "\n---------------------\n"

print json.dumps(vk_pair[-10:],indent=4)








