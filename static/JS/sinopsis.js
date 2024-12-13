document.addEventListener("DOMContentLoaded", function() {
    const sinopsisModal = document.getElementById('sinopsisModal');
    if (sinopsisModal) {
        sinopsisModal.addEventListener('show.bs.modal', (event) => {
            const button = event.relatedTarget;
            const sinopsis = button.getAttribute('data-sinopsis');
            const titulo = button.parentElement.querySelector('h5').textContent;

            const modalBody = sinopsisModal.querySelector('.modal-body');
            modalBody.textContent = sinopsis;

            const modalTitle = sinopsisModal.querySelector('.modal-title');
            modalTitle.textContent = titulo;
        });
    }
});
