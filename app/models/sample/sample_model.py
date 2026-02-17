from app.models.sample.sample_domain import SampleDomain


class SampleModel:
    def __init__(self, sample: SampleDomain):
        self.location = {
            "type": "Point",
            "coordinates": [sample.longitude, sample.latitude]
        }
        self.signal_strength = sample.signal_strength
        self.timestamp = sample.timestamp

    def to_dict(self):
        return {
            "location": self.location,
            "signal_strength": self.signal_strength,
            "timestamp": self.timestamp
        }
