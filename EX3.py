array = ["A","B","C","E","F"]
array2 = []
print("-----------------------------------------")
print("               Array                    ")
print("-----------------------------------------")
print("     Index        |       Stack     |")
print("-----------------------------------------")
for i in range(len(array)):
    print(f"       {i}         ","|",f"        {array[i]}      ","|")

print("-----------------------------------------")

array.pop()
array.pop()
array.pop()
array.pop()
array.pop()

array2.append("F")
array2.append("E")
array2.append("C")
array2.append("B")
array2.append("A")

print("-----------------------------------------")
print("               Array2                    ")
print("-----------------------------------------")
print("     Index        |       Stack     |")
print("-----------------------------------------")
for i in range(len(array2)):
    print(f"       {i}         ","|",f"        {array2[i]}      ","|")

print("-----------------------------------------")