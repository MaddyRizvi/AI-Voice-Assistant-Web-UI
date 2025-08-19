import streamlit as st
import speech_recognition as sr
import pyttsx3
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Load AI Model
llm = OllamaLLM(model="mistral")  # Change to "llama3" or another Ollama model

# Initialize Memory (LangChain v1.0+)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()  # Stores user-AI conversation history

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)  # Adjust speaking speed

# Speech Recognition
recognizer = sr.Recognizer()

# Function to Speak AI Responses
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to Listen to Voice Input
def listen():
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        st.write(f"👂 You Said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        st.write("🤖 Sorry, I couldn't understand. Try again!")
        return ""
    except sr.RequestError:
        st.write("⚠️ Speech Recognition Service Unavailable")
        return ""

# Define AI Chat Prompt
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
)

# Function to Process AI Responses
def run_chain(question):
    # Converting memory into text  
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])

    #Fills the prompt with (history + user) input and then invoking LLM
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

    # Store new user input and AI response in memory
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)

    return response

# Streamlit Web UI
st.title("🤖 AI Voice Assistant (Web UI)")
st.write("🎙️ Click the button below to speak to your AI assistant!")

# Button to Record Voice and generate Response to that
if st.button("🎤 Start Speaking"):
    user_query = listen()
    if user_query:
        ai_response = run_chain(user_query)
        st.write(f"**You:** {user_query}")
        st.write(f"**AI:** {ai_response}")
        speak(ai_response)  # AI speaks the response

# Display Full Chat History
st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")








































# import speech_recognition as sr
# import pyttsx3
# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM

# # load AI model
# llm = OllamaLLM(model = "mistral")

# # initialize Memory (LangChain v1.0+)
# chat_history = ChatMessageHistory()

# # speech recognition
# recognizer = sr.Recognizer()

# # initiliaze text to speech
# engine = pyttsx3.init()
# engine.setProperty("rate", 160)     # Adjust speaking Speed



# # Function to speak
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to Listen
# def listen():
#     with sr.Microphone() as source:
#         print("\n Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     try:
#         query = recognizer.recognize_google(audio)  # speech to text using google Web speech api 
#         print(f" You said: {query}")
#         return query.lower()
#     except sr.UnknownValueError:             # when audio can't be comprehended
#         print(" Sorry, i couldn't understand, Try again please!")
#         return ""
#     except sr.RequestError:        # when google speech recognition is not accessible
#         print(" Speech Recognition service unavailable")
#         return ""




# # AI Chat Prompt
# prompt = PromptTemplate(
#     input_variables=["chat_history", "question"],
#     template = "Previous conversation: {chat_history}\n User: {question}\n AI:"
# )

# # function to Process AI responses
# def run_chain(question):
#     # Converting memory into text  
#     chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])

#     #Fills the prompt with history + user input and then invoking LLM
#     response = llm.invoke(prompt.format(chat_history = chat_history_text, question = question))

#     # Stores both user’s question and AI’s answer into memory.
#     chat_history.add_user_message(question)
#     chat_history.add_ai_message(question)

#     return response

# # Main Loop 
# speak(" Hello i am your AI assistant, How can i help you today!")
# while True:
#     query = listen()
#     if "exit" in query or "stop" in query:
#         speak("GoodBye! Have a great day!")
#         break
#     if query:
#         response = run_chain(query)
#         print(f"\n AI Response: {response}")
#         speak(response)