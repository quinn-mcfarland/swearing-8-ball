#Import all the modules we need before the main module.
import random

#identify name and question here as well as set the random number generator.
name = 'AJ'
question = 'Will I be a millionaire?'
answervar = random.randint(1,20) #This is the random number generator. It should be generating numbers between 1 and 9
#print(str(answervar)) #Use this to test the randint variable. If all is well, comment out this line.

#This is where we define the answers to the above question.
if answervar == 1:
    answer = "It's lookin' real damn certain"
elif answervar == 2:
    answer = "Abso-fucking-lutely"
elif answervar == 3:
    answer = "without a goddamn doubt"
elif answervar == 4:
    answer = "Hell yeah!"
elif answervar == 5:
    answer = "You can fucking count on it"
elif answervar == 6:
    answer = "As I fucking see it, yeah!"
elif answervar == 7:
    answer = "Well it fucking better be"
elif answervar == 8:
    answer = "Outlook? Real goddamn good"
elif answervar == 9:
    answer = "All the fuckin way"
elif answervar == 10:
    answer = "The stars look real fucking confident"
elif answervar == 11:
    answer = "Yeah that's really goddamn unclear, try that shit again"
elif answervar == 12:
    answer = "Ask me that bullshit later"
elif answervar == 13:
    answer = "Yeah I'm not gonna tell you right now you'll probably fucking kill me"
elif answervar == 14:
    answer = "I'm too drunk to predict this shit right now"
elif answervar == 15:
    answer = "Fucking focus and try that shit again"
elif answervar == 16:
    answer = "Don't fucking count on it"
elif answervar == 17:
    answer = "My reply is a big fat FUCK NO"
elif answervar == 18:
    answer = "Hell nah. My sources? Oh, you mean the ones I made the fuck up."
elif answervar == 19:
    answer = "Outlook? Not fucking great, I'll tell you that much"
elif answervar == 20:
    answer = "I'm really fuckin doubtful right about now"
else:
    answer = "Aw shit. Something broke. The magic is fucking ruined. Thanks a lot, Jared."

#This is where we spit the output code. Also define if there is a name and a question.
if name == "" and question != "":
    print("Question: " + str(question))
    print("The Magic 8-ball says " + str(answer))
elif question == "":
    print("Ask a question, fucktard.")
elif name != "" and question != "": 
    print(str(name) + " asks " + str(question))
    print("The Magic 8-ball says " + str(answer))