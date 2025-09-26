function addToShoppingBag(productId, productTitle, productImage) {
    let shoppingBag = JSON.parse(localStorage.getItem("shoppingBag")) || [];
    shoppingBag.push({ id: productId, title: productTitle, image: productImage });
    localStorage.setItem("shoppingBag", JSON.stringify(shoppingBag));
    alert("Produkti u shtua në shopping bag!");
}

// Për të shfaqur produktet e ruajtura në shopping bag
function loadShoppingBag() {
    let shoppingBag = JSON.parse(localStorage.getItem("shoppingBag")) || [];
    let container = document.getElementById("shopping-container");
    container.innerHTML = "";
    shoppingBag.forEach((product) => {
        container.innerHTML += `
            <div class="product">
                <img src="${product.image}" alt="Product Image">
                <h5>${product.title}</h5>
            </div>
        `;
    });
}

document.addEventListener("DOMContentLoaded", loadShoppingBag);
