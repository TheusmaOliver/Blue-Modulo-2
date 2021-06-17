const elementoPorId = document.getElementById('elemento1');
elementoPorId.innerHTML = "Eu represento o elemento com ID 'elemento1'";

const elementosPorClasse = document.getElementsByClassName('classe-exemplo');
for (const elemento of elementosPorClasse){
    elemento.innerHTML = "Eu sou um elemento com a classe 'classe-exemplo'";
}
