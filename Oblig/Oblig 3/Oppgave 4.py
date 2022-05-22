

def calculate_omkrets(length, width):
    omkrets = float((length * 2) + (width * 2))
    return omkrets

lengthinput = float(input("input length: "))
widthinput = float(input("input width: "))

print(calculate_omkrets(lengthinput, widthinput))
for fi in range(25):
    print(fi)


#print(calculate_omkrets(1,5))