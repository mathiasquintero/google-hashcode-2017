import Classes.Endpoint as Endpoint
import Classes.Video as Video
import Classes.Cache as Cache
import Classes.Request as Request
import Classes.Problem as Problem

def parse(text):
    videos = []
    requests = []
    caches = []
    endpoints = []

    lines = text.split("\n")

    first = lines[0].split(" ")
    nv = int(first[0])
    ne = int(first[1])
    nr = int(first[2])
    nc = int(first[3])
    capacity = int(first[4])

    caches = [Cache.Cache(i, capacity) for i in range(nc)]

    second = lines[1].split(" ")
    videos = [Video.Video(i, int(second[i])) for i in range(len(second))]

    index = 2
    for i in range(ne):
        line = lines[index].split(" ")
        latency = int(line[0])
        k = int(line[1])
        caches_for_e = []
        for j in range(k):
            line = lines[index + 1 + j].split(" ")
            caches_for_e.append([int(a) for a in line])
        endpoints.append(Endpoint.Endpoint(i, latency, caches_for_e))
        index = index + k + 1

    request_lines = [lines[i].split(" ") for i in range(index, index + nr)]
    requests = [Request.Request(int(line[0]), int(line[1]), int(line[2])) for line in request_lines]

    return Problem.Problem(caches, videos, endpoints, requests)
