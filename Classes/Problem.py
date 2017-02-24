class Problem(object):

    videos = None
    endpoints = None
    requests = None
    caches = None

    def __init__(self, caches, videos, endpoints, requests):
        self.caches = caches
        self.videos = videos
        self.endpoints = endpoints
        self.requests = requests

    def describe(self):
        caches = [cache.describe() for cache in self.caches if len(cache.videos) > 0]
        return str(len(caches)) + "\n" + "\n".join(caches)

    def video_with(self, id):
        return self.videos[id]

    def cache_with(self, id):
        return self.caches[id]

    def requests_for(self, endpoint):
        return [r for r in self.requests if r.endpoint == endpoint.id]

    def solve(self):
        endpoints = sorted(self.endpoints, key=lambda e: e.cost_in(self), reverse=True)
        for endpoint in endpoints:
            endpoint.solve(self)