questions = [
    [
        "What is the output of the following code snippet? print(2 + 3 * 4)", 20, 14, 32, 15, 2
    ],
    [
        "Which of the following is a correct way to comment in Python?", "// This is a comment", "/* This is a comment */", "# This is a comment",
        "'This is a comment '", 3
    ],
    [
        "What is the purpose of the 'elif' keyword in Python?", "It is short for 'else if' ", "It is used for creating a list", "It is a typo and has no meaning",
        "It is an abbreviation for 'else list'", 1
    ],
    [
        "Which planet is known as the 'Red Planet'?", "Venus", "Mars", "Jupiter",
        "Saturn", 2
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen",
        "Mark Twain", 2
    ],
    [
        "In which year did the Titanic sink?", 1912,  1905,  1920,
        1931, 1
    ],
    [
        "What is the capital city of Japan?", "Beijing", "Seoul", "Tokyo",
        "Bangkok", 3
    ],
    [
        "Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci",
        "Michelangelo", 3
    ],
    [
        "Which ocean is the largest on Earth?", "Indian Ocean", "Atlantic Ocean", "Southern Ocean",
        "Pacific Ocean", 4
    ],
    [
        "What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra",
        " Brisbane", 3
    ],
    [
        "Which famous scientist developed the theory of relativity?", "Isaac Newton", "Galileo Galilei", "Albert Einstein",
        "Stephen Hawking", 3
    ],
    [
        "Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Iron",
        "Uranium", 1
    ],
    [
        "What is the capital city of France?", "Rome", "Berlin", "Madrid",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Paris", 4
    ],
    [
        "Which country is known as the 'Land of the Rising Sun'?", "China", "Japan",
        "South Korea", "Vietnam", 2
    ],
    [
        "What is the largest mammal in the world?", "Elephant", "Giraffe", "Blue Whale",
        "Polar Bear", 3
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 500000, 1000000, 70000000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit : "))
    if reply == 0:
        money = levels[i - 1]
        break
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 15:
            money = 70000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")
