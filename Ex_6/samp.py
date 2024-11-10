# Function to convert character to binary
def char_to_binary(char):
    return format(ord(char), '08b')  # Convert character to 8-bit binary

# Function to convert binary back to character
def binary_to_char(binary_string):
    decimal_value = int(binary_string, 2)  # Convert binary to decimal
    return chr(decimal_value)  # Convert decimal to character


# Step 1: Input string
input_string = "John Prath8p"

# Step 2: Convert each character to binary and store in an array
binary_array = [char_to_binary(char) for char in input_string]

# Display the binary representation of the input string
print("Binary representation of each character:")
for i, binary in enumerate(binary_array):
    print(f"Character '{input_string[i]}' -> Binary: {binary}")

# Step 3: Convert the binary array back to the original string
original_string = ''.join([binary_to_char(binary) for binary in binary_array])

# Step 4: Output the original string
print("\nOriginal string after converting back from binary:")
print(original_string)