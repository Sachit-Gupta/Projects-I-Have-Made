def remove_every_other_letter_from_six_letter_word(word):
    word = input("Enter a six letter word to have its alternate letters removed: ")
    print("Ah!, I see! " + "'" + word + "'! " + "What a nice word! I'll get right on it!")
    index = 1
    word = word[:index] + word[index+1:index+2] + word[index+3:index+4]
    print("The word now is: " + word)
    print("******************************************************************************************************************************")

print("**********************************************************************************************************************************")
remove_every_other_letter_from_six_letter_word(word="")