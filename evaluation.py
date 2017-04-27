from __future__ import division

def evaluation(list_gold, list_prediction):
	emotion = set(list_gold)
	listEKey = ['tp', 'fp', 'fn', 'tn', 'accuracy', 'precision', 'recall', 'F1']
	listEVal = []
	dictE = {}
	for e in emotion:
		listEVal = []
		tp = 0; fp = 0; fn = 0; tn = 0;
		for i in range(len(list_gold)):
			if list_gold[i] == list_prediction[i] and list_gold[i] == e:
				tp += 1
			elif list_prediction[i] == e and list_gold[i] != e:
				fp += 1
			elif list_gold[i] == e and list_prediction[i] != e:
				fn += 1
			else:
				tn += 1
		accuracy = (tp + tn) / (tp + tn + fp + fn) * 100
		precision = tp /(tp + fp) * 100
		recall = tp / (tp + fn) * 100
		F1 = 2 * precision * recall / (precision + recall)
		
		listEVal = listEVal + [tp, fp, fn, tn, round(accuracy,2), round(precision,2), round(recall,2), round(F1,2)]
		dictE[e] = listEVal

	#print dictE

	for k, v in dictE.iteritems():
		print k + ': ' + str(dict(zip(listEKey, v)))

fileg = open('dev-gold.csv')
filep = open('dev-predicted.csv')
lineg = fileg.readline()
linep = filep.readline()
list_gold = []
list_prediction = []
while lineg:
	list_gold.append(lineg.strip())
	list_prediction.append(linep.strip())
	lineg = fileg.readline()
	linep = filep.readline()

evaluation(list_gold, list_prediction)