import time
def hello(name):
    print("Hej " + name)

counter=1
while counter < 1000:
    hello("William " + str(counter))
    counter = counter + 1