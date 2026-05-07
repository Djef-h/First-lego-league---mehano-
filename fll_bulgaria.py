from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Инициализация на главния блок
hub = PrimeHub()
hub.system.set_stop_button(Button.LEFT)  # Бутонът LEFT служи за аварийно спиране

# --- Хардуерна конфигурация ---
# Дефиниране на мотори: ляв (порт F, обърнат), десен (порт B)
motor_left = Motor(Port.F, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.B)
# Допълнителни мотори за прикачен инвентар
motorE = Motor(Port.E)
motorA = Motor(Port.A)
# Сензори за цвят за следене на линии или засичане на полета
color_right = ColorSensor(Port.C)
color_left = ColorSensor(Port.D)

# Настройки на шасито (в милиметри)
wheel_diameter = 56
axle_track = 117
robot = DriveBase(motor_left, motor_right, wheel_diameter, axle_track)
robot.use_gyro(True) # Използване на жироскопа за прецизни завои

# Настройки на скорост и ускорение
robot.settings(
    straight_speed=800, # Скороста на робота на права линия
    straight_acceleration=900, # Ускороние на права линия
    turn_rate=500, # Скороста на робота на завои
    turn_acceleration=600 # Ускорение на завои
)

# --- Помощни функции за движение ---

def move_forward(distance_mm):
    """Движение напред/назад на точно разстояние."""
    robot.straight(distance_mm, then=Stop.BRAKE, wait=True)
    wait(100)

def turn(angle_degrees):
    """Завой на точен градус чрез жироскопа."""
    robot.turn(angle_degrees, then=Stop.BRAKE, wait=True)
    wait(100)

def strong_move_left(power, time_ms):
    """Директно управление на мотор E чрез мощност (DC)."""
    motorE.reset_angle(None)
    motorE.dc(power)
    wait(time_ms)
    motorE.stop()
    wait(50)

def strong_move(power, time_ms):
    """Директно управление на мотор A чрез мощност (DC)."""
    motorA.reset_angle(None)
    motorA.dc(power)
    wait(time_ms)
    motorA.stop()
    wait(50)


def arc(speed_left, speed_right, duration_ms):
    """Движение по дъга чрез задаване на мощност към двата мотора."""
    motor_left.dc(speed_left)
    motor_right.dc(speed_right)
    wait(duration_ms)
    motor_left.stop()
    motor_right.stop()
    wait(10)

def reset_motors():
    """Нулиране на градусите на всички мотори."""
    motorA.reset_angle(None)
    motor_left.reset_angle(None)
    motorE.reset_angle(None)
    motor_right.reset_angle(None)
    wait(10)

# --- МИСИИ (RUNS) ---

def run_1():
    """Първи рън: Мисии 5, 6, 7, 8. Точки: 120."""
    reset_motors()
    move_forward(425)
    turn(21)
    # Изкарване на зъбните колелета.
    for i in range(2):
        strong_move(-100, 300)
        strong_move(100, 300)
        wait(100)
    strong_move(-100, 300)
    strong_move(35, 300)
    turn(-25)
    move_forward(280) # Пускаме камъните
    strong_move(40, 500)
    move_forward(25)
    turn(-25) # Бутаме аксела на 5 мисия
    move_forward(-75)
    turn(-72)
    move_forward(-120)
    strong_move_left(80, 550) 
    move_forward(-130) # Прибираме камъните заедно с големия артефакт
    strong_move_left(-120, 550)
    arc(70, 100, 2650) # Завой с дъга и изпълнение на една част от 9 мисия
    stop()

def run_2():
    """Втори рън: Мисии 9, 11. Точки: 60."""
    move_forward(490)
    turn(-19)
    move_forward(70)
    turn(9)
    move_forward(20)
    strong_move_left(-300,1300)
    move_forward(-390)
    
    turn(60)

    move_forward(200)
    turn(-57)
    turn(50)
    strong_move(-100,200)
    move_forward(-300)
    move_forward(50)
    strong_move(100,200)
    move_forward(-300)
    stop()

"""
    move_forward(650)
    turn(-32)
    move_forward(105)
    turn(17)
    strong_move_left(190, 950) # Вдигаме артефакта с зъбни колелата 
    move_forward(-138)
    turn(110)
    move_forward(146)
    # Бутаме мачтата
    motorA.run_angle(speed=500, rotation_angle=250, wait=True)
    motorA.run_angle(speed=500, rotation_angle=-190, wait=True)
    move_forward(-135) # И взимаме артефакта от 9 мисия
    turn(-68)
    move_forward(120)
    motorA.run_angle(speed=500, rotation_angle=180, wait=True)
    move_forward(240)
    motorA.run_angle(speed=500, rotation_angle=-50, wait=True)
    turn(25) # Вдигаме скелета
    move_forward(-80)
    turn(-52)
    move_forward(300)
    arc(60, 80, 2000)
    stop()
"""
def run_3():
    """Трети рън: Мисии 10, 13. Точки: 60"""
    move_forward(560)
    turn(90)
    move_forward(175)
    # Бутаме мачтата
    motorE.run_angle(speed=500, rotation_angle=130, wait=True)
    motorE.run_angle(speed=500, rotation_angle=-130, wait=True)
    move_forward(-135) # И взимаме артефакта от 9 мисия
    turn(-138)
    turn(74)
    move_forward(126)
    motorA.run_angle(speed=500, rotation_angle=-150, wait=True)
    move_forward(330)
    motorA.run_angle(speed=400, rotation_angle=60, wait=True)
    turn(30)
    turn(-45)
    move_forward(-100) # Вдигаме скелета
    turn(-37)
    move_forward(800)

    #arc(60,100,1000)
    stop()
def run_4():
    """Четвърти рън: Мисии 1, 2. Точки: 60."""
    reset_motors()
    move_forward(510)
    wait(300)
    move_forward(-260) # Изпълнение на 1 мисия, като взимаме метлата
    turn(12)
    move_forward(270)
    turn(-57)
    motorA.run_angle(500, -150)
    move_forward(145)
    turn(6)
    move_forward(-40)
    motorA.run_angle(500, 70) # Откриване на картата 
    move_forward(-70)
    arc(-65, -100, 2050)
    stop()

def run_5():
    """Пети рън: Мисия 3, 4. Точки 60. """
    "Задно паркиране между мисия 2 и 4"
    move_forward(640)
    turn(92)
    move_forward(350)
    turn(45)
    move_forward(-300)
    turn(-48)
    motorA.run_angle(100,-145,then=Stop.BRAKE,wait=True)# Сваляме част от представката за да пратим влака на другия отбор
    move_forward(130)
    motorE.run_angle(500,390,then=Stop.BRAKE,wait=True)# С помощта на зъбни предавки гушкаме артефакта 
    motorA.run_angle(100,145,then=Stop.BRAKE,wait=True)# Пращаме влакчето 
    turn(4)
    move_forward(-110)
    turn(45)
    move_forward(200)
    arc(-90,-30,900)# Прибираме в базата подобаващо(дрифт)
    move_forward(-700)

def run_6():
    """Шести рън: Мисии 12, 15. Точки 40"""
    reset_motors()
    move_forward(600) # Бутаме кораба
    strong_move(-100, 100) # Оставяме знамето n 
    move_forward(-50)
    motorA.run_angle(100, 30) # Дърпаме пясъка
    move_forward(-490)
    stop()

def run_7():
    """Седми рън: Мисии 14. Точки: 30."""
    
    #Оставяне на всички артефакти 
    move_forward(155)
    turn(50)  
    move_forward(270)
    move_forward(-300)
    turn(-30)
    move_forward(500)
    turn(-13)

def run_8():
    """Осми рън: Мисии 14, 15 . Точки: 25."""
    
    reset_motors()
    move_forward(730)
    turn(92)
    move_forward(940)
    turn(-95)
    move_forward(120)
    
    move_forward(-120)
    turn(90)
    move_forward(-490)
    turn(-7)
    move_forward(-380)

# --- МЕНЮ СИСТЕМА ---
# Позволява избор на програма чрез бутоните на Hub-а
button = 1
prev_pressed = []
hub.display.number(button) # Показва номера на избраната програма

while True:
    pressed = hub.buttons.pressed()

    # Смяна на номера на програмата с десния бутон
    if Button.RIGHT in pressed and Button.RIGHT not in prev_pressed:
        button += 1
        if button > 8: # Рестартира от 1, ако надхвърли 8
            button = 1
        hub.display.number(button)

    # Стартиране на избраната програма с централния бутон
    elif Button.CENTER in pressed and Button.CENTER not in prev_pressed:
        if button == 1: run_1()
        elif button == 2: run_2()
        elif button == 3: run_3()
        elif button == 4: run_4()
        elif button == 5: run_5()
        elif button == 6: run_6()
        elif button == 7: run_7()
        elif button == 8: run_8()
        # След приключване на мисията, отново показва номера
        hub.display.number(button)

    prev_pressed = pressed
    wait(100) # Малко изчакване за стабилност на цикъла
