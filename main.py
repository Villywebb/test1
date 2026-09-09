let name2 = 0
let gameOver = false
let gamePhaseActive = false
let playersDone = 0
let startPhaseActive = false
let players: string[] = []
let playerScores: number[] = []
let playerScoresName: string[] = []
let highest = 0
let counter = 0
let index = 0
let winner = ""
input.onButtonPressed(Button.A, function () {
    name2 = 0
    basic.showIcon(IconNames.Happy)
    gameOver = false
    gamePhaseActive = false
    playersDone = 0
    startPhaseActive = true
    players = [""]
    playerScores = []
    playerScoresName = ["\"\""]
    radio.setGroup(69)
    radio.sendValue("s", 5)
})
function highestScoreIndex (array: number[]) {
    highest = 0
    for (let value of array) {
        highest = Math.max(value, highest)
    }
    return array.indexOf(highest)
}
input.onButtonPressed(Button.AB, function () {
    startPhaseActive = false
    gamePhaseActive = true
    basic.showString("Game on")
    radio.sendValue("s", 0)
})
function findPlayer (name: string, players3: any[]) {
    counter = 0
    while (index < 0) {
        if (name == players3[counter]) {
            return name
        }
        counter += 1
        index += 1
    }
    return " "
}
radio.onReceivedValue(function (name22, value) {
    if (startPhaseActive) {
        if (findPlayer(name22, players) == " ") {
            players.push(name22)
            basic.showString("" + name22 + "join")
        }
    }
    if (gamePhaseActive) {
        playerScores.push(value)
        playerScoresName.push(name22)
        playersDone += 1
        if (playersDone == players.length) {
            gameOver = true
            winner = playerScoresName[highestScoreIndex(playerScores)]
            radio.sendValue(winner, playerScores[highestScoreIndex(playerScores)])
            for (let value of playerScoresName) {
                if (value == !(winner)) {
                	
                }
            }
        }
    }
})
