class FRPBeamDesign:
    def __init__(self):
        self.nStrain = 0
        self.B = 0
        self.k = 0
        self.Icr = 0
        self.ebi = 0
        self.efd = 0
        self.c = 0
        self.c1 = 0
        self.b = 0
        self.d = 0
        self.efe = 0
        self.df = 0
        self.ec = 0
        self.ec1 = 0
        self.es = 0
        self.Es = 0
        self.fs = 0
        self.Ef = 0
        self.ffe = 0
        self.fc = 0
        self.fy = 0
        self.Ec = 0
        self.beta1 = 0
        self.alpha1 = 0
        self.As = 0
        self.Af = 0
        self.Mns = 0
        self.Mnf = 0
        self.addlreductionfactor = 0.85
        self.frpreductionfactor = 0.9
        self.oMn = 0
        self.rho_s = 0
        self.rho_f = 0
        self.fs_s = 0
        self.ff_s = 0
        self.ldf = 0
        self.n = 0
        self.tf = 0
        self.yb = 0
        self.yt = 0
        self.Pe = 0
        self.Acg = 0
        self.e = 0
        self.r = 0
        self.Ig = 0
        self.h = 0
        self.epnet = 0
        self.eps = 0
        self.epe = 0
        self.fps = 0
        self.fpe = 0
        self.ffe = 0
        self.Aps = 0
        self.epnets = 0
        self.epss = 0
        self.fpss = 0
        self.ecs = 0
        self.fcs = 0
        self.FRP_Beam = []
        self.frp_print = []

    def SoffitStrain(self, Es, Ec, b, As, d, MDL, df, yt, Pe, Acg, e, r, Ig, h, beamdesign):
        self.Es = Es
        self.Ec = Ec
        self.As = As
        self.b = b
        self.yt = yt
        self.Pe = Pe
        self.Acg = Acg
        self.e = e
        self.r = r
        self.Ig = Ig
        self.h = h
        self.d = d
        self.df = df
        self.nstrain = self.Es / self.Ec
        self.frp_print.append('n_strain = self.Es / self.Ec')
        self.frp_print.append('n_strain = '+str(self.Es)+' / '+str(self.Ec))
        self.frp_print.append('n_strain = '+str(self.nstrain))
        if beamdesign == 3:
            self.yb = self.h - self.yt
            self.frp_print.append('yb = h - yt')
            self.frp_print.append('yb = '+str(self.h)+' - '+str(self.yt))
            self.frp_print.append('yb = '+str(self.yb))
            self.ebi = -self.Pe/(self.Ec*self.Acg)*(1+self.e*self.yb/self.r**2)+MDL*self.yb/(self.Ec*self.Ig)*1000**2
            self.frp_print.append('ε_bi = - Pe / (Ec Acg) (1 + e yb / r^2) + MDL yb / (Ec Ig) * 1000^2  ')
            self.frp_print.append('ε_bi = -'+str(self.Pe)+'/('+str(self.Ec)+'*'+str(self.Acg)+')*(1+'+str(self.e) +
                                  '*'+str(self.yb)+'/'+str(self.r)+'^2)+'+str(MDL)+'*'+str(self.yb)+'/('+str(self.Ec) +
                                  '*'+str(self.Ig)+')*1000^2')
            self.frp_print.append('ε_bi = '+str(self.ebi))
            self.c = 0.1 * self.h
            self.frp_print.append('c = 0.1 * h')
            self.frp_print.append('c = 0.1 * '+str(self.h))
            self.frp_print.append('c = '+str(self.c))
        else:
            self.B = b / self.nstrain / self.As
            self.frp_print.append('B = b / n_strain / As')
            self.frp_print.append('B = '+str(b)+' / '+str(self.nstrain)+' / '+str(self.As))
            self.frp_print.append('B = '+str(self.B))
            self.k = ((2 * self.d * self.B + 1)**0.5 - 1) / self.B / self.d
            self.frp_print.append('k = [ (2 d B + 1)^0.5 - 1 ] / ( B d ) ')
            self.frp_print.append('k = ((2 * '+str(self.d)+' * '+str(self.B)+' + 1)^0.5 - 1) / '+str(self.B)+' / ' +
                                  str(self.d))
            self.frp_print.append('k = '+str(self.k))
            self.Icr = self.b * (self.k * self.d) ** 3 / 3 + self.nstrain * self.As * (self.d - self.k * self.d) ** 2
            self.frp_print.append('Icr = b (k d)^3 / 3  + n_strain As (d - k d )^2')
            self.frp_print.append('Icr = '+str(self.b)+' * ('+str(self.k)+' * '+str(self.d)+')^3 / 3 + ' +
                                  str(self.nstrain)+' * '+str(self.As)+' * ('+str(self.d)+' - '+str(self.k)+' * ' +
                                  str(self.d)+')^2')
            self.frp_print.append('Icr = '+str(self.Icr))
            self.ebi = MDL * (self.df - self.k * self.d) * 1000 ** 2 / (self.Icr * self.Ec)
            self.frp_print.append('ε_bi = MDL (df - k d) 1000^2 / (Icr Ec)')
            self.frp_print.append('ε_bi = '+str(MDL)+' * ('+str(self.df)+' - '+str(self.k)+' * ' +
                                  str(self.d)+') * 1000^2 / ('+str(self.Icr)+' * '+str(self.Ec)+')')
            self.frp_print.append('ε_bi = '+str(self.ebi))
            self.c = 0.2 * self.d
            self.frp_print.append('c = 0.2 * d')
            self.frp_print.append('c = 0.2 * '+str(self.d))
            self.frp_print.append('c = '+str(self.c))

    def FRPDesignStrain(self, fc, n, Ef, tf, beamdesign):
        self.Ef = Ef
        self.fc = fc
        self.n = n
        self.tf = tf
        if beamdesign != 2:
            self.efd = 0.41 * (self.fc / (self.n * self.Ef * self.tf)) ** 0.5
            self.frp_print.append("ε_fd = 0.41 [ fc' / (n Ef tf ) ]^0.5 ≤ 0.9ε_fu")
            self.frp_print.append('ε_fd = 0.41 * ('+str(self.fc)+' / ('+str(self.n)+' * '+str(self.Ef) +
                                  ' * '+str(self.tf)+'))^0.5')
            self.frp_print.append('ε_fd = '+str(self.efd))

    def FRPEffectiveStrain(self, fy, Af, epe, fpe, Aps, beamdesign):
        self.fy = fy
        self.Af = Af
        self.epe = epe
        self.fpe = fpe
        self.Aps = Aps
        while abs(self.c - self.c1) > 0.0000000001:
            if beamdesign == 2:
                self.efe = min(0.003 * ((self.df - self.c) / self.c) - self.ebi, 0.7 * self.efd)
            else:
                self.efe = min(0.003 * ((self.df - self.c) / self.c) - self.ebi, self.efd)
            self.ec = (self.efe + self.ebi) * (self.c / (self.df - self.c))
            if beamdesign == 3:
                self.epnet = (self.efe + self.ebi) * (self.d - self.c) / (self.df - self.c)
                self.eps = min(self.epe+self.Pe/(self.Acg*self.Ec)*(1+self.e**2/self.r**2)+self.epnet, 0.035)
                if self.eps <= 0.0086:
                    self.fps = (196500 * self.eps)
                else:
                    self.fps = (1860 - 0.276 / (self.eps - 0.007))
                self.ffe = self.Ef * self.efe
            else:
                self.es = (self.efe + self.ebi) * ((self.d - self.c) / (self.df - self.c))
                self.fs = min(self.Es * self.es, self.fy)
                self.ffe = self.Ef * self.efe
            self.ec1 = 1.7 * self.fc / self.Ec
            self.beta1 = (4 * self.ec1 - self.ec) / (6 * self.ec1 - 2 * self.ec)
            self.alpha1 = (3 * self.ec1 * self.ec - self.ec ** 2) / (3 * self.beta1 * self.ec1 ** 2)
            self.c1 = self.c
            if beamdesign == 3:
                self.c = (self.Aps * self.fps + self.Af * self.ffe) / self.alpha1 / self.beta1 / self.fc / self.b
            else:
                self.c = (self.As * self.fs + self.Af * self.ffe) / self.alpha1 / self.beta1 / self.fc / self.b

        self.frp_print.append('BY ITERATION:')
        if beamdesign == 2:
            self.frp_print.append('ε_fe = 0.003 [(df - c) / c] - ε_bi   ≤ Km ε_fd, where Km = 0.7')
            self.frp_print.append('ε_fe = '+str(self.efe))
        else:
            self.frp_print.append('ε_fe = 0.003 [(df - c) / c] - ε_bi   ≤ ε_fd')
            self.frp_print.append('ε_fe = ' + str(self.efe))
        self.frp_print.append('ε_c = (ε_fe + ε_bi) [c / (df - c)]')
        self.frp_print.append('ε_c = ' + str(self.ec))
        if beamdesign == 3:
            self.frp_print.append('ε_pnet = (ε_fe + ε_bi) [(dp - c) / (df - c)]')
            self.frp_print.append('ε_pnet = ' + str(self.epnet))
            self.frp_print.append('ε_ps = ε_pe + Pe / (Acg Ec) (1 + e^2 / r^2) + ε_pnet  ≤ 0.035')
            self.frp_print.append('ε_ps = ' + str(self.eps))
            self.frp_print.append('fps = [196500ε_ps for ε_ps ≤ 0.0086] or [1860 - 0.276/(ε_ps - 0.007) for ε_ps > '
                                  '0.0086] ≤ fpe')
            self.frp_print.append('fps = ' + str(self.fps))
            self.frp_print.append('ffe = Ef ε_fe')
            self.frp_print.append('ffe = ' + str(self.ffe))
        else:
            self.frp_print.append('ε_s = (ε_fe + ε_bi) [(d - c) / (df  - c)]')
            self.frp_print.append('ε_s = ' + str(self.es))
            self.frp_print.append('fs = Es εs ≤ fy')
            self.frp_print.append('fs = ' + str(self.fs))
            self.frp_print.append('ffe = Ef ε_fe')
            self.frp_print.append('ffe = ' + str(self.ffe))
        self.frp_print.append("ε_c' = 1.7 fc' / Ec ")
        self.frp_print.append("ε_c' = " + str(self.ec1))
        self.frp_print.append("β1 = (4ε_c' - ε_c) / (6ε_c' - 2ε_c)")
        self.frp_print.append("β1 = " + str(self.beta1))
        self.alpha1 = (3 * self.ec1 * self.ec - self.ec ** 2) / (3 * self.beta1 * self.ec1 ** 2)
        self.frp_print.append("α1 = (3ε_c' ε_c - ε_c^2) / (3β1 ε_c'^2)")
        self.frp_print.append("α1 = " + str(self.alpha1))

        if beamdesign == 3:
            self.frp_print.append("c = (Aps fps + Af ffe) / (α1 β1 fc' b) ;      w = b")
        else:
            self.frp_print.append("c = (As fs + Af ffe) / (α1 β1 fc' b) ;      w = b")
        self.frp_print.append("c = " + str(self.c))


    def FlexuralStrength(self, beamdesign):
        self.Mnf = self.Af * self.ffe * (self.df - self.beta1 * self.c / 2) / 1000 ** 2
        self.frp_print.append('Mnf = Af ffe (df - β1 c / 2) / 1000^2')
        self.frp_print.append('Mnf = '+str(self.Af)+' * '+str(self.ffe)+' * ('+str(self.df)+' - '+str(self.beta1) +
                              ' * '+str(self.c)+' / 2) / 1000^2')
        self.frp_print.append('Mnf = ' + str(self.Mnf))
        if beamdesign == 3:
            self.Mns = self.Aps * self.fps * (self.d - self.beta1 * self.c / 2) / 1000 ** 2
            self.frp_print.append('Mns = Aps fps (dp - β1 c / 2 ) / 1000^2')
            self.frp_print.append('Mns = '+str(self.Aps)+' * '+str(self.fps)+' * ('+str(self.d)+' - '+str(self.beta1) +
                                  ' * '+str(self.c)+' / 2) / 1000^2')
            if self.eps >= 0.013:
                self.frpreductionfactor = 0.9
            elif self.eps > 0.01:
                self.frpreductionfactor = 0.65 + 0.25 * (self.eps - 0.01) / (0.013 - 0.01)
            else:
                self.frpreductionfactor = 0.65
        else:
            self.Mns = self.As * self.fs * (self.d - self.beta1 * self.c / 2) / 1000 ** 2
            self.frp_print.append('Mns = As fs (d - β1 c / 2) / 1000^2')
            self.frp_print.append('Mns = '+str(self.As)+' * '+str(self.fs)+' * ('+str(self.d)+' - '+str(self.beta1) +
                                  ' * '+str(self.c)+' / 2) / 1000^2')
            if self.es >= 0.005:
                self.frpreductionfactor = 0.9
            else:
                self.frpreductionfactor = 0
        self.frp_print.append('Mns = ' + str(self.Mns))
        self.frp_print.append('FRP reduction factor, φ = ' + str(self.frpreductionfactor))
        self.oMn = self.frpreductionfactor * (self.Mns + self.addlreductionfactor * self.Mnf)
        self.frp_print.append('φMn = φ [Mns + ψf Mnf]')
        self.frp_print.append('φMn = '+str(self.frpreductionfactor)+' * ('+str(self.Mns)+' + ' +
                              str(self.addlreductionfactor)+' * '+str(self.Mnf)+')')
        self.frp_print.append('φMn = '+str(self.oMn))

    def PrestressCheck(self, Ms):
        self.epnets = Ms * self.e / self.Ec / self.Ig * 1000 ** 2
        self.frp_print.append('ε_pnet,s = Ms e / (Ec Ig) 1000^2')
        self.frp_print.append('ε_pnet,s = '+str(Ms)+' * '+str(self.e)+' / '+str(self.Ec)+' / '+str(self.Ig)+' * 1000^2')
        self.frp_print.append('ε_pnet,s = '+str(self.epnets))
        self.epss = self.epe + self.Pe / (self.Acg * self.Ec) * (1 + self.e ** 2 / self.r ** 2) + self.epnets
        self.frp_print.append('ε_ps,s = ε_pe + Pe / (Acg Ec) (1 + e^2 / r^2) + ε_pnet,s')
        self.frp_print.append('ε_ps,s = '+str(self.epe)+' + '+str(self.Pe)+' / ('+str(self.Acg)+' * '+str(self.Ec) +
                              ') * (1 + '+str(self.e)+'^2 / '+str(self.r)+'^2) + '+str(self.epnets))
        self.frp_print.append('ε_ps,s = '+str(self.epss))
        self.frp_print.append('fps,s = [196500ε_ps,s for ε_ps,s ≤ 0.0086] or [1860 - 0.276 / (ε_ps,s - 0.007) '
                              'for ε_ps,s > 0.0086] ≤ fpe')
        if self.epss <= 0.0086:
            self.fpss = (196500 * self.epss)
            self.frp_print.append('fps,s = min(196500 * '+str(self.epss)+', '+str(self.fpe)+')')
        else:
            self.fpss = (1860 - 0.276 / (self.epss - 0.007))
            self.frp_print.append('fps,s = min(1860 - 0.276 / ('+str(self.epss)+' - 0.007), '+str(self.fpe)+')')
        self.frp_print.append('fps,s = '+str(self.fpss))
        self.ecs = abs(-self.Pe/(self.Acg*self.Ec)*(1+self.e**2/self.r**2)-Ms*self.yt/self.Ec/self.Ig*1000**2)
        self.frp_print.append('ε_c,s = -Pe / (Acg Ec) (1 + e^2 / r^2) - Ms yt / (Ec Ig)')
        self.frp_print.append('ε_c,s = abs(-'+str(self.Pe)+'/('+str(self.Acg)+'*'+str(self.Ec)+')*(1+'+str(self.e) +
                              '^2/'+str(self.r)+'^2)-'+str(Ms)+'*'+str(self.yt)+'/'+str(self.Ec)+'/'+str(self.Ig) +
                              '*1000^2)')
        self.frp_print.append('ε_c,s = '+str(self.ecs))
        self.fcs = self.Ec * self.ecs
        self.frp_print.append('fc,s = Ec ε_c,s')
        self.frp_print.append('fc,s = ' + str(self.Ec)+' * '+str(self.ecs))
        self.frp_print.append('fc,s = ' + str(self.fcs))

    def ServiceStresses(self, Ms, beamdesign):
        if beamdesign == 3:
            self.ff_s = 1000 ** 2 * self.Ef / self.Ec * Ms * self.yb / self.Ig - self.ebi * self.Ef
            self.frp_print.append('ff,s = 1000^2 (Ef / Ec) Ms yb / Ig - ε_bi Ef')
            self.frp_print.append('ff,s = 1000^2 * '+str(self.Ef)+' / '+str(self.Ec)+' * '+str(Ms)+' * '+str(self.yb) +
                                  ' / '+str(self.Ig)+' - '+str(self.ebi)+' * '+str(self.Ef))
            self.frp_print.append('ff,s = ' + str(self.ff_s))
        else:
            self.rho_s = self.As / self.b / self.d
            self.frp_print.append('ρs =  As / (b d)')
            self.frp_print.append('ρs =  '+str(self.As)+' / '+str(self.b)+' / '+str(self.d))
            self.frp_print.append('ρs = ' + str(self.rho_s))
            self.rho_f = self.Af / self.b / self.d
            self.frp_print.append('ρf =  Af / (b d)')
            self.frp_print.append('ρf =  '+str(self.Af)+' / '+str(self.b)+' / '+str(self.d))
            self.frp_print.append('ρf = ' + str(self.rho_f))
            a = self.Es / self.Ec
            b = self.Ef / self.Ec
            self.k = ((self.rho_s*a+self.rho_f*b)**2+2*(self.rho_s*a+self.rho_f*b*self.df/self.d))**0.5-(self.rho_s*a +
                                                                                                         self.rho_f*b)
            self.frp_print.append('k = [(ρs Es/Ec + ρf Ef/Ec)^2 + 2(ρs Es/Ec + (ρf Ef/Ec)(df / d))]^0.5 - (ρs Es/Ec + '
                                  'ρf Ef/Ec)')
            self.frp_print.append('k = ' + str(self.k))
            c = self.k * self.d
            d = self.Af * self.Ef
            e = self.As * self.Es
            self.fs_s = (1000**2*Ms+self.ebi*d*(self.df-c/3))*(self.d-c)*self.Es/(e*(self.d-c/3)*(self.d-c) +
                                                                                  d*(self.df-c/3)*(self.df-c))
            self.frp_print.append('fs,s = [1000^2 Ms + ε_bi Af Ef (df - kd/3)] (d - kd) Es / [As Es (d - kd/3)(d - kd) '
                                  '+ Af Ef (df - kd/3)(df - kd)]')
            self.frp_print.append('fs,s = ' + str(self.fs_s))
            self.ff_s = self.fs_s * self.Ef / self.Es * (self.df - c) / (self.d - c) - self.ebi * self.Ef
            self.frp_print.append('ff,s = fs,s (Ef / Es) (df - kd) / (d - kd) - ε_bi Ef')
            self.frp_print.append('ff,s = ' + str(self.ff_s))
        if beamdesign != 2:
            self.ldf = (self.n * self.Ef * self.tf / self.fc ** 0.5 ) ** 0.5
            self.frp_print.append("ℓdf = [ n Ef tf / (fc')^0.5 ]^0.5")
            self.frp_print.append('ℓdf = ('+str(self.n)+' * '+str(self.Ef)+' * '+str(self.tf)+' / '+str(self.fc) +
                                  '^0.5 )^0.5')
            self.frp_print.append('ldf = ' + str(self.ldf))

