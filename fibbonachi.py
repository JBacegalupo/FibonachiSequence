# variable declaration
CurrentNum = 1
PreviousNum = 0
temp = 0
counter = 1
# asks the user what Fibonacci number they would like to work out and convert it to an integer
print("please enter the Fibonacci number you would like to find")
AmountOfTimes = input()
AmountOfTimes = int(AmountOfTimes)
# a while loop to work out the next number in the Fibonacci sequence
while counter <= AmountOfTimes:
 temp = PreviousNum
 PreviousNum = CurrentNum
 CurrentNum = temp + CurrentNum
 counter = counter + 1
 # breaks the loop when the desired number is found
 if counter >= AmountOfTimes:
  break
# tells the user the value of the desired Fibonacci number
print("the " + str(AmountOfTimes) + " Fibonacci number is " + str(CurrentNum))
