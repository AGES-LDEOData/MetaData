#===============================================================================
# EXTRACTION SCRIPT ngx_co2.py
#===============================================================================
"""
eqtime: 30
"""
def main():
    info('NGX laser analysis')
    p_test = get_pressure('Hub','IG1')
    info('the value of p_test is ={}'.format(p_test))
    if p_test > 1e-7:
        cancel()
    if p_test == 0:
        cancel()
    cryofocus = False
    #prepare for analysis
    #gosub('PrepareCryo')
    gosub('PrepareCO2')
    if analysis_type=='blank':
        info('is blank. not heating')
        close('D')
        sleep(duration)
    else:
        info('move to position {}'.format(position))

        for i, p in enumerate(position):
            move_to_position(position)
            if i==0:
                close('D')
            begin_interval(duration)
            if ramp_duration>0:
                fire_laser()
                info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units))
                ramp(setpoint=extract_value, duration=ramp_duration, period=0.5)
            else:
                info('set heat to {}'.format(extract_value))
                extract(extract_value)
            complete_interval()

    if not analysis_type=='blank':
        disable()
    sleep(cleanup)
    if cryofocus:
        open('C')
        gosub('CryoWaitFreeze')
        sleep(180)
        close('A')
        sleep(5)
        open('D')
        gosub('CryoWaitRelease')
        p_test = get_pressure('Hub','IG1')
        info('the value of p_test is ={}'.format(p_test))
        if p_test > 1e-7:
            cancel()
        if p_test == 0:
            cancel()
        sleep(300)
    if not cryofocus:
        open('A')

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_unknown.py
#===============================================================================
def main():
	info('Pump after air analysis')
	cryofocus = False
	sleep(3)
	open('D')
	if cryofocus:
		open('A')
		open('C')
		gosub('CryoWaitPump')
		sleep(120)
		close('C')
		set_cryo('freeze')
	open('A')
	# gosub('jan:PumpMicrobone')
	# gosub('jan:PumpMinibone')
	#

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='Z')
