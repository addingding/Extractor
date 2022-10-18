from ecosys import *
from app.cast import *

from app.scene_calibrate import *
from app.scene_perform import *

def start():
    
    # opening_show_window()
    infowin.show()
    app_worker.work_for(machine_init)
    app_worker.job_done.connect(window_ready)
    app_worker.start()

    application.exec_()
    machine_exit()
    sys.exit(0)

def opening_show_window():
    if not flash is None:
        flash.show()
        flash.playmovie(window.show)
    else:
        splash.effect()
        window.show()

def window_ready():
    infowin.close()
    if not is_real(machine):
        window.popup(about=(lang("Alert"),lang("Device Error!")))
        return
    control_assign()
    refresh_thread_start()
    window.showFullScreen()

def control_assign():
    control_button_activate()
    calibration_widget_activate()
    
def control_button_activate():
    start_widget.btn_start.clicked.connect(prepare_task)#prepare
    window.pushButton_4.clicked.connect(fan_switch)
    window.pushButton_5.clicked.connect(led_switch)
def fan_switch():
    return machine.fan.switch()
def led_switch(a=None):
    return machine.led.switch()


def refresh_thread_start():
    Thread(target=signal_update).start()
    update_timer.timeout.connect(status_widget.update)
    update_timer.start(1000)
def signal_update():
    while not e_stop_collect.is_set():
        machine.update()
        time.sleep(0.1)

def signal_collect_stop():
    e_stop_collect.set()

def machine_exit():
    signal_collect_stop()
    if is_real(machine):
        # job_dismiss.set()
        # main_job_thread.join()
        machine.exit()

def machine_init():
    infowin.show_info("Machine initializing")

    if is_real(machine):
        infowin.show_info("Machine Initialized")
        try:
            bottoms = defaults.get("motor_bottom")
            machine.led.turn_on()
            machine.fan.turn_on()
            machine.motor_disk.set_points(0,bottoms["motor_disk"])
            machine.motor_mask.set_points(0,bottoms["motor_mask"])
            machine.motor_mag.set_points(0,bottoms["motor_mag"])
            machine.motor_stir.set_points(200,bottoms["motor_stir"])
            machine.motor_mag.local_set_speed(8)
            machine.motor_disk.local_set_speed(1.5)

            infowin.show_info("Mask Motor homing ...")
            machine.motor_mask.home()
            infowin.show_info("Mask Motor homed")
            infowin.show_info("Stir Motor homing ...")
            machine.motor_stir.home_return()
            infowin.show_info("Stir Motor homed")
            infowin.show_info("Mag-sitck Motor homing ...")
            machine.motor_mag.home()
            machine.motor_mag.bottom()
            machine.motor_mag.home()
            infowin.show_info("Mag-sitck Motor homed")

            infowin.show_info("Disk Motor homing ...")
            machine.motor_disk.home_return(timeout=15)
            infowin.show_info("Disk Motor homed")
            machine.motor_disk.bottom()
            infowin.show_info("Disk Motor ready")

            print("machine is ready!")
            infowin.show_info("machine is ready!")

        except HomeError:
            infowin.popup(about=(lang('Alert'),lang('HomeError')))
        except TimeoutError:
            infowin.popup(about=(lang('Alert'),lang('TimeoutError')))
        except SafeError:
            infowin.popup(about=(lang('Alert'),lang('SafeError')))
        except Exception as e:
            print(e)
            infowin.popup(about=(lang('Alert'),lang('InitError')))
    else:
        print("machine is not ready ,wait for 5 secs and simulator on")
        time.sleep(5)


if __name__ == "__main__":
    start()