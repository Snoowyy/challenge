<template>
  <div class="purchase-card">
    <div class="shipping-info">
      <p class="free-shipping">Llega gratis mañana</p>
      <a href="#" class="link">Más formas de entrega</a>
    </div>
    <div class="pickup-info">
      <p>
        <strong>Retira gratis</strong> a partir del jueves en una agencia de Mercado Libre
      </p>
      <a href="#" class="link">Ver en el mapa</a>
    </div>

    <div class="stock-info">
      <p class="stock-title"><strong>Stock disponible</strong></p>
      
      <div class="quantity-selector">
        <label for="quantity">Cantidad:</label>
        <div class="dropdown-container">
          <button @click="toggleDropdown" class="dropdown-button">
            <span>{{ selectedQuantity }} unidad{{ selectedQuantity > 1 ? 'es' : '' }}</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-chevron-down" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
            </svg>
          </button>
          <span class="stock-available">({{ maxStock }} disponibles)</span>

          <ul v-if="isDropdownOpen" class="dropdown-menu">
            <li v-for="q in maxStock" :key="q" @click="selectQuantity(q)">
              {{ q }} unidad{{ q > 1 ? 'es' : '' }}
              <span v-if="q === selectedQuantity" class="checkmark">✓</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="action-buttons">
      <button class="btn btn-primary" @click="buyNow">Comprar ahora</button>
      <button class="btn btn-secondary" @click="addToCart">Agregar al carrito</button>
    </div>

    <div class="seller-info">
      <p>Vendido por <a href="#" class="link">{{seller.name}}</a></p>
      <p class="seller-status">MercadoLíder | <b>+{{seller.followers / 1000}}mil ventas</b></p>
    </div>

    <ul class="guarantees">
      <li>
        <svg class="icon" viewBox="0 0 16 16">...</svg> <div>
          <p><a href="#" class="link">Devolución gratis.</a> Tienes 30 días desde que lo recibes.</p>
        </div>
      </li>
      <li>
        <svg class="icon" viewBox="0 0 16 16">...</svg> <div>
          <p><a href="#" class="link">Compra Protegida</a>, recibe el producto que esperabas o te devolvemos tu dinero.</p>
        </div>
      </li>
      <li>
        <svg class="icon" viewBox="0 0 16 16">...</svg> <div>
          <p>12 meses de garantía de fábrica.</p>
        </div>
      </li>
    </ul>

    <div class="add-to-list">
      <a href="#" class="link">Agregar a una lista</a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const props = defineProps({
  product: Object,
});
const seller = ref(props.product.seller);
const maxStock = ref(props.product.stock);
const selectedQuantity = ref(1);
const isDropdownOpen = ref(false);

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value;
};


const selectQuantity = (quantity) => {
  selectedQuantity.value = quantity;
  isDropdownOpen.value = false;
};

const buyNow = () => {
  alert(`Comprando ${selectedQuantity.value} unidad(es).`);
};

const addToCart = () => {
  alert(`${selectedQuantity.value} unidad(es) agregada(s) al carrito.`);
};
</script>

<style scoped>
.purchase-card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 350px;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 24px;
  color: #333;
  background-color: #fff;
  height: fit-content;
  margin-bottom: 20px;
}

.link {
  color: #3483fa;
  text-decoration: none;
}
.link:hover {
  text-decoration: underline;
}

p {
  margin: 0;
  font-size: 12px;
  line-height: 1.4;
}

.shipping-info .free-shipping {
  color: #00a650;
  font-size: 14px;
  margin-bottom: 4px;
}
.pickup-info {
  margin-top: 16px;
}

.stock-info {
  margin-top: 24px;
  margin-bottom: 24px;
}
.stock-title {
    font-size: 14px;
    margin-bottom: 12px;
}

.quantity-selector {
  display: flex;
  flex-direction: column;
}
.quantity-selector label {
    font-size: 14px;
    margin-bottom: 8px;
    color: #555;
}
.dropdown-container {
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
}
.dropdown-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 150px;
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  background-color: #fff;
  cursor: pointer;
  text-align: left;
}
.dropdown-button span {
    font-size: 14px;
    font-weight: 600;
}
.dropdown-button .bi-chevron-down {
    color: #3483fa;
}
.stock-available {
    color: #888;
    font-size: 12px;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  width: 150px;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 6px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  list-style: none;
  padding: 8px 0;
  margin: 4px 0 0;
  z-index: 10;
}
.dropdown-menu li {
  padding: 10px 16px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.dropdown-menu li:hover {
  background-color: #f5f5f5;
}
.dropdown-menu .checkmark {
    color: #3483fa;
    font-weight: bold;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 24px;
}
.btn {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}
.btn-primary {
  background-color: #3483fa;
  color: white;
}
.btn-primary:hover {
  background-color: #2968c8;
}
.btn-secondary {
  background-color: rgba(52, 131, 250, 0.1);
  color: #3483fa;
}
.btn-secondary:hover {
  background-color: rgba(52, 131, 250, 0.2);
}

.seller-info {
  font-size: 12px;
  color: #555;
  margin-bottom: 24px;
}
.seller-status {
  color: #333;
  display: inline-block;
}

.guarantees {
  list-style: none;
  padding: 0;
  margin: 0 0 24px 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.guarantees li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.guarantees .icon {
  width: 20px;
  height: 20px;
  color: #888;
  flex-shrink: 0;
  margin-top: 2px;
}

.add-to-list a {
    font-size: 12px;
}

@media (max-width: 768px) {
  .purchase-card {
    border: none;
    padding: 20px;
  }
}
</style>