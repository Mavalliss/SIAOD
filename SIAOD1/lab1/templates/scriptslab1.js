function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

function readFile(object) {
    var file = object.files[0]
    var reader = new FileReader()
    reader.onload = function () {
        document.getElementById('txtIn').innerHTML = reader.result
    }
    reader.readAsText(file)
}

function SortMe() {
    res = res.slice(0, -1)
    res = res.replace(/  /g, " ")
    res = res.replace(/^\s*(.*)\s*$/, '$1')
}

function randomMe() {
    var randomstr = ""
    for (var i = 0; i < getRandomInt(20); i++) {
        for (var j = 0; j < getRandomInt(10); j++) {
            randomstr += getRandomInt(100) + " "
        }
        if (getRandomInt(1) === 0) {
            randomstr = randomstr.slice(0, -1)
            randomstr += "\n"
        }
    }
    randomstr = randomstr.slice(0, -1)
    document.getElementById('txtIn').innerHTML = randomstr
    SortMe()
}