def print_square(n):
    square = []
    for i in range(n):
        square.append([])
        for j in range(n):
            square[i].append(0)
    s = n*n
    num = 1
    square[(n-1)//2][(n-1)//2] = num
    num += 1
    for layer in range(1, (n+1)//2):
        for index in range(layer):
            if num <= s:
                x = layer
                y = layer - 1 - index
                square[n-1-x][y] = num
                num += 1
            if num <= s:
                x = layer - 1 - index
                y = x
                square[n-1-x][n-1-y] = num
                num += 1
            if num <= s:
                x = layer - 1 - index
                y = layer
                square[x][n-1-y] = num
                num += 1
            if num <= s:
                x = layer
                y = layer - 1 - index
                square[x][y] = num
                num += 1
    for row in square:
        print(' '.join(str(x) for x in row))

def calculate_magic_square(n):
    assert n % 2 == 1, "Magic squares are only possible on odd dimensions."
    magic_square = [[0]*n for _ in range(n)]
    magic_constant = n * (n**2 + 1) // 2
    current_value = 1
    magic_square[n//2][n//2] = current_value
    while current_value < magic_constant:
        next_x = (magic_square[n//2][n//2 - 1] - 1) % n
        next_y = (magic_square[n//2 - 1][n//2] - 1) % n
        if magic_square[next_x][next_y] != 0:
            next_x = (next_x - 1) % n
        magic_square[next_x][next_y] = current_value
        current_value += 1
    return magic_square

def main():
    n = int(input("Enter the size of the magic square: "))
    if n % 2 == 1:
        print_square(n)
    else:
        print("Sorry, but only odd sizes can make a magic square.")

if __name__ == "__main__":
    main()