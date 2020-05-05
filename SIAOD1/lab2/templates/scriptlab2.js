window.onload = function () {
    if (document.getElementById('txtIn').value === "")
        document.getElementById("clear").style.display = "none";
    else
        document.getElementById("clear").style.display = "block";
};

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

function readFile(object) {
    var file = object.files[0]
    var reader = new FileReader()
    reader.onload = function () {
        document.getElementById('txtIn').value = reader.result
    }
    reader.readAsText(file)
    document.getElementById("clear").style.display = "block";
}

function randomMe() {
    var randomstr = ""
    for (var i = 0; i < getRandomInt(100); i++) {
        for (var j = 0; j < getRandomInt(100); j++) {
            randomstr += getRandomInt(1000) + " "
        }
    }
    randomstr = randomstr.slice(0, -1)
    document.getElementById('txtIn').value = randomstr
    SortMe()
}

function compareNumbers(a, b) {
    return a - b;
}

function SortMe() {
    var res = ""
    var arr = document.getElementById('txtIn').value
    arr = arr.replace(/, /g, " ")
    document.getElementById('txtIn').value = arr
    arr = arr.split(' ')
    arr.sort(compareNumbers)
    for (var i = 0; i < arr.length; i++) {
        res += arr[i] + " "
    }
    res = res.replace(/,/g, " ")
    res = res.slice(0, -1)
    res = res.replace(/  /g, " ")
    res = res.replace(/^\s*(.*)\s*$/, '$1')
    document.getElementById('txtIn').value = res
    document.getElementById("clear").style.display = "block";
}

function ClearAll() {
    document.getElementById('txtIn').value = ""
    document.getElementById('charIn').value = ""
    document.getElementById("clear").style.display = "none";
}