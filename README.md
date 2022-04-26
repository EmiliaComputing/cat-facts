# Cat Facts

### Introduction
This is a very short program which I created to further my knowledge about how python can extract information from websites and about how “JSON” works. I decided to create a program which prints random cat facts in order to do this.

### Project Goals/Requirements
I used python to create this project, however I imported “JSON” so that the computer could store and transport the data. 

There is no target audience for this project, as the purpose of it was only to create a simple program to increase my knowledge about “JSON” and how python extracts information from websites.

### Design
The user interacts with the computer by pressing enter for a new fact to be printed. There are no buttons on screen as only the keyboard is used.

This project uses a “while”, condition controlled, loop so that the program prints a random fact from a website every time the enter key on the keyboard is pressed. Below is an extract of the code, written in python, which shows how this loop works:

    while True:
      prompt = input(“press enter to get a random cat fact”)
      random_fact = random.choice(all_facts)
      print(random_fact[“text”])
      print()

### Evaluation
I feel that this project went well as I successfully gained knowledge about the functions of python and JSON. I created a short project which demonstrates this by extracting and printing random cat facts from websites.

