<template>
  <div class="card">
    <h2 class="title">Características del producto</h2>

    <div class="feature-item large-feature" v-for="characteristic in slideCharacteristics" :key="characteristic.label">
      <div class="text-container">
        <p>{{ characteristic.label }}</p>
        <p class="sub-text">{{ characteristic.value }}</p>
        <div class="slider">
          <div class="slider-track">
            <div 
              class="slider-fill"
              :style="{ width: calculateSliderWidth(characteristic) + '%' }"
            ></div>
          </div>
          <div class="slider-labels">
            <span>PEQUEÑO</span>
            <span>GRANDE</span>
          </div>
        </div>
      </div>
    </div>

    <div class="features-grid">
      <div class="feature-item" v-for="characteristic in otherCharacteristics" :key="characteristic.label">
        <p>
          {{ characteristic.label }}: <strong>{{ characteristic.value }}</strong>
        </p>
      </div>
    </div>

    <a href="#" class="expand-link">
      Ver todas las características
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="chevron" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
      </svg>
    </a>
  </div>
</template>

<script setup lang="ts">
interface Characteristic {
  label: string;
  value: string;
  slider?: boolean;
  range?: {
    min: number;
    max: number;
    current: number;
  };
}

const props = defineProps<{
  characteristics: Array<Characteristic>;
}>();

const slideCharacteristics = props.characteristics.filter((c) => c.slider);
const otherCharacteristics = props.characteristics.filter((c) => !c.slider);

const calculateSliderWidth = (characteristic: Characteristic): number => {
  const range = characteristic.range;

  if (!range || range.max === range.min) {
    return 0;
  }
  
  const current = Math.max(range.min, Math.min(range.current, range.max));

  const percentage = ((current - range.min) / (range.max - range.min)) * 100;

  return percentage;
};
</script>

<style scoped>
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 850px;
  background-color: #fff;
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
.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 20px;
}
.feature-item p {
  margin: 0;
  font-size: 12px;
  color: #333;
}
.large-feature .text-container {
  width: 100%;
}
.large-feature .sub-text {
  font-size: 12px;
  color: #888;
  margin-top: 2px;
}
.slider {
  margin-top: 16px;
}
.slider-track {
  height: 4px;
  background-color: #f0f0f0;
  border-radius: 2px;
  width: 100%;
}
.slider-fill {
  height: 100%;
  background-color: #3483fa;
  border-radius: 2px;
  position: relative;
  transition: width 0.3s ease; 
}
.slider-fill::after {
  content: '';
  position: absolute;
  right: -4px;
  top: -2px;
  width: 8px;
  height: 8px;
  background-color: #3483fa;
  border-radius: 50%;
}
.slider-labels {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #888;
  margin-top: 8px;
}
.features-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px 32px;
  padding-top: 24px;
  margin-top: 24px;
}
.features-grid .feature-item {
  align-items: center;
}
.expand-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: #3483fa;
  font-size: 12px;
  margin-top: 24px;
  font-weight: 500;
}
</style>