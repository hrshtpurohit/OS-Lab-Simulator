#!/usr/bin/env python

#!/usr/bin/python
# -*- coding: utf-8 -*-

from firebase import firebase

import sys
import random
import subprocess
import os

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
		box1.setText("Welcome!\nIT204 Operating Systems Lab\nLab 2: System Calls for File Management\nIIIT-Vadodara\n(Gandhinagar Campus)\nWinter 2017\n\nDeveloped by: Vague Hacker")
		box1.setStyleSheet('qproperty-alignment: AlignCenter;background-color: white')
		box1.setStandardButtons(QMessageBox.Ok)
		box1.exec_()
		
		self.id = 0
		self.takeId()
        
		font = QFont()
		font.setPointSize(12)
		self.setFont(font)
        
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle('Operating Systems Lab 2')
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
		
		if self.i==0:
			self.assignment1()
			
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
		if self.i==1 or self.i==9:
			self.btn1.setEnabled(False)
			self.btn2.setEnabled(True)
		else:
			self.btn1.setEnabled(True)
			self.btn6.setEnabled(True)
		self.btn5.setEnabled(True)
			
		self.text3.setText("")
		self.text9.setText("")
		
		if self.i==1:
			self.text1.setText("Bonus - Test the given code for opening files")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\tint fd;\n\tfd = open(argv[1], O_RDONLY);\n\tif (fd==-1) {\n\tprintf(\"Couldn't open the file!\");\n\t}\n\telse {\n\tprintf(\"File opened successfully!\");\n\t}\n}")	
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')	
		elif self.i==2:
			self.text1.setText("Level 1 - Using system calls, implement the 'cat' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==3:
			self.text1.setText("Level 2 - Using system calls, implement the 'ls' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==4:
			self.text1.setText("Level 3 - Using system calls, implement the 'cp' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<original file> <new file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==5:
			self.text1.setText("Level 4 - Using system calls, implement the 'mv' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<original file> <new file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==6:
			self.text1.setText("Level 5 - Using system calls, implement the 'pwd' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==7:
			self.text1.setText("Level 6 - Determine the size of a file using the lseek command")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==8:
			self.text1.setText("Level 7 - Calculate the number of blocks assigned for the file using \"stat\" function in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\tstruct stat st;\n\tstat(argv[1], &st);\n\tlong size = st.st_size;\n\tprintf(\"%ld\", size);\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==9:
			self.text1.setText("Level 8 - Write a C program that deletes a directory with all its subfolders")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<directory>")
			self.text9.setStyleSheet('background-color:white;')
	
	def assignment1(self):
		if self.i==self.max:
			self.max=self.max+1
			if self.i!=1 and self.flag==0:
				self.score = self.score + self.maxpoint
		self.i=self.i+1
		self.flag=0
		
		self.text6.setText("SCORE : "+str(self.score)+"/100")
		self.text6.setAlignment(Qt.AlignCenter)
		
		if self.i==10:
			self.end_time = datetime.now()
            		diff = self.end_time - self.start_time
            		minu = str(int(diff.seconds/60))
            		seco = str(diff.seconds%60)
			
			self.text6.setText("SCORE : "+str(self.score)+"/100")
			self.text6.setAlignment(Qt.AlignCenter)
			
			box2 = QMessageBox()
			box2.setWindowTitle("Congratulations")
			box2.setText("You won!\n\nYour score - "+str(self.score)+"/100\n\nTime taken - "+minu+" minutes and "+seco+" seconds")
			box2.setStyleSheet('qproperty-alignment: AlignCenter;')
			box2.setStandardButtons(QMessageBox.No)
			buttonX = box2.button(QMessageBox.No)
        		buttonX.setText('Submit and Quit')
			buttonX.clicked.connect(lambda: self.sendscore())
			box2.exec_()
			if box2.clickedButton() == buttonX:
            			QApplication.quit()
		
		self.maxpoint = 10
		if self.i==7 or self.i==8:
			self.maxpoint = 15
		
		if self.i==9:
			self.maxpoint = 20
	
		if self.i==1:
			self.btn3.setEnabled(False)
		else:
			self.btn3.setEnabled(True)
		if self.i==self.max:
			self.btn2.setEnabled(False)
		else:
			self.btn2.setEnabled(True)
		if self.i==1:
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
			self.text1.setText("Bonus - Test the given code for opening files")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\tint fd;\n\tfd = open(argv[1], O_RDONLY);\n\tif (fd==-1) {\n\tprintf(\"Couldn't open the file!\");\n\t}\n\telse {\n\tprintf(\"File opened successfully!\");\n\t}\n}")	
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')	
		elif self.i==2:
			self.text1.setText("Level 1 - Using system calls, implement the 'cat' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==3:
			self.text1.setText("Level 2 - Using system calls, implement the 'ls' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==4:
			self.text1.setText("Level 3 - Using system calls, implement the 'cp' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<original file> <new file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==5:
			self.text1.setText("Level 4 - Using system calls, implement the 'mv' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<original file> <new file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==6:
			self.text1.setText("Level 5 - Using system calls, implement the 'pwd' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==7:
			self.text1.setText("Level 6 - Determine the size of a file using the lseek command")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==8:
			self.text1.setText("Level 7 - Calculate the number of blocks assigned for the file using \"stat\" function in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\tstruct stat st;\n\tstat(argv[1], &st);\n\tlong size = st.st_size;\n\tprintf(\"%ld\", size);\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==9:
			self.text1.setText("Level 8 - Write a C program that deletes a directory with all its subfolders")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<directory>")
			self.text9.setStyleSheet('background-color:white;')
			
		if self.i==1:
			box = QMessageBox()
			box.setWindowTitle("Instructions")
			box.setText("1. This lab consists of 8 assessment questions and 1 bonus questions.\n\n2. Questions 1 to 5 carry 10 marks each, questions 6 and 7 carry 15 marks each, while question 8 carries 20 marks.\n\n3. Maximum Score - 100\n\n4. No score for bonus questions - The bonus questions are for learning purpose.\n\n5. If you get stuck on a question, use hint.\n\n6. After using hint in a question, only 80% of the score in that question can be earned.\n\n7. Your score for any question will be rewarded after you reach the next level\n\n8. You can test your solution using the test button. Score won't be deducted for testing.\n\n9. No score for skipped questions.\n\n10. Once you skip a question you cannot come back to solve it later. However, you can come back to view the previous questions and test them.\n\n11. The Application works offline, however, internet connection is required while submission of score at the end.\n\n12. For file handling, the current working directory is Lab2\n\n13. Use command line arguments for input. Standard input function 'scanf' won't work.\n\n14. Use of system() function is prohibited.\n\n-> All the Best!")
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_() 
			
	def check(self):
	
		win=0
		
		temp = self.text2.toPlainText()
		x = str(temp)
		if x.find("system(")!=-1:
			box = QMessageBox()
			box.setIcon(QMessageBox.Critical)
			box.setWindowTitle("Warning")
			box.setText("Use of system() function is prohibited!")
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_()
		
		file1 = open('.data.c','w')
		file1.write(temp)
		file1.close()
				
		if self.i==2:
			try:
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"]+["temp/myfile2"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
				ctext = subprocess.check_output(["cat",".temp/myfile2"])
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if ctext==show:
				win=1
		elif self.i==3:
			try:
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				ctext = subprocess.check_output(["ls"])
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
				x = []
				y = []
				x = ctext.splitlines()
				y = show.splitlines()
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if set(x)==set(y):
				win=1
		elif self.i==4:
			try:
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"]+[".temp/myfile2",".temp/myfile5"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
				x = subprocess.check_output(["cat",".temp/myfile2"])
				y = subprocess.check_output(["cat",".temp/myfile5"])
				if x==y:
					win=1
					os.remove(".temp/myfile5")
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
		elif self.i==5:
			try:
				f = open(".temp/myfile3", "r")
				x = f.read()
				f.close()
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"]+[".temp/myfile3",".temp/tempfile"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
				f = open(".temp/tempfile", "r")
				y = f.read()
				f.close()
				if x==y and not os.path.isfile(".temp/myfile3"):
					win = 1
					subprocess.call(["cp", ".temp/myfile4", ".temp/myfile3"])
					os.remove(".temp/tempfile")
					
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
		elif self.i==6:
			try:
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
				ctext = subprocess.check_output(["pwd"])
				if show==ctext:
					win=1
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
		elif self.i==7:
			try:
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"]+[".temp/myfile2"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
				ctext = subprocess.check_output(["stat", "--printf=%s",".temp/myfile2"])
				if show==ctext:
					win=1
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
		elif self.i==8:
			try:
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"]+[".temp/myfile2"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
				ctext = subprocess.check_output(["stat", "--printf=%b",".temp/myfile2"])
				if show==ctext:
					win=1
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
		elif self.i==9:
			try:
				text = str(self.text9.toPlainText())
				self.inlist = text.split()
				subprocess.call(["gcc", "-o", ".data", ".data.c"])
				output = subprocess.Popen(["./.data"]+[".temp/mydir1"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				show = output.stdout.read()
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if not os.path.exists(".temp/mydir1"):
				win=1
				os.mkdir(".temp/mydir1")
				f=open(".temp/mydir1/myfile6", "w+")
			
                										
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
         			result = fb.get("Lab2/"+self.id, None)
         			if result==None:
         				result = fb.put("Lab2", self.id, ["-1"])
         			else:
         				result = fb.put("Lab2", self.id, result+["-1"])
         			attempt = fb.get("Lab2/"+self.id, None)
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
		x = str(temp)
		if x.find("system(")!=-1:
			box = QMessageBox()
			box.setIcon(QMessageBox.Critical)
			box.setWindowTitle("Warning")
			box.setText("Use of system() function is prohibited!")
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_()
		
		file1 = open('data.c','w')
		file1.write(temp)
		file1.close()
		
		try:
			text = str(self.text9.toPlainText())
			self.inlist = text.split()
			subprocess.call(["gcc", "-o", "data", "data.c"])
			output = subprocess.Popen(["./data"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			show = output.stdout.read()
			self.text3.setText(show)
		except Exception:
			box1 = QMessageBox()
			box1.setIcon(QMessageBox.Critical)
			box1.setWindowTitle("Warning")
			box1.setText("Syntax Error!")
			box1.setStandardButtons(QMessageBox.Ok)
			box1.exec_()
					
			
	def hint(self):
		self.maxpoint = 8
		if self.i==7 or self.i==8:
			self.maxpoint = 12
		
		if self.i==9:
			self.maxpoint = 16

		self.btn5.setEnabled(False)
		self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\n#include <dirent.h>\n#include <sys/wait.h>\n#include <grp.h>\n#include <pwd.h>\n#include <time.h>\nint main( int argc,char *argv[] )\n{")
		if self.i==1:
			self.text2.append("\tint fd;\n\tfd = open(argv[1], O_RDONLY);\n\tif (fd==-1) {\n\tprintf(\"Couldn't open the file!\");\n\t}\n\telse {\n\tprintf(\"File opened successfully!\");\n\t}\n}");
		elif self.i==2:
			self.text2.append("\tint fd;\n\tfd = open(/*Arguments*/);\n\t/*Read from file*/\n\tclose(fd);\n\treturn 0;\n}")
		elif self.i==3:
			self.text2.append("\tint count;\n\tif (getwd(pathname) == NULL )\n\t\texit(0);\n\tcount = scandir(/*Arguments*/);\n\t/*Print filenames in the directory using count*/\n\treturn 0;\n}")
		elif self.i==4:
			self.text2.append("\tint fd1,fd2;\n\tfd1=open(/*Arguments*/);\n\tfd2=creat(/*Arguments*/);\n\t/*Read from file 1 and write to file 2*/\n\tclose(fd1);\n\tclose(fd2);\n\treturn 0;\n}")
		elif self.i==5:
			self.text2.append("\tint fd1,fd2;\n\tfd1=open(/*Arguments*/);\n\tfd2=creat(/*Arguments*/);\n\t/*Read from file1, write to file2 and remove file1*/\n\tclose(fd1);\n\tclose(fd2);\n\treturn 0;\n}")
		elif self.i==6:
			self.text2.append("\tgetcwd(/*Arguments*/);\n\t/*Print current working directory*/\n\treturn 0;\n}")
		elif self.i==7:
			self.text2.append("\tlong size;\n\tint fp;\n\tfp = open(/*Arguments*/);\n\tsize = lseek(/*Arguments*/);\n\t/*Print size*/\n\tclose(fp);\n\treturn 0;\n}")
		elif self.i==8:
			self.text2.append("\tstruct stat st;\n\tstat(/*arguments*/);\n\tlong size = //...\n\tprintf(\"%ld\", size);\n\treturn 0;\n}")
		elif self.i==9:
			self.text2.append("\tchar dir[100];\n\tchar *di;\n\tdi = argv[1];\n\tint val = remove_directory(di);\n\treturn 0;\n}\n\nint remove_directory(const char *path)\n{\n\t//Complete the function\n}")
	def sendscore(self):
		try:
			result = fb.put("Lab2/"+self.id,str(self.att_value),self.score)
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
