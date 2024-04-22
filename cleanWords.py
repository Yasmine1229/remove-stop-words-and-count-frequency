import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def readFile(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def countDelimiters(text):
    delimiter=set()
    for letter in text:
        if letter.isalnum()==False:
            if letter == "-":
                continue
            delimiter.add(letter)
    
    return delimiter

def toWords(text):
    delimiters = countDelimiters(text)
    delimiter_pattern = '|'.join(re.escape(d) for d in delimiters)
    words = re.split(rf'\s|{delimiter_pattern}', text)
    words = [word.lower() for word in words if word]
    return words

def removeStopwords(words):
    stop_words = set(stopwords.words('english'))
    return [word for word in words if word not in stop_words]

def countFrequencies(words):
    return Counter(words)

def cleanText(path):
    text = readFile(path)
    words = toWords(text)
    filtered_words = removeStopwords(words)
    frequencies = countFrequencies(filtered_words)
    return frequencies

frequencies = cleanText('paragraphs.txt')
print(frequencies)