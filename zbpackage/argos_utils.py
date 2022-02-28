'''
This module contains several function related to argos system.
'''
from influxdb import InfluxDBClient
import json

def update_influxdb(measurement,tag,tag_value,value):
    try:
        host='tibco-app-vp05'
        client = InfluxDBClient(host=host, port=8086)
        client.switch_database('telegraf')
        json_body = [
            {
                "measurement": measurement,
                "tags": {
                    tag: tag_value
                },
                "fields": {
                    "value": value
                }
            }
        ]

        client.write_points(json_body)
        return "success"
    except Exception as e:
        return "There was exception while writing to mongodb. Error is " + str(e)
    finally:
        client.close()

if __name__=="__main__":
    print(update_influxdb('node_mem','node','AN_LB01_VD03',23.0))