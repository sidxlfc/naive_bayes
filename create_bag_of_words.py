import json

with open('F:\\Machine Learning\\project1\\data.json', 'r') as f :

	try :
		d = json.load(f)
	
	except ValueError :
		d = {}

	unique_words = {}

	for category, list in d.iteritems() :

		for word in list[0] :

			if word not in unique_words :
				
				unique_words[word] = 1
				continue

			unique_words[word] += 1

with open('F:\\Machine Learning\\project1\\unique_words.json', 'w') as f:

		json.dump(unique_words, f, indent=4)