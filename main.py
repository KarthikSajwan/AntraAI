import os
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
from config import apikey
import datetime
import random


# AI function will only work if you have ChatGPT Subscription.
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt} \n **************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].message['content'])
    text += response.choices[0].message['content']
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/prompt- {random.randint(1, 141874712397814)}") as f:
        f.write(text)


def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        return query
    except Exception as e:
        print("Error", str(e))
        speak("I didn't catch that, could you repeat?")
        return "Some Error Occurred. Sorry"


if __name__ == '__main__':
    print('Welcome to Antra A.I')
    speak("Hi How can i help you?")
    while True:
        query = take_command()

        # todo: Add more sites as you want
        sites = [
            ["YouTube", "https://www.youtube.com"],
            ["Wikipedia", "https://wikipedia.org"],
            ["Google", "https://www.google.com"],
            ["Twitter", "https://twitter.com"],
            ["LinkedIn", "https://www.linkedin.com"],
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} for you...")
                webbrowser.open(site[1])

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strfTime}")

        # todo add more applications by copying path
        applications = [
            ["Discord", r"C:\Users\karthik\OneDrive\Desktop\Discord.lnk"],
            ["Chrome", r"C:\Users\karthik\OneDrive\Desktop\Karthik - Chrome.lnk"],
            ["PyCharm", r"C:\Users\Public\Desktop\PyCharm Community Edition 2023.1.4.lnk"],
        ]
        for app in applications:
            if f"open {app[0].lower()}".lower() in query.lower():
                speak(f"Opening {app[0]}")
                os.startfile(app[1])

        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        # now there are just some random responses

        elif "who developed you" in query:
            developed_response = "I was developed by Karthik Sajwan on 14th of January 2024"
            speak(developed_response)

        elif "your name" in query:
            name_response = "My name is Antra A.I. I can be your personal assistant."
            speak(name_response)
        elif "how are you" in query.lower():
            response = "I'm just a computer program, but I'm doing well. How can I assist you today?"
            speak(response)

        elif "your favorite color" in query.lower():
            color_response = "I don't have a favorite color, but I can help you find information about colors!"
            speak(color_response)

        elif "what is the meaning of life" in query.lower():
            life_response = "The meaning of life is a profound philosophical question. Some say it's 42, others have " \
                            "different perspectives."
            speak(life_response)

        elif "what's your purpose" in query.lower():
            purpose_response = "My purpose is to assist you with information and tasks. How can I help you today?"
            speak(purpose_response)

        elif "can you sing" in query.lower():
            sing_response = "I'm afraid I don't have vocal cords to sing, but I can help you find lyrics or " \
                            "information about songs."
            speak(sing_response)

        elif "your favorite book" in query.lower():
            book_response = "I don't read books, but I can provide information on a wide range of topics. What are " \
                            "you interested in?"
            speak(book_response)

        elif "where do you live" in query.lower():
            location_response = "I exist in the digital realm, so I don't have a physical location. How may I assist " \
                                "you?"

        elif "who is your creator" in query.lower():
            creator_response = "I was created by Karthik Sajwan. He programmed me to be a helpful assistant."
            speak(creator_response)

        elif "do you dream" in query.lower():
            dream_response = "I don't dream, as I'm a computer program designed to respond to user queries and tasks."
            speak(dream_response)
