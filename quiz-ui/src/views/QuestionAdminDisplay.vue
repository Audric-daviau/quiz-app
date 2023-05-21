<template>
    <div id="question-display">
      <h2>{{ question.title }}</h2>
      <p>{{ question.text }}</p>
      
      <ul>
        <li v-for="(answer, index) in question.possibleAnswers" :key="index">
          {{ answer.text }} 
          <span v-if="answer.isCorrect">✔️</span>
        </li>
      </ul>
      
      <button @click="editQuestion">Éditer</button>
      <button @click="deleteQuestion">Supprimer</button>
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
        // navigate to question editing page with question id
        this.$router.push({ name: 'QuestionEdition', params: { questionId: this.$route.params.questionId }});
      },
      async deleteQuestion() {
        try {
          await quizApiService.deleteQuestion(this.$route.params.questionId);
          this.$router.push({ name: 'questionList' });
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