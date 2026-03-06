"""Unit tests for emotion detection package."""

import unittest
from unittest.mock import patch, Mock
import json

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Validate dominant emotion for known sample texts."""

    def setUp(self):
        """Set up mock API responses for each test."""
        self.patcher = patch("EmotionDetection.emotion_detection.requests.post")
        self.mock_post = self.patcher.start()

    def tearDown(self):
        """Stop the patcher after each test."""
        self.patcher.stop()

    def test_joy_for_glad_statement(self):
        """Joy should be dominant for a glad statement."""
        self.mock_post.return_value = Mock(
            status_code=200,
            text=json.dumps({"emotionPredictions": [{"emotion": {
                "anger": 0.01, "disgust": 0.01, "fear": 0.01,
                "joy": 0.95, "sadness": 0.02
            }}]})
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger_for_mad_statement(self):
        """Anger should be dominant for a mad statement."""
        self.mock_post.return_value = Mock(
            status_code=200,
            text=json.dumps({"emotionPredictions": [{"emotion": {
                "anger": 0.90, "disgust": 0.03, "fear": 0.02,
                "joy": 0.02, "sadness": 0.03
            }}]})
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust_for_disgusted_statement(self):
        """Disgust should be dominant for a disgusted statement."""
        self.mock_post.return_value = Mock(
            status_code=200,
            text=json.dumps({"emotionPredictions": [{"emotion": {
                "anger": 0.05, "disgust": 0.88, "fear": 0.02,
                "joy": 0.01, "sadness": 0.04
            }}]})
        )
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness_for_sad_statement(self):
        """Sadness should be dominant for a sad statement."""
        self.mock_post.return_value = Mock(
            status_code=200,
            text=json.dumps({"emotionPredictions": [{"emotion": {
                "anger": 0.02, "disgust": 0.01, "fear": 0.03,
                "joy": 0.01, "sadness": 0.93
            }}]})
        )
        result = emotion_detector("I am sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear_for_scared_statement(self):
        """Fear should be dominant for a scared statement."""
        self.mock_post.return_value = Mock(
            status_code=200,
            text=json.dumps({"emotionPredictions": [{"emotion": {
                "anger": 0.02, "disgust": 0.01, "fear": 0.91,
                "joy": 0.02, "sadness": 0.04
            }}]})
        )
        result = emotion_detector("I am really scared about this")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
