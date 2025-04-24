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
