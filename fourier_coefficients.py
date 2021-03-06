'''
Calculate Fourier coefficients of a 1D function.

This code improves over Ed Barry's by using Simpson's rule
to perform the numerical integration to calculate Fourier coefficients,
instead of what amounts to using a rectangular Riemann sum. 

Also, take care to consider Nyquist.
'''

import numpy as np
from numpy import arange, sin, cos, pi, floor
from scipy.integrate import simps

def coeffs_n(y, n, x = None):
    if x is None:
        x = arange(len(y))
    L = x[-1] - x[0]
    cos_terms = cos(n * 2. * pi * x / L)
    sin_terms = sin(n * 2. * pi * x / L)
    # off by factor of 2 for a_0
    a_n = 2. / L * simps(y * cos_terms, x)
    b_n = 2. / L * simps(y * sin_terms, x)
    return a_n, b_n

def coeffs_n2(y, n, x = None):
    # take convention of evenness, periodicity -L to L but symmetry assumed
    # therefore there are only cosine terms
    if x is None:
        x = arange(len(y))
    L = x[-1] - x[0]
    cos_terms = cos(n * pi * x / L) # change definition of q vs coeffs_n
    # off by factor of 2 for a_0
    a_n = 2. / L * simps(y * cos_terms, x) # prefactor stays the same
    return a_n


def fourier_coeffs(y, x = None, n_max = None):
    '''
    output from n = 0
    '''
    if x is None:
        x = arange(len(y))
    if n_max is None:
        n_max = floor(len(y)/2)
    coeffs = np.array([coeffs_n(y, n, x) for n in arange(n_max + 1)])
    a_ns = coeffs[:,0]
    # fix factor of 2 in a_0
    a_ns[0] *= 0.5
    b_ns = coeffs[:,1]
    return a_ns, b_ns


def fourier_coeffs2(y, x = None, n_max = None):
    '''
    output from n = 0
    '''
    if x is None:
        x = arange(len(y))
    if n_max is None:
        n_max = floor(len(y)/2)
    a_ns = np.array([coeffs_n2(y, n, x) for n in arange(n_max + 1)])
    # fix factor of 2 in a_0
    a_ns[0] *= 0.5
    return a_ns

