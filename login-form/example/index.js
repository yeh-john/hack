// Const GAS script link
const scriptURL = 'https://script.google.com/macros/s/AKfycbyDUBnToxOObswRpc3-sKglvp7oj3itCBkM698FqF37AV3Yjk6p_YBnJu6a5czpgtf1/exec'

// Const HTML form name
const form = document.forms['contactform']

// Main script
form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
        .then(response => console.log('Success!', response))
        .catch(error => console.error('Error!', error.message))
})