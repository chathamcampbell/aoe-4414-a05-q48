# pool_ops.p
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#  Determine the output shape and operation count of a pooling layer
# Parameters:
# c_in: input channel count 
# h_in: input height count
# w_in: inout width count
# h_pool: number of filters in the convolution layer
# w_pool: filter height count
# s: stride of convolution filters
# p: amount of padding on each of the four input map sides
# # Output:
# A description of the script output
# c_out: output channel count
# h_out: output height count
# w_out: output width count
# adds: number of additions performed
# muls: number of multiplications performed
# divs: number of divisions performed
#
# Written by Chatham Campbell
# Other contributors: None
#

# import Python modules

import sys # argv
import math

#initialize script arguments
c_in = float('nan') 
h_in = float('nan') 
w_in = float('nan') 
h_pool = float('nan')
w_pool = float('nan')
s = float('nan')
p = float('nan')

#parse script arguments
if len(sys.argv)==8:
  c_in = int(sys.argv[1])
  h_in = int(sys.argv[2])
  w_in = int(sys.argv[3])
  h_pool = int(sys.argv[4])
  w_pool = int(sys.argv[5])
  s = int(sys.argv[6])
  p = int(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'
  )
  exit()

# write script below this line

c_out = c_in
h_out = ((h_in+(2.0*p) - h_pool)/s)+1.0
w_out = ((w_in + (2.0*p)- w_pool)/s)+1.0

adds = c_in*h_out*w_out*(h_pool*w_pool-1)
muls = 0
divs = c_in*h_out*w_out


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
#python3 pool_ops.py 4 28 28 2 2 2 0