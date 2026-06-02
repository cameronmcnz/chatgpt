(function () {
  var AUTH_KEY = "xennialCourseAuth";
  var USERNAME = "xennial";
  var PASSWORD = "traice";

  function unlockSite() {
    document.documentElement.classList.remove("auth-locked");
    document.documentElement.classList.add("auth-ok");
  }

  function lockSite() {
    document.documentElement.classList.remove("auth-ok");
    document.documentElement.classList.add("auth-locked");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("auth-gate-form");
    var userInput = document.getElementById("auth-username");
    var passInput = document.getElementById("auth-password");
    var errorNode = document.getElementById("auth-gate-error");

    if (!form || !userInput || !passInput || !errorNode) {
      return;
    }

    try {
      if (localStorage.getItem(AUTH_KEY) === "ok") {
        unlockSite();
        return;
      }
    } catch (e) {
      // If localStorage is not available, continue with one-session gate.
    }

    lockSite();
    userInput.focus();

    form.addEventListener("submit", function (event) {
      event.preventDefault();

      var enteredUser = userInput.value.trim().toLowerCase();
      var enteredPass = passInput.value;

      if (enteredUser === USERNAME && enteredPass === PASSWORD) {
        try {
          localStorage.setItem(AUTH_KEY, "ok");
        } catch (e) {
          // Ignore storage failures and still unlock for current page load.
        }
        errorNode.textContent = "";
        unlockSite();
        return;
      }

      errorNode.textContent = "Incorrect username or password.";
      passInput.value = "";
      passInput.focus();
    });
  });
})();
