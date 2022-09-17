let innerCursor0 = document.querySelector('.inner-cursor0');
let innerCursor1 = document.querySelector('.inner-cursor1');
let innerCursor2 = document.querySelector('.inner-cursor2');
let innerCursor3 = document.querySelector('.inner-cursor3');
let innerCursor4 = document.querySelector('.inner-cursor4');
let innerCursor5 = document.querySelector('.inner-cursor5');
let outerCursor = document.querySelector('.outer-cursor');

document.addEventListener('mousemove', moveCursor)

function moveCursor(e){
  let x = e.clientX;
  let y = e.clientY;
 
  innerCursor0.style.left = `${x}px`;
  innerCursor0.style.top = `${y}px`;
  innerCursor1.style.left = `${x}px`;
  innerCursor1.style.top = `${y}px`;
  innerCursor2.style.left = `${x}px`;
  innerCursor2.style.top = `${y}px`;
  innerCursor3.style.left = `${x}px`;
  innerCursor3.style.top = `${y}px`;
  innerCursor4.style.left = `${x}px`;
  innerCursor4.style.top = `${y}px`;
  innerCursor5.style.left = `${x}px`;
  innerCursor5.style.top = `${y}px`;
  outerCursor.style.left = `${x}px`;
  outerCursor.style.top = `${y}px`;
}

let links = Array.from(document.querySelectorAll("a"));

console.log(links);

links.forEach(link =>{
    link.addEventListener('mouseover', ()=>{
        innerCursor3.classList.add("grow");
    });
    link.addEventListener('mouseleave', ()=>{
        innerCursor3.classList.remove("grow");
    });
});