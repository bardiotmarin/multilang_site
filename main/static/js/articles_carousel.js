var currentSlide = 0;
var carouselItems = document.querySelectorAll('.carousel-item');
var itemsPerPage = 6; 
var totalSlides = Math.ceil(carouselItems.length / itemsPerPage);

function showSlide(slideIndex) {
    var startIndex = slideIndex * itemsPerPage;
    var endIndex = startIndex + itemsPerPage;

    carouselItems.forEach(function(item, index) {
        if (index >= startIndex && index < endIndex) {
            item.style.display = 'inline-block';
        } else {
            item.style.display = 'none';
        }
    });

    currentSlide = slideIndex;
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    showSlide(currentSlide);
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    showSlide(currentSlide);
}

showSlide(currentSlide); // Afficher le premier ensemble d'articles au chargement de la page
