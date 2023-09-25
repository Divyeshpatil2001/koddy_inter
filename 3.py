def find_min_coins_notes(amount, denominations):
    result = {}  # Dictionary to store the denomination count

    # Sort the denominations in descending order to use larger denominations first
    denominations.sort(reverse=True)

    for denom in denominations:
        if amount >= denom:
            count = amount // denom  # Calculate how many of this denomination can be used
            result[denom] = count  # Store the count in the result dictionary
            amount -= count * denom  # Update the remaining amount

    return result

def main():
    # Define the denominations and their values as a dictionary
    denominations = {
        1: "One Rupee",
        2: "Two Rupees",
        5: "Five Rupees",
        10: "Ten Rupees",
        20: "Twenty Rupees",
        50: "Fifty Rupees",
        100: "One Hundred Rupees",
        200: "Two Hundred Rupees",
        500: "Five Hundred Rupees",
        2000: "Two Thousand Rupees",
    }

    # Input the amount
    amount = float(input("Enter the amount in Rupees: "))

    # Call the function to find the minimum coins/notes
    result = find_min_coins_notes(amount, list(denominations.keys()))

    # Display the results
    print("\nMinimum number of coins/notes needed:")
    for denom, count in result.items():
        print(f"{count} {denominations[denom]} ({denom} Rupees)")

if __name__ == "__main__":
    main()
