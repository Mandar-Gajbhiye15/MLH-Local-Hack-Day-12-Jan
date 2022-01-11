print("Enter total bill amount")
bill = float(input())
print("enter no. of persons")
persons = int(input())
#since no extra details are given we are assuming that the bill would be split equally
Amount = (bill / persons)
round(Amount,2)
print("The amount to be paid by each person is {:0.2f}".format(Amount))