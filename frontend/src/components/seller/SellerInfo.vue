<template>
  <div class="seller-card">
    <header class="seller-header">
      <div class="seller-logo">
        <img :src="seller.logo_url" alt="Logo del vendedor">
      </div>
      <div class="seller-info">
        <h2 class="seller-name">{{ seller.name }}</h2>
        <p class="seller-stats">
          +{{ seller.followers }} Seguidores | +{{ seller.quantity_products }} Productos
        </p>
      </div>
      <button class="follow-btn" @click="toggleFollow">
        {{ isFollowing ? 'Siguiendo' : 'Seguir' }}
      </button>
    </header>

    <div v-if="seller.is_mercado_lider">
      <div class="leader-status" >
        <div class="leader-text">
          <h3>MercadoLíder Platinum</h3>
          <p>¡Uno de los mejores del sitio!</p>
        </div>
      </div>
  
      <div class="reputation-meter">
        <div class="bar">
          <span style="background-color: #ffcdd2;"></span>
          <span style="background-color: #fff9c4;"></span>
          <span style="background-color: #dcedc8;"></span>
          <span style="background-color: #c8e6c9;"></span>
          <span style="background-color: #4caf50;"></span>
        </div>
      </div>
      
  
      <div class="seller-metrics">
        <div class="metric">
          <strong>+{{ seller.quantity_products }}</strong>
          <span>Ventas concretadas</span>
        </div>
        <div class="metric">
          <span class="metric-icon chat-icon"></span>
          <span>Brinda buena atención</span>
        </div>
        <div class="metric">
          <span class="metric-icon clock-icon"></span>
          <span>Entrega sus productos a tiempo</span>
        </div>
      </div>
    </div>

    <button class="action-btn">Ir a la página del vendedor</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  seller: {
    type: Object,
    required: true
  }
});

const isFollowing = ref(false);

const toggleFollow = () => {
  isFollowing.value = !isFollowing.value;
  alert(isFollowing.value ? `Ahora sigues a ${props.seller.name}` : `Dejaste de seguir a ${props.seller.name}`);
};
</script>

<style scoped>
.seller-card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 350px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  background-color: #fff;
}

.seller-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.seller-logo {
  flex-shrink: 0;
}

.seller-logo img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: 1px solid #eee;
  background-color: #f5f5f5;
  display: block;
}

.seller-info {
  flex-grow: 1;
}

.seller-name {
  font-size: 14px;
  font-weight: 600;
  margin: 0 0 4px 0;
}

.seller-stats {
  font-size: 8px;
  color: #666;
  margin: 0;
}

.follow-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  background-color: rgba(52, 131, 250, 0.1);
  color: #3483fa;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
}

.follow-btn:hover {
  background-color: rgba(52, 131, 250, 0.2);
}

.leader-status {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}

.leader-icon {
  color: #00a650;
}

.leader-text h3 {
  font-size: 14px;
  color: #00a650;
  margin: 0;
  font-weight: 600;
}

.leader-text p {
  font-size: 14px;
  color: #666;
  margin: 0;
}

.reputation-meter .bar {
  display: flex;
  height: 8px;
  width: 100%;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 16px;
}
.reputation-meter .bar span {
  flex-grow: 1;
}

.seller-metrics {
  display: flex;
  justify-content: space-between;
  text-align: center;
  margin-bottom: 24px;
  color: #333;
}

.metric {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  width: 33%;
}

.metric strong {
  font-size: 14px;
  font-weight: 400;
}

.metric-icon {
  width: 24px;
  height: 24px;
  background-color: #00a650;
  border-radius: 50%;
  display: block;
  position: relative;
}

.metric-icon::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
}

.chat-icon::after {
  width: 10px;
  height: 8px;
  clip-path: polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%);
}

.clock-icon::after {
  width: 10px;
  height: 10px;
  border: 1.5px solid white;
  border-radius: 50%;
  background-color: transparent;
}

.action-btn {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 6px;
  background-color: rgba(52, 131, 250, 0.1);
  color: #3483fa;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}
.action-btn:hover {
   background-color: rgba(52, 131, 250, 0.2);
}

@media (max-width: 768px) {
  .seller-card {
    padding: 14px;
    border: none;
  }
}
</style>