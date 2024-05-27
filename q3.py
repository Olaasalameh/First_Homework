import json
import csv
def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions
def ask_question(question):
    print(question["question"])
    while True:
        answer = input("Enter 'true' or 'false': ").strip().lower()
        if answer in ['true', 'false']:
            return answer == 'true'
        else:
            print("Invalid input. Please enter 'true' or 'false'.")
def conduct_quiz(questions):
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        if user_answer == question["answer"]:
            score += 1
    return score
def save_result(username, score, filename):
    result = {"username": username, "score": score}
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "score"])
        writer.writerow(result)
def main():
    questions = load_questions('network_questions.json')
    username = input("Enter your name: ").strip()
    score = conduct_quiz(questions)
    print(f"{username}, your score is: {score}/{len(questions)}")
    save_result(username, score, 'results.csv')
if __name__ == "__main__":
    main()
