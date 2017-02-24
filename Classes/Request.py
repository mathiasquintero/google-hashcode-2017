class Request(object):

    video = None
    endpoint = None
    views = None

    def __init__(self, video, endpoint, views):
        self.video = video
        self.endpoint = endpoint
        self.views = views

    def cost_with(self, latency):
        return self.views * latency