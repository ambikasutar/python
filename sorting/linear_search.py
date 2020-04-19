def search(numbers, findNo):
    counter = 0
    if type(numbers) is list and len(numbers) > 0:
        for i in numbers:
            if i == findNo:
                print(f"Number is found at {counter} index position.")
                break
            elif counter == len(numbers)-1:
                print("Number is not found.")
            counter += 1        
    else:
        print("Number is not found.")



if __name__ == "__main__":
    numbers = list(map(int,input("Enter list:\n").split()))
    findNo = int(input("Enter number to find:\n"))
    search(numbers, findNo)
