import json
import re
import string

def create_dictionary(file, category) :

	file = open(file)
	lines_from_file = file.readlines()
	
	count = 0

	#global d

	# read from json file
	with open('F:\\Machine Learning\\project1\\data.json', 'r') as f :

		try :
			d = json.load(f)
		
		except ValueError :
			d = {}


		#check if this category exists in the dictionay

		if category not in d :

			d[category] = [{}, 0]

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

				if each_word:
					
					if each_word in d[category][0] :
						d[category][0][each_word] += 1

					else :
						d[category][0][each_word] = 1
					
					count += 1

		if d[category][1] :

			d[category][1] += count

		else :

			d[category][1] = count

	#push new data to json file
	with open('F:\\Machine Learning\\project1\\data.json', 'w') as f:

		json.dump(d, f, indent=4)


from os import walk

files = []
folders = []

folder = "F:\\Machine Learning\\project1\\training"

for (dirpath, dirnames, filenames) in walk(folder):
    
    for d in dirnames :

    	folders.append(dirpath+'\\'+d)

    break

i = 0

for f in folders :

	for (x, y, filenames) in walk(f):
		
		for tempfile in filenames :
			
			#print tempfile, dirnames[i]
			create_dictionary(dirpath+"\\"+dirnames[i]+"\\"+tempfile, dirnames[i])
			#break

		#break

	#break

	i += 1