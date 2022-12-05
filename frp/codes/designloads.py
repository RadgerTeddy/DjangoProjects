class Loads:
    def __init__(self):
        self.momentDL = 0                 # deadload moment - existing kNm
        self.momentLL = 0                 # liveload moment - existing kNm
        self.momentDL1 = 0                # deadload moment - anticipated kNm
        self.momentLL1 = 0                # liveload moment - anticipated kNm
        self.momentMs = 0                 # service moment - existing kNm
        self.momentMs1 = 0                # service moment - anticipated kNm
        self.momentMus = 0                # unstrengthened moment - anticipated kNm
        self.momentMu = 0                 # factored moment - existing kNm
        self.momentMu1 = 0                # factored moment - anticipated kNm
        self.momentMu2 = 0                # factored moment DL + LL - anticipated kNm
        self.shearDL = 0                  # deadload shear - anticipated kN
        self.shearLL = 0                  # liveload shear - anticipated kN
        self.shearVus = 0                 # unstrengthened shear - anticipated kN
        self.shear = 0                    # factored required shear strength kN
        self.axialDL = 0                  # deadload axial - anticipated kN
        self.axialLL = 0                  # liveload axial - anticipated kN
        self.axialPus = 0                 # unstrengthened axial - anticipated kN
        self.axial = 0                    # factored required axial strength kN
        self.axial1 = 0                   # addl factored required axial strength kN
        self.frp_print = []

    def Calculate_Loads(self):
        self.momentMs = self.momentDL + self.momentLL
        self.frp_print.append('Existing Service-load Moment, Ms = existing service moment DL + existing service moment'
                              ' LL')
        self.frp_print.append('Ms = '+str(self.momentDL)+' + '+str(self.momentLL))
        self.frp_print.append('Ms = '+str(self.momentMs))
        self.momentMs1 = self.momentDL1 + self.momentLL1
        self.frp_print.append('Anticipated Service-load Moment, Ms = anticipated service moment DL + anticipated '
                              'service moment LL')
        self.frp_print.append('Ms = '+str(self.momentDL1)+' + '+str(self.momentLL1))
        self.frp_print.append('Ms = '+str(self.momentMs1))
        self.momentMus = self.momentDL1 * 1.1 + self.momentLL1 * 0.75
        self.frp_print.append('Anticipated Factored Moment, Mus = anticipated factored moment DL * 1.1  + anticipated'
                              ' factored moment LL * 0.75')
        self.frp_print.append('Mus = '+str(self.momentDL1)+' * 1.1 + '+str(self.momentLL1)+' * 0.75')
        self.frp_print.append('Mus = '+str(self.momentMus))
        # self.momentMu = self.momentDL * 1.2 + self.momentLL * 1.6
        # self.frp_print.append('Existing Factored Moment, Mu = existing factored moment DL * 1.2  + existing factored '
        #                       'moment LL * 1.6')
        # self.frp_print.append('Mu = '+str(self.momentDL)+' * 1.2 + '+str(self.momentLL)+' * 1.6')
        # self.frp_print.append('Mu = '+str(self.momentMu))
        # self.momentMu2 = self.momentDL1 * 1.2 + self.momentLL1 * 1.6
        # self.frp_print.append('Anticipated Factored Moment (DL+LL), Mu = anticipated factored moment DL * 1.2  + anticipated'
        #                       ' factored moment LL * 1.6')
        # self.frp_print.append('Mu (DL+LL) = '+str(self.momentDL1)+' * 1.2 + '+str(self.momentLL1)+' * 1.6')
        # self.frp_print.append('Mu (DL+LL) = '+str(self.momentMu2))

    def Calculate_ShearLoads(self):
        self.shearVus = self.shearDL * 1.1 + self.shearLL * 0.75
        self.frp_print.append('Anticipated Factored Shear, Vus = anticipated factored shear DL * 1.1  + anticipated'
                              ' factored shear LL * 0.75')
        self.frp_print.append('Vus = '+str(self.shearDL)+' * 1.1 + '+str(self.shearLL)+' * 0.75')
        self.frp_print.append('Vus = '+str(self.shearVus))

    def Calculate_ColumnLoads(self):
        self.axialPus = self.axialDL * 1.1 + self.axialLL * 0.75
        self.frp_print.append('Anticipated Factored Axial, Pus = anticipated factored axial DL * 1.1  + anticipated'
                              ' factored axial LL * 0.75')
        self.frp_print.append('Pus = '+str(self.axialDL)+' * 1.1 + '+str(self.axialLL)+' * 0.75')
        self.frp_print.append('Pus = '+str(self.axialPus))
        self.momentMus = self.momentDL * 1.1 + self.momentLL * 0.75
        self.frp_print.append('Anticipated Factored Moment, Mus = anticipated factored moment DL * 1.1  + anticipated'
                              ' factored moment LL * 0.75')
        self.frp_print.append('Mus = '+str(self.momentDL)+' * 1.1 + '+str(self.momentLL)+' * 0.75')
        self.frp_print.append('Mus = '+str(self.momentMus))
