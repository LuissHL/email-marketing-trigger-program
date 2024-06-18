const btnMobile = document.getElementById('btn-config');
const btnPersonal = document.getElementById('btn-person');

function toggleMenu(event) {
  if (event.type === 'touchstart') event.preventDefault();
  const nav = document.getElementById('nav');
  nav.classList.toggle('active');
  const active = nav.classList.contains('active');
  event.currentTarget.setAttribute('aria-expanded', active);
  if (active) {
    event.currentTarget.setAttribute('aria-label', 'Fechar Menu');
  } else {
    event.currentTarget.setAttribute('aria-label', 'Abrir Menu');
  }
}

btnMobile.addEventListener('click', toggleMenu);
btnMobile.addEventListener('touchstart', toggleMenu);

function togglePersonal(event) {
  if (event.type === 'touchstart') event.preventDefault();
  const nav = document.getElementById('navPerson');
  nav.classList.toggle('active');
  const active = nav.classList.contains('active');
  event.currentTarget.setAttribute('aria-expanded', active);
  if (active) {
    event.currentTarget.setAttribute('aria-label', 'Fechar infomacoes da conta');
  } else {
    event.currentTarget.setAttribute('aria-label', 'Abrir informacoes da conta');
  }
}
btnPersonal.addEventListener('click', togglePersonal);
btnPersonal.addEventListener('touchstart', togglePersonal);