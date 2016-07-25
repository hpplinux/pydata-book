import pandas as pd

unames=['user_id','gender','age','occupation','zip']

users=pd.read_csv('/root/pydata-book/ch02/movielens/users.dat',sep='::',names=unames,engine='python')

rnames=['user_id','movie_id','rating','timestamp']

ratings=pd.read_csv('/root/pydata-book/ch02/movielens/ratings.dat',sep='::',names=rnames,engine='python')

mnames=['movie_id','title','genres']
movies=pd.read_csv('/root/pydata-book/ch02/movielens/movies.dat',sep='::',names=mnames,engine='python')


data=pd.merge(users,ratings)

data=pd.merge(data,movies)


print "\n\n users.head()\n",users.head()	
print "\n\n ratings.head()\n",ratings.head()

#print "\n\n data\n",data.pivot_table.__doc__


mean_rating=data.pivot_table(values='rating',index='title',columns='gender',aggfunc='mean')

#print "\n\n mean_rating.head()\n",mean_rating.head()	



ratings_by_title=data.groupby('title').size()

print "\n\n ratings_by_title\n",ratings_by_title[:20]

active_titles=ratings_by_title.index[ratings_by_title>=250]

#print "\n\n",active_titles

mean_rating=mean_rating.ix[active_titles]

print "\n-------------------------------------\n"
print "\n\n",mean_rating



print "\n-------------------------------------\n"

top_f=mean_rating.sort_values(by='F',ascending=False)

print "top_f\n",top_f


print "\n-------------------------------------\n"

mean_rating['diff']=mean_rating['M']-mean_rating['F']
print "diff max \n",mean_rating.sort_values(by='diff')


print "\n-------------------------------------\n"
print "\n-------------------------------------\n"
print "\n-------------------------------------\n"
print "\n-------------------------------------\n"
