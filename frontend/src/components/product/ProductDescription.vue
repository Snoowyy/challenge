<template>
  <div class="description-card">
    <h2 class="title">Descripción</h2>

    <div class="content-wrapper" :class="{ 'expanded': isExpanded }">
      <p>{{ description }}</p>
    </div>
    
    <button @click="toggleDescription" class="toggle-button">
      <span>{{ isExpanded ? 'Ver menos' : 'Ver descripción completa' }}</span>
      <svg 
        xmlns="http://www.w3.org/2000/svg" 
        width="16" 
        height="16" 
        fill="currentColor" 
        class="chevron"
        :class="{ 'rotated': isExpanded }"
        viewBox="0 0 16 16"
      >
        <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
      </svg>
    </button>

  </div>
</template>

<script setup>
import { ref } from 'vue';
defineProps({
  description: String
});
const isExpanded = ref(false);
const toggleDescription = () => {
  isExpanded.value = !isExpanded.value;
};
</script>

<style scoped>
.description-card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 850px;
  padding: 24px;
  border-radius: 8px;
  border-top: 1px solid #eee;
  padding-top: 24px;
}

.title {
  font-size: 20px;
  font-weight: 500;
  color: #333;
  margin: 0 0 24px 0;
}

.content-wrapper {
  max-height: 120px; 
  overflow: hidden;
  position: relative;
  transition: max-height 0.5s ease-in-out;
}
.content-wrapper:not(.expanded)::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  background: linear-gradient(to bottom, transparent, white);
}

.content-wrapper.expanded {
  max-height: 1000px; 
}

h3 {
  font-size: 18px;
  font-weight: 600;
  color: #444;
  margin: 24px 0 8px 0;
}

p {
  font-size: 16px;
  color: #666;
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.toggle-button {
  background: none;
  border: none;
  color: #3483fa;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  padding: 0;
  margin-top: 16px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.chevron {
  transition: transform 0.3s ease;
}

.chevron.rotated {
  transform: rotate(180deg);
}
</style>