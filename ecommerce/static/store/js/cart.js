let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function(){
    const productId = this.dataset.product;
    const action = this.dataset.action;
    if (user === 'AnonymousUser') {
      console.log('Not logged in');
    } else {
      updateUserOrder(productId, action);
    }
  });
}

const updateUserOrder = (productId, action) => {
  console.log('User is logged in');
  const url = '/update_item/';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
      productId,
      action,
    }),
  })
  .then((res) => {
    return res.json()
  })
  .then((data) => {
    console.log({data})
    location.reload();
  })
}
