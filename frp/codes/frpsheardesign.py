import math

class FRPShearDesign:
    def __init__(self):
        self.Le = 0
        self.n = 0
        self.tf = 0
        self.Ef = 0
        self.k1 = 0
        self.fc = 0
        self.k2 = 0
        self.dfv = 0
        self.Kv = 0
        self.efu = 0
        self.efe = 0
        self.Afv = 0
        self.ffe = 0
        self.Vf = 0
        self.alpha = 0
        self.sf = 0
        self.Vc = 0
        self.Vs = 0
        self.reductionfactor = 0
        self.oVn = 0
        self.FRPShearReductionFactor = 0
        self.frp_print = []

    def EffectiveStrain(self, n, tf, Ef, fc, dfv, efu, SRF, sheardesign):
        self.n = n
        self.tf = tf
        self.Ef = Ef
        self.fc = fc
        self.dfv = dfv
        self.efu = efu
        if sheardesign == 2:
            self.reductionfactor = 0.85
            self.efe = min(0.75 * self.efu, 0.004)
            self.frp_print.append('ε_fe = 0.004 ≤ 0.75 ε_fu')
            self.frp_print.append('ε_fe = minimum (0.75 * '+str(self.efu)+', 0.004)')
        else:
            self.reductionfactor = 0.75
            self.Le = 23300 / (self.n * self.tf * self.Ef) ** 0.58
            self.frp_print.append('Le = 23,300 / [ n tf Ef ]^0.58')
            self.frp_print.append('Le = 0.004 ≤ 0.75 ε_fu')
            self.frp_print.append('Le = ' + str(self.Le))
            self.k1 = (self.fc / 27) ** (2 / 3)
            self.frp_print.append("k1 = ( fc' / 27 )^(2/3)")
            self.frp_print.append('k1 = ( ' + str(self.fc)+' / 27 )^(2/3)')
            self.frp_print.append('k1 = ' + str(self.k1))
            if SRF == 2:
                self.k2 = (self.dfv - self.Le) / self.dfv
                self.frp_print.append('k2 = (dfv - Le) / dfv   for three sides bonded')
                self.frp_print.append('k2 = ('+str(self.dfv)+'  - '+str(self.Le)+') / '+str(self.dfv))
            elif SRF == 3:
                self.k2 = (self.dfv - 2 * self.Le) / self.dfv
                self.frp_print.append('k2 = (dfv - 2 Le) / dfv   for two sides bonded')
                self.frp_print.append('k2 = (' + str(self.dfv) + '  - 2 * ' + str(self.Le) + ') / ' + str(self.dfv))
            self.frp_print.append('k2 = ' + str(self.k2))
            self.Kv = min(self.k1 * self.k2 * self.Le / 11900 / self.efu, 0.75)
            self.frp_print.append('Kv = (k1 k2 Le) / (11,900 εfu) ≤ 0.75')
            self.frp_print.append('Kv = min('+str(self.k1)+' * '+str(self.k2)+' * '+str(self.Le)+' / 11900 / ' +
                                  str(self.efu)+', 0.75)')
            self.frp_print.append('Kv = ' + str(self.Kv))
            self.efe = min(self.Kv * self.efu, 0.004)
            self.frp_print.append('ε_fe = Kv ε_fu  ≤ 0.004')
            self.frp_print.append('ε_fe = ' + str(self.Kv) + ' * ' + str(self.efu) + ', 0.004)')
        self.frp_print.append('ε_fe = ' + str(self.efe))
        self.frp_print.append('φ shear reduction factor = ' + str(self.reductionfactor))

    def FRPShearStrength(self, Afv, alpha, sf, Vc, Vs, FRPshear, designtype, bonded=1):
        self.Afv = Afv
        self.alpha = math.radians(alpha)
        print(alpha)
        self.sf = sf
        self.Vc = Vc
        self.Vs = Vs
        self.FRPShearReductionFactor = FRPshear
        self.ffe = self.Ef * self.efe
        self.frp_print.append('ffe = ε_fe * Ef')
        self.frp_print.append('ffe = ' + str(self.Ef) + ' * ' + str(self.efe))
        self.frp_print.append('ffe = ' + str(self.ffe))
        if designtype == 3:
            if bonded == 2:
                self.Vf = 2 * self.tf * self.efe * self.dfv * self.Ef / 1000
                self.frp_print.append('Vf = 2 tf ε_fe dfv Ef (FRP shear contribution for two sided)')
                self.frp_print.append('Vf = 2 * '+str(self.tf)+' * '+str(self.efe)+' * '+str(self.dfv)+' * ' +
                                      str(self.Ef)+' / 1000')
            else:
                self.Vf = 0.75 * self.tf * self.efe * self.dfv * self.Ef / 1000
                self.frp_print.append('Vf = 0.75 tf ε_fe dfv Ef (FRP shear contribution for one sided)')
                self.frp_print.append('Vf = 0.75 * '+str(self.tf)+' * '+str(self.efe)+' * '+str(self.dfv)+' * ' +
                                      str(self.Ef)+' / 1000')
            self.oVn = self.reductionfactor * (self.Vc + self.Vs + self.FRPShearReductionFactor * self.Vf)
        else:
            self.Vf = self.Afv * self.ffe * (math.sin(self.alpha) + math.cos(self.alpha)) * self.dfv / self.sf / 1000
            self.frp_print.append('Vf = Afv ffe (sin α + cos α) dfv / sf')
            self.frp_print.append('Vf = '+str(self.Afv)+' * '+str(self.ffe)+' * ('+str(math.sin(self.alpha)) +
                                  ' + '+str(math.cos(self.alpha))+') * '+str(self.dfv)+' / '+str(self.sf)+' / 1000')
            self.oVn = self.reductionfactor * (self.Vc + self.Vs + self.FRPShearReductionFactor * self.Vf)
        self.frp_print.append('Vf = ' + str(self.Vf))
        self.frp_print.append('φVn = φ [Vc + Vs + Ψf Vf]')
        self.frp_print.append('φVn = φ [' + str(self.Vc) + ' + ' + str(self.Vs) + ' + ' + str(self.FRPShearReductionFactor) + ' * ' + str(self.Vf) + ']')
        self.frp_print.append('φVn = ' + str(self.oVn))




