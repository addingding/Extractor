from prots import *

calib_map = {
    "btn_stir_calib":"pushButton_38",
    "btn_mag_calib":"pushButton_39",
    "btn_disk_calib":"pushButton_40",

    "btn_calibration":"pushButton_41",
    "grp_calibration":"groupBox_8",

    "spin_stir_current":"doubleSpinBox_2",
    "spin_mag_current":"doubleSpinBox_3",
    "spin_disk_current":"doubleSpinBox_4",
}

class Calibration(aWidget):
    def __init__(self, ui):
        super().__init__(ui, calib_map)
        self.ui = ui

