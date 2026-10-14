"""Flask server for the final project: emotion detection application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def index():
    """Render the application's index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_dect():
    """Analyze input text and return the detected emotion scores."""
    text_to_analyze = request.args.get('textToAnalyze')
    raw_output = emotion_detector(text_to_analyze)
    if raw_output["dominant_emotion"] is None:
        return "<b> Invalid text! Please try again! </b>"
    output = f"For the given statement, the system response is \
        'anger': {raw_output['anger']}, 'disgust': {raw_output['disgust']}, \
        'fear': {raw_output['fear']}, 'joy': {raw_output['joy']} and \
        'sadness': {raw_output['sadness']}. \
        The dominant emotion is  {raw_output['dominant_emotion']}"
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
