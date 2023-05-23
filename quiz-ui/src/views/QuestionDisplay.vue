<template>
    <div v-if="question && question.title">
      <h2>{{ question.title }}</h2>
      <p>{{ question.text }}</p>
      <img v-if="question.image" :src="question.image" />
      <ul v-if="question.possibleAnswers">
        <li v-for="option in question.possibleAnswers" :key="option.id" @click="selectOption(option)">
          {{ option.text }}
        </li>
      </ul>
      <a @click="selectOption(2)">La réponse D</a>
    </div>
    <div v-else>
      Loading question...
    </div>
</template>
  

  
<script>
  export default {
    name: 'QuestionDisplay',
    props: {
      question: {
        type: Object,
      }
    },
    emits: ['answer-selected'], // Déclaration de l'événement émis
    methods: {
      selectOption(option) {
        this.$emit('answer-selected', option);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Styles spécifiques au composant QuestionDisplay */
  </style>
  