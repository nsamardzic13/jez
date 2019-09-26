function copyText(user, text, datum) {
    answer = document.getElementById('id_tekst')

    answer.value += user + " je " + datum + " napisao/la:\n" + stripHtml(text) + "\n--------------------------------------------------\n";
    answer.style.color= 'red';

    Object.assign(answer.style, css);
}

function stripHtml(html)
{
    return document.getElementById('html').innerText

}

function changeclass(element){
    $(element).toggleClass('active')
}
