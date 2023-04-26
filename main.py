"""
get the 10 lastest commits from a git-hub repo
show
    hash
    author
    message
    date and hour
"""

from datetime import datetime
import requests

URL_REPO = 'https://api.github.com/repos/mouredev/retos-programacion-2023/commits'

def show_repo_data(data: list):
    """
    show data in console
    """
    for i in range(10):
        sha = data[i]['sha']
        author = data[i]['commit']['author']['name']
        message = data[i]['commit']['message'].replace('\n','')
        date_commit = data[i]['commit']['author']['date']        
        date_commit = datetime.strptime(date_commit,'%Y-%m-%dT%H:%M:%SZ')
        date_commit = date_commit.strftime('%Y-%m-%d %H:%M:%S')
        print(sha, author, message, date_commit, sep = '|')


def make_request(url_repo: str):
    """
    making a request
    """
    response = requests.get(url_repo)

    if response.status_code == 200:
        json_data = response.json()
        show_repo_data(json_data)
    elif response.status_code  == 404:
        print(response.status_code)
        print("Can't get a response from remote host")
    else:
        print("An error has ocurred")


make_request(URL_REPO)
