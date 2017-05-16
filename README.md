# Twitter Emotion Analysis
## Introduction of Data
* dev-gold.csv is a file of standard emotion label
* dev-predicted.csv is a file of predicted emotion label
* dev.csv is a file of twitter data with emotion label
* train.csv is a file of twitter data without emotion label
## First step(_evaluation_)
* I use accuracy, precision, recall, F1-measure to evaluate the predicted result
* Change the evaluation from evaluation.py to EvaluationOOP.py with object oriented programming
## Second step(_tokenization_)
* I use regular expression to tokenize the tweet content:
  At this time, I delete date, number, @-metions, English & Chinese punctuation, HTML tags, URLs, the word 'NEWLINE' and I also delete the hashtags but leaving the words after hashtags.