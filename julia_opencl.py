import math
import cmath
import graphics
import PIL
import pyopencl as cl
from pyopencl import array
import numpy as np
import matplotlib.pyplot as plt
import time
import math

from PIL import Image

from graphics import *

# in general size*scale in magnitude of 5 
plt.ion()
size = 500
xcoord = 0
ycoord = 0
xdist = 250
ydist = 250
scale = 0.004
c = 0.36 + 0.36j
cx = c.real
cy = c.imag
lp = 230

print("""size: {}
scale: {}
c: {}""".format(size,scale,c))

#xplot = []
#yplot = []
#color = [[0 for i in range(size+1)] for j in range(size+1)]

im = PIL.Image.new("RGB", (size,size))
pix = im.load()

#win = GraphWin('',size,size)
limit = 3

platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])

queue = cl.CommandQueue(context)

mem_flags = cl.mem_flags

print('Preparing matrices ...')

x_mat = np.zeros((size,size), np.float32)
y_mat = np.zeros((size,size), np.float32)

for i in range(size):
    for j in range(size):
        x_mat[i,j] = -xdist+j
        y_mat[i,j] = -ydist+i
        
# cx_mat = np.array(np.ones(x_mat.shape)*c.real, np.float32)
# cy_mat = np.array(np.ones(x_mat.shape)*c.imag, np.float32)

# x_1 = np.zeros(x_mat.shape, np.float32)
# y_1 = np.zeros(y_mat.shape, np.float32)

# x_2 = np.zeros(x_mat.shape, np.float32)
# y_2 = np.zeros(y_mat.shape, np.float32)

x_mat_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=x_mat)
y_mat_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=y_mat)
# cx_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf = cx)
# cy_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf = cy)
# lp_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf = lp)
# scale_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf = scale)
# limit_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf = limit)
# cx_mat_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=cx_mat)
# cy_mat_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=cy_mat)
# x_1_buf = cl.Buffer(context, mem_flags.READ_WRITE | mem_flags.COPY_HOST_PTR, hostbuf=x_1)
# y_1_buf = cl.Buffer(context, mem_flags.READ_WRITE | mem_flags.COPY_HOST_PTR, hostbuf=y_1)
# x_2_buf = cl.Buffer(context, mem_flags.READ_WRITE, hostbuf=x_2)
# y_2_buf = cl.Buffer(context, mem_flags.READ_WRITE, hostbuf=y_2)

fractal_matrix = np.zeros((size,size), np.float32)
dest_buf = cl.Buffer(context, mem_flags.WRITE_ONLY, fractal_matrix.nbytes)

print('Entering loop ...')

start = time.time()
for i in range(31):
    program = cl.Program(context,"""
    __kernel void fractal(__global const float *x_mat,__global const float *y_mat,
        __global float *result)
    {
        int i = get_global_id(0);
        int j = get_global_id(1);
        int s = """+str(size)+""";
        float x_2 = 0;
        float y_2 = 0;
        int lp = 0;
        
        float x_1 = x_mat[i*s+j]*"""+str(scale)+""";
        float y_1 = y_mat[i*s+j]*"""+str(scale)+""";

        while(lp<"""+str(lp)+""" && x_1*x_1 + y_1*y_1 <= """+str(limit)+"""){
            lp++;
            x_2 = x_1*x_1 - y_1*y_1 + """+str(cx)+""";
            y_2 = 2*x_1*y_1 + """+str(cy)+""";

            x_1 = x_2;
            y_1 = y_2;
        }

        if(lp>="""+str(lp)+"""){lp=0;}

        result[i*s+j] = lp;
    }
    """).build()
    program.fractal(queue, fractal_matrix.shape, None, x_mat_buf, y_mat_buf, dest_buf)

    cl.enqueue_copy(queue, fractal_matrix, dest_buf)

    # plt.show()
    image = plt.imshow(fractal_matrix)
    plt.pause(0.01)
    ang = math.pi/(400)*i
    cx = c.real*math.cos(ang)
    cy = c.imag*math.sin(ang)
    
    
#plt.show()
#pix = fractal_matrix
#im.show()
end = time.time()
print('Done.', end-start)
#print('Image created.')
#im.save("julia.tiff", "TIFF")
#print('Image saved.')
#im.show()

