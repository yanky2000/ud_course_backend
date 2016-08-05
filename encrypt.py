class Rot13():
    def __init__(self, 
                start_char = "a",
                end_char = "z",
                step = 13):
        self.start_char = start_char
        self.end_char = end_char
        self.step = step

        # 1. First we make lists of keys and thier encrypted values, based on ROT13 algorythm
        # 2. Create a dictionary from keys and values lists
        
        # Bunch of local vars
        start = ord(self.start_char)
        end = ord(self.end_char)
        char_range = range(start, end + 1)

        # List of keys
        self.keys = []
        for i in char_range:
            self.keys.append(chr(i))

        # List of values
        self.values = []
        for i in char_range:
            if not (i + step) > end:
                encrypted_value = chr(i + step)
            else:
                index = (i + step) - end
                encrypted_value = chr(char_range[index - 1])
            self.values.append(encrypted_value)

    # Make dictionary for encrypting
    def encrypted_dic(self):
        return dict(zip(self.keys, self.values))

    # Make dictionary for decrypting
    def decrypted_dic(self):
        return dict(zip(self.values, self.keys))

d = Rot13()
en = d.encrypted_dic()
de = d.decrypted_dic()
print "en :"+str(en)
print "de :"+str(de)
