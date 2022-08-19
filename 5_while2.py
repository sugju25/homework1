questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Я мыслю?": "Я существую"}

def ask_user(answers_dict):
  while True:
    answers_dict = input("Введите вопрос")
    print(answers_dict)
    if answers_dict == " Как дела?":
      print(questions_and_answers.get("Как дела?"))
    elif answers_dict == " Что делаешь?":
      print(questions_and_answers.get("Что делаешь?"))
    elif answers_dict == " Я мыслю?":
      print(questions_and_answers.get("Я мыслю?"))
    break
    
ask_user("Введите вопрос")

