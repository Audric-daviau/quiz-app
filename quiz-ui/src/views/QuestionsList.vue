<template>
    <div id="questions">
      <h2>Questions</h2>
      <div v-for="question in questions" :key="question.id" @click="goToQuestionDetail(question.id)">
        {{ question.title }}
      </div>
      <button @click="createQuestion">Créer une question</button>
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