from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import heapq

def summarize(text: str, num_sentences: int = 3):
    sentences = sent_tokenize(text)

    words = word_tokenize(text.lower())
    word_freq = Counter(words)

    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_freq[word]
                else:
                    sentence_scores[sent] += word_freq[word]

    best_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return " ".join(best_sentences)
