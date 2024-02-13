def remove_every_other_letter(word):
    word = input("Enter a word to have its alternate letters removed: ")
    print("Ah!, I see! '" + word + "'! " + "What a nice word! I'll get right on it!")
    index = 1
    res = ""
    add = 1
    add2 = 2
    res = word[:index] 
    for i in range(len(word)-2):
        res = res + word[index+add:index+add2]
        add = add +1
        add2 = add2 + 1
        index = index + 1
    print("The word now is: " + res)
    print("******************************************************************************************************************************")

print("**********************************************************************************************************************************")
remove_every_other_letter(word="")

