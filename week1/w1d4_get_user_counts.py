def get_user_counts():
    int_count = 0
    float_count = 0
    str_count = 0
    while True:
        user_in = input("Enter something: ")
        if not user_in:
            return (int_count, float_count, str_count)
        try:
            int(user_in)
            int_count += 1
        except:
            try:
                float(user_in)
                float_count += 1
            except:
                str_count += 1
       

int_count, float_count, str_count = get_user_counts()
print("You entered {} ints, {} floats, and {} strings".format(int_count, float_count, str_count) )     
