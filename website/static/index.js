let box1 = document.getElementById("box1");
let box2 = document.getElementById("box1");
let box3 = document.getElementById("box1");
let box4 = document.getElementById("box1");
let box5 = document.getElementById("box1");
let box6 = document.getElementById("box1");
let box7 = document.getElementById("box1");
let box8 = document.getElementById("box1");
let box9 = document.getElementById("box1");

const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener('mouseenter', Swal.stopTimer)
      toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
  })
  
  Toast.fire({
    icon: 'success',
    title: 'Signed in successfully'
  })