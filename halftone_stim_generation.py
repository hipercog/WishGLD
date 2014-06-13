
from psychopy import visual,core,monitors,event,gui
import itertools
import random
import os
import colorsys

from PIL import Image #, ImageDraw

# set FACES=0 or LETTERS=1 or TEST=2
type = 2

IMG_W = 512
IMG_H= 512
DIMX = 26
DIMY = 26

coef = (DIMX * DIMY) / 2
s = os.sep
tystr = ['face', 'letter', 'test']
pth = '26x26' + s
outdir = tystr[type] + 'Cards' + s
if not os.path.exists(outdir):
    os.makedirs(outdir)
# pth = 'C:\\Kride\\Projects\\ReKnow\\WCST\\26x26\\'

#lenovo
myMon=monitors.Monitor('yoga', width=29.3, distance=40); myMon.setSizePix((3200, 1800))
#desktop
#myMon=monitors.Monitor('asus', width=37.8, distance=40); myMon.setSizePix((1920, 1080))
win = visual.Window( size=(IMG_W, IMG_H),units='pix',fullscr=False,monitor=myMon, color=(1.0, 1.0, 1.0), colorSpace='rgb')

imgs = []

if type == 0:
    for i in range(16):
        imgs.append( Image.open(pth + 'sf' + '%02d' % (i+1,) + '.png') )   #faces
elif type == 1:
    for i in range(17):
        imgs.append( Image.open(pth + 'smlltr' + '%01d' % (i+1,) + '.png') )    #letters
else:
    imgs.append( Image.open(pth + 'testi.png') )   #TEST!


# CREATING COLORS -------------------------------------------------------------------------------------------

# Color selection for equally perceivable colours is covered in Zeileis, Hornik and Murrell (2007), available here:
#   http://epub.wu.ac.at/1692/1/document.pdf
# The simple answer seems to be: use the CIE Luv color space. Code is here:
#   http://cran.r-project.org/web/packages/colorspace/vignettes/hcl-colors.pdf
# A palette derived from that R code (procedure unknown) is given as:

col1 = "#DB9D85"
col2 = "#86B875"
col3 = "#4CB9CC"
col4 = "#CD99D8"

# In the link below, a list of 128 distinct CIE Lab colours is given in HEX - may be useful to expand the palette.
#   http://stackoverflow.com/questions/2328339/how-to-generate-n-different-colors-for-any-natural-number-n
# Another approach is given below; it is a palette in RGB, HSL and LAB space, derived from this peer reviewed paper:
#   Boynton. Eleven Colors That Are Almost Never Confused. (1989)
#   http://alumni.media.mit.edu/~wad/color/palette.html
# Derivation was based on matching the qualitative palette from the paper with roughly even distributions in Lab space.
#           H    S    L         L    A    B        R    G    B
#Black      0    0    0         0    0    0        0    0    0
#Dk. Gray   0    0    34        50   0    0        87   87   87
#Red        0    80   68        50   58   40       173  35   35
#Blue       229  80   95        50   40   -77      42   75   215
#Green      114  80   41        50   -50  42       29   105  20
#Brown      28   80   51        50   20   44       129  74   25
#Purple     275  80   75        50   65   -61      129  38   192
#Lt. Gray   0    0    63        75   0    0        160  160  160
#Lt. Green  114  38   77        80   -34  25       129  197  122
#Lt. Blue   229  38   100       80   9    -34      157  175  255
#Cyan       180  80   82        80   -43  -14      41   208  208
#Orange     28   80   100       80   28   62       255  146  51
#Yellow     60   80   97        96   -19  77       255  238  51
#Tan        28   20   93        91   5    12       233  222  187
#Pink       0    20   100       91   15    6       255  205  243
#White      0    0    100       100  0    0        255  255  255

# set of duller colors
#red = (173, 35, 35)
#blue = (42, 75, 215)
#green = (29, 105, 20)
#brown = (129, 74, 25)
#purple = (129, 38, 192)
# set of brighter colors
#ltgreen = (129, 197, 122)
#ltblue = (157, 175, 255)
#cyan = (41, 208, 208)
#orange = (255, 146, 51)
#
# gray can be lighter or darker
#gray = (1, 1, 1)
#
#norm = 255.0
#gray = [x*(87/norm) for x in gray] # gray that you can set at any level by changing one number
#red = [x/norm for x in red]
#blue = [x/norm for x in blue]
#green = [x/norm for x in green]
#brown = [x/norm for x in brown]
#purple = [x/norm for x in purple]
#ltgreen = [x/norm for x in ltgreen]
#ltblue = [x/norm for x in ltblue]
#cyan = [x/norm for x in cyan]
#orange = [x/norm for x in orange]

# HSL colors
# Absolutely equiluminant colours can be selected simply by iterating around the colour wheel in 360/N arcs
# HOWEVER, this is not based on perceptual findings, as described above.
def get_N_HexCol(N, S, L):

    HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    RGB_tuples = map(lambda x: tuple(map(lambda y: int(y * 255),x)),RGB_tuples)
    HEX_tuples = map(lambda x: tuple(map(lambda y: chr(y).encode('hex'),x)), RGB_tuples)
    HEX_tuples = map(lambda x: "".join(x), HEX_tuples)

    return HEX_tuples
#CMY, RGB
#colc = (0, 1, 1)
#colm = (1, 0, 1)
#coly = (1, 1, 0)
#colr = (1, 0, 0)
#colg = (0, 1, 0)
#colb = (0, 0, 1)

colors = []
colors.append( col1 )
colors.append( col2 )
colors.append( col3 )
colors.append( col4 )
#colors.append( gray )
#colors.append( red )
#colors.append( blue )
#colors.append( green )
#colors.append( brown )
#colors.append( purple )
#colors.append( ltgreen )
#colors.append( ltblue )
#colors.append( cyan )
#colors.append( orange )


# VISUAL FEATURES ----------------------------------------------------------------------------------------------
feats=[]

#SHAPES
featTriangle = visual.ShapeStim( win, lineWidth=1.0, lineColor=(0.0, 0.0, 0.0), lineColorSpace='rgb',\
                         fillColor=(0.0, 0.0, 0.0), fillColorSpace='rgb',\
                         vertices=((0, 10), (8, -10), (-8, -10), (0, 10)), 
                         closeShape=True )
                         
featDiamond = visual.ShapeStim( win, lineWidth=1.0, lineColor=(0.0, 0.0, 0.0), lineColorSpace='rgb',\
                         fillColor=(0.0, 0.0, 0.0), fillColorSpace='rgb',\
                         vertices=((0, 10), (8, -6), (0,-10), (-8, -6), (0, 10)), 
                         closeShape=True )

featHouse = visual.ShapeStim( win, lineWidth=1.0, lineColor=(0.0, 0.0, 0.0), lineColorSpace='rgb',\
                         fillColor=(0.0, 0.0, 0.0), fillColorSpace='rgb',\
                         vertices=((0, 10), (5.7, 0), (5.7,-9), (-5.7, -9), (-5.7,0), (0, 10)), 
                         closeShape=True )

featArrow = visual.ShapeStim( win, lineWidth=1.0, lineColor=(0.0, 0.0, 0.0), lineColorSpace='rgb',\
                         fillColor=(0.0, 0.0, 0.0), fillColorSpace='rgb',\
                         vertices=((0, 10), (8, 0), (4,0), (4, -10), (-4,-10), (-4, 0), (-8, 0), (0,10)), 
                         closeShape=True )

#not used
#featDrop = visual.ShapeStim( win, lineWidth=1.0, lineColor=(0.0, 0.0, 0.0), lineColorSpace='rgb',\
#                         fillColor=(0.0, 0.0, 0.0), fillColorSpace='rgb',\
#                         vertices=((0, 10), (7, 1), (6.9, -4), (5.65, -5.65), (4, -6.9), (0,-8), (-4, -6.9), (-5.65, -5.65), (-6.9, -4), (-7, 1), (0, 10)), 
#                         closeShape=True )

featStarTrek = visual.ShapeStim( win, lineWidth=1.0, lineColor=(0.0, 0.0, 0.0), lineColorSpace='rgb',\
                         fillColor=(0.0, 0.0, 0.0), fillColorSpace='rgb',\
                         vertices=((0, 10), (8, -10), (0,0), (-8, -10), (0, 10)), 
                         closeShape=True )

#featA = visual.ShapeStim( win, lineWidth=2.0, lineColor=(0.0, 0.0, 0.0), lineColorSpace='rgb',\
#                         fillColor=None, fillColorSpace='rgb',\
#                         vertices=((-6, -8), (0,10), (6,-8), (3,-4), (-3,-4) ),
#                         closeShape=True )


#LETTERS

#letters='ADEFHJKLMNPRSTUVY'
letters='ADEF'
lenltrs = len(letters)

# REFERENCE:
#visual.TextStim( win, text='a letter', font='a system font', pos=(0.0, 0.0), depth=0, rgb=None, color=(0.0, 0.0, 0.0),\
#                colorSpace='rgb', opacity=1.0, contrast=1.0, units='', ori=0.0, height=None, antialias=True,\
#                bold=False, italic=False, alignHoriz='center', alignVert='center', fontFiles=[], wrapWidth=None,\
#                flipHoriz=False, flipVert=False, name=None, autoLog=None ) )

if type == 0:
    feats.append( featTriangle )
    feats.append( featDiamond )
    feats.append( featHouse )
    feats.append( featArrow )
elif type == 1:
    for ltr in range(len(letters)):
        feats.append( visual.TextStim( win, text=letters[ltr], font='Sloan', color=(0.0, 0.0, 0.0), bold=True ) )
else:
    feats.append( featStarTrek )


# BUILDING CARDS AS STIM/COLOR/FEATURE/ORIENTATION COMBINATIONS -------------------------------------------------------

step = IMG_W/DIMX
half = -1*IMG_W/2 #image coords are centered

PREVAIL_COL_RATIO = 0.5
N_OF_FACES = len(imgs)
N_OF_FEATS = len(feats)
SAVE_FRAMES = True
N_CLRS = len(colors)

#card generation    
for faceN in range( N_OF_FACES ):
    
    # Build color probabilities by observation
    gt = 0  # greytotal
    for xi in range(DIMX):
        for yi in range(DIMY):
            vali = imgs[faceN].getpixel( (xi,DIMY-1-yi) )
            gt = gt + (255-vali)/255.0
#    print 'image gt=' + str(round(gt)) # DEBUG PRINT

    for cardColor in range(N_CLRS):
        colIdx = range(N_CLRS)
        colIdx.remove( cardColor )

        for featN in range( N_OF_FEATS ):

            for featOrientation in range( 4 ): 

                ct = 0  # color total - to collect how much of the total coloured area is dominant
                nt = 0  # other colors

                for x in range(DIMX):
                    for y in range(DIMY):

                        feats[featN].pos = ( half+(x+1)*step, half+(y+1)*step)
                   
                        val = imgs[faceN].getpixel( (x,DIMY-1-y) )
                        #flip y-axis
                        sz = (255-val)/255.0
                        
                        PREVAIL_COL_RATIO = (sz/gt)*coef
                        
#                        print 'size=' + str(round(sz,3)) + '; PCR=' + str(round(PREVAIL_COL_RATIO,2)) # DEBUG PRINT
                        
                        if (random.random() < PREVAIL_COL_RATIO):
                            c = cardColor
#                            ct = ct + sz
                        else:
                            c = colIdx[random.randint(0,2)]
#                            nt = nt + sz
                        
                        feats[featN].color      = colors[c]
                        feats[featN].fillColor  = colors[c]
                        feats[featN].lineColor  = colors[c]
                        feats[featN].ori        = 45+ 90*featOrientation
                        feats[featN].size       = sz #round(sz,1) #(sz, sz)
                        feats[featN].draw( win )

                win.flip()
                if( SAVE_FRAMES ):
                    win.getMovieFrame()
                    win.saveMovieFrames( outdir + '%02d_%02d_%02d_%02d.png' % (faceN, cardColor, featN, featOrientation ))

#                print 'image ct=' + str(round(ct)) + '; nt=' + str(round(nt)) + '; ratio=' + str(round(ct/gt, 2)) # DEBUG PRINT

#cleanup
win.close()
core.quit()

