function confirmarModificarCol(id_producto) {
    Swal.fire({
        title: '¿Estás seguro/a?',
        text: "Estas a punto de Modificar una Columna!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Modificar!'
      }).then((result) => {
        if (result.isConfirmed) {
          //redirigir al usuario
          window.location.href ="/crear_Tarea/"+id_tarea+"/";
        }
      })
  }

  function confirmarEliminarCol(id_columna) {
    Swal.fire({
        title: '¿Estás seguro/a?',
        text: "Estas a punto de Eliminar un Columna!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!'
      }).then((result) => {
        if (result.isConfirmed) {
          //redirigir al usuario
          window.location.href ="/crear_Tarea/"+id_tarea+"/";
        }
      })
  }

  function confirmarModificarTar(id_producto) {
    Swal.fire({
        title: '¿Estás seguro/a?',
        text: "Estas a punto de Modificar una Tarea!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Modificar!'
      }).then((result) => {
        if (result.isConfirmed) {
          //redirigir al usuario
          window.location.href ="/crear_Tarea/"+id_tarea+"/";
        }
      })
  }

  function confirmarEliminarTar(id_columna) {
    Swal.fire({
        title: '¿Estás seguro/a?',
        text: "Estas a punto de Eliminar un Tarea!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!'
      }).then((result) => {
        if (result.isConfirmed) {
          //redirigir al usuario
          window.location.href ="/crear_Tarea/"+id_tarea+"/";
        }
      })
  }