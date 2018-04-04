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
