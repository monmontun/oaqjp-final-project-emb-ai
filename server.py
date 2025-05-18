''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on localhost:5000.
'''
# Import the required libraries and function
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the html interface\
        and runs emotion detection using emotion_detector.
        It returns the formatted string with emotions with scores\
        and dominant emotion.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract dominant emotion from the response
    dominant_emotion = response['dominant emotion']

    #Check if dorminant_emotion is None, indicating blank entry
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract the emotions with their confidence scores
    emotions = ', '.join(f"'{key}': {value}" for key, value in response.items()\
        if key != 'dominant emotion')

    # Return a formatted response with emotions with corresponding scores and dominant emotion
    return f"For the given statement, the system response is {emotions}.\
    The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function renders the main web application page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
