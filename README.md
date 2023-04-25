# EnkPi_2.9_Software

### EnkPi is a series of 4 ePaper displays mounted on PCBs to provide sturdiness and comfort to the users.
Powered with **Raspberry Pi Pico W**, these EnkPi boards have Partial Refresh Support with up to 170 degrees Wide Viewing Angle. In this github repo will see setup and getting started guide for EnkPi 2.9" series.

<img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/EnkPi_2_9.jpg" />

<img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/pinout_2_9.png" width= "400" height = "400"/>

## Getting Started with EnkPi
### 1. Step to install boot Firmware
   - Every EnkPi will be provided with boot firmware already installed, so you can directly go to step 2
   - If in any case, you need to install firmware for your board, then you can follow the tutorial [here](https://github.com/sbcshop/PiCoder-Software/blob/main/README.md#1-how-to-install-boot-firmware-in-picoder-kit)

### 2. Testing Pico W on EnkPi
- Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.

- Once done start **Thonny IDE application**,
  - Connect EnkPi with a laptop/PC using a micro USB cable and the micro USB port on Pico W present on EnkPi.
  
  - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
    <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
    <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
   
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run on EnkPi. 
     <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
    Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up EnkPi and it should run your script, go to step 3.
    
### 3. How to shift your script on Pico W of EnkPi
  - Click on File -> Save as Copy -> select Raspberry Pi Pico , Then save file as main.py
   <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr1.jpg" />
   <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr2.jpg" />
   <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr3.jpg" />
   <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr4.jpg" />
   
In similar way you can add various micropython files to Pico. Also to try out sample codes given here in example folder you need to save library files from [lib](https://github.com/sbcshop/EnkPi_2.9_Software/tree/main/lib) folder into Pico W of EnkPi.
To do this follow same steps as shown in step 3 but **to save library file don't change name keep default one -> ** [EnkPi_2in9.py](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/lib/EnkPi_2in9.py), [pics.py](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/lib/pics.py)

### Example Codes
 - 
Now you are ready to try out your own codes, **_Happy Coding!_**

## Related Projects

## Documentation
  * [MicroPython getting started for RPI](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related HAT Products
 ![3vPicoRelayBoard](https://cdn.shopify.com/s/files/1/1217/2104/products/3vPicoRelayBoard.png?v=1617884866&width=200)
 
 * [2 Channel Relay Board](https://shop.sb-components.co.uk/products/pico-3v-relay-hat?_pos=1&_sid=82fa60545&_ss=r) - Compatible Relay Hat for PiCoder 
 
 ![1.14” LCD HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/6_c64376c7-a257-43a3-bb5f-0a9471741a7d.png?v=1624017126&width=200)
 
 * [1.14” LCD HAT](https://shop.sb-components.co.uk/products/1-14-lcd-hat-for-pico?_pos=3&_sid=82fa60545&_ss=r) - Compatible 1.14” LCD HAT for PiCoder 
 
 ![Motor Driver HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/motordriverforPico.png?v=1619523627&width=200)
 
 * [Motor Driver HAT](https://shop.sb-components.co.uk/products/pico-motor-driver?_pos=4&_sid=82fa60545&_ss=r) - Compatible 2 Channel Motor Driver HAT for PiCoder
 
 ![Ethernet_HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/NetPi_4.png?v=1675947155&width=200)
 
 * [Ethernet HAT](https://shop.sb-components.co.uk/products/netpi-ethernet-hat-for-raspberry-pi-pico?_pos=2&_sid=82fa60545&_ss=r) - Compatible Ethernet HAT for PiCoder

 ![Barcode_Reader_HAT](https://cdn.shopify.com/s/files/1/1217/2104/products/04.png?v=1669181209&width=200)
 
 * [Barcode Reader](https://shop.sb-components.co.uk/products/barcode-hat?_pos=5&_sid=82fa60545&_ss=r) - Compatible Barcode Reader HAT for PiCoder
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
