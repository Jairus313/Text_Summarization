# importing libraries
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

class Summariser():

    def create_frequency_table(text_string):
        stopWords = set(stopwords.words("english"))
        words = nltk.word_tokenize(text_string)
        ps = PorterStemmer()
        
        freqTable = dict()
        for word in words:
            word = ps.stem(word)
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

        return freqTable

    def score_sentences(text_string, freqTable):
        sentences = nltk.sent_tokenize(text_string)
        sentenceValue = dict()

        print(sentences)

        for sentence in sentences:
            word_count_in_sentence = (len(nltk.word_tokenize(sentence)))
            for wordValue in freqTable:
                if wordValue in sentence.lower():
                    if sentence[:10] in sentenceValue:
                        sentenceValue[sentence[:10]] += freqTable[wordValue]
                    else:
                        sentenceValue[sentence[:10]] = freqTable[wordValue]

            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]]

            return sentenceValue

    def find_average_score(sentenceValue):
        sumValues = 0
        for entry in sentenceValue:
            sumValues += sentenceValue[entry]

        # Average value of a sentence from original text
        average = int(sumValues / len(sentenceValue))

        return average

    def generate_summary(sentences, sentenceValue, threshold):
        sentence_count = 0
        summary = ''

        for sentence in sentences:
            if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
                summary += " " + sentence
                sentence_count += 1

        return summary