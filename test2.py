default_params = dict(
    start_index = ord('a'),
    end_index = ord('z'),
    step = 13
)

# delta_index = end_index - start_index + 1,

# 1. make enc dict with 2 list

# 2. define encr status

# 3. swap key&value pairs depending on enc status

# 4. make dict of (position: character) dict of user_text

# 5. loop over user_text_dict and replace with encr character.

# 6. Glue up text by char positions

# (1)
def encrypt_dict(start_ltr, end_ltr, step, is_encrypted=True):

    # First we make lists of keys and values, based on ROT13 algorythm
    # and then create encrypted dictionary from them

    # List of keys
    def make_keys(start_char, end_char, **kw):
        keys = []
        for i in range (ord(start_char), (ord(end_char)+1)):
            keys.append(chr(i))
        return keys

    # List of values
    def make_values(start_char, end_char, step):
        values = []
        start = ord(start_char)
        end = ord(end_char)
        delta_index = end - start + 1 
        for i in range (start, end + 1):
            if not (i + step) > end:
                encrypted_value = chr(i + step)
            else:
                encrypted_value = chr((i + step) - delta_index)
            values.append(encrypted_value)
        return values

    
    params = dict(
        start_char = start_ltr,
        end_char = end_ltr,
        step = step
    )

    # Here we make lists of keys and values for our dictionary 
    keys_list = make_keys(**params)
    values_list = make_values(**params)

    # Create dictionary from 2 lists
    z = {
      "encrypt": dict(zip(keys_list, values_list)),
      "decrypt": dict(zip(values_list, keys_list))  
    }
    # z.encrypt = dict(zip(keys_list, values_list))
    # z.decrypt = dict(zip(values_list, keys_list))
    # if not is_encrypted:
    #     z = dict(zip(keys_list, values_list))
    # else:
    #     z = dict(zip(values_list, keys_list))
    return z
    

z = encrypt_dict("a", "e", 2, False)
# encripted = encrypt_dict("a", "e", 2, True)
print z
print z.items()
print z.keys('encrypt')
# print encripted
# keys = make_keys("a", "z")
# values = make_values("a", "z", 13)
# print values