a=input(f"Input your file location :-"   )
b=input(f"Input your file location :-"   )

f1 = ''
f2 =''
d = "as"
try :
    f1=  open(a,mode='r') 
   
    f2 = open(b,mode='w') 
except FileNotFoundError as d :
        print(f"check your location dude  \n{d} ")
else:
   content = f1.read()
   for data in content:
    f2.write(data)
