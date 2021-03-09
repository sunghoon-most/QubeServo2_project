import spidev
import time

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
spi.mode=0b01
spi.bits_per_word=8
dummy=0xff #255
start=0x47 #71
sgl=0x20 #32
ch0=0x07
ch1=0x08 
msbf=0x88 #136

def measure(ch):
    ad=spi.xfer2([(start+sgl+ch+msbf),dummy])
    val=((((ad[0]&0x33)<<8)+ad[1])*3.3)/1023
    return val
try:
    while 1:
        mes_ch0=measure(ch0)
        mes_ch1=measure(ch1)
        print ('ch0=%2.2f' %mes_ch0,'[V],ch1=%2.2f' %mes_ch1,'[v]')
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
spi.close()