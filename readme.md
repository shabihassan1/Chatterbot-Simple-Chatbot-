
# Chatbot Demo with Flask UI

This project demonstrates a chatbot built with ChatterBot, trained on a customer support dataset (`qa_pairs_updated.csv`), and served locally with a simple web UI using Flask. The training and serving are separated to avoid retraining every time the app runs.

## Overview
- **Training**: The chatbot is trained on a dataset of question-answer pairs from customer support tickets, supplemented with casual conversation pairs and the ChatterBot English corpus.
- **UI**: A Flask-based web interface allows users to interact with the pre-trained chatbot.
- **Persistence**: The trained model state is saved to `db.sqlite3`, enabling fast startup of the Flask app.

## Prerequisites
- Python 3.6 or higher
- Internet connection for initial setup and library downloads

## Setup
1. **Clone or Download the Repository**:
   - Download the project files or clone this repository to your local machine.

2. **Install Dependencies**:
   - Run the following command to install required Python packages:
     ```bash
     pip install pandas chatterbot chatterbot_corpus pyyaml
     ```
   - Install the SpaCy English model for potential future enhancements (e.g., if you add natural language processing):
     ```bash
     python -m spacy download en_core_web_sm
     ```

3. **Prepare the Dataset**:
   - Ensure `qa_pairs_updated.csv` is in the project directory. This file should contain the question-answer pairs for training (e.g., generated from `dataset-tickets-multi-lang-4-20k.csv` with added casual conversation pairs).

## Usage

### Step 1: Train the Chatbot
- Run the training script to create and save the trained model state:
  ```bash
  python train_chatbot.py
  ```
  - This will train the chatbot and generate `db.sqlite3`, which stores the trained state. This step only needs to be run once or when updating the dataset.

### Step 2: Run the Flask App
- Start the Flask web server to access the chatbot UI:
  ```bash
  python app.py
  ```
- Open your browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

### Step 3: Interact
- Type messages in the chat interface (e.g., "Hi," "How can I secure medical data?").
- The chatbot will respond based on its training, with a fallback message for unrecognized inputs.

## Files
- `train_chatbot.py`: Trains the chatbot and saves the model state to `db.sqlite3`.
- `app.py`: Runs the Flask app, loading the pre-trained model and serving the UI.
- `templates/index.html`: HTML template for the chat interface with CSS styling and JavaScript for interactivity.
- `qa_pairs_updated.csv`: Dataset with question-answer pairs (including casual conversation pairs).
- `db.sqlite3`: SQLite database file storing the trained chatbot state (generated after running `train_chatbot.py`).


## Notes
- **Training Time**: Training with 2000 rows is fast locally. Retrain with `train_chatbot.py` if you update `qa_pairs_updated.csv`.
- **Dependencies**: Ensure all packages are installed. If issues arise, verify compatibility with your Python version.
- **Testing**: Test the UI locally after training to ensure responses are as expected.
- **Enhancements**: The SpaCy model (`en_core_web_sm`) is included for potential future NLP improvements, though it’s not currently used.

## Troubleshooting
- If the Flask app fails to load, check that `db.sqlite3` exists and was created successfully by `train_chatbot.py`.
- Ensure the `templates` folder and `index.html` are in the correct directory relative to `app.py`.

Happy chatting!


---
