# Import unittest library and emotion detector module to be tested
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        
        # Test case for dominant emotion 'joy'
        self.assertEqual(emotion_detector("I am glad this happened.")['dominant emotion'], 'joy')

        # Test case for dominant emotion 'anger'
        self.assertEqual(emotion_detector("I am really mad about this.")['dominant emotion'], 'anger')

        # Test case for dominant emotion 'disgust'
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this.")['dominant emotion'], 'disgust')

        # Test case for dominant emotion 'sadness'
        self.assertEqual(emotion_detector("I am so sad about this.")['dominant emotion'], 'sadness')

        # Test case for dominant emotion 'fear'
        self.assertEqual(emotion_detector("I am really afraid that this will happen.")['dominant emotion'], 'fear')
        
unittest.main()
    