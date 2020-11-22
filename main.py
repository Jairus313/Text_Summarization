from summariser import Summariser
import preprocessor

paragraph = str(preprocessor.text)

freq_table = Summariser.create_frequency_table(paragraph)

print(freq_table)

sentence = Summariser.sentence_tokenize(paragraph)

sentence_scores = Summariser.score_sentences(sentence, freq_table)

print(sentence_scores)

threshold = Summariser.find_average_score(sentence_scores)

print(threshold)

summary = Summariser.generate_summary(sentence, sentence_scores, 0.75 * threshold)

print(summary)