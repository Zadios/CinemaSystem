// Seleccionar todos los botones de suma y resta
const minusButtons = document.querySelectorAll(".btn-minus");
const plusButtons = document.querySelectorAll(".btn-plus");

// Función para actualizar la cantidad mostrada
function updateQuantityDisplay(display, summaryDisplay, increment) {
    let currentValue = parseInt(display.textContent);

    // Ajustar el valor dentro del rango permitido (0 a 10)
    const newValue = Math.max(0, Math.min(10, currentValue + increment));
    display.textContent = newValue;

    // Actualizar la cantidad en el resumen
    summaryDisplay.textContent = newValue;

    // Actualizar el valor del input oculto
    const hiddenInput = display.closest(".price-bar").querySelector(".quantity-input");
    hiddenInput.value = newValue; // Actualiza el valor del input oculto con la nueva cantidad

    // Actualizar los totales
    updateTotals();
}

// Función para calcular el total de dinero y entradas
function updateTotals() {
    let totalAmount = 0;
    let totalTickets = 0;

    // Seleccionar cada promoción y sumar sus valores en base a la cantidad seleccionada
    document.querySelectorAll(".price-summary").forEach(summary => {
        const quantity = parseInt(summary.querySelector(".quantity-display-summary").textContent);
        const amount = parseFloat(summary.getAttribute("data-amount"));
        const ticketQuantity = parseInt(summary.getAttribute("data-ticket-quantity"));

        // Actualizar total de dinero y total de entradas
        totalAmount += quantity * amount;
        totalTickets += quantity * ticketQuantity;
    });

    // Actualizar el HTML de los totales
    document.getElementById("total-payment").textContent = `Total a pagar: $${totalAmount}`;
    document.getElementById("total-tickets").textContent = `Total de entradas: ${totalTickets}`;
}

// Asignar eventos a los botones de restar
minusButtons.forEach((button, index) => {
    button.addEventListener("click", function () {
        // Buscar el display en el mismo contenedor de precio
        const display = this.closest(".price-bar").querySelector(".quantity-display");
        
        // Buscar el display en el resumen
        const summaryDisplay = document.querySelector(`#summary-price-${index} .quantity-display-summary`);
        
        updateQuantityDisplay(display, summaryDisplay, -1); // Disminuir en 1
    });
});

// Asignar eventos a los botones de sumar
plusButtons.forEach((button, index) => {
    button.addEventListener("click", function () {
        // Buscar el display en el mismo contenedor de precio
        const display = this.closest(".price-bar").querySelector(".quantity-display");

        // Buscar el display en el resumen
        const summaryDisplay = document.querySelector(`#summary-price-${index} .quantity-display-summary`);
        
        updateQuantityDisplay(display, summaryDisplay, 1); // Aumentar en 1
    });
});
