from typing import Dict
from threading import Lock


class SingletonMeta(type):
    """
    There are different ways to implement a singleton, this makes use of metaclass
    """

    _instance: Dict = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)

        return cls._instance[cls]
