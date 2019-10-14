#===============================================================================
# EXTRACTION SCRIPT helix_T2Air_big_x1_cryo.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('Helix MC 2 Air Tank Big Shot Standard Script')
    # Air tank is hooked up at valve 31; this is the 0.28 cc pipette
    close('16')
    close('17')
    gosub('CryoWaitFreeze')
    sleep(5)
    open('9')
    open('19')
    sleep(5)
    open('10')
    open('13')
    open('31')
    sleep(30)
    # pump pipette
    open('32')
    sleep(120)
    close('32')
    sleep(15)
    # fill pipette
    if not analysis_type=='blank':
        open('33')
    sleep(60)
    close('33')
    sleep(15)
    # close turbopump
    close('19')
    sleep(5)
    # inlet pipette and wait for first stage cleanup
    open('32')
    sleep(120)
    # open bare cryostat and freeze
    close('15')
    sleep(5)
    open('18')
    open('16')
    gosub('CryoWaitFreeze')
    sleep(120)
    # open charcoal cryostat and focus
    close('13')
    sleep(5)
    open('15')
    open('14')
    gosub('CryoWaitFreeze')
    sleep(900)
    # isolate charcoal, pump remainder, warm to release
    close('15')
    close('14')
    sleep(10)
    # open 10 and 13 if closed (might depend on getter/quad usage)
    open('10')
    open('13')
    sleep(5)
    # ensure pumping
    open('9')
    gosub('CryoWaitRelease')
    sleep(300)
    # equilibrate into inlet volume, then prepare to inlet
    close('9')
    sleep(5)
    open('14')

#===============================================================================
# POST EQUILIBRATION SCRIPT helix_T2Air.py
#===============================================================================
def main():
	info('Pump line after aux tank input')
	open('19')
	open('9')
	sleep(10)
	gosub('CryoWaitPump')
	sleep(60)
	close('16')
	open('15')
	close('32')
	close('34')
	sleep(60)
	set_cryo('freeze')
	sleep(5)
	close('14')

#===============================================================================
# POST MEASUREMENT SCRIPT helix_pump_ms.py
#===============================================================================
def main():
	info('Pump mass spec after analysis')
	open(name='1')
