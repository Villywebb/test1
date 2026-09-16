gameOver = False
gamePhaseActive = False
playersDone = 0
startPhaseActive = False
players: List[str] = []
playerScores: List[number] = []
playerScoresName: List[str] = []
highest = 0
winner = ""
counter = 0

def on_button_pressed_a():
    global gameOver, gamePhaseActive, playersDone, startPhaseActive, players, playerScores, playerScoresName
    basic.show_icon(IconNames.HAPPY)
    gameOver = False
    gamePhaseActive = False
    playersDone = 0
    startPhaseActive = True
    players = []
    playerScores = []
    playerScoresName = []
    radio.set_group(89)
input.on_button_pressed(Button.A, on_button_pressed_a)

def highestScoreIndex(array: List[number]):
    global highest
    highest = 0
    for value in array:
        highest = max(value, highest)
    return array.index_of(highest)

def on_received_value(name22, value2):
    global playersDone, gamePhaseActive, winner
    if startPhaseActive:
        if findPlayer(name22, players) == " ":
            players.append(name22)
            basic.show_string(name22)
    if gamePhaseActive:
        if findPlayer(name22, players) != " " and findPlayer(name22, playerScoresName) == " ":
            playerScores.append(value2)
            playerScoresName.append(name22)
            playersDone += 1
        if playersDone == len(players):
            gamePhaseActive = False
            winner = playerScoresName[highestScoreIndex(playerScores)]
            radio.send_value(winner, 1)
            for value3 in playerScoresName:
                if value3 != winner:
                    radio.send_value(value3, 0)
            basic.show_string(winner)
radio.on_received_value(on_received_value)

def on_button_pressed_ab():
    global startPhaseActive, gamePhaseActive
    startPhaseActive = False
    gamePhaseActive = True
    radio.send_value("s", 0)
    while gamePhaseActive:
        basic.show_icon(IconNames.SQUARE)
        basic.pause(200)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.pause(200)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def findPlayer(name: str, players3: List[any]):
    global counter
    counter = 0
    while counter < len(players3):
        if name == players3[counter]:
            return name
        counter += 1
    return " "