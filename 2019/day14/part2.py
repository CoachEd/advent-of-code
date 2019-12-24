import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

"""
pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
"""

start_secs = time.time()

s = """1 QDKHC => 9 RFSZD
15 FHRN, 17 ZFSLM, 2 TQFKQ => 3 JCHF
4 KDPV => 4 TQFKQ
1 FSTRZ, 5 QNXWF, 2 RZSD => 3 FNJM
15 VQPC, 1 TXCJ => 3 WQTL
1 PQCQN, 6 HKXPJ, 16 ZFSLM, 6 SJBPT, 1 TKZNJ, 13 JBDF, 1 RZSD => 6 VPCP
1 LJGZP => 7 VNGD
1 CTVB, 1 HVGW => 1 LJGZP
6 HVGW, 1 HJWT => 2 VDKF
10 PQCQN, 7 WRQLB, 1 XMCH => 3 CDMX
14 VNGD, 23 ZFSLM, 2 FHRN => 4 SJBPT
1 FSTRZ, 4 VTWB, 2 BLJC => 4 CKFW
2 ZTFH, 19 CKFW, 2 FHRN, 4 FNJM, 9 NWTVF, 11 JBDF, 1 VDKF, 2 DMRCN => 4 HMLTV
1 KVZXR => 5 FPMSL
8 XBZJ => 8 QDKHC
1 VQPC => 9 FHRN
15 RKTFX, 5 HKXPJ => 4 ZFSLM
1 HKXPJ, 8 LQCTQ, 21 VJGKN => 5 QCKFR
1 DCLQ, 1 TQFKQ => 4 KVZXR
4 NWTVF, 20 QNXWF => 9 JFLQD
11 QFVR => 3 RZSD
9 RFSZD, 6 WQTL => 7 JBDF
4 BLJC, 3 LQCTQ, 1 QCKFR => 8 QFVR
6 VNGD => 5 VQPC
7 CTMR, 10 SJBPT => 9 VTWB
1 VTWB => 9 DMRCN
6 BCGLR, 4 TPTN, 29 VNGD, 25 KDQC, 40 JCHF, 5 HMLTV, 4 CHWS, 2 CDMX, 1 VPCP => 1 FUEL
1 TQFKQ, 3 FPMSL, 7 KDPV => 6 RKTFX
8 HKXPJ, 2 WQTL => 6 WRQLB
146 ORE => 3 KDPV
9 KDQC => 2 XMCH
1 BGVXG, 21 KVZXR, 1 LQCTQ => 4 CTVB
1 LQCTQ => 5 VJGKN
16 VNGD, 5 VMBM => 1 CTMR
5 VCVTM, 1 FPMSL => 5 HKXPJ
4 HKXPJ => 5 BLJC
14 FHRN, 6 ZFSLM => 1 NWTVF
7 QCKFR, 2 VNGD => 7 VMBM
4 TXCJ, 1 VDKF => 2 QNXWF
136 ORE => 6 BGVXG
5 LQCTQ, 11 DCLQ => 9 XBZJ
3 VQPC => 7 ZTFH
114 ORE => 3 ZWFZX
1 HJWT, 18 KDPV => 7 TXCJ
1 VJGKN => 2 VCVTM
2 KVZXR => 1 HJWT
12 ZWFZX, 1 FHRN, 9 JFLQD => 1 CHWS
3 QFVR => 5 FSTRZ
5 XBZJ => 4 HVGW
1 ZWFZX => 8 LQCTQ
16 WQTL, 10 TXCJ => 9 KDQC
3 FHRN, 12 LJGZP => 5 TPTN
1 JCHF => 7 PQCQN
7 KDPV, 17 BGVXG => 7 DCLQ
1 CKFW, 3 TKZNJ, 4 PQCQN, 1 VQPC, 32 QFVR, 1 FNJM, 13 FSTRZ => 3 BCGLR
2 FSTRZ => 5 TKZNJ"""

arr = s.split('\n')
reactions = {}
surplus_dict = {}
elems_dict = {}
for l in arr:
  arr2 = l.split("=>")
  
  # process left side
  reaction = arr2[0].strip()
  reaction = reaction.replace(',','')
  temparr1 = []
  arr3 = reaction.split(' ')
  found_primitive = False
  for c in arr3:
    if c.isnumeric():
      temparr1.append(int(c))
    else:
      temparr1.append(c)

  # process right side
  produces = arr2[1].strip()
  arr3 = produces.split(' ')
  key = arr3[1]
  qty = arr3[0]
  temparr2 = []
  temparr2.append(int(qty))
  temparr2.append(key)
  temparr2.extend(temparr1)
  reactions[key] = temparr2

def countOre(qty_requested,elem):
  global reactions
  reaction = reactions[elem]
  qty_batch = reaction[0]

  if reaction[3] == 'ORE':
    if not elem in elems_dict:
      elems_dict[elem] = 0
    elems_dict[elem] = elems_dict[elem] + qty_requested
    return

  # try to use any surplus
  if not elem in surplus_dict:
    surplus_dict[elem] = 0
  surplus = surplus_dict[elem]
  if qty_requested <= surplus:
    surplus_dict[elem] = surplus - qty_requested
    return
  else:
    qty_requested = qty_requested - surplus
    surplus_dict[elem] = 0

  div = 1
  if qty_requested > qty_batch:
    div = qty_requested // qty_batch
    rem = qty_requested % qty_batch
    if rem > 0:
      div = div + 1

  # any surplus?
  temps = div * qty_batch - qty_requested
  surplus_dict[elem] = surplus_dict[elem] + temps

  for i in range(2,len(reaction),2):
    countOre(div*reaction[i],reaction[i+1])

  return

countOre(1,'FUEL')

total_ore = 0
for e in elems_dict:
  r = reactions[e]
  qty_needed = elems_dict[e]
  qty_batch = r[0]
  qty_ore = r[2]
  if qty_needed <= qty_batch:
    total_ore = total_ore + qty_batch
  else:
    div = qty_needed // qty_batch
    rem = qty_needed % qty_batch
    if rem > 0:
      div = div + 1
    total_ore = total_ore + div * qty_ore
print('total ore: ' + str(total_ore))



"""
pr.disable()  # end profiling

# print out some stats.
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
"""

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
