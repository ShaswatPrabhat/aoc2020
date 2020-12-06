
def calc_seat_id(boarding_pass):
    return 8 * int(boarding_pass[:-3], 2) + int(boarding_pass[-3:], 2)

def solve():
    seatIDs = []

    for seat_num in open('input_real.txt', 'r'):
        temp = seat_num.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        row = int(temp[0: 7], 2)
        col = int(temp[7: 10], 2)
        seatIDs.append(row * 8 + col)

    seatIDs.sort()
    t = seatIDs[0]

    print("Highest Seat ID: ", seatIDs[-1])

    for i in seatIDs:
        if t != i:
            print("Your seat is:", t)
            break
        t += 1

if __name__ == '__main__':
    solve()
    # print(get_row_id('FFFBBB'))
