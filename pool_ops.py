# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
# This script calculates the output shape and operation count of an average pooling layer.
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# h_pool: average pooling kernel height count
# w_pool: average pooling kernel width count
# s: stride of average pooling kernel
# p: amount of padding on each of the four input map sides
# Output:
# The script prints the following values:
# - Output channel count
# - Output height count
# - Output width count
# - Number of additions performed
# - Number of multiplications performed
# - Number of divisions performed
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys

# Parse script arguments
if len(sys.argv) != 8:
    print('Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p')
    sys.exit(1)

c_in = int(sys.argv[1])
h_in = int(sys.argv[2])
w_in = int(sys.argv[3])
h_pool = int(sys.argv[4])
w_pool = int(sys.argv[5])
s = int(sys.argv[6])
p = int(sys.argv[7])

# Calculate output dimensions
h_out = (h_in - h_pool + 2 * p) // s + 1
w_out = (w_in - w_pool + 2 * p) // s + 1
c_out = c_in

# Calculate the number of operations
adds = c_in * h_out * w_out * (h_pool * w_pool - 1)
muls = 0  
divs = c_in * h_out * w_out  

# Print the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed
