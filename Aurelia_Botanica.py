from pyfiglet import Figlet

def ascii_art():
    figlet = Figlet()
    banner = figlet.renderText("Aurelia Botanica")
    print(banner)

def high_yield():
    gram_input = int(input("how many grams of your herb you want to calculate? "))

    answer_divided = gram_input/100
    low_end_answer = answer_divided * 2
    high_end_answer = answer_divided * 5

    print(f"your yield will fall between {low_end_answer}ml and {high_end_answer}ml")

def mid_yield():
    gram_input = int(input("how many grams of your herb you want to calculate? "))

    answer_divided = gram_input/100
    low_end_answer = answer_divided*0.5
    high_end_answer = answer_divided*2

    print(f"your yield will fall between {low_end_answer}ml and {high_end_answer}ml")

def low_yield():
    gram_input = int(input("how many grams of your herb you want to calculate? "))

    answer_divided = gram_input/100
    low_end_answer = answer_divided*0.1
    high_end_answer = answer_divided*0.5

    print(f"your yield will fall between {low_end_answer}ml and {high_end_answer}ml")

def main():
    ascii_art()
    while True:
        # Display prompt
        command = input(">>> ")  # You can customize the prompt text
        
        if command.lower() == "exit":
            print("Exiting...")
            break
        
        # Process the command
        process_command(command)


def process_command(command):
    if command == "help":
        print("high yield = >2%\n"
              "medium yield = 2%-0,5%\n"
              "low yield = <0,5%")
    elif command == "high yield":
        high_yield()
    elif command == "medium yield":
        mid_yield()
    elif command == "low yield":
        low_yield()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()