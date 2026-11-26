import hashlib
import random
import time

# Input the SHA-256, pseudonym and nonce
# Hash is fixed cause I'm starting form one place
# pseudonym is fixed because its mine
# nonce starts at 0 and will be incremented until the difficulty is met
previousHashValue = "0000023cf3eaefb61f8bd0b36a5780e22a54c53d1e2513375d001564d90a8c26"
myPseudonym = "cranberry"
previousDifficulty = 22
#newHashValue = hashlib.sha256((previousHashValue + myPseudonym + myNonce).encode()).hexdigest()

#function to calculate the difficulty of a hash by counting the number of leading zeros bits byte by byte
def calculate_difficulty(hash_bytes):
    difficulty = 0
    for byte in hash_bytes:
        if byte == 0:
            difficulty += 8
        else:
            # Count the number of leading zeros in the byte
            mask = 1 << 7  # Start with the leftmost bit (128 in decimal)
            for i in range(8):  # Check bits from left to right
                if (byte & mask) == 0:
                    mask >>= 1  # Shift the mask to the right for the next bit
                    difficulty += 1
                else:
                    break
            break
    return difficulty

# Code to start mining
# Check the input integer to this python file, if it is 1, then set process_number to 1, else set it to 0
import sys

if len(sys.argv) > 1:
    process_number = int(sys.argv[1])
else:
    process_number = 0

total_mining_time = 0  # Initialize total mining time

#keeps mining until difficulty is 42
while previousDifficulty < 42:

    max_difficulty_found = 0

    while True:
        # Start the timer for this block
        interval_start_time = time.perf_counter()

        # Generate a unique nonce for the process by using a random number generator and bitwise operations
        
        #   Generate a random nonce# Generate a random nonce with alphanumeric characters
        myNonce = ''.join(random.choices('0123456789abcdef', k=16))  # Generate a random 16-character hexadecimal nonce
        # myNonce = random.randint(0, 2**32 - 1) # Generate a random 32-bit integer nonce
        
        #if process_number:
        #    myNonce = myNonce & 0x7FFFFFFF  # Set the most significant bit to 0 for process 1
        #else:
        #    myNonce = myNonce | 0x80000000 # Set the most significant bit to 1 for process 0

        # Calculate the SHA-256 hash of the concatenated string of previousHashValue, myPseudonym, and myNonce
        hash_bytes = hashlib.sha256(
            (previousHashValue + myPseudonym + str(myNonce)).encode()).digest() 
            # encode: This method converts the string to bytes.
            # digest: This method returns the sha 256 as raw bytes

        #calculate the difficulty of the new hash value by counting the leading zero bits
        difficulty = calculate_difficulty(hash_bytes)
        # Check if the difficulty is met
        if difficulty > previousDifficulty:
            newHashValue = hash_bytes.hex()
            break

        if difficulty > max_difficulty_found:
            max_difficulty_found = difficulty
            print("New max difficulty found:", max_difficulty_found, "at nonce:", myNonce, flush=True)
            #calculate time taken for every 100k nonces
            current_time = time.perf_counter()
            elapsed_time = current_time - interval_start_time
            print("Still mining... Nonce:",
                myNonce,
                "Current Difficulty:", difficulty,
                "Time taken for this interval:", round(elapsed_time, 4), "seconds",
                "Total mining time so far:", round(total_mining_time + elapsed_time, 4), "seconds",
                flush=True)
            interval_start_time = current_time
            total_mining_time += elapsed_time

        #outputs after every 100k iterations
        # myNonce += 1


    #calculates time tkaen after finding each successful hash value
    block_end_time = time.perf_counter()
    time_taken = block_end_time - interval_start_time

    #displays the new hash value, nonce, difficulty and time taken for each successful hash value
    print("\n" + "="*60)
    print("NEW BLOCK!!!!!!")
    print("="*60)
    print("New Hash Value:", newHashValue)
    print("Nonce:", myNonce)
    print("Difficulty:", difficulty)
    print("Time taken for this block:", round(time_taken, 4), "seconds")
    print("="*60 + "\n")

    #update the previous hash value and difficulty for the next round
    previousHashValue = newHashValue
    previousDifficulty = difficulty

    # Write the new hash value, nonce, and difficulty to a file
    with open("mining_results.txt", "a") as f:
        f.write(f"{previousHashValue}{myPseudonym}{myNonce}\n")