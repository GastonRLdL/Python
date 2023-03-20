import string
import sys

def text_analyzer(string=None):
    """
    This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.
    """
    if not isinstance(string, str):
        print("AssertionError: Argument is not a string")
        return
    if not string:
        string = input("What is the text to analyze?\n")
    space = string.count(' ')
    minus = sum(1 for c in string if c.islower())
    mayus = sum(1 for c in string if c.isupper())
    nums = sum(1 for c in string if c.isdigit())
    punctuation = len(string) -space -minus -mayus -nums
    print(f"The text contains {len(string)} character(s):")
    print(f"- {mayus} upper letter(s)")
    print(f"- {minus} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {space} space(s)")
if __name__ == "__main__":
    if len(sys.argv) > 2:
            print("Error Error Error!")
    elif len(sys.argv) == 2:
            text_analyzer(sys.argv[1])
    else:
        exit