var x = document.querySelectorAll("ul li");
x.forEach((e)=>{

    e.addEventListener("click", ()=>{
        e.classList.toggle("checked")
    }, false);

});
