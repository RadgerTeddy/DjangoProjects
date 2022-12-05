import math

class FRPData:
    def __init__(self):
        # Properties of FRP
        self.Af = 0                 # area of FRP external reinforcement,mm^2
        self.Afv = 0                # area of FRP external reinforcement for shear,mm^2
        self.n_frp = 0              # number of FRP ply
        self.tf_frp = 0             # nominal thickness of one ply of FRP reinforcement, mm
        self.wf_frp = 0             # width of FRP reinforcing plies, mm
        self.f_fu = 0               # design ultimate tensile strength of FRP, MPa
        self.f_fu1 = 0              # design ultimate tensile strength of FRP, MPa
        self.e_fu = 0               # design rupture strain of FRP reinforcement, mm/mm
        self.e_fu1 = 0              # design rupture strain of FRP reinforcement, mm/mm
        self.E_f = 0                # tensile modulus of elasticity of FRP, MPa
        self.ce_val = 'Interior exposure'
        self.ce_val1 = 'Carbon'
        self.CE = {'Interior exposure': {'Carbon': 0.95, 'Glass': 0.75, 'Aramid': 0.85},
                   'Exterior exposure': {'Carbon': 0.85, 'Glass': 0.65, 'Aramid': 0.75},
                   'Aggressive environment': {'Carbon': 0.85, 'Glass': 0.5, 'Aramid': 0.7}
                   }
        self.ce = 0
        self.sustainedstresslimit = 0
        self.FRPrebar = 0
        self.FRPnrebar = 0
        self.Af_rebar = 0
        self.SRF = 1                        # Completely Wrapped, Three-side Wrap, Two-opposite-sides Wrap
        self.FRPShearReductionFactor = 0
        self.alpha = 0
        self.dfv = 0                        # effective depth of each FRP sheet, dfv (mm)
        self.sf = 0                         # Span between each FRP sheet, sf (mm)
        self.stripL = 0                     # FRP strip length (mm)
        self.frp_print = []
        self.bonded = 0

    def Calculate_reduction(self):
        for ce_k, ce_v in self.CE.items():
            if ce_k == self.ce_val:
                self.ce = ce_v[self.ce_val1]
        self.frp_print.append('CE (from Table 9.4) = '+str(self.ce))
        self.f_fu = self.ce * self.f_fu1
        self.frp_print.append('f_fu = CE * f_fu1')
        self.frp_print.append('f_fu = '+str(self.ce)+' * '+str(self.f_fu1))
        self.frp_print.append('f_fu = '+str(self.f_fu))
        self.e_fu = self.ce * self.e_fu1
        self.frp_print.append('ε_fu = CE * ε_fu1')
        self.frp_print.append('ε_fu = '+str(self.ce)+' * '+str(self.e_fu1))
        self.frp_print.append('ε_fu = '+str(self.e_fu))

    def Calculate_FRP_Area(self, beamdesign):
        if beamdesign == 2:
            self.Af_rebar = self.FRPrebar ** 2 * self.FRPnrebar * math.pi / 4
            self.frp_print.append('Af_rebar = FRP rebar diameter ^ 2 * FRP number of rebar * math.pi / 4')
            self.frp_print.append(
                'Af_rebar = ' + str(self.FRPrebar) + ' ^ 2 * ' + str(self.FRPnrebar) + ' * ' + str(math.pi) + ' / 4')
            self.frp_print.append('Af_rebar = ' + str(self.Af_rebar))
        else:
            if self.bonded == 2:
                self.Af = 2 * self.n_frp * self.tf_frp * self.wf_frp
                self.frp_print.append('Af = 2 * n_frp * tf_frp * wf_frp')
                self.frp_print.append('Af = 2 * '+str(self.n_frp)+' * '+str(self.tf_frp)+' * '+str(self.wf_frp))
            else:
                self.Af = self.n_frp * self.tf_frp * self.wf_frp
                self.frp_print.append('Af = n_frp * tf_frp * wf_frp')
                self.frp_print.append('Af = '+str(self.n_frp)+' * '+str(self.tf_frp)+' * '+str(self.wf_frp))
            self.frp_print.append('Af = '+str(self.Af))

    def Calculate_FRP(self, beamdesign):
        self.Calculate_FRP_Area(beamdesign)
        self.Calculate_reduction()
        if self.ce_val1 == 'Carbon':
            self.sustainedstresslimit = 0.55 * self.f_fu
            self.frp_print.append('Sustained plus cyclic stress limit = 0.55 * f_fu')
            self.frp_print.append('Sustained plus cyclic stress limit = 0.55 * '+str(self.f_fu))
            self.frp_print.append('Sustained plus cyclic stress limit = '+str(self.sustainedstresslimit))
        elif self.ce_val1 == 'Glass':
            self.sustainedstresslimit = 0.20 * self.f_fu
            self.frp_print.append('Sustained plus cyclic stress limit = 0.20 * f_fu')
            self.frp_print.append('Sustained plus cyclic stress limit = 0.20 * '+str(self.f_fu))
            self.frp_print.append('Sustained plus cyclic stress limit = '+str(self.sustainedstresslimit))
        else:
            self.sustainedstresslimit = 0.30 * self.f_fu
            self.frp_print.append('Sustained plus cyclic stress limit = 0.30 * f_fu')
            self.frp_print.append('Sustained plus cyclic stress limit = 0.30 * '+str(self.f_fu))
            self.frp_print.append('Sustained plus cyclic stress limit = '+str(self.sustainedstresslimit))

    def Calculate_FRPShear(self):
        self.Calculate_FRP_Area(1)
        self.Calculate_reduction()
        if self.SRF == 1:
            self.FRPShearReductionFactor = 0.95
            self.frp_print.append('FRP Shear Reduction Factor = '+str(self.FRPShearReductionFactor))
        else:
            self.FRPShearReductionFactor = 0.85
            self.frp_print.append('FRP Shear Reduction Factor = ' + str(self.FRPShearReductionFactor))
        self.Afv = 2 * self.n_frp * self.tf_frp * self.wf_frp
        self.frp_print.append('Afv = 2 * n_frp * tf_frp * wf_frp')
        self.frp_print.append('Afv = 2 * '+str(self.n_frp)+' * '+str(self.tf_frp)+' * '+str(self.wf_frp))
        self.frp_print.append('Afv = '+str(self.Afv))



