# Property of NoviX Development
# https://nsic.dev/

import random

# Generate a random number
random_num = random.randint(1,9)

# Variables
name = ""
question = ""
answer = ''

# Print the number generated (Testing)
#print(random_num)

# Based on the number generated, set var answer to the corresponding response
if random_num == 1:
  answer = "Yes - definitely"
elif random_num == 2:
  answer = "It is decidedly so"
elif random_num == 3:
  answer = "Without a doubt"
elif random_num == 4:
  answer = "Reply hazy, try again"
elif random_num == 5:
  answer = "Ask again later"
elif random_num == 6:
  answer = "Better not tell you now"
elif random_num == 7:
  answer = "My sources say no"
elif random_num == 8:
  answer = "Outlook not so good"
elif random_num == 9:
  answer = "Very doubtful"
else:
  answer = "ERR"

# Display everything
if len(question) > 0:
  if len(name)== 0:
    print("Question: " + question)
  else:
    print(str(name) + " asks, " + question)
  print("The 8 ball says, " + str(answer))
else:
  print("You didnt ask me nothin foo!")