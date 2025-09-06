# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    t=float(input("Enter time here (in seconds):"))
    h0=float(input("Enter initial height here (in meters):"))
    g=9.8 #acceleration due to gravity (m/s^s)
    h=h0-0.5*g*t**2 # calculate height
    h=max(h, 0) #height cannot be negative
    hr=round(h,1) # height rounded to one decimal
    print("The height is", hr,"meters.")
        
# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    t=float(input("Enter time here (in seconds):"))
    speed=float(input("Enter speed here (in m/s):"))
    distance=speed*t
    print("The distance is", distance,"meters.")
