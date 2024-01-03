
function openNav() {
  document.getElementById("respnavbar").style.width = "100%";
  document.getElementById("open").style.display = "none";
}

function closeNav() {
  document.getElementById("respnavbar").style.width = "0";
    document.getElementById("open").style.display = "block";

}

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  // 80 is an arbitrary number here, just to make you think if you need the prevScrollpos variable:
  if (currentScrollPos > 80) {
    // I am using 'display' instead of 'top':
 document.getElementById("goTop").style.display = "block";

  }
  else {
 document.getElementById("goTop").style.display = "none";


  }

}



