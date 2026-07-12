class Solution:
    def multiply(self, num1: str, num2: str) -> str:
            if num1 == "0" or num2 == "0":
                return "0"
            
            # Initialize result array
            # Maximum possible length is len(num1) + len(num2)
            result = [0] * (len(num1) + len(num2))
            
            # Reverse both strings to make indexing easier
            # We'll process from least significant digit
            num1 = num1[::-1]
            num2 = num2[::-1]
            
            # Multiply each digit of num1 with each digit of num2
            for i in range(len(num1)):
                for j in range(len(num2)):
                    # Convert characters to integers
                    digit1 = ord(num1[i]) - ord('0')
                    digit2 = ord(num2[j]) - ord('0')
                    
                    # Multiply digits and add to appropriate position
                    product = digit1 * digit2
                    
                    # Add to existing value at position i+j
                    result[i + j] += product
                    
                    # Handle carry
                    if result[i + j] >= 10:
                        carry = result[i + j] // 10
                        result[i + j] %= 10
                        result[i + j + 1] += carry
            
            # Convert result array back to string
            # Remove leading zeros and reverse
            while len(result) > 1 and result[-1] == 0:
                result.pop()
            
            # Convert to string and reverse back
            return ''.join(str(digit) for digit in result[::-1])