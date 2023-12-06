def ChatBot_Thor(user_input):
    user_input_lower = user_input.lower()
    
    if "hello" in user_input_lower or "hii" in user_input_lower:
        return "Hello! How may I assist you?"
    elif "how are you" in user_input_lower:
        return "I'm doing well, thanks for asking! How about you?"
    elif "what's your name" in user_input_lower:
        return "I'm Thor, a ChatBot created by Sif!"
    elif "tell me something about you" in user_input_lower:
        return "I'm Thor, a prominent God in Germanic Paganism. I'm the God of war and fertility."
    elif "bye" in user_input_lower:
        return "No problem! Have a good day."
    elif "weather" in user_input_lower:
        return "Looks like it will be partly cloudy today."
    elif "thanks" in user_input_lower:
        return "I am glad to assist you."
    elif "mathematics" in user_input_lower:
        return "Yes, I can do basic mathematics such as addition, subtraction, multiplication, division, etc."
    elif any(operation in user_input_lower for operation in ["add", "subtract", "multiply", "divide", "remainder"]):
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            
            if "add" in user_input_lower:
                return f"The result is: {a + b}"
            elif "subtract" in user_input_lower:
                return f"The result is: {a - b}"
            elif "multiply" in user_input_lower:
                return f"The result is: {a * b}"
            elif "divide" in user_input_lower:
                if b != 0:
                    return f"The result is: {a / b}"
                else:
                    return "Cannot divide by zero. Please provide a non-zero divisor."
            elif "remainder" in user_input_lower:
                if b != 0:
                    return f"The result is: {a % b}"
                else:
                    return "Cannot find the remainder when dividing by zero. Please provide a non-zero divisor."
            else:
                return "Invalid operation. Please provide numeric values for the operation."
        except ValueError:
            return "Invalid input. Please provide numeric values for the operation."
    else:
        return "I'm sorry. I couldn't understand that. Can you please tell me in an understandable way?"

while True:
    user_query = input("You: ")
    if user_query.lower() == 'exit':
        print("ChatBot: Always there for you to assist you!")
        break
    response = ChatBot_Thor(user_query)
    print("ChatBot:", response)