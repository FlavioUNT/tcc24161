document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const name = form.name.value.trim();
        const subject = form.subject.value.trim();
        const email = form.email.value.trim();
        const phone = form.phone.value.trim();
        const reason = form.reason.value.trim();
        const message = form.message.value.trim();
        const subscribe = form.subscribe.checked;
        //const attachment = form.attachment.value;

        if (!name) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, ingrese su nombre.'
            });
            return;
        }

        if (!subject) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, ingrese un asunto.'
            });
            return;
        }

        if (!email) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, ingrese su correo electrónico.'
            });
            return;
        }

        if (!phone) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, ingrese su número de teléfono.'
            });
            return;
        }

        if (!reason) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, seleccione una razón.'
            });
            return;
        }

        if (!message) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, ingrese un mensaje.'
            });
            return;
        }

        // if (!attachment) {
        //     Swal.fire({
        //         icon: 'error',
        //         title: 'Error',
        //         text: 'Por favor, adjunte una imagen.'
        //     });
        //     return;
        // }

        Swal.fire({
            icon: 'success',
            title: 'Formulario enviado',
            text: 'El formulario se ha enviado correctamente.'
        }).then(() => {
            form.submit();
        });
    });
});
