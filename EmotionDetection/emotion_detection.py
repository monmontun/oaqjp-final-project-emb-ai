# Import the json and requests library to handle the http request and json
import json
import requests

# Define a function named emotion detector that takes a string input (text_to_analyze)
def emotion_detector(text_to_analyze):

    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create a dictionary with the text to be analyzed
    inputjson = { "raw_document": { "text": text_to_analyze } }

    # Send a Post request to the API with the text and headers
    response = requests.post(url, json=inputjson, headers=headers)

    # Convert the response text into a dictionary using the json library function
    formatted_response = json.loads(response.text)
    
    emotion_result = {}
    # If the reponse status code is 200, extract the required information.
    if response.status_code == 200:
        # Extract the required dictionary of emotions (anger, disgust, fear, joy and sadness), along with their scores
        emotion_result = formatted_response['emotionPredictions'][0]['emotion']

        # Find the dominant emotion with the highest score
        dominant_emotion = max(emotion_result, key=emotion_result.get)

        # Append the dominant emotion to the dictionary
        emotion_result['dominant emotion'] = dominant_emotion
    
    # if the response status code is 400, which means blank input, set all the values to None.
    elif response.status_code == 400:
        emotion_result['anger'] = None
        emotion_result['disgust'] = None
        emotion_result['fear'] = None
        emotion_result['joy'] = None
        emotion_result['sadness'] = None
        emotion_result['dominant emotion'] = None

    # Return emotion detector results in a dictionary format
    return emotion_result