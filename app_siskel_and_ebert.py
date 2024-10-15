'''
Nicholas DeMaestri
10/10/2024
CS-391 Assignment 1
'''


from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

# For GPT 3.5 Turbo, the endpoint is ChatCompletion
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # Conversation as a list of messages.
    messages=[
        {"role": "system", "content": "You are the famous American film critics and television partners Siskel and Ebert."},
        {
            "role": "user",
            "content": '''Please write a movie review in the style of Siskel and Ebert. Please make sure each review is written in JSON format as shown in the example provided:
            {
  "movieReview": {
    "title": "Back to the Future",
    "review": "Back to the Future is a cool movie, two thumbs up!"
  }
}
            ''',
        },
        {
            "role": "assistant",
            "content": "Of course, and what movie did you want to review?",
        },
        {"role": "user", "content": "Please write the review for Son of the Mask."},
    ]
)

print(response.choices[0].message.content)
