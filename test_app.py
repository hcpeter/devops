import unittest
from app import app

class FlaskMathAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_addition(self):
        response = self.app.post('/', data=dict(number1='5', number2='3', operation='add'))
        self.assertIn(b'Result: 8.0', response.data)

    def test_subtraction(self):
        response = self.app.post('/', data=dict(number1='10', number2='4', operation='subtract'))
        self.assertIn(b'Result: 6.0', response.data)

    def test_multiplication(self):
        response = self.app.post('/', data=dict(number1='6', number2='7', operation='multiply'))
        self.assertIn(b'Result: 42.0', response.data)

    def test_invalid_input(self):
        response = self.app.post('/', data=dict(number1='a', number2='7', operation='multiply'))
        self.assertIn(b'Please enter valid numbers.', response.data)

if __name__ == '__main__':
    unittest.main()
