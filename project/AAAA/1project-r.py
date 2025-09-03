email=input("Enter Your Email")
k=0
j=0
d=0
if(len(email)>=6):
  if(email[0].isalpha()):
    if(('@' in email) and (email.count("@")==1)):
      if((email[-4]=='.')^(email[-3]=='.')):
        for i in email:
          if(i==i.isspace()):
            k=1
          elif(i.isalpha()):
            if(i==i.upper()):
              j=1
          elif(i.isdigit()):
            continue
          elif(i=="_"or i=="."or i=='@'):
            continue
          else:
            d=1
        if(k==1,j==1,d==1):
            print('email wrong 5')
      else:
        print('email wrong 4')
    else:
      print('email wrong 3')
  else:
    print('email wrong 2')
else:
  print("email worong 1")