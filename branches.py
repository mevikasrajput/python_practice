things = ["apples orange banana crows telephone"]

print("wait there's not ten things")

stuff = things.split('')
more_stuff = ["day","night","morning","song","frisbee","corn","horn","torn","nrn","kr"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print("there's %d items now." % len(stuff))

print("there we go")
print("let's do some good things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.?.join(stuff))
print("#".join(stuff[3:5]))

