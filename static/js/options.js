
    const tareas = document.getElementsByClassName('list-group-item');
    const columnas = document.getElementById('columnas');

    new Sortable(tareas, {
        group: 'shared', 
        animation: 150,
        ghostClass: 'blue-background-class'
    });

    new Sortable(columnas, {
        group: 'shared', 
        animation: 150,
        ghostClass: 'blue-background-class'
    });

