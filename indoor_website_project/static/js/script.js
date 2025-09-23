// Countdown Timer for Hero Section
function startCountdown(targetDate) {
    const countdownEl = document.getElementById('countdown');
    const interval = setInterval(() => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        countdownEl.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        if (distance < 0) {
            clearInterval(interval);
            countdownEl.innerHTML = "MATCH HAS BEGUN!";
        }
    }, 1000);
}

// Set a target date (e.g., 3 days from now)
const targetDate = new Date();
targetDate.setDate(targetDate.getDate() + 3);
startCountdown(targetDate);