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
randStudent.addEventListener('click',randomStudent);

var fib = document.getElementById("fib");
fib.addEventListener('click',preFib);

var gcdButton = document.getElementById("gcd");
gcdButton.addEventListener('click',preGcd);

