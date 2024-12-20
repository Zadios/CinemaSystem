document.addEventListener('DOMContentLoaded', function () {
    const cvvInput = document.querySelector('input[name="cvv"]');
    cvvInput.addEventListener('input', function (e) {
        // Permitir solo números y limitar a 3 caracteres
        this.value = this.value.replace(/[^0-9]/g, '').slice(0, 3);
    });

    const fechaInput = document.querySelector('input[name="fecha_caducidad"]');

    fechaInput.addEventListener('input', function (e) {
        let value = this.value.replace(/[^0-9]/g, ''); // Elimina cualquier carácter no numérico
        if (value.length > 2) {
            value = value.slice(0, 2) + '/' + value.slice(2, 6); // Agrega la "/"
        }
        this.value = value.slice(0, 7); // Limita el número de caracteres a 7
    });

    fechaInput.addEventListener('blur', function (e) {
        // Validar que la fecha tenga el formato correcto cuando el usuario salga del campo
        const regex = /^(0[1-9]|1[0-2])\/\d{4}$/;
        if (!regex.test(this.value)) {
            this.value = ''; // Vacía el campo si el formato es incorrecto
        }
    });
});
