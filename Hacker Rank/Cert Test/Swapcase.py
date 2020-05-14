def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
      
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence.swapcase()


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
