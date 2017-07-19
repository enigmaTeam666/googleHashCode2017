line = list(map(int,input().split()))
videosN = line[0]
endPointN = line[1]
requestN = line[2]
cachN = line[3]
cachVol = line[4]
videosVol = list(map(int,input().split()))
endPoints = []
for _ in range(endPointN) :
    endPoint = list(map(int,input().split()))
    tmp = {"latency":endPoint[0],"cachesN":endPoint[1],"cachLatencys":[]}
    for i in range(endPoint[1]):
        tmp2 = list(map(int,input().split()))
        tmp["cachLatencys"].append((tmp2[0],tmp2[1]))
    tmp["cachLatencys"]  = sorted(tmp["cachLatencys"], key=lambda x: x[1])
    tmp["requests"] = []
    endPoints.append(tmp)
for i in range(requestN):
    tmp = list(map(int,input().split()))
    
    endPoints[int(tmp[1])]["requests"].append({"endPointId":tmp[1],"videoId":tmp[0],"requestN":tmp[2]})
queue = []
index = 0 


for endpoint in endPoints:
	latency = endpoint["latency"]
	for req in endpoint["requests"]:
		queue.append([index,req["videoId"],req["requestN"]*latency])
	index += 1
		
#tri_queue

quesorted = sorted(queue,key=lambda x:x[2] , reverse=True)
result = {}

for ele in quesorted:
	if videosVol[ele[1]] <= cachVol :
		for cache in endPoints[ele[0]]["cachLatencys"] :
			idCache = cache[0]

			if idCache in result.keys():
				if result[idCache]["size"] >= videosVol[ele[1]]:
					if ele[1] not in result [idCache]["videos"]:
						result[idCache]["size"]-= videosVol[ele[1]]
						result [idCache]["videos"].append(ele[1])
						break 
			else:
				result[idCache]={"videos":[] , "size":cachVol}
				if result[idCache]["size"] >= videosVol[ele[1]]:
					result[idCache]["size"]-= videosVol[ele[1]]
					result [idCache]["videos"].append(ele[1])
					break 
					
print(len(result.keys()))

# print results
for elm in result:
	line = str(elm) 
	
	for i in result[elm]["videos"]:
		line+= " " + str(i)
	print(line)
