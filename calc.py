def level_calculate(victories, defeats):
    winning_balance = victories - defeats

    if victories < 10:
        level = "Iron"
    elif 11 <= victories <= 20:
        level = "Bronze"
    elif 21 <= victories <= 50:
        level = "Silver"
    elif 51 <= victories <= 80:
        level = "Gold"
    elif 81 <= victories <= 90:
        level = "Diamond"
    elif 91 <= victories <= 100:
        level = "Legendary"
    else:
        level = "Immortal"

    message = f"The hero has a balance of {winning_balance} and is in level {level}."
    return message


victories = int(input("Enter the number of victories: "))
defeats = int(input("Enter the number of defeats: "))

result = level_calculate(victories, defeats)
print(result)
