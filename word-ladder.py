import random

def load_words():
    return [
        "cat", "bat", "rat", "hat", "heat", "meet", "meat", "seat",
        "seam", "team", "lamp", "camp", "bump", "dump", "damp",
        "farm", "form", "firm", "worm", "word", "cord", "card",
        "hard", "herd", "bird", "bark", "dark", "park", "part",
        "cart", "coat", "boat", "moat", "moot", "root", "foot",
        "fool", "pool", "poul", "pull", "bowl", "bowl", "roll",
        "toll", "tall", "mall", "call", "fall", "ball", "bail",
        "tail", "mail", "rail", "sail", "fail", "gail", "veil",
        "seal", "meal", "heal", "real", "deal", "peal", "feel",
        "leak", "leap", "loop", "look", "book", "cook", "cool",
        "pool", "tool", "tool", "fool", "foot", "root", "boot",
        "suit", "stun", "run", "fun", "sun", "bun", "gun"
    ]

def is_one_letter_diff(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

def find_neighbors(word, word_list):
    return [w for w in word_list if is_one_letter_diff(word, w)]

def word_ladder_game():
    words = load_words()
    start_word = random.choice(words)
    end_word = random.choice(words)

    while start_word == end_word:
        end_word = random.choice(words)

    print(f"Start word: {start_word}")
    print(f"End word: {end_word}")
    
    current_word = start_word
    steps = 0

    while current_word != end_word:
        print(f"Current word: {current_word}")
        neighbors = find_neighbors(current_word, words)
        print(f"Possible next words: {', '.join(neighbors)}")
        
        player_guess = input("Enter your next word: ").strip().lower()
        
        if player_guess in neighbors:
            current_word = player_guess
            steps += 1
        else:
            print("Invalid move. Try again.")

    print(f"Congratulations! You've transformed '{start_word}' into '{end_word}' in {steps} steps.")

if __name__ == "__main__":
    word_ladder_game()
