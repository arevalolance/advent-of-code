let data = prompt("input");
let nums = data.split("\n").map(Number);

function solveSecond() {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i; j < nums.length; j++) {
            for (let k = j; k < nums.length; k++) {
                let x = nums[i];
                let y = nums[j];
                let z = nums[k];
                if (+(x+y+z) === 2020) {
                    return x*y*z;
                }
            }
        }
    }
    return null;
}

function solveFirst() {
    nums.sort();
    let done = false;
    let small = 0;
    let large = nums.length - 1;
    while (!done) {
        sum = nums[small] + nums[large];
        if (sum > 2020)
            large--;
        if (sum < 2020)
            small++;
        
        if (sum === 2020) {
            done = true;
            return nums[small] * nums[large];
        }
    }
}

console.log(solveFirst());
console.log(solveSecond());