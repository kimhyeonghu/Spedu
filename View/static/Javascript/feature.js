window.addEventListener('load', () => {

    const params = (new URL(document.location)).searchParams;
    const number = params.get('number');

    document.getElementById('quantity').innerHTML = number;

})