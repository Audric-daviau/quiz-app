<template>
  <div class="page">
    <div class="content" v-if="question && question.title">
      <h2>{{ question.title }}</h2>
      <p>{{ question.text }}</p>
      <img width="400" height="400" v-if="question.image" :src="question.image" />
      <ul class="pts" v-if="question.possibleAnswers">
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
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.content {
  text-align: center;
}

.question-details {
  text-align: left;
}

h2 {
  font-size: 2.5em;
}

.pts {
  display: flex;
  flex-wrap: wrap;
}

ul li {
  font-size: 1.2em;
  list-style: none;
  flex: 0 0 50%; /* Each item occupies 50% of the container width */
  padding: 10px;
}

ul li:before {
  content: '👒';
}
</style>
  