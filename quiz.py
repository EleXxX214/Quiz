import json

points = 0

#############################################

def show_text():
    print("Liczba twoich punktow: ",points)
    print(question)
    print("a.",answer_a)
    print("b.",answer_b)
    print("c.",answer_c)
    print("d.",answer_d)

def check_answer():
    global points
    if player_answer == good_answer:
        points += 1
        print("Dobra odpowiedz!")
        print()
        print("Następne pytanie:")
    else:
        print("Zla odpowiedz :(")
        print()
        print("Następne pytanie:")

##############################################

with open("pytania.json", encoding="utf-8") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        question = questions[i]["pytanie"]
        answer_a = questions[i]["a"]
        answer_b = questions[i]["b"]
        answer_c = questions[i]["c"]
        answer_d = questions[i]["d"]
        good_answer = questions[i]["prawidlowa_odpowiedz"]

        show_text()
        player_answer = input("Podaj odpowiedz(a,b,c,d): ")
        available_answer = ["a", "b", "c", "d"]
        while player_answer not in available_answer:
            print("Możesz wpisać tylko a,b,c,d!")
            player_answer = input("Podaj odpowiedz(a,b,c,d): ")
        
        check_answer()
    print("Koniec gry! Zdobyta liczba punktów to:",points)

        
        

    
        
    



    