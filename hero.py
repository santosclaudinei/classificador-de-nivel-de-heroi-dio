hero_name = input("Enter the hero's name: ")
amount_experience = int(input("Enter the amount's experience: "))

if amount_experience <= 1000:
    level = "Iron"
elif 1001 <= amount_experience <= 2000:
    level = "Bronze"
elif 2001 <= amount_experience <= 5000:
    level = "Silver"
elif 6001 <= amount_experience <= 7000:
    level = "Gold"
elif 7001 <= amount_experience <= 8000:
    level = "Platinum"
elif 8001 <= amount_experience <= 9000:
    level = "Ascending"
elif 9001 <= amount_experience <= 10000:
    level = "Immortal"
else:
    level = "Radiant"

print(f"The hero's name is {hero_name} is in level {level}.")