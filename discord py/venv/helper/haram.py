import random
symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '💎', '🍀']

async def slot_machine():
    # Pick 3 random symbols
    result = [random.choice(symbols) for _ in range(3)]
    
    # Show the result of the slot machine
    result_str = " | ".join(result)
    
    # Check if the player wins (all three symbols are the same)
    if result[0] == result[1] == result[2]:
        return f"🎰 {result_str} 🎉 You win!"
    else:
        return f"🎰 {result_str} 😢 Try again!"