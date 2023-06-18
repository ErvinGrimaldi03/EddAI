import json


def get_top_emotions(data, top_n=5):
    # Load the JSON string if necessary
    if isinstance(data, str):
        data = json.loads(data)

    # Parse the results and get predictions

    predictions = data[0]['results']['predictions']

    # Keep track of top emotions and scores
    top_emotions = []

    for prediction in predictions:
        models = prediction['models']
        if 'language' in models:
            lang_predictions = models['language']['grouped_predictions']

            for pred in lang_predictions:
                if 'predictions' in pred:
                    for emotion_pred in pred['predictions']:
                        if 'emotions' in emotion_pred:
                            # Get the emotions and their scores
                            emotions = emotion_pred['emotions']
                            emotions.sort(key=lambda x: x['score'], reverse=True)  # Sort by score
                            top_emotions.extend(emotions[:top_n])  # Get the top n emotions

    return top_emotions[:top_n]  # Return the top n emotions overall



