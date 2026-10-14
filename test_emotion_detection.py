from EmotionDetection.emotion_detection import emotion_detector
import unittest

class EmotionDection(unittest.TestCase):
    def test_emotion_detection(self):
        res_1 = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(res_1, "joy")
        res_2 = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(res_2, "anger")
        res_3 = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(res_3, "disgust")
        res_4 = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(res_4, "sadness")
        res_5 = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(res_5, "fear")

unittest.main()