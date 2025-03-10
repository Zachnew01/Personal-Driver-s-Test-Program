# Zachary Newman - Driver's Test Program
# Question csv: https://docs.google.com/spreadsheets/d/16gPRqgF9ePJ2fukIEFx9QIZ-iuKubD5zve7sqRelLtM/edit?gid=1741480597#gid=1741480597
# Manual: https://www.dot.state.pa.us/Public/DVSPubsForms/BDL/BDL%20Manuals/Manuals/PA%20Drivers%20Manual%20By%20Chapter/English/PUB%2095.pdf


import sys
import csv
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow
from QuestionScreen import Ui_QuestionScreen

DEBUG = True
# Pre-set example list of questions
questionList = [["WHEN YOU SEE THIS SIGN, YOU MUST:",
                 "Images\C2-Q1.png",
                 "Stop completely, check for pedestrians, and cross traffic",
                 "Slow down without coming to a complete stop",
                 "Stop completely and wait for a green light",
                 "Slow down and check for traffic",
                 1],
                ["THIS IS THE SHAPE AND COLOR OF A __________ SIGN.",
                 "Images\C2-Q2.png",
                 "Stop",
                 "Wrong Way",
                 "Yield",
                 "Do not enter",
                 3]
                ]
currentQuestion = 0
questionAnswered = False
numberCorrectAnswers = 0


class QuestionScreen(QMainWindow,Ui_QuestionScreen): # Class of Question Screen

    def __init__(self, *args, obj=None, **kwargs):
        super(QuestionScreen, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.nextQuestionInit()

        self.A_Button.clicked.connect(self.aButtonFunc)
        self.B_Button.clicked.connect(self.bButtonFunc)
        self.C_Button.clicked.connect(self.cButtonFunc)
        self.D_Button.clicked.connect(self.dButtonFunc)
        self.Next_Button.clicked.connect(self.nextButtonFunc)

    # END OF __init


    def nextQuestionInit(self):
        global questionList
        global currentQuestion
        global DEBUG

        if currentQuestion < len(questionList):
            # set QuestionNumberLabel
            questionNumStr = "Question # {}".format(str(currentQuestion + 1))
            self.questionNumberLabel.setText(questionNumStr)

            # set Question Label
            self.questionLabel.setText(questionList[currentQuestion][0])

            # set Image
            imageText = questionList[currentQuestion][1]
            if DEBUG:
                print(imageText)
            self.imageLabel.setPixmap(QtGui.QPixmap(imageText))

            # set A_Button
            buttonText = questionList[currentQuestion][2]
            self.A_Button.setText(buttonText)
            
            # set B_Button
            buttonText = questionList[currentQuestion][3]
            self.B_Button.setText(buttonText)
            
            # set C_Button
            buttonText = questionList[currentQuestion][4]
            self.C_Button.setText(buttonText)
            
            # set D_Button
            buttonText = questionList[currentQuestion][5]
            self.D_Button.setText(buttonText)
        else: # The program has run out of questions
            self.close()

    # END OF nextQuestionInit


    def aButtonFunc(self):
        global questionAnswered
        global DEBUG
        if not(questionAnswered):
            if DEBUG:
                print("Button A press valid")
            questionAnswered = True
            feedback = self.answerValidation(1)
            self.OutputLabel.setText(feedback)
        else:
            if DEBUG:
                print("Button A press invalid")
    # END OF aButtonFunc


    def bButtonFunc(self):
        global questionAnswered
        global DEBUG
        if not(questionAnswered):
            if DEBUG:
                print("Button B press valid")
            questionAnswered = True
            feedback = self.answerValidation(2)
            self.OutputLabel.setText(feedback)
        else:
            if DEBUG:
                print("Button B press invalid")
    # END OF bButtonFunc


    def cButtonFunc(self):
        global questionAnswered
        global DEBUG
        if not(questionAnswered):
            if DEBUG:
                print("Button C press valid")
            questionAnswered = True
            feedback = self.answerValidation(3)
            self.OutputLabel.setText(feedback)
        else:
            if DEBUG:
                print("Button C press invalid")
    # END OF cButtonFunc


    def dButtonFunc(self):
        global questionAnswered
        global DEBUG
        if not(questionAnswered):
            if DEBUG:
                print("Button D press valid")
            questionAnswered = True
            feedback = self.answerValidation(4)
            self.OutputLabel.setText(feedback)
        else:
            if DEBUG:
                print("Button D press invalid")
    # END OF dButtonFunc


    def nextButtonFunc(self):
        global questionAnswered
        global currentQuestion
        global DEBUG
        if questionAnswered:
            if DEBUG:
                print("Next Button press valid")
            questionAnswered = False
            self.OutputLabel.setText("")
            currentQuestion = currentQuestion + 1
            self.nextQuestionInit()
        else:
            if DEBUG:
                print("Next Button press invalid")
    # END OF nextButtonFunc


    def answerValidation(self, buttonAnswer):
        global questionList
        global currentQuestion
        global numberCorrectAnswers
        correctAnswer = questionList[currentQuestion][6]
        buttonLetter = self.numberToLetter(buttonAnswer)
        correctLetter = self.numberToLetter(correctAnswer)

        if (buttonAnswer == correctAnswer):
            result = "{} is correct.".format(buttonLetter)
            numberCorrectAnswers = numberCorrectAnswers + 1
        else:
            result = "{} is incorrect. {} is correct.".format(buttonLetter, correctLetter)
        return result
    # END OF answerValidation


    def numberToLetter(self, number):
        match number:
            case 1:
                return "A"
            case 2:
                return "B"
            case 3:
                return "C"
            case 4:
                return "D"
            case _:
                return "Null"
    # End of numberToLetter
            

# END OF QuestionScreen
        

def main(): # # Main command line program loop
    global numberCorrectAnswers
    global questionList
    global DEBUG
    global currentQuestion

    # Initialize questionList from file
    tempQuestionList = []
    with open('questions.csv',newline='') as csvfile:
        rawQuestionList = csv.reader(csvfile, delimiter='&', quotechar='|')
        for row in rawQuestionList:
            tempRow = []
            counter = 0
            for element in row:
                if (element[0:2] == "\"," or element[0:2] == ",\""):
                    element = element[2:]
                elif (element[0:1] == "," or element[0:1] == "\""):
                    element = element[1:]
                if counter == 6:
                    element = int(element)
                tempRow.append(element)
                counter = counter + 1
            tempQuestionList.append(tempRow)
    questionList = tempQuestionList
    #print(tempQuestionList)
    
    # Showing the question screen
    app = QApplication(sys.argv)

    window = QuestionScreen()
    window.show()
    app.exec()

    score = "Number Correct: {}/{}".format(numberCorrectAnswers,len(questionList))
    print(score)
# END OF main

main() # Calling main function to run the code
