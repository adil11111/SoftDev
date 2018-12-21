// SoftDev1 pd7
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-20

//fib function
var fibby = function (num){
    if(num == 0){
	return 0;
    }
    if(num < 3){
	return 1;
    }
    return fibby(num - 1) + fibby(num - 2);
}

var num = 0; //counter for fib number
var items = document.getElementById("thelist");
var button = document.getElementById("b");

// if button is clicked add word to list
button.addEventListener("click", function(){
    var node = document.createElement("li");
    node.innerHTML= "WORD";
    items.appendChild(node);
});

var fib = document.getElementById("fb");
var fiblist = document.getElementById("fiblist");

// if fib button clicked add next fib number
fib.addEventListener("click",function(){
    var fibNode = document.createElement("li");
    fibNode.innerHTML=fibby(num);
    num+=1;
    fiblist.appendChild(fibNode);
});
var heading = document.getElementById('h');

//change heading to item that mouse is over
items.addEventListener('mouseover', function(e) {
  heading.innerHTML = e.target.innerHTML;
});

//remove item on click
items.addEventListener('click', function(e) {
    e.target.remove();
});

//revert heading back when no longer over item
items.addEventListener("mouseout",function(){
    heading.innerHTML = "Hello World!";
});

