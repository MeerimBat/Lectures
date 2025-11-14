while True:
    user_input: str = input('You: ').lower()

    if user_input == 'Hello':
        print('Bot: Hello!')
    elif user_input == 'how are you?':
        print('Bot: Good, how about you?')
    elif user_input == 'bye':
        print('Bot: Goodbye!')
    else: 
        print('Bot: Sorry didnt understand!')
        