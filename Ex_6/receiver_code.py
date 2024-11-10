def detectError(received):
    r = calredundant(len(received))  # Calculate the number of redundant bits
    received = list(received[::-1])  # Reverse the received code for easier parity check
    error_position = 0
    
    # Check each redundant bit position (power of 2)
    for red in range(r):
        count = 0
        for i in range(len(received)):
            if i + 1 == pow(2, red):
                step = pow(2, red)
                for temp in range(i, len(received), step * 2):
                    j = step
                    while j > 0 and temp < len(received):
                        if received[temp] == '1':
                            count += 1
                        temp += 1
                        j -= 1
        # If the parity check fails, update the error position
        if count % 2 != 0:
            error_position += pow(2, red)
    
    return error_position

def calredundant(l):
    for i in range(l):
        if( 2**i >= l+i+1 ):
            return i

def receiver(received):
    error_position = detectError(received)
    
    if error_position != 0:
        print(f"Error detected at position {error_position}")

        if error_position <= len(received):
        # Correct the error by flipping the bit at the detected error position
            received = list(received)
            error_index = error_position - 1
            received[error_index] = '0' if received[error_index] == '1' else '1'
            # print(f"Corrected data: {''.join(received)}")
        else:
            print("Error position is out of range.")
    
    message = ''.join([binary_to_char(binary) for binary in received])
    print(f"Message is : {message}")

def binary_to_char(binary_string):
    decimal_value = int(binary_string, 2)  # Convert binary to decimal
    return chr(decimal_value)

def read_data():
    with open("channel.txt", "r") as file:
        bin_data = file.readlines()
    return [line.strip() for line in bin_data]

read = read_data()
receiver(read)