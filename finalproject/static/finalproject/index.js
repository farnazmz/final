//requesting some of the functions to be run on load of the page.
document.addEventListener('DOMContentLoaded', function () {

	//charts will be shown on nutrition.html page as an google chart.
	//chart for the sleepdaily page
	google.charts.load('current', { 'packages': ['bar'] });
	google.charts.setOnLoadCallback(drawStuff);

	//chart for the nutrition page
	google.load('visualization', '1', {packages:['gauge']});
    google.setOnLoadCallback(drawChart);
});


//creating the analog clock on all application pages' heading.
const minuteHand = document.querySelector('.minuteHand');
const hourHand = document.querySelector('.hourHand');
function analogClock() {
	const analogNow = new Date();
	const minute = analogNow.getMinutes();
	const mdeg = ((minute / 60) * 360) + 90;
	minuteHand.style.transform = `rotate(${mdeg}deg)`;
	const hour = analogNow.getHours();
	const hdeg = ((hour / 12) * 360) + ((minute / 60) * 30) + 90;
	hourHand.style.transform = `rotate(${hdeg}deg)`;
}
setInterval(analogClock, 1000);
analogClock();

//declaring the variables for alarm funtion.
var digitalTime, alarm, Hour, Minute,
	alarmOn = false,
	audio = new Audio("https://audio.code.org/winpoint2.mp3");
audio.loop = true;

//this function will be shown on the alarm.html page
function digitalClock() {
	var ampm;
	var digitalNow = new Date();
	digitalTime = digitalNow.toLocaleTimeString([], {
		hour: '2-digit',
		minute: '2-digit',
		ampm
	});
	clock.textContent = digitalTime;
	if (digitalTime === alarm) {
		audio.play();
	}
	setTimeout(digitalClock, 1000);
}

//setting the time format and custom options.
digitalClock();

//decrating variables and the code for minutes count.
function digitalMin(id) {
	var select = id;
	var min = 59;
	for (i = 0; i <= min; i++) {
		select.options[select.options.length] = new Option(i < 10 ? "0" + i : i, i < 10 ? "0" + i : i);
	}
}

//showing the time as an 12 hour format.
function digitalHour(id) {
	var select = id;
	var hour = 12;
	for (i = 0; i <= hour; i++) {
		select.options[select.options.length] = new Option(i < 10 ? "0" + i : i, i < 10 ? "0" + i : i);
	}
}

//keep the alarm on or off, based on the initial status.
digitalMin(minutes);
digitalHour(hours);
startstop.onclick = function () {
	//turning the alarm on.
	if (alarmOn === false) {
		hours.disabled = true;
		minutes.disabled = true;
		ampm.disabled = true;
		alarm = hours.value + ":" + minutes.value + " " + ampm.value;
		this.textContent = "Clear alarm at: " + hours.value + ":" + minutes.value + " " + ampm.value;
		alarmOn = true;
	} else {
		//turning the alarm off.
		hours.disabled = false;
		minutes.disabled = false;
		ampm.disabled = false;
		audio.pause();
		alarm = "00:00:00 AM";
		this.textContent = "Set Alarm";
		alarmOn = false;
	}
};


var consumed = document.querySelector('#counted').innerHTML;
//creating a google chart based on daily nutritions and their maximum leves. Exeeded amount will be shown with a red bar.
function drawStuff() {
  var consumed_4 = document.querySelector('#Carbohydrates').innerHTML;
  var consumed_7 = document.querySelector('#DietaryFibre').innerHTML;
  var consumed_2 = document.querySelector('#Fat').innerHTML;
  var consumed_1 = document.querySelector('#Protein').innerHTML;
  var consumed_3 = document.querySelector('#SaturatedFattyAcids').innerHTML;
  var consumed_6 = document.querySelector('#Sodium').innerHTML;
  var consumed_5 = document.querySelector('#Sugars').innerHTML;

  //creating the data needed before drawing the chart.
  var data = new google.visualization.arrayToDataTable([
	['Category', {'number': 'Consumed'}, 'Max'],
	['Carbohydrates', consumed_4, 304],
	['DietaryFibre', consumed_7, 25],
	['Fat', consumed_2, 65],
	['Protein', consumed_1, 50],
	['SaturatedFattyAcids', consumed_3, 20],
	['Sodium', consumed_6, 2.3],
	['Sugars', consumed_5, 38],
]);

  //options for chart appearance.
  var options = {
	  width: 800,
	  chart: {
		  title: 'Consumed Values',
		  subtitle: 'Max in red, Consumed in blue',
	  },
	  bars: 'vertical',
	  axes: {
		  y: {
			all:{
				range: {
					max: 100
				}
			}
		}

	  },
	  chartArea: {
		  backgroundColor: {
			fill: '#ffeda3',
			fillOpacity: 0.1
		  },
		},
		backgroundColor: {
		  fill: '#ffeda3',
		  fillOpacity: 0.8
		},
  };
  var chart = new google.charts.Bar(document.getElementById('myChart'));
  chart.draw(data, options);

  meterialChart.draw(data, google.charts.Bar.convertOptions(options));
}


//to be shown on nutrition page for total data
function drawChart() {
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'Label');
	data.addColumn('number', 'Value');
	data.addRows(7);
	data.setValue(0, 0, 'Protein');
	data.setValue(0, 1, 50);

	data.setValue(1, 0, 'Fat');
	data.setValue(1, 1, 65);

	data.setValue(2, 0, 'SaturatedFattyAcids');
	data.setValue(2, 1, 20);

	data.setValue(3, 0, 'Carbohydrates');
	data.setValue(3, 1, 304);

	data.setValue(4, 0, 'Sugars');
	data.setValue(4, 1, 38);

	data.setValue(5, 0, 'Sodium');
	data.setValue(5, 1, 2.3);

	data.setValue(6, 0, 'DietaryFibre');
	data.setValue(6, 1, 25);

	var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
	
	//intervals are for random animation display
	setInterval(function() {
		data.setValue(0, 1, 50 +  10);
		 var options = {
			redFrom: 40, redTo: 100,
			yellowFrom:20, yellowTo: 40, width: 400, height: 621};
		chart.draw(data, options);
	  }, 1200);

	setInterval(function() {
		data.setValue(1, 1, 65 + 10);
		var options = {
			redFrom: 65, redTo: 100,
			yellowFrom:40, yellowTo: 65, width: 400, height: 621};
		chart.draw(data, options);
	  }, 5000);

	setInterval(function() {
		data.setValue(2, 1, 20 + Math.round(20 * Math.random()));
		var options = {
			redFrom: 20, redTo: 100,
			yellowFrom:15, yellowTo: 20, width: 400, height: 621};
		chart.draw(data, options);
	  }, 18000);

	  setInterval(function() {
		data.setValue(1, 1, 304 + Math.round(50 * Math.random()));
		var options = {
			redFrom: 90, redTo: 100,
			yellowFrom:80, yellowTo: 90, width: 400, height: 621};
		chart.draw(data, options);
	  }, 2500);

	setInterval(function() {
		data.setValue(1, 1, 38 + Math.round(30 * Math.random()));
		var options = {
			redFrom: 38, redTo: 100,
			yellowFrom:20, yellowTo: 38, width: 400, height: 621};		
		chart.draw(data, options);
	  }, 7000);

	setInterval(function() {
		data.setValue(2, 1, 2.3 + Math.round(70 * Math.random()));
		var options = {
			redFrom: 2.3, redTo: 100,
			yellowFrom:1, yellowTo: 2, width: 400, height: 621};
		chart.draw(data, options);
	  }, 5500);

	  setInterval(function() {
		data.setValue(2, 1, 25 + Math.round(60 * Math.random()));
		var options = {
			redFrom: 25, redTo: 100,
			yellowFrom:15, yellowTo: 25, width: 400, height: 621};
		chart.draw(data, options);
	  }, 2000);

	  chart.draw(data);
  }
  

//this function makes sure the change on memos page workes seperately on all entries.
var buttons = document.getElementsByClassName('buttons');
for (var i = 0; i < buttons.length; i++) {
	(function (ind) {
		buttons[ind].onclick = edit_button(ind);
	})(i)
}

//working as a front end / json updating the note entries.
function edit_button(ind) {
	document.querySelector(`#edit-view${ind}`).style.display = 'block';
	let x = document.querySelector(`#my_note${ind}`).innerHTML;
	document.querySelector(`#edited-my_note${ind}`).innerHTML = `${x}`;
	document.querySelector(`#edit-form${ind}`)
		.onsubmit = () => {
			fetch(`edit/memos/${ind}`, {
				method: 'POST',
				body: JSON.stringify({
					my_note: document.querySelector(`#edited-my_note${ind}`)
						.value,
				})
			})
				.then(response => response.json())
				.then(result => {
					console.log(result['my_note']);
					document.querySelector(`#edited-my_note-new${ind}`)
						.innerHTML = result[`my_note`];
				})
			return false;
		}
}