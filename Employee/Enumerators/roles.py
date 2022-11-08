from enum import Enum
from enum import auto

class Roles(Enum):
    """Add every role that a worker can have. Program automatically adjust to more and less roles."""
    MANAGER = auto()
    CASHIER = auto()
    WORKER = auto()
    INTERN = auto()