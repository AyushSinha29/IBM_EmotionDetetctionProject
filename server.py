
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    text = request.args.get('textToAnalyze', '')
    result = emotion_detector(text)

    if result.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!'

    return (f"For the given statement, the system response is {result}. "
            f"The dominant emotion is {result['dominant_emotion']}.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
