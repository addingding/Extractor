#-*- coding: utf-8 -*
import RPi.GPIO as GPIO
import time

"""
金币 3 7
蘑菇 3 5  3123
过关 5 1 3 5 1 3 5 3
b6 1 b3 b6 1 b3 b6 b3
b7 2 4 b7 2 4 b7 b7 b7 b7 1
挂掉 1444321 或者_5444321
"""

class Beeper():

    def __init__(self,pin=22):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) #GPIO.BOAR
        GPIO.setup(pin,GPIO.OUT)
        self.pin = pin
        self.off()

    def on(self):
        GPIO.output(self.pin, GPIO.LOW)    
    def off(self):
        GPIO.output(self.pin, GPIO.HIGH)
    def beep(self):
        for i in range(3):
            self.on()
            time.sleep(0.5)
            self.off()
            time.sleep(0.5)
    def exit(self):
        GPIO.cleanup()
        self.off()

    def __del__(self):
        self.exit()

class Singer(object):
    def __init__(self,pin_buzzer=22,delay_beat=0.5):
        
        # 设置蜂鸣器引脚模式
        self.pin_buzzer = pin_buzzer
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_buzzer,GPIO.OUT) 

        # 创建PWM对象初始频率 440hz，占空比50%
        self.buzzer = GPIO.PWM( pin_buzzer , 440)
        self.buzzer.start(50)
        
        # 音符到频率的转换字典，cl低音，cm中音，ch高音
        self.note2freq = {"cl1":131,"cl2":147 ,'cl3':165 ,"cl4":175 ,"cl5":196 ,"cl6":211 ,"cl7":248,
                          "cm1":262,"cm2":294 ,'cm3':330 ,"cm4":350 ,"cm5":393 ,"cm6":441 ,"cm7":495,
                          "ch1":525,"ch2":589 ,'ch3':661 ,"ch4":700 ,"ch5":786 ,"ch6":882 ,"ch7":990
                          }
        # 节拍时长初始化
        self.delay_beat = delay_beat
    def __del__(self):
        self.destroy()

    def play_song(self,notes,beats):
       
        for note,beat in zip(notes,beats):
            # 切换频率，演奏音乐
            self.buzzer.ChangeFrequency(self.note2freq[note])
            # 持续的时间
            time.sleep(self.delay_beat*beat)
            
    def destroy(self):
        self.buzzer.stop()
        GPIO.output(self.pin_buzzer, GPIO.LOW)
        GPIO.cleanup()
        
    def play_good(self,times:int=1):
        for i in range(times):
            self.play_song(['cm3','cm7'],[1,1])
            time.sleep(0.5)
    def play_nice(self,times:int=1):
        for i in range(times):
            self.play_song(['cm3','cm5','cm3','cm1','cm2','cm3'],[1,1,1,1,1,1])
            time.sleep(0.5)
    def play_good_end(self,times:int=1):
        for i in range(times):
            self.play_song(['cm5','cm1','cm3','cm5','cm1','cm3','cm5','cm3'],[1,1,1,1,1,1,1,1])
            time.sleep(0.5)
    def play_bad_end(self,times:int=1):
        for i in range(times):
            self.play_song(["cl5","cm4","cm4","cm4","cm3","cm2","cm1"],[1,1,1,1,1,1,1])
            time.sleep(0.5)


class SongHappy():

    
    notes = ['cm1' ,'cm1' , 'cm1' , 'cl5' , 'cm3' , 'cm3' , 'cm3' , 'cm1' ,
             'cm1' , 'cm3' , 'cm5' , 'cm5' , 'cm4' , 'cm3' , 'cm2' , 'cm2' ,
             'cm3' , 'cm4' , 'cm4' , 'cm3' , 'cm2' , 'cm3' , 'cm1' , 'cm1' ,
             'cm3' , 'cm2' , 'cl5' , 'cl7', 'cm2' , 'cm1']
    beats = [1 , 1 , 2 , 2 , 1 , 1 , 2 , 2 ,
            1 , 1 , 2 , 2 , 1 , 1 , 3 , 1 ,
            1 , 2 , 2 , 1 , 1 , 2 , 2 , 1 ,
            1 , 2 , 2 , 1 , 1 , 3]

class Beepers:
    def get_beeper(self,pin=22):
        return Beeper(pin)
    def get_singer(self,pin=22):
        return Singer(pin,0.5)

beepers = Beepers()

class TestBeeper:
    def beeper(self):
        beeper = beepers.get_beeper(22)
        beeper.beep()

    def test_singer(self):
        singer = beepers.get_singer(22)
        song = SongHappy()
        singer.play_song(song.notes,song.beats)
    def test_mario(self):
        singer = beepers.get_singer(22)
        singer.play_good()
        singer.play_nice()
        singer.play_good_end()
        singer.play_bad_end()


if __name__ == '__main__':
    T = TestBeeper()
    T.beeper()
