function copyText(user, text, datum) {
    document.getElementById('id_tekst').value += "<<< " + user + " je " + datum + " napisao/la: " + text + ">>>";
}

function changeclass(element){
    $(element).toggleClass('active')
}
