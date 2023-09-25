def findPairsWithSum(inputArray, targetSum):
    pairsFound = False  # A flag to track if any pairs were found

    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            if inputArray[i] + inputArray[j] == targetSum:
                print("Pair found:", inputArray[i], inputArray[j])
                pairsFound = True

    if not pairsFound:
        print("No pairs found with the given sum.")

# Example usage:
inputArray = [2, 4, 3, 5, 7, 8]
targetSum = 10
findPairsWithSum(inputArray, targetSum)
