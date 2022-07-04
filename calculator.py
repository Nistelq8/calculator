

# def main():
# 	#write your code here
# 	firstnumber = input("Whats the first number ?")
# 	secondnumber = input("Whats the second number?")
# 	operation = input("Choose an operation")
# if operation == "*":
#     answer = firstnumber * secondnumber
#    	print(f'{firstnumber}*{secondnumber}={answer}')
# elif operation == "/":
# 	answer = firstnumber / secondnumber
# 	print(f'{firstnumber}/{secondnumber}={answer}')
# elif operation == "+":
#    	answer = firstnumber + secondnumber
# 	print(f'{firstnumber}+{secondnumber}+{answer}')
# elif operation == "-":
#  	answer = firstnumber - secondnumber
# 	print(f'{firstnumber}-{secondnumber}+{answer}')
# else 
# 	return none

# if __name__ == '__main__':
# 	main()





def main():
    #write your code here

    FirstNumber= input("Enter first number: ")
    SecondNumber= input("Enter second number: ")
    operation= input("Choose the operation (+, -, /, ): ")

    if FirstNumber.isdigit() and SecondNumber.isdigit():
        FirstNumber= int(FirstNumber)
        SecondNumber= int(SecondNumber)
        operation= operation
    else:
        print("the numbers were invalid")
        return FirstNumber, SecondNumber, operation

    if operation == "+":
        sum= FirstNumber + SecondNumber
        print(f"The answer is : {sum}")
    elif operation == "-":
        sub= FirstNumber - SecondNumber
        print(f"The answer is : {sub}")
    elif operation == "/":
        div= FirstNumber / SecondNumber
        print(f"The answer is : {div}")
    elif operation == "":
        mul= FirstNumber * SecondNumber
        print(f"The answer is : {mul}")
    else: 
        print("operation is not valid")






if __name__ == '__main__':
    main()