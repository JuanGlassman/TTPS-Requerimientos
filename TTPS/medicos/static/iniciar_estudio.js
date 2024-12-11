const parentescoId = document.getElementById('parentescoId');
const sospechaId = document.getElementById('sospechaId');

var datap;
var statusCode;

const sintomasInput = document.getElementById('buscador-sintomas')
const sintomasSelect = document.getElementById('select-sintomas')
const divSintomasSeleccionados = document.getElementById('sintomas-seleccionados')
var valores = [];  

sintomasInput.addEventListener('input', function(e) {        
    if (sintomasInput.value.length > 3) {
        fetch(`https://api.claudioraverta.com/lista-sintomas/?nombre=${sintomasInput.value}`)
        .then(response => response.json())
        .then(data => {
            sintomasSelect.innerHTML = '';
            const optionDefault = document.createElement('option');
            optionDefault.textContent = "Elegir síntoma"
            sintomasSelect.appendChild(optionDefault);
            sintomasSelect[0].disabled = true 
            data.results.forEach(sintoma => {
                const option = document.createElement('option');
                option.value = sintoma.id;
                option.textContent = sintoma.nombre;
                sintomasSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error al obtener los síntomas:', error);
        });
    }
});

sintomasSelect.addEventListener('change', function(e) {
    e.preventDefault()
    if (!valores.some(s => s.id === e.target.value)) {
        const nuevoSintoma = {
            id: e.target.value,
            nombre: sintomasSelect.querySelector(`option[value="${e.target.value}"]`).innerHTML
        };
        valores.push(nuevoSintoma);        

        const chip = document.createElement('span');
        chip.className = "badge rounded-pill text-bg-primary me-2";
        chip.textContent = sintomasSelect.querySelector(`option[value="${e.target.value}"]`).innerHTML;

        const closeBtn = document.createElement('a');
        const icon = document.createElement('i');
        icon.className = "bi bi-x-lg ml-2 delete-sintoma";
        icon.id = e.target.value;

        closeBtn.appendChild(icon)
        chip.appendChild(closeBtn)
        divSintomasSeleccionados.appendChild(chip);
    }
});

document.addEventListener('click', function(e) {
    if (e.target.classList.contains('delete-sintoma')) {
        valores = valores.filter((s) =>  s.id !== e.target.id);
        const chip = e.target.closest('.badge');
        if (chip) {
            chip.remove();
        }
    }
});

const patologiaSelect = document.getElementById('patologia-select');
const gen_div = document.getElementById('gen-analizar');

var nombrePatologia;

patologiaSelect.addEventListener('change', function(e) {
    nombrePatologia = patologiaSelect.querySelector(`option[value="${e.target.value}"]`).innerHTML;
    fetch(`https://api.claudioraverta.com/genes-analizar/${nombrePatologia}`)
    .then(response => {
        statusCode = response.status;
        return response.json()
    })
    .then(data => {
        datap = data; 
        if (statusCode == 200) {
            gen_div.innerHTML = data.gen;
            gen_div.className = "badge text-bg-success"
            console.log(data);
        }
        else {
            gen_div.innerHTML = data.error;
            console.log(data);
        }     
    })
    .catch(error => {
        debugger;
        errorp = error;
        gen_div.innerHTML = "Hubo problemas para conectarse a los servicios. Intente nuevamente más tarde."
        console.error('Error:', error);
    });
});

sospechaId.addEventListener('change', function(e) {
    if (sospechaId.value == '1') {
        parentescoId.style = "display: block;"
    }
    else {
        parentescoId.style = "display: none;"
    }
});

document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault(); // Detiene el envío del formulario
 
    const formData = new FormData(e.target);      

    if (await validarForm(formData)) {

        // Crear input hidden
        const inputSintomas = document.createElement('input');
        inputSintomas.type = 'hidden';
        inputSintomas.name = 'sintomas';
        inputSintomas.value = JSON.stringify(valores);
        this.appendChild(inputSintomas);

        const inputGenes = document.createElement('input');
        inputSintomas.type = 'hidden';
        inputSintomas.name = 'genes';
        inputSintomas.value = JSON.stringify(genes);
        this.appendChild(inputGenes);

        const inputPatologia = document.createElement('input');
        inputPatologia.type = 'hidden';
        inputPatologia.name = 'patologia_nombre';
        inputPatologia.value = patologiaSelect.querySelector(`option[value="${formData.get('patologia')}"]`).innerHTML;
        this.appendChild(inputPatologia);

        this.submit(); // Envía el formulario
    };     
 });

async function validarForm(formData) {
    if (!validarSintomas()) return false
    if (!validarPatologia(formData.get('patologia'))) return false
    if (!validarSospecha(formData.get('sospecha'), formData.get('parentesco'))) return false
    if (formData.get('sospecha') === "0") {
        if (!await validarSintomasConPatologia(
            patologiaSelect.querySelector(`option[value="${formData.get('patologia')}"]`).innerHTML)) 
            return false
    }
    return true;
} 

function validarSintomas() {
    if(valores.length == 0) {
        sintomasSelect.className = "form-select is-invalid"
        document.getElementById('error-sintomas').style = "display: block;"
        return false;
    }
    sintomasSelect.className = "form-select is-valid"
    document.getElementById('error-sintomas').style = "display: none;"
    return true
}

function validarPatologia(patologia) {
    if(!patologia) {
        patologiaSelect.className = "form-control is-invalid"
        document.getElementById('error-patologia').style = "display: block;"
        return false;
    }
    patologiaSelect.className = "form-control is-valid"
    document.getElementById('error-patologia').style = "display: none;"
    return true;
}

function validarSospecha(sospecha, parentesco) {
    console.log(sospecha)
    console.log(parentesco)
    if (sospecha == '1' & !parentesco) {
        document.getElementById('parentescoInput').className = "form-control is-invalid"
        document.getElementById('error-parentesco').style = "display: block;"
        return false;
    }
    document.getElementById('parentescoInput').className = "form-control is-valid"
    document.getElementById('error-parentesco').style = "display: none;"
    return true;
}

async function validarSintomasConPatologia(patologia) {
    
    var sintomas = [];
    valores.forEach(e => sintomas.push(e.nombre));

    console.log(JSON.stringify({
        patologia: patologia,
        sintomas: sintomas
    }));

    try {
        const response = await fetch('https://api.claudioraverta.com/sintomas-validos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                patologia: patologia,
                sintomas: sintomas
            })
        });
        const data = await response.json();
        if (!data.valido) {
            const myModal = new bootstrap.Modal(document.getElementById('my-modal'));
            myModal.show();
            return false
        } 
    } catch (error) {
        console.error('Error:', error);
        return false;
    }
    return true
}

const genesSelect = document.getElementById('genes-select');
const divGenesSeleccionados = document.getElementById('genes-seleccionados');
var genes = []

genesSelect.addEventListener('change', function(e) {
    e.preventDefault()
    if (!genes.some(g => g.id === e.target.value)) {
        const nuevoSintoma = {
            id: e.target.value,
            nombre: genesSelect.querySelector(`option[value="${e.target.value}"]`).innerHTML
        };
        genes.push(nuevoSintoma);        

        const chip = document.createElement('span');
        chip.className = "badge rounded-pill text-bg-primary me-2";
        chip.textContent = genesSelect.querySelector(`option[value="${e.target.value}"]`).innerHTML;

        const closeBtn = document.createElement('a');
        const icon = document.createElement('i');
        icon.className = "bi bi-x-lg ml-2 delete-gen";
        icon.id = e.target.value;

        closeBtn.appendChild(icon)
        chip.appendChild(closeBtn)
        divGenesSeleccionados.appendChild(chip);
    }
});

document.addEventListener('click', function(e) {
    if (e.target.classList.contains('delete-gen')) {
        genes = genes.filter((s) =>  s.id !== e.target.id);
        const chip = e.target.closest('.badge');
        if (chip) {
            chip.remove();
        }
    }
});
 