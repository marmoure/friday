import { concatAll, delay, finalize, from, map, of, tap } from "rxjs";

interface Workout {
    name: string,
    duration: number,
    description?: string,
}

const container = document.querySelector(".container");
const start = document.querySelector(".start");


start.addEventListener("click", () => {
    start_workout();
});


// workout list
const workout_list: Workout[] = [
    {
        name: "thigh",
        duration: 120,
        description: " ",
    },
    {
        name: "it band",
        duration: 120,
        description: " ",
    },
    {
        name: "gluts",
        duration: 120,
        description: " ",
    },
    {
        name: "glutei fold",
        duration: 120,
        description: " ",
    },
    {
        name: "adductor",
        duration: 120,
        description: " ",
    },
    {
        name: "lumbar",
        duration: 120,
        description: " ",
    },
    {
        name: "calfs",
        duration: 120,
        description: " ",
    },
    {
        name: "abs",
        duration: 120,
        description: " ",
    },
    {
        name: "inner ribs",
        duration: 120,
        description: " ",
    },
    {
        name: "pecs",
        duration: 120,
        description: " ",
    },
]

const list: Workout[] = []

for (let i = 0; i < workout_list.length; i++) {
    list.push({
        name:`right ${workout_list[i].name}`,
        duration:workout_list[i].duration,
        description:workout_list[i].description
    });

    list.push({
        name:`left ${workout_list[i].name}`,
        duration:workout_list[i].duration,
        description:workout_list[i].description
    });

    if (i === workout_list.length - 1) continue;
    list.push({
        name: "rest",
        duration: 15,
        description: "Get Ready for the next one",
    })
}


function start_workout() {
    // remove the start button
    container.innerHTML = ``;

    //  iterate over the workout list and render
    from(list)
        .pipe(
            map(item => {
                return of(item).pipe(
                    tap(render_workout),
                    delay(item.duration * 1000)
                )
            }),
            concatAll(),
            finalize(() => {
                container.innerHTML = "done"
            })
        ).subscribe();
}

function render_workout(workout: Workout) {
    const seconds = workout.duration % 60;
    const minutes = Math.floor(workout.duration / 60)
    container.innerHTML = `
    <div class="name">${workout.name}</div>
        <p class="description">
            ${workout.description}
        </p> 
    <div id="timer" class="time">${minutes}:${seconds}</div>
    `;
    const timer = document.getElementById("timer");

    let remaining = workout.duration;

    setInterval(() => {
        const seconds = remaining % 60;
        const minutes = Math.floor(remaining / 60)
        timer.innerHTML = `${minutes}:${seconds}`;
        remaining -= 1;
    }, 1000)
}
