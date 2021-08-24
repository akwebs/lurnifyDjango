/********************
header
********************/
$(".header .header__bars").on('click', function () {

    var selector = $(".header .header__nav")

    if (selector.hasClass('shown')) {
        selector.css('right', "100%");
        selector.removeClass('shown');
    } else {
        selector.css('right', "0");
        selector.addClass('shown');
    }
});

$(".header .header__nav span").on('click', function () {

    var selector = $(".header .header__nav")

    if (selector.hasClass('shown')) {
        selector.css('right', "100%");
        selector.removeClass('shown');
    } else {
        selector.css('right', "0");
        selector.addClass('shown');
    }
});

$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();
    let elementId = $(event.target).attr('href');
    if (elementId == '#') return;

    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 1000, 'swing');
});

$(window).on('scroll', () => {
    if ($(window).scrollTop() > 50) {
        $('.header-1').addClass('fixed');
    } else {
        $('.header-1').removeClass('fixed');
    }
});

$(window).on('scroll', () => {
    if ($(window).scrollTop() > 0) {
        $('.header-2').addClass('fixed');
    } else {
        $('.header-2').removeClass('fixed');
    }
});

/********************
testimonial
********************/
$(".testimonial__wrapper").on('mouseover click', (e) => {
    if ($(e.target).is('img')) {
        let parentElement = $(e.target).parent().parent();
        //console.log(parentElement);
        parentElement.addClass('active');
        if (parentElement.siblings().hasClass('active')) {
            parentElement.siblings().removeClass('active');
        }
    }
});

/********************
clients slider
********************/
var clients = new Swiper('.clients-slider', {
    loop: true,
    autoplay: true,
    slidesPerView: 1,
    centeredSlides: true,
    breakpoints: {
        0: {
            slidesPerView: 1.75,
            spaceBetween: 10,
        },
        991.98: {
            slidesPerView: 3,
        },
        768: {
            slidesPerView: 2,
        }
    }
});

/********************
screenshot slider
********************/
var screenshot = new Swiper('.screenshot-slider', {
    loop: true,
    slidesPerView: 4.75,
    centeredSlides: true,
    spaceBetween: 30,
    navigation: {
        nextEl: '.screenshot-nav-next',
        prevEl: '.screenshot-nav-prev',
    },
    breakpoints: {
        0: {
            slidesPerView: 1.25,
            spaceBetween: 10,
        },
        991.98: {
            slidesPerView: 2.75,
        },
        1200: {
            slidesPerView: 3.25,
        },
        1350: {
            slidesPerView: 3.5,
        },
        1600: {
            slidesPerView: 3.90,
        },
        1800: {
            slidesPerView: 4.75,
        }
    }
});

/********************
related post slider
********************/
var related_post = new Swiper('.blog_related-slider', {
    loop: true,
    slidesPerView: 2,
    navigation: {
        nextEl: '.related-post-nav .screenshot-nav-next',
        prevEl: '.related-post-nav .screenshot-nav-prev',
    },
    spaceBetween: 30,
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        991.98: {
            slidesPerView: 2
        }
    }
});

/********************
accordion
********************/
$('.card').on('hide.bs.collapse', function (e) {
    var parentId = $(e.target).parent().attr('id');
    $(`#${parentId} > .card-header > h5`).addClass('hidden');
});

$('.card').on('show.bs.collapse', function (e) {
    var parentId = $(e.target).parent().attr('id');
    $(`#${parentId} > .card-header > h5`).removeClass('hidden');
});

/********************
blog
********************/
$('.category__dropdown').on('click', (e) => {
    if (($(e.target).parents().hasClass('category__dropdown')) && !($('.category__dropdown-box').hasClass('shown'))) {
        $('.category__dropdown-box').addClass('shown');
    } else if (($(e.target).parents().hasClass('category__dropdown-info')) && ($('.category__dropdown-box').hasClass('shown'))) {
        $('.category__dropdown-box').removeClass('shown');
    }
});
$('.date__dropdown').on('click', (e) => {
    if (($(e.target).parents().hasClass('date__dropdown')) && !($('.date__dropdown-box').hasClass('shown'))) {
        $('.date__dropdown-box').addClass('shown');
    } else if (($(e.target).parents().hasClass('date__dropdown-info')) && ($('.date__dropdown-box').hasClass('shown'))) {
        $('.date__dropdown-box').removeClass('shown');
    }
});

$(window).on('hover', (e) => {
    if (!($(e.target).parents().hasClass('category__dropdown'))) {
        $('.category__dropdown-box').removeClass('shown');
    }
    if (!($(e.target).parents().hasClass('date__dropdown'))) {
        $('.date__dropdown-box').removeClass('shown');
    }
});


$('.nav__dropdown-info').on('click', (e) => {
    let parentId = $(e.target).closest('li').attr('id');
    $(`#${parentId} > .nav__dropdown-box`).toggleClass('shown');
});




//custom selecter
var x, i, j, l, ll, selElmnt, a, b, c;
/*look for any elements with the class "custom-select":*/
x = document.getElementsByClassName("custom-select");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  /*for each element, create a new DIV that will act as the selected item:*/
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /*for each element, create a new DIV that will contain the option list:*/
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    /*for each option in the original select element,
    create a new DIV that will act as an option item:*/
    c = document.createElement("DIV");
    // c.setAttribute("class", "option");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
        /*when an item is clicked, update the original select box,
        and the selected item:*/
        var y, i, k, s, h, sl, yl;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        sl = s.length;
        h = this.parentNode.previousSibling;
        for (i = 0; i < sl; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }
        h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
      /*when the select box is clicked, close any other select boxes,
      and open/close the current select box:*/
      e.stopPropagation();
      closeAllSelect(this);
      this.nextSibling.classList.toggle("select-hide");
      this.classList.toggle("select-arrow-active");
    });
}
function closeAllSelect(elmnt) {
  /*a function that will close all select boxes in the document,
  except the current select box:*/
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}
/*if the user clicks anywhere outside the select box,
then close all select boxes:*/
document.addEventListener("click", closeAllSelect);


window.onload = function(){
    crear_select();
  }
  
  function isMobileDevice() {
      return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
  };
  
   
  var li = new Array();
  function crear_select(){
  var div_cont_select = document.querySelectorAll("[data-mate-select='active']");
  var select_ = '';
  for (var e = 0; e < div_cont_select.length; e++) {
  div_cont_select[e].setAttribute('data-indx-select',e);
  div_cont_select[e].setAttribute('data-selec-open','false');
  var ul_cont = document.querySelectorAll("[data-indx-select='"+e+"'] > .cont_list_select_mate > ul");
   select_ = document.querySelectorAll("[data-indx-select='"+e+"'] >select")[0];
   if (isMobileDevice()) { 
  select_.addEventListener('change', function () {
   _select_option(select_.selectedIndex,e);
  });
   }
  var select_optiones = select_.options;
  document.querySelectorAll("[data-indx-select='"+e+"']  > .selecionado_opcion ")[0].setAttribute('data-n-select',e);
  document.querySelectorAll("[data-indx-select='"+e+"']  > .icon_select_mate ")[0].setAttribute('data-n-select',e);
  for (var i = 0; i < select_optiones.length; i++) {
  li[i] = document.createElement('li');
  if (select_optiones[i].selected == true || select_.value == select_optiones[i].innerHTML ) {
  li[i].className = 'active';
  document.querySelector("[data-indx-select='"+e+"']  > .selecionado_opcion ").innerHTML = select_optiones[i].innerHTML;
  };
  li[i].setAttribute('data-index',i);
  li[i].setAttribute('data-selec-index',e);
  // funcion click al selecionar 
  li[i].addEventListener( 'click', function(){  _select_option(this.getAttribute('data-index'),this.getAttribute('data-selec-index')); });
  
  li[i].innerHTML = select_optiones[i].innerHTML;
  ul_cont[0].appendChild(li[i]);
  
      }; // Fin For select_optiones
    }; // fin for divs_cont_select
  } // Fin Function 
  
  
  
  var cont_slc = 0;
  function open_select(idx){
  var idx1 =  idx.getAttribute('data-n-select');
    var ul_cont_li = document.querySelectorAll("[data-indx-select='"+idx1+"'] .cont_select_int > li");
  var hg = 0;
  var slect_open = document.querySelectorAll("[data-indx-select='"+idx1+"']")[0].getAttribute('data-selec-open');
  var slect_element_open = document.querySelectorAll("[data-indx-select='"+idx1+"'] select")[0];
   if (isMobileDevice()) { 
    if (window.document.createEvent) { // All
    var evt = window.document.createEvent("MouseEvents");
    evt.initMouseEvent("touchstart mousedown", false, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
      slect_element_open.dispatchEvent(evt);
  } else if (slect_element_open.fireEvent) { // IE
    slect_element_open.fireEvent("onmousedown");
  }else {
    slect_element_open.click();
  }
  }else {
  
    
    for (var i = 0; i < ul_cont_li.length; i++) {
  hg += ul_cont_li[i].offsetHeight;
  }; 
   if (slect_open == 'false') {  
   document.querySelectorAll("[data-indx-select='"+idx1+"']")[0].setAttribute('data-selec-open','true');
   document.querySelectorAll("[data-indx-select='"+idx1+"'] > .cont_list_select_mate > ul")[0].style.height = hg+"px";
   document.querySelectorAll("[data-indx-select='"+idx1+"'] > .icon_select_mate")[0].style.transform = 'rotate(180deg)';
  }else{
   document.querySelectorAll("[data-indx-select='"+idx1+"']")[0].setAttribute('data-selec-open','false');
   document.querySelectorAll("[data-indx-select='"+idx1+"'] > .icon_select_mate")[0].style.transform = 'rotate(0deg)';
   document.querySelectorAll("[data-indx-select='"+idx1+"'] > .cont_list_select_mate > ul")[0].style.height = "0px";
   }
  }
  
  } // fin function open_select
  
  function salir_select(indx){
  var select_ = document.querySelectorAll("[data-indx-select='"+indx+"'] > select")[0];
   document.querySelectorAll("[data-indx-select='"+indx+"'] > .cont_list_select_mate > ul")[0].style.height = "0px";
  document.querySelector("[data-indx-select='"+indx+"'] > .icon_select_mate").style.transform = 'rotate(0deg)';
   document.querySelectorAll("[data-indx-select='"+indx+"']")[0].setAttribute('data-selec-open','false');
  }
  
  
  function _select_option(indx,selc){
   if (isMobileDevice()) { 
  selc = selc -1;
  }
    var select_ = document.querySelectorAll("[data-indx-select='"+selc+"'] > select")[0];
  
    var li_s = document.querySelectorAll("[data-indx-select='"+selc+"'] .cont_select_int > li");
    var p_act = document.querySelectorAll("[data-indx-select='"+selc+"'] > .selecionado_opcion")[0].innerHTML = li_s[indx].innerHTML;
  var select_optiones = document.querySelectorAll("[data-indx-select='"+selc+"'] > select > option");
  for (var i = 0; i < li_s.length; i++) {
  if (li_s[i].className == 'active') {
  li_s[i].className = '';
  };
  li_s[indx].className = 'active';
  
  };
  select_optiones[indx].selected = true;
    select_.selectedIndex = indx;
    select_.onchange();
    salir_select(selc); 
  }
  
  

























































