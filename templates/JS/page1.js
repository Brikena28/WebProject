const images = [
        "{% static 'IMG/all.jpeg' %}",
        "{% static 'IMG/1.jepg' %}",
        "{% static 'IMG/2.jepg' %}"
    ];

    let currentIndex = 0;

    function changeImage() {
        const imageElement = document.getElementById("dynamicImage");
        currentIndex = (currentIndex + 1) % images.length;
        imageElement.src = images[currentIndex];
    }

    // Ndrysho fotografinë çdo 5 sekonda
    setInterval(changeImage, 5000);