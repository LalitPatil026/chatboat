from django.shortcuts import render
from .client1 import chat_gpt  # Import the function from openai_client.py

def chatbot_view(request):
    response = ""
    if request.method == "POST":
        # Correct way to get user input from POST data
        user_input = request.POST.get("query", "")  # Get the user query from the form
        
        if user_input:  # Only query GPT if there's input
            response = chat_gpt(user_input)  # Get the response from GPT-3/4
        else:
            response = "Please provide a query."

    return render(request, "chatbot.html", {"response": response})
