# oaqjp-final-project-emb-ai
This repo is for the final project which is based on Embedded AI libraries.

## Emotion Detection Application (Watson NLP + Flask)

This project uses the Watson embeddable NLP Emotion API and deploys the app using Flask.

### Project Structure

```
practice_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
└── test_emotion_detection.py
```

### Setup (Windows)

1. Create and activate virtual environment (if needed):

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install required packages:

```powershell
.venv\Scripts\python.exe -m pip install requests flask pylint
```

### Run the Web App

```powershell
.venv\Scripts\python.exe server.py
```

Open `http://127.0.0.1:5000` in your browser.

### Run Unit Tests

```powershell
.venv\Scripts\python.exe -m unittest test_emotion_detection.py -v
```

### Run Static Analysis

```powershell
.venv\Scripts\python.exe -m pylint server.py EmotionDetection/emotion_detection.py
```

### Notes

- For valid input, the app returns emotion scores and the dominant emotion.
- For blank or invalid input (status 400), the app returns: `Invalid text! Please try again.`

### Task Mapping (IBM Final Project)

1. Task 1: Clone and setup repository
2. Task 2: Create emotion detection app using Watson NLP Emotion API
3. Task 3: Format output — returns anger, disgust, fear, joy, sadness, and dominant_emotion
4. Task 4: Packaged as `EmotionDetection` with `__init__.py` export
5. Task 5: Unit tests in `test_emotion_detection.py` covering joy, anger, disgust, sadness, fear
6. Task 6: Flask deployment via `server.py` with `/` and `/emotionDetector` routes
7. Task 7: Error handling — status 400 returns all None values; Flask returns error message
8. Task 8: Static code analysis with pylint achieving a perfect score
