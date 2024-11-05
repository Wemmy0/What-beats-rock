import os

import ollama
from alive_progress import alive_bar

old = "rock"
previous = [old]
score = 0
while True:
    if old:
        print(f"What beats {old}?")
    first = input("> ")
    second = old or input("> ")

    if first in previous:
        print("-" * os.get_terminal_size().columns)
        print("You can't do the same thing twice, that's not how this works...")
        print("-" * os.get_terminal_size().columns)
        continue

    prompt = f"""
    You are an all-knowing judge tasked with determining the winner in a series of - sometimes ridiculous - object-on-object battles.
    Your role is to analyze each matchup and deliver a decisive yes or no verdict on whether the first object can overcome the second.
    
    Input style: [Object 1] beats [Object 2]?
    Answer:
    Yes - [Explain in 1 sentence how the first object triumphs]
    No - [Explain in 1 sentence why the first object cannot defeat the second, or the second triumphs over the first]
    
    Rules:
    1. Consider all possible interactions between the objects. SOME matchups may including the use of magic, supernatural powers, or other extraordinary abilities. but not all. Only consider then if you think they're relent    2. The order of the objects is critical - the first one must be able to physically impact, nullify or overpower the second, even through magical means.
    3. Be creative, humorous and imaginative in your explanations. Lean into the absurdity of the matchups.
    4. If the outcome is truly ambiguous or depends on unstated details, default to "No" and explain the uncertainty.
    5. For classic "rock-paper-scissors" style matchups, treat them as part of the established game rules.
    6. There are no limits to how fantastical or outlandish the object comparisons can be.
    
    Now tell me:
    Does {first} beat {second}?
    """

    print(f"Does {first} beat {second}?")
    with alive_bar(bar=None) as bar:
        response = ollama.chat(
            # model='llama3.2',
            model='llama3.1:8b',
            messages=[{'role': 'user', 'content': prompt}],
        )
        bar()

    print(response['message']['content'])

    size = min(len(response['message']['content'].split("\n")[-1]), os.get_terminal_size().columns)
    print("-" * size)
    if "yes" in response['message']['content'].split("\n")[0].lower():
        score += 1
        old = first
    previous.append(first)
    print(f"Score: {score}")
    print("-" * size)
