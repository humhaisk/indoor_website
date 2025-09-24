document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".about-container section");

    const revealOnScroll = () => {
        const triggerBottom = window.innerHeight * 0.8;
        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top < triggerBottom) {
                section.classList.add("visible");
            }
        });
    };

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll();
});