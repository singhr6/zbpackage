'''
This module have function to update mongodb nosql database collection.
'''

import pymongo
import yaml

# This function add and  update job status with status and time stamp for last run. This return True if successfully added/updated else false
def send_jobstatus(job_name,status,time,output,joblocation):
    try:
        url = 'mongodb://tibco-adm-vp01:27017/'
        client = pymongo.MongoClient(url)
        db = client['local']
        collection = db['job_status']
        query={"job":job_name}
        newvalues={"$set":{"lastrun":time,"laststatus":status,"jobresult":output,"joblocation":joblocation}}
        update_status= collection.update_one(query,newvalues,upsert=True)
        return update_status.acknowledged
    except Exception as e:
        return("MongoDB operation failed. Error message : " + str(e))

# This function fetch job details based on job name.
def get_jobstatus(job_name):
    url='mongodb://tibco-adm-vp01:27017/'
    client = pymongo.MongoClient(url)
    db = client['local']
    collection = db['job_status']
    query={"job":job_name}
    data= collection.find(query)
    return data


# unit test for this module
if __name__=="__main__":
    #x=send_jobstatus("bw6_monitor1","good","2021-01-21T22:40:00Z","ada","TIBCO-ADM-VP01")
    #print(x)

    x=get_jobstatus("mft_cleanup")
    for i in x:
        print(i)
