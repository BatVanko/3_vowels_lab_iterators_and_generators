class vowels:
    def __init__(self, str_vowels):
        self.str_vowels = str_vowels
        self.i = 0
        self.vowel = 'eyuioa'

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current_vowel = self.i
            self.i += 1
            if current_vowel >= len(self.str_vowels):
                raise StopIteration
            if self.str_vowels[current_vowel].lower()  in self.vowel:
                return self.str_vowels[current_vowel]



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
