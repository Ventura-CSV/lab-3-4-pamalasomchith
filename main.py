def main():
    x = int(input('Enter a number for x-coordinate: '))
    y = int(input('Enter a number for y-coordinate: '))
   
    if (int(x) > 0) and (int(y) >0):
        quadrant = 1
    elif (int(x) < 0) and (int(y) > 0):
        quadrant = 2
    elif (int(x) < 0) and (int(y) < 0):
        quadrant = 3
    else:
        quadrant 4
        
    print(f'Quadrant: {quadrant}')
    ########################################
    # Do not delete the return statement
    ########################################
    return quadrant


if __name__ == '__main__':
    main()
