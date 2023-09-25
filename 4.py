def reverse_with_spaces(input_string):
    # Create a list to store the positions of spaces
    space_positions = []
    
    # Iterate through the input string and record the space positions
    for i, char in enumerate(input_string):
        if char.isspace():
            space_positions.append(i)
    
    # Reverse the input string without spaces
    reversed_string = ''.join(input_string.split()[::-1])
    print(reversed_string)
    
    # Initialize variables for the reversed string with spaces and space index
    reversed_with_spaces = list(reversed_string)
    
    space_index = 0
    
    # Insert spaces at the original positions
    for pos in space_positions:
        reversed_with_spaces.insert(pos, ' ')
    
    # Convert the list back to a string
    reversed_with_spaces = ''.join(reversed_with_spaces)
    
    return reversed_with_spaces

def main():
    input_string = input("Enter a string: ")
    reversed_result = reverse_with_spaces(input_string)
    print("Reversed string with preserved spaces:")
    print(reversed_result)

if __name__ == "__main__":
    main()
