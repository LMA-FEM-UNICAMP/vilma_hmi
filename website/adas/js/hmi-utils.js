const HMI = (function () {

  // private state
  let isBlinking = false;
  const alertSound = new Audio("assets/notification.wav");
  const warningSound = new Audio("assets/warning.mp3");

  function startBlinking() {
    if (isBlinking) return;
    isBlinking = true;
    document.body.classList.add("blink-warning");
  }

  function stopBlinking() {
    isBlinking = false;
    document.body.classList.remove("blink-warning");
  }

  function playAlertSound() {
    alertSound.currentTime = 0;
    alertSound.play().catch(() => {});
  }

  function playWarningLoop() {
    warningSound.loop = true;
    warningSound.currentTime = 0;
    warningSound.play().catch(() => {});
  }

  function stopWarningLoop() {
  warningSound.pause();
  warningSound.currentTime = 0;
  warningSound.loop = false;
  }   

  function showNotification(message, type = "default", timeout = 4000) {
  const notif = document.getElementById("notification");
  const msg = document.getElementById("notification-message");

  if (!notif || !msg) return;

  // update content
  msg.innerText = message;

  // reset classes
  notif.classList.remove("warning", "error");
  if (type !== "default") notif.classList.add(type);

  // show
  notif.classList.remove("hidden");

  // auto-hide
  if (timeout > 0) {
    clearTimeout(notif._timeout);
    notif._timeout = setTimeout(hideNotification, timeout);
  }
}

function hideNotification() {
  const notif = document.getElementById("notification");
  if (!notif) return;

  notif.classList.add("hidden");
}

// --- INIT / EVENT BINDING ---
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("notification-close");
  if (btn) btn.onclick = hideNotification;
});

  // public API
  return {
    startBlinking,
    stopBlinking,
    playAlertSound,
    playWarningLoop,
    stopWarningLoop,
    showNotification,
    hideNotification
  };

})();

// initialize when DOM is ready
document.addEventListener("DOMContentLoaded", HMI.init);