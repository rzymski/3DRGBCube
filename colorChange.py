from tkinter import *
import tkinter.font as font
from first_version import slowest_version
from secondVersion import minimalizedVersion
from thirdVersion import facesVersion
class ColorChange:
    def __init__(self, root):
        self.root = root
        self.root.title("Color change Piotr Szumowski")
        bigFont = font.Font(size=30, weight="bold")

        self.convertRGBButton = Button(self.root, text="Convert RGB to CMYK", command=self.convertRGB, padx=50, pady=20)
        self.convertRGBButton.grid(row=0, column=0, rowspan=1, sticky="WE")
        self.convertRGBButton['font'] = bigFont

        self.convertCMYKButton = Button(self.root, text="Convert CMYK to RGB", command=self.convertCMYK, padx=20, pady=20)
        self.convertCMYKButton.grid(row=1, column=0, rowspan=1, sticky="WE")
        self.convertCMYKButton['font'] = bigFont

        self.renderCubeButton = Button(self.root, text="Render 3D RGB Cube", command=self.renderCube, padx=20, pady=20)
        self.renderCubeButton.grid(row=2, column=0, rowspan=1, sticky="WE")
        self.renderCubeButton['font'] = bigFont


    def convertRGB(self):
        convertRGB = Toplevel()
        labelRGB = Label(convertRGB, padx=10, pady=10)
        labelRGB.pack(side="top", fill="both")
        #entry validation
        vcmd = (labelRGB.register(self.validateEntryRGB))
        #red
        self.redLabel = Label(labelRGB, text="Red")
        self.redLabel.grid(row=0, column=0)
        self.svRed = StringVar()
        self.redEntry = Entry(labelRGB, validate='all', validatecommand=(vcmd, '%P'), textvariable=self.svRed)
        self.redEntry.grid(row=0, column=1)
        self.redEntry.insert(0, "0")
        self.redSlider = Scale(labelRGB, from_=0, to=255, orient=HORIZONTAL, variable=self.svRed)
        self.redSlider.grid(row=1, column=0, columnspan=4, sticky="nsew")
        # green
        self.greenLabel = Label(labelRGB, text="Green")
        self.greenLabel.grid(row=2, column=0)
        self.svGreen = StringVar()
        self.greenEntry = Entry(labelRGB, validate='all', validatecommand=(vcmd, '%P'), textvariable=self.svGreen)
        self.greenEntry.grid(row=2, column=1)
        self.greenEntry.insert(0, "0")
        self.greenSlider = Scale(labelRGB, from_=0, to=255, orient=HORIZONTAL, variable=self.svGreen)
        self.greenSlider.grid(row=3, column=0, columnspan=4, sticky="nsew")
        #blue
        self.blueLabel = Label(labelRGB, text="Blue")
        self.blueLabel.grid(row=4, column=0)
        self.svBlue = StringVar()
        self.blueEntry = Entry(labelRGB, validate='all', validatecommand=(vcmd, '%P'), textvariable=self.svBlue)
        self.blueEntry.grid(row=4, column=1)
        self.blueEntry.insert(0, "0")
        self.blueSlider = Scale(labelRGB, from_=0, to=255, orient=HORIZONTAL, variable=self.svBlue)
        self.blueSlider.grid(row=5, column=0, columnspan=4, sticky="nsew")
        #6 color
        self.colorRGBLabel = Label(labelRGB, background="#000000")
        self.colorRGBLabel.grid(row=6, column=0, columnspan=4, sticky="nsew")
        #7 name of color
        self.cyanLabel = Label(labelRGB, text="CYAN")
        self.cyanLabel.grid(row=7, column=0)
        self.magentaLabel = Label(labelRGB, text="Magenta")
        self.magentaLabel.grid(row=7, column=1)
        self.yellowLabel = Label(labelRGB, text="Yellow")
        self.yellowLabel.grid(row=7, column=2)
        self.blackLabel = Label(labelRGB, text="BLACK")
        self.blackLabel.grid(row=7, column=3)
        #8 params
        self.cyan = Entry(labelRGB, state=DISABLED)
        self.cyan.grid(row=8, column=0)
        self.magenta = Entry(labelRGB, state=DISABLED)
        self.magenta.grid(row=8, column=1)
        self.yellow = Entry(labelRGB, state=DISABLED)
        self.yellow.grid(row=8, column=2)
        self.black = Entry(labelRGB, state=DISABLED)
        self.black.grid(row=8, column=3)
        # Początkowe ustawienia
        self.entryChangedRGB('e')
        # Śledzenie zmian w Entry
        self.svRed.trace("w", lambda name, index, mode, sv=self.svRed: self.entryChangedRGB(''))
        self.svGreen.trace("w", lambda name, index, mode, sv=self.svGreen: self.entryChangedRGB(''))
        self.svBlue.trace("w", lambda name, index, mode, sv=self.svBlue: self.entryChangedRGB(''))

    def validateEntryRGB(self, P):
        if P == "" or (str.isdigit(P) and 0 <= int(P) <= 255):
            return True
        else:
            return False

    def entryChangedRGB(self, event):
        if self.redEntry.get() == "" or self.greenEntry.get() == "" or self.blueEntry.get() == "":
            return
        # Get the values from the entry fields
        red = int(self.svRed.get())
        green = int(self.svGreen.get())
        blue = int(self.svBlue.get())
        # Call the conversion function
        cmyk_values = self.conversionRGBtoCMYK(red, green, blue)
        # Update the CMYK entry fields
        self.cyan.config(state=NORMAL)
        self.magenta.config(state=NORMAL)
        self.yellow.config(state=NORMAL)
        self.black.config(state=NORMAL)
        self.cyan.delete(0, END)
        self.magenta.delete(0, END)
        self.yellow.delete(0, END)
        self.black.delete(0, END)
        self.cyan.insert(0, f"{cmyk_values[0]}")
        self.magenta.insert(0, f"{cmyk_values[1]}")
        self.yellow.insert(0, f"{cmyk_values[2]}")
        self.black.insert(0, f"{cmyk_values[3]}")
        self.cyan.config(state=DISABLED)
        self.magenta.config(state=DISABLED)
        self.yellow.config(state=DISABLED)
        self.black.config(state=DISABLED)
        #
        hex_red = format(red, '02x')
        hex_green = format(green, '02x')
        hex_blue = format(blue, '02x')
        self.colorRGBLabel.config(background=f"#{hex_red}{hex_green}{hex_blue}")

    def conversionRGBtoCMYK(self, red, green, blue):
        if 255 < red < 0 or 255 < green < 0 or 255 < blue < 0:
            raise Exception("Zła wartość. Wartości muszą być z zakresu od 0 do 255 dla RGB.")
        red /= 255
        green /= 255
        blue /= 255
        black = min(1-red, 1-green, 1-blue)
        cyan = int(100 * (1-red-black)/(1-black)) if black != 1 else "Nie istnieje"
        magenta = int(100 * (1-green-black)/(1-black)) if black != 1 else "Nie istnieje"
        yellow = int(100 * (1-blue-black)/(1-black)) if black != 1 else "Nie istnieje"
        # print(f"red={red} green={green} blue={blue} cyan={cyan} magenta={magenta} yellow={yellow} black={black}")
        black = round(black * 100, 2)
        return cyan, magenta, yellow, black

    def convertCMYK(self):
        convertCMYK = Toplevel()
        labelCMYK = Label(convertCMYK, padx=10, pady=10)
        labelCMYK.pack(side="top", fill="both")
        # entry validation
        vcmd = (labelCMYK.register(self.validateEntryCMYK))
        # cyan
        self.cyanLabel = Label(labelCMYK, text="Cyan")
        self.cyanLabel.grid(row=0, column=0)
        self.svCyan = StringVar()
        self.cyanEntry = Entry(labelCMYK, validate='all', validatecommand=(vcmd, '%P'), textvariable=self.svCyan)
        self.cyanEntry.grid(row=0, column=1)
        self.cyanEntry.insert(0, "0")
        self.cyanSlider = Scale(labelCMYK, from_=0, to=100, orient=HORIZONTAL, variable=self.svCyan)
        self.cyanSlider.grid(row=1, column=0, columnspan=4, sticky="nsew")
        # magenta
        self.magentaLabel = Label(labelCMYK, text="Magenta")
        self.magentaLabel.grid(row=2, column=0)
        self.svMagenta = StringVar()
        self.magentaEntry = Entry(labelCMYK, validate='all', validatecommand=(vcmd, '%P'), textvariable=self.svMagenta)
        self.magentaEntry.grid(row=2, column=1)
        self.magentaEntry.insert(0, "0")
        self.magentaSlider = Scale(labelCMYK, from_=0, to=100, orient=HORIZONTAL, variable=self.svMagenta)
        self.magentaSlider.grid(row=3, column=0, columnspan=4, sticky="nsew")
        # yellow
        self.yellowLabel = Label(labelCMYK, text="Yellow")
        self.yellowLabel.grid(row=4, column=0)
        self.svYellow = StringVar()
        self.yellowEntry = Entry(labelCMYK, validate='all', validatecommand=(vcmd, '%P'), textvariable=self.svYellow)
        self.yellowEntry.grid(row=4, column=1)
        self.yellowEntry.insert(0, "0")
        self.yellowSlider = Scale(labelCMYK, from_=0, to=100, orient=HORIZONTAL, variable=self.svYellow)
        self.yellowSlider.grid(row=5, column=0, columnspan=4, sticky="nsew")
        # black
        self.blackLabel = Label(labelCMYK, text="Black")
        self.blackLabel.grid(row=6, column=0)
        self.svBlack = StringVar()
        self.blackEntry = Entry(labelCMYK, validate='all', validatecommand=(vcmd, '%P'), textvariable=self.svBlack)
        self.blackEntry.grid(row=6, column=1)
        self.blackEntry.insert(0, "0")
        self.blackSlider = Scale(labelCMYK, from_=0, to=100, orient=HORIZONTAL, variable=self.svBlack)
        self.blackSlider.grid(row=7, column=0, columnspan=4, sticky="nsew")
        # 6 color
        self.colorCMYKLabel = Label(labelCMYK, background="#000000")
        self.colorCMYKLabel.grid(row=8, column=0, columnspan=4, sticky="nsew")
        # 7 name of color
        self.redLabel = Label(labelCMYK, text="RED")
        self.redLabel.grid(row=9, column=0)
        self.greenLabel = Label(labelCMYK, text="GREEN")
        self.greenLabel.grid(row=9, column=1)
        self.blueLabel = Label(labelCMYK, text="BLUE")
        self.blueLabel.grid(row=9, column=2)
        # 8 params
        self.red = Entry(labelCMYK, state=DISABLED)
        self.red.grid(row=10, column=0)
        self.green = Entry(labelCMYK, state=DISABLED)
        self.green.grid(row=10, column=1)
        self.blue = Entry(labelCMYK, state=DISABLED)
        self.blue.grid(row=10, column=2)
        # Początkowe ustawienia
        self.entryChangedCMYK('e')
        # Śledzenie zmian w Entry
        self.svCyan.trace("w", lambda name, index, mode, sv=self.svCyan: self.entryChangedCMYK(''))
        self.svMagenta.trace("w", lambda name, index, mode, sv=self.svMagenta: self.entryChangedCMYK(''))
        self.svYellow.trace("w", lambda name, index, mode, sv=self.svYellow: self.entryChangedCMYK(''))
        self.svBlack.trace("w", lambda name, index, mode, sv=self.svBlack: self.entryChangedCMYK(''))

    def validateEntryCMYK(self, P):
        if P == "" or (str.isdigit(P) and 0 <= int(P) <= 100):
            return True
        else:
            return False

    def entryChangedCMYK(self, event):
        if self.cyanEntry.get() == "" or self.magentaEntry.get() == "" or self.yellowEntry.get() == "" or self.blackEntry.get() == "":
            return
        # Get the values from the entry fields
        cyan = int(self.svCyan.get())
        magenta = int(self.svMagenta.get())
        yellow = int(self.svYellow.get())
        black = int(self.svBlack.get())
        # Call the conversion function
        rgb_values = self.conversionCMYKtoRGB(cyan, magenta, yellow, black)
        # Update the CMYK entry fields
        self.red.config(state=NORMAL)
        self.green.config(state=NORMAL)
        self.blue.config(state=NORMAL)
        self.red.delete(0, END)
        self.green.delete(0, END)
        self.blue.delete(0, END)
        self.red.insert(0, f"{rgb_values[0]}")
        self.green.insert(0, f"{rgb_values[1]}")
        self.blue.insert(0, f"{rgb_values[2]}")
        self.red.config(state=DISABLED)
        self.green.config(state=DISABLED)
        self.blue.config(state=DISABLED)
        # convert rgb to hex
        hex_red = format(int(rgb_values[0]), '02x')
        hex_green = format(int(rgb_values[1]), '02x')
        hex_blue = format(int(rgb_values[2]), '02x')
        self.colorCMYKLabel.config(background=f"#{hex_red}{hex_green}{hex_blue}")

    def conversionCMYKtoRGB(self, cyan, magenta, yellow, black):
        if 100 < cyan < 0 or 100 < magenta < 0 or 100 < yellow < 0 or 100 < black < 0:
            raise Exception("Zła wartość. Wartości muszą być z zakresu od 0 do 100 dla CMYK")
        cyan /= 100
        magenta /= 100
        yellow /= 100
        black /= 100
        red = round(255 * (1 - min(1, cyan*(1-black)+black)))
        green = round(255 * (1 - min(1, magenta*(1-black)+black)))
        blue = round(255 * (1 - min(1, yellow*(1-black)+black)))
        # print(f"red={red} green={green} blue={blue} cyan={cyan} magenta={magenta} yellow={yellow} black={black}")
        return red, green, blue

    def renderCube(self):
        # slowest_version() # najwolniejsza wersja ładuje sie ponad 30 sekund, a obracanie trwa wieki
        minimalizedVersion(dimension=32) # najszybsza wersja
        # facesVersion(dimension=32) #najładniejsza wersja i tez w miare szybka, ale troche wolniejsza niz minimalizedVersion
