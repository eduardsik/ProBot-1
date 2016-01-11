import pygame
import ZMQCommunication
import LowPassFilter

Pub=ZMQCommunication.Publisher()
LPF=LowPassFilter.LowPassFilter()



# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255, 0, 0)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printf(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def printf2(self, screen, textString):
        textBitmap = self.font.render(textString, True, RED)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("ProBot Joystick")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    
    # For each joystick:
    for i in range(joystick_count):
        	joystick = pygame.joystick.Joystick(i)
        	joystick.init()
    
        	# Get the name from the OS for the controller/joystick
        	name = joystick.get_name()
        	textPrint.indent() 
        	textPrint.indent()
        	textPrint.indent()
       		textPrint.indent() 
       		textPrint.indent()
       		textPrint.indent()
       		textPrint.indent() 
       		textPrint.indent()
       		textPrint.indent() 
       		textPrint.indent() 
       		textPrint.indent()
       		textPrint.indent()
       		textPrint.indent() 
        	textPrint.indent() 
        	textPrint.printf(screen, "{}".format(name) )
       		textPrint.printf(screen, "")

        
        	axis1 = joystick.get_axis( 1 )
        	axis2 = joystick.get_axis( 2 )

       		textPrint.unindent()
       		textPrint.unindent()
        	textPrint.unindent()
        	textPrint.unindent()
        	textPrint.unindent()
        	textPrint.printf(screen, "")

        	directionForward=0
        	directionReverse=0
        	directionLeft=0	
        	directionRight=0

        	directionForwardReverse=float(axis1)
        	if directionForwardReverse<0:
        		directionForward=-directionForwardReverse
        		directionReverse=0
        		textPrint.printf2(screen, "{:>6.3f}".format(directionForward))
        		textPrint.printf(screen, "")
        		textPrint.printf2(screen, "FORWARD")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "REVERSE")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "{:>6.3f}".format(directionReverse))
		
       		elif directionForwardReverse>0:
        		directionForward=0
        		directionReverse=directionForwardReverse
        		textPrint.printf(screen, "{:>6.3f}".format(directionForward))
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "FORWARD")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "")
        		textPrint.printf2(screen, "REVERSE")
        		textPrint.printf(screen, "")
        		textPrint.printf2(screen, "{:>6.3f}".format(directionReverse))
		
       		elif directionForwardReverse==0:
       			directionForward=0
       			directionReverse=0		
       			textPrint.printf(screen, "{:>6.3f}".format(directionForward))
       			textPrint.printf(screen, "")
       			textPrint.printf(screen, "FORWARD")
       			textPrint.printf(screen, "")
       			textPrint.printf(screen, "")
       			textPrint.printf(screen, "REVERSE")
       			textPrint.printf(screen, "")
       			textPrint.printf(screen, "{:>6.3f}".format(directionReverse))
		


        	textPrint.printf(screen, "")
        	textPrint.printf(screen, "")
        	textPrint.printf(screen, "")


        	directionLeftTRight=float(axis2)
        	if directionLeftTRight<0:
        		directionLeft=-directionLeftTRight
        		directionRight=0
        		textPrint.printf2(screen, "{:>6.3f}".format(directionLeft))
        		textPrint.printf(screen, "")
        		textPrint.printf2(screen, " LEFT")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "RIGHT")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "{:>6.3f}".format(directionRight))
		
        	elif directionLeftTRight>0:
        		directionLeft=0
        		directionRight=directionLeftTRight
        		textPrint.printf(screen, "{:>6.3f}".format(directionLeft))
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, " LEFT")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "")
        		textPrint.printf2(screen, "RIGHT")
        		textPrint.printf(screen, "")
        		textPrint.printf2(screen, "{:>6.3f}".format(directionRight))
		
       		elif directionLeftTRight==0:
        		directionLeft=0
        		directionRight=0		
        		textPrint.printf(screen, "{:>6.3f}".format(directionLeft))
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, " LEFT")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "RIGHT")
        		textPrint.printf(screen, "")
        		textPrint.printf(screen, "{:>6.3f}".format(directionRight))
		
		
		FilteredValuesFR=LPF.lowPassFilterFR(directionForward,directionReverse)
		FilteredValuesLR=LPF.lowPassFilterLR(directionLeft,directionRight)
		Publisher=Pub.publisher(FilteredValuesFR[0],FilteredValuesFR[1],FilteredValuesLR[0],FilteredValuesLR[1])
		
		# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    		# Go ahead and update the screen with what we've drawn.
    		pygame.display.flip()

    		# Limit to 20 frames per second
   		clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
