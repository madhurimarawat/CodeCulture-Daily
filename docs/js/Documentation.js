//
//*********************************************************************************************
//* File: documentation.js
//* Author: Madhurima Rawat
//* Date: October 10, 2024
//* Description: JavaScript functionality for the documentation page of the CodeCulture Daily
//*               platform, providing smooth scrolling behavior for dropdown menu links to enhance
//*               user navigation and improve content accessibility.
//* Version: 1.0
//* GitHub Repository: https://github.com/madhurimarawat/CodeCulture-Daily
//* Issues/Bugs: For any issues or bugs, please visit the GitHub repository's [Issues](https://github.com/madhurimarawat/CodeCulture-Daily/issues) section.
//* Comments: This script attaches smooth scrolling functionality to dropdown menu links,
//*           calculating target section positions with appropriate offsets for mobile and desktop
//*           devices to ensure an optimal user experience.
//* Dependencies:
//*   - **Bootstrap 4.5.2**: External CSS framework for responsive design and dropdown components.
//* Design Notes:
//*   - **Smooth Scrolling**: Enhances user experience by providing a smooth transition to
//*     the selected section, improving readability and navigation efficiency.
//*   - **Responsive Behavior**: Adjusts scrolling behavior based on device type, ensuring
//*     usability across various screen sizes and orientations.
//*********************************************************************************************
//

// This Function handles the smooth scrolling functionality for the dropdown menu
document.addEventListener("DOMContentLoaded", function () {
    // Function to handle smooth scrolling with offset
    function smoothScroll(event) {
        // Prevent default anchor click behavior
        event.preventDefault();

        // Get the target section ID from the href attribute
        const targetId = this.getAttribute("href").substring(1);
        const targetSection = document.getElementById(targetId);

        if (targetSection) {
            // Calculate the position to scroll to
            const navbarHeight = document.querySelector(".navbar").offsetHeight;

            // Define minimal paddings for mobile and desktop
            const mobilePadding = -420; // Set to 0 for no padding on mobile
            const desktopPadding = 40; // Very minimal padding for desktop

            // Determine if the device is mobile
            const isMobile = window.innerWidth <= 768; // Change 768 to the desired breakpoint for mobile

            // Calculate target position based on device type
            const padding = isMobile ? mobilePadding : desktopPadding;

            // Calculate the target position
            const targetPosition = targetSection.getBoundingClientRect().top + window.pageYOffset - navbarHeight - padding;

            // Log values for debugging
            console.log(`Target Section: ${targetId}`);
            console.log(`Navbar Height: ${navbarHeight}`);
            console.log(`Padding: ${padding}`);
            console.log(`Calculated Target Position: ${targetPosition}`);

            // Smoothly scroll to the target position
            window.scrollTo({
                top: targetPosition,
                behavior: isMobile ? "auto" : "smooth" // Instant scroll for mobile, smooth for desktop
            });
        } else {
            console.error(`No target section found for ID: ${targetId}`);
        }
    }

    // Select all dropdown menu links
    const dropdownLinks = document.querySelectorAll(".dropdown-item");

    // Attach the smoothScroll function to each dropdown link
    dropdownLinks.forEach(function (link) {
        link.addEventListener("click", smoothScroll);
    });
});
