'''
This module contain function to notify prometheus alert manager to send alerts. Alert manager uses the payload to decide on sending alerts
to team using different channel configured in the alert manager. Alert manager also take care of alert suppression if alert condition still remain
satified.
'''
import requests
import json
from datetime import datetime,timedelta
import yaml

headers={
    "Content-Type":"application/json"
}

def notify_alertmanager(label,annotations):
    try:
        url='http://tibco-app-vp06:9093/api/v2/alerts'
        # we are always setting resolve time to be 2 hour ahead to avoid faster auto resolution by the alert manager.
        now = datetime.now()
        updated_time=now + timedelta(hours = 5.30)
        strtime = str(updated_time).split(" ")
        alert_resolvetime = strtime[0] + "T" + strtime[1].split(".")[0] + "Z"

        payload=[
            {
                "labels":label,
                "annotations": annotations,
                "endsAt" : str(alert_resolvetime)
            }
        ]

        req=requests.request("POST",url,headers=headers, data=json.dumps(payload))

        if(req.status_code==200):
            return("success")
        else:
            return("error")

    except Exception as e:
        return("Alertmanager update failed with error message: " + str(e))


if __name__=="__main__":
    labels={
                "alertname": "moduletest",
                "dev": "sda1",
                "instance": "example2",
                "appName": "MES"
            }
    annotations={

                "alerttime":"2021-01-22 17:40:13.143600",
                "message": "This is a test message"

            }

    print(notify_alertmanager(labels,annotations))