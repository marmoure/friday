let popped = null;
poppedShow = null;
let towers = document.querySelector(".towers");
let overlay = document.querySelector(".overlay");




document.querySelectorAll(".tower").forEach(tower => {
    tower.addEventListener("click",() => {
        if(tower.childElementCount > 0 && popped == null) {
            let last = tower.childElementCount;
            last--;
            popped = tower.children[last];
            tower.children[last].remove();
            poppedShow = document.createElement("div");
            poppedShow.classList = [`popped size-${popped.value}`];
            let calc = popped.value*20+20;
            calc /= 2;
            poppedShow.style.left = `calc(50% - ${calc}px)`;
            towers.appendChild(poppedShow);

        }else if(popped != null) {
            if(tower.childElementCount === 0) {
                tower.appendChild(popped);
                towers.removeChild(poppedShow);
                popped = null;
            }else {
                let last = tower.childElementCount;
                last--;
                value = tower.children[last].value;
                if(value > popped.value) {
                    tower.appendChild(popped);
                    towers.removeChild(poppedShow);
                    popped = null;
                }
                if(tower.childElementCount == 8 && tower.id != "tower1") {
                    overlay.style.display = "flex";
                }
            }
        }
    });
});

document.getElementById("reload").addEventListener("click", () => {
    location.reload();
})
