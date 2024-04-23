"""
create a function'ask_questions', It takes the questions dictionary as an argument
 and iterates over each question,
 prompting the user for an answer and storing it in the dictionary. 
 create a variable score that will store the performance of user
 the if condition compares user's answer and the corerct answers,
 finally the number of questions that are answered correctly is displayed and the percentage as well 
"""
def ask_questions(questions):
    score=0
    for question, answer in questions.items():
        user_answer = input(question+ " ")
        questions[question] = user_answer
        if user_answer.lower() == answer.lower():
         print("Correct")
         score += 1
        else:
         print("Incorrect, the correct answer is:", answer)

    print("You got " +str(score), " questions right")
    print("You scored " +str(score/len(questions))+"%")

"""
create the main function, containing a dictionary with the questions as keys and the answers as values
call the 'ask_questions' function which will execute the quiz

"""
def main():
 questions={
    "What is DNS?":"Domain Name System",
    "What does OOP stand for?":"Object-Oriented Programming",
    "Define API":"Application Programming Interface",
    "Define SQL":"Structured Query Language",
    "Define RAM":": Random Access Memory",
    "What is IPv6":"Internet Protocol version 6",
    "Explain TCP.":"Transmission Control Protocol",
    "Define IDE":"Integrated Development Environment",
    "What is SSH":"Secure Shell"
  }

 print("welcome to my quiz game!")
 playing=input("Would you like to play?: ")
 if playing.lower() != "yes":
     quit()

 print("Time to play!")
 
 ask_questions(questions)

if __name__ == "__main__":
    main()