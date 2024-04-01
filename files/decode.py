def decode(message_file):
    word_file = open(message_file)
    lines = word_file.readlines()
    print("lines", lines, len(lines))
    ordered_word_list = len(lines) * [""]
    word_file.close()
    solution = ""

    for line in lines:
        words_parts = line.split(" ")
        word=words_parts[1].strip()
        index= int(words_parts[0])-1
        ordered_word_list[index]= word
    print(ordered_word_list)

    step = 1

    while len(ordered_word_list) >= step:
        current_step_words = ordered_word_list[:step]
        print(current_step_words)
        ordered_word_list = ordered_word_list[step:]
        solution = solution + current_step_words[-1] + " "
        step += 1
    return solution.strip()

print(decode("decode_test.txt"))

print(decode("decode.txt"))
