document.addEventListener('DOMContentLoaded', function() {
    // Cargar y verificar los horarios en window.horarios
    try {
        window.horarios = JSON.parse(document.getElementById("horarios-data").dataset.horarios);
    } catch (error) {
        console.error("Error al analizar los datos de horarios:", error);
    }

    // Selección de formato e idioma
    document.getElementById('format-select').addEventListener('change', function() {
        const selectedFormat = this.value;
        const selectedLanguage = document.getElementById('language-select').value;
        window.location.href = `?format=${selectedFormat}&language=${selectedLanguage}`;
    });

    document.getElementById('language-select').addEventListener('change', function() {
        const selectedLanguage = this.value;
        const selectedFormat = document.getElementById('format-select').value;
        window.location.href = `?format=${selectedFormat}&language=${selectedLanguage}`;
    });

    const dayButtons = document.querySelectorAll(".day-button");
    const scheduleContainer = document.getElementById("schedule-container");

    // Función para mostrar los horarios disponibles
    function mostrarHorarios(fechaSeleccionada) {
        // Limpiar el contenedor de horarios
        scheduleContainer.innerHTML = "";

        // Verificar si hay horarios para la fecha seleccionada
        const horarios = window.horarios[fechaSeleccionada] || [];
        if (horarios.length > 0) {
            horarios.forEach(horario => {
                const horarioButton = document.createElement("button");
                horarioButton.className = "btn btn-outline-light me-2 horario-button";
                horarioButton.textContent = horario.show_time; // Mostrar la hora
                horarioButton.setAttribute("data-show-id", horario.show_id); // Añadir el show_id como atributo

                scheduleContainer.appendChild(horarioButton);
            });
        } else {
            // Mostrar mensaje si no hay horarios para el día seleccionado
            const noScheduleMsg = document.createElement("p");
            noScheduleMsg.textContent = "No hay horarios disponibles para la selección realizada.";
            noScheduleMsg.className = "text-light";
            scheduleContainer.appendChild(noScheduleMsg);
        }
    }

    // Manejador de evento para los botones de día
    dayButtons.forEach(button => {
        button.addEventListener("click", function() {
            dayButtons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");
            const fechaSeleccionada = button.getAttribute("data-day");
            mostrarHorarios(fechaSeleccionada);
        });
    });

    let selectedShowId = null; // Variable para almacenar el último show_id seleccionado

    // Manejador de evento para los botones de horarios
    scheduleContainer.addEventListener("click", function(event) {
        if (event.target && event.target.matches("button.horario-button")) {
            //cambio
            // Quitar la clase 'selected' de todos los botones
            const horarioButtons = document.querySelectorAll(".horario-button");
            horarioButtons.forEach(button => button.classList.remove("selected"));

            // Añadir la clase 'selected' al botón clickeado
            event.target.classList.add("selected");
            console.log("Clase 'selected' añadida al botón:", event.target);

            //cambio
            // Obtener el show_id seleccionado
            selectedShowId = event.target.getAttribute("data-show-id");
            console.log("Show ID seleccionado:", selectedShowId);
        }
    });

    // Manejador de evento para el botón de "Comprar Entrada"
    const comprarButton = document.querySelector(".btn.btn-red");

    comprarButton.addEventListener("click", function(event) {
        if (selectedShowId) { // Verifica que haya un show_id seleccionado
            // Redirige a la URL usando el show_id almacenado
            window.location.href = `/comprar_entradas/${selectedShowId}/`;
        } else {
            alert("Por favor, selecciona un horario antes de comprar una entrada.");
        }
    });
});

// Video de YouTube
// Función para extraer el ID del video de un enlace de YouTube
function extractYouTubeID(url) {
    const regex = /(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
    const match = url.match(regex);
    return match ? match[1] : null;
}

// Selecciona todos los contenedores de videos
const videoContainers = document.querySelectorAll('#video-container');

// Itera sobre cada contenedor de video y agrega un iframe si el enlace es válido
videoContainers.forEach(videoContainer => {
    const videoLink = videoContainer.getAttribute('data-video-link');
    const videoId = extractYouTubeID(videoLink);

    // Crear el iframe solo si hay un ID de video válido
    if (videoId) {
        const iframe = document.createElement("iframe");
        iframe.src = `https://www.youtube.com/embed/${videoId}`;
        iframe.classList.add("embed-responsive-item");
        iframe.setAttribute("allowfullscreen", "");
        videoContainer.appendChild(iframe);
    } else {
        console.error("No se pudo obtener un ID de video válido de YouTube.");
    }
});


