from django import forms


class ColumnForm(forms.Form):
    h = forms.FloatField(required=True, label='Column longer side h, mm')
    b = forms.FloatField(required=True, label='Column shorter side b, mm')
    fc = forms.FloatField(required=True, label="Concrete fc', MPa (Minimum = 17 MPa)", min_value=17)
    fy = forms.FloatField(required=True, label='Main rebar fy, MPa')
    cc = forms.FloatField(required=True, label='Column clear concrete cover, mm')
    bardia = forms.FloatField(required=True, label='Main rebar diameter, mm')
    verbarspacing = forms.IntegerField(required=True, label='Number of rebar along longer side')
    horbarspacing = forms.IntegerField(required=True, label='Number of rebar along shorter side')
    sbardia = forms.FloatField(required=True, label='Tie rebar diameter, mm')
    tf_frp = forms.FloatField(required=True, label='FRP Laminates Thickness of Ply, mm')
    n_frp = forms.ChoiceField(required=True, label='FRP Laminates Number of Ply', choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6)))
    f_fu1 = forms.FloatField(required=True, label='FRP Laminates Ultimate Tensile Strength, Mpa')
    e_fu1 = forms.FloatField(required=True, label='FRP Laminates Rupture Strain, mm/mm')
    E_f = forms.FloatField(required=True, label='FRP Laminates Modulus of elasticity, Mpa')
    frp_exposure = forms.ChoiceField(required=True, label='FRP Exposure Conditions', choices=(('Interior exposure', ('Interior exposure')),
                                                                                              ('Exterior exposure', ('Exterior exposure')),
                                                                                              ('Aggressive environment', ('Aggressive environment'))))
    frp_type = forms.ChoiceField(required=True, label='FRP Laminates Fiber Type', choices=(('Carbon', ('Carbon')),
                                                                                              ('Glass', ('Glass')),
                                                                                              ('Aramid', ('Aramid'))))
    axialDL = forms.FloatField(required=True, label='Anticipated axial dead load, kN')
    axialLL = forms.FloatField(required=True, label='Anticipated axial live load, kN')
    momentDL = forms.FloatField(required=True, label='Anticipated moment dead load, kNm')
    momentLL = forms.FloatField(required=True, label='Anticipated moment live load, kNm')
    axial = forms.FloatField(required=True, label='Factored axial strength Pu, kN')
    momentMu = forms.FloatField(required=True, label='Factored moment strength Mu, kNm')
    axial1 = forms.FloatField(required=True, label='Factored required/anticipated axial strength Pu, kN')
    momentMu1 = forms.FloatField(required=True, label='Factored required/anticipated moment strength Mu, kNm')

    def clean_fc(self):
        data = self.cleaned_data.get('fc')
        if data < 17:
            raise forms.ValidationError("fc' should not be less than 17 Mpa")
        return data


class ShearWallForm(forms.Form):
    hw = forms.FloatField(required=True, label='Shear wall height hw, mm')
    Lw = forms.FloatField(required=True, label='Shear wall length Lw, mm (dfv=0.8*Lw)')
    tw = forms.FloatField(required=True, label='Shear wall thickness tw, mm')
    fc = forms.FloatField(required=True, label="Concrete fc', MPa (Minimum = 17 MPa)", min_value=17)
    fy = forms.FloatField(required=True, label='Shear wall vertical rebar fy, MPa')
    frp_layer = forms.ChoiceField(required=True, label='Shear wall number of rebar layer', choices=((1, 1),(2, 2)))
    verbardia = forms.FloatField(required=True, label='Shear wall vertical rebar diameter, mm')
    verbarspacing = forms.FloatField(required=True, label='Shear wall vertical rebar spacing, mm')
    fy_s = forms.FloatField(required=True, label='Shear wall horizontal rebar fy, MPa')
    horbardia = forms.FloatField(required=True, label='Shear wall horizontal rebar diameter, mm')
    horbarspacing = forms.FloatField(required=True, label='Shear wall horizontal rebar spacing, mm')
    cc = forms.FloatField(required=True, label='Shear wall clear concrete cover, mm')
    efu = forms.FloatField(required=True, label='Shear wall longitudinal reinforcing yield strain, εfu*, mm/mm')
    tf_frp = forms.FloatField(required=True, label='FRP Laminates Thickness of Ply, mm')
    wf_frp = forms.FloatField(required=True, label='FRP Laminates Width of Ply, mm')
    n_frp = forms.ChoiceField(required=True, label='FRP Laminates Number of Ply', choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6)))
    frp_bonded = forms.ChoiceField(required=True, label='FRP Laminates Bonded Part', choices=((1, ('One side bonded')),
                                                                                              (2, ('Two side bonded'))))
    f_fu1 = forms.FloatField(required=True, label='FRP Laminates Ultimate Tensile Strength, Mpa')
    e_fu1 = forms.FloatField(required=True, label='FRP Laminates Rupture Strain, mm/mm')
    E_f = forms.FloatField(required=True, label='FRP Laminates Modulus of elasticity, Mpa')
    frp_exposure = forms.ChoiceField(required=True, label='FRP Exposure Conditions', choices=(('Interior exposure', ('Interior exposure')),
                                                                                              ('Exterior exposure', ('Exterior exposure')),
                                                                                              ('Aggressive environment', ('Aggressive environment'))))
    frp_type = forms.ChoiceField(required=True, label='FRP Laminates Fiber Type', choices=(('Carbon', ('Carbon')),
                                                                                              ('Glass', ('Glass')),
                                                                                              ('Aramid', ('Aramid'))))
    shearDL = forms.FloatField(required=True, label='Anticipated Dead Load Shear, kNm')
    shearLL = forms.FloatField(required=True, label='Anticipated Live Load Shear, kNm')
    axial = forms.FloatField(required=True, label='Factored required axial strength Pu, kN')
    shear = forms.FloatField(required=True, label='Factored required shear strength Vu, kN')
    moment = forms.FloatField(required=True, label='Factored required moment strength Mu, kNm')


class ShearForm(forms.Form):
    shear_design = forms.ChoiceField(required=True, label='FRP shear type design', choices=((1, ('Shear Interior Beam')),
                                                                                              (2, ('Shear Exterior Column '))))
    d = forms.FloatField(required=True, label='Effective Depth d, mm')
    b = forms.FloatField(required=True, label='Width b, mm')
    fc = forms.FloatField(required=True, label="Concrete fc', MPa (Minimum = 17 MPa)", min_value=17)
    fy_s = forms.FloatField(required=True, label='Shear Rebar fy, MPa')
    sbardia = forms.FloatField(required=True, label='Shear Rebar diameter, mm')
    sbar = forms.FloatField(required=True, label='Spacing of Shear Rebar')
    tf_frp = forms.FloatField(required=True, label='FRP Laminates Thickness of Ply, mm')
    wf_frp = forms.FloatField(required=True, label='FRP Laminates Width of Ply, mm')
    n_frp = forms.ChoiceField(required=True, label='FRP Laminates Number of Ply', choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6)))
    dfv = forms.FloatField(required=True, label='FRP Laminates Effective Depth of each FRP sheet (dfv), mm')
    sf = forms.FloatField(required=True, label='FRP Laminates Span between each FRP sheet (sf), mm')
    alpha = forms.FloatField(required=True, label='FRP Laminates Wrapping Angle')
    frp_bonded = forms.ChoiceField(required=True, label='FRP Laminates Bonded Part', choices=((1, ('Completely Wrapped')),
                                                                                              (2, ('Three side Wrap')),
                                                                                              (3, ('Two opposite sides Wrap'))))
    f_fu1 = forms.FloatField(required=True, label='FRP Laminates Ultimate Tensile Strength, Mpa')
    e_fu1 = forms.FloatField(required=True, label='FRP Laminates Rupture Strain, mm/mm')
    E_f = forms.FloatField(required=True, label='FRP Laminates Modulus of elasticity, Mpa')
    frp_exposure = forms.ChoiceField(required=True, label='FRP Exposure Conditions', choices=(('Interior exposure', ('Interior exposure')),
                                                                                              ('Exterior exposure', ('Exterior exposure')),
                                                                                              ('Aggressive environment', ('Aggressive environment'))))
    frp_type = forms.ChoiceField(required=True, label='FRP Laminates Fiber Type', choices=(('Carbon', ('Carbon')),
                                                                                              ('Glass', ('Glass')),
                                                                                              ('Aramid', ('Aramid'))))
    shearDL = forms.FloatField(required=True, label='Anticipated Dead Load Shear, kNm')
    shearLL = forms.FloatField(required=True, label='Anticipated Live Load Shear, kNm')
    shear = forms.FloatField(required=True, label='Design Anticipated Factored Shear Vu, kN')


class FlexuralForm(forms.Form):
    h = forms.FloatField(required=True, label='Beam Height h, mm')
    d = forms.FloatField(required=True, label='Beam Effective Depth d, mm')
    b = forms.FloatField(required=True, label='Beam Width b, mm')
    fc = forms.FloatField(required=True, label="Concrete fc', MPa (Minimum = 17 MPa)", min_value=17)
    fy = forms.FloatField(required=True, label='Main Rebar fy, MPa')
    bardia = forms.FloatField(required=True, label='Main Rebar diameter, mm')
    nbar = forms.IntegerField(required=True, label='Number of Main Rebar')
    tf_frp = forms.FloatField(required=True, label='FRP Laminates Thickness of Ply, mm')
    wf_frp = forms.FloatField(required=True, label='FRP Laminates Width of Ply, mm')
    n_frp = forms.ChoiceField(required=True, label='FRP Laminates Number of Ply', choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6)))
    f_fu1 = forms.FloatField(required=True, label='FRP Laminates Ultimate Tensile Strength, Mpa')
    e_fu1 = forms.FloatField(required=True, label='FRP Laminates Rupture Strain, mm/mm')
    E_f = forms.FloatField(required=True, label='FRP Laminates Modulus of elasticity, Mpa')
    frp_exposure = forms.ChoiceField(required=True, label='FRP Exposure Conditions', choices=(('Interior exposure', ('Interior exposure')),
                                                                                              ('Exterior exposure', ('Exterior exposure')),
                                                                                              ('Aggressive environment', ('Aggressive environment'))))
    frp_type = forms.ChoiceField(required=True, label='FRP Laminates Fiber Type', choices=(('Carbon', ('Carbon')),
                                                                                              ('Glass', ('Glass')),
                                                                                              ('Aramid', ('Aramid'))))
    momentDL = forms.FloatField(required=True, label='Existing Dead Load Moment, kNm')
    momentLL = forms.FloatField(required=True, label='Existing Live Load Moment, kNm')
    momentDL1 = forms.FloatField(required=True, label='Anticipated Dead Load Moment, kNm')
    momentLL1 = forms.FloatField(required=True, label='Anticipated Live Load Moment, kNm')
    momentMu = forms.FloatField(required=True, label='Design Anticipated Factored Moment Mu, kNm')


class FlexuralFormA(forms.Form):
    h = forms.FloatField(required=True, label='Beam Height h, mm')
    d = forms.FloatField(required=True, label='Beam Effective Depth d, mm')
    b = forms.FloatField(required=True, label='Beam Width b, mm')
    fc = forms.FloatField(required=True, label="Concrete fc', MPa (Minimum = 17 MPa)", min_value=17)
    fy = forms.FloatField(required=True, label='Main Rebar fy, MPa')
    bardia = forms.FloatField(required=True, label='Main Rebar diameter, mm')
    nbar = forms.IntegerField(required=True, label='Number of Main Rebar')
    FRPrebar = forms.FloatField(required=True, label='FRP Laminates Rebar Diameter, mm')
    FRPnrebar = forms.FloatField(required=True, label='FRP Laminates Number of Rebar')
    f_fu1 = forms.FloatField(required=True, label='FRP Laminates Ultimate Tensile Strength, Mpa')
    e_fu1 = forms.FloatField(required=True, label='FRP Laminates Rupture Strain, mm/mm')
    E_f = forms.FloatField(required=True, label='FRP Laminates Modulus of elasticity, Mpa')
    frp_exposure = forms.ChoiceField(required=True, label='FRP Exposure Conditions', choices=(('Interior exposure', ('Interior exposure')),
                                                                                              ('Exterior exposure', ('Exterior exposure')),
                                                                                              ('Aggressive environment', ('Aggressive environment'))))
    frp_type = forms.ChoiceField(required=True, label='FRP Laminates Fiber Type', choices=(('Carbon', ('Carbon')),
                                                                                              ('Glass', ('Glass')),
                                                                                              ('Aramid', ('Aramid'))))
    momentDL = forms.FloatField(required=True, label='Existing Dead Load Moment, kNm')
    momentLL = forms.FloatField(required=True, label='Existing Live Load Moment, kNm')
    momentDL1 = forms.FloatField(required=True, label='Anticipated Dead Load Moment, kNm')
    momentLL1 = forms.FloatField(required=True, label='Anticipated Live Load Moment, kNm')
    momentMu = forms.FloatField(required=True, label='Design Anticipated Factored Moment Mu, kNm')


class FlexuralFormB(forms.Form):
    h = forms.FloatField(required=True, label='Beam Height h, mm')
    d = forms.FloatField(required=True, label='Beam Effective Depth d, mm')
    b = forms.FloatField(required=True, label='Beam Width b, mm')
    hf = forms.FloatField(required=True, label='Beam Flange height hf, mm')
    bf = forms.FloatField(required=True, label='Beam Flange Width bf, mm')
    fc = forms.FloatField(required=True, label="Concrete fc', MPa (Minimum = 17 MPa)", min_value=17)
    fy = forms.FloatField(required=True, label='Main Rebar fy, MPa')
    npressbar = forms.IntegerField(required=True, label='Number of Prestressing Reinforcement')
    pressbar = forms.FloatField(required=True, label='Area of Prestressing Reinforcement, sq.mm.')
    fpe = forms.FloatField(required=True, label='Prestressed Effective Strength fpe, MPa')
    fpy = forms.FloatField(required=True, label='Prestressed Yield Strength fpy, MPa')
    fpu = forms.FloatField(required=True, label='Prestressed Ultimate Strength fpu, MPa')
    Ep = forms.FloatField(required=True, label='Prestressed Modulus of Elasticity Ep, MPa')
    tf_frp = forms.FloatField(required=True, label='FRP Laminates Thickness of Ply, mm')
    wf_frp = forms.FloatField(required=True, label='FRP Laminates Width of Ply, mm')
    n_frp = forms.ChoiceField(required=True, label='FRP Laminates Number of Ply', choices=((1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6)))
    f_fu1 = forms.FloatField(required=True, label='FRP Laminates Ultimate Tensile Strength, Mpa')
    e_fu1 = forms.FloatField(required=True, label='FRP Laminates Rupture Strain, mm/mm')
    E_f = forms.FloatField(required=True, label='FRP Laminates Modulus of elasticity, Mpa')
    frp_exposure = forms.ChoiceField(required=True, label='FRP Exposure Conditions', choices=(('Interior exposure', ('Interior exposure')),
                                                                                              ('Exterior exposure', ('Exterior exposure')),
                                                                                              ('Aggressive environment', ('Aggressive environment'))))
    frp_type = forms.ChoiceField(required=True, label='FRP Laminates Fiber Type', choices=(('Carbon', ('Carbon')),
                                                                                              ('Glass', ('Glass')),
                                                                                              ('Aramid', ('Aramid'))))
    momentDL = forms.FloatField(required=True, label='Existing Dead Load Moment, kNm')
    momentLL = forms.FloatField(required=True, label='Existing Live Load Moment, kNm')
    momentDL1 = forms.FloatField(required=True, label='Anticipated Dead Load Moment, kNm')
    momentLL1 = forms.FloatField(required=True, label='Anticipated Live Load Moment, kNm')
    momentMu = forms.FloatField(required=True, label='Design Anticipated Factored Moment Mu, kNm')

class MonitorForm(forms.Form):
    frp_system = forms.ChoiceField(required=True, label='FRP System', choices=((1, "Dry"), (2, "Wet")))
    frp_fiber = forms.ChoiceField(required=True, label='FRP Fiber', choices=((1, "uni-directional"), (2, "bi-directional")))
    engineer = forms.CharField(required=True, label='Project Engineer')
    frp_engineer = forms.CharField(required=True, label='FRP Engineer')
    testing_agency = forms.CharField(required=True, label='FRP Independent Testing Agency')
    manufacturer = forms.CharField(required=True, label='FRP Manufacturer')


class MonitorFormS(forms.Form):
    ChoicesA = (('1', 'Product Standards'),
                ('2', 'Physical and Chemical Characteristics'),
                ('3', 'Technical Specifications'),
                ('4', 'Limitations'),
                ('5', 'Maintenance Instructions'),
                ('6', 'Cleaning and Safety Instructions'),
                ('7', 'General Recommendation'))
    A = forms.MultipleChoiceField(choices=ChoicesA, widget=forms.CheckboxSelectMultiple(), label='Product Data (Fiber Sheet, Resins, Top-Coat, etc.):')
    ChoicesB = (('1', 'FRP System used'),
                ('2', 'Product Names of each constituent materials'),
                ('3', 'Repair areas and location'),
                ('4', 'Detailing and layout of the FRP system'),
                ('5', 'Lap splicing details'),
                ('6', 'Installation Steps: Concrete Surface preparation'),
                ('7', 'Installation Steps: FRP System'),
                ('8', 'Installation Steps: Final protective top-coating (if any)'))
    B = forms.MultipleChoiceField(choices=ChoicesB, widget=forms.CheckboxSelectMultiple(), label='Shop Drawings:')
    ChoicesC = (('1', 'FRP System tensile requirements'),
                ('2', 'FRP systems mechanical properties'),
                ('3', 'Strength/unit width and stiffness/unit width'),
                ('4', 'Installation Procedure'),
                ('5', 'Test Reports (for each materials)'))
    C = forms.MultipleChoiceField(choices=ChoicesC, widget=forms.CheckboxSelectMultiple(), label='Engineering Calculations, Installations, and Test:')
    ChoicesD = (('1', 'Tracking & verifying the quality of all FRP constituent materials'),
                ('2', 'Inspection of all prepared surfaces prior to installation of the FRP'),
                ('3', 'Inspection of installation of FRP system and completed work'),
                ('4', 'Number of quality control test samples'),
                ('5', 'Procedures for repair of defective work'))
    D = forms.MultipleChoiceField(choices=ChoicesD, widget=forms.CheckboxSelectMultiple(), label='Quality Control Plan/Procedures:')
    ChoicesE = (('1', 'Years and similar experience'),
                ('2', 'Constituent materials have been tested together as a system'),
                ('3', 'Training program to train Contractors'),
                ('4', 'Employs a knowledgeable technical field representative'),
                ('5', 'or Letters of references from previous projects'))
    E = forms.MultipleChoiceField(choices=ChoicesE, widget=forms.CheckboxSelectMultiple(), label='Qualifications of FRP system manufacturer:')
    ChoicesF = (('1', 'Years and similar experience'),
                ('2', 'Employs a trained field representative'),
                ('3', 'Maintains a documented safety program'),
                ('4', 'Training Certificate or letter from the manufacturer'),
                ('5', 'or Letters of references from previous projects'))
    F = forms.MultipleChoiceField(choices=ChoicesF, widget=forms.CheckboxSelectMultiple(), label='Qualifications of Installation Contractor:')


class MonitorFormQ(forms.Form):
    ChoicesA = (('1', 'Years and similar experience'),
                ('2', 'Employs a knowledgeable field representative'))
    A = forms.MultipleChoiceField(choices=ChoicesA, widget=forms.CheckboxSelectMultiple(), label='Independent Testing Agency:')
    ChoicesB = (('1', 'Demonstrate typical installation methods'),
                ('2', 'Same as field and environmental conditions'),
                ('3', 'Adhesion strength by direct tension pull-off tests'))
    B = forms.MultipleChoiceField(choices=ChoicesB, widget=forms.CheckboxSelectMultiple(), label='Optional requirement for a mockup:')
    ChoicesC = (('1', 'Manufacturer’s original'),
                ('2', 'Factory-sealed'),
                ('3', 'Unopened containers'),
                ('4', 'Label intact identifying the manufacturer'),
                ('5', 'Brand name'),
                ('6', 'System component name & identification number'),
                ('7', 'Production date'))
    C = forms.MultipleChoiceField(choices=ChoicesC, widget=forms.CheckboxSelectMultiple(), label='Materials Delivery to Project site in:')
    ChoicesD = (('1', 'Manufacturer’s recommended temperature'),
                ('2', 'Off of the ground'),
                ('3', 'Under cover'),
                ('4', 'Dry location'),
                ('5', 'Protected from dust'),
                ('6', 'Protected from direct sunlight'),
                ('7', 'Protected from physical damage'),
                ('8', 'Protected from rain'),
                ('9', 'Protected from water'),
                ('10', 'Protected from freezing and excessive heat'),
                ('11', 'Protected from foreign matter or other detrimental conditions'))
    D = forms.MultipleChoiceField(choices=ChoicesD, widget=forms.CheckboxSelectMultiple(), label='Storage:')
    ChoicesE = (('1', 'Avoid separating fibers, folding, or wrinkling'),
                ('2', 'Stack cut fiber sheets on flat or on a roll as per manufacturer'),
                ('3', 'Safety hazards when handling the materials'),
                ('4', 'Monitor resins during and after mixing'),
                ('5', 'All stages of Work conform to the local government unit'),
                ('6', 'Material Datasheet are available and accessible to all personnel'),
                ('7', 'Ventilate the resin mixing area to the outside'))
    E = forms.MultipleChoiceField(choices=ChoicesE, widget=forms.CheckboxSelectMultiple(), label='Handling:')
    ChoicesF = (('1', 'Clean up the site of any hazardous materials on a daily basis'),
                ('2', 'Component that has exceeded its shelf life'),
                ('3', 'Component that has not been properly mixed or stored'),
                ('4', 'Component that has unused or excess material'))
    F = forms.MultipleChoiceField(choices=ChoicesF, widget=forms.CheckboxSelectMultiple(), label='Disposal:')
    ChoicesG = (('1', 'Minimum guaranteed properties for tensile strength'),
                ('2', 'Minimum guaranteed properties for elongation'),
                ('3', 'Average values for tensile stiffness'))
    G = forms.MultipleChoiceField(choices=ChoicesG, widget=forms.CheckboxSelectMultiple(), label='Mechanical Property Requirement, ASTM D7565:')
    ChoicesH = (('1', 'Minimum of 5 or more tests'),
                ('2', 'Exceeds 60°C or plus 15°C to manufacturers expected temp.'))
    H = forms.MultipleChoiceField(choices=ChoicesH, widget=forms.CheckboxSelectMultiple(), label='Physical Property Requirement Glass Transition Temp., ASTM E1640:')
    ChoicesI = (('1', 'Water at 3000 hrs, ASTM D2247, E104'),
                ('2', 'Saltwater at 3000 hrs, ASTM D1141, C581'),
                ('3', 'Alkali at 3000 hrs, ASTM C581'),
                ('4', 'Dry Heat at 3000 hrs, ASTM D3045'),
                ('5', 'Free-Thaw at 20 cycles, ICC-ES method'),
                ('6', 'Cyclic Exterior Exposure at 2000 hrs, ASTM G153'),
                ('7', 'Carbon FRP strengthening systems shall retain 85%'),
                ('8', 'E-glass FRP systems shall retain 50%, Aggressive condition'),
                ('9', 'E-glass FRP systems shall retain 65%, Normal condition'),
                ('10', 'Others, Smoke and Flame Spread Requirements, ASTM E84'))
    I = forms.MultipleChoiceField(choices=ChoicesI, widget=forms.CheckboxSelectMultiple(), label='Durability Requirements after exposure to the environments:')


class MonitorFormE(forms.Form):
    ChoicesA = (('1', 'Verify dimensions of concrete members to be strengthened'),
                ('2', 'Visually assess the members to be strengthened'),
                ('3', 'Report all areas exhibiting evidence of deterioration or distress'),
                ('4', 'Conduct exploratory and/or non-destructive tests of the concrete'),
                ('5', 'Provide necessary pathways, scaffoldings and other means of access'),
                ('6', 'Make a record drawing, sketch, or photo of all obstructions'),
                ('7', 'Remove, replace, and dispose of any obstructions'),
                ('8', 'Provide all necessary equipment in clean and operating condition'),
                ('9', 'All necessary equipment should be in sufficient quantities'))
    A = forms.MultipleChoiceField(choices=ChoicesA, widget=forms.CheckboxSelectMultiple(), label='Examination:')
    ChoicesB = (('1', 'Make all substrate concrete repairs as per specifications'),
                ('2', 'Confirm the appropriate degree of curing and drying of repairs'),
                ('3', 'Do not apply FRP systems to concrete with corroded reinforcement'),
                ('4', 'Do not apply FRP systems to concrete with alkali aggregate reaction'),
                ('5', 'Inject epoxy resin to all cracks wider than 0.25 mm'))
    B = forms.MultipleChoiceField(choices=ChoicesB, widget=forms.CheckboxSelectMultiple(), label='Substrate Repair:')
    ChoicesC = (('1', 'Secure approval from the Engineer, Independent Testing Agency'),
                ('2', 'Make all necessary substrate and crack repairs'),
                ('3', 'Remove out-of-plane variation that exceed 0.8 mm or as per Mfr.'),
                ('4', 'Surface profile not less than concrete surface profile (CSP) 3 or as per Mfr.'),
                ('5', 'Round all outside corners and sharp edges, min. radius = 13 mm'),
                ('6', 'Construct a circular fillet, min. radius = 13 mm, or as per Mfr.'),
                ('7', 'Clean concrete surfaces as per Mfr.'))
    C = forms.MultipleChoiceField(choices=ChoicesC, widget=forms.CheckboxSelectMultiple(), label='Surface Preparation:')
    ChoicesD = (('1', 'Document the temperature & weather conditions (before & during)'),
                ('2', 'Comply contracts and recommendation OF manufacturer'),
                ('3', 'Do not apply to frozen or wet surfaces'),
                ('4', 'Do not apply if rain, snow, or dew point condensation is expected'),
                ('5', 'Ensure ambient and concrete surface temperatures as per Mfr.'),
                ('6', 'If heat sources necessary, do not use kerosene heaters'),
                ('7', 'Ensure moisture levels on concrete substrate as per Mfr.'),
                ('8', 'Ensure moisture vapor transmission rates as per Mfr.'),
                ('9', 'Do not install when moisture vapor transmission comes from the concrete substrate'),
                ('10', 'Commencement will constitute acceptance of substrate conditions'))
    D = forms.MultipleChoiceField(choices=ChoicesD, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Environmental Conditions:')
    ChoicesE = (('1', 'Mix all resin constituent materials as per Mfr.'),
                ('2', 'Mix ratio as per Mfr.'),
                ('3', 'Temperature range as per Mfr.'),
                ('4', 'Paddle type as per Mfr.'),
                ('5', 'Mix duration as per Mfr.'),
                ('6', 'Do not dilute any resin constituent materials with any organic solvents or thinners'),
                ('7', 'Discard any mixed resin that exceeds its pot life or shows signs of increased viscosity'))
    E = forms.MultipleChoiceField(choices=ChoicesE, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Mixing of Resin Constituent Materials:')
    ChoicesF = (('1', 'Coat the concrete surface if required'),
                ('2', 'Primer should penetrates the pores of the concrete substrate but does not drip or run'),
                ('3', 'Fill any bug holes or small voids and level any uneven surfaces with the putty resin'),
                ('4', 'Do not apply the putty until the primer is tack-free, unless approved by the Mfr.'),
                ('5', 'Fillers or other thickening agents may be added to the putty as per Mfr.'),
                ('6', 'Do not apply putty to a previously cured primer or putty coat, unless as per Mfr.'))
    F = forms.MultipleChoiceField(choices=ChoicesF, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Application of Primer and Putty:')
    ChoicesG = (('1', 'Impregnate fiber sheets with saturating resin as per Mfr.'),
                ('2', 'Apply saturating resin using a medium nap roller or mechanical saturator'),
                ('3', 'Do not apply saturating resin or impregnated fiber sheet to a cured resin coat, unless as per Mfr.'),
                ('4', 'Place fiber sheet onto substrate'),
                ('5', 'Roll fiber sheets in the direction of the fibers using a fin roller'),
                ('6', 'Achieve full contact with the concrete substrate during rolling'),
                ('7', 'Do not roll unidirectional fiber sheets in the direction transverse to the fibers'))
    G = forms.MultipleChoiceField(choices=ChoicesG, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Impregnating with Saturating Resin and Applying Fiber Sheet:')
    ChoicesH = (('1', 'Install FRP sheets with the fibers aligned in the direction indicated on the drawings'),
                ('2', 'Deviation in the alignment of the fibers of more than 5° (90 mm/m) for acceptance/rejection of Engineers'))
    H = forms.MultipleChoiceField(choices=ChoicesH, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Alignment of FRP Materials:')
    ChoicesI = (('1', 'Installation as per Mfr. such as orientation of the fibers, ply stacking sequence, and length'),
                ('2', 'Limit the number of plies applied in a single day without sloughing or sliding'),
                ('3', 'Maximum number of plies that can be applied in a single day should be as per Mfr.'),
                ('4', 'Do not apply additional fiber sheet plies to previously cured plies unless as per Mfr.'),
                ('5', 'Apply an additional coat of saturating resin, if required by the Mfr.'))
    I = forms.MultipleChoiceField(choices=ChoicesI, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Multiple Fiber Sheet Plies:')
    ChoicesJ = (('1', 'Provide lap splices equal to or exceeding the length as per Mfr.'),
                ('2', 'Install lap splices in acceptable regions (low moment or low shear)'),
                ('3', 'Stagger lap splices for multiple plies or side-by-side installations'),
                ('4', 'Document the location of lap splices on an as-built drawing'))
    J = forms.MultipleChoiceField(choices=ChoicesJ, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Lap Splicing of Fiber Plies:')
    ChoicesK = (('1', 'Secure approval of the FRP anchoring system prior to the start of construction'),
                ('2', 'Install FRP anchoring system in accordance with drawings and as per Mfr.'))
    K = forms.MultipleChoiceField(choices=ChoicesK, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Anchoring of FRP Sheets:')
    ChoicesL = (('1', 'Do not allow bare metal to come into direct contact with the carbon FRP system'),
                ('2', 'Protect metal hardware by providing an insulating barrier of additional resin or E-glass FRP'),
                ('3', 'Secure approval from the Engineer for all penetrations of FRP sheets'))
    L = forms.MultipleChoiceField(choices=ChoicesL, widget=forms.CheckboxSelectMultiple(), label='Installation of FRP System - Metal Contact with Carbon FRP Systems:')
    ChoicesM = (('1', 'Date and time of installation'),
                ('2', 'Environmental conditions including general weather'),
                ('3', 'Ambient and surface temperatures'),
                ('4', 'Relative humidity'),
                ('5', 'If applicable, the type of auxiliary heat source used'),
                ('6', 'Fiber lot numbers used that day (members strengthened & any inspections performed)'),
                ('7', 'Type and location of defects found'),
                ('8', 'How the defects were dealt with'),
                ('9', 'Results of adhesion tests'),
                ('10', 'Any repairs made to the FRP system'))
    M = forms.MultipleChoiceField(choices=ChoicesM, widget=forms.CheckboxSelectMultiple(), label='Prepare daily reports documenting the following:')
    ChoicesN = (('1', 'Make witness panels from the same fiber, saturating resins, equipment, and methods'),
                ('2', 'Make panels with 1 or 2 plies & large enough to extract a min. of 10 tensile test coupons'),
                ('3', 'Fabricate a panel for every 500 sq.m. of material installed or as per contracts'),
                ('4', 'Store witness panels in a dry location on site and allow the panels to cure under the same conditions'),
                ('5', 'Send panels to a third party FRP materials tensile testing laboratory & test 5 samples as per ASTM D7565'),
                ('6', 'Average tensile strength should exceeds required strength, unless test remaining 5 samples'),
                ('7', 'Average tensile strength of combined test should exceeds required strength'))
    N = forms.MultipleChoiceField(choices=ChoicesN, widget=forms.CheckboxSelectMultiple(), label='FRP System Tensile Testing:')
    ChoicesO = (('1', 'No bubbles'),
                ('2', 'No air pockets'),
                ('3', 'No voids'),
                ('4', 'No areas of debonding'),
                ('5', 'No dead sounds when lightly tapped w/ hammer'),
                ('6', 'Small delaminations should be less than 1290 sq.mm for less than 5% of the total laminate area'),
                ('7', 'No more than 10 such delaminations per 1 sq.m.'),
                ('8', 'Repair or removed of rejected areas'))
    O = forms.MultipleChoiceField(choices=ChoicesO, widget=forms.CheckboxSelectMultiple(), label='Inspection for Delaminations, after of min. 24 hours of FRP System initially cured:')
    ChoicesP = (('1', 'Obtain resin-cup samples for each batch of mixed resin used'),
                ('2', 'Cure resin-cup samples at the temperature as the installed FRP system'),
                ('3', 'Verify the relative cure by regularly examining the resin-cup samples'),
                ('4', 'For questionable samples, consult with the manufacturer for acceptance criteria'),
                ('5', 'Remove and repair all areas where the resin is found to have not properly cured'))
    P = forms.MultipleChoiceField(choices=ChoicesP, widget=forms.CheckboxSelectMultiple(), label='Inspection for Relative Cure of Resin:')
    ChoicesQ = (('1', 'Conduct adhesion testing (3 tests per day or 1 test per 93 sq.m of substrate contact)'),
                ('2', 'Pull-off strength shall exceed 1.4 MPa & failure shall occur in the concrete substrate'),
                ('3', 'Failures occurring between plies or between the concrete substrate and the FRP system, subject for evaluation'),
                ('4', 'If 1 or 2 of the pull-off tests is found unacceptable, perform 2 additional tests adjacent to it'),
                ('5', 'If one of the additional pull-off tests is found unacceptable, the Work shall be rejected'))
    Q = forms.MultipleChoiceField(choices=ChoicesQ, widget=forms.CheckboxSelectMultiple(), label='Inspection for Adhesion to Substrate, direct tension pull-off tests, ASTM D7522:')
    ChoicesR = (('1', 'Submit all proposed repair procedures to the FRP system to the Engineer for approval'),
                ('2', 'Repair all unacceptable defects found in the cured FRP system as per Mfr.'),
                ('3', 'All repairs shall be subject to the same application, curing, and quality control'),
                ('4', 'Apply an overlapping FRP sheet patch of equivalent plies for delaminations as per Mfr.'),
                ('5', 'If any delamination growth is suspected between the FRP plies due to injection, it shall be halted'),
                ('6', 'For larger defects, extend the additional FRP layers a min. of 153 mm on all sides of the defect repair or as per Mfr.'),
                ('7', 'Do not apply additional fiber sheet plies to previously cured plies unless as per Mfr.'))
    R = forms.MultipleChoiceField(choices=ChoicesR, widget=forms.CheckboxSelectMultiple(), label='Repair of Defective Work and QC Test Sites:')
    ChoicesS = (('1', 'Remove excess epoxy resin prior to curing of the FRP strengthening'),
                ('2', 'Do not use solvents to remove or clean already cured epoxy resin'))
    S = forms.MultipleChoiceField(choices=ChoicesS, widget=forms.CheckboxSelectMultiple(), label='Cleaning:')


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class InstallForm(forms.Form):
    Resins_Storage_Date = forms.DateField(widget=DateInput)
    Rshell_life = forms.IntegerField(required=True, label='Resins shelf life as per manufacturer, months')
    Rstorage_temp_min = forms.FloatField(required=True, label='Resins - storage min temperature requirements as per manufacturer, °C')
    Rstorage_temp_max = forms.FloatField(required=True, label='Resins - storage max temperature requirements as per manufacturer, °C')
    Rstorage_temp_act = forms.FloatField(required=True, label='Resins - storage actual temperature, °C')
    Fabrics_Storage_Date = forms.DateField(widget=DateInput)
    Fshell_life = forms.IntegerField(required=True, label='Fabrics shelf life as per manufacturer, months')
    Fstorage_temp_min = forms.FloatField(required=True, label='Fabrics - storage min temperature requirements as per manufacturer, °C')
    Fstorage_temp_max = forms.FloatField(required=True, label='Fabrics - storage max temperature requirements as per manufacturer, °C')
    Fstorage_temp_act = forms.FloatField(required=True, label='Fabrics - storage actual temperature, °C')
    Rpot_life = forms.IntegerField(required=True, label='Resins pot life as per manufacturer, minutes')
    Ambient_temp_min = forms.FloatField(required=True, label='Min Ambient Air temperature requirements as per manufacturer, °C')
    Ambient_temp_max = forms.FloatField(required=True, label='Max Ambient Air temperature requirements as per manufacturer, °C')
    Ambient_temp_act = forms.FloatField(required=True, label='Actual Ambient Air temperature, °C')
    Substrate_temp_min = forms.FloatField(required=True, label='Min Substrate temperature requirements as per manufacturer, °C')
    Substrate_temp_max = forms.FloatField(required=True, label='Max Substrate temperature requirements as per manufacturer, °C')
    Substrate_temp_act = forms.FloatField(required=True, label='Actual Substrate temperature, °C')
    Substrate_moist_max = forms.FloatField(required=True, label='Max Substrate moisture content requirements as per manufacturer, %')
    Substrate_moist_act = forms.FloatField(required=True, label='Actual Substrate moisture content, %')
    FRP_curing_time = forms.IntegerField(required=True, label='Waiting time as per manufacturer before application of next layer incase pot life lapsed, hours')


