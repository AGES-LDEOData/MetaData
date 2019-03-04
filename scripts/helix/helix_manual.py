#===============================================================================
# EXTRACTION SCRIPT helix_manual.py
#===============================================================================
'''
sensitivity_multiplier: 0.5
modifier: 1
eqtime: 30
'''
def main():
    info('Helix MC Manual Extraction')
    # Does nothing but record that a manual extraction was performed

#===============================================================================
# POST EQUILIBRATION SCRIPT helix_none.py
#===============================================================================
def main():
	info('The line is left in its current state')

#===============================================================================
# POST MEASUREMENT SCRIPT helix_pump_ms.py
#===============================================================================
def main():
	info('Pump mass spec after analysis')
	open(name='1')
