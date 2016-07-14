import re


def clean(sentence):
    return re.sub(r'[^a-zA-Z]', '', sentence).lower()


def is_palindrome(sentence):
    sentence = clean(sentence)

    if len(sentence) <= 1:
        return True

    first_char = sentence[0]
    last_char = sentence[-1]

    if first_char != last_char:
        return False

    return is_palindrome(sentence[1:-1])


# First iterative solution
# def is_palindrome(sentence):
#     sentence = clean(sentence)
#
#    if len(sentence) <= 1:
#        return True
#
#    sentence = list(sentence)
#
#    reversed_sentence = sentence[::-1]
#
#    return sentence == reversed_sentence


# Awesome improved iterative solution without extra junk
# def is_palindrome(sentence):
#     sentence = clean(sentence)
#
#     return sentence == sentence[::-1]


def main():
    user_in = input("Enter a potential palindrome: ")

    if is_palindrome(user_in):
        print("is a pal")
    else:
        print("not so much")


if __name__ == '__main__':
    main()
