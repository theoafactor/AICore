import time
import spacy
from spacy import displacy

class Assistance:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm") 

    def ask(self, question = None):
        import responses
        if question == None:
            print("You did not ask me anything ...")
            time.sleep(3)
            print("Please ask me anything ...")

        else:
            ## find the  match from the responses
            responses = responses.responses
            for response in responses:
                question = question.lower()
                if response["question"] == question:
                    print(response["question"])

                    print("processing ...")
                    time.sleep(3)
                    doc = self.nlp(question)
                    for token in doc:
                        print(token.pos_)

                    print(response["answer"])


    

class Engine:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm") 

    def start(self):
        print("AI has started running ...")
        assistance = Assistance()

        return assistance
        



app = Engine()