<<<<<<< HEAD:Python 12_Sep/Assignment/Module-2 (Fundamentals of python)/Que_20.py
""" Write a Python function that takes a list of words and returns the length 
of the longest one."""

def main():
    text = input("Please input a list of words to evaluate: ")

    longest = 0

    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words

    print("The longest word is", longest_word, "with length", len(longest_word))

=======
""" Write a Python function that takes a list of words and returns the length 
of the longest one."""

def main():
    text = input("Please input a list of words to evaluate: ")

    longest = 0

    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words

    print("The longest word is", longest_word, "with length", len(longest_word))

>>>>>>> 80c6c9d626d696772149a7b8dda5a88e926ca214:Assignment/Module-2 (Fundamentals of python)/Que_20.py
main() 