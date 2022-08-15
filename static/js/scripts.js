// Custom Scripts
// // Custom scripts
// // Мобильное меню бургер
function burgerMenu() {
   const burger = document.querySelector(".burger");
   const menu = document.querySelector(".menu");
   const body = document.querySelector("body");
   burger.addEventListener("click", () => {
      if (!menu.classList.contains("active")) {
         menu.classList.add("active");
         burger.classList.add("active-burger");
         body.classList.add("locked");
      } else {
         menu.classList.remove("active");
         burger.classList.remove("active-burger");
         body.classList.remove("locked");
      }
   });
   // Вот тут мы ставим брейкпоинт навбара
   window.addEventListener("resize", () => {
      if (window.innerWidth > 991.98) {
         menu.classList.remove("active");
         burger.classList.remove("active-burger");
         body.classList.remove("locked");
      }
   });
}
burgerMenu();

// // Вызываем эту функцию, если нам нужно зафиксировать меню при скролле.
// function fixedNav() {
//    const nav = document.querySelector("nav");

//    // тут указываем в пикселях, сколько нужно проскроллить что бы наше меню стало фиксированным
//    const breakpoint = 1;
//    if (window.scrollY >= breakpoint) {
//       nav.classList.add("fixed__nav");
//    } else {
//       nav.classList.remove("fixed__nav");
//    }
// }
// window.addEventListener("scroll", fixedNav);

function accordion() {
   const items = document.querySelectorAll(".menu__trigger");
   items.forEach((item) => {
      item.addEventListener("click", () => {
         const parent = item.parentNode;
         if (parent.classList.contains("menu__item-angle-active")) {
            parent.classList.remove("menu__item-angle-active");
         } else {
            document
               .querySelectorAll(".menu__item-angle")
               .forEach((child) =>
                  child.classList.remove("menu__item-angle-active")
               );
            parent.classList.add("menu__item-angle-active");
         }
      });
   });
}
accordion();
function filter() {
   const items = document.querySelectorAll(".filter-trigger");
   items.forEach((item) => {
      item.addEventListener("click", () => {
         const parent = item.parentNode;
         if (parent.classList.contains("filter-active")) {
            parent.classList.remove("filter-active");
         } else {
            document
               .querySelectorAll(".filter")
               .forEach((child) => child.classList.remove("filter-active"));
            parent.classList.add("filter-active");
         }
      });
   });
}
filter();




function size() {
   const select = document.querySelector(".select__select");
   const enable = document.querySelector(".product__enable");
	const btn = document.querySelector('.product__btn')
   select.addEventListener("change", () => {
      if (select.value == "Выбрать") {
         enable.innerHTML = "";
			btn.disabled = true
      } else {
         enable.innerHTML = "В наличии";
			btn.disabled = false
      }
   });
}
size();

function cart(){
	const btns = document.querySelectorAll(".cart_prod__counter");
		const removeBtns = document.querySelectorAll(".cart_prod__btn");
		const cartWrapper = document.querySelector('.cart__wrap')
		const cartItem = document.querySelectorAll('.cart__item')
		if(cartItem.length == 0){
			cartWrapper.innerHTML = 'Ваша корзина пока пуста.'
			cartWrapper.classList.add('empty-cart')
		}
      btns.forEach((item) => {
         const plusBtn = item.childNodes[5]
      	const minusBtn = item.childNodes[1]
      	const count = item.childNodes[3].childNodes[0]
         plusBtn.addEventListener("click", () => {
            if (Number(count.innerHTML) >= 1) {
               count.innerHTML = Number(count.innerHTML) + 1;
            }
         });
         minusBtn.addEventListener("click", () => {
            if (Number(count.innerHTML) == 1) {
               count.innerHTML = 1;
            } else {
               count.innerHTML = Number(count.innerHTML) - 1;
            }
         });
			removeBtns.forEach((btn, i) => {
				btn.addEventListener('click', ()=>{
					btn.parentElement.remove()
					let cartItems = document.querySelectorAll('.cart__item')
					if(cartItems.length == 0){
						cartWrapper.innerHTML = 'Ваша корзина пока пуста.'
						cartWrapper.classList.add('empty-cart')
					}		
				})
			})
      });
}
cart()


