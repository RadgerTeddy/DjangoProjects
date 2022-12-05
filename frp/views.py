import datetime
from django.shortcuts import render
from .forms import FlexuralFormA, FlexuralFormB, FlexuralForm, ShearForm, ShearWallForm, ColumnForm, MonitorForm, \
    MonitorFormS, MonitorFormQ, MonitorFormE, InstallForm
from frp.codes.frpdata import *
from frp.codes.concrete import *
from frp.codes.designloads import *
from frp.codes.frpbeamdesign import *
from frp.codes.frpsheardesign import *
from frp.codes.frpshearwall import *
from frp.codes.frpcolumndesign import *
import matplotlib.pyplot as plt
from matplotlib import path
import base64
from io import BytesIO

concrete = ConcreteProperties()
frp = FRPData()
loads = Loads()
frpDesign = FRPBeamDesign()
frpShear = FRPShearDesign()
frpWall = FRPShearWallDesign()
frpColumn = FRPColumnDesign()
y = []


# Create your views here.
def home(request):
    return render(request, 'home.html')


def frpflexural(request):
    global frpBeam
    if request.method == 'POST':
        form = FlexuralForm(request.POST)
        if form.is_valid():
            frpData = form.cleaned_data
            frpBeam = calculate_beam(frpData, 1)
    else:
        form = FlexuralForm()
        frpBeam = ""
    return render(request, 'frpflexural.html', {'form': form, 'frpBeam': frpBeam})


def frpflexuralA(request):
    global frpBeam
    if request.method == 'POST':
        form = FlexuralFormA(request.POST)
        if form.is_valid():
            frpData = form.cleaned_data
            frpBeam = calculate_beam(frpData, 2)
    else:
        form = FlexuralFormA()
        frpBeam = ""
    return render(request, 'frpflexuralA.html', {'form': form, 'frpBeam': frpBeam})


def frpflexuralB(request):
    global frpBeam
    if request.method == 'POST':
        form = FlexuralFormB(request.POST)
        if form.is_valid():
            frpData = form.cleaned_data
            frpBeam = calculate_beam(frpData, 3)
    else:
        form = FlexuralFormB()
        frpBeam = ""
    return render(request, 'frpflexuralB.html', {'form': form, 'frpBeam': frpBeam})


def frpShearCalc(request):
    global frpbeamshear
    if request.method == 'POST':
        form = ShearForm(request.POST)
        if form.is_valid():
            frpData = form.cleaned_data
            frpbeamshear = calculate_shear(frpData)
    else:
        form = ShearForm()
        frpbeamshear = ""
    return render(request, 'frpshear.html', {'form': form, 'frpbeamshear': frpbeamshear})


def frpShearWall(request):
    global frpwallshear
    if request.method == 'POST':
        form = ShearWallForm(request.POST)
        if form.is_valid():
            frpData = form.cleaned_data
            frpwallshear = calculate_wall(frpData)
    else:
        form = ShearWallForm()
        frpwallshear = ""
    return render(request, 'frpShearWall.html', {'form': form, 'frpwallshear': frpwallshear})


def frpColumnCalc(request):
    global frpcolumndesign, chart
    if request.method == 'POST':
        form = ColumnForm(request.POST)
        if form.is_valid():
            frpData = form.cleaned_data
            frpcolumndesign, chart = calculate_column(frpData)
    else:
        form = ColumnForm()
        frpcolumndesign, chart = "", ""
    return render(request, 'frpColumn.html', {'form': form, 'frpcolumndesign': frpcolumndesign, 'chart': chart})


def frpMonitor(request):
    if request.method == 'POST':
        formI = MonitorForm(request.POST)
        formS = MonitorFormS(request.POST)
        formQ = MonitorFormQ(request.POST)
        formE = MonitorFormE(request.POST)
        if formI.is_valid():
            frpData1 = formI.cleaned_data
        if formS.is_valid():
            frpData2 = formS.cleaned_data
        if formQ.is_valid():
            frpData3 = formQ.cleaned_data
        if formE.is_valid():
            frpData4 = formE.cleaned_data
    else:
        formI = MonitorForm()
        formS = MonitorFormS()
        formQ = MonitorFormQ()
        formE = MonitorFormE()
    form = {'formI': MonitorForm, 'formS': MonitorFormS, 'formQ': MonitorFormQ, 'formE': MonitorFormE}
    return render(request, 'frpMonitor.html', {'form': form})


def frpInstall(request):
    global frpInstall
    if request.method == 'POST':
        form = InstallForm(request.POST)
        if form.is_valid():
            frpData = form.cleaned_data
            frpInstall = frpInstallData(frpData)
    else:
        form = InstallForm()
        frpInstall = ""
    return render(request, 'frpInstall.html', {'form': form, 'frpInstall': frpInstall})


def calculate_column(f):
    global graph
    concrete.h = f.get("h")
    concrete.b = f.get("b")
    concrete.fc = f.get("fc")
    concrete.fy = f.get("fy")
    concrete.cc = f.get("cc")
    concrete.bardia = f.get("bardia")
    concrete.verbarspacing = f.get("verbarspacing")
    concrete.horbarspacing = f.get("horbarspacing")
    concrete.sbardia = f.get("sbardia")
    frp.tf_frp = f.get("tf_frp")
    frp.n_frp = float(f.get("n_frp"))
    frp.f_fu1 = f.get("f_fu1")
    frp.e_fu1 = f.get("e_fu1")
    frp.E_f = f.get("E_f")
    frp.ce_val = f.get("frp_exposure")
    frp.ce_val1 = f.get("frp_type")
    loads.axialDL = f.get("axialDL")
    loads.axialLL = f.get("axialLL")
    loads.momentDL = f.get("momentDL")
    loads.momentLL = f.get("momentLL")
    loads.axial = f.get("axial")
    loads.momentMu = f.get("momentMu")
    loads.axial1 = f.get("axial1")
    loads.momentMu1 = f.get("momentMu1")

    concrete.frp_print = []
    frp.frp_print = []
    loads.frp_print = []
    frpColumn.frp_print = []
    try:
        concrete.Calculate_Column()
        frp.Calculate_FRPShear()
        loads.Calculate_ColumnLoads()
        frpColumn.oPn = []
        frpColumn.oMn = []
        frpColumn.CalculateColumn(concrete.fc, concrete.fy, concrete.Ac, concrete.Ast, frp.SRF, concrete.b, concrete.h,
                                  concrete.Ec, concrete.Es, concrete.rebar_pos, concrete.rebar_Area, concrete.ecu)
        frpColumn.CalculateColumnFRP(concrete.bardia, concrete.rho_g, 0.95, frp.alpha, frp.n_frp,
                                     frp.tf_frp, frp.f_fu1, frp.e_fu1, frp.E_f)

    except ZeroDivisionError:
        print("Cannot divide by zero")

        return 0

    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    y = []
    for x in concrete.frp_print:
        y.append(x)
    for x in frp.frp_print:
        y.append(x)
    for x in loads.frp_print:
        y.append(x)
    for x in frpColumn.frp_print:
        y.append(x)
    if frpColumn.oPn and frpColumn.oMn:
        if len(frpColumn.oPn) == 6:
            for x in range(3):
                a.append(frpColumn.oMn[x])
                b.append(frpColumn.oPn[x])
                c.append(frpColumn.oMn[x + 3])
                d.append(frpColumn.oPn[x + 3])
            k = frpColumn.oPn[0] / 0.8
            k1 = frpColumn.oPn[3] / 0.8
            m = (frpColumn.oPn[0] - k) * (frpColumn.oMn[1] - frpColumn.oMn[0]) / (frpColumn.oPn[1] - k) + frpColumn.oMn[
                0]
            m1 = (frpColumn.oPn[3] - k1) * (frpColumn.oMn[4] - frpColumn.oMn[3]) / (frpColumn.oPn[4] - k1) + \
                 frpColumn.oMn[3]
            a.insert(1, m)
            b.insert(1, frpColumn.oPn[0])
            c.insert(1, m1)
            d.insert(1, frpColumn.oPn[3])
            e = [frpColumn.oMn[0], m]
            f = [k, frpColumn.oPn[0]]
            g = [frpColumn.oMn[3], m1]
            h = [k1, frpColumn.oPn[3]]

            plt.switch_backend('AGG')
            plt.figure(figsize=(10, 5))
            plt.clf()
            plt.plot(a, b)
            plt.plot(c, d)
            plt.plot(e, f, linestyle='dotted')
            plt.plot(g, h, linestyle='dotted')
            plt.ylabel("φPn (kN)")
            plt.xlabel("φMn (kNm)")
            plt.plot(loads.momentMu, loads.axial, marker='o')
            plt.annotate("Existing (φPn, φMn)", (loads.momentMu, loads.axial))
            plt.plot(loads.momentMus, loads.axialPus, marker='o')
            plt.annotate("Anticipated DL+LL (φPn, φMn)", (loads.momentMus, loads.axialPus))
            plt.plot(loads.momentMu1, loads.axial1, marker='o')
            plt.annotate("Required (φPn, φMn)", (loads.momentMu1, loads.axial1))
            plt.annotate("A", (g[0], h[0]))
            plt.annotate("A'", (c[0], d[0]))
            plt.annotate("B", (c[1], d[1]))
            plt.annotate("C", (c[2], d[2]))
            graph = get_graph()
            q = path.Path([(a[0], b[0]), (a[1], b[1]), (a[2], b[2]), (a[3], b[3]), (0, 0)])
            r = path.Path([(c[0], d[0]), (c[1], d[1]), (c[2], d[2]), (c[3], d[3]), (0, 0)])
            if q.contains_point([loads.momentMus, loads.axialPus]):
                y.append('φPn & φMn unstrengthened ≥ Pus & Mus, OK')
            else:
                y.append('φPn & φMn unstrengthened ≤ Pus & Mus, NOT OK, the strengthening limits exceeds')
            if r.contains_point([loads.momentMu1, loads.axial1]):
                y.append('φPn & φMn ≥ Pu & Mu, OK')
            else:
                y.append('φPn & φMn ≤ Pu & Mu, NOT OK')

    return y, graph


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def calculate_wall(f):
    concrete.hw = f.get("hw")
    concrete.Lw = f.get("Lw")
    concrete.dfv = 0.8 * concrete.Lw
    frp.dfv = 0.8 * concrete.Lw
    concrete.tw = f.get("tw")
    concrete.fc = f.get("fc")
    concrete.fy = f.get("fy")
    concrete.layer = int(f.get("frp_layer"))
    concrete.verbardia = f.get("verbardia")
    concrete.verbarspacing = f.get("verbarspacing")
    concrete.fy_s = f.get("fy_s")
    concrete.horbardia = f.get("horbardia")
    concrete.horbarspacing = f.get("horbarspacing")
    concrete.cc = f.get("cc")
    concrete.efu = f.get("efu")
    frp.tf_frp = f.get("tf_frp")
    frp.wf_frp = f.get("wf_frp")
    frp.n_frp = float(f.get("n_frp"))
    frp.bonded = int(f.get("frp_bonded"))
    frp.SRF = 3
    frp.f_fu1 = f.get("f_fu1")
    frp.e_fu1 = f.get("e_fu1")
    frp.E_f = f.get("E_f")
    frp.ce_val = f.get("frp_exposure")
    frp.ce_val1 = f.get("frp_type")
    loads.shearDL = f.get("shearDL")
    loads.shearLL = f.get("shearLL")
    loads.axial = f.get("axial")
    loads.shear = f.get("shear")
    loads.momentMu1 = f.get("moment")

    concrete.frp_print = []
    frp.frp_print = []
    loads.frp_print = []
    frpWall.frp_print = []
    try:
        concrete.Calculate_ShearWall()
        frp.Calculate_FRPShear()
        loads.Calculate_ShearLoads()
        oVn = concrete.Vn * frpWall.shear_reduction
        if oVn >= loads.shear:
            frpWall.frp_print.append(
                'φVn ≥ Vu, ' + str(oVn) + ' > ' + str(loads.shear) + ' OK, no need for FRP Shear Wall')
        else:
            frpWall.frp_print.append(
                'φVn ≥ Vu, ' + str(oVn) + ' < ' + str(loads.shear) + ' NOT OK, need for FRP Shear Wall')
        if oVn >= loads.shearVus:
            frpWall.frp_print.append('φVn unstrengthened ≥ Vus, ' + str(oVn) + ' > ' + str(loads.shearVus) + ' OK')
        else:
            frpWall.frp_print.append('φVn unstrengthened ≥ Vus, ' + str(oVn) + ' < ' + str(loads.shearVus) + ' NOT OK, the strengthening limits exceeds')
        frpWall.CalculateTf(concrete.fc, frp.n_frp, frp.E_f, frp.tf_frp, frp.e_fu, frp.ce, frp.Af, concrete.efu,
                            concrete.fy, concrete.Asw)
        frpWall.CalculateMoment(loads.axial, concrete.tw, concrete.Beta1, frp.wf_frp, concrete.Lw, concrete.d_comp,
                                concrete.rebar_pos, concrete.Es, concrete.rebar_Area, frp.ce)
        if frpWall.oMn >= loads.momentMu1:
            frpWall.frp_print.append('φMn ≥ Mu, ' + str(frpWall.oMn) + ' > ' + str(loads.momentMu1) + ' OK')
        else:
            frpWall.frp_print.append('φMn ≥ Mu, ' + str(frpWall.oMn) + ' < ' + str(loads.momentMu1) + ' NOT OK')

        frpShear.EffectiveStrain(frp.n_frp, frp.tf_frp, frp.E_f, concrete.fc, frp.dfv, frp.e_fu, frp.SRF, 1)
        frpShear.reductionfactor = 1
        frpShear.FRPShearStrength(frp.Afv, frp.alpha, frp.sf, concrete.Vc, concrete.Vsw, frp.FRPShearReductionFactor,
                                  3, frp.bonded)
        if frpShear.oVn >= loads.shear:
            frpShear.frp_print.append('φVn ≥ Vu, ' + str(frpShear.oVn) + ' > ' + str(loads.shear) + ' OK')
        else:
            frpShear.frp_print.append('φVn ≥ Vu, ' + str(frpShear.oVn) + ' < ' + str(loads.shear) + ' NOT OK')

    except ZeroDivisionError:
        print("Cannot divide by zero")
        return 0

    y = []
    for x in concrete.frp_print:
        y.append(x)
    for x in frp.frp_print:
        y.append(x)
    for x in loads.frp_print:
        y.append(x)
    for x in frpWall.frp_print:
        y.append(x)
    for x in frpShear.frp_print:
        y.append(x)
    return y


def calculate_beam(f, beamdesign):
    concrete.h = f.get("h")
    concrete.d = f.get("d")
    concrete.b = f.get("b")
    concrete.hf = f.get("hf")
    concrete.bf = f.get("bf")
    concrete.fc = f.get("fc")
    concrete.fy = f.get("fy")
    concrete.bardia = f.get("bardia")
    concrete.nbar = f.get("nbar")
    concrete.npressbar = f.get("npressbar")
    concrete.pressbar = f.get("pressbar")
    concrete.fpe = f.get("fpe")
    concrete.fpy = f.get("fpy")
    concrete.fpu = f.get("fpu")
    concrete.Ep = f.get("Ep")
    frp.tf_frp = f.get("tf_frp")
    frp.wf_frp = f.get("wf_frp")
    if f.get("n_frp"):
        frp.n_frp = float(f.get("n_frp"))
    frp.FRPrebar = f.get("FRPrebar")
    frp.FRPnrebar = f.get("FRPnrebar")
    frp.f_fu1 = f.get("f_fu1")
    frp.e_fu1 = f.get("e_fu1")
    frp.E_f = f.get("E_f")
    frp.ce_val = f.get("frp_exposure")
    frp.ce_val1 = f.get("frp_type")
    loads.momentDL = f.get("momentDL")
    loads.momentLL = f.get("momentLL")
    loads.momentDL1 = f.get("momentDL1")
    loads.momentLL1 = f.get("momentLL1")
    loads.momentMu1 = f.get("momentMu")

    concrete.frp_print = []
    frp.frp_print = []
    loads.frp_print = []
    frpDesign.frp_print = []
    try:
        concrete.Calculate_Concrete(beamdesign)
        frp.Calculate_FRP(beamdesign)
        loads.Calculate_Loads()
        frpDesign.SoffitStrain(concrete.Es, concrete.Ec, concrete.b, concrete.As, concrete.d, loads.momentDL,
                               concrete.h, concrete.yt, concrete.P_e, concrete.Acg, concrete.e, concrete.r, concrete.Ig,
                               concrete.h, beamdesign)
        frpDesign.FRPDesignStrain(concrete.fc, frp.n_frp, frp.E_f, frp.tf_frp, beamdesign)
        if concrete.moment >= loads.momentMus:
            frpDesign.frp_print.append('φMn unstrengthened ≥ Mus, ' + str(concrete.moment) + ' > ' + str(loads.momentMus) + ' OK')
        else:
            frpDesign.frp_print.append('φMn unstrengthened ≥ Mus, ' + str(concrete.moment) + ' < ' + str(loads.momentMus) + ' NOT OK, the strengthening limits exceeds')
        if beamdesign == 2:
            Af = frp.Af_rebar
            frpDesign.efd = frp.e_fu
        else:
            Af = frp.Af
            if frpDesign.efd <= 0.9 * frp.e_fu:
                frpDesign.frp_print.append('ε_fd ≤ 0.9 ε_fu,  OK < , ' + str(0.9 * frp.e_fu))
            else:
                frpDesign.frp_print.append('ε_fd ≤ 0.9 ε_fu,  NOT OK > , ' + str(0.9 * frp.e_fu))
        frpDesign.FRPEffectiveStrain(concrete.fy, Af, concrete.epe, concrete.fpe, concrete.Aps, beamdesign)
        frpDesign.FlexuralStrength(beamdesign)
        if frpDesign.oMn >= loads.momentMu1:
            frpDesign.frp_print.append('φMn ≥ Mu, ' + str(frpDesign.oMn) + ' > ' + str(loads.momentMu1) + ' OK')
        else:
            frpDesign.frp_print.append('φMn ≥ Mu, ' + str(frpDesign.oMn) + ' < ' + str(loads.momentMu1) + ' NOT OK')
        if beamdesign == 3:
            frpDesign.PrestressCheck(loads.momentMs1)
            if frpDesign.fpss <= 0.82 * concrete.fpy:
                frpDesign.frp_print.append('fps,s ≤ 0.82fpy, ' + str(frpDesign.fpss) + ' < ' + str(0.82 * concrete.fpy)
                                           + ' OK')
            else:
                frpDesign.frp_print.append('fps,s ≤ 0.82fpy, ' + str(frpDesign.fpss) + ' > ' + str(0.82 * concrete.fpy)
                                           + ' NOT OK')
            if frpDesign.fpss <= 0.74 * concrete.fpu:
                frpDesign.frp_print.append('fps,s ≤ 0.74fpu, ' + str(frpDesign.fpss) + ' < ' + str(0.74 * concrete.fpu)
                                           + ' OK')
            else:
                frpDesign.frp_print.append('fps,s ≤ 0.74fpu, ' + str(frpDesign.fpss) + ' > ' + str(0.74 * concrete.fpu)
                                           + ' NOT OK')
            if frpDesign.fcs <= 0.45 * concrete.fc:
                frpDesign.frp_print.append("fc,s ≤ 0.45f'c, " + str(frpDesign.fcs) + ' < ' + str(0.45 * concrete.fc) +
                                           ' OK')
            else:
                frpDesign.frp_print.append("fc,s ≤ 0.45f'c, " + str(frpDesign.fcs) + ' > ' + str(0.45 * concrete.fc) +
                                           ' NOT OK')
        frpDesign.ServiceStresses(loads.momentMs1, beamdesign)
        if beamdesign != 3:
            if frpDesign.fs_s <= 0.8 * concrete.fy:
                frpDesign.frp_print.append(
                    'fs,s ≤ 0.8fy, ' + str(frpDesign.fs_s) + ' < ' + str(0.8 * concrete.fy) + ' OK')
            else:
                frpDesign.frp_print.append(
                    'fs,s ≤ 0.8fy, ' + str(frpDesign.fs_s) + ' > ' + str(0.8 * concrete.fy) + ' NOT OK')
        if frpDesign.ff_s <= frp.sustainedstresslimit:
            frpDesign.frp_print.append('ff,s ≤ FRP Sustained plus cyclic service load stress limits, ' +
                                       str(frpDesign.ff_s) + ' < ' + str(frp.sustainedstresslimit) + ' OK')
        else:
            frpDesign.frp_print.append('ff,s ≤ FRP Sustained plus cyclic service load stress limits, ' +
                                       str(frpDesign.ff_s) + ' > ' + str(frp.sustainedstresslimit) + ' NOT OK')
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return 0
    y = []
    for x in concrete.frp_print:
        y.append(x)
    for x in frp.frp_print:
        y.append(x)
    for x in loads.frp_print:
        y.append(x)
    for x in frpDesign.frp_print:
        y.append(x)
    return y


def calculate_shear(f):
    sheardesign = int(f.get("shear_design"))
    concrete.d = f.get("d")
    concrete.b = f.get("b")
    concrete.fc = f.get("fc")
    concrete.fy_s = f.get("fy_s")
    concrete.sbardia = f.get("sbardia")
    concrete.sbar = f.get("sbar")
    frp.tf_frp = f.get("tf_frp")
    frp.wf_frp = f.get("wf_frp")
    frp.n_frp = float(f.get("n_frp"))
    frp.dfv = f.get("dfv")
    frp.sf = f.get("sf")
    frp.alpha = f.get("alpha")
    frp.SRF = int(f.get("frp_bonded"))
    frp.f_fu1 = f.get("f_fu1")
    frp.e_fu1 = f.get("e_fu1")
    frp.E_f = f.get("E_f")
    frp.ce_val = f.get("frp_exposure")
    frp.ce_val1 = f.get("frp_type")
    loads.shearDL = f.get("shearDL")
    loads.shearLL = f.get("shearLL")
    loads.shear = f.get("shear")

    concrete.frp_print = []
    frp.frp_print = []
    loads.frp_print = []
    frpShear.frp_print = []
    try:
        concrete.Calculate_Shear(sheardesign)
        frp.Calculate_FRPShear()
        loads.Calculate_ShearLoads()
        frpShear.EffectiveStrain(frp.n_frp, frp.tf_frp, frp.E_f, concrete.fc, frp.dfv, frp.e_fu, frp.SRF, sheardesign)
        frpShear.FRPShearStrength(frp.Afv, frp.alpha, frp.sf, concrete.Vc, concrete.Vs, frp.FRPShearReductionFactor, 2,
                                  1)
        if concrete.oVn >= loads.shearVus:
            frpShear.frp_print.append('φVn unstrengthened ≥ Vus, ' + str(concrete.oVn) + ' > ' + str(loads.shearVus) + ' OK')
        else:
            frpShear.frp_print.append('φVn unstrengthened ≥ Vus, ' + str(concrete.oVn) + ' < ' + str(loads.shearVus) + ' NOT OK, the strengthening limits exceeds')
        if frpShear.oVn >= loads.shear:
            frpShear.frp_print.append('φVn ≥ Vu, ' + str(frpShear.oVn) + ' > ' + str(loads.shear) + ' OK')
        else:
            frpShear.frp_print.append('φVn ≥ Vu, ' + str(frpShear.oVn) + ' < ' + str(loads.shear) + ' NOT OK')

    except ZeroDivisionError:
        print("Cannot divide by zero")
        return 0

    y = []
    for x in concrete.frp_print:
        y.append(x)
    for x in frp.frp_print:
        y.append(x)
    for x in loads.frp_print:
        y.append(x)
    for x in frpShear.frp_print:
        y.append(x)
    return y


def frpInstallData(f):
    Resins_Storage_Date = f.get("Resins_Storage_Date")
    Rshell_life = f.get("Rshell_life")
    Rstorage_temp_min = f.get("Rstorage_temp_min")
    Rstorage_temp_max = f.get("Rstorage_temp_max")
    Rstorage_temp_act = f.get("Rstorage_temp_act")
    Fabrics_Storage_Date = f.get("Fabrics_Storage_Date")
    Fshell_life = f.get("Fshell_life")
    Fstorage_temp_min = f.get("Fstorage_temp_min")
    Fstorage_temp_max = f.get("Fstorage_temp_max")
    Fstorage_temp_act = f.get("Fstorage_temp_act")
    Rpot_life = f.get("Rpot_life")
    Ambient_temp_min = f.get("Ambient_temp_min")
    Ambient_temp_max = f.get("Ambient_temp_max")
    Ambient_temp_act = f.get("Ambient_temp_act")
    Substrate_temp_min = f.get("Substrate_temp_min")
    Substrate_temp_max = f.get("Substrate_temp_max")
    Substrate_temp_act = f.get("Substrate_temp_act")
    Substrate_moist_max = f.get("Substrate_moist_max")
    Substrate_moist_act = f.get("Substrate_moist_act")
    FRP_curing_time = f.get("FRP_curing_time")
    now = datetime.date.today()
    Rremain = (now.year - Resins_Storage_Date.year) * 12 + (now.month - Resins_Storage_Date.month) + (
            now.day - Resins_Storage_Date.day) / 30
    y = []
    if Rremain < Rshell_life:
        y.append('Resins actual shell life: ' + str(Rremain) + ' months -  OK')
    else:
        y.append('Resins actual shell life: ' + str(Rremain) + ' months -  NOT OK, for disposal')
    if Rstorage_temp_max > Rstorage_temp_act > Rstorage_temp_min:
        y.append('Resins storage temperature is OK')
    else:
        y.append('Resins storage temperature is NOT OK')
    Fremain = (now.year - Fabrics_Storage_Date.year) * 12 + (now.month - Fabrics_Storage_Date.month) + (
            now.day - Fabrics_Storage_Date.day) / 30
    if Fremain < Fshell_life:
        y.append('Fabrics actual shell life: ' + str(Fremain) + ' months -  OK')
    else:
        y.append('Fabrics actual shell life: ' + str(Fremain) + ' months -  NOT OK, for disposal')
    if Fstorage_temp_max > Fstorage_temp_act > Fstorage_temp_min:
        y.append('Fabrics storage temperature is OK')
    else:
        y.append('Fabrics storage temperature is NOT OK')
    if Ambient_temp_max > Ambient_temp_act > Ambient_temp_min:
        y.append('Ambient temperature is OK')
    else:
        y.append('Ambient temperature is NOT OK')
    if Substrate_temp_max > Substrate_temp_act > Substrate_temp_min:
        y.append('Substrate temperature is OK')
    else:
        y.append('Substrate temperature is NOT OK')
    if Substrate_moist_act < Substrate_moist_max:
        y.append('Substrate moisture content is OK')
    else:
        y.append('Substrate moisture content is NOT OK')
    Premain = datetime.datetime.now() + datetime.timedelta(hours=Rpot_life / 60)
    y.append('MIXED RESINS WILL EXPIRED ON: ' + Premain.strftime("%B-%d-%Y %H:%M:%S, %A"))
    Wremain = datetime.datetime.now() + datetime.timedelta(hours=FRP_curing_time)
    y.append('NEXT LAYER APPLICATION IF MIXED RESINS EXPIRED WILL BE ON: ' + Wremain.strftime("%B-%d-%Y %H:%M:%S, %A"))
    return y
