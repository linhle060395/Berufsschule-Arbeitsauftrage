def reverse_array(array):
    length = len(array)
    reversed_array = [0] * length

    for i in range(length):
        reversed_array[i] = array[length - 1 - i]

    return reversed_array

original_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

reversed_array = reverse_array(original_array)

print("Ursprüngliches Array:", ", ".join(map(str, original_array)))
print("Umgekehrtes Array:", ", ".join(map(str, reversed_array)))
