ques = "HOW MANY PARTİCLES ARE YOU MADE OF ?"  ##add What is your mass quetion!
import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
import random

ques_ = [
    "How many smaller particles are you made of?",  ##"ParticleNumber"
    "Do you take up space or pile on?",  ##"Space"
    "Are your particles strongly-interacting?",  ##"StrongInteraction"
    "How many quarks are we talking?",  ##"QuarkAmount"
    "Are you found in atomic nuclei?",  ##"AtomicNuclei"
    "What is your electric charge?",  ##"ElectricityCharge"
    "Is your field nonzero even in empty space?",  ##"Field"
    "What force do you carry?",  ##"ForceCarry"
    "Do you feel the strong force?"
]  ##"StrongForce"
finish1 = """You might be an
ATOM
or a molecule or whatever.
Too complicated for particle physics!

"""
finish2 = """I guess you are
POSITRONIUM
or somethink?
Weirdo!
"""
finish3 = """you are a
HIGGS BOSON
You mysterious
recluse,you
"""
finish4 = """You are an
UP-TYPE QUARK
UP-CHARM-TOP
"""

  ##quark tipleri
finish4_1 = """
You are a
DOWN-TYPE QUARK!
DOWN-STRANGE-BOTTOM
"""
finish4_2 = """
You are a
CHARGED LEPTON!
ELECTRON-MUON-TAU
"""
finish4_3 = """
You are a
NEUTRIONO!
ELECTRON NEUTRIONO-MUON NEUTRIONO-TAU 
"""
finish5 = """You are a
FERMION
A particle of mater.
"""
finish6 = """You are a
HADRON
A colerless collection
of quarks and gluons
"""
finish7_1 = """You are a
GLUEBALL
You are hypothetical at best
"""
finish7_2 = """Probably a
NUCLEUS
Although you could
be a pentaquark(or worse)

"""
finish7_3 = """you are a
BARYON
kind of fermion
"""
finish8 = """You are some excited
or strange or heavier
baryon.Enjoy your
brief lifetime!
"""
finish9 = """You are
NUCLEON!
You are kind of
a big deal.
"""
finish9_1 = """You are a
NEUTRON!
Not bad!
"""
finish9_2 = """You are a
PROTON!
Go you
"""
finish17 = """
You are a
MESON!
Which is a kind
of boson.
"""
finish10 = """You are a
BOSON!
A force-carrying particle.
"""
finish11 = """You are a
GUAGE BOSON!
You reflect a symetry
of Nature.
"""
finish12_1 = """You are a
GRAVITON!
And you exist.
Ignore the haters.
"""
finish12_2 = """You are a
GLUON!
In one of eight
colurful hues.
"""
finish12_3 = """You are a
PHOTON!
From radio to
gamma rays.
"""
finish13_1 = """You are a
W BOSON!
When fermions change
flavor,it's your fault!"
"""
finish13_2="""You are a
Z BOSON!
Neutral currents
for the win!     
"""     ##çatal
finish14 = """You are
QUARK!
You are stuck inside
some hadron.
"""
finish15 = """You are a
LEPTON!
Light,but powerful!
"""
finish9_0 = """Yeah I'm not going
to list all the mesons
Pions,Kaons,
Etas,Rhos,etc.
"""


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("WHICH PARTICLE ARE YOU...")

        self.title_font = tkfont.Font(family='Helvetica',
                                      size=18,
                                      weight="bold",
                                      slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ParticleNumber, Space, StrongInteraction,
                  QuarkAmount, AtomicNuclei, ElectricityCharge, Field,
                  ForceCarry, StrongForce, WeakForce, ElctCharge,
                  FinishParticleAmount, FinishStrongInteraction, FinishField,
                  FinishElectCharge1, FinishAtomicNuclei, MeanStrong,
                  MeanStrongInteraction, FinishElectQuark1, FinishElectQuark2,
                  MeanQuarkAmount, MeanAtomicNuclei, FinishElectricityCharge1,
                  FinishElectricityCharge2, FinishQuarkAmount0, MeanSpace,
                  MeanSpace2, MeanSpace2, FinishBoson1, FinishBoson2,
                  FinishBoson3, WeakForce1, WeakForce2, FinishElectCharge1,
                  FinishElectCharge2, FinishElectCharge3, FinishElectCharge4,
                  MeanStrongForce1, MeanStrongForce2, Meanabc):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,
                         text="Which particle are you?",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(
            self,
            text="START",
            command=lambda: controller.show_frame("ParticleNumber"))
        button1.pack()


class Question(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=120, width=300)
        self.ques_Frame.pack()
        self.ans_Frame = tk.Frame(self, height=240, width=300)
        self.ans_Frame.pack(fill=tk.X)

    @classmethod
    def random_color(cls):
        colors = [
            'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
            'old lace', 'linen', 'antique white', 'papaya whip',
            'blanched almond', 'bisque', 'peach puff', 'navajo white',
            'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
            'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
            'slate gray', 'light slate gray', 'gray', 'light grey',
            'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
            'slate blue', 'medium slate blue', 'light slate blue',
            'medium blue', 'royal blue', 'blue', 'dodger blue',
            'deep sky blue', 'sky blue', 'light sky blue', 'steel blue',
            'light steel blue', 'light blue', 'powder blue', 'pale turquoise',
            'dark turquoise', 'medium turquoise', 'turquoise', 'cyan',
            'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine',
            'dark green', 'dark olive green', 'dark sea green', 'sea green',
            'medium sea green', 'light sea green', 'pale green',
            'spring green', 'lawn green', 'medium spring green',
            'green yellow', 'lime green', 'yellow green', 'forest green',
            'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
            'light goldenrod yellow', 'light yellow', 'yellow', 'gold',
            'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
            'indian red', 'saddle brown', 'sandy brown', 'dark salmon',
            'salmon', 'light salmon', 'orange', 'dark orange', 'coral',
            'light coral', 'tomato', 'orange red', 'red', 'hot pink',
            'deep pink', 'pink', 'light pink', 'pale violet red', 'maroon',
            'medium violet red', 'violet red', 'medium orchid', 'dark orchid',
            'dark violet', 'blue violet', 'purple', 'medium purple', 'thistle',
            'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4',
            'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4',
            'bisque2', 'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3',
            'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
            'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2',
            'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4',
            'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2',
            'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
            'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1',
            'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'RoyalBlue1',
            'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
            'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1',
            'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2',
            'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3',
            'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3',
            'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
            'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2',
            'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2',
            'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3',
            'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3',
            'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
            'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3',
            'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1',
            'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
            'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2',
            'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2',
            'SeaGreen3', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3',
            'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
            'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3',
            'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4',
            'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3',
            'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
            'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3',
            'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4',
            'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4',
            'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
            'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3',
            'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3',
            'RosyBrown4', 'IndianRed1', 'IndianRed2', 'IndianRed3',
            'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4',
            'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'wheat1',
            'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1',
            'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
            'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4',
            'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2',
            'LightSalmon3', 'LightSalmon4', 'orange2', 'orange3', 'orange4',
            'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
            'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3',
            'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2',
            'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1',
            'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3',
            'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4',
            'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3',
            'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4',
            'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'magenta2',
            'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4',
            'plum1', 'plum2', 'plum3', 'plum4', 'MediumOrchid1',
            'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1',
            'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2',
            'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
            'MediumPurple3', 'MediumPurple4'
        ]

        return random.choice(colors)


##        label = tk.Label(self, text=ques_[0], font=controller.title_font)
##
##        label.pack(side="top", fill="x", pady=10)
##        button = tk.Button(self, text="Go to the start page",
##                           command=lambda: controller.show_frame("StartPage"))
##        button.pack()
class ParticleNumber(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[0],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(self.ans_Frame,
                            text="ONE",
                            bg=Question.random_color(),
                            command=lambda: controller.show_frame("Space"))
        button2 = tk.Button(
            self.ans_Frame,
            text="JUST A FEW",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("StrongInteraction"))
        button3 = tk.Button(
            self.ans_Frame,
            text="MANY",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishParticleAmount"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)
        button3.pack(side="left", fill=tk.X, expand=1)


class Space(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[1],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(self.ans_Frame,
                            text="PILE ON",
                            bg=Question.random_color(),
                            command=lambda: controller.show_frame("MeanSpace"))
        button2 = tk.Button(
            self.ans_Frame,
            text="TAKE UP SPACE",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("MeanStrong"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)


class StrongInteraction(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[2],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="YES",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("MeanStrongInteraction"))
        button2 = tk.Button(
            self.ans_Frame,
            text="NO",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishStrongInteraction"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)


class QuarkAmount(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[3],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="ZERO",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectQuark1"))
        button2 = tk.Button(
            self.ans_Frame,
            text="MORE THAN THREE",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectQuark2"))
        button3 = tk.Button(
            self.ans_Frame,
            text="THREE",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("MeanQuarkAmount"))
        button4 = tk.Button(self.ans_Frame,
                            text="ONE QUARK and ONE ANTI-QUARK",
                            bg=Question.random_color(),
                            command=lambda: controller.show_frame("Meanabc"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)
        button3.pack(side="left", fill=tk.X, expand=1)
        button4.pack(side="left", fill=tk.X, expand=1)


class AtomicNuclei(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[4],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="YES",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("MeanAtomicNuclei"))
        button2 = tk.Button(
            self.ans_Frame,
            text="NO",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishAtomicNuclei"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)


class ElectricityCharge(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[5],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="+1",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectricityCharge2"))
        button2 = tk.Button(
            self.ans_Frame,
            text="0",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectricityCharge1"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)


class Field(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[6],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="YES",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishField"))
        button2 = tk.Button(
            self.ans_Frame,
            text="NO",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("MeanSpace2"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)


class ForceCarry(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[7],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="GRAVİTY",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishBoson1"))
        button2 = tk.Button(
            self.ans_Frame,
            text="STRONG",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishBoson2"))
        button3 = tk.Button(
            self.ans_Frame,
            text="ELECTROMAGNETİK",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishBoson3"))
        button4 = tk.Button(self.ans_Frame,
                            text="WEAK",
                            bg=Question.random_color(),
                            command=lambda: controller.show_frame("WeakForce"))

        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)
        button3.pack(side="left", fill=tk.X, expand=1)
        button4.pack(side="left", fill=tk.X, expand=1)


class WeakForce(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[8],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="YES",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("WeakForce1"))
        button2 = tk.Button(
            self.ans_Frame,
            text="NO",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("WeakForce2"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)


class StrongForce(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[8],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="YES",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("MeanStrongForce1"))
        button2 = tk.Button(
            self.ans_Frame,
            text="NO",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("MeanStrongForce2"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)


class ElctCharge(Question):
    def __init__(self, parent, controller):
        Question.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self.ques_Frame,
                         text=ques_[5],
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")
        button1 = tk.Button(
            self.ans_Frame,
            text="+2/3",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectCharge1"))
        button2 = tk.Button(
            self.ans_Frame,
            text="-1/3",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectCharge2"))
        button3 = tk.Button(
            self.ans_Frame,
            text="-1",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectCharge3"))
        button4 = tk.Button(
            self.ans_Frame,
            text="0",
            bg=Question.random_color(),
            command=lambda: controller.show_frame("FinishElectCharge4"))
        button1.pack(side="left", fill=tk.X, expand=1)
        button2.pack(side="left", fill=tk.X, expand=1)
        button3.pack(side="left", fill=tk.X, expand=1)
        button4.pack(side="left", fill=tk.X, expand=1)


class FinishParticleAmount(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish1, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishStrongInteraction(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish2, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishField(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish3, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectCharge1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish4, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectCharge2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish4_1,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectCharge3(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish4_2,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectCharge4(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish4_3,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectQuark1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish7_1,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectQuark2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish7_2,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishAtomicNuclei(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish8, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectricityCharge1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish9_1,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishElectricityCharge2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish9_2,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class MeanStrong(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish5, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("StrongForce"))
        button1.pack()


class MeanStrongInteraction(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish6, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("QuarkAmount"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class MeanQuarkAmount(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish7_3,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("AtomicNuclei"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class MeanAtomicNuclei(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame, text=finish9, font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("ElectricityCharge"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishQuarkAmount0(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish9_0,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class MeanSpace(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish10,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(self,
                            text="CONTINUE",
                            command=lambda: controller.show_frame("Field"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class MeanSpace2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish11,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("ForceCarry"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishBoson1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish12_1,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishBoson2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish12_2,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class FinishBoson3(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish12_3,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class WeakForce1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish13_1,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class WeakForce2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish13_2,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))


class MeanStrongForce1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish14,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("ElctCharge"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class MeanStrongForce2(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish15,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("ElctCharge"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


class Meanabc(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=360, width=300)
        self.ques_Frame = tk.Frame(self, height=360, width=300)
        label = tk.Label(self.ques_Frame,
                         text=finish17,
                         font=("Helvetica", 26))
        label.pack(side="top", fill="x", pady=10)
        self.ques_Frame.pack()
        button1 = tk.Button(
            self,
            text="CONTINUE",
            command=lambda: controller.show_frame("FinishQuarkAmount0"))
        button1.pack()
        exit_ = tk.Button(self,
                          text="Restart",
                          command=lambda: controller.show_frame("StartPage"))
        exit_.pack(side="bottom")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
