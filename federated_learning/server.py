"""Federated learning server."""
class FLServer:
    def __init__(self, rounds=10, strategy="fedavg"):
        self.rounds = rounds
        self.strategy = strategy
        
    def train(self, clients):
        for r in range(self.rounds):
            updates = [c.compute_update() for c in clients]
            self._aggregate(updates)
            
    def _aggregate(self, updates):
        pass
