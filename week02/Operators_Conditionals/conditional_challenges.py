#Create a variable named temperature. if its greater than 80, print "It's hot!"

temperature = int(input("Enter the temperature: "))

if temperature >80:
    print("It's hot!")
    
# Create a variable named score. If the score is 70 or higher, print "You passed!"; otherwise, print "you need to study more.""

score = int(input("Enter your score: "))

if score >=70:
    print(" You passed!")
else:
    print("You need to study more!")

# Create a variable named grade. Use if, elif, and else to print: "A" for 90 or above, "B" for 80–89, "C" for 70–79, etc. 

grade = int(input("Enter your grade: "))
if grade >=90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
elif grade >=60:
    print("D")
else:
    print("F")
    

# Challenge: Create variables age and has_license. If the person is at least 16 and has a license, print "You can drive."

age = int(input("Enter your age: "))
has_license = input("Do you have a drivers license? (Yes/no): ")
if age>=16 and has_license =="yes":
    print("You can drive!")
    

# Challenge: Create a variable day. If it is "Saturday" or "Sunday", print "It's the weekend!"

day = input("What day is it? ").strip().lower()

if day in ["saturday", "sunday"]:
    print("It's the weekend!")