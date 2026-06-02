from groq import Groq


api_key="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"
Client=Groq(api_key=api_key)
while True:
    prompt=input("Enter your prompt:")
    if prompt.lower()=="exit":
        print("Exiting the program.")
        break
    response=Client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1024
    )
    print("Response:", response.choices[0].message.content)