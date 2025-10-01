import random
#function section
def generateGuessedWord(randomWord, lengthOfWord, visited):
    countVisited=0
    for i in range(lengthOfWord):
            ch = randomWord[i].lower()
            if ch == " ":
                print(" ", end=" ")  # keep spaces visible
                continue
            chIndex = ord(ch) - ord('a')
            if not visited[chIndex]:
                print("_", end=" ")
            else:
                countVisited += 1
                print(ch, end=" ")
    return countVisited


def processGuessedWord(lengthOfWord,randomWord,visited,guess,found,lives):
    for i in range(lengthOfWord):
        if guess == randomWord[i].lower():
            visited[index] = True
            found = True

    if (not found):
        lives -= 1
        print("❌", guess.upper(), "is not in the word.")
    return lives


#start of main program
words = [
    # Easy terms
    "Inflammation", "Edema", "Hyperplasia", "Hypertrophy", "Atrophy",
    "Necrosis", "Apoptosis", "Granuloma", "Fibrosis", "Ulcer",
    "Hemorrhage", "Thrombosis", "Embolism", "Ischemia", "Infarction",
    
    # Hard terms
    "Leukocytoclastic vasculitis", "Amyloidosis", "Dysplasia", "Metaplasia",
    "Karyorrhexis", "Karyolysis", "Coagulative necrosis", "Caseous necrosis",
    "Granulomatous inflammation", "Hyperkeratosis", "Steatosis", "Hemosiderosis",
    "Lipofuscinosis", "Necroptosis", "Pyknosis"
]

pathology_clues = [
    # Easy terms
    "Swelling, redness, and pain due to injury or infection.",
    "Extra fluid collected in body tissues.",
    "More cells than normal in a tissue.",
    "Cells getting bigger, making the organ bigger.",
    "Cells or tissue shrinking or wasting away.",
    "Death of cells due to damage or lack of blood.",
    "Natural process where cells die in a controlled way.",
    "Small bump of immune cells in chronic inflammation.",
    "Extra scar tissue forming in an organ.",
    "A cut or break in skin or mucous membrane.",
    "Blood leaking out of a vessel.",
    "Blood clot formed inside a vessel.",
    "Something blocking a blood vessel.",
    "Tissue not getting enough blood.",
    "Tissue dying because of no blood supply.",
    
    # Hard terms
    "Inflamed blood vessel with broken white blood cells.",
    "Protein building up abnormally in tissues.",
    "Cells growing abnormally, may become pre-cancer.",
    "One cell type replaced by another type not normal there.",
    "Cell nucleus breaking apart during cell death.",
    "Cell nucleus completely dissolving.",
    "Tissue death with cell outlines but no nucleus.",
    "Necrosis that looks like cheese, seen in TB.",
    "Chronic inflammation with grouped immune cells.",
    "Skin or lining getting thicker.",
    "Fat building up in liver cells.",
    "Too much iron stored in tissues.",
    "Brownish pigment building up in cells with age.",
    "Controlled necrosis that causes inflammation.",
    "Nucleus shrinking during cell death."
]

print("\n🎉 Welcome to Pathology Hangman! 🎉")
print("Try to guess the word based on the clue. You have 6 lives.\n")

while (True):
    # Setup for a new game
    rand = random.randint(0, len(words) - 1)
    randomWord = words[rand]
    clue = pathology_clues[rand]
    lengthOfWord = len(randomWord)
    lives = 6
    completed = False
    visited = [False] * 26

    print("👉 Clue:", clue)

    while (not completed and lives > 0):
        found = False
        print("\nWord: ", end="")

        countVisited=generateGuessedWord(randomWord, lengthOfWord, visited)

        print("\n❤️ Lives left:", lives)

        # Win condition
        if countVisited == lengthOfWord - randomWord.count(" "):
            print("\n🎊 Congratulations! You guessed it right:", randomWord)
            break

        guess = input("👉 Enter your guess (a single letter): ").lower()

        # Input validation
        if (not guess.isalpha() or len(guess) != 1):
            print("⚠️ Please enter only one alphabet letter.")
            continue

        index = ord(guess) - ord('a')
        if visited[index]:
            print("⚠️ You already tried", guess.upper(), "- pick another letter.")
            continue

        # Process guess
        lives=processGuessedWord(lengthOfWord,randomWord,visited,guess,found,lives)

    if lives == 0:
        print("\n💀 Game Over! The word was:", randomWord)

    choice = input("\n🔄 Do you want to play again? (y/n): ").lower()
    if choice != 'y':
        print("\n👋 Thanks for playing Pathology Hangman! Stay healthy!")
        break
