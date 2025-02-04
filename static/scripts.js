// Smooth scrolling for navigation links within the page
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Dynamic text animation in the hero section
document.addEventListener('DOMContentLoaded', (event) => {
    const dynamicText = document.getElementById('dynamicText');
    const textArray = [
        "A passionate tech enthusiast...",
        "Expert in Python, Java, C...",
        "Skilled in AI and cloud computing...",
        "Loves to create innovative projects..."
    ];
    let textIndex = 0;
    let charIndex = 0;

    function typeText() {
        if (charIndex < textArray[textIndex].length) {
            dynamicText.textContent += textArray[textIndex].charAt(charIndex);
            charIndex++;
            setTimeout(typeText, 100);
        } else {
            setTimeout(deleteText, 2000);
        }
    }

    function deleteText() {
        if (charIndex > 0) {
            dynamicText.textContent = textArray[textIndex].substring(0, charIndex - 1);
            charIndex--;
            setTimeout(deleteText, 50);
        } else {
            textIndex = (textIndex + 1) % textArray.length;
            setTimeout(typeText, 500);
        }
    }

    typeText();
});
