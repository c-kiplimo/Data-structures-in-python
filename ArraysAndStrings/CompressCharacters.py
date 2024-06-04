class Solution(object):#class Solution
    def compress(self, chars):#function to compress the characters
        if len(chars) <= 1:
            return len(chars)
        
        write_idx = 0  # Pointer to write compressed characters
        count = 1  # Count of consecutive repeating characters
        
        for i in range(1, len(chars)):#loop through the characters
            if chars[i] == chars[i - 1]:#if the character at i is equal to the character at i-1
                count += 1#increment count by 1
            else:
                chars[write_idx] = chars[i - 1]#write the character at i-1
                write_idx += 1#increment write_idx by 1
                
                if count > 1:#if count is greater than 1
                    for digit in str(count):#loop through the count
                        chars[write_idx] = digit#write the digit
                        write_idx += 1#increment write_idx by 1
                        
                count = 1  # Reset count for new character
        
        # Write the last character and its count
        chars[write_idx] = chars[-1]
        write_idx += 1
        if count > 1:
            for digit in str(count):
                chars[write_idx] = digit
                write_idx += 1
        
        return write_idx
