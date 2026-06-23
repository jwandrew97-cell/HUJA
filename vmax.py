from astropy.cosmology import FlatLambdaCDM
import numpy as np

dz = 0.01
zmin = 7.5
zmax = 8.5

field_area = 1.7201431257141546 # COSMOS
field_area = 0.6536 # Euclid COSMOS #TODO: check which one i neeeeed

# TODO: Workout the argument we need to pass to the function and which ones are intrinsic
# TODO: Decide the output of the function i.e. in list or fits? -> Possibly a numpy array and \
# create a seperate function for converting the array output to a fits?
# TODO: Add docstring to the function

def calc_vmax_from_z(field_area, zmin, zmax, dz=0.1):
    # Define the cosmology
    H = 70
    omegaM = 0.3
    omegaV = 0.7
    cosmo = FlatLambdaCDM(H0=H, Om0=omegaM)

    # Convert field area into steradians
    field_area_ster = field_area * (np.pi / 180)**2

    # Initialise list of volumes
    Vmaxs = []

    # Compute the volume
    z = zmin
    while z <= zmax:
        z += dz
        V = field_area_ster/3 * (cosmo.comoving_distance(z)**3 - cosmo.comoving_distance(zmin)**3)
        maximum_V = field_area_ster/3 * (cosmo.comoving_distance(zmax)**3 - cosmo.comoving_distance(zmin)**3)
        Vmax = min(V, maximum_V)
        Vmaxs.append(Vmax)
        #print('Vmax =', Vmax)
        #print('Maximum Vmax =', maximum_V)
        
    return Vmaxs

# test = calc_vmax_from_z(field_area, zmin, zmax)
# print(test)





