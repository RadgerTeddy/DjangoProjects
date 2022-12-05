class FRPShearWallDesign:
    def __init__(self):
        self.flexural_reduction = 1                 # flexural reduction factor
        self.shear_reduction = 1                    # shear reduction factor
        self.efd = 0
        self.fc = 0
        self.n = 0
        self.Ef = 0
        self.tf = 0
        self.efu = 0
        self.CE = 0
        self.Af = 0
        self.Tf = 0
        self.a = 0
        self.Asw = 0
        self.fy = 0
        self.Pu = 0
        self.tw = 0
        self.a = 0
        self.c = 0
        self.c1 = 0
        self.Beta = 0
        self.wf = 0
        self.Lw = 0
        self.ec = 0
        self.esc = 0
        self.d_comp = 0
        self.efu_rebar = 0
        self.Aisi = 0
        self.pos = 0
        self.Es = 0
        self.Asi = 0
        self.E_Asi_fsi = 0
        self.E_Asi_fsi_dsi = 0
        self.oMn = 0
        self.ce = 0
        self.frp_print = []

    def CalculateTf(self, fc, n, Ef, tf, efu, CE, Af, efu_rebar, fy, Asw):
        self.fc = fc
        self.n = n
        self.Ef = Ef
        self.tf = tf
        self.efu = efu
        self.CE = CE
        self.Af = Af
        self.efu_rebar = efu_rebar
        self.Asw = Asw
        self.fy = fy
        self.Aisi = self.Asw * self.fy / 1000
        self.frp_print.append('Asw fy = '+str(self.Asw)+' * '+str(self.fy)+' / 1000')
        self.frp_print.append('Asw fy = ' + str(self.Aisi))
        self.efd = min(0.41*(self.fc/(self.n*self.Ef*self.tf))**0.5, 0.9*self.efu)
        self.frp_print.append("ε_fd = 0.41 [fc' / (n Ef tf)]^0.5  ≤  0.9 ε_fu")
        self.frp_print.append('ε_fd = min(0.41*('+str(self.fc)+'/('+str(self.n)+'*'+str(self.Ef)+'*'+str(self.tf) +
                              '))^0.5, 0.9*'+str(self.efu)+')')
        self.frp_print.append('ε_fd = ' + str(self.efd))
        self.Tf = self.CE * self.Ef * self.Af * self.efd / 1000
        self.frp_print.append('Tf = CE Ef Af ε_fd')
        self.frp_print.append('Tf = ' + str(self.CE)+' * '+str(self.Ef)+' * '+str(self.Af)+' * '+str(self.efd)+'/1000')
        self.frp_print.append('Tf = ' + str(self.Tf))

    def CalculateMoment(self, Pu, tw, Beta, wf, Lw, d_comp, pos, Es, Asi, ce):
        self.Pu = Pu
        self.tw = tw
        self.Beta = Beta
        self.wf = wf
        self.Lw = Lw
        self.d_comp = d_comp
        self.pos = pos
        self.a = (self.Aisi + self.Pu + self.Tf) / (0.85 * self.fc * self.tw) * 1000
        self.frp_print.append("a = [Asw fy + Pu + Tf] / [0.85 fc' tw]")
        self.frp_print.append('a = ('+str(self.Aisi)+' + '+str(self.Pu)+' + '+str(self.Tf)+') / (0.85 * '+str(self.fc) +
                              ' * '+str(self.tw)+') * 1000')
        self.frp_print.append('a = ' + str(self.a))
        self.c = self.a / self.Beta
        self.frp_print.append('c = a / β')
        self.frp_print.append('c = ' + str(self.a)+' / '+str(self.Beta))
        self.frp_print.append('c = ' + str(self.c))
        self.Es = Es
        self.Asi = Asi
        self.ce = ce
        while abs(self.c - self.c1) > 0.0000000001:
            actual_efeCG = self.efd * (1 + self.wf / 2 / (self.c + 1 - self.Lw))
            if actual_efeCG <= self.efd:
                actual_Tf = self.CE * self.Ef * self.Af * actual_efeCG / 1000
                if actual_Tf <= self.Tf:
                    self.Tf = actual_Tf
            self.ec = min(self.efd * (1 / (self.Lw / self.c - 1)), 0.003)
            self.esc = min(self.ec * (self.c - self.d_comp) / self.c, self.efu)
            length = len(self.pos)
            self.E_Asi_fsi = 0
            self.E_Asi_fsi_dsi = 0
            l_esi = []
            l_fsi = []
            l_Asi_fsi =[]
            l_dsi = []
            l_Asi_fsi_dsi = []
            for x in range(length):
                esi = self.ec * (1 - self.pos[x] / self.c)
                if esi > 0:
                    fsi = min(self.fy, self.Es * esi)
                    Asi_fsi = self.Asi[x] * fsi / 1000
                    dsi = self.c - self.pos[x]
                    Asi_fsi_dsi = abs(Asi_fsi * dsi / 1000)
                else:
                    fsi = max(-self.fy, self.Es * esi)
                    Asi_fsi = self.Asi[x] * fsi / 1000
                    dsi = self.c - self.pos[x]
                    Asi_fsi_dsi = -1 * abs(Asi_fsi * dsi / 1000)
                l_esi.append(esi)
                l_fsi.append(fsi)
                l_Asi_fsi.append(Asi_fsi)
                l_dsi.append(dsi)
                l_Asi_fsi_dsi.append(Asi_fsi_dsi)
                self.E_Asi_fsi += Asi_fsi
                self.E_Asi_fsi_dsi += Asi_fsi_dsi
            self.c1 = self.c
            self.a = (abs(self.E_Asi_fsi) + self.Pu + self.Tf) / (0.85 * self.fc * self.tw) * 1000
            self.c = self.a / self.Beta
        self.frp_print.append('BY ITERATION:')
        self.frp_print.append('actual ε_feCG = ε_fd [1 + wf/2 / (c + 1 - Lw)]')
        self.frp_print.append('actual ε_feCG = ' + str(actual_efeCG))
        self.frp_print.append('actual Tf = CE Ef Af ε_feCG')
        self.frp_print.append('actual Tf = ' + str(actual_Tf))
        self.frp_print.append('ε_c = ε_fd [1 / (Lw / c - 1)]  ≤  ε_cu = 0.003')
        self.frp_print.append('ε_c = ' + str(self.ec))
        self.frp_print.append("ε_sc = ε_c [c - d'] / c")
        self.frp_print.append('ε_sc = ' + str(self.esc))
        self.frp_print.append('Asi = ' + str(self.Asi))
        self.frp_print.append('di = ' + str(self.pos))
        self.frp_print.append('ε_si = ε_c (1 - di/c)')
        self.frp_print.append('ε_si = ' + str(l_esi))
        self.frp_print.append('fsi = = ε_c (1 - di/c)')
        self.frp_print.append('fsi = ' + str(l_fsi))
        self.frp_print.append('Asi fsi = ' + str(l_Asi_fsi))
        self.frp_print.append('dsi = c - di')
        self.frp_print.append('dsi = ' + str(l_dsi))
        self.frp_print.append('Asi_fsi_dsi = ' + str(l_Asi_fsi_dsi))
        self.frp_print.append('ΣAsi_fsi = ' + str(abs(self.E_Asi_fsi)))
        self.frp_print.append('ΣAsi_fsi_dsi = ' + str(abs(self.E_Asi_fsi_dsi)))
        self.frp_print.append("a = [ΣAsi_fsi + Pu + Tf] / [0.85 fc' tw]")
        self.frp_print.append('a = ('+str(abs(self.E_Asi_fsi))+' + '+str(self.Pu)+' + '+str(self.Tf)+') / (0.85 * ' +
                              str(self.fc) + ' * '+str(self.tw)+') * 1000')
        self.frp_print.append('a = ' + str(self.a))
        self.frp_print.append('c = a / β')
        self.frp_print.append('c = ' + str(self.a) + ' / ' + str(self.Beta))
        self.frp_print.append('c = ' + str(self.c))
        Cc = abs(self.E_Asi_fsi) + self.Pu + self.Tf
        self.frp_print.append('Cc = [Tf + Pu + ΣAsi_fsi]')
        self.frp_print.append('Cc = '+str(abs(self.E_Asi_fsi))+') + '+str(self.Pu)+' + '+str(self.Tf))
        self.frp_print.append('Cc = ' + str(Cc))
        self.oMn = self.flexural_reduction * (Cc*(self.c-self.a/2)+self.Pu*(self.Lw/2-self.c)+self.Tf*self.ce*
                                              (self.Lw-self.c-self.wf/2-self.d_comp)+abs(self.E_Asi_fsi_dsi)*1000)/1000
        self.frp_print.append("φMn = φ [Cc (c - a/2) + Pu (Lw/2 - c) + Ψf Tf (Lw - c - wf/2 - d') + ΣAsi_fsi_di]")
        self.frp_print.append('φMn = '+str(self.flexural_reduction)+' * ('+str(Cc)+'*('+str(self.c)+'-'+str(self.a) +
                              '/2)+'+str(self.Pu)+'*('+str(self.Lw)+'/2-'+str(self.c)+')+'+str(self.Tf) +
                              '*'+str(self.ce)+'*('+str(self.Lw)+'-'+str(self.c)+'-'+str(self.wf) +
                              '/2-'+str(self.d_comp)+')+'+str(abs(self.E_Asi_fsi_dsi))+'*1000)/1000')
        self.frp_print.append('φMn = ' + str(self.oMn))



