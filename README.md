# Federated Learning SDK 🔐

Privacy-preserving distributed training with federated averaging, secure aggregation, and differential privacy.

## Features

- **FedAvg/FedProx**: Multiple aggregation strategies
- **Differential Privacy**: ε-differential privacy guarantee
- **Secure Aggregation**: Encrypted model updates
- **Heterogeneous Data**: Non-IID handling

## Privacy Budget

| ε | δ | Accuracy | Utility Loss |
|---|---|----------|-------------|
| 1.0 | 1e-5 | 91.2% | -3.1% |
| 3.0 | 1e-5 | 93.8% | -0.5% |
| 8.0 | 1e-5 | 94.5% | +0.2% |

## Quick Start

```python
from federated_learning import FLServer, FLClient

server = FLServer(rounds=10, strategy="fedavg")
clients = [FLClient(data=local_data) for local_data in datasets]
server.train(clients)
```

## License

Apache 2.0