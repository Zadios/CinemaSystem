// JavaScript para manejar el popup de sinopsis
document.addEventListener('DOMContentLoaded', function() {
    var modal = document.querySelector('.sinopsis-modal');
    var closeModal = document.querySelector('.sinopsis-modal .close');
    var buttons = document.querySelectorAll('.VerSinopsis');

    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var synopsis = this.dataset.synopsis;
            modal.querySelector('p').textContent = synopsis;
            modal.style.display = 'block';
        });
    });

    closeModal.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});
