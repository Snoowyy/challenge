<template>
  <div class="gallery-container">
    <div class="gallery-wrapper">
      <div class="thumbnails">
        <div 
          v-for="(image, index) in images" 
          :key="index" 
          class="thumbnail"
          :class="{ 'active': index === activeImageIndex }"
          @mouseover="activeImageIndex = index"
        >
          <img :src="image">
        </div>
      </div>
      <div class="main-image">
        <img :src="images[activeImageIndex]" >
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

defineProps({
  images: Array
});

const activeImageIndex = ref(0);
</script> 

<style scoped>
.gallery-container {
  display: flex;
  flex-direction: row;
  gap: 16px;
  width: 65%;
  position: relative;
}

.gallery-wrapper{
display: flex;
  position: sticky;
  top: 24px;
  height: fit-content;
}

.thumbnails {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.thumbnail {
  width: 48px;
  height: 48px;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.thumbnail.active {
  border: 2px solid #3483fa;
}

.thumbnail img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.main-image {
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-image img {
  max-width: 100%;
  max-height: 500px;
  object-fit: contain;
}

@media (max-width: 768px) {
  .gallery-container {
    width: fit-content;
  }
}
</style>