# Example of display text
import EnkPi_2in9 as epd
import time

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0xff)
    
e_paper.imageblack.text("SB COMPONENTS", 5, 10, 0x00) # Text, x, y, color
e_paper.imagered.text("EnkPi 2.9 inch", 5, 40, 0x00)  # Text, x, y, color
e_paper.display()

print("sleep")
e_paper.sleep()



