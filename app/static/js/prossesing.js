async function frase(){
    const text = await document.querySelector("#response").innerText;
    return text
}

const elemento = document.querySelector("#mytext")

frase().then( text => {

const intervalo = 45;
function message(elemento, text, intervalo){
    const char = text.split("").reverse();
    const type = setInterval(() => {
        if(!char.length){
            return clearInterval(type);
        }
        const next = char.pop();
        elemento.innerHTML += next;
        

    }, intervalo);
}
message(elemento, text, intervalo)
});

