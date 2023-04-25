# Example of display pattern
import EnkPi_2in9 as epd
import time

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)

#loop to generate rectangular pattern
for k in range(0, 6):
    for j in range(0, 6):
        for i in range(0, 50):
            e_paper.imageblack.fill_rect(0+20+j*40, i*2+k*60, 10, 5, 0x00)
        for i in range(0, 50):
            e_paper.imagered.fill_rect(0+10+j*20, i*20+10+k*60, 10, 5, 0xff)
            
e_paper.display()

print("sleep")
e_paper.sleep()

