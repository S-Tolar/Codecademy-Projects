# magic 8 ball project
# Important module for generating random numbers
import random
# Set the name of the asker
name = "Seth"
# Set the question to ask
question = "Is this project going to be valuable to me in the future?"
# Generate a random number between 1 and 9
random_number = random.randint(1, 9)
# Initialize answer variable
answer = str()
print(f"{name} asks: {question}")
#print(random_number)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
print(f"Magic 8-Ball answer: {answer}")