Bohan Gao(25611161)'s COSC 310 project
README

DESCRIPTION:// This a chatbot project that is built upon and implemented in python(includes the spaCy api) that allows users to have a conversation by prompting questions and answering them through a response dataset made a head of time.

HOW TO COMPILE & RUN:// Make sure python and the spaCy NLP API is installed in the computer. Click run button to compile and run the code. To run the code, you have to say hi and your name to program. After this, you can just ask questions to program depend on keys which has been implemented in program. 

Here is the link for the spaCy NLP API: https://spacy.io/

CLASS:// chatBot: This class stores a dataset for response, prompt questions and give responses, check the users' inputs validity, provide help when necessary.

     
LIST OF FEATURES:
1. HELP:// type 'help'± if you need help. This is to provide help to the user when he/she does not know what to ask.

#Example:
#If you do not know what to ask, type 'help'
#Here is a sample question: What is your major
#What question do you want to ask me?

#help
#POS tag ananlysis:
#[[help, 'VB']]
#dict_keys(['major', 'birthday', 'food', 'drink', 'sport', 'color', 'weather', 'breakfast', 'homework', 'sleep', 'gym', #'coffee', 'class', 'semester', 'father', 'mother', 'cousin', 'sister', 'friend', 'hometown', 'summer', 'game', 'car', #'DNE'])

2. GREETINGS:// Say "Hi" to the chatbot, the chatbot will say hi+your name back. This make the chatbot sounds more like a human-being

#Example:
#Hi
#POS tag ananlysis:
#[[Hi, 'UH']]
#Hi! Ben

3. TERMINATING CONVERSATION :// Say bye to the chatbot, the chatbot will say "bye" and "It was nice to talk to you" back to you. Then the program is terminated. We have to allow the user to terminate the conversation we he/she wants to.

#Example:
#bye
#POS tag ananlysis:
#[[bye, 'UH']]
#Bye,  Ben 
#It was nice to talk to you
#Terminated: 15

4. TOPICS ALLOWED:// This chatbot can answer questions under two topics: personal life and hobbies and family members (2 marks). This stores everything the chatbot knows and potential conversation topics.

#Example:
#dict_keys(['major', 'birthday', 'food', 'drink', 'sport', 'color', 'weather', 'breakfast', 'homework', 'sleep', 'gym', #'coffee', 'class', 'semester', 'father', 'mother', 'cousin', 'sister', 'friend', 'hometown', 'summer', 'game', 'car', #'DNE'])

5. ANSWERING QUESTION:// When the user ask the chatbot a question, the chatbot will search and extract the keyword based on the POStag analysis(10 marks). If the resulting keyword is in the answer base, the chatbot will give the answer. If the resulting keyword is not in the answer base, the chat bot will give 5 different reasonable responses(3 marks). This allows the chatbot to understands what the user is asking and gives a variety to the response when the chatbot does not know the answer of the question.

#Example: 
#What is your major?
#POS tag ananlysis:
#[[What, 'WP'], [is, 'VBZ'], [your, 'PRP$'], [major, 'JJ'], [?, '.']]
#My major is CS .

#Who is your mother?
#POS tag ananlysis:
#[[Who, 'WP'], [is, 'VBZ'], [your, 'PRP$'], [mother, 'NN'], [?, '.']]
#Her name is Sara

#Who is your father?
#POS tag ananlysis:
#[[Who, 'WP'], [is, 'VBZ'], [your, 'PRP$'], [father, 'NN'], [?, '.']]
#His name is ChatbotA


6. NAME EXTRACTION:// When the conversion starts, the chatbot will ask and remember what the user's name is. The chatbot will extract the name from the input sentence based on the result of named entity recognition.(10 marks) This is to improve the accuracy when extracting names from a sentence.

#Example:
#What's your name? :)
#My name is Ben
#Named entity recognition to extract a person's name:
#Ben PERSON
#Ask me some questions Ben :)