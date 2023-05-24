<template>
  <div class = "page">
    <div v-if="question && question.title">
      <h2>{{ question.title }}</h2>
      <p>{{ question.text }}</p>
      <img width="400" height="400" v-if="question.image" :src="question.image" />
      <ul v-if="question.possibleAnswers">
        <li v-for="(option, optionIndex) in question.possibleAnswers" :key="option.id" @click="$emit('answer-selected', optionIndex)">
          {{ option.text }}
        </li>
      </ul>
    </div>
    <div v-else>
      Loading question...
    </div>
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
.page { 
  background: url("../assets/quizDisplay.jpg") no-repeat center center fixed; 
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

img {
  display: block;
  max-width:230px;
  max-height:95px;
  width: auto;
  height: auto;
}
</style>
  