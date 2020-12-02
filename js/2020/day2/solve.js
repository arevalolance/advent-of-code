let data = prompt("input");
let lines = data.split("\n")

function solve() {
    let partOne = 0;
    let partTwo = 0;
    for (let i = 0; i < lines.length; i++) {
        let data = lines[i].split(" ");
        let key = data[2];
        let char = data[1][0];
        let nums = data[0].split("-").map(Number);
        partOne += part_one(nums[0], nums[1], char, key);
        partTwo += part_two(nums[0], nums[1], char, key);
    }
    console.log(partOne);
    console.log(partTwo);
}

function part_one(low, high, letter, key) {
    let count = 0;
    for (let i = 0; i < key.length; i++) {
        if (key[i] == letter)
            count++;
    }
    if (low <= count && count <= high)
        return 1;
    return 0;
}

function part_two(low, high, letter, key) {
    if ((key[low-1] == letter) ^ (key[high-1] == letter))
        return 1;
    return 0;
}

solve();