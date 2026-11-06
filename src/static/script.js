function mostrarSenha() {
  const elementoHTML = document.getElementById('icone-mostrar-exibir-senha')

  if (senha.type === 'text') {
    senha.type = 'password'
    elementoHTML.classList = 'bi bi-eye-fill'
  } else {
    senha.type = 'text'
    elementoHTML.classList = 'bi bi-eye-slash-fill'
  }

  desconsideraIssoAqui() // REMOVE ISSO AQUI; FOI SÓ PRA TESTAR E ENSINAR
}


function desconsideraIssoAqui() {
  const elementoErroLogin = document.getElementById('erro-login')
  const elementoLogin = document.getElementById('login')

  if (elementoLogin.value == '') {
    elementoErroLogin.style = 'display: block;'
    elementoLogin.classList = 'form-control border border-danger'
  } else {
    elementoLogin.classList = 'form-control'
    elementoErroLogin.style = 'display: none;'
  }
}