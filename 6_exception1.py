def hello_user(ask_user):
  try:
    while True:
      ask_user = input ("Как дела?")
      if ask_user == " Хорошо":
        break
      else:
        print("что значит {}?" .format(ask_user))
  except (KeyboardInterrupt):
    print("Пока!")

hello_user("Как дела?")