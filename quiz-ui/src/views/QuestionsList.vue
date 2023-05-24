<template>
  <div id="questions" class="questions-container">
    <h2>Questions</h2>
    <div class="question-list">
      <div class="question-item" v-for="question in questions" :key="question.id" @click="goToQuestionDetail(question.id)">
        {{ question.title }}
      </div>
    </div>
    <button class="create-question-btn" @click="createQuestion">Créer une question</button>
  </div>
</template>
  
  <script>
  import quizApiService from "@/services/QuizApiService";

  export default {
    name: "QuestionList",
    data() {
      return {
        questions: [],
      };
    },
    methods: {
      async getQuestions() {
        try {
          const response = await quizApiService.getAllQuestions();
          this.questions = response.data;
        } catch (error) {
          console.error(error);
        }
      },
      createQuestion() {
        // Implement the logic for creating a question
        this.$router.push('/questionEdition');
      },
      goToQuestionDetail(id) {
        this.$router.push({ name: 'QuestionAdminDisplay', params: { questionId: id }});
      },
    },
    mounted() {
      this.getQuestions();
    },
  };
  </script>

<style scoped>
h2 {
  font-size: 2.5em;
}
.questions-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 2em;
}

.question-list {
  display: flex;
  flex-direction: column;
  gap: 1em;
}

.question-item {
  cursor: pointer;
}

.create-question-btn {
  margin-top: 1em;
}
</style>