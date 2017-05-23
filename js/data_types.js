/**
 * Created by JoeHow on 5/15/17.
 */

// int 1234567890
// float 456.678
// array []
// string 'bla bla'
// json {'key: "value",}

let name = 'Joe';

let names = ["joe", "bob", "jill"];



function greet(nam) {
    let color;
    if (nam === 'Joe'){
        color = '#498784'
    } else if (nam === 'Chris') {
        color = '#7d4087'
    } else {
        color = '#987'
    }

    let greeting = "hello " + nam + "!";


    let msg = document.getElementById("message")
        msg.innerHTML = greeting;
    msg.style.color = color;

}

// greet(name)
function iterate_them(n) {

}
// for (let i = 0; i < names.length; i++){
//     greet(names[i])
// }

function dothis() {
    greet(document.getElementById("thename").value)
}
document.getElementById("mybtn").addEventListener("click", dothis);
// document.getElementById("mybtn").addEventListener("click", () => greet(document.getElementById("thename").value));

