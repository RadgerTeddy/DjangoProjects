class FRPColumnDesign:
    def __init__(self):
        self.fc = 0
        self.Ag = 0
        self.Ast = 0
        self.fy = 0
        self.red_factor = 0.65
        self.SRF = 0
        self.fcc = 0
        self.E2 = 0
        self.eccu = 0
        self.b = 0
        self.h = 0
        self.c = 0
        self.Ec = 0
        self.ec = 0
        self.Es = 0
        self.Ke = 0.55
        self.frp_print = []
        self.oPn = []
        self.oMn = []

    def CalculateColumn(self, fc, fy, Ag, Ast, SRF, b, h, Ec, Es, pos, Asi, ecu):
        self.fc = fc
        self.fy = fy
        self.Ag = Ag
        self.Ast = Ast
        self.SRF = SRF
        self.fcc = fc
        self.b = b
        self.h = h
        self.Ec = Ec
        self.Es = Es
        self.pos = pos
        self.Asi = Asi
        self.yt = 0
        self.E2 = 0
        if pos != []:
            self.d1 = pos[0]
            self.c = self.d1
        self.eccu = ecu

        self.PointA()
        self.esy = self.fy / self.Es
        self.frp_print.append('ε_sy = fy / Es')
        self.frp_print.append('ε_sy = '+str(self.fy)+' / '+str(self.Es))
        self.frp_print.append('ε_sy = ' + str(self.esy))
        self.CalculatePM()
        self.c = self.eccu * self.d1 / (self.esy + self.eccu)
        self.frp_print.append('c = ε_ccu d1 / (ε_sy + ε_ccu)')
        self.frp_print.append('c = '+str(self.eccu)+' * '+str(self.d1)+' / ('+str(self.esy)+' + '+str(self.eccu)+')')
        self.frp_print.append('c = ' + str(self.c))
        self.CalculatePM()

    def CalculateColumnFRP(self, bardia, rho_g, SRF, alpha, n_frp, tf_frp, f_fu, e_fu, E_f):
        self.rho_g = rho_g
        self.rc = bardia
        self.SRF = SRF
        self.alpha = alpha
        self.n_frp = n_frp
        self.tf_frp = tf_frp
        self.f_fu = f_fu
        self.e_fu = e_fu
        self.E_f = E_f
        self.Dconc = (self.b**2 + self.h**2)**0.5
        self.frp_print.append('Dconc = (b^2 + h^2)^0.5')
        self.frp_print.append('Dconc = ('+str(self.b)+'^2 / '+str(self.h)+'^2)^0.5')
        self.frp_print.append('Dconc = ' + str(self.Dconc))
        self.frp_print.append('rc = diameter of main bar')
        self.Ae_Ac = (1-(self.b*(self.h-2*self.rc)**2/self.h+self.h*(self.b-2*self.rc)**2/self.b)/(3*self.Ag) -
                      self.rho_g)/(1-self.rho_g)
        self.frp_print.append('Ae / Ac = [1 - (b(h - 2rc)^2 / h +  h(b - 2rc)^2 / b) / (3 Ag) - ρg] / [1 - ρg]')
        self.frp_print.append('Ae / Ac = ' + str(self.Ae_Ac))
        self.Ka = self.Ae_Ac * (self.b / self.h)**2
        self.frp_print.append('Ka = [Ae / Ac] [b / h]^2')
        self.frp_print.append('Ka = ' + str(self.Ka))
        self.Kb = self.Ae_Ac * (self.h / self.b)**0.5
        self.frp_print.append('Kb = [Ae / Ac] [h / b]^0.5')
        self.frp_print.append('Kb = ' + str(self.Kb))
        self.efe = self.Ke * self.e_fu
        self.frp_print.append("ε_fe = Ke ε_fu ; where Ke=0.55 with minimum confinement ratio of fl / fc' = 0.08")
        self.frp_print.append('ε_fe = ' + str(self.efe))
        self.FRPVariable()
        self.PointA()
        self.efe = min(0.004, self.Ke * self.e_fu)
        self.frp_print.append("ε_fe = 0.004 ≤ Ke εfu ; where Ke=0.55 with minimum confinement ratio of fl / fc' = 0.08")
        self.frp_print.append('ε_fe = ' + str(self.efe))
        self.FRPVariable()
        self.eccu = self.esy * (1.5 + 12 * self.Kb * self.fl / self.fc * (self.efe / self.esy)**0.45)
        self.frp_print.append("ε_ccu = ε_c' [1.5 + 12 Kb (fl / fc') (ε_fe / ε_c')^0.45 ")
        self.frp_print.append('ε_ccu = ' + str(self.eccu))
        self.E2 = (self.fcc - self.fc) / self.eccu
        self.frp_print.append("E2 = (fcc' - fc') / ε_ccu")
        self.frp_print.append('E2 = ' + str(self.E2))
        self.c = self.d1
        self.frp_print.append('c = d1')
        self.frp_print.append('c = ' + str(self.c))
        self.CalculatePM()
        self.c = self.eccu * self.d1 / (self.esy + self.eccu)
        self.frp_print.append('c = ε_ccu d1 / (ε_sy + ε_ccu)')
        self.frp_print.append('c = ' + str(self.c))
        self.CalculatePM()

    def FRPVariable(self):
        self.fl = 2 * self.SRF * self.E_f * self.n_frp * self.tf_frp * self.efe / self.Dconc
        self.frp_print.append('fl = 2 Ψf Ef n tf ε_fe / Dconc')
        self.frp_print.append('fl = 2 * '+str(self.SRF)+' * '+str(self.E_f)+' * '+str(self.n_frp) +
                              ' * '+str(self.tf_frp)+' * '+str(self.efe)+' / '+str(self.Dconc))
        self.frp_print.append('fl = '+str(self.fl))
        if self.fl / self.fc < 0.08:
            self.frp_print.append('Increase the number of FRP ply')
        self.fcc = self.fc + 3.3 * self.Ka * self.fl
        self.frp_print.append("fcc' = fc' + 3.3 Ka fl")
        self.frp_print.append("fcc' = " + str(self.fc)+' + 3.3 * '+str(self.Ka)+' * '+str(self.fl))
        self.frp_print.append("fcc' = " + str(self.fcc))

    def PointA(self):
        a = self.red_factor*0.8*(0.85*self.fcc*(self.Ag-self.Ast)+self.fy*self.Ast)/1000
        self.oPn.append(a)
        self.frp_print.append("φPn = φ 0.8 [0.85 fc' (Ag - Ast) + fy Ast]  where φ = 0.65 for tied column")
        self.frp_print.append('φPn = '+str(self.red_factor)+'*0.8*(0.85*'+str(self.fcc)+'*('+str(self.Ag) +
                              '-'+str(self.Ast)+')+'+str(self.fy)+'*'+str(self.Ast)+')/1000')
        self.frp_print.append('φPn = ' + str(a))
        self.oMn.append(0)
        self.frp_print.append('φMn = 0')

    def CalculatePM(self):
        self.E_Asi_fsi = 0
        self.E_Asi_fsi_dsi = 0
        l_esi = []
        l_fsi = []
        l_Asi_fsi = []
        l_dsi = []
        l_Asi_fsi_dsi = []
        self.et = 2 * self.fc / (self.Ec - self.E2)
        self.frp_print.append("ε_t' = 2 fc' / (Ec - E2)")
        self.frp_print.append("ε_t' = 2 * "+str(self.fc)+' / ('+str(self.Ec)+' - '+str(self.E2))
        self.frp_print.append("ε_t' = " + str(self.et))
        self.yt = self.c * self.et / self.eccu
        self.frp_print.append("yt = c ε_t' / ε_ccu")
        self.frp_print.append('yt = '+str(self.c)+' * '+str(self.et)+' / '+str(self.eccu))
        self.frp_print.append('yt = '+str(self.yt))
        A = -self.b*(self.Ec-self.E2)**2/12/self.fc*(self.eccu/self.c)**2/1000
        self.frp_print.append("A = -b (Ec - E2)^2 (ε_ccu / c)^2 / (12 fc')")
        self.frp_print.append('A = ' + str(A))
        B = self.b*(self.Ec-self.E2)*(self.eccu/self.c)/2/1000
        self.frp_print.append("B = b (Ec - E2) (ε_ccu / c) / 2")
        self.frp_print.append('B = ' + str(B))
        C = -self.b*self.fc/1000
        self.frp_print.append("C = -b fc'")
        self.frp_print.append('C = ' + str(C))
        D = self.b*self.c*(self.fc+self.E2*self.eccu/2)/1000
        self.frp_print.append("D = b c fc' + b c E2 ε_ccu / 2")
        self.frp_print.append('D = ' + str(D))
        E = -self.b*(self.Ec-self.E2)**2/16/self.fc*(self.eccu/self.c)**2/1000
        self.frp_print.append("E = -b (Ec - E2)^2 (ε_ccu / c)^2 / (16 fc')")
        self.frp_print.append('E = ' + str(E))
        F = (self.b*(self.c-self.h/2)*(self.Ec-self.E2)**2/12/self.fc*(self.eccu/self.c)**2+self.b*(self.Ec-self.E2) *
             (self.eccu/self.c)/3)/1000
        self.frp_print.append("F = b (c - h/2) (Ec - E2)^2 (ε_ccu / c)^2 / (12 fc') + b (Ec - E2) (ε_ccu / c) / 3")
        self.frp_print.append('F = ' + str(F))
        G = -(self.b*self.fc/2+self.b*(self.c-self.h/2)*(self.Ec-self.E2)*(self.eccu/self.c)/2)/1000
        self.frp_print.append("G = - [b fc' / 2 + b (c - h/2) (Ec - E2) (ε_ccu / c) / 2]")
        self.frp_print.append('G = ' + str(G))
        H = self.b*self.fc*(self.c-self.h/2)/1000
        self.frp_print.append("H = b fc' (c - h/2)")
        self.frp_print.append('H = ' + str(H))
        I = (self.b*self.c**2*self.fc/2-self.b*self.c*self.fc*(self.c-self.h/2)+self.b*self.c**2*self.E2*self.eccu/3 -
             self.b*self.c*self.E2*self.eccu*(self.c-self.h/2)/2)/1000
        self.frp_print.append("I = b c^2 fc'/2 - b c fc' (c - h/2) + b c^2 E2 ε_ccu/3 - b c E2 (c - h/2) ε_ccu/2")
        self.frp_print.append('I = ' + str(I))
        length = len(self.pos)
        for x in range(length):
            esi = self.eccu * (1 - self.pos[x] / self.c)
            if esi > 0:
                fsi = min(self.fy, self.Es * esi)
            else:
                fsi = max(-self.fy, self.Es * esi)
            Asi_fsi = self.Asi[x] * fsi / 1000
            dsi = self.h / 2 - self.pos[x]
            Asi_fsi_dsi = Asi_fsi * dsi / 1000
            l_esi.append(esi)
            l_fsi.append(fsi)
            l_Asi_fsi.append(Asi_fsi)
            l_dsi.append(dsi)
            l_Asi_fsi_dsi.append(Asi_fsi_dsi)
            self.E_Asi_fsi += Asi_fsi
            self.E_Asi_fsi_dsi += Asi_fsi_dsi
        self.frp_print.append('Asi = ' + str(self.Asi))
        self.frp_print.append('di = ' + str(self.pos))
        self.frp_print.append('ε_si = = ε_ccu (1 - di/c)')
        self.frp_print.append('ε_si = ' + str(l_esi))
        self.frp_print.append('fsi = min(fy, ε_si Es)')
        self.frp_print.append('fsi = ' + str(l_fsi))
        self.frp_print.append('Asi fsi = ' + str(l_Asi_fsi))
        self.frp_print.append('dsi = h/2 - di')
        self.frp_print.append('dsi = ' + str(l_dsi))
        self.frp_print.append('Asi_fsi_dsi = ' + str(l_Asi_fsi_dsi))
        self.frp_print.append('ΣAsi_fsi = ' + str(abs(self.E_Asi_fsi)))
        self.frp_print.append('ΣAsi_fsi_dsi = ' + str(abs(self.E_Asi_fsi_dsi)))
        P = self.red_factor*(A*self.yt**3+B*self.yt**2+C*self.yt+D+self.E_Asi_fsi)
        self.oPn.append(P)
        self.frp_print.append("φ Pn = φ [A yt^3 + B yt^2 + C yt + D + ΣAsi_fsi]")
        self.frp_print.append('φ Pn = ' + str(P))
        M = self.red_factor*((E*self.yt**4+F*self.yt**3+G*self.yt**2+H*self.yt+I)/1000+self.E_Asi_fsi_dsi)
        self.oMn.append(M)
        self.frp_print.append("φ Mn = φ [E yt^4 + F yt^3 + G yt^2 + H yt + I + ΣAsi_fsi_di]")
        self.frp_print.append('φ Mn = ' + str(M))


