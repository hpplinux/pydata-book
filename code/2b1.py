import pandas as pd

uname=['user_id','gender','age','occupation','zip']

users=pd.read_table('/root/pydata-book/ch02/movielens/users.dat',sep='::',header=None,names=uname)

print len(users)
print users[:20]
print "\n--------------------------------\n"


rnames=['user_id','movie_id','rating','timestamp']

ratings=pd.read_table('/root/pydata-book/ch02/movielens/ratings.dat',sep='::',names=rnames)

print len(ratings)
print ratings[:20]
print "\n--------------------------------\n"

mnames=['movie_id','title','genres']
movies=pd.read_csv('/root/pydata-book/ch02/movielens/movies.dat',sep='::',names=mnames)


print len(movies)
print movies[:20]
print "\n--------------------------------\n"



data=pd.merge(users,ratings)
print "\nmerge 1\n",len(data)
print "\n,merge 1\n",data[:20]

data=pd.merge(data,movies)
print "\nmerge 2\n",len(data)
print "\n,merge 2\n",data[:20]



meanrating=data.pivot_table('rating',rows='title',clos='gender',aggfunc='mean')

print meanrating[:40]



