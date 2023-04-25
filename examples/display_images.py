# Example of Display images
# Download and save EnkPi_2in9.py, pics.py file in Pico W of EnkPi from github -> https://github.com/sbcshop/EnkPi_2.9_Software/tree/main/lib
import EnkPi_2in9 as epd  # to include this library save EnkPi_2in9.py file in EnkPi
import time
import pics # to include this library save pics.py file in EnkPi

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)
    
e_paper.imagered.blit(pics.sb_logo ,0,0) # print sb components logo
e_paper.display()

e_paper.sleep()

