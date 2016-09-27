import json

def calculate_probabilities(unique_words, data) :

	unique_words_length = len(unique_words)

	with open('F:\\Machine Learning\\project1\\probabilities.json', 'r') as f :

		try :
			probabilities = json.load(f)
		
		except ValueError :
			probabilities = {}

	#probabilities = data

	
	count = 0

	for category in data :

		probabilities[category] = [{}, 0]

		for unique_word in unique_words :

			try :
				
				probabilities[category][0][unique_word] = float(float(data[category][0][unique_word] + 1)/float(data[category][1]+unique_words_length))

			except KeyError :

				count += 1
				probabilities[category][0][unique_word] = float(float(1)/float(data[category][1]+unique_words_length))
			
			probabilities[category][0][unique_word]
			'''print category + " : " + word
			
			print data[category][0][word] + 1
			
			print data[category][1]
			
			print unique_words_length

			print float(float(data[category][0][word] + 1)/float(data[category][1]+unique_words_length))
			print "----------------------------------------------------------"'''
		
		probabilities[category][1] = len(probabilities[category][0])
		
		'''print unique_words_length

		print count

		print unique_words_length-count

		print len(data[category][0])'''
		
		#break


	with open('F:\\Machine Learning\\project1\\probabilities.json', 'w') as f:

		json.dump(probabilities, f, indent=4)


unique_words = None
data = None
with open('F:\\Machine Learning\\project1\\unique_words.json', 'r') as f :

	try :
		unique_words = json.load(f)
	
	except ValueError :
		unique_words = {}

	with open('F:\\Machine Learning\\project1\\data.json', 'r') as f2 :

		try :
			data = json.load(f2)
		
		except ValueError :
			data = {}


calculate_probabilities(unique_words, data)