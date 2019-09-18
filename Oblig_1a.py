
class Oblig1a(object):
	def __init__(self):
		self.txt = None
		self.read_file()
		self.word_list = self.txt.split()
		self.line_list = None
		self.read_file_to_list()
		self.word_list2 = None
		self.split_list()
	
	def read_file(self):
		f = open("InO1.txt", encoding="utf-8")
		self.txt = f.read()
		f.close

	def count_substrings(self, substring):
		print("Bokstavsekvensen \'{0}\' forekommer {1} ganger i teksten.".format(substring,self.txt.count(substring))) 

	def count_ends_with(self, ending):
		count = 0
		for w in self.word_list:
			if(w.endswith(ending)):
				count+=1
		print("Bokstavendelsen-{0} forekommer {1} ganger i teksten.".format(ending, count))

	def two_last_letters(self):
		return [word[-2:] for word in self.word_list]

	def list_to_streng(self,list):
		return " ".join(list)

	# Oppgave 4 Tokenisering
	#a)
	def read_file_to_list(self):
		with open('InO1.txt', encoding="utf-8") as f:
			self.line_list = [line.rstrip('\n') for line in f]
		f.close()
		return self.line_list

	def split_list(self):
		self.word_list2 = [word for line in self.word_list for word in line.split()]

	#b)	
	def count_words(self):
		count = 0
		for w in self.word_list2:
			count += 1
		print("Antall ord i teksten er:", count)

	#5 Tokenisering av norsk tekst

	def write_to_file(self):
		f = open("test.txt", 'w')

		for w in self.word_list2:
			f.write(w + '\n')
		f.close()

ob = Oblig1a()
ob.count_substrings('er')
ob.count_ends_with('er')
#ending_list = ob.two_last_letters()
#print(ob.list_to_streng(ending_list))
ob.count_words()
print("Antall linjer i teksten er:",len(ob.line_list))