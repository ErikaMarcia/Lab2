

from service.metriccalculator import generateMetrics
from service.projectmanager import clearProject, cloneProject
from models.resultmodel import ResultModel
import json
import pandas

CSV_FILE = 'csv/REPOSITORIES_WITH_METRICS.csv'


def isPopulatedFile(): 
    
    try:
        df = pandas.read_csv(CSV_FILE)
        return len(df) >= 1000
    except: 
        return False


def parseRepositoriesToCsv(data):

    result = []
    for value in data:

        singleResult = ResultModel.toJson(
            value['id'],
            value['nameWithOwner'],
            value['createdAt'],
            value['primaryLanguage'],
            value['stargazers'],
            value['releases']
        )

        result.append(singleResult)

    saveInFile(result)

    return result


def iterateAndGenerateMetrics():
    df = pandas.read_csv(CSV_FILE)

    for index, row in df.iterrows():

        try:

            if (row['CBO'] != "-" and row['LOC'] != "-"):
                print(' - ')
                continue

            

            metrics = buildMetrics(row['ProjectName'])
            
            
            
            df.loc[index, 'CBO'] = str(metrics['cbo'])
            df.loc[index, 'DIT'] = str(metrics['dit'])
            df.loc[index, 'LOC'] = str(metrics['loc'])
            df.loc[index, 'LCOM'] = str(metrics['lcom'])

            df.to_csv(CSV_FILE, index=False)

        except Exception as e:
            print("EROR ON BUILD METRICS OF PROJECT - ", str(e), " - ", row['ProjectName'])


def buildMetrics(projectName):
    
    if (cloneProject(projectName)):
        metrics = generateMetrics()
        
        if (metrics is None):
            print('Error')
            return
        
        print('Clean project')
        clearProject()

        return metrics


def saveInFile(result):
    if (result is None):
        print('Error')
    else:
        json_string = json.dumps(result)

        df_data = json.loads(json_string)
        df = pandas.DataFrame(df_data)

        df.to_csv(CSV_FILE, sep=',', encoding='UTF-8')
