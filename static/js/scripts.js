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
    if (messages) {
        let alert = new bootstrap.Alert(messages);
        alert.close();
    } else {}
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

// Remove the existing click event handler
$(".slot").off("click");

// Add a new click event handler to show the corresponding form on click
$(".slot").on("click", function (e) {
  e.preventDefault();
  var formId = $(this).attr("id");
  $("#" + formId + "-form").show();
});

