"""Federated learning client."""
class FLClient:
    def __init__(self, data=None):
        self.data = data
        
    def compute_update(self):
        return {"weights": None, "num_samples": 0}
