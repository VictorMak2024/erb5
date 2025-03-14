const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();
date.getFullYear();

setTimeout(() => {
    $('#message').fadeOut('slow');
}, 3000);