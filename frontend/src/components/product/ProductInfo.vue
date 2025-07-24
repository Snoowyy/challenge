<template>
  <div class="product-details">
    <header class="product-header">
      <div class="product-meta">
        {{ productInfo.condition }} | +{{ productInfo.sold_quantity }} vendidos
      </div>
      <button class="favorite-btn" @click="toggleFavorite">
        <svg :class="{ favorited: productInfo.is_favorited }" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
      </button>
    </header>

    <h1 class="product-title">{{ productInfo.title }}</h1>

    <div class="product-rating">
      <span>{{ productInfo.rating.average }}</span>
      <span class="stars">★★★★★</span>
      <a href="#" class="link">({{ productInfo.rating.reviews }})</a>
    </div>

    <div class="pricing">
      <span class="original-price">$ {{ productInfo.price.real_amount.toLocaleString('es-CO') }}</span>
      <div class="current-price-line">
        <span class="current-price">$ {{ productInfo.price.discounted_amount.toLocaleString('es-CO') }}</span>
        <span class="discount">{{ productInfo.price.discount }}% OFF</span>
      </div>
      <a href="#" class="link">Ver los medios de pago</a>
    </div>

    <div class="variant-selectors">
      <div class="selector">
        <p><strong>Color:</strong> {{ selectedColor.name }}</p>
        <div class="options-container">
          <button
            v-for="color in productInfo.variants.colors"
            :key="color.name"
            @click="selectColor(color)"
            :class="{ selected: selectedColor.name === color.name }"
            class="color-option"
          >
            <img :src="color.thumbnail" :alt="color.name">
          </button>
        </div>
      </div>

      <div class="selector">
        <p><strong>Memoria interna:</strong> {{ selectedStorage }} GB</p>
        <div class="options-container">
          <button
            v-for="storage in productInfo.variants.storage"
            :key="storage"
            @click="selectStorage(storage)"
            :class="{ selected: selectedStorage === storage }"
            class="text-option"
          >
            {{ storage }} GB
          </button>
        </div>
      </div>
      
      <div class="selector">
        <p><strong>Memoria RAM:</strong> {{ selectedRam }} GB</p>
        <div class="options-container">
            <button
            v-for="ram in productInfo.variants.ram"
            :key="ram"
            @click="selectRam(ram)"
            :class="{ selected: selectedRam === ram }"
            class="text-option"
          >
            {{ ram }} GB
          </button>
        </div>
      </div>
    </div>

    <div class="product-features">
      <h2>Lo que tienes que saber de este producto</h2>
      <ul>
        <li v-for="feature in productInfo.features" :key="feature">{{ feature }}</li>
      </ul>
      <a href="#" class="link">Ver características</a>
    </div>

    <div class="purchase-options">
      <h3>Opciones de compra:</h3>
      <a href="#" class="link">5 productos nuevos desde $ {{ productInfo.price.discounted_amount.toLocaleString('es-CO') }}</a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  productInfo: {
    type: Object,
    required: true
  }
});

const selectedColor = ref(props.productInfo.variants.colors[0]);
const selectedStorage = ref(props.productInfo.variants.storage[0]);
const selectedRam = ref(props.productInfo.variants.ram[0]);

const toggleFavorite = () => {
  props.productInfo.isFavorited = !props.productInfo.isFavorited;
};

const selectColor = (color) => {
  selectedColor.value = color;
};

const selectStorage = (storage) => {
  selectedStorage.value = storage;
};

const selectRam = (ram) => {
  selectedRam.value = ram;
};
</script>

<style scoped>
.product-details {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 600px;
  margin: 0 auto;
  padding: 16px;
  color: #333;
}

.link {
  color: #3483fa;
  text-decoration: none;
  font-size: 14px;
}
.link:hover {
  text-decoration: underline;
}

.product-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}
.product-meta {
  font-size: 14px;
  color: #666;
}
.favorite-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  color: #3483fa;
}
.favorite-btn svg.favorited {
  fill: #3483fa;
}

.product-title {
  font-size: 22px;
  font-weight: 500;
  margin: 0 0 8px 0;
}

.product-rating {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  margin-bottom: 16px;
}
.product-rating .stars {
  color: #3483fa;
}

.pricing {
  margin-bottom: 24px;
}
.original-price {
  text-decoration: line-through;
  color: #999;
  font-size: 16px;
}
.current-price-line {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 4px 0;
}
.current-price {
  font-size: 36px;
  font-weight: 400;
}
.discount {
  font-size: 18px;
  color: #00a650;
  font-weight: 500;
}
.installments {
  font-size: 16px;
  color: #00a650;
  margin-bottom: 8px;
}

.variant-selectors {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 24px;
}
.selector p {
  margin: 0 0 8px 0;
  font-size: 16px;
}
.options-container {
  display: flex;
  gap: 8px;
}
.color-option {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 2px;
  background: none;
  cursor: pointer;
}
.color-option.selected {
  border: 2px solid #3483fa;
}
.color-option img {
  width: 40px;
  height: 40px;
  display: block;
  background-color: #f0f0f0; 
  border-radius: 2px;
}

.text-option {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  background-color: #fff;
  cursor: pointer;
  font-size: 14px;
}
.text-option.selected {
  border-color: #3483fa;
  background-color: #edf4fe;
  color: #3483fa;
  font-weight: 600;
}

.product-features {
  border-top: 1px solid #eee;
  padding-top: 24px;
  margin-bottom: 24px;
}
.product-features h2 {
  font-size: 18px;
  font-weight: 500;
  margin: 0 0 16px 0;
}
.product-features ul {
  list-style-type: disc;
  padding-left: 20px;
  margin: 0 0 16px 0;
  font-size: 14px;
  line-height: 1.5;
  color: #555;
}
.product-features li::marker {
  color: #3483fa;
}

.purchase-options {
  border-top: 1px solid #eee;
  padding-top: 24px;
}
.purchase-options h3 {
  font-size: 16px;
  margin: 0 0 8px 0;
}
</style>