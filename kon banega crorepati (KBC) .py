Questions = [
    ["What is the national language of Pakistan?", ["1. English", "2. Spanish", "3. Urdu", "4. French"]],
    ["What is the capital of Pakistan?", ["1. Karachi", "2. Peshawar", "3. Mardan", "4. Islamabad"]],
    ["What is the currency used in Pakistan?", ["1. Dollar", "2. Rupees", "3. Riyal", "4. Darham"]],
    ["What is the name of the mountain range that is located in the north of Pakistan?", ["1. Himalayas", "2. Koh-e-Quraquram", "3. Koh-e-Hindukash", "4. None of these"]],
    ["What is the name of the parliamentary system used in Pakistan?", ["1. Presidential", "2. Monarchy", "3. Communism", "4. Republic"]],
    ["Who is the current Prime Minister of Pakistan?", ["1. Shahbaz", "2. Imran", "3. Zardari", "4. Usman"]],
    ["What is the largest city in Pakistan?", ["1. Peshawar", "2. Islamabad", "3. Karachi", "4. Quetta"]],
    ["What is the name of the longest river located in Pakistan?", ["1. Indus", "2. Tigris", "3. Euphrates", "4. Ganges"]],
    ["Who wrote the national anthem of Pakistan?", ["1. Allama Muhammad Iqbal", "2. Faiz Ahmad Faiz", "3. Quaid-e-Azam Mohammad Ali Jinnah", "4. Hafeez jalindre"]],
    ["When did Pakistan gain independence from the British?", ["1. 1947", "2. 1946", "3. 1948", "4. 1949"]]
]

Answers = ["Urdu","Islamabad","Rupees","Himalayas","Republic","Shahbaz","Karachi","Indus","Hafeez jalindre","1947"]
score = 0
for i, question in enumerate(Questions):
    print(question[0])
    for option in question[1]:
        print(option)

    Answer = input("Enter your answer: ").strip().lower()
    
    if Answer == Answers[i].lower():
        score += 1
        print("Correct!\n")
        print (score + 1, "Crooddddd !!")
    else:
        print(f"Incorrect! The correct answer is {Answers[i]}.\n")
        break


print(f"Your amount you won is {score} croooooddddd !!")