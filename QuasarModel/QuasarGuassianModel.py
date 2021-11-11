import numpy as np
import matplotlib.pyplot as plt

def sersic(filename, pixels, noise):                         # Defining function

    data = np.loadtxt(filename)                              # Import data
    xpixel, ypixel, B, r0, index = (data[:,0] , data[:,1],
                                    data[:,2] , data[:,3],   # Applying column data to variables
                                    data[:,4])               # xpixel/ypixel are the centre points of galaxies used later for distance to other pixels (r).
        
    x = np.linspace(1,pixels,pixels)                         # Lists of pixels
    y = np.linspace(1,pixels,pixels)

    xx, yy = np.meshgrid(x,y)                                # Meshgrid of pixels
    
    a = np.random.normal(0,noise,(pixels,pixels))            # Random gaussian noise
                                                                                            
    for i in range(len(data)):                               # Looping over galaxies (example for this data is 3 galaxies)
                                                             # Note that xpixel/ypixel are the centre of the galaxies and not an array of pixels

        r = ((xx - xpixel[i])**2 + (yy - ypixel[i])**2)**0.5 # length to each pixel from galactic centre
        a += B[i]*np.exp(-(r/r0[i])**(1/index[i]))           # Brightness of each pixel relative to a galaxy added to noise array

    return(a)                                                # Returning galaxy data

a = sersic("filename.txt", 100, 0.1)                         # a equals function with these inputs

plt.imshow(a,origin='lower',cmap='jet')                      # Plotting
plt.show()

