from google.transit import gtfs_realtime_pb2
import requests
import math
from datetime import datetime
from pytz import timezone
import configparser
import operator
from operator import itemgetter

config = configparser.ConfigParser()
config.read("nyc.ini")
apikey = config["api"]["key"]

def printRoute(id,name,time):
    if time == '0':
        print('\x1b[0;30;41m ' + id + ' \x1b[0m', '\x1b[1;31;40m' + name + '\x1b[0m', '\x1b[1;31;40m' + time + '\x1b[0m', '\x1b[1;31;40m' +  "min" + '\x1b[0m', sep="")
    else:
        print('\x1b[0;30;41m ' + id + ' \x1b[0m', '\x1b[1;32;40m' + name + '\x1b[0m', '\x1b[1;32;40m' + time + '\x1b[0m', '\x1b[1;32;40m' +  "min" + '\x1b[0m', sep="")

dict = {}
dictCount = 0
destinations = {'1': " Van Cort Park 242 St    ",'2':" Wakefield-241 St        ",'3':" Harlem-148 St           "}

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(apikey)
responseString = response.content
feed.ParseFromString(responseString)
if not responseString:
    print("MTA is Busy")
for entity in feed.entity:
     if entity.HasField('trip_update'):
        tu = entity.trip_update
        tr = tu.trip
        rt = tr.route_id
        sc = len(tu.stop_time_update)
        count = 0
        if rt == '1' or rt == '2' or rt == '3':
            while count < sc:
                stu = tu.stop_time_update[count]
                sid = stu.stop_id
                arr = stu.arrival.time
                dep = stu.departure.time
                at = datetime.fromtimestamp(arr)
                dt = datetime.fromtimestamp(dep)
                now = datetime.now()
                tdelta = at - now
                seconds = tdelta.total_seconds()
                minutes = seconds / 60
                final = math.floor(minutes)
                if final < 0:
                    final=1000
                count = count + 1
                if sid == '127N':
                    if rt == '1':
                        dict[dictCount] = final, "1"
                        dictCount = dictCount + 1
                    elif rt == '2':
                        dict[dictCount] = final, "2"
                        dictCount = dictCount + 1
                    elif rt == '3':
                        dict[dictCount] = final, "3"
                        dictCount = dictCount + 1
                    else:
                        pass
                else:
                    pass
dictSorted = sorted(dict.items(), key=operator.itemgetter(1))
tubListItem1 = dictSorted[0]
tubListItem2 = dictSorted[1]
tub1 = tubListItem1[1]
tub2 = tubListItem2[1]
time1 = str(tub1[0])
time2 = str(tub2[0])
new_york = timezone('America/New_York')
ny_time = datetime.now(new_york)

#Output
print ("Times Sq-42 St -", ny_time.strftime('%H:%M:%S'))
printRoute(tub1[1],destinations[tub1[1]],time1)
printRoute(tub2[1],destinations[tub2[1]],time2)
