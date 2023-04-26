"""
get the 10 lastest commits from a git-hub repo
show
    hash
    author
    message
    date and hour
"""

import requests

try:
    response = requests.get('https://api.github.com/repos/mouredev/retos-programacion-2023/commits')
    if response.status_code == 200:
        data = response.json()
except:
    print("Can't get a response from remote host")


#print(data[0]['sha'])
#filtered_data = 


for i in range(10):
    print(data[i]['sha'], data[i]['commit']['author']['name'], data[i]['commit']['message'].replace('\n',''),data[i]['commit']['author']['date'], sep=' | ')
