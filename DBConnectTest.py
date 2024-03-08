import sqlite3
import threading
import unittest
from unittest.mock import patch
from DBConnect import DatabaseConnection

class TestDBConnect(unittest.TestCase):

    def setUp(self):
        self.database_name = "test_db.sqlite"
    
    def tearDown(self):
        # Close any open connections after each test
        DatabaseConnection.close()
    
    def test_connection(self):
        # Test creating a connection
        connection1 = DatabaseConnection.connection(self.database_name)
        self.assertIsInstance(connection1, sqlite3.Connection)
        
        # Ensure the same connection is returned within the same thread
        connection2 = DatabaseConnection.connection(self.database_name)
        self.assertIs(connection1, connection2)
        
        # Ensure different connections are returned in different threads
        with patch.object(threading, 'get_ident', return_value=123):
            connection3 = DatabaseConnection.connection(self.database_name)
            self.assertIsNot(connection1, connection3)



    def test_close(self):
        # Test closing a connection
        DatabaseConnection.close()
        self.assertNotIn(threading.get_ident(), DatabaseConnection._instances)

if __name__ == "__main__":
    unittest.main()