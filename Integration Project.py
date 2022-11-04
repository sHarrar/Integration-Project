#Sean Harrar
#NBA2k Calculating stat averages over a certain number of games

#Sprint 1
#Required Elements

#print function greeting
print("Hello!")
#formatting print() output with sep= arguments
totalCost = 100
print("Total cost: $", format(totalCost, "0.2f"), sep='')
#formatting print() output with end= arguments
totalCost = 100
print("Total cost: $", format(totalCost, "0.2f"), end='\n')
#input function
num = (input("Enter a number"))
#basic calculations
#Multiplication
print(5 * 3)
#Division
print(12 / 6)
#Addition
print( 5 + 10)
#Subtraction
print(10 - 5)
#Exponents
print(2 ** 4)
#Floor Division
print(13 // 2)
#Modulus
print(7 % 2)

#Sprint 2 required elements

#shortcut operator
x=5
y=10
x+=y
#if statement #>= operator
value = 100
if value >= 100:
    print("Correct!")
#!= operator
value = 100
if value != 100:
    print("Incorrect")
#if else statement
score = 700
if score >= 700:
    print("New High Score!")
else:
    print("Try Again")
#elif statement #== operator
grade = int(input("Enter your grade: "))
if grade == 100:
    print("Perfect!")
elif grade >= 60:
    print("Good Enough")
else:
    print("Fail")
#Boolean Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)
#While Loop
color = input("Enter your favorite color: ")
t = 0
while(t < 5):
    print(color)
    t = t+ 1
#For Loop #in #range
color = input("Enter your favorite color: ")
for t in range(5):
    print(color)
#Function
import math

def calculateArea(radius):
    return math.pi*radius*radius
def calculateDiameter(radius):
    return 2.0*radius

radius = int(input("Enter the radius: "))
area = calculateArea(radius)
diameter = calculateDiameter(radius)
print(area)
print(diameter)


#integration project starts under this line

#Calculating points average for first 5 games
game1_points = 27
game2_points = 15
game3_points = 10
game4_points = 30
game5_points = 25
total_games = 5
total_points = (game1_points + game2_points + game3_points + game4_points + game5_points)
point_average = (total_points / total_games)
print("Point Average: ", format(point_average, ".2f"), sep='')


#Calculating rebounds average for first 5 games
game1_reb = 11
game2_reb = 7
game3_reb = 17
game4_reb = 22
game5_reb = 5
total_rebounds = (game1_reb + game2_reb + game3_reb + game4_reb + game5_reb)
rebound_average= (total_rebounds / total_games)
print("Rebound Average: ", format(rebound_average, ".2f"), sep='')


#Calculating assists average for first 5 games
game1_assists = 6
game2_assists = 0
game3_assists = 15
game4_assists = 4
game5_assists = 8
total_assists = (game1_assists + game2_assists + game3_assists + game4_assists + game5_assists)
assists_average = (total_assists / total_games)
print("Assist Average: ", format(assists_average, ".2f"), sep='')
