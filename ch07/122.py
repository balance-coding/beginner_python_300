score = input("score: ")
rating = ""
if 81 <= int(score) <= 100:
    rating = "A"
elif 61 <= int(score) <= 80:
    rating = "B"
elif 41 <= int(score) <= 60:
    rating = "C"
elif 21 <= int(score) <= 40:
    rating = "D"
else:
    rating = "E"

print("grade is", rating)

