import requests
import json

def emotion_detection(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header  = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url=url, headers = header, json = obj)
    formatted_output = json.loads(response.text)
    
    emotion_predictions = formatted_output['emotionPredictions'][0]['emotion']
    dominant_emotion = [key for key, value in emotion_predictions.items() if value == max(emotion_predictions.values())]
    emotion_predictions['dominant_emotion'] = dominant_emotion[0]

    return emotion_predictions