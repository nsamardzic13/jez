function copyText(user, text, datum) {
    document.getElementById('id_tekst').value += user + " je " + datum + " napisao/la:\n" + stripHtml(text) + "\n--------------------------------------------------\n";
}

function stripHtml(html)
{
   var c = document.getElementById(html);
   return c.innerText;
}

function changeclass(element){
    $(element).toggleClass('active')
}

