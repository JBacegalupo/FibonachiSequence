# variable declaration
CurrentNum = 1
PreviousNum = 0
temp = 0
counter = 1
# asks the user what fibonachi number they would like to work out and convert it to an integer
print("please enter the fibonnaci number you would like to find")
AmountOfTimes = input()
AmountOfTimes = int(AmountOfTimes)
# a while loop to work out the the next number in the fibonachi sequence
while counter <= AmountOfTimes:
 temp = PreviousNum
 PreviousNum = CurrentNum
 CurrentNum = temp + CurrentNum
 counter = counter + 1
 # breaks the loop when the desired number is found
 if counter >= AmountOfTimes:
  break
# tells the user the value of the desired fibonachi number
print("the " + str(AmountOfTimes) + " Fibbonachi number is " + str(CurrentNum))
