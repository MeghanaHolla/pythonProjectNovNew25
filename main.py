class Car:
    number_Of_Cars = 10
    colorOfMyCar = "Red"

    def addNumbers(self,num1,num2,*extraNumbers):
        sum = num1 + num2
        for numbers in extraNumbers:
            sum = sum +numbers
        print (sum)


    def subtractNumbers(self,num1,num2):
        diff = num1 - num2
        print(diff)
    def multiplyNumbers(self,num1,num2):
        product = num1 * num2
        print(product)
    def divideNumbers(self,num1,num2):
        div = num1/num2
        print(div)
