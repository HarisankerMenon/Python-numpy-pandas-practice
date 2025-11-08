# identity metrix

f1 = open("positive", "r")
for i in f1:
    pdata = i.split(",")

f2 = open("negative", "r")
for i in f2:
    ndata = i.split(",")

review = 0

f = open("review", "r")

for i in f:
    data = i.split(" ")
    print(data)

for i in data:

    if i in pdata:
        review = review + 1
    if i in ndata:
        review = review - 1
    else:
        pass
print("Review=", review)

if (review > 0):
    print("Positive Review")
elif (review < 0):
    print("Negative Review")
else:
    print("Review is neutral")
print(data)
