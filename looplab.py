## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205

## 2) Using a while loop and input , do the following :
# Ask the the user : "what is the product of 7 * 24 ?"
# check if the answer is right then exit the loop and print "You answered this Question correctly"
# if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.

for num in range (45,210):
    if num == 100 :
        continue
    elif num == 205 :
        break
    print(num)
product_answer = 168
product_answer : int(input("what is the product of 7 * 24 ? "))
while product_answer != product_answer :
    print("Your Answer is wrong try again..")
else :
   int(input("what is the product of 7 * 24 ? "))
print("You answered this Question correctly")