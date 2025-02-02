import string
import re
from collections import Counter
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import networkx as nx

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Step 1: Read the Text File
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Step 2: Preprocess the Text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    words = word_tokenize(text)  # Tokenize text
    stop_words = set(stopwords.words("english"))
    custom_stopwords = {'chatgpt', 'user', '’'}  # Custom stopwords
    words = [word for word in words if word not in stop_words and word not in custom_stopwords]
    return words

# Step 3: Count Word Frequency
def count_word_frequency(words):
    return Counter(words)

# Step 4: Word Cloud
def generate_wordcloud(word_counts):
    wordcloud = WordCloud(width=800, height=400, background_color="black",
                          colormap="cool", max_words=100).generate_from_frequencies(word_counts)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")  # Hide axis
    plt.title("Word Cloud of Most Common Words")
    plt.show()

# Main Execution
if __name__ == "__main__":
    file_path = "my_document.txt"  # Change this to your file path
    text = read_text_file(file_path)
    words = preprocess_text(text)
    word_counts = count_word_frequency(words)

    # Get the 10 most common words
    most_common_words = word_counts.most_common(10)
    print("Most common words:", most_common_words)
