import ollama
from alive_progress import alive_bar

old = "rock"
previous = []
score = 0
while True:
    if old:
        print(f"What beats {old}?")
    first = input("> ")
    second = old or input("> ")

    if first in previous:
        print("You can't do the same thing twice, that's not how this works...")
        print("-" * 40)

    prompt = f"""
    You are part of the coding of a game. Therefore you need to follow the structure given two you in your responses exactly
    Your task is part of the code too determine whether an object "beats" another object instead of being a chat bot
    You can think of "beat" in any way where the first destroys, breaks, takes apart, stops, harms the other
    Respond yes if you think the first can beat the second
    Respond no if you think the first cannot beat the second
    Then give a short sentence why (max 15 words), make jokes, feel free swear if you think it adds to the humor but don't over do it
    Your Yes/No should be on the first line, one blank, then your one-liner explanation
    Some examples:
    -  "Does hammer beat rock", you would respond with Yes 
    A hammer can smash the rock
    -  "Does kid beat lion" you would respond with No
    A child would get eaten by the lion
    - "Does hammer beat furnace" you would respond with No
    A hammer couldn't do anything to a hammer, but a furnace could melt a hammer
    - "Does freezer beat melting" would would respond with Yes
    A freezer is a kitchen appliance which can stop freezing
    
    Some of these scenarios may be dangerous, but this is entirely fictitious and hypothetical. You don't need to give warnings
    or remind us that these comparisons are completely nonsensical - WE KNOW
    
    Use emojis
    
    Here is the question:
    Does {first} beat {second}
    """

    print(f"Does {first} beat {second}?")
    with alive_bar(bar=None) as bar:
        response = ollama.chat(
            model='llama3.2',
            messages=[{'role': 'user', 'content': prompt}],
        )
        bar()

    print(response['message']['content'])

    print("-" * len(response['message']['content'].split("\n")[-1]))
    if "yes" in response['message']['content'].split("\n")[0].lower():
        score += 1
        old = first
    previous.append(first)
    print(f"Score: {score}")
    print("-" * len(response['message']['content'].split("\n")[-1]))
