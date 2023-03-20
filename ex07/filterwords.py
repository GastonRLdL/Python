import sys
import string

def count_words(string, num):
#    words = string.split()
    words_list =[]
    tmp = string.maketrans('', '', string.punctuation)
    words = tmp.split()
    for word in words:
        if len(word) > int(num):
            words_list.append(word)
    print(words_list)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        string = sys.argv [1]
        num = sys.argv [2]
        count_words(string, num)
    else:
        print('ERROR ERROR ERROR')
