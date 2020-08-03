"use strict";
$(document).ready(function () {
    $('.header').height($(window).height());
});

window.addEventListener("scroll",function(){
  let pageY = window.pageYOffset;
  let background = document.querySelector("header");
  background.style.backgroundPosition = `-${pageY * .25}px -100px`
})

window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation');
    // Loop over them and prevent submission
    forms.forEach(form =>{
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    })
    // var validation = Array.prototype.filter.call(forms, function(form) {
    //   form.addEventListener('submit', function(event) {
    //     if (form.checkValidity() === false) {
    //       event.preventDefault();
    //       event.stopPropagation();
    //     }
    //     form.classList.add('was-validated');
    //   }, false);
    // });
  }, false);