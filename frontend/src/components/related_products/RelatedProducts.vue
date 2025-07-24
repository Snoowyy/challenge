<template>
  <section class="related-products-container">
    <div v-if="loading" class="state-feedback">Cargando productos...</div>
    <div v-if="error" class="state-feedback error">{{ error }}</div>

    <div v-if="related_products.length > 0">
      <header class="section-header">
        <h2>Productos relacionados</h2>
        <span>Promocionado</span>
      </header>

      <div class="cards-wrapper">
        <article v-for="product in related_products" :key="product.name" class="product-card">
          <img src="https://www.gynprog.com.br/wp-content/uploads/2017/06/wood-blog-placeholder.jpg" class="product-image" />
          
          <div class="product-info">
            <p class="product-name">{{ product.name }}</p>
            
            <div class="price-section">
              <span v-if="product.value" class="original-price">
                {{ formatCurrency(product.value) }}
              </span>
              <div class="current-price-container">
                <span class="current-price">{{ formatCurrency(product.value) }}</span>
              </div>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const props = defineProps({
  productId: {
    type: String,
    required: true,
  },
});

interface RelatedProduct {
  name: string;
  value: number;
}

const related_products = ref<RelatedProduct[]>([]);
const loading = ref<boolean>(true);
const error = ref<string | null>(null);

const formatCurrency = (value: number): string => {
  return new Intl.NumberFormat('es-CO', {
    style: 'currency',
    currency: 'COP',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(value);
};

onMounted(async () => {
  try {
    const response = await fetch(`http://localhost:8000/api/related_products/${props.productId}`, {
      method: 'POST',
    });
    if (!response.ok) {
      throw new Error('No se pudieron cargar los productos.');
    }
    related_products.value = await response.json();
  } catch (err: any) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.related-products-container {
  width: 100%;
  max-width: 850px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.section-header {
  padding: 0 1rem; 
}

.section-header h2 {
  font-size: 1.5rem;
  color: #333;
  margin: 0;
}

.section-header span {
  font-size: 0.8rem;
  color: #777;
}

.cards-wrapper {
  display: flex;
  overflow-x: auto; 
  gap: 1rem;
  padding: 1rem;
  
  scrollbar-width: none; 
  -ms-overflow-style: none;  
}
.cards-wrapper::-webkit-scrollbar {
  display: none; 
}

.product-card {
  flex: 0 0 220px; 
  background-color: #fff;
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: box-shadow 0.2s ease;
}
.product-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.product-image {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-bottom: 1px solid #eee;
}

.product-info {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1; 
}

.product-name {
  font-size: 0.9rem;
  color: #333;
  margin: 0 0 1rem 0;
  line-height: 1.4;
  flex-grow: 1; 
}

.price-section {
  margin-bottom: 0.5rem;
}

.original-price {
  font-size: 0.8rem;
  color: #777;
  text-decoration: line-through;
}

.current-price-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.current-price {
  font-size: 1.4rem;
  color: #333;
}

.discount {
  font-size: 0.9rem;
  color: #00a650; 
  font-weight: 600;
}

.installments {
  font-size: 0.85rem;
  color: #333;
  margin: 0;
}

.card-discount {
  font-size: 0.8rem;
  color: #3483fa;
  margin: 0.5rem 0;
}

.shipping {
  font-size: 0.85rem;
  color: #00a650;
  font-weight: 600;
  margin-top: auto;
  padding-top: 0.5rem;
}

.shipping-full {
  font-style: italic;
}

.state-feedback {
  padding: 2rem;
  text-align: center;
  color: #777;
}

.state-feedback.error {
  color: #d93025;
}

@media (max-width: 768px) {
  .related-products-container {
    padding: 10%
  }
  .cards-wrapper {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    overflow-x: hidden;
    padding: 1rem 0;
  }

  .section-header {
    padding: 0;
  }
}
</style>