import sqlite3
import threading

class DatabaseConnection:
    _lock = threading.Lock()
    _instances = {}

    def __init__(self, database_name):
        raise RuntimeError("Cannot instantiate DatabaseConnection directly. Use connection() method instead.")
    
    
    @classmethod
    def connection(cls, database_name):
        thread_id = threading.get_ident()
        with cls._lock:
            if thread_id not in cls._instances:
                cls._instances[thread_id] = sqlite3.connect(database_name)
                print("Connection established in thread:", threading.current_thread().name, "Thread ID:", thread_id)
        return cls._instances[thread_id]
    
    @classmethod
    def close(cls):
        thread_id = threading.get_ident()
        if thread_id in cls._instances:
            cls._instances[thread_id].close()
            del cls._instances[thread_id]
            print("Connection closed in thread:", threading.current_thread().name, "Thread ID:", thread_id)

