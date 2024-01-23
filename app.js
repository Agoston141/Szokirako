document.addEventListener("DOMContentLoaded", function() {
  var header = document.getElementById("heading");
  var word = "Betűvarázs";
  var index = 0;
  var interval = setInterval(function() {
    header.textContent += word[index];
    index++;
    if (index === word.length) {
      clearInterval(interval);
    }
  }, 250);
});


