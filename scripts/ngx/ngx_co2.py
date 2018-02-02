#===============================================================================
# EXTRACTION SCRIPT ngx_co2.py
#===============================================================================
"""
eqtime: 30
"""
def main():
    info('NGX laser analysis')

    #prepare for analysis
    #gosub('PrepareCryo')
    gosub('PrepareCO2')


    if analysis_type=='blank':
        info('is blank. not heating')
        sleep(duration)
    else:
        info('move to position {}'.format(position))

        for i, p in enumerate(position):
            move_to_position(position)
            if i==0:
                close('D')
            begin_interval(duration)
            if ramp_rate>0:
                info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units))
                ramp(setpoint=extract_value, rate=ramp_rate)
            else:
                info('set heat to {}'.format(extract_value))
                extract(extract_value)
            complete_interval()

    if not analysis_type=='blank':
        disable()
    sleep(cleanup)

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
