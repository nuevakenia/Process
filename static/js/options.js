
var lista = document.getElementsByClassName("list-group-item xd");
for (var i = 0; i < lista.length; i++) {
 lista[i].setAttribute("id", "tareas" + i);
}
const tareas = document.getElementById('tareas1');
const tareas2 = document.getElementById('tareas2');
const tareas3 = document.getElementById('tareas3');
const tareas4 = document.getElementById('tareas4');


new Sortable(tareas, {
    group: 'shared', 
    animation: 150,
    ghostClass: 'blue-background-class'
});

new Sortable(tareas2, {
    group: 'shared', 
    animation: 150,
    ghostClass: 'blue-background-class'
});

new Sortable(tareas3, {
    group: 'shared', 
    animation: 150,
    ghostClass: 'blue-background-class'
});

new Sortable(tareas4, {
    group: 'shared', 
    animation: 150,
    ghostClass: 'blue-background-class'
});
