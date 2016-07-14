def build_phonebook():
    book = {}
    while True:
        user_name = input("what name? ")
        if user_name == "":
            return book
        user_num = input("What is %s's number?" % user_name)
        book[user_name] = user_num


phone_book = build_phonebook()

for name in phone_book:
    print(name, phone_book[name])
        
