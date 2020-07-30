const updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function () {
    const productId = this.dataset.product
    const action = this.dataset.action
    if (user === 'AnonymousUser') {
      addCookieItem(productId, action)
    } else {
      updateUserOrder(productId, action)
    }
  })
}

const addCookieItem = (productId, action) => {
  if (action === 'add') {
    if (!cart[productId]) {
      cart[productId] = { 'quantity': 1 }
    } else {
      cart[productId]['quantity'] += 1
    }
  }

  if (action === 'remove') {
    cart[productId]['quantity'] -= 1

    if (cart[productId]['quantity'] <= 0) {
      console.log('Remove item')
      delete cart[productId]
    }
  }
  console.log({ cart })
  document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
  location.reload()
}

const updateUserOrder = (productId, action) => {
  const url = '/update_item/'
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
      console.log({ data })
      location.reload()
    })
}
