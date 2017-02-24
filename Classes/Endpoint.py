class Endpoint(object):

    id = None
    centerLatency = None
    caches = None

    def __init__(self, id, centerLatency, caches):
        self.id = id
        self.centerLatency = centerLatency
        self.caches = caches

    def cost_in(self, problem):
        requests = problem.requests_for(self)
        costs = [r.cost_with(self.centerLatency) for r in requests]
        result = 0
        for i in costs:
            result += i
        return result

    def caches_in(self, problem):
        return [[problem.cache_with(id[0]), id[1]]  for id in self.caches]

    def solve(self, problem):
        caches = sorted(self.caches_in(problem), key=lambda c: c[1])
        requests = problem.requests_for(self)
        for cache in caches:
            requests = cache[0].solve(requests, problem)