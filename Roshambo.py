import random


scoreboard = {
'p1Name': 'name',
'p2Name': 'name',
'computer': 'computer',
'p1Score': 0,
'p2Score': 0,
'cpuScore': 0,
}

print('Singleplayer: 1')
print('Mulitplayer: 2')
gameMode = input('Select Gamemode (1/2): ').lower()

if gameMode == '2':
  name1 = input('Player 1 Name: ')
  scoreboard['p1Name'] = name1
  print("\033[H\033[J", end="")
  name2 = input('Player 2 Name: ')
  scoreboard['p2Name'] = name2

if gameMode == '1':
  name1 = input('Player 1 Name: ')
  scoreboard['p1Name'] = name1
  print("\033[H\033[J", end="")
  computer = 'computer'
  



while True:

  if gameMode == '2':
    def getThrow(player):
      throws = ('paper', 'rock', 'scissors')
      throw = input(player +': what is your throw: ')
      return throws.index(throw.lower())

    def findWinner(throw1, throw2):
      winningCombo = ((0,1), (1,2), (2,0))
      if throw1 == throw2:
        return 'tie :('
      if (throw1, throw2) in winningCombo:
        return scoreboard['p1Name']
      return scoreboard['p2Name']
    
    def currentWinner(scoreboard):
      if scoreboard['p1Score'] == scoreboard['p2Score']:
        return 'Tie'
      if scoreboard['p1Score'] > scoreboard['p2Score']:
        return scoreboard['p1Name']
      return scoreboard['p2Name']

    throws = ('paper', 'rock', 'scissors')

    p1Throw = getThrow(scoreboard['p1Name'])
    print("\033[H\033[J", end="")
    p2Throw = getThrow(scoreboard['p2Name'])
      

    length = len(name1) + len(name2) + 5
    
    if findWinner(p1Throw, p2Throw) == scoreboard['p1Name']:
      scoreboard['p1Score'] += 1 
    if findWinner(p1Throw, p2Throw) == scoreboard['p2Name']:
      scoreboard['p2Score'] += 1 

    print(findWinner(p1Throw, p2Throw))
    print('<' + name1 + '>' + '|' + '<' + name2 + '>')
    print('-'*(length))
    print(scoreboard['p1Score'], end=' ')
    print(end=' '*(length - 3))
    print(scoreboard['p2Score'])
    print('Current Winner: ' + currentWinner(scoreboard))


    end = input('Continue? Y/N: ').lower()
    if end.lower() == 'n':
      print('Thank You!')
      break
    elif end.lower() =='y':
      continue
    else:
      print('Incorrect Input, Continuing')


  if gameMode == '1':
    def getThrow(player):
      throws = ('paper', 'rock', 'scissors')
      throw = input(player +': what is your throw: ')
      return throws.index(throw.lower())


    def findWinner(throw1, cpu,):
      winningCombo = ((0,1), (1,2), (2,0))
      if throw1 == cpu:
        return 'tie :('
      if (throw1, cpu) in winningCombo:
        return 'player 1'
      return 'computer'

    def currentWinner(scoreboard):
      if scoreboard['p1Score'] == scoreboard['cpuScore']:
        return 'Tie'
      if scoreboard['p1Score'] > scoreboard['cpuScore']:
        return scoreboard['p1Name']
      return scoreboard['computer']


    p1Throw = getThrow(scoreboard['p1Name'])
    print("\033[H\033[J", end="")
    comThrow = random.randint(0,2)
    print(comThrow)

    length = len(name1) + len(computer) + 5
    
    if findWinner(p1Throw, comThrow) == 'player 1':
      scoreboard['p1Score'] += 1 
    if findWinner(p1Throw, comThrow) == 'computer':
      scoreboard['cpuScore'] += 1 

  

    print(findWinner(p1Throw, comThrow))
    print('<' + name1 + '>' + '|' + '<' + computer + '>')
    print('-'*(length))
    print(scoreboard['p1Score'], end=' ')
    print(end=' '*(length - 3))
    print(scoreboard['cpuScore'])
    print('Current Winner: ' + currentWinner(scoreboard))

    end = input('Continue? Y/N: ').lower()
    if end.lower() == 'n':
      print('Thank You!')
      break
    elif end.lower() =='y':
      continue
    else:
      print('Incorrect Input, Continuing')


#Sorry about the excessive ammount of code.