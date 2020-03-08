

import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = wpilib.Spark(0)#pwm 0
        self.right_motor = wpilib.Spark(1)#pwm 1
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.joystick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.forwardLimitSwitch = wpilib.DigitalInput(3)#pwm 3
        self.reverseLimitSwitch = wpilib.DigitalInput(4)#pwm 4
        self.arm = wpilib.Spark(5,6)#pwm 5 and 6
      
        self.spinner1 = wpilib.Jaguar(2)#pwm 2
        
       
        self.toggle = (self.joystick, 1)

   

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.joystick.getY(), self.joystick.getX())
        if self.joystick.getRawButton(5):
            self.spinner1.set(1)
        else:
            self.spinner1.set(0)
       
        




if __name__ == "__main__":
    wpilib.run(MyRobot)
