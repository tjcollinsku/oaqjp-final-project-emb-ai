"""Unit tests for emotion detection package."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Validate dominant emotion for known sample texts."""

    def test_joy_for_glad_statement(self):
        """Joy should be dominant for a glad statement."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_for_mad_statement(self):
        """Anger should be dominant for a mad statement."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_for_disgusted_statement(self):
        """Disgust should be dominant for a disgusted statement."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_for_sad_statement(self):
        """Sadness should be dominant for a sad statement."""
        result = emotion_detector("I am sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_for_scared_statement(self):
        """Fear should be dominant for a scared statement."""
        result = emotion_detector("I am really scared about this")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == "__main__":
    unittest.main()
