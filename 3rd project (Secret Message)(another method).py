class Coding:
   def alptonum(self,str1):
       for i in str1:
           if i==" ":
               continue
           elif ord(i)>=97 and ord(i)<=122:     #code for small letters
               str1=str1.replace(i,str((((ord(i)-48)*4)-152)//2))
           elif ord(i)>=65 and ord(i)<=90:    #code for capital letters
               str1=str1.replace(i,str(((((ord(i)-39)*2)+4)//2)+46))
           #raise Exception("input type error") or raise Exception  also correct...
       print(str1)

#-------------------------------

class Decoding:
    def numtoalp(self,str2):      #6430305622 24222462
        i=0
        str3=''
        while i<len(str2):
            spclchrlist=['|',';',':',' ','"',"'",'<','>',',','.','?','/','~','!','#','$','%','^','&','*','(',')','_','+','`','-','=','{','[','}',']']
            if str2[i] in spclchrlist:
               str3+=str2[i]
               i+=1
               continue
            a=int(str2[i:i+2])
            if a>=22 and a<=72:
                str3+=chr((((a*2+152)//4)+48))      #'/' for float division and '//' for integer division
            elif a>=74 and a<=99:
                str3+=chr(((((a-46)*2)-4)//2)+39)
            i=i+2
        print(str3)


#----------------------------------
            
def main():
    ob1=Coding()                                        #indentation error occur in python but not in c++,java,c
    ob2=Decoding()
    try:
     print("\n1.CODING\n2.DECODING")
     choice=int(input("Enter Your Choice:"))    #default takes new line
     if choice==1:
          str1=input("Enter input word/sentence/para")
          ob1.alptonum(str1)
     elif choice==2:
          str2=input("Enter decoded message in numbers:")
          ob2.numtoalp(str2)

          
    except:
      print("\nsomething went wrong\n----------TRY AGAIN------")     #possibleerrors 1.choice=string/2.invalid input.
      main()

      
    else:
      print("-----Your process completed successfully--------")
      if int(input("press 1 to continue or 0 to exit")):
          main()
      else:
          print("------Thank You-----")
          exit()
      
          
  
main()

##NOTE:On debugging always go from the basics checks.....
#1.checking variable names throughout the program
#2.Logic Checking
#3.give try except block to last while coding
