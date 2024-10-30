// Función para mostrar la sinopsis en el modal
const sinopsisModal = document.getElementById('sinopsisModal');
sinopsisModal.addEventListener('show.bs.modal', (event) => {
    // Obtener el botón que abrió el modal
    const button = event.relatedTarget;

    // Extraer la sinopsis y el título de la película del botón
    const sinopsis = button.getAttribute('data-sinopsis');
    const titulo = button.parentElement.querySelector('h5').textContent;

    // Actualizar el contenido del modal
    const modalBody = sinopsisModal.querySelector('.modal-body');
    modalBody.textContent = sinopsis;

    // Actualizar el título del modal
    const modalTitle = sinopsisModal.querySelector('.modal-title');
    modalTitle.textContent = titulo;
});
