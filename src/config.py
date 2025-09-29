from dataclasses import dataclass

@dataclass
class Config:
    seed: int = 42
    context_size: int = 1024
    val_size: float = 0.2
