CurrentNum = 1
PreviousNum = 0
temp = 0
counter = 1

print("please enter the fibonnaci number you would like to find")
AmountOfTimes = input()
AmountOfTimes = int(AmountOfTimes)
while counter <= AmountOfTimes:
 temp = PreviousNum
 print(temp)
 PreviousNum = CurrentNum
 print(PreviousNum)
 CurrentNum = temp + CurrentNum
 print(CurrentNum)
 counter = counter + 1
 if counter >= AmountOfTimes:
  break

print("the " + str(AmountOfTimes) + " Fibbonachi number is " + str(CurrentNum))
