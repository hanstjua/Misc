import pyopencl as cl
from pyopencl import array
import numpy as np
import random as rd
import time

seed = time.time()
iter_num = 900

print()
print('[1000x1000]MATRIX-[1000x1]VECTOR DOT PRODUCT,', iter_num ,'iterations')

print()
print('Preparing for SERIAL computation ...')

mat = np.zeros((1000,1000))
vec = np.zeros((1000,1))

rd.seed(seed)

for i in range(1000):
    for j in range(1000):
        mat[i,j] = rd.randint(0,250)

mat = np.array(mat)

for i in range(1000):
    vec[i,0] = rd.randint(0,250)

vec = np.array(vec)

print('Preparation DONE.')

exec("""
print('Computing ...')
start = time.time()
count = 0
while count<iter_num:
    res = np.dot(mat,vec)
    count += 1
print('SERIAL computation DONE.  >>  Time :',time.time()-start,'sec')
""")

print()
print('Preparing for PARALLEL computation ...')

rd.seed(seed)

vector = np.zeros((250, 1), cl.array.vec.float4)
matrix = np.zeros((250, 1000), cl.array.vec.float4)
iterations = np.array([iter_num], cl.cltypes.int)
iterations = np.uint16(iter_num)

dim = ""

for i in range(1000):
    for j in range(250):
        partial = []
        for k in range(4):
            partial.append(rd.randint(0,250))
        matrix[j,i] = tuple(partial)
        dim = str(j) + ' x ' + str(i)

for i in range(250):
    partial = []
    for j in range(4):
        partial.append(rd.randint(0,250))
    vector[i,0] = tuple(partial)
    dim = str(i) + ' x 0'

## Step #250. Obtain an OpenCL platform.
platform = cl.get_platforms()[0]
 
## It would be necessary to add some code to check the check the support for
## the necessary platform extensions with platform.extensions
 
## Step #2. Obtain a device id for at least one device (accelerator).
device = platform.get_devices()[0]
 
## It would be necessary to add some code to check the check the support for
## the necessary device extensions with device.extensions
 
## Step #3. Create a context for the selected device.
context = cl.Context([device])
 
## Step #4. Create the accelerator program from source code.
## Step #5. Build the program.
## Step #6. Create one or more kernels from the program functions.
program = cl.Program(context, """
    __kernel void matrix_dot_vector(__global const float4 *matrix,
    __global const float4 *vector, __global float *result)
    {
      int gid = get_global_id(0);
      int count = 0;
      while(count<"""+str(iter_num)+""")
      {
          result[gid] = dot(matrix[gid], vector[0]);
          result[gid] = dot(matrix[gid],matrix[gid]);
          count++;
      }
    }
    """).build()

## Step #7. Create a command queue for the target device.
queue = cl.CommandQueue(context)
 
## Step #8. Allocate device memory and move input data from the host to the device memory.
mem_flags = cl.mem_flags
#iter_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=iterations)
matrix_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=matrix)
vector_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=vector)
matrix_dot_vector = np.zeros(4, np.float32)
destination_buf = cl.Buffer(context, mem_flags.WRITE_ONLY, matrix_dot_vector.nbytes)

print('Preparation DONE.')

## Step #9. Associate the arguments to the kernel with kernel object.
## Step #10. Deploy the kernel for device execution.
exec("""
print('Computing ...')
start = time.time()
program.matrix_dot_vector(queue, matrix_dot_vector.shape, None, matrix_buf, vector_buf, destination_buf)
print('PARALLEL computation DONE.  >>  Time :',time.time()-start,'sec')
""")

## Step #11. Move the kernel’s output data to host memory.
cl.enqueue_copy(queue, matrix_dot_vector, destination_buf)
 
## Step #12. Release context, program, kernels and memory.
## PyOpenCL performs this step for you, and therefore,
## you don't need to worry about cleanup code
 
#print(matrix_dot_vector[250,23])

