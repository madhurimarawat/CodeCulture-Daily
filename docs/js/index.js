//
//*********************************************************************************************
//* File: index.js
//* Author: Madhurima Rawat
//* Date: October 10, 2024
//* Description: JavaScript functionality for the main page of the CodeCulture Daily platform,
//*               providing smooth scrolling behavior for navigation links, enhancing user
//*               experience and interaction with the page content.
//* Version: 1.0
//* GitHub Repository: https://github.com/madhurimarawat/CodeCulture-Daily
//* Issues/Bugs: For any issues or bugs, please visit the GitHub repository's [Issues](https://github.com/madhurimarawat/CodeCulture-Daily/issues) section.
//* Comments: This script includes event listeners for navigation links, calculates target
//*           positions for smooth scrolling, and adjusts scroll behavior based on the device type.
//* Dependencies:
//*   - **Bootstrap 4.5.2**: External CSS framework for responsive design and pre-built components.
//* Design Notes:
//*   - **Smooth Scrolling**: The smooth scroll effect enhances navigation by providing a
//*     visually appealing transition when users click on navigation links.
//*   - **Responsive Behavior**: Adjustments are made to scrolling behavior for mobile devices,
//*     ensuring a seamless experience across different screen sizes.
//*********************************************************************************************
//

// Smooth scroll to the Problems section
document.querySelector('.nav-link[href="#problems"]').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent default anchor click behavior

    // Get the target section
    const targetSection = document.getElementById('problems');

    // Calculate the target position with an offset for the navbar
    const navbarHeight = document.querySelector('.navbar').offsetHeight;

    // Determine if the device is mobile
    const isMobile = window.innerWidth <= 768; // Adjust the breakpoint as needed

    // Set padding values based on the device type
    const padding = isMobile ? -95 : 15; // No padding for mobile, 15px for desktop

    // Calculate the section position based on device type
    const sectionPosition = targetSection.getBoundingClientRect().top + window.scrollY - navbarHeight - padding;

    // Smoothly scroll to the adjusted position
    window.scrollTo({
        top: sectionPosition,
        behavior: isMobile ? 'auto' : 'smooth' // Instant scroll for mobile, smooth for desktop
    });
});
