//define global
displayOut = document.getElementById("display-here");
summed = false;
nightMode = false;

function clickIn(btn){
	if(summed === true){
		clearDisplay();
		summed = false;
	}
	
	var temp = String(btn);
	displayOut.innerHTML += temp;
}


function clearDisplay(){
	displayOut.innerHTML = '&emsp;';
}

function getSum(){
	var getLine = displayOut.innerHTML;
	console.log(getLine);
	//swap in * / 3.141... use reg-exp to replace instances
	getLine = getLine.replace(/x/g, "*");
	//getLine = getLine.replace(/divide/g, "/");
	getLine = getLine.replace(/pi/g, "3.142");
	console.log(getLine);
	summed = true;

	try {
		displayOut.innerHTML = +eval(getLine).toFixed(3); 
	} catch (e) {
		if (e instanceof SyntaxError || e instanceof ReferenceError) {
			displayOut.innerHTML = "Error!";
		} 
	}	

	
}

function nightModeToggle(){
	if(nightMode === false){
		document.getElementById('pageStyle').setAttribute('href',"night.css");
		nightMode = true;
		document.getElementsByTagName('footer')[0].innerHTML = "<i>Day mode...</i>";
	} else {
			document.getElementById('pageStyle').setAttribute('href',"day.css");
			nightMode = false;
			document.getElementsByTagName('footer')[0].innerHTML = "<i>Night mode...</i>";

	}
}

//now assign functions to buttons:
document.getElementById('bPt').onclick = function(){clickIn('.')};
document.getElementById('b0').onclick = function(){clickIn('0')};
document.getElementById('b1').onclick = function(){clickIn('1')};
document.getElementById('b2').onclick = function(){clickIn('2')};
document.getElementById('b3').onclick = function(){clickIn('3')};
document.getElementById('b4').onclick = function(){clickIn('4')};
document.getElementById('b5').onclick = function(){clickIn('5')};
document.getElementById('b6').onclick = function(){clickIn('6')};
document.getElementById('b7').onclick = function(){clickIn('7')};
document.getElementById('b8').onclick = function(){clickIn('8')};
document.getElementById('b9').onclick = function(){clickIn('9')};
document.getElementById('bX').onclick = function(){clickIn('x')};
document.getElementById('bPlus').onclick = function(){clickIn('+')};
document.getElementById('bMin').onclick = function(){clickIn('-')};
document.getElementById('bDiv').onclick = function(){clickIn('/')};
document.getElementById('bLeft').onclick = function(){clickIn('(')};
document.getElementById('bRight').onclick = function(){clickIn(')')};
document.getElementById('bPi').onclick = function(){clickIn('pi')};
document.getElementById('bEq').onclick = function(){getSum()};
document.getElementById('bC').onclick = clearDisplay;
document.getElementById('setMode').onclick = function(){nightModeToggle()};