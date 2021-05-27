print('''
                      _________________________
                  __ /  ,------++---. .-------.`.
                    /  /      //    | ||       |.`.
                __ /  /      //     | ||       | `.`.
               __ |  '------++------' |`-------+--[)| `---..___
               __ !]            _     |             |    ______"""-.
                 _!]__________ |_|    |             |   ,,----.\___|_
                 |___ /',--. \\       |_____________|  // ,--.\\____|
                  \_-/'|    |! \----------------------'| |    |!|_/
                      \ `--' /!'----------------------' \ `--' /
                       `'---'                            `'---'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input('Which way do you choose to go? left or right? ')
if left_right == 'right'.lower() or 'r'.lower():
  print('game over') 
elif left_right == 'left'.lower() or 'l'.lower():
  swim_wait = input('Would you like to swim or wait? swim or wait? ')
  if swim_wait == 'swim'.lower() or 's'.lower():
     print('game over')
  elif swim_wait == 'wait'.lower() or 'w'.lower():
    door = input('which door do you want to follow? Red or Blue or Yellow? ')
    if door == 'Yellow'.lower() or 'Y'.lower():
      print('You Win!')
    elif door == 'Red'.lower() or 'R'.lower():
      print('Burned by fire. Game Over.')
    elif door == 'Blue'.lower() or 'B'.lower():
      print('Eaten by beasts. Game Over.')
    else:
      print('please select one of the choices to continue')
  else:
    print('please select one of the choices to continue')
else:
  print('please select one of the choices to continue')

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload