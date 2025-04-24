
function updateCountdown() {
    fetch('/countdown')
        .then(response => response.json())
        .then(data => {
            document.getElementById("days").innerText = data.days;
            document.getElementById("hours").innerText = data.hours;
            document.getElementById("minutes").innerText = data.minutes;
            document.getElementById("seconds").innerText = data.seconds;
        });
}

setInterval(updateCountdown, 1000);


function startCountdown() {
    document.getElementById('loading-spinner').style.display = 'none';
    document.getElementById('countdown').style.display = 'block';
    document.getElementById('waiting').style.display = 'block';
}

setTimeout(startCountdown, 2000); 
