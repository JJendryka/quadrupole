from PySide6.QtGui import QRegularExpressionValidator
from enum import Enum
import time
from parameter import ParameterID

FLOAT_VALIDATOR = QRegularExpressionValidator("[+-]?[0-9]+[.,]?[0-9]*(e[+-]?[0-9]+)?")


class State(Enum):
    STOPPED = 0
    RUNNING = 1
    PAUSED = 2


class DataPacket:
    def __init__(self, timestamp: float = time.time(), step=0):
        self.timestamp = timestamp
        self.step = step
        self.data = {}

    def addData(self, param: ParameterID, value: float) -> None:
        self.data[param] = value
