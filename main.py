def main():
    x = int(input('Enter a number for x-coordinate: '))
    y = int(input('Enter a number for y-coordinate: '))

if (x > 0) and (y>0):
    quadrant = 1

    print(f'Quadrant: {quadrant}')
    ########################################
    # Do not delete the return statement
    ########################################
    return quadrant


if __name__ == '__main__':
    main()
