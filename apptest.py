import unittest
import app

class TestAppFunctions(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(app.subtract(10, 3), 7)
        self.assertEqual(app.subtract(5, 5), 0)
        self.assertEqual(app.subtract(0, 7), -7)

    def test_divide(self):
        self.assertEqual(app.divide(10, 2), 5)
        self.assertAlmostEqual(app.divide(7, 3), 2.3333333333, places=7)
        with self.assertRaises(ValueError):
            app.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
