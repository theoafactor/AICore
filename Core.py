import time

class Assistance:
    def __init__(self):
        pass

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
                    time.sleep(3)
                    print(response["answer"])


    

class Engine:

    def __init__(self):
        pass

    def start(self):
        print("AI has started running ...")
        assistance = Assistance()

        return assistance
        



app = Engine()