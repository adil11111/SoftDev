var fibby = function (num){
    if(num == 0){
	return 0;
    }
    if(num < 3){
	return 1;
    }
    return fibby(num - 1) + fibby(num - 2);
}

var gcd = function (a, b){
    if(b == 0){
	return a;
    }
    return gcd(b, a % b);
}

var students = ["Sam", "Tom", "Bobby", "Smith", "Tony", "John"];


var randomStudent = function (){
    var rand = Math.floor(Math.random() * 6);
    console.log(students[rand]);
    return students[rand];
}
var preFib = function(){
    var result = fibby(10);
    console.log(result);
    return result;
}
var preGcd = function(){
    var answer = gcd(25,55);
    console.log(answer);
    return answer;
}
var randStudent = document.getElementById("randStudent");
randStudent.addEventListener('click',function(){
    var result = randomStudent();
    var par = document.getElementById("show");
    par.innerHTML="Random Student Name: ";
    par.innerHTML+= result;
    console.log(result);
});

var fib = document.getElementById("fib");
fib.addEventListener('click',function(){
    var result = fibby(7);
    var par = document.getElementById("show");
    par.innerHTML="Seventh Fibonacci Number: ";
    par.innerHTML+= result;
    console.log(result);
});

var gcdButton = document.getElementById("gcd");
gcdButton.addEventListener('click',function(){
    var result = gcd(25,55);
    var par = document.getElementById("show");
    par.innerHTML="GCD of 25 & 55: ";
    par.innerHTML+= result;
    console.log(result);
});

