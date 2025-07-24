<template>
  <div class="qa-card">
    <h2 class="title">Preguntas</h2>

    <form @submit.prevent="submitQuestion" class="question-form">
      <input 
        type="text"
        v-model.trim="newQuestionText"
        placeholder="Escribe tu pregunta..."
        class="question-input"
        :disabled="isSubmitting"
      />
      <button type="submit" class="submit-button" :disabled="isSubmitting || !newQuestionText">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
          <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-4.718-2.984 11.886-6.958Z"/>
        </svg>
        {{ isSubmitting ? 'Enviando...' : 'Preguntar' }}
      </button>
    </form>
    
    <div class="questions-list" v-if="localQuestions.length > 0">
      <h3 class="subtitle">Últimas realizadas</h3>
      <div v-for="qa in localQuestions" :key="qa.id" class="qa-item">
        <p class="question-text">{{ qa.questionText }}</p>
        <div class="answer-block" v-if="qa.answerText">
          <p class="answer-text">{{ qa.answerText }}</p>
          <span class="answer-date">{{ qa.answerDate }}</span>
        </div>
      </div>
    </div>
    
    <div class="load-more-container" v-if="hasMoreQuestions">
       <button @click="loadMoreQuestions" class="load-more-button" :disabled="isLoadingMore">
         {{ isLoadingMore ? 'Cargando...' : 'Cargar más preguntas' }}
       </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

interface Question {
  id: number;
  questionText: string;
  answerText?: string;
  answerDate?: string;
}

const mockExtraQuestions = [
  {
    id: 101,
    questionText: '¿El equipo viene sellado en su caja original con todos sus accesorios?',
    answerText: '¡Hola! Sí, todos nuestros equipos son 100% nuevos y vienen sellados de fábrica con todos los accesorios originales. ¡Anímate a comprar!',
    answerDate: '19/07/2025'
  },
  {
    id: 102,
    questionText: '¿Es compatible con la red 5G de Claro en Colombia?',
    answerText: '¡Hola! Sí, este modelo es totalmente compatible con las redes 5G de todos los operadores en Colombia, incluyendo Claro.',
    answerDate: '18/07/2025'
  },
  {
    id: 103,
    questionText: '¿Tienen disponible el color "Titanium Blue"?',
    answerText: '¡Hola! Por el momento solo manejamos el color "Titanium Black" de la publicación. ¡Es un color increíble!',
    answerDate: '17/07/2025'
  },
];
const props = defineProps<{
  questions: Array<Question>;
  productId: string | number;
}>();

const newQuestionText = ref('');
const isSubmitting = ref(false);
const isLoadingMore = ref(false);
const hasMoreQuestions = ref(true);
const localQuestions = ref([...props.questions]);

watch(() => props.questions, (newVal) => {
  localQuestions.value = [...newVal];
}, { immediate: true, deep: true });

const submitQuestion = async () => {
  if (!newQuestionText.value || isSubmitting.value) return;
  isSubmitting.value = true;
  
  const payload = { questionText: newQuestionText.value };
  
  try {
    await new Promise(resolve => setTimeout(resolve, 1000));
    const savedQuestion: Question = {
      id: Date.now(),
      questionText: payload.questionText,
      answerText: '¡Gracias por tu pregunta! Te responderemos pronto.',
      answerDate: new Date().toLocaleDateString('es-CO')
    };
    
    localQuestions.value.unshift(savedQuestion);
    newQuestionText.value = '';

  } catch (error) {
    console.error("Error al enviar la pregunta:", error);
  } finally {
    isSubmitting.value = false;
  }
};
const loadMoreQuestions = async () => {
  if (isLoadingMore.value) return;
  isLoadingMore.value = true;

  await new Promise(resolve => setTimeout(resolve, 1500));

  const newQuestions = mockExtraQuestions.splice(0, 1); 
  
  if (newQuestions.length > 0) {
    localQuestions.value.push(...newQuestions);
  }

  if (mockExtraQuestions.length === 0) {
    hasMoreQuestions.value = false;
  }

  isLoadingMore.value = false;
};
</script>

<style scoped>
.qa-card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  max-width: 800px;
  background-color: #fff;
  padding: 24px;
  border-radius: 8px;
}
.title {
  font-size: 24px;
  font-weight: 500;
  color: #333;
  margin: 0 0 16px 0;
}
.question-form {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}
.question-input {
  flex-grow: 1;
  padding: 10px 16px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 16px;
}
.question-input:focus {
  outline: none;
  border-color: #3483fa;
}
.submit-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background-color: #3483fa;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
}
.submit-button:disabled {
  background-color: #a9c7f7;
  cursor: not-allowed;
}
.questions-list {
  border-top: 1px solid #eee;
  padding-top: 24px;
}
.subtitle {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 16px 0;
}
.qa-item {
  margin-bottom: 24px;
}
.question-text {
  font-size: 16px;
  color: #333;
  line-height: 1.5;
  margin: 0 0 16px 0;
}
.answer-block {
  border-left: 2px solid #e0e0e0;
  padding-left: 16px;
  margin-left: 8px;
}
.answer-text {
  font-size: 16px;
  color: #666;
  line-height: 1.5;
  margin: 0 0 8px 0;
}
.answer-date {
  font-size: 14px;
  color: #999;
}
.load-more-container {
  text-align: center;
  padding-top: 16px;
  border-top: 1px solid #eee;
}
.load-more-button {
  background: none;
  border: none;
  color: #3483fa;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  padding: 8px 16px;
}
.load-more-button:disabled {
  color: #a9c7f7;
  cursor: not-allowed;
}
@media (max-width: 768px) {
  .question-form {
    flex-direction: column;
  }
}
</style>