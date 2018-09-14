#===============================================================================
# EXTRACTION SCRIPT ngx_crusher_air_x1_split.py
#===============================================================================
"""
eqtime: 30
"""
def main():
    info('NGX crusher air standard')
    close('C')
    gosub('CryoWaitFreeze')
    open('I')
    open('J')
    open('D')
    open('A')
    close('H')
    sleep(5)
    open('G')
    sleep(120)
    close('G')
    sleep(15)
    p_test = get_pressure('Hub','IG1')
    info('the value of p_test is ={}'.format(p_test))
    if p_test > 1e-7:
        cancel()
    if p_test == 0:
        cancel()
    sleep(5)
    if not analysis_type=='blank':
        open('H')
    sleep(60)
    close('H')
    close('J')
    info('Procedural Air standard')
    sleep(duration)
    close('A')
    close('D')
    sleep(5)
    open('G')
    open('J')
    sleep(cleanup)
    close('C')
    sleep(5)
    open('A')
    sleep(60)
    close('A')
    open('C')
    gosub('CryoWaitFreeze')
    sleep(240)
    close('A')
    sleep(5)
    open('D')
    gosub('CryoWaitRelease')
    close('G')
    p_test = get_pressure('Hub','IG1')
    info('the value of p_test is ={}'.format(p_test))
    if p_test > 1e-7:
        cancel()
    if p_test == 0:
        cancel()
    sleep(300)

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_crusher.py
#===============================================================================
def main():
	info('Pump after crusher analysis')
	sleep(3)
	open('D')
	open('A')
	open('C')
	open('I')
	open('J')
	gosub('CryoWaitPump')
	sleep(120)
	close('C')
	set_cryo('freeze')
	# gosub('jan:PumpMicrobone')
	# gosub('jan:PumpMinibone')
	#

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='Z')
