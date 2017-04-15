#!/usr/bin/env python

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import subprocess
import os

from datetime import datetime
random.seed()

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Example(QWidget):
	
	def closeEvent(self,event):
    		result = QMessageBox.question(self, "Confirm Exit...", "Are you sure you want to exit ?", QMessageBox.Yes| QMessageBox.No)
    		event.ignore()
    
    		if result == QMessageBox.Yes:
     			event.accept()
    
   	def __init__(self):
		super(Example, self).__init__()     
		self.initUI()
        
        
	def initUI(self):
		self.setWindowIcon(QIcon('icon.png'))
	
		box1 = QMessageBox()
		box1.setWindowTitle("Operating System Lab")
		box1.setIconPixmap(QPixmap("cl.png"))
		box1.setText("Welcome!\nIT204 Operating Systems Lab\nLab 3: Operation on Process\nIIIT-Vadodara (Gandhinagar Campus)\nWinter 2017\n\nDeveloped by:____")
		box1.setStyleSheet('qproperty-alignment: AlignCenter;')
		box1.setStandardButtons(QMessageBox.Ok)
		box1.exec_()
		
		self.id = 0
		while len(str(self.id))!=9:
			self.takeId()
        
		font = QFont()
		font.setPointSize(12)
		self.setFont(font)
        
		self.setGeometry(300, 300, 300, 300)
		self.setWindowTitle('Operating Systems Lab 3')
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
		if self.i==2 or self.i==3:
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
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <errno.h>\nint main( int argc,char *argv[1] )\n{\n\tint fd;\n\tfd = open(argv[1], O_RDONLY);\n\tprintf(\"%d\", fd);\n\tif (fd==-1) {\n\tfprintf (stderr,\"Error Number %d\", errno);\n\tperror(\"Program\");\n\t}\n}")	
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')	
		elif self.i==2:
			self.text1.setText("Level 1 - Using system calls, implement the 'cat' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==3:
			self.text1.setText("Level 2 - Using system calls, implement the 'ls' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==4:
			self.text1.setText("Level 3 - Using system calls, implement the 'cp' command in C (rename a file)")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<original file> <new file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==5:
			self.text1.setText("Level 4 - Using system calls, implement the 'mv' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<original file> <new file>")
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==6:
			self.text1.setText("Level 5 - Using system calls, implement the 'pwd' command in C")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==7:
			self.text1.setText("Level 6 - Determine the size of a file using the lseek command")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==8:
			self.text1.setText("Level 7 - Calculate the number of blocks assigned for the file")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==9:
			self.text1.setText("Bonus - Compare previous results with the similar results obtained when using the function stat")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\nint main( int argc,char *argv[1] )\n{\n\tstruct stat st;\n\tstat(argv[1], &st);\n\tlong size = st.st_size;\n\tprintf(\"%ld\", size);\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<file>")		
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==10:
			self.text1.setText("Level 8 - Write a C program that deletes a directory with all its subfolders")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<directory>")
			self.text9.setStyleSheet('background-color:white;')
		elif self.i==11:
			self.text1.setText("Level 9 - Write a C program that finds a file in a file-tree starting from a given directory")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\nint main( int argc,char *argv[1] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(True)
			self.text9.setText("<directory> <file>")
			self.text9.setStyleSheet('background-color:white;')
	
	def assignment1(self):
		if self.i==self.max:
			self.max=self.max+1
			if self.i!=2 and self.i!=3 and self.flag==0:
				self.score = self.score + self.maxpoint
		self.i=self.i+1
		self.flag=0
		
		self.text6.setText("SCORE : "+str(self.score)+"/100")
		self.text6.setAlignment(Qt.AlignCenter)
		
		if self.i==12:
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
        		buttonX.setText('Quit')
			box2.exec_()
			if box2.clickedButton() == buttonX:
            			QApplication.quit()
		
		self.maxpoint = 10
		if self.i==10 or self.i==11:
			self.maxpoint = 15
	
		if self.i==1:
			self.btn3.setEnabled(False)
		else:
			self.btn3.setEnabled(True)
		if self.i==self.max:
			self.btn2.setEnabled(False)
		else:
			self.btn2.setEnabled(True)
		if self.i==2 or self.i==3:
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
			self.text1.setText("Level 1 - Write a program in C that creates a child process, waits for the termination of the child and lists its PID, together with the state in which the process was terminated (in decimal and hexadecimal)")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")	
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')	
		elif self.i==2:
			self.text1.setText("Bonus - Test the codes for creation of orphan process")
			self.text2.setText("#include<stdio.h>\n#include <sys/types.h>\n#include <unistd.h>\n\nint main(){\n\t// Create a child process\n\tint i = fork();\n\n\tif (i > 0)\n\t\tprintf(\"in parent process :  pid = %d \t parent id = %d \n\",getpid(),getppid());\n\n\t// Note that pid is 0 in child process\n\t// and negative if fork() fails\n\telse if (i == 0) {\n\n\tsleep(30);\n\n\tprintf(\"in child process :  pid = %d \t parent id = %d\n\",getpid(),getppid());\n\n\t}\n\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==3:
			self.text1.setText("Bonus - Test the codes for creation of zombie process")
			self.text2.setText("#include <sys/wait.h>\n#include<stdio.h>\n\nvoid ChildProc(void)\n{\n\tint i;\n\tfor(i = 0; i < 100; i++) {\n\tprintf(\"Child : %d from process <%d> : Parent <%d>\n\",i, getpid(), getppid());\n\t}\n}\n\nvoid ParentProc(void)\n{\n\tint i;\n\tfor(i = 0; i < 20; i++) {\n\tprintf(\"Parent : %d from process <%d> : Parent <%d>\n\",i, getpid(), getppid());\n\t}\n}\n\nint main(void)\n{\n\tpid_t child;\n\tchild = fork();\n\n\tif(child == 0) {\n\tChildProc();\n\t}\n\telse {\n\tParentProc();\n\t//waitpid(child,NULL,0);\n\t}\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==4:
			self.text1.setText("Level 2 - ")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==5:
			self.text1.setText("Level 3 - ")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
		elif self.i==6:
			self.text1.setText("Level 4 - Modify the code below, such that after all created processes have finished execution, output the total number of created processes")
			self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\nint main( int argc,char *argv[] )\n{\n\t//edit your code here\n\treturn 0;\n}")
			self.text9.setEnabled(False)
			self.text9.setStyleSheet('background-color:silver;')
			
		if self.i==1:
			box = QMessageBox()
			box.setWindowTitle("Instructions")
			box.setText("-> This lab consists of 10 questions\n\n-> Every question carries 4 marks\n\n-> Use of hint will cost you 20% of the marks in that question\n\n-> No score for skipped questions\n\n-> Once you skip a question you cannot come back\n\n-> All the Best!")
			box.setStandardButtons(QMessageBox.Ok)
			box.exec_()
			
	def check(self):
	
		win=0
		self.inlist = []
		
		temp = self.text2.toPlainText()
		
		file1 = open('data.c','w')
		file1.write(temp)
		file1.close()
		
		try:
			text = str(self.text9.toPlainText())
			self.inlist = text.split()
			subprocess.call(["gcc", "-o", "data", "data.c"])
			output = subprocess.Popen(["./data"]+self.inlist, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			show = output.stdout.read()
			self.text3.setText(show)
		except Exception:
			box1 = QMessageBox()
			box1.setIcon(QMessageBox.Critical)
			box1.setWindowTitle("Warning")
			box1.setText("Syntax Error!")
			box1.setStandardButtons(QMessageBox.Ok)
			box1.exec_()
				
		if self.i==1:
			try:
				ctext = subprocess.check_output(["cat"]+self.inlist)
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			if ctext==show and len(show)!=0 and len(self.inlist)!=0:
				win=1
			win=1
		elif self.i==4:
			try:
				ctext = subprocess.check_output(["ls"])
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
			if set(x)==set(y) and len(show)!=0:
				win=1
			win=1
		elif self.i==5:
			try:
				x = subprocess.check_output(["cat"]+[self.inlist[0]])
				y = subprocess.check_output(["cat"]+[self.inlist[1]])
				if x==y:
					win=1
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
			win=1
		elif self.i==6:
			try:
				self.inlist.reverse()
				ctext = subprocess.check_output(["mv"]+self.inlist)
				if len(self.inlist)!=0:
					win=1
			except Exception:
				box1 = QMessageBox()
				box1.setIcon(QMessageBox.Critical)
				box1.setWindowTitle("Warning")
				box1.setText("Syntax Error!")
				box1.setStandardButtons(QMessageBox.Ok)
				box1.exec_()
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
			output = subprocess.Popen(["./data"]+self.inlist, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
		if self.i==10 or self.i==11:
			self.maxpoint = 12
		self.btn5.setEnabled(False)
		self.text2.setText("#include<sys/types.h>\n#include<sys/stat.h>\n#include <sys/dir.h>\n#include <sys/param.h>\n#include<stdio.h>\n#include<fcntl.h>\n#include <linux/fs.h>\nint main( int argc,char *argv[] )\n{")
		if self.i==2:
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
			self.text2.append("\n\treturn 0;\n}")
		elif self.i==10:
			self.text2.append("\n\treturn 0;\n}")
		elif self.i==11:
			self.text2.append("\n\treturn 0;\n}")
		
def main():
    
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
