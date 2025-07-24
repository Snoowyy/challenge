<template>
  <div class="payment-methods-summary">
    <h3>Medios de pago</h3>

    <div class="highlight-banner">
      Paga en hasta <strong> 12 cuotas con 0% interés</strong>
    </div>

    <div class="card-section">
      <h4>Tarjetas de crédito</h4>
      <div class="logo-group">
        <img src="https://img.icons8.com/?size=100&id=1429&format=png&color=000000" alt="Visa">
        <img src="https://cdn.worldvectorlogo.com/logos/mastercard-7.svg" alt="Mastercard">
        <img src="https://img.icons8.com/?size=100&id=1433&format=png&color=000000" alt="American Express">
        <img src="https://cdn.aglty.io/scotiabank-colombia/CodensaAssets/logos-codensa/logo05.png" alt="Codensa">
      </div>
    </div>

    <div class="card-section">
      <h4>Tarjetas de débito</h4>
      <div class="logo-group">
        <img src="https://w7.pngwing.com/pngs/442/319/png-transparent-debit-visa-card-credit-money-pay-payment-pinpoint-payment-icon.png" alt="Visa Débito">
        <img src="https://images.icon-icons.com/1259/PNG/512/1495815236-jd07_84584.png" alt="Mastercard Débito">
      </div>
    </div>
    
    <div class="card-section">
      <h4>Efectivo</h4>
       <div class="logo-group">
        <img src="https://uni2.com.co/wp-content/uploads/2021/06/efecty-logo.png" alt="Efecty">
      </div>
    </div>

    <button @click="isModalOpen = true" class="link-button">
      Conoce otros medios de pago
    </button>
  </div>

  <PaymentMethodsModal 
    v-if="isModalOpen" 
    @close="isModalOpen = false" 
  />
</template>

<script setup lang="ts">
import { ref } from 'vue';
import PaymentMethodsModal from './PaymentMethodsModal.vue';

const isModalOpen = ref(false);
</script>

<style scoped>
.payment-methods-summary {
  font-family: Arial, sans-serif;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 12px;
  background-color: #fff;
  margin-top: 24px;
}

h3 {
  font-size: 1.25rem;
  margin-top: 0;
  color: #333;
}

.highlight-banner {
  background-color: #00a650;
  color: white;
  padding: 1rem;
  border-radius: 6px;
  margin: 1rem 0;
  display: flex;
  font-size: 12px;
}

.card-section {
  margin-bottom: 1.5rem;
}

h4 {
  font-size: 1rem;
  font-weight: normal;
  color: #555;
  margin-bottom: 0.5rem;
}

.logo-group {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.logo-group img {
  height: 25px;
}

.link-button {
  background: none;
  border: none;
  color: #3483fa;
  font-size: 1rem;
  cursor: pointer;
  padding: 0;
}
.link-button:hover {
  text-decoration: underline;
}
@media (max-width: 768px) {
  .payment-methods-summary {
    border: none;
    padding: 20px;
    margin-bottom: 20px;
  }

}
</style>