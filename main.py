Welcome = "Welcome to my computer quiz!"
print(Welcome)

playing = input("Do you want to play? ")
print(playing)

score = 0

if playing.lower() != "yes":
    quit()

print("okay! Let's play :)")

answer = input("what does CPU stand for? ")

if answer.lower() == ("central processing unit"):
    print("Thumbs up, you have a correct answer!")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does FIFO stand for? ")

if answer.lower() == ("first in first out"):
    print("Thumbs up, you have a correct answer!")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does RAM stand for? ")

if answer.lower() == ("random access memory"):
    print("Thumbs up, you have a correct answer!")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does CLI stand for? ")

if answer.lower() == ("command line interface"):
    print("Thumbs up, you have a correct answer!")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does GUI stand for? ")

if answer.lower() == ("graphics user interface"):
    print("Thumbs up, you have a correct answer!")
    score += 1
else:
    print("Incorrect answer")

print("Your score is",(score/5 * 100),"%","You got", score, "answers correctly ")
print("Thank you for participating, this is the end of the game!")
