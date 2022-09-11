
import os
import shutil


def produceMetrics():

    clearMetrics()

    print(' [*] - Clear metricts and generate again!')
 
    os.system(
        'java -jar ./jar/ck.jar ./project/clone/ true 0 false'
    )


def clearMetrics():

    if os.path.exists('./jar/metrics/'):
        shutil.rmtree('./jar/metrics/')
