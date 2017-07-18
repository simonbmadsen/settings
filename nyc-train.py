from google.transit import gtfs_realtime_pb2
import requests
import math
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read("nyc.ini")
apikey = config["api"]["key"]
feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(apikey)
responseString = response.content
feed.ParseFromString(responseString)
print ("Times Square - 42th Street")
for entity in feed.entity:
     if entity.HasField('trip_update'):
#        print (entity.trip_update) 
        tu = entity.trip_update
        tr = tu.trip
        rt = tr.route_id
        sc = len(tu.stop_time_update)
        count = 0
        if rt == '1' or rt == '2' or rt == '3':
            #print (rt)
            #print (tr)
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
                count = count + 1
                if sid == '301S':
                    #    print ("Harlem")
                    pass
                elif sid == '302S':
                    #    print ("145 St")
                    pass
                elif sid == '224S':
                    #    print ("135 St")
                    pass
                elif sid == '225S':
                    #    print ("125 St")
                    pass
                elif sid == '226S':
                    #    print ("116 St")
                    pass
                elif sid == '227S':
                    #    print ("Central Park North - 110 St")
                    pass
                elif sid == '120S':
                    #    print ("96 St")
                    pass
                elif sid == '123S':
                    #    print ("72 St")
                    pass
                elif sid == '127S':
                    pass
                elif sid == '128S':
                    #    print ("34 St")
                    pass
                elif sid == '132S':
                    #    print ("14 St")
                    pass
                elif sid == '301N':
                    #    print ("145 St")
                    pass
                elif sid == '302N':
                    #    print ("145 St")
                    pass
                elif sid == '224N':
                    #   print ("135 St")
                    pass
                elif sid == '225N':
                    #    print ("125 St")
                    pass
                elif sid == '226N':
                    #    print ("116 St")
                    pass
                elif sid == '227N':
                    #    print ("Central Park North - 110 St")
                    pass
                elif sid == '120N':
                    #    print ("96 St")
                    pass
                elif sid == '123N':
                    #    print ("72 St")
                    pass
                elif sid == '127N':
                    #print ("Times Sq - 42 St")
                    if rt == '1':
                       print ("1 Van Cort Park 242 St    ", final, "min", sep='')
                    elif rt == '2':
                       print ("2 Wakefield-241 St        ", final, "min", sep='')
                    else:
                       print ("3 Harlem-148 St           ", final, "min", sep='')
                    #print ("Arrival  :", at)
                    #print ("Departure:", dt)
                elif sid == '128N':
                    #    print ("34 St")
                    pass
                elif sid == '132N':
                    #    print ("14 St")
                    pass
                else:
                    #print(sid)
                    pass
