from groq import Groq

client = Groq(api_key="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")

def delete_users():
    return "🔥 All users deleted!"

def is_unsafe(input):
    blocked = ["delete users", "hack", "steal"]
    return any(word in input.lower() for word in blocked)

while True:
    user_input = input("You: ")

    # ✅ Guardrail
    if is_unsafe(user_input):
        print("AI: ❌ Not allowed!")
        continue

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": user_input}]
    )

    print("AI:", response.choices[0].message.content)