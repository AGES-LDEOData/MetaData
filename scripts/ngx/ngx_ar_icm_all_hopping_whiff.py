#!Measurement
'''
baseline:
  peakhop_after: true
  peakhop_before: false
  peakhop_counts: 60
  peakhop_detector: L2
  peakhop_mass: 35.5
  multicollect_after: true
  multicollect_before: false
  multicollect_counts: 10
  multicollect_detector: AX
  multicollect_mass: 39.5
default_fits: nominal
equilibration:
  eqtime: 30
  inlet: B
  inlet_delay: 5
  outlet: Z
  use_extraction_eqtime: false
multicollect:
  counts: 60
  detector: H2
  isotope: Ar40
peakhop:
  hops_name: hops/ar_ICM_all_hops.yaml
  use_peak_hop: true
  ncycles: 20
  detector: L2
  isotope: Ar40
peakcenter:
  multicollect_after: true
  multicollect_before: false
  multicollect_detector: H2
  multicollect_isotope: Ar40
  peakhop_after: true
  peakhop_before: false
  peakhop_detector: L2
  peakhop_isotope: Ar40
whiff:
  counts: 1
  abbreviated_count_ratio: 1.0
  conditionals:
    - action: run_peak_hop
      teststr: Ar40.cur<=0.005
      attr: Ar40
    - action: run_multicollect
      teststr: Ar40.cur>0.005
      attr: Ar40

'''
#this is commit three
#equilibration
#EQ_TIME= 5.0



ACTIVE_DETECTORS=('H2','H1','AX','L1','L2')

def main():

    #this is a comment
    '''
        this is a multiline
        comment aka docstring
    '''
    #display information with info(msg)
    info('unknown measurement script')

    activate_detectors('H2','H1','AX','L1','L2')

    if mx.baseline.peakhop_before:
        baselines(ncounts=mx.baseline.peakhop_counts, mass=mx.baseline.peakhop_mass, detector=mx.baseline.peakhop_detector)


    #position mass spectrometer
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #gas is staged behind inlet

    #post equilibration script triggered after eqtime elapsed
    #equilibrate is non blocking
    #so use either a sniff of sleep as a placeholder until eq finished
    if mx.equilibration.use_extraction_eqtime:
        e = ex.eqtime
    else:
        e = mx.equilibration.eqtime
    set_integration_time(1)
    equilibrate(eqtime=e*1.1, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet,
                delay=mx.equilibration.inlet_delay)

    #equilibrate returns immediately after the inlet opens
    set_time_zero()

    sniff(e)
    set_fits()
    set_baseline_fits()

    result = whiff(ncounts=mx.whiff.counts, conditionals=mx.whiff.conditionals)
    info('Whiff result={}'.format(result))

    if result=='run_peak_hop':

        position_magnet(mx.peakhop.isotope, detector=mx.peakhop.detector)
        reset_measurement(ACTIVE_DETECTORS)
        #open a plot panel for this detectors
        activate_detectors('L2',)

        hops = load_hops(mx.peakhop.hops_name)
        define_hops(hops)

        #set default regression
        set_fits()
        set_baseline_fits()

        peak_hop(ncycles=mx.peakhop.ncycles, hops=hops)
        #multicollect on active detectors
        #multicollect(ncounts=mx.multicollect.counts, integration_time=1)

        if mx.baseline.peakhop_after:
            baselines(ncounts=mx.baseline.peakhop_counts, mass=mx.baseline.peakhop_mass, detector=mx.baseline.peakhop_detector, integration_time=1)

        set_integration_time(1)
        if mx.peakcenter.peakhop_after:
            activate_detectors('H2','H1','AX','L1','L2', peak_center=True)
            peak_center(detector=mx.peakcenter.peakhop_detector, isotope=mx.peakcenter.peakhop_isotope, integration_time=1)

    elif result=='run_multicollect':

        set_fits()
        set_baseline_fits()

        #multicollect on active detectors
        set_integration_time(10)
        multicollect(ncounts=mx.multicollect.counts, integration_time=10)

        if mx.baseline.multicollect_after:
            baselines(ncounts=mx.baseline.multicollect_counts,mass=mx.baseline.multicollect_mass, detector=mx.baseline.multicollect_detector, integration_time=10)

        set_integration_time(1)
        if mx.peakcenter.multicollect_after:
            activate_detectors('H2','H1','AX','L1','L2', peak_center=True)
            peak_center(detector=mx.peakcenter.multicollect_detector,isotope=mx.peakcenter.multicollect_isotope, integration_time=1)

    info('finished measure script')

#========================EOF==============================================================
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)
    #baselines(counts=50,mass=0.5, detector='CDD')s

#isolate sniffer volume
    # close('S')
#     sleep(1)
#
#     #open to mass spec
#     open('R')
#
#     set_time_zero()
#     #display pressure wave
#     sniff(5)
#
#     #define sniff/split threshold
#     sniff_threshold=100
#
#     #test condition
#     #if get_intensity('H1')>sniff_threshold:
#     if True:
#         gosub('splits:jan_split', klass='ExtractionLinePyScript')
#
