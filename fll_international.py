from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Main hub initialization
hub = PrimeHub()
hub.system.set_stop_button(Button.LEFT)  # LEFT button acts as an emergency stop

# --- Hardware Configuration ---
# Motor definitions: Left (Port B, counterclockwise), Right (Port F)
motor_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.F)

# Attachment motors
motorE = Motor(Port.E)
motorA = Motor(Port.A)

# Color sensors for line following or field detection
color_right = ColorSensor(Port.C)
color_left = ColorSensor(Port.D)

# Chassis settings (in millimeters)
wheel_diameter = 56
axle_track = 117
robot = DriveBase(motor_left, motor_right, wheel_diameter, axle_track)
robot.use_gyro(True) # Use gyroscope for precise turns

# Speed and acceleration settings
robot.settings(
    straight_speed=500,        # Robot speed on straight lines
    straight_acceleration=600, # Acceleration on straight lines
    turn_rate=400,             # Robot turning speed
    turn_acceleration=500      # Turning acceleration
)

# --- Helper Movement Functions ---

def move_forward(distance_mm):
    """Move forward/backward a precise distance."""
    robot.straight(distance_mm, then=Stop.BRAKE, wait=True)
    wait(100)

def turn(angle_degrees):
    """Turn a precise degree using the gyroscope."""
    robot.turn(angle_degrees, then=Stop.BRAKE, wait=True)
    wait(100)

def strong_move_left(power, time_ms):
    """Direct control of Motor E using power (DC)."""
    motorE.reset_angle(None)
    motorE.dc(power)
    wait(time_ms)
    motorE.stop()
    wait(50)

def strong_move(power, time_ms):
    """Direct control of Motor A using power (DC)."""
    motorA.reset_angle(None)
    motorA.dc(power)
    wait(time_ms)
    motorA.stop()
    wait(50)

def arc(speed_left, speed_right, duration_ms):
    """Movement in an arc by setting power to both motors."""
    motor_left.dc(speed_left)
    motor_right.dc(speed_right)
    wait(duration_ms)
    motor_left.stop()
    motor_right.stop()
    wait(10)

def reset_motors():
    """Reset the rotation angles of all motors."""
    motorA.reset_angle(None)
    motor_left.reset_angle(None)
    motorE.reset_angle(None)
    motor_right.reset_angle(None)
    wait(10)

# --- MISSIONS (RUNS) ---

def run_1():
    """First run: Missions 5, 6, 7, 8. Points: 120."""
    
    reset_motors()
    move_forward(425)
    turn(26)
    # Outputting the gears.
    for i in range(2):
        strong_move(-100, 300)
        strong_move(100, 300)
        wait(50)
    strong_move(-100, 300)
    strong_move(100, 300)
    turn(-28)
    move_forward(260)
    turn(-45)
    move_forward(40)
    
    move_forward(-125)
    turn(-45)
    move_forward(-150)
    
    motorE.run_angle(600,-120,Stop.BRAKE,wait=True)
    #move_forward(20)
    motorE.run_angle(700,110,Stop.BRAKE,wait=True)
    
    #move_forward(80)
    arc(50,100,1200)
    move_forward(600)
    
    """
    Experimental logic:
    turn(21)
    # Outputting the gears.
    for i in range(2):
        strong_move(-100, 300)
        strong_move(100, 300)
        wait(100)
    strong_move(-100, 300)
    strong_move(35, 300)
    turn(-25)
    move_forward(280) # Releasing the stones
    strong_move(40, 500)
    move_forward(25)
    turn(-25) # Pushing the axle for mission 5
    move_forward(-75)
    turn(-72)
    move_forward(-120)
    strong_move_left(80, 550) 
    move_forward(-130) # Collecting stones and the large artifact
    strong_move_left(-120, 550)
    arc(60,100,2300) # Arc turn and partial execution of mission 9
    """
    stop()

def run_2():
    """Second run: Missions 9, 11. Points: 60."""
    move_forward(490)
    turn(-19)
    move_forward(70)
    turn(9)
    move_forward(20)
    strong_move_left(-300,1300)
    move_forward(-390)
    
    turn(60)

    move_forward(190)
    turn(-57)
    turn(50)
    strong_move(-100,200)
    move_forward(-150)
    move_forward(100)
    strong_move(100,200)
    move_forward(-500)
    stop()

def run_3():
    """Third run: Missions 10, 13. Points: 60."""
    move_forward(560)
    turn(90)
    move_forward(155)
    # Pushing the mast
    motorE.run_angle(speed=500, rotation_angle=130, wait=True)
    motorE.run_angle(speed=500, rotation_angle=-130, wait=True)
    move_forward(-115) # Collecting the artifact from mission 9
    turn(-135)
    turn(70)
    move_forward(106)
    motorA.run_angle(speed=500, rotation_angle=-150, wait=True)
    move_forward(320)
    motorA.run_angle(speed=300, rotation_angle=65, wait=True)
    turn(30)
    turn(-45)
    move_forward(-100) # Raising the skeleton
    turn(-37)
    move_forward(800)
    stop()

def run_4():
    """Fourth run: Missions 1, 2. Points: 60."""
    reset_motors()
    move_forward(650)
    wait(300)
    move_forward(-260) # Executing mission 1 by taking the broom
    turn(12)
    move_forward(280)
    turn(-57)
    #motorA.run_angle(500, -150)
    move_forward(145)
    turn(12)
    move_forward(-40)
    motorA.run_angle(500, 70) # Uncovering the map 
    move_forward(-70)
    arc(-65, -100, 2050)
    stop()

def run_5():
    """Fifth run: Missions 3, 4. Points: 60."""
    # Reverse parking between mission 2 and 4
    move_forward(640)
    turn(92)
    move_forward(350)
    turn(45)
    move_forward(-300)
    turn(-48)
    # Lowering part of the attachment to send the train to the other team
    motorA.run_angle(100,-145,then=Stop.BRAKE,wait=True)
    move_forward(130)
    # Using gears to "hug" the artifact
    motorE.run_angle(500,390,then=Stop.BRAKE,wait=True)
    # Sending the train
    motorA.run_angle(100,145,then=Stop.BRAKE,wait=True)
    turn(4)
    move_forward(-110)
    turn(45)
    move_forward(210)
    # Return to base with a "drift"
    arc(-90,-30,900)
    move_forward(-800)

def run_6():
    """Sixth run: Missions 12, 15. Points: 40."""
    move_forward(600) # Pushing the ship
    motorA.run_angle(500, -100) # Leaving the flag
    move_forward(-50)
    motorA.run_angle(300, 30) # Pulling the sand
    move_forward(-490)
    stop()

def run_7():
    """Seventh run: Mission 14. Points: 30."""
    # Dropping off all artifacts 
    move_forward(155)
    turn(50)  
    move_forward(270)
    move_forward(-200)
    turn(-41)
    move_forward(410)
    stop()
    """
    Experimental logic:
    turn(-30)
    move_forward(500)
    turn(-13)
    """

def run_8():
    """Eighth run: Missions 14, 15. Points: 25."""
    reset_motors()
    move_forward(550)
    turn(-50)
    move_forward(830)
    turn(-54)
    move_forward(100)
    #motorA.run_angle(500,-150,then=Stop.BRAKE,wait=True)
    move_forward(-130)
    turn(-92)
    move_forward(810)
    turn(-15)
    stop()
    """
    Experimental logic:
    move_forward(550)
    turn(-75)
    move_forward(100)
    motorA.run_angle(500,300,then=Stop.BRAKE,wait=True)
    move_forward(-50)
    turn(75)
    move_forward(270)
    turn(-50)
    move_forward(80)
    turn(-40)
    move_forward(100)
    motorA.run_angle(100,145,Stop,True)
    move_forward(-150)
    turn(-92)
    move_forward(600)
    turn(45)
    """

# --- MENU SYSTEM ---
# Allows program selection via Hub buttons
button = 1
prev_pressed = []
hub.display.number(button) # Displays the selected program number

while True:
    pressed = hub.buttons.pressed()
 
    # Change program number with the RIGHT button
    if Button.RIGHT in pressed and Button.RIGHT not in prev_pressed:
        button += 1
        if button > 8: # Reset to 1 if it exceeds 8
            button = 1
        hub.display.number(button)

    # Start the selected program with the CENTER button
    elif Button.CENTER in pressed and Button.CENTER not in prev_pressed:
        if button == 1: run_1()
        elif button == 2: run_2()
        elif button == 3: run_3()
        elif button == 4: run_4()
        elif button == 5: run_5()
        elif button == 6: run_6()
        elif button == 7: run_7()
        elif button == 8: run_8()
        # Display the number again after finishing a mission
        hub.display.number(button)

    prev_pressed = pressed
    wait(100) # Small wait for loop stability