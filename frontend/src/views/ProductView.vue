<template>
  <div v-if="loading" class="loading">Cargando producto...</div>
  <div v-if="error" class="error">{{ error }}</div>
  
  <div v-if="product" class="page-container">
    <main class="main-content">
      <div class="product-core-details">
        <ProductGallery :images="product.product_info.images" />
        <ProductInfo 
          :productInfo="product.product_info"
        />
        <div class="right-side">
          <PurchaseSection
            :product="product"
          />
          <SellerInfo :seller="product.seller" />
          <PaymentMethods />
        </div>
      </div>
      <div class="detail-section">
        <RelatedProducts :productId="product.id" />
        <ProductCharacteristics 
          :characteristics="product.characteristics"
        />
        <ProductDescription 
        :description="product.description"
        />
        <QuestionsAndAnswers 
        :questions = "product.questions"
        :productId="product.id"
        />
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import ProductGallery from '../components/product/ProductGallery.vue';
import ProductInfo from '../components/product/ProductInfo.vue';
import ProductCharacteristics from '../components/product/ProductCharacteristics.vue';
import ProductDescription from '../components/product/ProductDescription.vue';
import PurchaseSection from '../components/purchase/PurchaseSection.vue';
import SellerInfo from '../components/seller/SellerInfo.vue';
import QuestionsAndAnswers from '../components/questions/QuestionsAndAnswers.vue';
import RelatedProducts from '../components/related_products/RelatedProducts.vue';
import PaymentMethods from '../components/payments/PaymentMethods.vue';

const product = ref(null);
const loading = ref(true);
const error = ref(null);
const route = useRoute();

onMounted(async () => {
  try {
    const productId = route.params.id; 
    const response = await fetch(`http://localhost:8000/api/products/${productId}`);
    if (!response.ok) {
      throw new Error('The product could not be loaded');
    }
    product.value = await response.json();
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.loading, .error {
  text-align: center;
  padding: 50px;
  font-size: 1.2rem;
}
.error { color: red; }
.main-content {
  background-color: #fff;
  padding: 32px;
  border-radius: 8px;
  width: 1184px;
}
.product-core-details {
  display: flex;
  gap: 48px;
}

@media (max-width: 768px) {
  .main-content {
    width: fit-content;
    padding: 16px;
  }
  .product-core-details {
    flex-direction: column;
    padding: 10%;
  }
}
</style>