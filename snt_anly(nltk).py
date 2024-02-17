import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open("D:/Data_Scientist/MachineLearningProjects/sentimantalAnalysic(NLP)/Data/read.txt", encoding="utf-8").read()
lower_case = text.lower()
clean_text = lower_case.translate(str.maketrans("", "", string.punctuation))

tokenized_words = word_tokenize(clean_text,"english")

final_words = []
for word in tokenized_words:
    if word not in set(stopwords.words("english")):
        final_words.append(word)
 
emotion_list = []
with open("D:/Data_Scientist/MachineLearningProjects/sentimantalAnalysic(NLP)/Data/emotion.txt", "r") as file:
    for line in file:
        clean_lines = line.replace("\n","").replace(",","").replace("'","").strip()
        words, emotion = clean_lines.split(":")

        if words in final_words:
            emotion_list.append(emotion)
emotions_counter = Counter(emotion_list)
print(emotions_counter)

def sentimantal_Analysic(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    pos = score["pos"]
    neg = score["neg"]
    if pos > neg:
        print("positive sentiment")
    elif pos < neg:
        print("negitive sentiment")
    else:
        print("neutral sentiment")

sentimantal_Analysic(clean_text)

fig, axis1 = plt.subplots()
axis1.bar(emotions_counter.keys(), emotions_counter.values())
fig.autofmt_xdate()
plt.show()