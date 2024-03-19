import unittest
import os
from robonnx.roberta_onnx import OnnxSession

class RobertaTestMeta(unittest.TestCase):
    def assertIsFalse(self, path):
        if not os.path.isfile(path):
            raise AssertionError(f"{path} is not a file or does not exist!")

class RobertaTest(RobertaTestMeta):
    def setUp(self):
        self.onnx_session = OnnxSession('model.onnx', 'emotion')

    def test_labels(self):
        self.assertEqual(self.onnx_session.labels, ['anger', 'joy', 'optimism', 'sadness'])

    def test_model(self):
        self.assertIsFile(self.onnx_session.model)