import json
import re
import string
import operator
import math

def naiive_bayes(file) :

	lines_from_file = file.readlines()

	d = {}

	for category in probabilities :
		
		P = 0

		for line in lines_from_file :

			line = line.strip()
			line = line.lower()

			'''pattern = re.compile(r'\:')
																					
												if pattern.findall(line):
									
													if len(line.split(":")[0])>0 :
														continue'''
			
			specials = '~`!@#$%^&*()_-+={}|[]\\:;"\'<>,.?/+\t'
			
			trans = string.maketrans(specials, ' '*len(specials))

			line = line.translate(trans)
			line = line.strip()
			words = line.split(' ')

			for each_word in words :

				each_word = str(unicode(each_word, errors='ignore'))
				
				each_word = each_word.strip()

				if each_word in probabilities[category][0]:

					#P = float((P)*float(probabilities[category][0][each_word]))
					P += float(math.log(probabilities[category][0][each_word]))
					#print float(probabilities[category][0][each_word])

		d[category] = P

	#print d
	#print category + str(max(d.iteritems(), key=operator.itemgetter(1))[0])

	return max(d.iteritems(), key=operator.itemgetter(1))[0]
	#print d


probabilities = None
with open('F:\\Machine Learning\\project1\\probabilities.json', 'r') as f :

	try :
		probabilities = json.load(f)
	
	except ValueError :
		probabilities = {}


#---------------------------TRAINING-----------------driver code------------------------#

from os import walk


'''
folder = "F:\\Machine Learning\\project1\\training\\alt.atheism"

count = 0

for (x, y, filenames) in walk(folder):
		
	for tempfile in filenames :
		
		if naiive_bayes(open(folder + "\\" + tempfile)) == "alt.atheism" :

			count += 1

print str((float(count)/float(500))*100) + "% accuracy"

print "-------------------------------------------------------------------------"

#---------------------------TESTING-----------------driver code------------------------#

folder = "F:\\Machine Learning\\project1\\testing\\alt.atheism"

count = 0

for (x, y, filenames) in walk(folder):
		
	for tempfile in filenames :
		
		if naiive_bayes(open(folder + "\\" + tempfile)) == "alt.atheism" :

			count += 1

print str((float(count)/float(500))*100) + "% accuracy"


'''

files = []
folders = []

folder = "F:\\Machine Learning\\project1\\testing"

for (dirpath, dirnames, filenames) in walk(folder):
    
    for d in dirnames :

    	folders.append(dirpath+'\\'+d)

    break

i = 0

count2 = 0

for f in folders :

	count = 0

	for (x, y, filenames) in walk(f):

		for tempfile in filenames :
			
			#print tempfile, dirnames[i]
			if naiive_bayes(open(dirpath+"\\"+dirnames[i]+"\\"+tempfile)) == dirnames[i] :

				count += 1
				count2 += 1
			#break

		#break

	#break

	print dirnames[i] + " : " + str((float(count)/float(500))*100) + "% accuracy"

	i += 1

print "overall accuracy : " + str((float(count2)/float(10000))*100) + "% accuracy"