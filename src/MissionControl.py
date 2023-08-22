import numpy as np

class MissionControl:
    """
    Razred, ki simulira gibanje vesoljskega plovila Apollo v poenostavljenem sistemu Zemlje in Lune.

    Attributes:
        EARTH_MASS (float): Masa Zemlje v kilogramih.
        MOON_MASS (float): Masa Lune v kilogramih.
        EARTH_FRACTION (float): Delež mase Zemlje v sistemu.
        MOON_FRACTION (float): Delež mase Lune v sistemu.
        EARTH_MOON_DISTANCE (int): Razdalja med Zemljo in Luno v kilometrih.
        EARTH_DIAMETER (int): Premer Zemlje v kilometrih.
        POSITION_SURFACE (float): Relativna pozicija plovila na površini Zemlje.
        POSITION_STABLE_ORBIT (float): Relativna pozicija plovila v stabilni orbiti.
        GRAVITATIONAL_CONSTANT (float): Gravitacijska konstanta v m^3 kg^-1 s^-2.

    Methods:
        Fx1, Fx2, Fy1, Fy2, Fz1, Fz2, newR, newr, ApolloMissionSimulationStep
    """

    EARTH_MASS = 5.97 * 10e24 
    MOON_MASS = 7.35 * 10e22
    EARTH_FRACTION = EARTH_MASS/(EARTH_MASS+MOON_MASS)
    MOON_FRACTION = MOON_MASS/(EARTH_MASS+MOON_MASS)
    EARTH_MOON_DISTANCE = 384400
    EARTH_DIAMETER = 6371
    POSITION_SURFACE = EARTH_DIAMETER/EARTH_MOON_DISTANCE
    POSITION_STABLE_ORBIT = (EARTH_DIAMETER+350)/EARTH_MOON_DISTANCE
    GRAVITATIONAL_CONSTANT = 6.67430e-11


    def __init__():
        pass

    def Fx1(self, x, R):
        return (self.EARTH_FRACTION/R**3) * (x + self.MOON_FRACTION)
    def Fx2(self, x, r):
        return (self.MOON_FRACTION/r**3) * (x - self.EARTH_FRACTION)
    def Fy1(self, y, R):
        return (self.EARTH_FRACTION/R**3) * y
    def Fy2(self, y, r):
        return (self.MOON_FRACTION/r**3) * y
    def Fz1(self, z, R):
        return self.Fy1(self, z,R)
    def Fz2(self, z, r):
        return self.Fy2(self, z, r)
    def newR(self, x,y,z):
        """
        Izračuna razdaljo od vesoljskega plovila do masnega središča Zemlje.

        Arguments:
            x (float): x-koordinata vesoljskega plovila.
            y (float): y-koordinata vesoljskega plovila.
            z (float): z-koordinata vesoljskega plovila.

        Returns:
            float: Razdalja od vesoljskega plovila do masnega središča Zemlje.
        """
        return np.sqrt((x+self.MOON_FRACTION)**2 + y**2 + z**2)
    def newr(self, x,y,z):
        """
        Izračuna razdaljo od vesoljskega plovila do masnega središča Lune.

        Arguments:
            x (float): x-koordinata vesoljskega plovila.
            y (float): y-koordinata vesoljskega plovila.
            z (float): z-koordinata vesoljskega plovila.

        Returns:
            float: Razdalja od vesoljskega plovila do središča Lune.
        """
        return np.sqrt((x-self.EARTH_FRACTION)**2 + y**2 + z**2)
    

    def ApolloMissionSimulationStep(self, variables, t):
        """
        Simulira gibanje vesoljskega plovila Apollo v sistemu Zemlje in Lune.

        Arguments:
            spremenljivke (list): Seznam spremenljivk vesoljskega plovila [hitrost_x, pospešek_x, histrost_y, pospešek_y, hitrost_z, pospešek_z].
            t (float): Časovni parameter (ni uporabljen v tej funkciji).

        Returns:
            tuple: Posodobljene vrednosti spremenljivk vesoljskega plovila [x_, x__, y_, y__, z_, z__].
        """
        x, x_, y, y_, z, z_ = variables
        R,r = self.newR(self, x,y,z),self.newr(self, x,y,z)
        x__ = x + 2* y_ - self.Fx1(self, x, R) - self.Fx2(self, x, r)
        y__ = y - 2* x_ - self.Fy1(self, y, R) - self.Fy2(self, y, r)
        z__ = - self.Fz1(self, z, R) - self.Fz2(self, z, r)

        return x_,x__,y_,y__,z_,z__