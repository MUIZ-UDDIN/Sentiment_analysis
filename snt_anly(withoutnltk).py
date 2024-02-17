import string
from collections import Counter
import matplotlib.pyplot as plt

text = open("D:/Data_Scientist/MachineLearningProjects/sentimantalAnalysic(NLP)/Data/read.txt", encoding="utf-8").read()
lower_case = text.lower()
clean_text = lower_case.translate(str.maketrans("", "", string.punctuation))

tokenized_words = clean_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
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

fig, axis1 = plt.subplots()
axis1.bar(emotions_counter.keys(), emotions_counter.values())
fig.autofmt_xdate()
plt.show()