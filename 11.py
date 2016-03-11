
from bs4 import BeautifulSoup
import urllib2

name1 = raw_input("give the first name:")
name2 = raw_input("give the second name:")

url1 = urllib2.urlopen("http://www.twitter.com/"+name1)
soup = BeautifulSoup(url1.read())
c=0
for a in soup.find_all('span', 'ProfileNav-value'):
 if(c==0):
  tweets1=a.text
 if(c==1):
  following1=a.text
 if(c==2):
   followers1=a.text
 if(c==3):
   likes1=a.text
 c+=1 

 
  
 

url2 = urllib2.urlopen("http://www.twitter.com/"+name2)
soup = BeautifulSoup(url2.read())
c=0
for b in soup.find_all('span', 'ProfileNav-value'):
   b.text
   if(c==0):
     tweets2=b.text
   if(c==1):
     following2=b.text
   if(c==2):
      followers2=b.text
   if(c==3):
      likes2=b.text
   c+=1    



score1=0
score2=0
if (following1>following2):
  score1+=1
elif(following1<following2):
  score2+=1

if (followers1>followers2):
  score1+=1
elif(followers1<followers2): 
  score2+=1

if (likes1>likes2):
  score1+=1
elif(likes1<likes2):
  score2+=1

if (tweets1 > tweets2):
  score1+=1
elif(tweets1 < tweets2):
  score2+=1

print 'profile', name1, 'TWEETS', tweets1, ',FOLLOWING', following1, ',FOLLOWERS', followers1, ',LIKES', likes1
print ' -profile', name2, 'TWEETS', tweets2, ',FOLLOWING', following2, ',FOLLOWERS', followers2, ',LIKES', likes2
print  'score',score1, '-', score2 