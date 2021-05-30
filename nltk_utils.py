from nltk.stem.porter import PorterStemmer
import numpy as np
import nltk
# nltk.download('punkt')

stemmer = PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)

    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag


if __name__ == "__main__":
    string = "How long will the shipping take?"
    print("Before tokenizing:", string)
    string = tokenize(string)
    print("After tokenizing:", string)
    print('*'*10)
    stems = ['organize', 'organizer', 'organizing']
    print("Before stemming", stems)
    stems = [stem(word) for word in stems]
    print("After stemming", stems)
