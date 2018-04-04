#===============================================================================
# EXTRACTION SCRIPT ngx_air_x1.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('NGX Air Script')
    cryofocus = True
    open('D')
    close('H')
    sleep(5)
    open('G')
    sleep(120)
    close('G')
    if cryofocus:
        close('C')
        gosub('CryoWaitFreeze')
    sleep(5)
    if not analysis_type=='blank':
        open('H')
    sleep(60)
    close('H')
    close('D')
    sleep(5)
    open('G')
    sleep(180)
    if cryofocus:
        open('C')
        gosub('CryoWaitFreeze')
        sleep(180)
        close('A')
        gosub('CryoWaitRelease')
        sleep(300)
    if not cryofocus:
        open('A')

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_cryo.py
#===============================================================================
"""
"""

def main():
    args = set_cryo('pump')
    if args:
        v1,v2 = args
        tol = 5
        cnt = 0
        cnt_tol = 2
        while 1:
          av1 = get_cryo_temp(1)
          if abs(av1 - v1)<tol:
              av2 = get_cryo_temp(2)
              if abs(av2-v2)<tol:
                  cnt+=1
          if cnt>cnt_tol:
              break
          sleep(5)

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='Z')
