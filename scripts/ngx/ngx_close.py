#===============================================================================
# EXTRACTION SCRIPT ngx_close.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('NGX close then pause')
    close('D')
    sleep(180)

    # gosub('jan:WaitForMiniboneAccess')
    # gosub('jan:PrepareForAirShot')
    # gosub('jan:EvacPipette2')
    # gosub('common:ExpandPipette2')
    # gosub('common:FillPipette2')
    # gosub('jan:PrepareForAirShotExpansion')
    # gosub('common:ExpandPipette2')
    # close(description='Outer Pipette 2')

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_unknown.py
#===============================================================================
def main():
    info('Pump after analysis')
    open('D')

    # degas t
    # gosub('obama:PumpBone')
    # gosub('obama:PumpMinibone')

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='Z')
