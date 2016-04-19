'''
Created on Apr 18, 2016

@author: pbuitrag
'''
import itertools
from twisted.persisted.sob import guessType

class NumberAnalyzer:
    
    options = []
    
    def __init__(self, nDigits):
        digits = range(0,10)
        self.options = list(itertools.permutations(digits,nDigits))
        nOptions = len(self.options)
        print "There are %d options." %nOptions

    def matchesGuess(self, optionT, guess, fixes, pics):
        nFixes = 0
        nPics = 0
        
        option = list(optionT)
        print option
        #if option[0] == 0 and option[1] == 1 and option[2] == 3:
        #    print "Here we go"
        
        for digitOption, digitGuess in itertools.izip (option, guess):    
            print "Comparing..."
            print digitOption
            print digitGuess
            
            if digitOption in guess: 
                if digitOption == digitGuess:
                    nFixes += 1
                else:
                    nPics += 1
        
        return nFixes == fixes and nPics == pics

    def processGuess(self, guessP, fixes, pics):
        nOptions = len(self.options)
        print "There are %d options." %nOptions
        
        guess = self.guessToIntList(guessP)
        nIter = 0
        print type(self.options)
        #self.options[:] = [option for option in self.options if self.matchesGuess(option, guess, fixes, pics)]
        newOptions = []
        
        '''for option in self.options:
            if self.matchesGuess(option, guess, fixes, pics):
                newOptions.append(option)
        
        '''
        
        for option in self.options:
            if not self.matchesGuess(option, guess, fixes, pics):
                self.options.remove(option)
            nIter += 1
        
        #self.options = newOptions
        
        print "Checked %d tuples" %nIter
        nOptions = len(self.options)
        print "There are %d options." %nOptions  
        if nOptions < 30:
            print self.options
        
        
    def guessToIntList(self, guess):
        guessS = str(guess)
        guess = []
        for digit in guessS:
            guess.append(int(digit))
        return guess

        
digits = input('How many digits? > ')
analyzer = NumberAnalyzer(digits)
guess = input('Next guess? > ')
 
#print analyzer.matchesGuess((0,1,3), (3,4,2), 3, 0)
 

while isinstance( guess, ( int, long ) ):
        fixes = input('How many fixes? > ')
        pics = input('How many pics? > ')
        analyzer.processGuess(guess, fixes, pics)
        guess = input('Next guess? > ')
