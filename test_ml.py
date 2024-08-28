# test_iris_ml.py
import unittest
from ML-linerregression import model  # Assuming model is accessible

class TestIrisModel(unittest.TestCase):
    def test_model_accuracy(self):
        self.assertGreater(model.score(X_test, y_test), 0.8)  # Example threshold

if __name__ == '__main__':
    unittest.main()
