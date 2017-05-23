/**
 * Created by JoeHow on 5/15/17.
 */
// import TweenMax from "gsap";
// function change_color(){
//     let colr = {h: 0, s: 50, l: 100};
//     let element = document.getElementsByTagName("body")[0];
//     applyColor = () => {
//         element.style.backgroundColor = "hsl(" + colr.h + "," + colr.s + "%," + colr.l + "%)";
//     };
//     end_color = () => {
//         TweenMax.to(colr, 20, {h: 0, l: 100, onUpdate: applyColor});
//     };
//     TweenMax.to(colr, 5, {
//         h: -360,
//         l: 50,
//         onUpdate: applyColor,
//         onComplete: end_color,
//         yoyo: true,
//         repeat: 2
//     });
// }

function change_color() {
    let element = document.getElementsByTagName("body")[0];
    element.style.backgroundColor = "hsl(" + colr.h + "," + colr.s + "%," + colr.l + "%)";
}
change_color();