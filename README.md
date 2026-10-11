
# SmartLearn AI - Adaptive Learning Assistant

## Project Overview

SmartLearn AI is a Python application demonstrating
AI-based adaptive human-computer interaction.

It uses a Decision Tree Classifier to recommend question
difficulty based on recent user performance.

## Features

- 30 questions across three difficulty levels
- 10 questions per quiz session
- One question displayed at a time
- AI-based difficulty recommendations
- Correct and incorrect answer feedback
- Score and accuracy tracking
- No repeated questions within a session
- Restart quiz functionality

## Technologies

- Python 3.11
- Gradio
- scikit-learn
- Jupyter Notebook

## Installation

Create a Python virtual environment.

Install dependencies:

    python -m pip install -r requirements.txt

## Run Application

    python app.py

Open the local URL displayed in Terminal.

## Run Automated Tests

    python -m unittest test_app.py -v

## AI Model

The application uses a Decision Tree Classifier trained
on synthetic examples of student performance.

It considers recent answers and current question
difficulty to predict the recommended next difficulty.

The model is an educational prototype, not a validated
assessment of real student learning.

## AI Assistance Disclosure

ChatGPT from OpenAI assisted with code development,
explanations, project structure, and documentation.
All final implementation and testing results should
be reviewed and verified before academic submission.
