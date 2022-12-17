import pyttsx3
os = pyttsx3.init();
os.say("your device has been hacked ");

os.say("types of varible in python ")
os.say("this is string type ");
os.runAndWait();
# define the first varible
a = "amit kuamr ";
print(a);
print(type(a));
# define the second variable 
os.say("this is integer type ");
b = 12324;
print(b);
print(type(b));
os.runAndWait();
# define the third varible 
os.say("this is floating point number ");
c = 25473524.632543;
print(c);
print(type(c));
os.runAndWait();
#define the fourth type 
os.say("define the boolian type ");
d = True;  # boolan =true / false 
print (d );
print(type(d));
os.runAndWait();
# define the fifth variable
os.say("define the none type ")
e = None;
print(e)
print(type(e));
os.runAndWait();
from playsound import playsound
playsound('C:\\Users\\HP\\Downloads\\Ek Din Mar Jayega kutte Ki Maut.mp3');
