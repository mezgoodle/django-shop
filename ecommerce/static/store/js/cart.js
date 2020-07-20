let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function(){
    productId = this.dataset.product;
    action = this.dataset.action;
    console.log({productId, action});
  });
}