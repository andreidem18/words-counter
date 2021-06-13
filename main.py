from file_class import File

        
print("\n\n" +
      "        ********************************************\n" +
      "        ********                            ********\n" +
      "        ********       WORDS SEARCHER       ********\n" +
      "        ********                            ********\n" +
      "        ********************************************\n\n")
try:
    print("        Hey there! I have extracts of:\n" +
          "           1. Don Quijote\n" +
          "           2. The Lord of the Rings\n" +
          "           3. The odyssey\n\n")
    text = int(input("         === Give me the number of a file: "))
    flag = True
    while flag:
        if text == 1 or text == 2 or text == 3:
            flag = False
        else:
            print("        Sorry, invalid value\n")
            text = int(input("         === Give me the number of a file: "))
    
    if text == 1:
        text = 'don_quijote'
    elif text == 2:
        text = 'the_lord_of_the_rings'
    elif text == 3:
        text = 'the_odyssey'
    file = File(text)
        
    top_num = input("         === How many words do you want to consult: ")
    
    print(f'\nThe Top {top_num} most repited words in my "{text}" extract are:')
    print(file.get_top(int(top_num)))
    
except Exception as error:
    print(error)
    