let gameOver = false
let gamePhaseActive = false
let playersDone = 0
let startPhaseActive = false
let players: string[] = []
let playerScores: number[] = []
let playerScoresName: string[] = []
let highest = 0
let winner = ""
let counter = 0
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    gameOver = false
    gamePhaseActive = false
    playersDone = 0
    startPhaseActive = true
    players = []
    playerScores = []
    playerScoresName = []
    radio.setGroup(89)
})
function highestScoreIndex (array: number[]) {
    highest = 0
    for (let value of array) {
        highest = Math.max(value, highest)
    }
    return array.indexOf(highest)
}
radio.onReceivedValue(function (name22, value2) {
    if (startPhaseActive) {
        if (findPlayer(name22, players) == " ") {
            players.push(name22)
            basic.showString(name22)
        }
    }
    if (gamePhaseActive) {
        if (findPlayer(name22, players) != " " && findPlayer(name22, playerScoresName) == " ") {
            playerScores.push(value2)
            playerScoresName.push(name22)
            playersDone += 1
            if (playersDone == players.length) {
                gamePhaseActive = false
                winner = playerScoresName[highestScoreIndex(playerScores)]
                radio.sendValue(winner, 1)
                for (let value3 of playerScoresName) {
                    if (value3 != winner) {
                        radio.sendValue(value3, 0)
                    }
                }
                basic.showString(winner)
            }
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    startPhaseActive = false
    gamePhaseActive = true
    radio.sendValue("s", 0)
    while (gamePhaseActive) {
        basic.showIcon(IconNames.Square)
        basic.pause(200)
        basic.showIcon(IconNames.SmallSquare)
        basic.pause(200)
    }
})
function findPlayer (name: string, players3: any[]) {
    counter = 0
    while (counter < players3.length) {
        if (name == players3[counter]) {
            return name
        }
        counter += 1
    }
    return " "
}
