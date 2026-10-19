import json
import unittest

from emotion_detection import emotion_detector


def top_emotion(text):
    """Return the emotion with the highest score for the given text."""
    result = json.loads(emotion_detector(text))
    scores = result["emotionPredictions"][0]["emotion"]
    return max(scores, key=scores.get)


class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        self.assertEqual(top_emotion("I am glad this happened"), "joy")

    def test_anger(self):
        self.assertEqual(top_emotion("I am really mad about this"), "anger")

    def test_disgust(self):
        self.assertEqual(top_emotion("I feel disgusted just hearing about this"), "disgust")

    def test_sadness(self):
        self.assertEqual(top_emotion("I am so sad about this"), "sadness")

    def test_fear(self):
        self.assertEqual(top_emotion("I am really afraid that this will happen"), "fear")


if __name__ == "__main__":
    unittest.main()