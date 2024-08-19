def quadrants(x,y):
    if x==0 and y==0:
        print("Origin")
    elif x<0:
        if y==0:
            print("Negative X axis")
        elif y>0:
            print("2nd Quandrant")
        else:
            print("3rd Quandrant")
    elif y<0:
        if x==0:
            print("Negative Y axis")
        else:
            print("4th Quadrant") 
    else:
        if x==0 and y>0:
            print("Positive Y axis")
        elif y==0 and x>0:
            print("Positive X axis")
        else:
            print("1st Quandrant")

# Test cases
quadrants(0, 0)       # Origin
quadrants(0, 5)       # Positive Y axis
quadrants(0, -5)      # Negative Y axis
quadrants(5, 0)       # Positive X axis
quadrants(-5, 0)      # Negative X axis
quadrants(5, 5)       # 1st Quadrant
quadrants(-5, 5)      # 2nd Quadrant
quadrants(-5, -5)     # 3rd Quadrant
quadrants(5, -5)      # 4th Quadrant