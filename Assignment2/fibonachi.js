// number
const number = 1000000000000000000000000000000000000000000000000000002333333333300000000000000000000000000000000000055555555555555555243333333333;

if(number <=0) {
    console.log('Input Error');
}
else {
    for(let i = 0; i < number; i++) {
        console.log(fibonacci(i));
    }
}

function fibonacci(num) {
    if(num < 2) {
        return num;
    }
    else {
        return fibonacci(num-1) + fibonacci(num - 2);
    }
}

