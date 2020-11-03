class MovingAverage:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        return f'{self.queue}'

    def next(self, val):
        size = self.size
        queue = self.queue
        queue.append(val)

        window_sum = sum(queue[-size:])
        return window_sum / min(len(queue), size)


movingAvg = MovingAverage(3)
movingAvg.next(1)
movingAvg.next(10)
movingAvg.next(3)
movingAvg.next(5)

print(movingAvg)
