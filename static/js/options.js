    const tareas = document.getElementById('tareas2');
    const columnas = document.getElementById('columnas2');

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

