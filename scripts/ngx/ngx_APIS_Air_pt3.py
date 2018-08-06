#===============================================================================
# EXTRACTION SCRIPT ngx_APIS_Air_pt3.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('NGX APIS Air pt3 Script')
    p_test = get_pressure('Hub','IG1')
    info('the value of p_test is ={}'.format(p_test))
    if p_test > 1e-7:
        cancel()
    if p_test == 0:
        cancel()
    cryofocus = False
    open('D')
    sleep(5)
    if not analysis_type=='blank':
        extract_pipette('Air pt3 cc', timeout=120)
    else:
        extract_pipette('Blank Air pt3 cc', timeout=120)
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
        sleep(5)

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
