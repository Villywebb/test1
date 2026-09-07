function newPlayer (playerName: string, players: string[]) {
    players.push(playerName)
    counter = 0
}
radio.onReceivedValue(function (name, value) {
    let startPhaseActive = 0
    text_list = []
    if (startPhaseActive) {
        counter = 0
        for (let index = 0; index < text_list.length; index++) {
            if (name == text_list[counter]) {
                basic.showString("" + (value))
                break;
            }
            counter += 1
        }
        if (counter == text_list.length) {
            newPlayer(name, text_list)
        }
    }
})
let text_list: number[] = []
let counter = 0
radio.sendValue("server", 5)
basic.forever(function () {
	
})
