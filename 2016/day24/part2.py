"""
AoC
"""
import time
import sys
import copy
from itertools import permutations


# validate coord
def vc(y,x,a):
  if y < 0 or y >= len(a) or x < 0 or x >= len(a[0]):
    return False
  return True

# add edge
def add_edge(y1,x1,y2,x2,a,d):
  if not vc(y1,x1,a) or not vc(y2,x2,a) or (y1 == y2 and x1 == x2):
    return
  if a[y1][x1] == '#' or a[y2][x2] == '#':
    return
  n1 = str(y1)+','+str(x1)
  n2 = str(y2)+','+str(x2)
  if not n1 in d:
    d[n1] = {}
  if not n2 in d:
    d[n2] = {}
  
  if not n2 in d[n1]:
    # add it
    d[n1][n2] = 1

  if not n1 in d[n2]:
    # add it
    d[n2][n1] = 1

# add edges, distance,array
def add_edges(d,a):
  for y in range(len(a)):
    for x in range(len(a[y])):

      if a[y][x] == '#':
        # wall
        continue

      ty = y-0
      tx = x
      by = y+1
      bx = x
      ry = y
      rx = x+1
      ly = y
      lx = x-1
      
      add_edge(y,x,ty,tx,a,d)
      add_edge(y,x,by,bx,a,d)
      add_edge(y,x,ry,rx,a,d)
      add_edge(y,x,ly,lx,a,d)


def print_map(arr):
  s = ''
  for row in arr:
    for c in row:
      s += c
    s += '\n'
  print(s)

def get_path(A,B):
  (y0,x0) = (targets[A][0],targets[A][1])
  (y1,x1) = (targets[B][0],targets[B][1])
  return path(y0,x0,y1,x1)

def path(y0,x0,y1,x1):
  unvisited = {node: None for node in nodes} #using None as +inf
  visited = {}
  current = str(y0) + ',' + str(x0)
  currentDistance = 0
  unvisited[current] = currentDistance
  while True:
      for neighbour, distance in distances[current].items():
          if neighbour not in unvisited: continue
          newDistance = currentDistance + distance
          if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
              unvisited[neighbour] = newDistance
      visited[current] = currentDistance
      del unvisited[current]
      if not unvisited: break
      candidates = [node for node in unvisited.items() if node[1]]
      if len(candidates) == 0:
        break
      current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

  dest = str(y1) + ',' + str(x1)
  return visited[dest]

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

rows = len(l)
cols = len(l[0])
arr = [[' ' for x in range(cols)] for y in range(rows)]

targets = {}  # dictionary target 0-7 (int), [y,x] int,int

for y in range(rows):
  for x in range(cols):
    c = l[y][x]
    if c.isnumeric():
      c = int(c)
      targets[c] = [y,x]
    arr[y][x] = c
# targets:
# {0: [1, 175], 2: [3, 49], 1: [7, 7], 4: [17, 165], 3: [19, 1], 7: [31, 11], 5: [31, 177], 6: [33, 43]}
#print(targets)

nodes = () # tuple
for y in range(rows):
  for x in range(cols):
    if arr[y][x] != '#':
      nodes = nodes + ( str(y) + ',' + str(x), ) # add tuple to tuple

distances = {}
add_edges(distances,arr)
"""
for key, value in distances.items():
  print(str(key) + ': ' + str(value))
print()
"""

# 5 to others
arr = [0,5,4,2,3,1,7,6] # 
A = arr[-1]
for i in range(0,8):
  if i in arr:
    continue
  print(str(A) + ' -> ' + str(i) + '  ' + str(get_path(A,i)) + ' steps.' )
print()
"""
0 -> 1  266 steps.
0 -> 2  208 steps.
0 -> 3  252 steps.
0 -> 4  26 steps. *****
0 -> 5  44 steps. *****
0 -> 6  196 steps.
0 -> 7  246 steps.
"""

path_back = {}
for i in range(1,8):
  dist = get_path(i,0)
  path_back[i] = dist

# try
steps = 0
orders1 = [''.join(p) for p in permutations('12367')]
orders2 = [ '045'+s for s in orders1 ]
orders3 = [ '054'+s for s in orders1 ]
orders = orders2 + orders3
#print('orders: ' + str(len(orders)))
#print()

order_num = 1
for order in orders:
  steps = 0
  for i in range(0,len(order)-1):
    A=int(order[i])
    B=int(order[i+1])
    (y0,x0) = (targets[A][0],targets[A][1])
    (y1,x1) = (targets[B][0],targets[B][1])
    steps += path(y0,x0,y1,x1)

  # add steps back to 0
  last_node = int(order[-1])
  steps += path_back[last_node]
  print(str(steps) + '    ' + str(order_num) + '.  order: ' + order + '    steps = ' + str(steps))
  order_num += 1

# order: 04513627    steps = 550
# order: 04513267    steps = 538
# order: 04531762    steps = 504
# order: 04573126    steps = 492
# 466 too high: 04526317
# 458 too high: 05462317
# 454 too high: 04562317
# 446 too high: 04526731
#   04562137    steps = 442 RIGHT!!!!
#
# 402 too low

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

"""
660    26.  order: 04521376    steps = 660
660    95.  order: 04567312    steps = 660
664    146.  order: 05421376    steps = 664
664    215.  order: 05467312    steps = 664
672    32.  order: 04523176    steps = 672
672    92.  order: 04567132    steps = 672
676    152.  order: 05423176    steps = 676
676    212.  order: 05467132    steps = 676
684    43.  order: 04527136    steps = 684
684    45.  order: 04527316    steps = 684
684    76.  order: 04561372    steps = 684
684    86.  order: 04563172    steps = 684
688    109.  order: 04573126    steps = 688
688    163.  order: 05427136    steps = 688
688    165.  order: 05427316    steps = 688
688    196.  order: 05461372    steps = 688
688    206.  order: 05463172    steps = 688
688    79.  order: 04562137    steps = 688
692    199.  order: 05462137    steps = 692
692    229.  order: 05473126    steps = 692
692    29.  order: 04521736    steps = 692
692    89.  order: 04563712    steps = 692
696    149.  order: 05421736    steps = 696
696    209.  order: 05463712    steps = 696
700    81.  order: 04562317    steps = 700
700    99.  order: 04571326    steps = 700
704    201.  order: 05462317    steps = 704
704    219.  order: 05471326    steps = 704
704    35.  order: 04523716    steps = 704
704    78.  order: 04561732    steps = 704
708    155.  order: 05423716    steps = 708
708    198.  order: 05461732    steps = 708
712    100.  order: 04571362    steps = 712
712    11.  order: 04513726    steps = 712
712    110.  order: 04573162    steps = 712
712    12.  order: 04513762    steps = 712
712    37.  order: 04526137    steps = 712
712    39.  order: 04526317    steps = 712
712    41.  order: 04526713    steps = 712
712    42.  order: 04526731    steps = 712
712    53.  order: 04531726    steps = 712
712    54.  order: 04531762    steps = 712
712    83.  order: 04562713    steps = 712
712    84.  order: 04562731    steps = 712
716    131.  order: 05413726    steps = 716
716    132.  order: 05413762    steps = 716
716    157.  order: 05426137    steps = 716
716    159.  order: 05426317    steps = 716
716    161.  order: 05426713    steps = 716
716    162.  order: 05426731    steps = 716
716    173.  order: 05431726    steps = 716
716    174.  order: 05431762    steps = 716
716    203.  order: 05462713    steps = 716
716    204.  order: 05462731    steps = 716
716    220.  order: 05471362    steps = 716
716    230.  order: 05473162    steps = 716
720    67.  order: 04537126    steps = 720
720    80.  order: 04562173    steps = 720
724    187.  order: 05437126    steps = 724
724    200.  order: 05462173    steps = 724
732    21.  order: 04517326    steps = 732
732    82.  order: 04562371    steps = 732
736    141.  order: 05417326    steps = 736
736    202.  order: 05462371    steps = 736
744    103.  order: 04572136    steps = 744
744    119.  order: 04576312    steps = 744
744    22.  order: 04517362    steps = 744
744    25.  order: 04521367    steps = 744
744    38.  order: 04526173    steps = 744
744    40.  order: 04526371    steps = 744
744    50.  order: 04531276    steps = 744
744    68.  order: 04537162    steps = 744
744    85.  order: 04563127    steps = 744
744    93.  order: 04567213    steps = 744
748    142.  order: 05417362    steps = 748
748    145.  order: 05421367    steps = 748
748    158.  order: 05426173    steps = 748
748    160.  order: 05426371    steps = 748
748    170.  order: 05431276    steps = 748
748    188.  order: 05437162    steps = 748
748    205.  order: 05463127    steps = 748
748    213.  order: 05467213    steps = 748
748    223.  order: 05472136    steps = 748
748    239.  order: 05476312    steps = 748
756    105.  order: 04572316    steps = 756
756    116.  order: 04576132    steps = 756
756    31.  order: 04523167    steps = 756
756    75.  order: 04561327    steps = 756
756    8.  order: 04513276    steps = 756
756    94.  order: 04567231    steps = 756
760    128.  order: 05413276    steps = 760
760    151.  order: 05423167    steps = 760
760    195.  order: 05461327    steps = 760
760    214.  order: 05467231    steps = 760
760    225.  order: 05472316    steps = 760
760    236.  order: 05476132    steps = 760
764    111.  order: 04573216    steps = 764
764    2.  order: 04512376    steps = 764
764    56.  order: 04532176    steps = 764
764    73.  order: 04561237    steps = 764
764    87.  order: 04563217    steps = 764
764    91.  order: 04567123    steps = 764
764    96.  order: 04567321    steps = 764
764    97.  order: 04571236    steps = 764
768    10.  order: 04513672    steps = 768
768    122.  order: 05412376    steps = 768
768    176.  order: 05432176    steps = 768
768    193.  order: 05461237    steps = 768
768    207.  order: 05463217    steps = 768
768    211.  order: 05467123    steps = 768
768    216.  order: 05467321    steps = 768
768    217.  order: 05471236    steps = 768
768    231.  order: 05473216    steps = 768
768    47.  order: 04527613    steps = 768
768    48.  order: 04527631    steps = 768
768    52.  order: 04531672    steps = 768
772    117.  order: 04576213    steps = 772
772    130.  order: 05413672    steps = 772
772    167.  order: 05427613    steps = 772
772    168.  order: 05427631    steps = 772
772    172.  order: 05431672    steps = 772
772    49.  order: 04531267    steps = 772
776    113.  order: 04573612    steps = 776
776    169.  order: 05431267    steps = 776
776    237.  order: 05476213    steps = 776
776    27.  order: 04521637    steps = 776
776    28.  order: 04521673    steps = 776
776    30.  order: 04521763    steps = 776
776    5.  order: 04512736    steps = 776
776    65.  order: 04536712    steps = 776
776    69.  order: 04537216    steps = 776
776    71.  order: 04537612    steps = 776
776    74.  order: 04561273    steps = 776
776    90.  order: 04563721    steps = 776
780    125.  order: 05412736    steps = 780
780    147.  order: 05421637    steps = 780
780    148.  order: 05421673    steps = 780
780    150.  order: 05421763    steps = 780
780    185.  order: 05436712    steps = 780
780    189.  order: 05437216    steps = 780
780    191.  order: 05437612    steps = 780
780    194.  order: 05461273    steps = 780
780    210.  order: 05463721    steps = 780
780    233.  order: 05473612    steps = 780
784    118.  order: 04576231    steps = 784
784    7.  order: 04513267    steps = 784
788    102.  order: 04571632    steps = 788
788    127.  order: 05413267    steps = 788
788    18.  order: 04516732    steps = 788
788    19.  order: 04517236    steps = 788
788    238.  order: 05476231    steps = 788
788    24.  order: 04517632    steps = 788
788    33.  order: 04523617    steps = 788
788    34.  order: 04523671    steps = 788
788    36.  order: 04523761    steps = 788
788    59.  order: 04532716    steps = 788
788    77.  order: 04561723    steps = 788
788    88.  order: 04563271    steps = 788
792    138.  order: 05416732    steps = 792
792    139.  order: 05417236    steps = 792
792    144.  order: 05417632    steps = 792
792    153.  order: 05423617    steps = 792
792    154.  order: 05423671    steps = 792
792    156.  order: 05423761    steps = 792
792    179.  order: 05432716    steps = 792
792    197.  order: 05461723    steps = 792
792    208.  order: 05463271    steps = 792
792    222.  order: 05471632    steps = 792
796    107.  order: 04572613    steps = 796
796    108.  order: 04572631    steps = 796
796    51.  order: 04531627    steps = 796
796    9.  order: 04513627    steps = 796
800    129.  order: 05413627    steps = 800
800    16.  order: 04516372    steps = 800
800    171.  order: 05431627    steps = 800
800    227.  order: 05472613    steps = 800
800    228.  order: 05472631    steps = 800
800    44.  order: 04527163    steps = 800
800    46.  order: 04527361    steps = 800
800    62.  order: 04536172    steps = 800
804    114.  order: 04573621    steps = 804
804    136.  order: 05416372    steps = 804
804    164.  order: 05427163    steps = 804
804    166.  order: 05427361    steps = 804
804    182.  order: 05436172    steps = 804
804    3.  order: 04512637    steps = 804
804    4.  order: 04512673    steps = 804
804    63.  order: 04536217    steps = 804
804    72.  order: 04537621    steps = 804
804    98.  order: 04571263    steps = 804
808    123.  order: 05412637    steps = 808
808    124.  order: 05412673    steps = 808
808    183.  order: 05436217    steps = 808
808    192.  order: 05437621    steps = 808
808    218.  order: 05471263    steps = 808
808    234.  order: 05473621    steps = 808
816    101.  order: 04571623    steps = 816
816    112.  order: 04573261    steps = 816
816    13.  order: 04516237    steps = 816
816    23.  order: 04517623    steps = 816
816    57.  order: 04532617    steps = 816
816    58.  order: 04532671    steps = 816
820    133.  order: 05416237    steps = 820
820    143.  order: 05417623    steps = 820
820    177.  order: 05432617    steps = 820
820    178.  order: 05432671    steps = 820
820    221.  order: 05471623    steps = 820
820    232.  order: 05473261    steps = 820
828    14.  order: 04516273    steps = 828
828    20.  order: 04517263    steps = 828
828    64.  order: 04536271    steps = 828
828    70.  order: 04537261    steps = 828
832    134.  order: 05416273    steps = 832
832    140.  order: 05417263    steps = 832
832    184.  order: 05436271    steps = 832
832    190.  order: 05437261    steps = 832
848    1.  order: 04512367    steps = 848
848    115.  order: 04576123    steps = 848
848    120.  order: 04576321    steps = 848
848    55.  order: 04532167    steps = 848
852    121.  order: 05412367    steps = 852
852    175.  order: 05432167    steps = 852
852    235.  order: 05476123    steps = 852
852    240.  order: 05476321    steps = 852
860    104.  order: 04572163    steps = 860
860    6.  order: 04512763    steps = 860
860    61.  order: 04536127    steps = 860
860    66.  order: 04536721    steps = 860
864    126.  order: 05412763    steps = 864
864    181.  order: 05436127    steps = 864
864    186.  order: 05436721    steps = 864
864    224.  order: 05472163    steps = 864
872    106.  order: 04572361    steps = 872
872    15.  order: 04516327    steps = 872
872    17.  order: 04516723    steps = 872
872    60.  order: 04532761    steps = 872
876    135.  order: 05416327    steps = 876
876    137.  order: 05416723    steps = 876
876    180.  order: 05432761    steps = 876
876    226.  order: 05472361    steps = 876

"""