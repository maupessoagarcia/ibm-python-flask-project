from emotion_detector import emotion_detector

def test_emotion_detector1():
    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == "joy"

def test_emotion_detector2():
    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == "anger"

def test_emotion_detector3():
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == "disgust"

def test_emotion_detector4():
    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == "sadness"

def test_emotion_detector5():
    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == "fear"
