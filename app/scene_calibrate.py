from app.cast import *
from ecosys import *


def calibration_widget_activate():
    calib_widget.btn_stir_calib.clicked.connect(calibrate_axis_stir)
    calib_widget.btn_mag_calib.clicked.connect(calibrate_axis_mag)
    calib_widget.btn_disk_calib.clicked.connect(calibrate_axis_disk)

    _default_current = defaults.get("motor_current")
    calib_widget.spin_stir_current.setValue(_default_current.get("motor_stir"))
    calib_widget.spin_mag_current.setValue(_default_current.get("motor_mag"))
    calib_widget.spin_disk_current.setValue(_default_current.get("motor_disk"))

    calib_widget.spin_stir_current.valueChanged.connect(update_stir_current)
    calib_widget.spin_mag_current.valueChanged.connect(update_mag_current)
    calib_widget.spin_disk_current.valueChanged.connect(update_disk_current)

def update_stir_current(a:float=1):
    update_defaults("motor_current",{"motor_stir":a})
    machine.motor_stir.driver.set_current_by_a(a)
def update_mag_current(a:float=1):
    update_defaults("motor_current",{"motor_mag":a})
    machine.motor_mag.set_current_by_a(a)
def update_disk_current(a:float=1):
    update_defaults("motor_current",{"motor_disk":a})
    machine.motor_disk.set_current_by_a(a)

def calibrate_axis_stir():
    if e_work.is_set():
        return
    e_work.set()
    calibrate_motor_stir()
    e_work.clear()

def calibrate_axis_mag():
    if e_work.is_set():
        return
    e_work.set()
    calibrate_motor_mag() 
    e_work.clear()

def calibrate_axis_disk():
    if e_work.is_set():
        return
    e_work.set()
    disk_calibrate()
    e_work.clear()


def motor_mag_spin(a:float=0):
    # assert -90.0 <= a <= -50.0
    # if a<-90: a = -90
    # if a>-50: a = -50
    # window.doubleSpinBox.setValue(a)
    machine.motor_mag.move_to(a)

def calibrate_motor_mag():
    bottom_u = defaults.get("motor_bottom").get("motor_mag")
    if window.popup(question=(lang("Alert"),lang("motor_mag")+','+lang("Are_you_sure_to_calibrate?"))):
        window.doubleSpinBox.valueChanged.connect(motor_mag_spin)
        window.pushButton_42.clicked.connect(return_with_save_assure)
        window.doubleSpinBox.setEnabled(False)
        window.stackedWidget.setCurrentIndex(6)
        machine.motor_stir.home_return()
        machine.motor_mag.home()
        window.doubleSpinBox.setValue(float(-bottom_u))
        window.doubleSpinBox.setEnabled(True)
def return_with_save_assure(): 
    bottom_u = None
    if window.popup(question=(lang("Alert"),lang("Sure_to_Save?"))):
        bottom_u = window.doubleSpinBox.value()
        update_defaults("motor_bottom",{"motor_mag":-bottom_u})
    machine.motor_mag.home()
    window.stackedWidget.setCurrentIndex(5)
    return bottom_u

def calibrate_motor_stir():
    motor_name = "motor_stir"
    motor:Union[ModbusStepper,LsStepper] = getattr(machine,motor_name)
    bottom_u = defaults.get("motor_bottom").get(motor_name)
    if window.popup(question=(lang("Alert"),lang(motor_name)+', '+lang("Are_you_sure_to_calibrate?"))):
        motor.hard_stop()
        ret = window.popup(question=("How to","Please enssure the position, and press 'Yes'"))
        if ret:
            bottom_p = motor.calibrate()
            bottom_u = bottom_p/motor.ppu
            update_defaults("motor_bottom",{motor_name:bottom_u})
            window.popup(about=(lang("About"),lang(motor_name)+', '+lang("finished")))

        else:
            bottom_u = calibrate_motor_stir()
    else:
        motor.home_return()
    return bottom_u

def disk_calibrate():
    if disk_calibrate_disk_1():
        disk_calibrate_disk_8()
        machine.motor_disk.prepare_at_grid_1()

def disk_calibrate_disk_1():
    motor_name = "motor_disk"
    motor = machine.motor_disk
    if window.popup(question=(lang("Alert"),lang(motor_name)+', '+lang("Are_you_sure_to_calibrate?"))):
        machine.motor_mask.home()
        machine.motor_stir.home_direct()
        motor.hard_stop()
        ret = window.popup(question=(lang("How to"),lang("Align_DISK_1")))
        if ret:
            ret = window.popup(question=(lang("Important!"),lang("Sure_Align_DISK_1")))
            if ret:
                motor_stir_drop()
                ret = window.popup(about=(lang("Alert"),lang("Aligned?")))
                motor_stir_home()
                bottom_p = motor.calibrate()
                motor._grid = 1
                motor_stir_drop()
                if window.popup(question=(lang("Alert"),lang("Is the target on the same site you want?"))):
                    motor_stir_home()
                    bottom_u = bottom_p/motor.ppu
                    if bottom_u > 0.4447:
                        window.popup(about=(lang("Alert"),lang("Bias_Error")))
                        disk_calibrate_disk_1()
                    else:
                        update_defaults("motor_bottom",{"motor_disk":bottom_u})
                        return True
                else:
                    motor_stir_home()
                    disk_calibrate_disk_1()
    return False

def motor_stir_drop():
    machine.motor_stir.hard_stop()
def motor_stir_home():
    machine.motor_stir.home_return()

def disk_calibrate_disk_8():
    motor_name = "motor_disk"
    motor = machine.motor_disk
    disk1_u = defaults.get("motor_bottom").get("motor_disk")
    ppr = defaults.get("motor_ppr").get("motor_disk")
    if window.popup(question=(lang("Alert"),lang(motor_name)+', '+lang("Continue to calibrate?"))):
        motor.hard_stop()
        ret = window.popup(question=(lang("How to"),lang("Align DISK 8, and press 'Yes'")))
        if ret:
            motor_stir_drop()
            ret = window.popup(about=(lang("Alert"),lang("Aligned?")))
            motor_stir_home()
            disk8_p = motor.calibrate()
            motor._grid = 8
            motor_stir_drop()
            if window.popup(question=(lang("Alert"),lang("Is the target on the same site you want?"))):
                motor_stir_home()
                disk1_p = motor.ppu*disk1_u
                delta_p = disk8_p - disk1_p
                new_upr = 7/delta_p*ppr
                update_defaults("motor_upr",{"motor_disk":new_upr})

                new_disk1_u = disk1_p/(ppr/new_upr)
                update_defaults("motor_bottom",{"motor_disk":new_disk1_u})

                window.popup(about=(lang("About"),lang(motor_name)+', '+lang("Done. Good Job!")))
            else:
                motor_stir_home()
                disk_calibrate_disk_8()

