import time

info = dict(
    pg_idx = None,
    pg_name = None,
    disk_1_preset = 50,
    disk_8_preset = 80,
    pg_total_time = 1,
    pg_start_time = time.time(),

    step_idx = 1,
    op_name= "mixing",
    disk = 1,
    sec_wait= 50,
    sec_mix= 60,
    sec_mag= 6,
    ul_volumn= 700,
    speed_mix= 2,
    temperature= 25,
    step_total_time = 1,
    step_start_time = time.time(),
    
    disk_1_temperature = 25,
    disk_8_temperature = 25,
    disk_pos = 1,
    led_is_on = False,
    fan_is_on = False,
    uv_is_on = False,
    door_at_spot = False,
    sheath_at_spot = False,


    

)

class Updater:
    ...