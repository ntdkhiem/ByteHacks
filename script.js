"use strict";
$(document).ready(function () {
    $('.header').height($(window).height());
});

window.addEventListener("scroll",function(){
  let pageY = window.pageYOffset;
  let background = document.querySelector("header");
  background.style.backgroundPosition = `-${pageY * .25}px -100px`
})