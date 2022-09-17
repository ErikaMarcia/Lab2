from service.graphrequest import callGitApiPaginated
from utils.parsedata import isPopulatedFile, iterateAndGenerateMetrics,  parseRepositoriesToCsv

GIT_URL = 'https://api.github.com/graphql'

if (isPopulatedFile()):
    iterateAndGenerateMetrics()
else:

    resultData = callGitApiPaginated(GIT_URL)
    parseRepositoriesToCsv(resultData)
    iterateAndGenerateMetrics()
