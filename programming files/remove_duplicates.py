def remove_duplicates(arr):
    # Sort arr
    arr.sort()
    # Create two arrays, one to hold the removed elements and one to hold the final array with no duplicates
    unique_arr = []
    removed_elements = []
    # Loop through arr
    for i in range(len(arr)):
        # If this is the first element of arr or
        # the element at index i if it is not equal to the previous element in arr
        if i == 0 or arr[i] != arr[i-1]:
            # Add the value to unique_arr
            unique_arr.append(arr[i])
        else:
            # Else, the element is a duplicate value, so add it to removed_elements
            removed_elements.append(arr[i])
    # Return the two arrays
    return unique_arr, removed_elements

# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)
