import random

def generate_sentence():
    subjects = ["The cat", "A dog", "My friend", "The teacher", "The student"]
    verbs = ["eats", "plays with", "sees", "enjoys", "finds"]
    objects = ["a ball", "the book", "a toy", "an apple", "a puzzle"]
    adverbs = ["quickly", "happily", "lazily", "gracefully", "angrily"]

    # Randomly select one word from each list
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object_ = random.choice(objects)
    adverb = random.choice(adverbs)

    # Construct the sentence
    sentence = f"{subject} {verb} {object_} {adverb}."
    return sentence

def main():
    sentence = generate_sentence()
    print(f"Generated Sentence: {sentence}")

if __name__ == "__main__":
    main()