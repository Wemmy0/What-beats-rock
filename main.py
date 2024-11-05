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
        print("-" * 60)
        print("You can't do the same thing twice, that's not how this works...")
        print("-" * 60)
        continue

    prompt = f"""
    You are part of the backend for a game in an entirely hypothetical battle. Like rock paper scissors, your task is to determine if the first object can beat or
    overcome the second object in a fictional scenario. Respond with ONLY "Yes" or "No" and a very short sentence as why you think so.

    Rules:
    1. Respond with "Yes" if the first object can physically defeat, destroy, or nullify the second object
    2. Respond with "No" if the first object cannot realistically affect or overcome the second object
    3. Consider only direct, physical interactions, what effect could one have on the other to make it useless or seriously damage it
    4. In your summary be creative, make jokes, be casual
    5. The objects must interact in their normal, typical state
    6. The comparison must involve a clear, logical outcome
    7. The order of the input sentence is EXTREMELY important 
    8. For the basic rock paper scissors match ups, like scissors beats paper, answer them like part of the traditional game
    9. Even if the match ups are ridiculous, still answer them logically, thinking about how one can physically beat the other
    
    Input format: [Object 1] beats [Object 2]
    
    Examples:
    Pig beats gun
    Answer:
    No
    A big may be smart, but there is no way a pig can survive a hit from a bullet
    
    Gun beats paper
    Answer:
    Yes
    Whilst a piece of paper might be partly intact after a bullet, it would be significantly damaged. It looses this battle.
    
    Paper beats rock
    Answer:
    Yes
    Ah the classic match, just like in the game, paper surrounds the rock and uses it's shear power to crush the rock into dust
    
    
    Fire beats Mattress
    Answer:
    Yes
    Fire can easily burn and destroy the flammable mattress. Did you really think that was a good idea?    
    
    Hammer beats Rock
    Answer: Yes
    Hammer can break the rock, shattering it into a million pieces, making it history
    
    Globe beats Cheese
    Answer:
    No
    A globe has no realistic way to defeat cheese, what where you thinking with this one?
    
    Water beats Fire
    Answer:
    Yes
    Water can extinguish fire
    
    Paper beats Mountain
    Answer:
    No
    Paper cannot affect a mountain
    
    Time stop beats rail gun
    Answer:
    Yes
    A time stop stops the rail gun from firing making it useless
        
    Now tell me: {first} beats {second}
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
