"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Daniel Crandle
Date: 2024-10-26

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    if character_class == "Warrior":
        strength = 10 + (level * 3)
        magic = 2 + (level * 1)
        health = 100 + (level * 10)
    elif character_class == "Mage":
        strength = 3 + (level * 1)
        magic = 15 + (level * 4)
        health = 70 + (level * 5)
    elif character_class == "Rogue":
        strength = 7 + (level * 2)
        magic = 7 + (level * 2)
        health = 60 + (level * 4)
    elif character_class == "Cleric":
        strength = 6 + (level * 2)
        magic = 12 + (level * 3)
        health = 90 + (level * 7)
    else:
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 80 + (level * 5)
    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    
    if not character or not filename:
        return False

    # Check if the directory exists
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False


    with open(filename, 'w') as character_save:
        character_save.write(f"Character Name: {character['name']}\n")
        character_save.write(f"Class: {character['class']}\n")
        character_save.write(f"Level: {character['level']}\n")
        character_save.write(f"Strength: {character['strength']}\n")
        character_save.write(f"Magic: {character['magic']}\n")
        character_save.write(f"Health: {character['health']}\n")
        character_save.write(f"Gold: {character['gold']}\n")
        return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    
    if not os.path.exists(filename):
        return None
    
    with open(filename, 'r') as character_load:
        lines = character_load.readlines()
        character = {}
        character['name'] = lines[0].strip().split(": ")[1]
        character['class'] = lines[1].strip().split(": ")[1]
        character['level'] = int(lines[2].strip().split(": ")[1])
        character['strength'] = int(lines[3].strip().split(": ")[1])
        character['magic'] = int(lines[4].strip().split(": ")[1])
        character['health'] = int(lines[5].strip().split(": ")[1])
        character['gold'] = int(lines[6].strip().split(": ")[1])      
    return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character['level'] += 1
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    # Example usage
    my_char = create_character("Aria", "Mage")
    display_character(my_char)
    save_character(my_char, "aria_save.txt")
    loaded_char = load_character("aria_save.txt")
    display_character(loaded_char)
    level_up(loaded_char)
    display_character(loaded_char)
    save_character(loaded_char, "aria_save.txt")
    test_char = load_character("test_character.txt")
    display_character(test_char)
    display_character(loaded_char)