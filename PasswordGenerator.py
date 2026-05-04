import random

#define lists of characters to pull from
alph_lower = ['a','b','c','d','e',
              'f','g','h','i','j',
              'k','l','m','n','o',
              'p','q','r','s','t',
              'u','v','w','x','y','z']

alph_upper = [letter.upper() for letter in alph_lower]

special_char = ['!','@','#','$','%','&']

def GeneratePassword(length, num_lower, num_upper, num_special) -> str:
    """Generates a random string 10 characters long"""

    #converts input string to int type
    try:
        length = int(length)
    except ValueError as e:
        return f'{e}\nPassword length must be a number'
    except Exception as e:
        return f'Unexpected error:\n{e}'

    try:
        num_lower = int(num_lower)
    except ValueError as e:
        return f'{e}\nNumber of lowercase characters must be a number'
    except Exception as e:
        return f'Unexpected error:\n{e}'
    
    try:
        num_upper = int(num_upper)
    except ValueError as e:
        return f'{e}\nNumber of uppercase characters must be a number'
    except Exception as e:
        return f'Unexpected error:\n{e}'
    
    try:
        num_special = int(num_special)
    except ValueError as e:
        return f'{e}\nNumber of special characters must be a number'
    except Exception as e:
        return f'Unexpected error:\n{e}'
    
    #checks that length is between 8 and 16
    if length < 8 or length > 16:
        raise ValueError('Password length must be between 8 and 16')
    
    if num_lower + num_upper + num_special > length:
        raise ValueError('The sum of lowercase, uppercase and special characters must be less than or equal to desired length')

    #define password as empty string
    password = ''

    #loops until password is desired length
    while len(password) < length:

        #chooses random list of characters to pull from
        rand_list = random.choice([1,2,3])
        if rand_list == 1:
            password += random.choice(alph_upper)
        elif rand_list == 2:
            password += random.choice(alph_lower)
        elif rand_list == 3:
            password += random.choice(special_char)

    lower_count = 0
    upper_count = 0
    special_count = 0
    
    #checks that password has at least 2 of each character type
    for i in alph_lower:
        if i in password:
            lower_count += 1
    for i in alph_upper:
        if i in password:
            upper_count += 1
    for i in special_char:
        if i in password:
            special_count += 1

    if lower_count >= num_lower and upper_count >= num_upper and special_count >= num_special:
        return password
    else:
        return GeneratePassword(length, num_lower, num_upper, num_special)

if __name__ == '__main__':
    print(GeneratePassword(input('Please select a password length between 8 and 16:\n'),input('Please select a minimum number of lowercase characters:\n'),input('Please select a minimum number of uppercase characters:\n'),input('Please select a minimum number of special characters:\n')))