import random


class Word():

    def __init__(self):
        self.word = " "

    def get_word(self):
        i = random.randint(0,6)
        words_list = ["algorithm", "barycenter", "chebyshev", "determinant", "diffusion", "eigen", "fourier"]
        word = words_list[i]
        self.word = word

    #def show_word(self):


class Letter():

    def __init__(self):
        self.letter = " "

    def get_letter(self):
        entry = str(input("Guess a letter [a-z]: "))
        self.letter = entry


class Picture():

    def show_picture_1(self):
        print ("  ___  ")
        print (" /   \ ")
        print ("  ___  ")
        print (" \   / ")
        print ("  \ /  ")
        print ("   o   ")
        print ("  /|\  ")
        print ("  / \  ")

    def show_picture_2(self):
        print (" /   \ ")
        print ("  ___  ")
        print (" \   / ")
        print ("  \ /  ")
        print ("   o   ")
        print ("  /|\  ")
        print ("  / \  ")

    def show_picture_3(self):
        print (" \   / ")
        print ("  \ /  ")
        print ("   o   ")
        print ("  /|\  ")
        print ("  / \  ")

    def show_picture_4(self):
        print ("  \ /  ")
        print ("   o   ")
        print ("  /|\  ")
        print ("  / \  ")

    def show_picture_5(self):
        print ("   x   ")
        print ("  /|\  ")
        print ("  / \  ")


class Jumper(Word,Letter,Picture):

    def __init__(self):
        self



jumper = Jumper()

jumper.get_word()

#jumper.show_word()

jumper.get_letter()

#if jumper.get_letter() in jumper.get_word():
    #jumper.show_word()

#elif.....: jumper.get-picture_1()






























