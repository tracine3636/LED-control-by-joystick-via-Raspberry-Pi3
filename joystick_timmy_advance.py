import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)

import pygame


pygame.init()

clock = pygame.time.Clock()

FPS = 30

running = True



#basic do joystick

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)

joystick.init()

screen = pygame.display.set_mode((400,300))

pygame.display.set_caption('Control')





while running:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False

    clock.tick(FPS)

    pygame.display.update()




    verticalaxis = joystick.get_axis(1)

    if verticalaxis < -0.1:

        print('up')

    if verticalaxis > 0.1:

        print('down')

    horizontalaxis = joystick.get_axis(0)

    if horizontalaxis < -0.1:

        print('left')

    if horizontalaxis > 0.1:

         print('right')



    TRIANGLE = joystick.get_button(0)

    CIRCLE = joystick.get_button(1)

    X = joystick.get_button(2)

    SQUARE  = joystick.get_button(3)

    L1 = joystick.get_button(4)

    L2 = joystick.get_button(4)

    R1 = joystick.get_button(6)

    R2 = joystick.get_button(7)

    SELECT = joystick.get_button(8)

    START = joystick.get_button(9)

    L3 = joystick.get_button(10)

    R3 = joystick.get_button(11)


    if X:


        print ('FIRE')

    if X:

        GPIO.output(15, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(15, GPIO.LOW)

    if SQUARE:

        print ("MISSLE")


    if SQUARE:

        GPIO.output(18, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(18, GPIO.LOW)


    if TRIANGLE:

        print ("NUKE")

    if TRIANGLE:

        GPIO.output(20, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(20, GPIO.LOW)

        GPIO.output(20, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(20, GPIO.LOW)

        GPIO.output(20, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(20, GPIO.LOW)


    if CIRCLE:

        print ("EM PULSE")

    if CIRCLE:

        GPIO.output(7, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(7, GPIO.LOW)

        GPIO.output(7, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(7, GPIO.LOW)

        GPIO.output(7, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(7, GPIO.LOW)

        GPIO.output(7, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(7, GPIO.LOW)

        GPIO.output(7, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(7, GPIO.LOW)

        GPIO.output(7, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(7, GPIO.LOW)






pygame.quit()

