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

    // Función para limpiar y mostrar los horarios disponibles
    function mostrarHorarios(fechaSeleccionada) {
        // Limpiar el contenedor de horarios
        scheduleContainer.innerHTML = "";

        // Verificar si hay horarios para la fecha seleccionada
        const horarios = window.horarios[fechaSeleccionada] || [];
        if (horarios.length > 0) {
            horarios.forEach(horario => {
                const horarioButton = document.createElement("button");
                horarioButton.className = "btn btn-outline-light me-2";
                horarioButton.textContent = horario.time;

                // Agregar el data-show-id con el id del show correspondiente
                horarioButton.setAttribute("data-show-id", horario.show_id);

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

    // Función para manejar el clic en los botones de día
    dayButtons.forEach(button => {
        button.addEventListener("click", function() {
            // Remover la clase 'active' de todos los botones de día
            dayButtons.forEach(btn => btn.classList.remove("active"));
            // Agregar la clase 'active' al botón seleccionado
            button.classList.add("active");

            // Obtener la fecha seleccionada del botón
            const fechaSeleccionada = button.getAttribute("data-day");
            // Mostrar los horarios para la fecha seleccionada
            mostrarHorarios(fechaSeleccionada);
        });
    });

    // Función para manejar el clic en los botones de horarios
    scheduleContainer.addEventListener("click", function(event) {
        if (event.target && event.target.matches("button")) {
            // Obtener el show_id desde el atributo data-show-id del botón
            const showId = event.target.getAttribute("data-show-id");

            // Mostrar el show_id en la consola
            console.log("Show ID seleccionado:", showId);

            // Aquí puedes guardar o procesar el showId, por ejemplo, almacenarlo en la sesión o en un campo oculto
        }
    });
});

// Video de YouTube
// Obtén el enlace completo del video desde el atributo de datos en el contenedor
const videoContainer = document.getElementById('video-container');
const videoLink = videoContainer.getAttribute('data-video-link');

// Función para extraer el ID del video de un enlace de YouTube
function extractYouTubeID(url) {
    const regex = /(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
    const match = url.match(regex);
    return match ? match[1] : null;
}

const videoId = extractYouTubeID(videoLink);

// Crear el iframe solo si hay un ID de video válido
if (videoId) {
    const iframe = document.createElement('iframe');
    iframe.className = 'embed-responsive-item';
    iframe.src = `https://www.youtube.com/embed/${videoId}`;
    iframe.frameBorder = '0';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope';
    iframe.allowFullscreen = true;

    videoContainer.appendChild(iframe);
} else {
    console.error('No se encontró un ID de video válido en el enlace proporcionado.');
}
