let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function(){
    productId = this.dataset.product;
    action = this.dataset.action;
    console.log({productId, action});
    console.log({user});
    if (user === 'AnonymousUser') {
      console.log('Not logged in');
    } else {
      console.log('User is logged in')
    }
  });
}