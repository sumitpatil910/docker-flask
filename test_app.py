from app import app
import unittest

class FirstTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        response = app.test_client().get('/')
        assert response.status_code == 200

if __name__ == "__main__":
    unittest.main()
