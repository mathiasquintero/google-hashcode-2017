import knapsack

class Cache(object):

    id = None
    capacity = None
    videos = None

    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.videos = []

    def describe(self):
        videos = " ".join([str(video) for video in self.videos])
        return str(self.id) + " " + videos

    def capacity_left(self, problem):
        capacity = self.capacity
        for id in self.videos:
            capacity = capacity - problem.video_with(id).size
        return capacity

    def cost_for(self, video):
        if video.id in self.videos:
            return 0
        return video.size

    def solve(self, requests, problem):

        items = [[self.cost_for(problem.video_with(r.video)), r.views, r.video] for r in requests]

        # sizes = [self.cost_for(problem.video_with(r.video)) for r in requests]
        # utility = [r.views for r in requests]

        solution = knapsack.pack5(items, self.capacity_left(problem))

        for video in solution:
            if video not in self.videos:
                self.videos.append(video)

        return [r for r in requests if r.video not in self.videos]
