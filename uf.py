import glob
import os

root_dir = "/home/domizzi/Documents/Muyal-Painal-Chimalli/metadata/metadata/"

impactfactor = 0.2
nodes = [{"id": 1,"storage":40000000000,"files":[],"utilization":0},
         {"id": 2,"storage":40000000000,"files":[],"utilization":0},
         {"id": 3,"storage":80000000000,"files":[],"utilization":0},
         {"id": 4,"storage":40000000000,"files":[],"utilization":0},
         {"id": 5,"storage":40000000000,"files":[],"utilization":0},
         {"id": 6,"storage":80000000000,"files":[],"utilization":0},
         {"id": 7,"storage":40000000000,"files":[],"utilization":0},
         {"id": 8,"storage":40000000000,"files":[],"utilization":0},
         {"id": 9,"storage":80000000000,"files":[],"utilization":0},
         {"id": 10,"storage":40000000000,"files":[],"utilization":0},
         {"id": 11,"storage":40000000000,"files":[],"utilization":0},
         {"id": 12,"storage":80000000000,"files":[],"utilization":0},
         {"id": 13,"storage":40000000000,"files":[],"utilization":0},
         {"id": 14,"storage":40000000000,"files":[],"utilization":0},
         {"id": 15,"storage":80000000000,"files":[],"utilization":0},
         ]

for filename in glob.iglob(root_dir + '**/*', recursive=True):
    #print(filename)
    file_stats = os.stat(filename)
    filesize = file_stats.st_size
    for n in nodes:
        n["uf"] = 1.0 - (n["storage"] - (n["utilization"] + filesize)) / n["storage"]

    nodes.sort(key=lambda x: x["uf"])

    nodes[0]["files"].append(filename)
    nodes[0]["utilization"] += filesize

nodes.sort(key=lambda x: x["id"])

for n in nodes:
    print(n["utilization"])


# filesize = 10
# for n in nodes:
#     n["uf"] = 1.0 - (n["storage"] - (n["utilization"] + filesize)) / n["storage"]

# nodes.sort(key=lambda x: x["uf"], reverse=True)
# print(nodes)
#replication = len(nodes) * impactfactor
