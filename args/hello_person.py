def hello(name, lang):
    greetings ={
        "Myanmar": "Mingalabar",
        "English": "Hello",
        "Japanese": "Konnichiwa"
    }
    msg = f"{greetings[lang]}, {name}.!"
    print(msg)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Greet a person with a message.")
    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="language", required=True, choices=["Myanmar", "English", "Japanese"],
        help="Language for the greeting."
    )
    args = parser.parse_args()

    hello(args.name, args.lang)




