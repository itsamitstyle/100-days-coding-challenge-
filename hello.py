# making a voice recognation traffic system  using python
#free time day=0
import pyttsx3 #import pyttsx3 module 
engine = pyttsx3.init();
engine.say("welcome to traffic signal machine ");
engine.runAndWait();
engine.say("enter your age sir ");
engine.runAndWait();
age = input ("enter your age ");

if(age <"18" ):
    
    engine.say("you can not drive it sir ");
    engine.runAndWait();
elif(age >"18"):
    engine.say("yes you can drive it sir ");
    engine.runAndWait();
elif(age == "18"):
    engine.say("you are just 18 year old sir so please you can drive it ");
    engine.runAndWait();





