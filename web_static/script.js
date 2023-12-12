function myFunction() {
    document.getElementById("dropdownContent").classList.toggle("show");
  }

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropdown-toggle')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  } 

  const logoutButton = document.querySelector('.logout-button');

  logoutButton.addEventListener('click', function(e) {
    e.preventDefault();
    window.location.href = 'login.html';
  });1