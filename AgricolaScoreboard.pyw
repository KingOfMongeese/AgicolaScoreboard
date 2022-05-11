#KingOfMongeese
#importing the modules for the UI
import tkinter
import tkinter.messagebox
import platform

system = platform.system()

#Intialize the Window, I could set a size but I like the size it is at
window = tkinter.Tk()
window.title('Agricola Scoreboard')
if system == 'Windows':
    window.iconbitmap('agricola.ico')


#Initial Variables that will be pulled from the entry fields
player = tkinter.StringVar()
fields = tkinter.IntVar()
pastures = tkinter.IntVar()
grain = tkinter.IntVar()
veg = tkinter.IntVar()
sheep = tkinter.IntVar()
boars = tkinter.IntVar()
cattle = tkinter.IntVar()
spaces = tkinter.IntVar()
stables = tkinter.IntVar()
clay = tkinter.IntVar()
stone = tkinter.IntVar()
fam = tkinter.IntVar()
cards = tkinter.IntVar()
beg = tkinter.IntVar()

#The build of the UI
tkinter.Label(window, text = 'Player Name:', font = ('calibre', 12)).grid(row = 0)
player_entry = tkinter.Entry(window, textvariable = player, font = ('calibre', 12)).grid(row = 0, column = 1)

tkinter.Label(window, text ='Fields:', font = ('calibre', 12)).grid(row = 1)
fields_entry = tkinter.Entry(window, textvariable = fields, font = ('calibre', 12)).grid(row = 1, column = 1)

tkinter.Label(window, text = 'Pastures:', font = ('calibre', 12)).grid(row = 2)
pastures_entry = tkinter.Entry(window, textvariable = pastures, font = ('calibre', 12)).grid(row = 2, column = 1)

tkinter.Label(window, text ='Grain:', font = ('calibre', 12)).grid(row = 3)
grain_entry = tkinter.Entry(window, textvariable = grain, font = ('calibre', 12)).grid(row = 3, column = 1)

tkinter.Label(window, text ='Vegetables:', font = ('calibre', 12)).grid(row = 4)
veg_entry = tkinter.Entry(window, textvariable = veg, font = ('calibre', 12)).grid(row = 4, column = 1)

tkinter.Label(window, text='Sheep:', font = ('calibre', 12)).grid(row = 5)
sheep_entry = tkinter.Entry(window, textvariable = sheep, font = ('calibre', 12)).grid(row = 5, column = 1)
                      
tkinter.Label(window, text = 'Boars:', font = ('calibre', 12)).grid(row = 6)
boars_entry = tkinter.Entry(window, textvariable = boars, font = ('calibre', 12)).grid(row = 6, column = 1)

tkinter.Label(window, text = 'Cattle:', font = ('calibre', 12)).grid(row = 7)
cattle_entry = tkinter.Entry(window, textvariable = cattle, font = ('calibre', 12)).grid(row = 7, column = 1)

tkinter.Label(window, text = 'Unused Spaces:', font = ('calibre', 12)).grid(row = 8)
spaces_entry = tkinter.Entry(window, textvariable = spaces, font = ('calibre', 12)).grid(row = 8, column = 1)

tkinter.Label(window, text = 'Fenced Stables:', font = ('calibre', 12)).grid(row = 9)
stables_entry = tkinter.Entry(window, textvariable = stables, font = ('calibre', 12)).grid(row = 9, column = 1)

tkinter.Label(window, text = 'Clay Rooms:', font = ('calibre', 12)).grid(row = 10)
clay_entry = tkinter.Entry(window, textvariable = clay, font = ('calibre', 12)).grid(row = 10, column = 1)

tkinter.Label(window, text = 'Stone Rooms:', font = ('calibre', 12)).grid(row = 11)
stone_entry = tkinter.Entry(window, textvariable = stone, font = ('calibre', 12)).grid(row = 11, column = 1)

tkinter.Label(window, text = 'Family Members:', font = ('calibre', 12)).grid(row = 12)
fam_entry = tkinter.Entry(window, textvariable = fam, font = ('calibre', 12)).grid(row = 12, column = 1)

tkinter.Label(window, text = 'Bouns Cards:', font = ('calibre', 12)).grid(row = 13)
cards_entry = tkinter.Entry(window, textvariable = cards, font = ('calibre', 12)).grid(row = 13, column = 1)

tkinter.Label(window, text = 'Begging Cards:', font = ('calibre', 12)).grid(row = 14)
beg_entry = tkinter.Entry(window, textvariable = beg, font = ('calibre', 12)).grid(row = 14, column = 1)

#This function will be called within the print_score() function when the button is pushed
def score():

    field_ct = fields.get()
    pasture_ct = pastures.get()
    grain_ct = grain.get()
    veg_ct = veg.get()
    sheep_ct = sheep.get()
    boar_ct = boars.get()
    cattle_ct = cattle.get()
    spaces_ct = spaces.get()
    stables_ct = stables.get()
    clay_ct = clay.get()
    stone_ct = stone.get()
    fam_ct = fam.get()
    cards_ct = cards.get()
    beg_ct = beg.get()

    if field_ct <= 1:
        field_pts = -1
    elif field_ct == 2:
        field_pts = 1
    elif field_ct == 3:
        field_pts = 2
    elif field_ct == 4:
        field_pts = 3
    elif field_ct >= 5:
        field_pts = 4

    if pasture_ct <= 0:
        past_pts = -1
    elif pasture_ct == 1:
        past_pts = 1
    elif pasture_ct == 2:
        past_pts = 2
    elif pasture_ct == 3:
        past_pts = 3
    elif pasture_ct >= 4:
        past_pts = 4

    if grain_ct <= 0:
        grain_pts = -1
    elif grain_ct == 1 or grain_ct == 2 or grain_ct == 3:
        grain_pts = 1
    elif grain_ct == 4 or grain_ct == 5:
        grain_pts = 2
    elif  grain_ct == 6 or grain_ct == 7:
        grain_pts = 3
    elif grain_ct >= 8:
        grain_pts = 4

    if veg_ct <= 0:
        veg_pts = -1
    elif veg_ct == 1:
        veg_pts = 1
    elif veg_ct == 2:
        veg_pts = 2
    elif veg_ct == 3:
        veg_pts = 3
    elif veg_ct >= 4:
        veg_pts = 4

    if sheep_ct <= 0:
        sheep_pts = -1
    elif sheep_ct == 1 or sheep_ct == 2 or sheep_ct == 3:
        sheep_pts = 1
    elif sheep_ct == 4 or sheep_ct == 5:
        sheep_pts = 2
    elif sheep_ct == 6 or sheep_ct == 7:
        sheep_pts = 3
    elif sheep_ct >= 8:
        sheep_pts = 4

    if boar_ct <= 0:
        boar_pts = -1
    elif boar_ct == 1 or boar_ct == 2:
        boar_pts = 1
    elif boar_ct == 3 or boar_ct == 4:
        boar_pts = 2
    elif boar_ct == 5 or boar_ct == 6:
        boar_pts = 3
    elif boar_ct >= 7:
        boar_pts = 4

    if cattle_ct <= 0:
        cattle_pts = -1
    elif cattle_ct == 1:
        cattle_pts = 1
    elif cattle_ct == 2 or cattle_ct == 3:
        cattle_pts = 2
    elif cattle_ct == 4 or cattle_ct == 5:
        cattle_pts = 3
    elif cattle_ct >= 6:
        cattle_pts = 4

    space_pts = spaces_ct * -1
    stable_pts = stables_ct
    clay_pts = clay_ct
    stone_pts = stone_ct *2
    fam_pts = fam_ct * 3
    cards_pts = cards_ct
    beg_pts = beg_ct * -3

    total = field_pts + past_pts + grain_pts + veg_pts + sheep_pts + boar_pts + cattle_pts + space_pts + stable_pts + clay_pts + stone_pts + fam_pts + cards_pts + beg_pts
    points = str(total)
    return points
    
def showLicense():
    global system
    Ltext =""
    with open("LICENSE.txt") as file:
        for line in file:
            Ltext += line
    licenseWindow = tkinter.Toplevel(window)
    licenseWindow.title("MIT License")
    if system == 'Windows':
        licenseWindow.iconbitmap('agricola.ico')
    text = tkinter.Label(licenseWindow, text=Ltext)
    text.pack()

#This function servers as the score button command, also acts exception handling
def print_score():
    try:
        player_name = player.get()
    
        out = score()
        tkinter.Label(window, text = player_name + "'s score is " + out + '.', font = ('calibre', 12)).grid(column = 2)
    except:
        tkinter.messagebox.showinfo('Input Error', 'Only enter whole numbers. Letters and decimals are not accepted unless in the player name.')
   


if __name__ == '__main__':

    #button and command bind
    score_btn = tkinter.Button(window, text ='Click Me To Score', command = print_score).grid(row = 15, column = 2)
    license_btn = tkinter.Button(window, text='View License', command= showLicense).grid(row = 15, column=0)

    #infiite loop of the UI window
    window.mainloop()
