import numpy
from math import sqrt, atan2, cos, sin

eta = 1.
g = 1.
Ra = g/eta
R1, R2 = 1.22, 2.22
n = 2
k = 2

if n>1:
    A5 = R1**2*R2**(4*n + 2) + R1**(4*n + 2)*R2**2 - (R1**(2*n)*R2**4 + R1**(2*n + 4))*R2**(2*n)
    # velocity: coefficients for n, -n, n+2, -n+2 and k+3 powers off r
    C = -Ra * (R1**(k + n + 1) - R2**(k + n + 1))*R1**2*R2**2/((R1**n*R2 + R1*R2**n)*(R1*R2**n - R1**n*R2)*(k + n + 1)*(k - n + 3))/4.
    D = -Ra * (R1**n*R2**(k + 1) - R1**(k + 1)*R2**n)*R1**(n + 2)*R2**(n + 2)/((R1**(n + 1) + R2**(n + 1))*(R1**(n + 1) - R2**(n + 1))*(k + n + 3)*(k - n + 1))/4.
    E = -Ra * (R1**(k + n + 3) - R2**(k + n + 3))*g/((R1**(n + 1) + R2**(n + 1))*(R1**(n + 1) - R2**(n + 1))*(k + n + 3)*(k - n + 1))/4.
    F = -Ra * (R1**n*R2**(k + 3) - R1**(k + 3)*R2**n)*R1**n*R2**n*g/((R1**n*R2 + R1*R2**n)*(R1*R2**n - R1**n*R2)*(k + n + 1)*(k - n + 3))/4.
    A0 = Ra * n / (((k+3)**2-n**2)*((k+1)**2-n**2))

    # pressure: coefficients for n, -n, and k+1
    G = -4*eta*E*(n+1)
    H = -4*eta*F*(n-1)
    K = -g*(k + 1)/((k+1)**2-n**2)
else:
    raise NotImplemented()


def u_r(r, theta):
    dpsi_dtheta = n*cos(n*theta)*(C*r**n+D*r**(-n)+E*r**(n+2)+F*r**(-n+2)+A0*r**(k+3))
    return -dpsi_dtheta/r

numpy.testing.assert_almost_equal(u_r(R1, 0.), 0.)
numpy.testing.assert_almost_equal(u_r(R2, 0.), 0.)

def u_theta(r, theta):
    dpsi_dr = sin(n*theta)*(C*n*r**(n-1) + D*-n*r**(-n-1) + E*(n+2)*r**(n+1) + F*(-n+2)*r**(-n+1)+A0*(k+3)*r**(k+2))
    return dpsi_dr

def p(r, theta):
    return (G*r**n + H*r**(-n) + K*r**(k+1))*cos(n*theta)

def delta_rho(r, theta):
    return r**k * cos(n*theta)

def get_cartesian_solution(X):
    r = sqrt(X[0]**2+X[1]**2)
    theta = atan2(X[1], X[0])
    ur = u_r(r,theta)
    ut = u_theta(r,theta)
    return [ur*X[0]/r - ut*X[1]/r, ur*X[1]/r + ut*X[0]/r]

def get_cartesian_pressure_solution(X):
    r = sqrt(X[0]**2+X[1]**2)
    theta = atan2(X[1], X[0])
    return p(r, theta)

def delta_rho_cartesian(X):
    r = sqrt(X[0]**2+X[1]**2)
    theta = atan2(X[1], X[0])
    return delta_rho(r, theta)
