"""AGE CHECK

This program ask the user's age and print if the user is an adult
"""


def age_check(user_age: int):
    """Age validation function"""
    if user_age >= 18:
        print(f'Hi user, you are an adult')
    else:
        print(f'Hi user, you are a child')


if __name__ == '__main__':

    age = int(input('How old are you?: '))  # Ask to the user for his age
    age_check(age)
