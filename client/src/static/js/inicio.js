//codigo refatorado:

const btnConfig = document.getElementById('btn-config');
const btnPerson = document.getElementById('btn-person');
const navConfig = document.getElementById('nav');
const navPerson = document.getElementById('navPerson');

function toggleMenu(btn, nav, openLabel, closeLabel) {
  return function(event) {
    if (event.type === 'touchstart') event.preventDefault();
    if (!nav) return; // Error handling

    const otherNav = nav === navConfig ? navPerson : navConfig;
    otherNav.classList.remove('active');

    nav.classList.toggle('active');
    const active = nav.classList.contains('active');
    btn.setAttribute('aria-expanded', active);
    btn.setAttribute('aria-label', active ? closeLabel : openLabel);
  }
}

const toggleConfig = toggleMenu(btnConfig, navConfig, 'Abrir Menu', 'Fechar Menu');
const togglePersonal = toggleMenu(btnPerson, navPerson, 'Abrir informacoes da conta', 'Fechar informacoes da conta');

if (btnConfig) {
  btnConfig.addEventListener('click', toggleConfig);
  btnConfig.addEventListener('touchstart', toggleConfig);
}

if (btnPerson) {
  btnPerson.addEventListener('click', togglePersonal);
  btnPerson.addEventListener('touchstart', togglePersonal);
}

window.addEventListener('scroll', function() {
  let navbar = document.getElementsByClassName('main-nav')[0]; // Pegue o primeiro elemento com a classe 'main-nav'
  if (navbar) {
    navbar.classList.add('has-scroll'); // Adicione a classe 'has-scroll'
  } else {
    navbar.removeClass('has-scroll'); 
  }
});



////////////// codigo antigo ///////////////////////////////

// const btnMobile = document.getElementById('btn-config');
// const btnPersonal = document.getElementById('btn-person');

// function toggleMenu(event) {
//   if (event.type === 'touchstart') event.preventDefault();
//   const nav = document.getElementById('nav');
//   nav.classList.toggle('active');
//   const active = nav.classList.contains('active');
//   event.currentTarget.setAttribute('aria-expanded', active);
//   if (active) {
//     event.currentTarget.setAttribute('aria-label', 'Fechar Menu');
//   } else {
//     event.currentTarget.setAttribute('aria-label', 'Abrir Menu');
//   }
// }

// btnMobile.addEventListener('click', toggleMenu);
// btnMobile.addEventListener('touchstart', toggleMenu);

// function togglePersonal(event) {
//   if (event.type === 'touchstart') event.preventDefault();
//   const nav = document.getElementById('navPerson');
//   nav.classList.toggle('active');
//   const active = nav.classList.contains('active');
//   event.currentTarget.setAttribute('aria-expanded', active);
//   if (active) {
//     event.currentTarget.setAttribute('aria-label', 'Fechar infomacoes da conta');
//   } else {
//     event.currentTarget.setAttribute('aria-label', 'Abrir informacoes da conta');
//   }
// }
// btnPersonal.addEventListener('click', togglePersonal);
// btnPersonal.addEventListener('touchstart', togglePersonal);