# char = input("enter a sentence")
# for i in char:
#     val = ord(i)
#     print(f"'{i}' {val}")

# Step 1: Input Sentence
input_sentence = input("Enter a sentence: ")

# Step 2: Tokenization
words = input_sentence.split()

# Initialize variables for tracking highest and lowest averages
highest_avg = float('-inf')  # Start with negative infinity
lowest_avg = float('inf')    # Start with positive infinity
word_with_highest_avg = ""
word_with_lowest_avg = ""

# Step 3: Calculate ASCII Averages
for word in words:
    # print(len(word))
    word_avg = sum(ord(char) for char in word if char != ' ') / len(word)
    # print(word_avg)
    # Step 4: Track Highest and Lowest Averages
    if word_avg > highest_avg:
        highest_avg = word_avg
        word_with_highest_avg = word
    if word_avg < lowest_avg:
        lowest_avg = word_avg
        word_with_lowest_avg = word

# Step 5: Print Results
print(f"Word with Highest Average ASCII Value: {word_with_highest_avg} ({highest_avg})")
print(f"Word with Lowest Average ASCII Value: {word_with_lowest_avg} ({lowest_avg})")
