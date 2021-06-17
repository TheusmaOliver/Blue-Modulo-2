const botao = document.querySelector('#botao');
const botaoFoiClicado = () =>{
    alert('Você clicou no botão');
}

botao.addEventListener('click', botaoFoiClicado);
botao.innerText = "Clique aqui!"