def send_data(bit, length):
    r = calredundant(length) # It calculate the no of redundant bit
    pos = posRedundantBit(bit, r, length) # It find the position of the redundant bit
    par = findParity(pos, r) # It set the value in the redundant position 
    return par
    
def calredundant(l):
    for i in range(l):
        if( 2**i >= l+i+1 ):
            return i

def posRedundantBit(bit, r, l):
    j = int(0)
    res = []
    reverse_bit = bit[::-1] # Reverse of 'bit'
    rev_len = 0 # Length of 'reverse_bit'
    for i in range(1,l+r+1):
        if(pow(2,j) == i):
            res.append('0')
            j+=1
        else:
            res.append(reverse_bit[rev_len])
            rev_len+=1
    return res # Returning the reversed data + redundant bit

def findParity(pos, r):
    red = 0
    while red <= r:
        count = 0
        for i in range(len(pos)):
            if i+1 == pow(2,red):
                step = pow(2,red)
                for temp in range(i, len(pos), step * 2):
                    j = step
                    while j > 0 and temp < len(pos):
                        if pos[temp] == '1':
                            count += 1
                        temp += 1  # increment temp for each j
                        j -= 1
                if count % 2 != 0:
                    pos[i] = '1'
                else:
                    pos[i] = '0'
        red += 1
    return pos[::-1]

def write_data(message):
    with open("channel.txt", "w") as file:
        if isinstance(message, list):
            # Join the binary strings in the message with a separator, like space or newline
            file.write('\n'.join(message) + '\n')
        else:
            # If it's a single string, write it directly
            file.write(message + '\n')

def char_to_binary(char):
    return format(ord(char), '08b')

message = input("Enter your message: ")
bit = [char_to_binary(char) for char in message]
length = len(bit)
hamming_code = send_data(bit, length)
send = write_data(hamming_code)