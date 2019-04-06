# Author: Bohan Gao (25611161)
# Instead of using stanford npl tool kit, I use spacy.
# This tool pack is famous for its high efficiency 
# and it is trusted by many great companies, like micosoft and airbnb.
# I believe this assignment can be a great opportunity for me to use this  
# tool kit to creat something interesting. So please allow me to do so. :)   

import random
import spacy
nlp = spacy.load("en")

#initialize our chat sentences
#topics included:(2 points)
#1. Personal life & hobbies
#2. Family members

data={
'major':['CS'],
'birthday':['october 10th 2000'],
'food':['pudding','cake','spaghetti','Kung pao chicken'],
'drink':['blood','7 up','Pepsi','orange juice'],
'sport':['soccer','badminton','basketball','archery'],
'color':['red','black','green','yellow'],
'weather':['sunny','snowy','rainy'],
'breakfast':['burger','cereal','corn','bread'],
'homework':['I haven''t finished it yet','uhhh, let''s change a topic'],
'sleep':['at 12:00 pm','at 3:00 am','I have sleep disorder yesterday...'],
'gym':['last month','yesterday','a week ago, I guess....'],
'coffee':['yesterday'],
'class':['no, I am a good student','uhh, maybe.','I refuse to answer this question.'],
'semester':['4 months'],
#'finish homework':['about 10 hours','about 2 hours'],
'father':['His name is ChatbotA'],
'mother':['Her name is Sara'],
'cousin':['Her name is Sam'],
'sister':['Her name is Amy'],
#'math teacher':['steve'],
#'art teacher':['Ronny'],
#'drama teacher':['Abie'],
#'CS teacher':['Aron'],
#'social teacher':['Aaron'],
#'history teacher':['summer'],
'friend':['I do not have friend except you','her name is annie'],
'hometown':['kelowna','Mars'],
'summer':['vancouver','ontario'],
'game':['LOL'],
'car':['Audi'],
#5 different reasonable responses when the user enters something outside the two topics: (3 points)
'DNE':['Sorry, I cannot understand the question.', "I don't understand QAQ.", "Please ask something that I can understand.", "Sorry, what do you mean?", "Can you ask a different question?"]

}
# testing the POS tag performance on every data key
dataKey=list(data.keys())
# str = ""
# for word in dataKey:
#    str+= word+" "

# temp = nlp(str)
# for word1 in temp:
#    print (word1, word1.tag_)

# Conversion starts here:

    #Say hi to each other:
answer=input("Hi! I am chatBot! (Say hi to me!).\n")
while "hi" not in answer.lower():
    print("Please say hi to me :).")
    answer=input("Hi! I am chatBot!\n")

    #Ask user's name and then greet the user.
        #(10 points) Here I use the name entity recognition to extract a person's name from a sentence      
name=input("What's your name? :)\n")
doc = nlp(name)
for token in doc.ents:
    print("Named entity recognition to extract a person's name:")
    print(token.text, token.label_)
    if(token.label_ == "PERSON"):
        name = token.text
        break
    else:
        name = name.split()[-1]

#print("Nice to meet you "+name+"\n")
    #Start asking questions:
print("Ask me some questions "+name+" :)\n")
print("If you do not know what to ask, type 'help'")
print("Here is a sample question: What is your major")
print("What question do you want to ask me?")

    #Make sure the chatbot keeps talking until the user says bye.
isContinue = True
while isContinue:
    question = input("\n")
    document = nlp(question)
    POStag = []
    for word in document:
        POStag.append([word, word.tag_])
    
    print("POS tag ananlysis:")
    print(POStag)

    # locating the key word using POStag analysis: (10 points)
    keyWord = ""

    for temp in POStag:
        if str(temp[0]).lower() == "major" or temp[1] == 'NN' or str(temp[0]).lower() == "help" or str(temp[0]).lower() == "hi" or str(temp[0]).lower() == "bye":
            keyWord = str(temp[0]).lower()
            break

    
    #For testing purpose
    #print(keyWord)

    if keyWord == "help":
        print(data.keys())
        print("\n")
        continue

    if keyWord == "hi":
        print("Hi!",name)
        continue
    
    if keyWord == "bye":
        print("Bye, ",name,"\nIt was nice to talk to you")
        isContinue =False
        continue

    if keyWord in dataKey:
        temp = random.randint(0,len(data[keyWord])-1)
        if len((data[keyWord])[temp].split()) >1:
            print((data[keyWord])[temp])
            
        else:
            print("My",keyWord,"is",(data[keyWord])[temp],".")
            

    else: 
        print((data["DNE"])[random.randint(0,len(data["DNE"])-1)])
        

