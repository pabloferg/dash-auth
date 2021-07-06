

class Channel:
    def __init__(self, name, women_pct, retention_d1_pct, cpu):
        self.name = name
        self.women_pct = women_pct
        self.retention_d1_pct = retention_d1_pct
        self.cpu = cpu

channels = [Channel('tiktok', 0.42, 0.6, 1.5),
            Channel('facebook', 0.5, 0.7, 1.6),
            Channel('google', 0.5, 0.7, 1.6)]

budget = 7800000