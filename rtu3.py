#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python
 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr
 This is distributed under GNU LGPL license, see license.txt
"""

import serial
import datetime
import modbus_tk
import modbus_tk.defines as cst
import csv
import sys
import pygame
from modbus_tk import modbus_rtu


PORT = 'COM7'

#PORT = '/dev/ttyp5'
def Timeclock(i,n,array):
   
    
    currentDT=datetime.datetime.now()
    print(currentDT.minute)
    global Switch
    if (currentDT.hour==0 and currentDT.minute==0 and currentDT.second==0):
                 
        flog=open(str(n)+'.csv','x',newline='')
        return Switch+1
                
    if i>0:
        
        flog=open(str(n)+'.csv','a',newline='')
        writer=csv.writer(flog)
        writer.writerow(array)
        return Switch       
    if i==0:
        Switch=0
        flog=open(str(n)+'.csv','x',newline='')
        return Switch
    
def main():
    """main"""
        #logger = modbus_tk.utils.create_logger("console")
    i=0
    n=0
    
    try:
        #Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        #logger.info("connected")
        resp = input('Нажмите любую клавишу чтобы продолжить')
        x=50
        y=450
        width=5
        height=5
        screen=pygame.display.set_mode((1000,500))
        bg=pygame.image.load('unk.png')
        pygame.display.set_caption("График")
        screen.blit(bg,(0,0))
        switch=True
        
        pygame.init()
        
        font=pygame.font.SysFont('comicsans',15)
  
        while switch==True:
            
           
            array=master.execute(13, cst.READ_HOLDING_REGISTERS, 8, 9)
            print(array)
            #print( "%04x %04x %04x %04x %04x %04x %04x %04x %04x %04x %04x %04x %04x %04x %04x %04x " % array[ 0]), int(array[ 1]), int(array[ 2]), int(array[ 3]), array[ 4]), int(array[ 5]), int(array[ 6]), int(array[ 7]), array[ 8]), int(array[ 9]), int(array[10]), int(array[11]), array[12]), int(array[13]), int(array[14]), int(array[15]) ) )
            #array=master.execute(13, cst.READ_SINGLE_REGISTER, 16)
            switch=True
            x+=30
            #y-=(array[8]/1000)
            a=pygame.time.get_ticks()
           
        
            
            pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
            pygame.draw.rect(screen,(0,255,0),(x,470,2,height))
            pygame.display.update()
            text=font.render(str(array[8]),1,(0,255,0))
            screen.blit(text,(x,480))
            #if (currentDT.hour==0 and currentDT.minute==0 and currentDT.second==0):
                #switch=False
            currentDT=datetime.datetime.now()
            
            
            #if (currentDT.hour==14 and currentDT.minute==1 and currentDT.second==0):
                
            #    n=n+1
            #    flog=open(str(n)+'.csv','x',newline='')
                
            #if i>0:
            #    flog=open(str(n)+'.csv','a',newline='')
            #    writer=csv.writer(flog)
            #    writer.writerow(array)
                
            #if i==0:
            #   flog=open(str(n)+'.csv','x',newline='')
            #i=i+1
             
            #if currentDT.minute<13:
                #flog=open("data.csv",'w',newline='')
                #writer=csv.writer(flog)
                #writer.writerow(array)
            #writer=csv.writer(flog)
            #writer.writerow(array)
            #send some queries
            #logger.info(master.execute(1, cst.READ_COILS, 0, 10))
            #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
            #logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
            #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
            #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
            #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))
            currentDT=datetime.datetime.now()
            if (currentDT.hour==0 and currentDT.minute==0 and currentDT.second==0.00000000):
                n=n+1
                print(n)
                pygame.time.delay(1000)
                
            ghjgj=Timeclock(i,n,array)
            
        
            
            i=i+1
    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

        

if __name__ == "__main__":
    main()



