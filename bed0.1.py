import random

# version 0.1

print ('bed #', end='')

pseudoRand1 = ['2','3','4','5','6','7','8','9','4']
print(random.choice(pseudoRand1), end='')

pseudoRandA = ['A','B','C','D','E','F',
'G','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y',
'Z','Z']
print(random.choice(pseudoRandA), end='')

pseudoRand2 = ['1','2','3','4','5','6','7','8','9','7']
print(random.choice(pseudoRand2), end='')

pseudoRandB = ['A','B','C','D','E','F',
'G','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y',
'Z','Z']
print(random.choice(pseudoRandB))

# bed generation starts

bedPref  = ['Your bed has a',
'The bed has a',
'The bed inside has a']
print(random.choice(bedPref), end=' ')

mattDesc1 = ['premium memory foam',
'sleep number',
'classic spring',
'hybrid',
'Eurotop']                
print(random.choice(mattDesc1), end=' ')

mattDesc2 = ['round',
'daybed',
'king',
'twin XL',
'full',
'queen',
'Alaska king',
'twin',
'short king (twin)',
'queen']
print(random.choice(mattDesc2), end=' ')

print ('mattress and ')

bedSheets = ['silky',
'luxury cotton',
'90s-era mint condition pokemon',
'narwhal print',
'real silk',
'rose patterned',
'pre-warmed',
'black butter-soft cotton',
'cool blue',
'impeccably clean white',
'soft jersey knit purple'] 
print(random.choice(bedSheets), end=' ')

print ('sheets. It')

bedSheets = ['is covered in plush sharks.',
'also houses a number of beanie babies both on top and underneath.',
'has a weighted blanket on top.',
'smells like pumpkin spice.',
'smells like chocolate chip cookies.',
'smells like lavendar.',
'has a gecko in a luxurious terrarium next to it; itself already asleep under its heatlamp.',
'is exceptionally warm and cozy.',
'has very chilly pillows.',
'has a therapeutic pillow that properly aligns your spine.',
'has a cat purring contentedly atop.',
'has a small dog sleeping in a matching bed next to it.',
'is resessed into the floor and surrounded by walls lined with bookcases.',
'has a nightstand with a glass of cool water and some strawberry melatonin tablets next to it.',
'is just stiff enough to make your spine feel rejuvenated in the morning.',
'is floating serenely about 20cm off the floor.',
'is a racecar bed! Vroom vroom!',
'exudes a calming aura.',
'has a force field of protection.',
'is suspended from the ceiling beams by velvet-wrapped chains.',
'has pillowy sides.',
'has a selection of blackets of various materials and thicknesses in a chest at the foot.',
'has a giant unicorn plushy to keep you company.',
'has advanced anti-nightmare technology.',
'has a build-a-bear tucked into it.',
'has a variety of massage functions.'] 
print(random.choice(bedSheets))             
