''' Problem 2 '''
# Define the main function)
def main():

    awardPoint()  # Call the awardPoint function

# Define the awardPoint function
def awardPoint():
   #Get the number of purchased book in this month from user
   books = int(input("How many books have you purchased in this month?: "))

   #Decide how many points give to user as a reward point
   #if entered value is not in range, print error message
   if books < 0:
       print("Enter a valid amount of books")

   # if number of purchased books under 2 books, grant 0 points
   elif books >= 0 and books <2:
       print(f"You purchased {books} books.")
       print("You earn 0 points.")

   # if the number of purchased books is between 2 and 3, grant 5 points
   elif books >= 2 and books < 4:
       print(f"You purchased {books} books.")
       print("You earn 5 points.")

   # if the number of purchased books is between 4 and 5, grant 15 points
   elif books >= 4 and books < 6 :
       print(f"You purchased {books} books.")
       print("You earn 15 points.")

   # if the number of purchased books is between 6 and 7, grant 30 points
   elif books >= 6 and books < 8:
       print(f"You purchased {books} books.")
       print("You earn 30 points.")

   # if the number of purchased books is over 8, grant 60 points
   else:
       print(f"You purchased {books} books.")
       print("You earn 60 points.")

# Execute the main function
main()
