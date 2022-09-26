from ecosys import *
from prots import *

# 各轴电机功能 ：
#     1.圆盘电机X轴 57： 负责旋转到指定孔盘位置
#     2.屏蔽电机Y   42： 负责X轴电机旋转时将磁棒套遮住
#     3.磁棒套马达Z 57： 磁棒套上下移动与搅拌
#     4.磁棒马达V   42： 磁棒上下
# 动作帮助 ：
#     1.首次搅拌 ： 
#       o X 轴移到指定位置 （A）
#       > V轴移到磁棒套底部 （B） 
#       > Z、V 同步移到到孔盘底部 （C） 
#       > Z、V 同步缓慢上升到液高面高度一半（D） 
#       > V 轴回HOME 
#       > Z 轴上下快速搅拌（E）（F） 
#       > Z 轴 上升到液面上方 （G） 
#       > V下降磁棒套底部 
#       > Z、V 同时缓慢下降至底部 （H） 
#       > Z、V 同步缓慢上升至液面上方 （G） 
#       > Z、V 同步上升至顶部 
#       > Y 轴  移入磁棒套底部 。 
#     2. 搅拌 ： 
#       o X 轴移到指定位置 （ A） 
#       > Y 轴 移动到HOME 
#       > Z、V 同时移到液高面高度一半（D） 
#       > V轴回HOME 
#       > Z 轴上下快速搅拌（E）（F） 
#       > Z 轴 上升到液面上方 
#       > V下降磁棒套底部 
#       > Z、V 同步缓慢下降至底部 （H） 
#       > Z、V 同步缓慢上升至液面上方 （G） 
#       > Z、V 同步上升至顶部 
#       > Y 轴 移至磁棒套底部 。
#      3. 磁珠弃置 ： 
#       o X 轴移到指定位置 
#       > Y 轴 移动到HOME 
#       > Z、V 同步下降移到液高面高度一半（D） 
#       > V轴回HOME 
#       > Z 轴上下快速搅拌 （E）（F） 
#       > Z 回 HOME

# A 为用户编辑
# B.C为可工程模式设定
# D 为实际量测.100ul200ul... 1000ul的一半
# H 为可以工程设定
# G 为实际量测.100ul200ul... 1000ul 的液面高度
# E 为速度 3个档位
# F 两个行程高度 3mm，7mm

points_map:dict = {
    "main":{
        "home":0,
        "liquid_t":0,
        "liquid_m":0,
        "liquid_b":0,
        "ready_point":0,
        "hard_limit":0
    }
}

def get_operation(operation_idx):
    ...
def get_operation_moves(operation_idx):
    ...

class Move(aMove):
    ...

class Operation(aOperation):
    ...

