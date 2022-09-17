from utils.gitquerys import getFirstQuery
import requests
import json

pageSize = 100
limitData = 1000 

def callGitApiPaginated(url):

    hasNext = True
    page = None
    data = []

    while(hasNext and len(data) < limitData):
        resultOfApi = callGitByPage(url, page)

        if (resultOfApi):
            hasNext = resultOfApi['pageInfo']['hasNextPage']
            page = resultOfApi['pageInfo']['endCursor']
            data.extend(resultOfApi['nodes'])

    return data


def callGitByPage(url, page):

    query = getFirstQuery(pageSize, page)

    result = requests.post(url,
                           headers={
                               'Authorization': 'bearer '},
                           json={'query': query}
                           ) 
    

    data = json.loads(result.text)['data']['search']

    return data
