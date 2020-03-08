#MADE BY FRC 7210 ROBOJACKETS. Programmers: C.J. Clos

import wpilib 
import wpilib.drive


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        # Drivetrain

        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        # Controller and timer

        self.stick = wpilib.Joystick(1)
        self.timer = wpilib.Timer()
    
    def autonomousInit(self)
        # Reset FRC timer and start it only once every time we enter autonomous mode

        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self)
        # We will call this function periodically durring autonomous(every 20ms?)

        # Drive for 2 seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive foward at half speed
        else:
            self.drive.arcadeDrive(0,0) # Stop!!!!!!!!!!!!

    def teleopPeriodic(self):

