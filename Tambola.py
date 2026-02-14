import random
def generate_ticket():
    ticket = [[0 for _ in range(9)] for _ in range(3)]

    numbers = list(range(1, 91))
    random.shuffle(numbers)

    index = 0
    for col in range(9):
        count = random.randint(1, 2)  
        for _ in range(count):
            row = random.randint(0, 2)
            while ticket[row][col] != 0:
                row = random.randint(0, 2)
            ticket[row][col] = numbers[index]
            index += 1

    for col in range(9):
        col_nums = []
        for row in range(3):
            if ticket[row][col] != 0:
                col_nums.append(ticket[row][col])
        col_nums.sort()
        r = 0
        for row in range(3):
            if ticket[row][col] != 0:
                ticket[row][col] = col_nums[r]
                r += 1

    return ticket


def print_ticket(ticket):
    print("\nYour Tambola Ticket:\n")
    for row in ticket:
        for num in row:
            if num == 0:
                print("  ", end="\t")
            else:
                print(num, end="\t")
        print()
    print()


def mark_number(ticket, number):
    for row in range(3):
        for col in range(9):
            if ticket[row][col] == number:
                ticket[row][col] = "X"



def check_winner(ticket):
    # Early Five
    count = sum(row.count("X") for row in ticket)
    if count >= 5:
        print("🎉 Early Five Completed!")

    # Top Line
    if all(cell == "X" or cell == 0 for cell in ticket[0]):
        print("🏆 Top Line Completed!")

    # Middle Line
    if all(cell == "X" or cell == 0 for cell in ticket[1]):
        print("🏆 Middle Line Completed!")

    # Bottom Line
    if all(cell == "X" or cell == 0 for cell in ticket[2]):
        print("🏆 Bottom Line Completed!")

    # Full House
    if all(cell == "X" or cell == 0 for row in ticket for cell in row):
        print("🎊 Full House Completed!")
        return True

    return False


def play_tambola():
    ticket = generate_ticket()
    print_ticket(ticket)

    numbers = list(range(1, 91))
    random.shuffle(numbers)

    print("Game Started! 🎯\n")

    for number in numbers:
        input(f"Press Enter to call next number...")
        print(f"Number Called: {number}")

        mark_number(ticket, number)
        print_ticket(ticket)

        if check_winner(ticket):
            print("🎉 Game Over! 🎉")
            break


play_tambola()
