FROM rasa/rasa_core_sdk:latest

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_md
RUN python -m nltk.downloader vader_lexicon