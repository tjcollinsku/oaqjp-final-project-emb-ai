"""Unit tests for emotion detection package."""

import json
import unittest
from unittest.mock import patch, Mock

from EmotionDetection import emotion_detector


def make_mock_response(emotions):
    """Build a mock requests.Response for the given emotion scores."""
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.text = json.dumps(
        {"emotionPredictions": [{"emotion": emotions}]}
    )
    return mock_resp


class TestEmotionDetector(unittest.TestCase):
    """Validate dominant emotion for known sample texts."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_for_glad_statement(self, mock_post):
        """Joy should be dominant for a glad statement."""
        mock_post.return_value = make_mock_response(
            {"anger": 0.01, "disgust": 0.01, "fear": 0.01,
             "joy": 0.95, "sadness": 0.02}
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger_for_mad_statement(self, mock_post):
        """Anger should be dominant for a mad statement."""
        mock_post.return_value = make_mock_response(
            {"anger": 0.90, "disgust": 0.03, "fear": 0.02,
             "joy": 0.02, "sadness": 0.03}
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust_for_disgusted_statement(self, mock_post):
        """Disgust should be dominant for a disgusted statement."""
        mock_post.return_value = make_mock_response(
            {"anger": 0.05, "disgust": 0.88, "fear": 0.02,
             "joy": 0.01, "sadness": 0.04}
        )
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness_for_sad_statement(self, mock_post):
        """Sadness should be dominant for a sad statement."""
        mock_post.return_value = make_mock_response(
            {"anger": 0.02, "disgust": 0.01, "fear": 0.03,
             "joy": 0.01, "sadness": 0.93}
        )
        result = emotion_detector("I am sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear_for_scared_statement(self, mock_post):
        """Fear should be dominant for a scared statement."""
        mock_post.return_value = make_mock_response(
            {"anger": 0.02, "disgust": 0.01, "fear": 0.91,
             "joy": 0.02, "sadness": 0.04}
        )
        result = emotion_detector("I am really scared about this")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
