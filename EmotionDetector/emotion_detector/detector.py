import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raises an error for bad status codes
        return format_json(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def format_json(response):
    
    anger_score = response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = response["emotionPredictions"][0]["emotion"]["sadness"]
    all_responses = response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(all_responses,key=all_responses.get)
    
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }