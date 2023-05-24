<template>
  <div v-if="question" id="question-display" class="question-container">
    <h2>{{ question.title }}</h2>
    <p>{{ question.text }}</p>
    
    <ul class="answers-list">
      <li v-for="(answer, index) in question.possibleAnswers" :key="index" class="answer-item">
        {{ answer.text }} 
        <span v-if="answer.isCorrect">✔️</span>
      </li>
    </ul>
    
    <div class="buttons">
      <button @click="editQuestion">Éditer</button>
      <button @click="deleteQuestion">Supprimer</button>
    </div>
  </div>
</template>
  
  <script>
  import quizApiService from "@/services/QuizApiService";
  
  export default {
    data() {
      return {
        question: null,
      };
    },
    methods: {
      async getQuestion() {
        const questionId = this.$route.params.questionId;
        try {
          const response = await quizApiService.getQuestionById(questionId);
          this.question = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      editQuestion() {
        this.$router.push({ name: 'QuestionEdition', params: { questionId: this.$route.params.questionId }});
      },
      async deleteQuestion() {
        try {
          await quizApiService.deleteQuestionById(this.$route.params.questionId);
          this.$router.push('/questionsList');
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.getQuestion();
    },
  };
  </script>
  <style scoped>
  h2 {
    font-size: 2em;
  }
  .question-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    gap: 20px;
    height: 100vh;
  }
  
  .answers-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .buttons {
    display: flex;
    justify-content: end;
    width: 50%;
  }
  </style>