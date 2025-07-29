from flask import Flask, request, render_template
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'EmotionDetector'))


from emotion_detector import emotion_detector

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    text_to_analyze = request.form.get('text') or request.json.get('text')

    if not text_to_analyze:
        return "Error: No text provided", 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Error: Emotion detection failed", 500

 
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
