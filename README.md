# Text Summarization with FastAPI

This project implements a simple API for summarizing texts using FastAPI and NLTK (Natural Language Toolkit). The main function performs text summarization based on word frequency, returning the most representative sentences.

## How it works
The summarize function receives a text and a desired number of sentences for the summary. It follows these steps:

<p align="center">
    <img src="https://github.com/FabioAugustoRodrigues/text-summarizer-api/blob/main/images/diagram.jpg" width="1000" alt="Diagram">
</p>

## How to run the project
#### 1. Build the Docker Image
First, navigate to the root directory of the project where the docker-compose.yaml file is located.
Then, build and start the container using the following command:
```bash
docker-compose up --build
```
This will build the image and start the API application inside a container.

#### 2. Access the API
Once the container is running, the API application will be available at:
```bash
http://localhost:8400
```

## Endpoint: Summarize Text
```POST /summarize/```
#### Request Body
The request must be a JSON containing the following parameters:
- ```text``` (string): The text you want to summarize.
- ```num_sentences``` (integer, optional, default 3): The number of sentences you want in the summary.

#### Request Body Example
```json
{
  "text": "Natural language processing (NLP) is a field of computer science and artificial intelligence concerned with the interactions between computers and human language. It focuses on programming computers to fruitfully process large natural language data.",
  "num_sentences": 2
}
```
