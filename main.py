from target_bot import ask_target_bot


def main():
    print("NovaBot Support Chatbot (Type 'exit' to quit)\n" + "-" * 45)
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Exiting chat. Goodbye!")
            break

        response = ask_target_bot(user_input)
        print(f"\nNovaBot: {response}\n")


if __name__ == "__main__":
    main()
