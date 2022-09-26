from ecosys import *
from app.cast import *


def calibration_widget_activate():
    calib_widget.btn_stir_calib.clicked.connect(calibrate_axis_stir)
    calib_widget.btn_mag_calib.clicked.connect(calibrate_axis_mag)
    calib_widget.btn_disk_calib.clicked.connect(calibrate_axis_disk)


def calibrate_axis_stir():
    if event_working.is_set():
        return
    event_working.set()
    calibrate_motor_stir()
    event_working.clear()
def calibrate_axis_mag():
    if event_working.is_set():
        return
    event_working.set()
    calibrate_motor_mag() #TODO
    event_working.clear()

def calibrate_axis_disk():
    if event_working.is_set():
        return
    event_working.set()
    disk_calibrate()
    event_working.clear()

def motor_mag_spin(a:float=0):
    assert -70.0 <= a <= -50.0
    if a<-70: a = -70
    if a>-50: a = -50
    window.doubleSpinBox.setValue(a)
    machine.motor_mag.move_to(a)

def calibrate_motor_mag():
    bottom_u = defaults.get("motor_bottom").get("motor_mag")
    if window.popup(question=(lang("Alert"),lang("motor_mag")+','+lang("Are you sure to calibrate?"))):
        window.doubleSpinBox.valueChanged.connect(motor_mag_spin)
        window.pushButton_42.clicked.connect(return_with_save_assure)
        window.doubleSpinBox.setEnabled(False)
        window.stackedWidget.setCurrentIndex(6)
        machine.motor_stir.home_return()
        machine.motor_mag.home()
        window.doubleSpinBox.setValue(float(-bottom_u))
        window.doubleSpinBox.setEnabled(True)
def return_with_save_assure(): 
    if window.popup(question=(lang("Alert"),lang("Sure to Save?"))):
        bottom_u = window.doubleSpinBox.value()
        update_defaults("motor_bottom",{"motor_mag":-bottom_u})
    machine.motor_mag.home()
    window.stackedWidget.setCurrentIndex(5)
    return bottom_u

def calibrate_motor_stir():
    motor_name = "motor_stir"
    motor:Union[ModbusStepper,LsStepper] = getattr(machine,motor_name)
    bottom_u = defaults.get("motor_bottom").get(motor_name)
    if window.popup(question=(lang("Alert"),lang(motor_name)+', '+lang("Are you sure to calibrate?"))):
        motor.hard_stop()
        ret = window.popup(question=("How to","Please assure the position, and press 'Yes'"))
        if ret:
            bottom_p = motor.calibrate()
            bottom_u = bottom_p/motor.ppu
            update_defaults("motor_bottom",{motor_name:bottom_u})
            window.popup(about=(lang("About"),lang(motor_name)+', '+lang("Job finished!")))

        else:
            bottom_u = calibrate_motor_stir()
    else:
        motor.home_return()
    return bottom_u




def disk_calibrate():
    disk_calibrate_disk_1()
    disk_calibrate_disk_8()

def disk_calibrate_disk_1():
    motor_name = "motor_disk"
    motor = machine.motor_disk
    if window.popup(question=(lang("Alert"),lang(motor_name)+', '+lang("Are sure to calibrate?"))):
        machine.motor_mask.home()
        machine.motor_stir.home()
        motor.hard_stop()
        ret = window.popup(question=(lang("How to"),lang("Align DISK 1")))
        if ret:
            calibrate_motor_stir()
            bottom_p = motor.calibrate()
            motor._grid = 1
            if window.popup(question=(lang("Alert"),lang("Is the target on the same site you want?"))):
                bottom_u = bottom_p/motor.ppu
                update_defaults("motor_bottom",{"motor_disk":bottom_u})
            else:
                bottom_u = disk_calibrate_disk_1()
def disk_calibrate_disk_8():
    motor_name = "motor_disk"
    motor = machine.motor_disk
    disk1_u = defaults.get("motor_bottom").get("motor_disk")
    ppr = defaults.get("motor_ppr").get("motor_disk")
    if window.popup(question=(lang("Alert"),lang(motor_name)+', '+lang("Continue to calibrate?"))):
        motor.hard_stop()
        ret = window.popup(question=("How to",f"Align DISK 8, and press 'Yes'"))
        if ret:
            calibrate_motor_stir()
            disk8_p = motor.calibrate()
            motor._grid = 8
            if window.popup(question=(lang("Alert"),lang("Is the target on the right site you wanted?"))):
                disk1_p = motor.ppu*disk1_u
                delta_p = disk8_p - disk1_p
                new_upr = 7/delta_p*ppr
                update_defaults("motor_upr",{"motor_disk":new_upr})

                new_disk1_u = disk1_p/(ppr/new_upr)
                update_defaults("motor_bottom",{"motor_disk":new_disk1_u})

                window.popup(about=(lang("About"),lang(motor_name)+', '+lang("Ok, Job finished!")))
            else:
                disk_calibrate_disk_8()

