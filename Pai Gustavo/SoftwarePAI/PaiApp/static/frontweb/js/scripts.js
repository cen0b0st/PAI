// Email
function chequeoEmail(input) {
    var valor = input.value.substr(-12)
    if (valor != "@cenabast.cl") {
        input.setCustomValidity("Correo invalido");
        document.getElementById('email').style.borderColor = '#ff0000';
        return false;

    } else if (input.validity.patternMismatch) {
        input.setCustomValidity("Correo invalido");
        document.getElementById('email').style.borderColor = '#ff0000';
        return false;
    } else {
        input.setCustomValidity("");
        document.getElementById('email').style.borderColor = '#2aff00 ';
    }
}

// VALIDA RUT
function chequeoRut(rut) {
    // Despejar Puntos
    var valor = rut.value.replace('.', '');
    // Despejar Guión
    valor = valor.replace('-', '');
    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();
    // Formatear RUN
    rut.value = cuerpo + '-' + dv
        // Si no cumple con el mínimo ej. (n.nnn.nnn)
    if (cuerpo.length < 1) {
        rut.setCustomValidity("RUT Incompleto");
        document.getElementById('rut').style.borderColor = '#ff0000';
        return false;
    }

    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;

    // Para cada dígito del Cuerpo
    for (i = 1; i <= cuerpo.length; i++) {
        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * valor.charAt(cuerpo.length - i);
        // Sumar al Contador General
        suma = suma + index;
        // Consolidar Múltiplo dentro del rango [2,7]
        if (multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }
    }

    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11);
    // Casos Especiales (0 y K)
    dv = (dv == 'K') ? 10 : dv;
    dv = (dv == 0) ? 11 : dv;

    // Validar que el Cuerpo coincide con su Dígito Verificador
    if (dvEsperado != dv) {
        rut.setCustomValidity("RUT Inválido");
        document.getElementById('rut').style.borderColor = '#ff0000';
        return false;
    } else {
        rut.setCustomValidity('');
        document.getElementById('rut').style.borderColor = '#2aff00'
    }
}

// FUNCION CIERRE MENSUAL
function mensualclose() {
    const fecha = new Date();
    const mesActual = fecha.toLocaleDateString("es-AS", {
        month: "long"
    });
    let obtenerDatos = document.getElementsByTagName('td');
    let insumoid = []
    var id = ""
    for (let i = 5; i < obtenerDatos.length; i += 7) {
        insumoid.push(obtenerDatos[i]);
    }
    for (let i = 0; i < insumoid.length; i++) {
        id = id + "_" + insumoid[i].getAttribute('id');
    }
    $.ajax({
        url: window.location.pathname,
        type: "POST",
        data: {
            action: "enviar_cierre",
            id: id,
        },
        dataType: "json",
    });
    alert('Atencion!\nSe ha INGRESADO el cierre mensual correspondiente al mes de ' + mesActual.toUpperCase());
}