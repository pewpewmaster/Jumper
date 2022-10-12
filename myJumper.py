import random


# Creat a picture
class parachute():

	def __init__(self, score):
		self.score = score
		self.size  = 10
		self.parachute = ["  ___  ", " /   \ ", "  ___  ", " \   / ", "  \ /  ", "   o   ", "  /|\  ", "  / \  ", "       ", "^^^^^^^"]

	def display(self):
		left_parachut = 5 - self.score 
		for i in range(left_parachut, self.size):
			if i == 5 and self.score == 0:
		 		print("   x   ")
			else:
				print(self.parachute[i])
    
	def cut_line(self):
		self.score -= 1


# Count the score
class game_counter():
	def __init__(self, score):
		self.score = score
		self.is_lost_prm = False

	def count_result(self, result):
		if result == False:
			self.score -= 1
		if self.score == 0:
			self.is_lost_prm = True

	def is_lost(self):
		return self.is_lost_prm


class word():

	def __init__(self):
		self.selected_word = []
		self.guessed_word = []
		self.amount = 0

    # Choose a word randomly
	def choose_word(self):
		i = random.randint(0,6)
		words_list = ["algorithm", "barycenter", "chebyshev", "determinant", "diffusion", "eigen", "fourier"]
		self.selected_word = list(words_list[i])
		self.guessed_word = [None]*len(self.selected_word)

    # Dispaly the word
	def display(self):
		word_str = ""
		for i in range(len(self.guessed_word)):
			if self.guessed_word[i] != None:
				word_str += str(self.guessed_word[i])
				word_str += " "
			else:
				word_str += "_ "
		print(word_str)

    # Display the letter
	def guess(self, letter):
		if letter == None:
			return True
		for i in range(len(self.selected_word)):
			if letter == self.selected_word[i]:
				self.guessed_word[i] = letter
				self.selected_word[i] = None
				self.amount += 1
				return True
		return False

    # End condition
	def is_done(self):
		if len(self.selected_word) == self.amount:
			return True
		else:
			return False


# Creat a class contains classes above
class game():

	def __init__(self, parachute, game_counter, word):
		self.parachute = parachute
		self.game_counter = game_counter
		self.word = word

    # User input letters
	def guess_once(self):
		self.word.display()
		self.parachute.display()
		letter = input("Guess a letter [a-zl:")
		result = self.word.guess(letter)
		if result == False:
			self.parachute.cut_line()
			self.game_counter.count_result(False)

	# main function
	def play(self):
		self.word.choose_word()
		while True:
			self.guess_once()
			if self.word.is_done():
				self.word.display()
				self.parachute.display()
				break
			if self.game_counter.is_lost():
				self.word.display()
				self.parachute.display()
				break
		exit(0)
		

# Initial score is 5
game = game(parachute(5), game_counter(5), word())
game.play()
		

















