import math

class ConcreteProperties:
    def __init__(self):
        # Properties of Section
        self.L = 0                  # length of beam, m
        self.b = 0                  # width of beam, mm
        self.d = 0                  # effective depth of beam, mm
        self.h = 0                  # total depth of beam, mm
        self.hf = 0                 # thickness of T-beam flange, mm
        self.bf = 0                 # width of T-beam flange, mm
        self.fc = 0                 # compressive strength of concrete, MPa
        self.fy = 0                 # rebar yield strength, MPa
        self.fy_s = 0               # rebar yield strength for shear reinforcement, MPa
        self.nbar = 0               # no of rebars
        self.bardia = 0             # rebar diameter, mm
        self.sbar = 0               # spacing of shear rebars
        self.sbardia = 0            # shear rebar diameter, mm
        self.As = 0                 # area of rebar - flexural, sq.mm.
        self.Ast = 0                # total area of rebar - column, sq.mm.
        self.Asw = 0                # area of shear wall rebar - flexural, sq.mm.
        self.Av = 0                 # area of rebar - shear, sq.mm.
        self.reductionfactor = 0.9  # flexural reduction factor
        self.ecu = 0.003            # strain concrete
        self.Beta1 = 0.85           # concrete Beta1 value
        self.a = 0                  # effective concrete stress block
        self.moment = 0             # moment without FRP
        self.Ec = 0                 # modulus of elasticity, concrete
        self.Es = 200000            # modulus of elasticity, rebars
        self.Acg = 0                # gross area of T-beam, sq.mm.
        self.Ac = 0                 # gross area of column, sq.mm.
        self.rho_g = 0              # column steel to concrete ratio
        self.yt = 0                 # centroid of T-beam, mm
        self.Ig = 0                 # moment of inertia of T-beam, mm^4
        self.r = 0                  # radius of gyration of T-beam, mm
        self.npressbar = 0          # number of prestressing bar
        self.pressbar = 0           # prestressing bar area,sq.mm.
        self.fpe = 0                # effective prestressing strength, MPa
        self.fpy = 0                # prestressing yield strength, MPa
        self.fpu = 0                # prestressing ultimate strength, MPa
        self.Ep = 1                 # modulus of elasticity, prestress, Mpa
        self.Aps = 0                # total area, prestress, sq.mm.
        self.epe = 0                # effective prestressing strain
        self.P_e = 0                # effective prestressing force, N
        self.e = 0                  # eccentricity of prestressing strain, mm
        self.Vc = 0                 # concrete nominal shear strength
        self.Vs = 0                 # steel nominal shear strength
        self.Vsw = 0                # steel nominal shear strength of existing shearwall
        self.Vn = 0                 # nominal shear strength of existing shearwall
        self.oVn = 0                # design shear strength of existing beam
        self.sreductionfactor = 0.75# shear reduction factor
        self.modfactor = 1          # lightweight modification factor
        self.hw = 0                 # shear wall height, mm
        self.Lw = 0                 # shear wall length, mm
        self.tw = 0                 # shear wall thickness,
        self.layer = 1              # shear wall number of rebar layers
        self.horbardia = 0          # shear wall horizontal rebar diameter, mm
        self.horbarspacing = 0      # shear wall horizontal rebar spacing, mm
        self.verbardia = 0          # shear wall vertical rebar diameter, mm
        self.verbarspacing = 0      # shear wall vertical rebar spacing, mm
        self.cc = 0                 # clear concrete cover, mm
        self.d_comp = 0             # distance of compressive rebar from outer fiber, mm
        self.efu = 0                # Longitudinal reinforcing yield strain, mm/mm
        self.dfv = 0
        self.n = 0
        self.frp_print = []

    def Calculate_Beta(self):
        if self.fc >= 28:
            if self.fc >= 55:
                self.Beta1 = 0.65
                self.frp_print.append('β = 0.65')
            else:
                self.Beta1 = 0.85 - (self.fc - 28) * 0.05 / 7
                self.frp_print.append("β = 0.85 - (fc' - 28) * 0.05 / 7")
                self.frp_print.append('β = 0.85 - (' + str(self.fc) + ' - 28) * 0.05 / 7')
                self.frp_print.append('β = ' + str(self.Beta1))
        else:
            self.Beta1 = 0.85
            self.frp_print.append('β = 0.85')
        self.Ec = 4700 * self.fc ** 0.5
        self.frp_print.append("Ec = 4700 * fc' ^ 0.5")
        self.frp_print.append('Ec = 4700 * ' + str(self.fc) + ' ^ 0.5')
        self.frp_print.append('Ec = ' + str(self.Ec))

    def Calculate_Concrete(self, beamdesign):
        if beamdesign == 3:
            self.Acg = self.bf * self.hf + self.b * (self.h - self.hf)
            self.frp_print.append('Acg = bf * hf + b * (h - hf)')
            self.frp_print.append('Acg = '+str(self.bf)+' * '+str(self.hf)+' + '+str(self.b)+' * ('+str(self.h)+' - ' +
                                  str(self.hf)+')')
            self.frp_print.append('Acg = '+str(self.Acg))
            self.yt = (self.bf*self.hf**2/2+self.b*(self.h-self.hf)*(self.hf+(self.h-self.hf)/2))/self.Acg
            self.frp_print.append('yt = (bf*hf^2/2+b*(h-hf)*(hf+(h-hf)/2))/Acg')
            self.frp_print.append('yt = ('+str(self.bf)+'*'+str(self.hf)+'^2/2+'+str(self.b)+'*('+str(self.h)+'-' +
                                  str(self.hf)+')*('+str(self.hf)+'+('+str(self.h)+'-'+str(self.hf)+')/2))/' +
                                  str(self.Acg))
            self.frp_print.append('yt = '+str(self.yt))
            self.Ig = self.bf*self.hf**3/12+self.bf*self.hf*(self.yt-self.hf/2)**2+self.b*(self.h-self.hf)**3/12 +\
                      self.b*(self.h-self.hf)*(self.yt-(self.h-self.hf)/2)**2
            self.frp_print.append('Ig = bf*hf^3/12+bf*hf*(yt-hf/2)^2+b*(h-hf)^3/12+b*(h-hf)*(yt-(h-hf)/2)^2')
            self.frp_print.append('Ig = '+str(self.bf)+'*'+str(self.hf)+'^3/12+'+str(self.bf)+'*'+str(self.hf) +
                                  '*('+str(self.yt)+'-'+str(self.hf)+'/2)^2+'+str(self.b)+'*('+str(self.h)+'-' +
                                  str(self.hf)+')^3/12+'+str(self.b)+'*('+str(self.h)+'-'+str(self.hf)+')*('+
                                  str(self.yt)+'-('+str(self.h)+'-'+str(self.hf)+')/2)^2')
            self.frp_print.append('Ig = '+str(self.Ig))
            self.r = (self.Ig / self.Acg) ** 0.5
            self.frp_print.append('r = (Ig / Acg) ^ 0.5')
            self.frp_print.append('r = ('+str(self.Ig)+' / '+str(self.Acg)+') ^ 0.5')
            self.frp_print.append('r = ' + str(self.r))
            self.Aps = self.npressbar * self.pressbar
            self.frp_print.append('Aps = number of prestressed bar * prestressed bar area')
            self.frp_print.append('Aps = '+str(self.npressbar)+' * '+str(self.pressbar))
            self.frp_print.append('Aps = '+str(self.Aps))
        else:
            self.As = math.pi * self.bardia ** 2 / 4 * self.nbar
            self.frp_print.append('As = pi * bar diameter ^ 2 / 4 * number of bar')
            self.frp_print.append('As = ' + str(math.pi) + ' * ' + str(self.bardia) + ' ^ 2 / 4 * ' + str(self.nbar))
            self.frp_print.append('As = ' + str(self.As))
        self.Calculate_Beta()
        if beamdesign == 3:
            self.epe = self.fpe / self.Ep
            self.frp_print.append('ε_pe = fpe / Ep')
            self.frp_print.append('ε_pe = '+str(self.fpe)+' / '+str(self.Ep))
            self.frp_print.append('ε_pe = '+str(self.epe))
            self.P_e = self.Aps * self.fpe
            self.frp_print.append('P_e = Aps * fpe')
            self.frp_print.append('P_e = '+str(self.Aps)+' * '+str(self.fpe))
            self.frp_print.append('P_e = '+str(self.P_e))
            self.e = self.d - self.yt
            self.frp_print.append('e = d - yt')
            self.frp_print.append('e = '+str(self.d)+' - '+str(self.yt))
            self.frp_print.append('e = '+str(self.e))
            self.a = self.Aps * self.fpy / 0.85 / self.fc / self.b
            self.frp_print.append("a = Aps * fpy / 0.85 / fc' / b")
            self.frp_print.append(
                'a = ' + str(self.Aps) + ' * ' + str(self.fpy) + ' / 0.85 / ' + str(self.fc) + ' / ' + str(self.b))
            self.frp_print.append('a = ' + str(self.a))
            self.moment = self.reductionfactor * (self.Aps * self.fpy * (self.d - self.a / 2)) / 1000 ** 2
            self.frp_print.append('φMn (existing) = φ * (Aps * fpy * (d - a/2)) / 1000 ^ 2')
            self.frp_print.append(
                'φMn (existing) = ' + str(self.reductionfactor) + ' * (' + str(self.Aps) + ' * ' + str(self.fpy) + ' * (' +
                str(self.d) + ' - ' + str(self.a) + '/2)) / 1000 ^ 2')
            self.frp_print.append('φMn (existing) = ' + str(self.moment))
        else:
            self.a = self.As * self.fy / 0.85 / self.fc / self.b
            self.frp_print.append("a = As * fy / 0.85 / fc' / b")
            self.frp_print.append(
                'a = ' + str(self.As) + ' * ' + str(self.fy) + ' / 0.85 / ' + str(self.fc) + ' / ' + str(self.b))
            self.frp_print.append('a = ' + str(self.a))
            self.moment = self.reductionfactor * (self.As * self.fy * (self.d - self.a / 2)) / 1000 ** 2
            self.frp_print.append('φMn (existing) = φ * (As * fy * (d - a/2)) / 1000 ^ 2')
            self.frp_print.append(
                'φMn (existing) = ' + str(self.reductionfactor) + ' * (' + str(self.As) + ' * ' + str(self.fy) + ' * (' +
                str(self.d) + ' - ' + str(self.a) + '/2)) / 1000 ^ 2')
            self.frp_print.append('φMn (existing) = ' + str(self.moment))

    def Calculate_Shear(self, sheardesign):
        self.Vc = 0.17*self.modfactor*self.fc**0.5*self.b*self.d / 1000
        self.frp_print.append("Vc = 0.17 * λ * fc' ^0.5 * b * d / 1000")
        self.frp_print.append('Vc = 0.17*'+str(self.modfactor)+'*'+str(self.fc)+'^0.5*'+str(self.b)+'*'+str(self.d) +
                              '/1000')
        self.frp_print.append('Vc = '+str(self.Vc))
        self.Vs = 2 * math.pi * self.sbardia ** 2 / 4 * self.fy_s * self.d / self.sbar / 1000
        self.frp_print.append('Vs = 2 * pi * shear bar diameter ^ 2 / 4 * fy * d / spacing / 1000')
        self.frp_print.append('Vs = 2 * '+str(math.pi)+' * '+str(self.sbardia)+' ** 2 / 4 * '+str(self.fy_s)+' * ' +
                              str(self.d)+' / '+str(self.sbar)+' / 1000')
        self.frp_print.append('Vs = '+str(self.Vs))
        self.oVn = self.sreductionfactor * (self.Vc + self.Vs)
        self.frp_print.append('φVn (existing) = φ * (Vc + Vs)')
        self.frp_print.append('φVn (existing) = '+str(self.sreductionfactor)+' * ('+str(self.Vc)+' + '+str(self.Vs))
        self.frp_print.append('φVn (existing) = '+str(self.oVn))

    def Calculate_ShearWall(self):
        self.d_comp = self.cc + 0.5 * self.verbardia
        self.frp_print.append("d' = clear cover + 0.5 * vertical bar diameter")
        self.frp_print.append("d' = "+str(self.cc)+" + 0.5 * "+str(self.verbardia))
        self.frp_print.append("d' = "+str(self.d_comp))
        self.Calculate_Beta()
        self.Vc = 0.167 * self.fc ** 0.5 * self.tw * self.dfv / 1000
        self.frp_print.append("Vc = 0.167 * fc' ^ 0.5 * tw * dfv / 1000")
        self.frp_print.append('Vc = 0.167 * '+str(self.fc)+' ^ 0.5 * '+str(self.tw)+' * '+str(self.dfv)+' / 1000')
        self.frp_print.append('Vc = '+str(self.Vc))
        self.Av = self.layer * math.pi * self.horbardia ** 2 / 4
        self.frp_print.append('Av = number of layer * pi * horizontal bar diameter ^ 2 / 4')
        self.frp_print.append('Av = '+str(self.layer)+' * '+str(math.pi)+' * '+str(self.horbardia)+' ^ 2 / 4')
        self.frp_print.append('Av = '+str(self.Av))
        self.As = self.layer * math.pi * self.verbardia ** 2 / 4
        self.frp_print.append('As = no. of layer * pi * vertical bar diameter ^ 2 / 4')
        self.frp_print.append('As = '+str(self.layer)+' * '+str(math.pi)+' * '+str(self.verbardia)+' ^ 2 / 4')
        self.frp_print.append('As = '+str(self.As))
        self.Vsw = self.Av * self.fy_s * self.dfv / self.horbarspacing / 1000
        self.frp_print.append('Vsw = Av * fy * dfv / horizontal bar spacing / 1000')
        self.frp_print.append('Vsw = '+str(self.Av)+' * '+str(self.fy_s)+' * '+str(self.dfv)+' / ' +
                              str(self.horbarspacing)+' / 1000')
        self.frp_print.append('Vsw = '+str(self.Vsw))
        self.Vn = self.Vc + self.Vsw
        self.frp_print.append('φVn (existing) = φ(Vc + Vsw);  where φ = 1.0')
        self.frp_print.append('φVn (existing) = '+str(self.Vc)+' + '+str(self.Vsw))
        self.frp_print.append('φVn (existing) = '+str(self.Vn))
        self.n = math.ceil((self.Lw - 2 * self.d_comp) / self.verbarspacing)
        a = (self.Lw - self.d_comp)
        space = (a - self.d_comp) / (self.n - 1)
        self.rebar_pos = []
        self.rebar_Area = []
        for x in range(self.n):
            self.rebar_pos.append(a)
            self.rebar_Area.append(self.As)
            a -= space
        self.frp_print.append('di = ' + str(self.rebar_pos))
        self.frp_print.append('Asi = ' + str(self.rebar_Area))
        self.Asw = self.As * (self.n - 1)
        self.frp_print.append('Asw = ' + str(self.Asw))

    def Calculate_Column(self):
        self.Ac = self.b * self.h
        self.frp_print.append('Ac = b * h')
        self.frp_print.append('Ac = '+str(self.b)+' * '+str(self.h))
        self.frp_print.append('Ac = '+str(self.Ac))
        self.d_comp = self.cc + 0.5 * self.bardia + self.sbardia
        self.frp_print.append('d1 = clear cover + 0.5 * main bar diameter + bar ties diameter')
        self.frp_print.append('d1 = '+str(self.cc)+' + 0.5 * '+str(self.bardia)+' + '+str(self.sbardia))
        self.frp_print.append('d1 = '+str(self.d_comp))
        self.Calculate_Beta()
        a = self.h - self.d_comp
        space = (a - self.d_comp) / (self.verbarspacing - 1)
        self.rebar_pos = []
        self.rebar_Area = []
        self.Ast = 0
        for x in range(self.verbarspacing):
            self.rebar_pos.append(a)
            if x == 0 or x == self.verbarspacing - 1:
                self.As = math.pi * self.bardia ** 2 / 4 * self.horbarspacing
            else:
                self.As = math.pi * self.bardia ** 2 / 4 * 2
            self.rebar_Area.append(self.As)
            self.Ast += self.As
            a -= space
        self.frp_print.append('di = ' + str(self.rebar_pos))
        self.frp_print.append('Asi = ' + str(self.rebar_Area))
        self.frp_print.append('Ast = ' + str(self.Ast))
        self.rho_g = self.Ast / self.Ac
        self.frp_print.append('ρg = Ast / Ac')
        self.frp_print.append('ρg = ' + str(self.Ast)+' / ' + str(self.Ac))
        self.frp_print.append('ρg = ' + str(self.rho_g))
