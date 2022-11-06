from ecosys import aSim
from prots import *

splash_screen:aSplashScreen = aSim(aSplashScreen)
login_screen:aLoginScreen = aSim(aLoginScreen)
configor_screen:aConfigorScreen = aSim(aConfigorScreen)
op_screen:aOperatorScreen = aSim(aOperatorScreen)
review_screen:aReviewScreen = aSim(aReviewScreen)

configor:aConfigor = aSim(aConfigor)
operator:aOperator = aSim(aOperator)

machine: aMachine = aSim(aMachine)
uv_widget:aUV = aSim(aUV)
beeper:aBeeper = aSim(aBeeper)



def is_real(obj):
    return obj and (not isinstance(obj,aSim))
def call(obj_sim,obj_ret):
    return obj_ret if obj_ret else obj_sim 

