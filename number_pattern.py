def number_pattern(n):
    result = ""

    if not isinstance(n, int):
        return "Argument must be an integer value."
        
    if n <= 0:
        return "Argument must be an integer greater than 0."
    
    for number in range(1,n+1):
        result += str(number) + " "
    return result.strip()
        
    

    

print(number_pattern(4))
print(number_pattern(12))
