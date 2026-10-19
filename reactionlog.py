class ReactionLog:
    def __init__(self, player):
        self.player = player
        self.times = []

    def add(self, time_ms):
        """Add a reaction time to the log."""
        self.times.append(time_ms)

    def count(self):
        """Return the number of recorded rounds."""
        return len(self.times)

    def best(self):
        """Return the fastest reaction time, or 0 if empty."""
        if not self.times:
            return 0
        return min(self.times)

    def average(self):
        """Return the average reaction time, or 0 if empty."""
        if not self.times:
            return 0
        return sum(self.times) / len(self.times)

    def summary(self):
        """Return a formatted summary string."""
        if not self.times:
            return f"{self.player}: no valid rounds"
        return (f"{self.player}: {self.count()} rounds, "
                f"best {self.best():.0f} ms, average {self.average():.0f} ms")
