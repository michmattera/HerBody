/*!
 * Start Bootstrap - Agency v7.0.12 (https://startbootstrap.com/theme/agency)
 * Copyright 2013-2023 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
 */
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});


// dropdown navigation links
$(document).ready(function () {
    $('.dropdown-toggle').dropdown()
});

// function to set a timeout for messages
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);


let map;

function initMap(data) {
        const gym = {
        lat: 20.659698,
        lng: -103.349609
    };
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: gym,
    });
    const marker = new google.maps.Marker({
        position: gym,
        map: map,
    });

}
//   function initMap() {
//     const gym = {
//         lat: -25.344,
//         lng: 131.031
//     };
//     const map = new google.maps.Map(document.getElementById("map"), {
//         zoom: 4,
//         center: gym,
//     });
//     const marker = new google.maps.Marker({
//         position: gym,
//         map: map,
//     });
// }

document.addEventListener("DOMContentLoaded", function() {
    // Get the available dates from the server
    var availableDates = ["2023-07-05", "2023-07-10", "2023-07-15"];
    
    // Calculate the date range (next 6 days)
    var today = new Date();
    var endRange = new Date();
    endRange.setDate(today.getDate() + 6);
    
    // Initialize the datepicker
    var datepicker = document.getElementById("datepicker");
    datepicker.addEventListener("focus", function() {
      // Show the datepicker when the input is focused
      var options = {
        dateFormat: "yy-mm-dd",
        minDate: today,
        maxDate: endRange,
        beforeShowDay: function(date) {
          var formattedDate = formatDate(date);
          if (availableDates.includes(formattedDate)) {
            // The date is available
            return [true, "available-date", "Available"];
          } else {
            // The date is unavailable
            return [false, "unavailable-date", "Unavailable"];
          }
        },
        onSelect: function(dateText, inst) {
          // Set the selected date to the input value
          datepicker.value = dateText;
        }
      };
      
      jQuery(datepicker).datepicker(options);
    });
  
    // Format date as "yyyy-mm-dd"
    function formatDate(date) {
      var year = date.getFullYear();
      var month = ("0" + (date.getMonth() + 1)).slice(-2);
      var day = ("0" + date.getDate()).slice(-2);
      return year + "-" + month + "-" + day;
    }
  });
  