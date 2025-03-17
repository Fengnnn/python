import math


def find_sequences(n):
    # min is 2p**2
    sqrt_number = int(math.sqrt(n)//2)
    sequences = list()
    # start from  till sqrt_number
   
    for p in range(1,sqrt_number):
        #if m*p**2 == n, m is bigger than the acutal one 
        m = int(n// p**2)
        while True:
            if m ==0:
                break
            m -= 1
            result = sum(p,m)
            if result == n:
                sequences.append([p,m])
            elif result < n: # smaller than n , no need to continue
                break
            
    result = format_output(sequences)
    return result

def format_output(sequences):
    out_put = list()
    out_put.append(len(sequences))
    for sequence in sequences:
        out_array = list()
        m = sequence[1]
        p = sequence[0]
        out_array.append(m+1)
        for i in range(0,m+1):
            out_array.append(p+i)
        
        out_put.append(" ".join(map(str, out_array)))
    return out_put
    
def sum(p,m):
    total = p**2
    for i in range(1,m+1):
       total +=  (p+i)**2

    return total

def find_sequences_2(n):
    sequences = []
    
    for p in range(1, int((n)**0.5) + 1):
        total = 0
        m = 0
        sequence = []
        
        while total < n:
            current = p + m
            total += current ** 2
            sequence.append(current)
            m += 1
        
        if total == n:
            sequences.append(sequence)
    
    # Sort sequences by length in descending order
    sequences.sort(key=lambda x: len(x), reverse=True)
    
    # Prepare the output
    output = [str(len(sequences))]
    for seq in sequences:
        output.append(f"{len(seq)} {' '.join(map(str, seq))}")
    
    return output


def test():
    # Example usage:
    n = 2030
    result = find_sequences(14)
    for line in result:
        print(line)


    assert(len(result)== 0)