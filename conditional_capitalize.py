"""Write a function(preLetterCase) that accepts two parameters ( a string ,and a letter). The function must return the string with all characters before the first instance of the letter converted to lowercase and all other characters converted to uppercase. Hence, if the specified letter is the first character of the string then the entire string will be converted to uppercase. The new string should be returned by the function.
e.g.
preLetterCase ("CAtCHa","a") -> "cATCHA",
preLetterCase ("Preteen","e") -> "prETEEN"
preLetterCase ("You've got this", "m") -> "you've got this"
preLetterCase ("Keep trying", "k") -> "KEEP TRYING"""

def preLetterCase(s, letter):
    index = s.find(letter)
    if index == -1:
        return s
    before_letter = s[:index].lower()
    after_letter = s[index:].upper()
    return before_letter + after_letter
