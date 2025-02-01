import string
from collections import Counter
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import matplotlib.pyplot as plt

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

# Step 1: Read and Extract Text from HTML
with open("my_document.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "lxml")
text = soup.get_text()

# Step 2: Preprocess Text
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    return words

words = preprocess_text(text)
word_counts = Counter(words)

# Step 3: Display and Visualize Word Frequency
most_common_words = word_counts.most_common(10)
print("Most common words:", most_common_words)

# Visualization
labels, counts = zip(*most_common_words)
plt.figure(figsize=(10, 5))
plt.bar(labels, counts, color="skyblue")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Common Words in HTML Document")
plt.show()