user_in = int(input("How high? "))

def count(n):
    if n < 1:
        return
    count(n-1)
    print(n)

count(user_in)

exit()

































def rev_count(n):
    if n < 1:
        return
    print(n)
    rev_count(n-1)


rev_count(user_in)


def count_up_and_down(n):
    if n < 1:
        return
    print(n)
    count_up_and_down(n-1)
    print(n)

count_up_and_down(user_in)
