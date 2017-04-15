#!/usr/bin/env python

#!/usr/bin/python
# -*- coding: utf-8 -*-

from firebase import firebase
import sys
import random
import subprocess
import os.path
import requests

from datetime import datetime
random.seed()

from PyQt4.QtGui import *
from PyQt4.QtCore import *

fb = firebase.FirebaseApplication('https://os-lab.firebaseio.com/')

class Example(QWidget):

	def resource_path(self,relative_path):
    		""" Get absolute path to resource, works for dev and for PyInstaller """
    		try:
        		# PyInstaller creates a temp folder and stores path in _MEIPASS
        		base_path = sys._MEIPASS
    		except Exception:
        		base_path = os.path.abspath(".")

    		return os.path.join(base_path, relative_path)
	
	def closeEvent(self,event):
    		result = QMessageBox.question(self, "Confirm Exit...", "Are you sure you want to exit ?", QMessageBox.Yes| QMessageBox.No)
    		event.ignore()
    
    		if result == QMessageBox.Yes:
     			event.accept()
    
   	def __init__(self):
		super(Example, self).__init__()     
		self.initUI()
        
        
	def initUI(self):
		font1 = QFont()
		font1.setPointSize(14)
		box1 = QMessageBox()
		box1.setFont(font1)
		box1.setWindowTitle("Operating System Lab")
		img = self.resource_path("img.png")
		box1.setIconPixmap(QPixmap(img))
		box1.setText("Welcome!\nIT204 Operating Systems Lab\nLab 1.2: Shell Scripting\nIIIT-Vadodara\n (Gandhinagar Campus)\nWinter 2017\n\nDeveloped by: Vague Hacker")
		box1.setStyleSheet('qproperty-alignment: AlignCenter;background-color: white')
		box1.setStandardButtons(QMessageBox.Ok)
		box1.exec_()
		
		self.id = '0'
		self.takeId()
        
		font = QFont()
		font.setPointSize(12)
		self.setFont(font)
        
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle('Operating System Lab 1.2')
		self.setFixedSize(1000,640)
        	
		self.interface()
        
		self.move(180, 10)
		self.show()
        
	def interface(self):
		self.start_time = datetime.now()
	
		self.max = 0
		self.i = 0
		self.score = -6
		self.maxpoint = 6
		self.flag = 0
		self.text1 = QTextBrowser(self)
		self.text1.move(80,50)
		self.text1.setFixedSize(840,60)
		
		self.text2 = QTextEdit(self)
		self.text2.move(80,150)
		self.text2.setFixedSize(400,300)
		
		self.text3 = QTextBrowser(self)
		self.text3.move(520,150)
		self.text3.setFixedSize(400,300)
		
		self.text4 = QTextBrowser(self)
		self.text4.move(80,120)
		self.text4.setFixedSize(400,30)
		self.text4.setText("Your Code")
		self.text4.setAlignment(Qt.AlignCenter)
		
		self.text5 = QTextBrowser(self)
		self.text5.move(520,120)
		self.text5.setFixedSize(400,30)
		self.text5.setText("Output")
		self.text5.setAlignment(Qt.AlignCenter)
		
		self.text6 = QTextBrowser(self)
		self.text6.move(420,10)
		self.text6.setFixedSize(150,30)
		
		self.text7 = QTextBrowser(self)
		self.text7.move(80,10)
		self.text7.setFixedSize(150,30)
		self.text7.setText("ID : "+self.id)
		self.text7.setAlignment(Qt.AlignCenter)
		
		self.text8 = QTextBrowser(self)
		self.text8.move(80,460)
		self.text8.setFixedSize(840,30)
		self.text8.setText("Command line input")
		
		self.text9 = QTextEdit(self)
		self.text9.move(80,490)
		self.text9.setFixedSize(840,100)
		
		self.btn1 = QPushButton("Submit", self)
		self.btn1.move(460, 600)
		self.btn1.clicked.connect(lambda: self.check())
		
		self.btn2 = QPushButton("Next Level", self)
		self.btn2.move(580, 600)
		self.btn2.clicked.connect(lambda: self.assignment1())
		
		self.btn3 = QPushButton("Previous Level", self)
		self.btn3.move(300, 600)
		self.btn3.clicked.connect(lambda: self.moveback())
		
		self.btn4 = QPushButton("Test", self)
		self.btn4.move(180, 600)
		self.btn4.clicked.connect(lambda: self.test())
		
		self.btn5 = QPushButton("Hint", self)
		self.btn5.move(720, 600)
		self.btn5.clicked.connect(lambda: self.hint())
		
		self.btn6 = QPushButton("Skip", self)
		self.btn6.move(830, 10)
		self.btn6.clicked.connect(lambda: self.skip())
		
		self.button = QPushButton(self)
		help = self.resource_path("help.png")
		icon = QIcon(help)
		self.button.setIcon(icon)
		self.button.move(20, 10)
		self.button.clicked.connect(lambda: self.instruct())
		
		if self.i==0:
			self.assignment1()
			
	def instruct(self):
		result = QMessageBox.information(self, "Instructions", "1. This lab consists of 10 assessment questions and 3 bonus questions.\n\n2. Each assessment question carries 6 marks.\n\n3. Maximum Score - 60\n\n4. No score for bonus questions - The bonus questions are for learning purpose.\n\n5. If you get stuck on a question, use hint.\n\n6. After using hint in a question, only 80% of the score in that question can be earned.\n\n7. Your score for any question will be rewarded after you reach the next level\n\n8. You can test your solution using the test button. Score won't be deducted for testing.\n\n9. No score for skipped questions.\n\n10. Once you skip a question you cannot come back to solve it later. However, you can come back to view the previous questions and test them.\n\n11. The Application works offline, however, internet connection is required while submission of score at the end.\n\n12. For file handling, the current working directory is Lab1.2\n\n13. Calling external applications like vi, gedit, octave, python may crash the application. So refrain yourself from using them.\n\n14. Use command-line arguments as specified, to test your code.", QMessageBox.Ok)
	
	def skip(self):
		result = QMessageBox.question(self, "Warning", "Are you sure you want to skip ?", QMessageBox.Yes| QMessageBox.No)
    
    		if result == QMessageBox.Yes:
     			self.flag=1
			self.assignment1()					
			
	def moveback(self):
		self.i = self.i-1
		
		if self.i==1:
			self.btn3.setEnabled(False)
		else:
			self.btn3.setEnabled(True)
		if self.i==self.max:
			self.btn2.setEnabled(False)
		else:
			self.btn2.setEnabled(True)
		if self.i==4 or self.i==11 or self.i==13:
			self.btn1.setEnabled(False)
			self.btn2.setEnabled(True)
		else:
			self.btn1.setEnabled(True)
			self.btn6.setEnabled(True)
		self.btn5.setEnabled(True)
			
		self.text3.setText("")
		self.text9.setText("")
		
		
		if self.i==1:
			self.text1.setText("Level 1 - Write a shell script program to display list of user currently logged in")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==2:
			self.text1.setText("Level 2 - Write a shell script that takes a command-line argument and reports on whether it is directory or a file")
			self.text2.setText("#!/bin/bash\n\n#If argument is directory then display \"DIRECTORY\"\n#Or else if file then display \"FILE\"")
			self.text9.setEnabled(True)
			self.text9.setText("<argument>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==3:
			self.text1.setText("Level 3 - Write a shell script that accepts one or more files as arguments and converts all of them to uppercase, provided they exist in the current directory")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(True)
			self.text9.setText("<file1> <file2> ...")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==4:
			self.text1.setText("Bonus - Write a shell script that determines the period for which a specified user is working on the system")
			self.text2.setText("#!/bin/bash\n\nlast -R <user>\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==5:
			self.text1.setText("Level 4 - Write a shell script that accepts a file name, starting and ending line numbers as arguments and displays all the lines between the given line numbers")
			self.text2.setText("#!/bin/bash\n\n#Use sed command")
			self.text9.setEnabled(True)
			self.text9.setText("<file> <starting line number> <ending line number>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==6:
			self.text1.setText("Level 5 - Write a shell script that deletes all lines containing a specified word in a file supplied as arguments to it")
			self.text2.setText("#!/bin/bash\n\n#User sed command")
			self.text9.setEnabled(True)
			self.text9.setText("<word> <file1>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==7:
			self.text1.setText("Level 6 - Write a shell script program to check whether the given number is even or odd")
			self.text2.setText("#!/bin/bash\n\n#If number is even then display \"EVEN\"\n#Or else display \"ODD\"")
			self.text9.setEnabled(True)
			self.text9.setText("<number>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==8:
			self.text1.setText("Level 7 - Write a shell script program to search whether element is present in the list or not")
			self.text2.setText("#!/bin/bash\n\n#If element exists then display \"EXISTS\"\n#Or else display \"NOT\"")
			self.text9.setEnabled(True)
			self.text9.setText("<element> <list>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==9:
			self.text1.setText("Level 8 - Write a shell script which receives two file names as arguments. It should check whether the two file contents are same or not")
			self.text2.setText("#!/bin/bash\n\n#If both files are same then display \"SAME\"\n#Or else display \"DIFFERENT\"")
			self.text9.setEnabled(True)
			self.text9.setText("<file1> <file2>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==10:
			self.text1.setText("Level 9 - Develop an interactive script that ask for a word and a file name and then tells how many times that word occurred in the file")
			self.text2.setText("#!/bin/bash\n\n#Use grep command")
			self.text9.setEnabled(True)
			self.text9.setText("<word> <file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==11:
			self.text1.setText("Bonus - Try testing the given shell script to extract a sub-string from a given string")
			self.text2.setText("#!/bin/bash\n\necho \"$1\"| cut -c $2-$3\n\n")
			self.text9.setEnabled(True)
			self.text9.setText("<string> <start-index> <end-index>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==12:
			self.text1.setText("Level 10 - Write a shell script to find the length of a given string")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(True)
			self.text9.setText("<string>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==13:
			self.text1.setText("Bonus - Explore the process attributes using the commands: ps, ps lx, ps -aux")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
	
	def assignment1(self):
		if self.i==self.max:
			self.max=self.max+1
			if self.i!=4 and self.i!=11 and self.i!=13 and self.flag==0:
				self.score = self.score + self.maxpoint
		self.i=self.i+1
		self.flag=0								#change
		
		self.text6.setText("SCORE : "+str(self.score)+"/60")
		self.text6.setAlignment(Qt.AlignCenter)
		
		if self.i==14:
			self.end_time = datetime.now()
            		diff = self.end_time - self.start_time
            		minu = str(int(diff.seconds/60))
            		seco = str(diff.seconds%60)
			
			self.text6.setText("SCORE : "+str(self.score)+"/60")
			self.text6.setAlignment(Qt.AlignCenter)
			
			box2 = QMessageBox()
			box2.setWindowTitle("Congratulations")
			box2.setText("You won!\n\nYour score - "+str(self.score)+"/60\n\nTime taken - "+minu+" minutes and "+seco+" seconds")
			box2.setStyleSheet('qproperty-alignment: AlignCenter;')
			box2.setStandardButtons(QMessageBox.No)
			buttonX = box2.button(QMessageBox.No)
        		buttonX.setText('Submit and Quit')
			buttonX.clicked.connect(lambda: self.sendscore())
			box2.exec_()
			
			if box2.clickedButton() == buttonX:
            			QApplication.quit()
		
		self.maxpoint = 6
	
		if self.i==1:
			self.btn3.setEnabled(False)
		else:
			self.btn3.setEnabled(True)
		if self.i==self.max:
			self.btn2.setEnabled(False)
		else:
			self.btn2.setEnabled(True)
		if self.i==4 or self.i==11 or self.i==13:
			self.btn1.setEnabled(False)
			self.btn2.setEnabled(True)
			self.btn6.setEnabled(False)
		else:
			self.btn1.setEnabled(True)
			self.btn6.setEnabled(True)
		self.btn5.setEnabled(True)
			
		self.text3.setText("")
		self.text9.setText("")
		
		if self.i==1:
			self.text1.setText("Level 1 - Write a shell script program to display list of user currently logged in")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==2:
			self.text1.setText("Level 2 - Write a shell script that takes a command-line argument and reports on whether it is directory or a file")
			self.text2.setText("#!/bin/bash\n\n#If argument is directory then display \"DIRECTORY\"\n#Or else if file then display \"FILE\"")
			self.text9.setEnabled(True)
			self.text9.setText("<argument>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==3:
			self.text1.setText("Level 3 - Write a shell script that accepts one or more files as arguments and converts all of them to uppercase, provided they exist in the current directory")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(True)
			self.text9.setText("<file1> <file2> ...")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==4:
			self.text1.setText("Bonus - Write a shell script that determines the period for which a specified user is working on the system")
			self.text2.setText("#!/bin/bash\n\nlast -R <user>\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==5:
			self.text1.setText("Level 4 - Write a shell script that accepts a file name, starting and ending line numbers as arguments and displays all the lines between the given line numbers")
			self.text2.setText("#!/bin/bash\n\n#Use sed command")
			self.text9.setEnabled(True)
			self.text9.setText("<file> <starting line number> <ending line number>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==6:
			self.text1.setText("Level 5 - Write a shell script that deletes all lines containing a specified word in a file supplied as arguments to it")
			self.text2.setText("#!/bin/bash\n\n#User sed command")
			self.text9.setEnabled(True)
			self.text9.setText("<word> <file1>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==7:
			self.text1.setText("Level 6 - Write a shell script program to check whether the given number is even or odd")
			self.text2.setText("#!/bin/bash\n\n#If number is even then display \"EVEN\"\n#Or else display \"ODD\"")
			self.text9.setEnabled(True)
			self.text9.setText("<number>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==8:
			self.text1.setText("Level 7 - Write a shell script program to search whether element is present in the list or not")
			self.text2.setText("#!/bin/bash\n\n#If element exists then display \"EXISTS\"\n#Or else display \"NOT\"")
			self.text9.setEnabled(True)
			self.text9.setText("<element> <list>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==9:
			self.text1.setText("Level 8 - Write a shell script which receives two file names as arguments. It should check whether the two file contents are same or not")
			self.text2.setText("#!/bin/bash\n\n#If both files are same then display \"SAME\"\n#Or else display \"DIFFERENT\"")
			self.text9.setEnabled(True)
			self.text9.setText("<file1> <file2>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==10:
			self.text1.setText("Level 9 - Develop an interactive script that ask for a word and a file name and then tells how many times that word occurred in the file")
			self.text2.setText("#!/bin/bash\n\n#Use grep command")
			self.text9.setEnabled(True)
			self.text9.setText("<word> <file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==11:
			self.text1.setText("Bonus - Try testing the given shell script to extract a sub-string from a given string")
			self.text2.setText("#!/bin/bash\n\necho \"$1\"| cut -c $2-$3\n\n")
			self.text9.setEnabled(True)
			self.text9.setText("<string> <start-index> <end-index>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==12:
			self.text1.setText("Level 10 - Write a shell script to find the length of a given string")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(True)
			self.text9.setText("<string>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==13:
			self.text1.setText("Bonus - Explore the process attributes using the commands: ps, ps lx, ps -aux")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		
		if self.i==1:
			box = QMessageBox()
			box.setWindowTitle("Instructions")
			box.setText("1. This lab consists of 10 assessment questions and 3 bonus questions.\n\n2. Each assessment question carries 6 marks.\n\n3. Maximum Score - 60\n\n4. No score for bonus questions - The bonus questions are for learning purpose.\n\n5. If you get stuck on a question, use hint.\n\n6. After using hint in a question, only 80% of the score in that question can be earned.\n\n7. Your score for any question will be rewarded after you reach the next level\n\n8. You can test your solution using the test button. Score won't be deducted for testing.\n\n9. No score for skipped questions.\n\n10. Once you skip a question you cannot come back to solve it later. However, you can come back to view the previous questions and test them.\n\n11. The Application works offline, however, internet connection is required while submission of score at the end.\n\n12. For file handling, the current working directory is Lab1.2\n\n13. Calling external applications like vi, gedit, octave, python may crash the application. So refrain yourself from using them.\n\n14. Use command-line arguments as specified, to test your code.\n\n-> All the Best!")
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_()
			
	def check(self):
	
		win=0
		
		
		temp = self.text2.toPlainText()
		file1 = open('.data.sh','w')
		file1.write(temp)
		file1.close()	
		
		if self.i==1:
			try:
				ctext = subprocess.check_output(["users"])
				output = subprocess.check_output(["sh", ".data.sh"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			
			if output==ctext:
				win=1
		elif self.i==2:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", ".temp/myfile2"])
				output2 = subprocess.check_output(["sh", ".data.sh", ".temp/mydir1"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("FILE")!=-1 and output2.find("DIRECTORY")!=-1:
				win=1
		elif self.i==3:
			win=1
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", ".myfile1"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
				
			x = "myfile1".upper()
			if not os.path.isfile(x):
				win=0
			else:
				f=open("myfile1", "w+")
				os.remove("MYFILE1")
		elif self.i==5:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", ".temp/myfile2", "2", "3"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("You should be able to use a text editor\nYou should be able to understand system boot and shutdown processes, init and initscripts")!=-1:
				win=1
		elif self.i==6:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", "and", ".temp/myfile2"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("and")==-1 and output1.find("You should be able to use a text editor")!=-1 and len(output1)!=0:
				win=1
		elif self.i==7:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", "23"])
				output2 = subprocess.check_output(["sh", ".data.sh", "46"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("ODD")!=-1 and output2.find("EVEN")!=-1:
				win=1
		elif self.i==8:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", "1", "1", "2", "3"])
				output2 = subprocess.check_output(["sh", ".data.sh", "4", "1", "2", "3"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("EXISTS")!=-1 and output2.find("NOT")!=-1:
				win=1
		elif self.i==9:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", ".temp/myfile2", ".temp/myfile4"])
				output2 = subprocess.check_output(["sh", ".data.sh", ".temp/myfile3", ".temp/myfile4"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("DIFFERENT")!=-1 and output2.find("SAME")!=-1:
				win=1
		elif self.i==10:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", "You", ".temp/myfile2"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("6")!=-1:
				win=1
		elif self.i==12:
			try:
				output1 = subprocess.check_output(["sh", ".data.sh", "yellow"])
				output2 = subprocess.check_output(["sh", ".data.sh", "catterpillerguy"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if output1.find("6")!=-1 and output2.find("15")!=-1:
				win=1
				
		if win==1:
			box1 = QMessageBox()
			box1.setWindowTitle("Congratulations")
			box1.setText("Correct Answer!")
			box1.setStandardButtons(QMessageBox.Ok)
			box1.exec_()
			
			self.btn1.setEnabled(False)
			self.btn2.setEnabled(True)
			self.btn5.setEnabled(False)
			self.btn6.setEnabled(False)
				
		else:
			box2 = QMessageBox()
			box2.setWindowTitle("Sorry")
			box2.setText("Wrong Answer!")
			box2.setStandardButtons(QMessageBox.Ok)
			box2.exec_()
	
	def takeId(self):
		text, ok = QInputDialog.getText(self, 'Sign in', 'Enter your ID: (Ex - 201X5X0XX)')
      		if ok:
      			self.id = str(text)
      			if len(str(text))!=9:
      				self.takeId()
      			try:
         			result = fb.get("Lab1_2/"+self.id, None)
         			if result==None:
         				result = fb.put("Lab1_2", self.id, ["-1"])
         			else:
         				result = fb.put("Lab1_2", self.id, result+["-1"])
         			attempt = fb.get("Lab1_2/"+self.id, None)
         			self.att_value = len(attempt)-1
         		except Exception:
         			box = QMessageBox()
				box.setWindowTitle("Warning")
				box.setText("Network error! Check your connection")
				box.setStandardButtons(QMessageBox.Ok)
				box.exec_()
				self.takeId()
		else:	
			exit()
		
	
	def test(self):
		self.inlist = []
		temp = self.text2.toPlainText()
		file1 = open('.data.sh','w')
		file1.write(temp)
		file1.close()
		
		try:
			text = str(self.text9.toPlainText())
			self.inlist = text.split()
			output = subprocess.check_output(["sh", ".data.sh"]+self.inlist)
			self.text3.setText(output)
		except Exception:
			box1 = QMessageBox()
			box1.setIcon(QMessageBox.Critical)
			box1.setWindowTitle("Warning")
			box1.setText("Syntax Error!")
			box1.setStandardButtons(QMessageBox.Ok)
			box1.exec_()		
			
	def hint(self):
		self.maxpoint = 4.8
		self.btn5.setEnabled(False)
		self.text2.setText("#!/bin/bash\n")
		
		if self.i==1:
			self.text2.append("users")
		elif self.i==2:
			self.text2.append("if ...\nthen\necho \"DIRECTORY\"\nelif ...\nthen\necho \"FILE\"\nfi")
		elif self.i==3:
			self.text2.append("for i in $*\ndo\na=`echo $i | tr <expr> `\nmv $i $a\ndone")
		elif self.i==4:
			self.text2.append("last -R <user>\n\n")		
		elif self.i==5:
			self.text2.append("sed -n <expr> <file>")
		elif self.i==6:
			self.text2.append("sed <expr> <file>")
		elif self.i==7:
			self.text2.append("if ...\nthen\necho \"EVEN\"\nelse\necho \"ODD\"\nfi")
		elif self.i==8:
			self.text2.append("elem=$1\nshift\nfor i in $*\ndo ...\ndone")
		elif self.i==9:
			self.text2.append("if cmp ...\nthen\necho \"SAME\"\nelse\necho \"DIFFERENT\"\nfi")
		elif self.i==10:
			self.text2.append("grep -wc <expr> <file>")
		elif self.i==12:
			self.text2.append("string=\"$1\"\nlength=...\necho $length")
		elif self.i==13:
			self.text2.append("ps")
			
	def sendscore(self):
		try:
			result = fb.put("Lab1_2/"+self.id,str(self.att_value),self.score)
		except Exception:
			box = QMessageBox()
			box.setWindowTitle("Warning")
			box.setText("Network error! Check your connection")
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_()
			self.sendscore()	
	
def main():
    
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
