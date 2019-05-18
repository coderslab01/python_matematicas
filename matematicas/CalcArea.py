import msvcrt 
from turtle import *

shape('turtle');
speed(0);
color('red');
def cuad():
	for i in range(4):
		forward(100);
		right(90);
		

def square():
	for i in range(60):
		
		right(5);
		
		cuad();
		

square();

msvcrt.getch();
