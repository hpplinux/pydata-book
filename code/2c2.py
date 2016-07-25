import pandas as pd


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                     index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                      'B': ['B4', 'B5', 'B6', 'B7'],
                      'C': ['C4', 'C5', 'C6', 'C7'],
                      'S': ['D4', 'D5', 'D6', 'D7']},
                       index=[1, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                     'B': ['B8', 'B9', 'B10', 'B11'],
                     'C': ['C8', 'C9', 'C10', 'C11'],
                     'D': ['D8', 'D9', 'D10', 'D11']},
                     index=[1, 9, 10, 11])



df4 = pd.DataFrame({'B': ['B22', 'B33', 'B6', 'B7'],
                  'D': ['D22', 'D33', 'D6', 'D7'],
                  'F': ['F2', 'F3', 'F6', 'F7']},
                 index=[2, 3, 1, 7])


frames=[df1,df2,df3]

print "\n\n",df1
print "\n\n",df2
print "\n\n",df3
results=pd.concat(frames,keys=['x','y','z','w'])
print "\n\n\n",results.ix['y']


print  "\n-------------------------\n"

print pd.concat([df1,df2],axis=1,join='inner')


print  "\n-------------------------\n"
print pd.concat([df1,df2])
print  "\n-------------------------\n"


print "\n",df4

result = pd.concat([df1, df4], axis=0,join='inner')
print "\n",result

print  "\n-------------------------\n"


result = df1.append([df2,df3])
print result

print  "\n-------------------------\n"

result=pd.concat([df1,df4],ignore_index=True,join='inner')

print result	

print  "\n-------------------------\n"
