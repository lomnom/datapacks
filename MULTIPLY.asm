//RAM[2]=RAM[0]*RAM[1]
//RAM=[12,2,0,0]
//while True:
//	if RAM[1]==RAM[3]: #chsck if done
//		RAM[3]=0
//		print(RAM)
//		quit()
//	RAM[3]=RAM[3]+1 #inc multiplycounter
//	RAM[2]=RAM[2]+RAM[0] #add again

@0 //check which val is bigger
D=M

@1
D=M-D

@Start1 //jump to loop that iterates RAM[1] times if ram[1] is smaller
D;JLT

(Start0)
@0 //check if done, go to end if done
D=M
@3
D=D-M
@End
D;JEQ

@3
M=M+1 //inc multiplycounter

@1 //add again
D=M
@2
M=M+D 

@Start0 //go back to start of loop
0;JMP

(Start1)
@1 //check if done, go to end if done
D=M
@3
D=D-M
@End
D;JEQ

@3
M=M+1 //inc multiplycounter

@0 //add again
D=M
@2
M=M+D 

@Start1 //go back to start of loop
0;JMP

(End) //end in infinite loop of clearing counter
@3
M=0

@End
0;JMP