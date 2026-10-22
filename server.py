from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detection Tool")

@app.route("/emotionDetector")
def emotion_analyzer():
    # Retrieving the text from the form
    text_to_analyze = request.args.get("textToAnalyze")
    # Passing retrieved text to emotion detector
    response = emotion_detection(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "<b>Invalid text!, Please try again!<b>"
    else:
        return f"""For the given statement, the system response is 'anger':{response['anger']}, 'disgust': {response['disgust']}, 'fear':{response['fear']}, 'joy':{response['joy']},
        'sadness':{response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}<b>"""

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)