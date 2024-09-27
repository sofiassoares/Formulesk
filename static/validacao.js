document.addEventListener('DOMContentLoaded', function () {
    console.log('esta carrengando');

    function validarTitulo() {
        const campoTitulo = document.getElementById('titulo');
        const erroTitulo = document.getElementById('erro-titulo');
        
        console.log(campoTitulo.value.length); 

        if (campoTitulo.value.length > 200) {
            erroTitulo.style.display = 'block'; 
            return false;
        } else {
            erroTitulo.style.display = 'none';  
            return true; 
        }
    }

    const formulario = document.querySelector('form');
    formulario.addEventListener('submit', function (evento) {
        if (!validarTitulo()) {
            evento.preventDefault();
            alert('O título não pode ter mais de 200 caracteres!');
        }
    });
});
