
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_import(self):
        self.assertTrue(callable(emotion_detector))

if __name__ == '__main__':
    unittest.main()
