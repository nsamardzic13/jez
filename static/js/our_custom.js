function copyText(user, text, datum) {
    document.getElementById('id_tekst').value += datum + ";" + user + ":\n" + stripHtml(text) + "\n--------------------------------------------------\n";
}

function stripHtml(html)
{
   var c = document.getElementById(html);
   return c.innerText;
}





