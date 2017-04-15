#!/usr/bin/env python

#!/usr/bin/python
# -*- coding: utf-8 -*-

from firebase import firebase
import sys
import random
import subprocess
import os
import requests

from datetime import datetime
random.seed()

from PyQt4.QtGui import *
from PyQt4.QtCore import *

fb = firebase.FirebaseApplication('https://os-lab-winter-2017.firebaseio.com/')
		
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
		box1.setIconPixmap(QPixmap(img))				#change
		box1.setText("Welcome!\nIT204 Operating Systems Lab\nLab 1.1: Basic Unix commands\nIIIT-Vadodara\n (Gandhinagar Campus)\nWinter 2017\n\nDeveloped by: Vague Hackers")
		box1.setStyleSheet('qproperty-alignment: AlignCenter;background-color: white')
		box1.setStandardButtons(QMessageBox.Ok)
		box1.exec_()
		
		self.id = '0'
		self.takeId()
        
		font = QFont()
		font.setPointSize(12)
		self.setFont(font)
        
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle('Operating Systems Lab 1.1')
		self.setFixedSize(1000,640)
        
		self.interface()
        
		self.move(180, 10)
		self.show()
        
	def interface(self):
		self.start_time = datetime.now()
	
		self.max = 0
		self.i = 0
		self.score = -4
		self.maxpoint = 4
		self.flag = 0					#change
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
		
		self.btn6 = QPushButton("Skip", self)				#change
		self.btn6.move(830, 10)
		self.btn6.clicked.connect(lambda: self.skip())
		
		if self.i==0:
			#os.chdir("temp")
			self.assignment1()				
			
	def skip(self):	
		result = QMessageBox.question(self, "Warning", "Are you sure you want to skip ?", QMessageBox.Yes| QMessageBox.No)
    
    		if result == QMessageBox.Yes:
     			self.flag=1
			self.assignment1()						#change
				
		
			
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
		if self.i==3:
			self.btn1.setEnabled(False)
			self.btn2.setEnabled(True)
		else:
			self.btn1.setEnabled(True)
			self.btn6.setEnabled(True)				#change
		self.btn5.setEnabled(True)
			
		self.text3.setText("")
		self.text9.setText("")
		
		if self.i==1:
			self.text1.setText("Level 1 - Use echo command to print your id")
			self.text2.setText("#!/bin/bash\n\n")	
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')	
		elif self.i==2:
			self.text1.setText("Level 2 - Use the appropriate command to determine your login shell")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==3:
			self.text1.setText("Bonus - Try using the /etc/passwd file to verify the result of previous step")
			self.text2.setText("#!/bin/bash\n\n#try opening file - /etc/passwd")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==4:
			self.text1.setText("Level 3 - Use the who command and redirect the result to a file called myfile1")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile1\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==5:
			self.text1.setText("Level 4 - Use the more command to see the contents of myfile1")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile1\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==6:
			self.text1.setText("Level 5 - Use the date and who commands in sequence (in one line) such that the output of date will display on the screen and the output of who will be redirected to a file called myfile2")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile2\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==7:
			self.text1.setText("Level 6 - Use the more command to check the contents of myfile2")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile2\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==8:
			self.text1.setText("Level 7 - Write a sed command that deletes the first character in each line in a file")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile3\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==9:
			self.text1.setText("Level 8 - Write a sed command that deletes the character before the last character in each line in a file")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile3\"\n\n")
			self.text9.setEnabled(False)		
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==10:
			self.text1.setText("Level 9 - Write a sed command that swaps the first and second words in each line in a file")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile3\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==11:
			self.text1.setText("Level 10 - Pipe your /etc/passwd file to awk, and print out the home directory of each user")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==12:
			self.text1.setText("Bonus - Try testing the given grep script that tells how many lines of a file contain a word (use command line input)")
			self.text2.setText("#!/bin/bash\n\ngrep -c \"$1\"  $2")
			self.text9.setEnabled(True)
			self.text9.setText("<word> <file>")
			self.text9.setStyleSheet('background-color:white;')
	
	def assignment1(self):
	
		if self.i==self.max:
			self.max=self.max+1
			if self.i!=3 and self.i!=12 and self.flag==0:		#change
				self.score = self.score + self.maxpoint
		self.i=self.i+1
		self.flag=0
		
		self.text6.setText("SCORE : "+str(self.score)+"/40")
		self.text6.setAlignment(Qt.AlignCenter)
		
		if self.i==13:
			self.end_time = datetime.now()
            		diff = self.end_time - self.start_time
            		minu = str(int(diff.seconds/60))
            		seco = str(diff.seconds%60)
			
			self.text6.setText("SCORE : "+str(self.score)+"/40")
			self.text6.setAlignment(Qt.AlignCenter)
			
			box2 = QMessageBox()
			box2.setWindowTitle("Congratulations")
			box2.setText("You won!\n\nYour score - "+str(self.score)+"/40\n\nTime taken - "+minu+" minutes and "+seco+" seconds")
			box2.setStyleSheet('qproperty-alignment: AlignCenter;')
			box2.setStandardButtons(QMessageBox.No)
			buttonX = box2.button(QMessageBox.No)
        		buttonX.setText('Submit and Quit')
        		buttonX.clicked.connect(lambda: self.sendscore())
			box2.exec_()
			if box2.clickedButton() == buttonX:
            			QApplication.quit()
		
		self.maxpoint = 4
	
		if self.i==1:
			self.btn3.setEnabled(False)
		else:
			self.btn3.setEnabled(True)
		if self.i==self.max:
			self.btn2.setEnabled(False)
		else:
			self.btn2.setEnabled(True)
		if self.i==3 or self.i==12:
			self.btn1.setEnabled(False)
			self.btn2.setEnabled(True)
			self.btn6.setEnabled(False)			#change
		else:
			self.btn1.setEnabled(True)
			self.btn6.setEnabled(True)				#change
		self.btn5.setEnabled(True)	
		
		self.text3.setText("")
		self.text9.setText("")
		
		
		if self.i==1:
			self.text1.setText("Level 1 - Use echo command to print your id")
			self.text2.setText("#!/bin/bash\n\n")	
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')	
		elif self.i==2:
			self.text1.setText("Level 2 - Use the appropriate command to determine your login shell")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==3:
			self.text1.setText("Bonus - Try using the /etc/passwd file to verify the result of previous step")
			self.text2.setText("#!/bin/bash\n\n#try opening file - /etc/passwd")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==4:
			self.text1.setText("Level 3 - Use the who command and redirect the result to a file called myfile1")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile1\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==5:
			self.text1.setText("Level 4 - Use the more command to see the contents of myfile1")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile1\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==6:
			self.text1.setText("Level 5 - Use the date and who commands in sequence (in one line) such that the output of date will display on the screen and the output of who will be redirected to a file called myfile2")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile2\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==7:
			self.text1.setText("Level 6 - Use the more command to check the contents of myfile2")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile2\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==8:
			self.text1.setText("Level 7 - Write a sed command that deletes the first character in each line in a file")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile3\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==9:
			self.text1.setText("Level 8 - Write a sed command that deletes the character before the last character in each line in a file")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile3\"\n\n")
			self.text9.setEnabled(False)		
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==10:
			self.text1.setText("Level 9 - Write a sed command that swaps the first and second words in each line in a file")
			self.text2.setText("#!/bin/bash\n\nfile=\"myfile3\"\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==11:
			self.text1.setText("Level 10 - Pipe your /etc/passwd file to awk, and print out the home directory of each user")
			self.text2.setText("#!/bin/bash\n\n")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==12:
			self.text1.setText("Bonus - Try testing the given grep script that tells how many lines of a file contain a word (use command line input)")
			self.text2.setText("#!/bin/bash\n\ngrep -c \"$1\"  $2")
			self.text9.setEnabled(True)
			self.text9.setText("<word> <file>")
			self.text9.setStyleSheet('background-color:white;')
		
		if self.i==1:						#change
			box = QMessageBox()
			box.setWindowTitle("Instructions")
			box.setText("1. This lab consists of 10 assessment questions and 2 bonus questions.\n\n2. Each assessment question carries 4 marks.\n\n3. Maximum Score - 40\n\n4. No score for bonus questions - The bonus questions are for learning purpose.\n\n5. If you get stuck on a question, use hint.\n\n6. After using hint in a question, only 80% of the score in that question can be earned.\n\n7. Your score for any question will be rewarded after you reach the next level\n\n8. You can test your solution using the test button. Score won't be deducted for testing.\n\n9. No score for skipped questions.\n\n10. Once you skip a question you cannot come back to solve it later. However, you can come back to view the previous questions and test them.\n\n11. The Application works offline, however, internet connection is required while submission of score at the end.\n\n12. For file handling, the current working directory is Lab1.1\n\n-> All the Best!")
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_()
			
	def check(self):
	
		win=0
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
		
		if self.i==1:
			ctext = int(self.id)
			try:
				if int(output)==ctext:
					win=1
			except Exception:
				win=0
				
		elif self.i==2:
			dt = self.resource_path("level2.sh")
			ctext = subprocess.check_output(["sh", dt])
			if output==ctext:
				win=1
		elif self.i==4:
			dt = self.resource_path("level3.sh")
			ctext = subprocess.check_output(["sh", dt])
			file2 = open('myfile1','r')
			file3 = open('.test1', 'r')
			
			x = file2.read()
			y = file3.read()
			
			file2.close()
			file3.close()
			
			if x==y:
				win=1
				self.text3.setText("myfile1 created successfully")
			
		elif self.i==5:
			dt = self.resource_path("level4.sh")
			ctext = subprocess.check_output(["sh", dt])
			if output==ctext:
				win=1
		elif self.i==6:
			dt = self.resource_path("level5.sh")
			ctext = subprocess.check_output(["sh", dt])
			file2 = open('myfile2','r')
			file3 = open('.test2', 'r')
			
			x = file2.read()
			y = file3.read()
			
			file2.close()
			file3.close()
			
			if x==y and output==ctext:
				win=1
				self.text3.append("\nmyfile2 created successfully")
		elif self.i==7:
			dt = self.resource_path("level6.sh")
			ctext = subprocess.check_output(["sh", dt])
			if output==ctext:
				win=1
		elif self.i==8:
			dt = self.resource_path("level7.sh")
			ctext = subprocess.check_output(["sh", dt])
			if output==ctext:
				win=1
		elif self.i==9:
			dt = self.resource_path("level8.sh")
			ctext = subprocess.check_output(["sh", dt])
			
			if output==ctext:
				win=1
		elif self.i==10:
			dt = self.resource_path("level9.sh")
			ctext = subprocess.check_output(["sh", dt])
			
			if output==ctext:
				win=1
		elif self.i==11:
			dt = self.resource_path("level10.sh")
			ctext = subprocess.check_output(["sh", dt])
			
			if output==ctext:
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
			self.btn6.setEnabled(False)			#change		
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
         			result = fb.get("Lab1/"+self.id, None)
         			if result==None:
         				result = fb.put("Lab1", self.id, ["-1"])
         			else:
         				result = fb.put("Lab1", self.id, result+["-1"])
         			attempt = fb.get("Lab1/"+self.id, None)
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
		self.maxpoint = 3.2
		self.btn5.setEnabled(False)
		self.text2.setText("#!/bin/bash\n")
		if self.i==1:
			self.text2.append("echo ...")
		if self.i==2:
			self.text2.append("echo ...")
		elif self.i==3:
			self.text2.append("more /etc/passwd")
		elif self.i==4:
			self.text2.append("file=\"myfile1\"\n\nwho>")
		elif self.i==5:
			self.text2.append("file=\"myfile1\"\n\nmore")
		elif self.i==6:
			self.text2.append("file=\"myfile2\"\n\ndate && who>")
		elif self.i==7:
			self.text2.append("file=\"myfile2\"\n\nmore")
		elif self.i==8:
			self.text2.append("file=\"myfile3\"\n\nsed <expr> <file>")
		elif self.i==9:
			self.text2.append("file=\"myfile3\"\n\nsed <expr> <file>")
		elif self.i==10:
			self.text2.append("file=\"myfile3\"\n\nsed <expr> <file>")
		elif self.i==11:
			self.text2.append("cat /etc/passwd | awk -F :")
		elif self.i==12:
			self.text2.append("grep -c \"$1\"  $2")
			self.text9.setText("are temp\myfile3")
	
	def sendscore(self):
		try:
			result = fb.put("Lab1/"+self.id,str(self.att_value),self.score)
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
