# Quiz

Quiz = {
    "Q1":{
    "Question": "What is the protocol used for sending emails?",
    "Answer": "Simple Mail Transfer Protocol"
    }, "Q2": {
        "Question": "What is the protocol used for transferring web pages?",
        "Answer": "Hypertext Transfer Protocol"
    }, "Q3": {
        "Question": "What is the unique identifier for a device on a network?",
        "Answer": "Internet Protocol address"
    },"Q4": {
        "Question": "What device connects multiple networks together?",
        "Answer": "Router"
    }, "Q5": {
        "Question": "What device connects multiple computers within the same network?",
        "Answer": "Switch"
    }, "Q6": {
        "Question": "What protocol is used to translate domain names to IP addresses?",
        "Answer": "Domain Name System"
    },"Q7": {
        "Question": "What protocol is used to secure communication over a network?",
        "Answer": "Hypertext Transfer Protocol Secure"
    },"Q8": {
        "Question": "What type of network covers a small geographical area?",
        "Answer": "Local Area Network"
    }, "Q9": {
        "Question": "What type of network covers a large geographical area?",
        "Answer": "Wide Area Network"
    }, "Q10": {
        "Question": "What is a group of interconnected networks?",
        "Answer": "Internet"
    },
}
Score = 0

for key,value in Quiz.items():
    print(value['Question'])
    answer = input("Answer : ")
    
    if answer.lower() == value['Answer'].lower():
        print("Correct")
        Score +=1
        print("Your Score : ", Score)

    else: 
        print("Wrong")
        print("The correct answer is :", value['Answer'])
        print("Your Score : ", Score)

print("Your Total Score is " + str(Score) + " / 10")
print("Your Percentage is " + str(Score/10*100) + "%")

     