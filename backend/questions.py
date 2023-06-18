import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

def score_question(question):
    # Implement your scoring mechanism here
    # You can consider factors like question length, presence of certain keywords, etc.
    # Return a higher score for more meaningful questions

    # Example: Assign a higher score to longer questions
    return len(question)

def generate_questions(text, n=10):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Prepare a set of stopwords to filter out common words
    stop_words = set(stopwords.words('english'))

    questions = []

    for sentence in sentences:
        # Remove punctuation and tokenize the sentence into words
        words = nltk.word_tokenize(sentence.lower())
        words = [word for word in words if word.isalpha()]

        # Filter out stopwords
        words = [word for word in words if word not in stop_words]

        # Generate n-grams from the words
        n = min(3, len(words))  # Consider up to trigrams
        ngrams_list = list(ngrams(words, n))

        # Generate questions from the n-grams and score them
        for ngram in ngrams_list:
            question = "What is " + " ".join(ngram) + "?"
            score = score_question(question)
            questions.append((question, score))

    # Sort the questions based on score in descending order
    questions.sort(key=lambda x: x[1], reverse=True)

    # Return the top n questions
    top_questions = [q[0] for q in questions[:n]]
    return top_questions

# Example usage
file_contents = open("./data/textlecture_audio.txt", "r").read()
questions = generate_questions(file_contents, n=2)

# Print the generated questions
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question}")
