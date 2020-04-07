function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}
function readFile(object) {
var file = object.files[0]
var reader = new FileReader()
reader.onload = function() {
    document.getElementById('txtIn').innerHTML = reader.result
}
reader.readAsText(file)
}

function randomMe() {
var randomstr = ""
for (var i = 0; i < getRandomInt(20); i++) {
    for (var j = 0; j < getRandomInt(10); j++) {
        randomstr += getRandomInt(100) + " "
    }
}
randomstr = randomstr.slice(0, -1)
document.getElementById('txtIn').value = randomstr
}

function compareNumbers(a, b) {
    return a - b;
}
function SortMe() {
var res = ""
var arr = document.getElementById('txtIn').value
arr = arr.split(' ')
arr.sort(compareNumbers)
for (var i = 0; i < arr.length; i++) {
    res += arr[i] + " "
}
res = res.slice(0, -1)
document.getElementById('txtIn').value = res
}