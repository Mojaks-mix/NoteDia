// Dropdown Menu Function
const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;


//Theme Toggle
const toggle = document.querySelector('#toggle-theme');
const storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

if (storedTheme)
    document.documentElement.setAttribute('data-theme', storedTheme)

toggle.onclick = function() {
    const currentTheme = document.documentElement.getAttribute("data-theme");

    const targetTheme =  currentTheme === 'dark' ? 'light' : 'dark';

    document.documentElement.setAttribute('data-theme', targetTheme)
    localStorage.setItem('theme', targetTheme);
};


//Header visibility function
var prevScrollPos = window.pageYOffset || document.documentElement.scrollTop;
var header = document.getElementById('header');

window.addEventListener('scroll', function() {
  var currentScrollPos = window.pageYOffset || document.documentElement.scrollTop;

  if (prevScrollPos > currentScrollPos) {
    header.classList.remove('hidden');
    header.classList.add('visible');
  } else {
    header.classList.remove('visible');
    header.classList.add('hidden');
  }
  prevScrollPos = currentScrollPos;
});


var form_fields = document.getElementsByTagName('input');
for (var field in form_fields){	
  form_fields[field].className += ' input-field '
}

var form_DropDown = document.getElementsByTagName('select');
for (var field in form_DropDown ){	
  form_DropDown[field].className += ' DropDownList '
}


// rate room
// Get the room elements
// Load the user's ratings from storage or set default values
const ratingInputs = document.querySelectorAll('input[name="rating"]');
const userRatings = JSON.parse(localStorage.getItem('userRatings')) || {};



// Function to handle rating change
function handleRatingChange(event) {
  const rating = event.target.value;
  const room = event.target.closest('.room');
  const roomId = room.dataset.roomId; // Get the room ID from the dataset

  // Update the user's rating for the specific room in the userRatings object
  userRatings[roomId] = rating;

  // Save the updated user's ratings to local storage
  localStorage.setItem('userRatings', JSON.stringify(userRatings));
}

// Function to initialize the ratings for each room
function initializeRatings() {
  ratingInputs.forEach((input) => {
    const room = input.closest('.room');
    const roomId = room.dataset.roomId; // Get the room ID from the dataset

    // Check if the user has a saved rating for the specific room in the userRatings object
    if (userRatings.hasOwnProperty(roomId)) {
      const rating = userRatings[roomId];
      if (input.value === rating) {
        input.checked = true;
        room.querySelectorAll('label').forEach((label) => {
          label.classList.add('active');
        });
      }
    } else {
      input.checked = false; // Uncheck the input if no rating is found
    }

    // Attach event listeners to handle rating change
    input.addEventListener('change', handleRatingChange);
  });
}

// Call the initializeRatings function on page load
initializeRatings();




// Rating Functionality

if (ratingInputs) {
  ratingInputs.forEach((input) => {
    input.addEventListener("change", () => {
      input.closest("form").submit();
    });
  });
}

// Call the initializeRatings function on page load
initializeRatings();

//error message disappear after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
  var messages = document.querySelector('.error-messages');
  if (messages) {
    // Hide messages after 5 seconds with a smooth fade-out effect
    setTimeout(function() {
      messages.style.opacity = '0';
      setTimeout(function() {
        messages.style.display = 'none';
      }, 500); // Wait for the fade-out transition to complete before hiding the element
    }, 5000);
  }
});

document.addEventListener('DOMContentLoaded', function() {
  var messages = document.querySelector('.success-messages');
  if (messages) {
    // Hide messages after 5 seconds with a smooth fade-out effect
    setTimeout(function() {
      messages.style.opacity = '0';
      setTimeout(function() {
        messages.style.display = 'none';
      }, 500); // Wait for the fade-out transition to complete before hiding the element
    }, 5000);
  }
});


//Hide upload media button from room form
document.getElementById('file_upload_button').addEventListener('click', function() {
  document.getElementById('id_media_file').click();
});

//Display file name on attach a file button
document.getElementById('id_media_file').addEventListener('change', function() {
  var fileInput = this;
  var fileName = fileInput.value.split('\\').pop(); // Extract the file name from the file path

  if (fileName) {
    // Display the file name
    document.getElementById('file_name').textContent = fileName;

  } else {
    // No file selected
    document.getElementById('file_name').textContent = 'No file selected';
  }
});