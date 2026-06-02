document.addEventListener("DOMContentLoaded", function () {
  var revealItems = document.querySelectorAll(".reveal-up");
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.16 }
    );
    revealItems.forEach(function (item) {
      observer.observe(item);
    });
  } else {
    revealItems.forEach(function (item) {
      item.classList.add("is-visible");
    });
  }

  var counters = document.querySelectorAll("[data-counter]");
  counters.forEach(function (counter) {
    var target = parseInt(counter.getAttribute("data-counter"), 10);
    if (!Number.isFinite(target)) {
      return;
    }
    var value = 0;
    var increment = Math.max(1, Math.round(target / 30));
    var timer = setInterval(function () {
      value += increment;
      if (value >= target) {
        value = target;
        clearInterval(timer);
      }
      counter.textContent = value + (target >= 40 ? "+" : "");
    }, 24);
  });

  var currentPath = window.location.pathname.replace(/\/$/, "");
  if (currentPath === "") {
    currentPath = "/";
  }

  document.querySelectorAll(".navbar .nav-link").forEach(function (link) {
    var href = link.getAttribute("href");
    if (!href) {
      return;
    }

    if (href.indexOf("http") === 0 || href.indexOf("#") === 0) {
      return;
    }

    var normalized = href.replace(/\/$/, "");
    if (normalized === "") {
      normalized = "/";
    }

    var isExactMatch = normalized === currentPath;
    var isSectionMatch = normalized !== "/" && currentPath.indexOf(normalized + "/") === 0;

    if (isExactMatch || isSectionMatch) {
      link.classList.add("active");
    }
  });
});
