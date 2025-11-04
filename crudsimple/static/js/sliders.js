let currentIndex = 0; // Índice de la imagen actual
const slides = document.querySelector('.slides');
const totalSlides = document.querySelectorAll('.slide').length;

function showNextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides; // Incrementa el índice
    const offset = -currentIndex * 50; // Calcula el desplazamiento
    slides.style.transform = `translateX(${offset}%)`; // Desplaza las imágenes
}

setInterval(showNextSlide, 1000); // Cambia de imagen cada 3 segundos
